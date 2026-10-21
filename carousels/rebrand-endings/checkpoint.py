"""Record one requested image edit and preserve original pixels outside brand word.

No visual QA, OCR, text rendering or retries. Called from the cloud checkout.
"""
import json
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image

batch_root = Path(__file__).resolve().parent
checkout = batch_root.parents[1]
log_path = batch_root / 'manifest.json'
batch = json.loads(log_path.read_text())
action, cid = sys.argv[1:3]
job = next(j for j in batch['slides'] if j['carousel_id'] == cid)
root = checkout / 'carousels' / cid
mp = root / 'manifest.json'
manifest = json.loads(mp.read_text())
entry = next(s for s in manifest['slides'] if s.get('slide_number', s.get('slide')) == job['slide'])
now = datetime.now(timezone.utc).isoformat()
if action == 'start':
    if job['attempts']:
        raise RuntimeError('No automatic additional attempts authorized')
    attempt = dict(attempt=1, tool='image_gen.imagegen', status='in_progress',
        started_at=now, prompt_file=job['prompt_file'],
        referenced_image_paths=[str(checkout / job['file'])], transparent_background=False)
    job['attempts'].append(attempt)
    job['status'] = 'in_progress'
elif action == 'save':
    raw_path = Path(sys.argv[3])
    with Image.open(job['original_cloud_file']) as source:
        canvas = source.convert('RGBA')
    with Image.open(raw_path) as generated:
        raw_format = dict(size=list(generated.size), mode=generated.mode)
        edited = Image.new('RGBA', generated.size, '#F0F1EB')
        edited.alpha_composite(generated.convert('RGBA'))
        edited = edited.resize((1080, 1350), Image.Resampling.LANCZOS)
        box = tuple(job['brand_word_rectangle'])
        canvas.paste(edited.crop(box), box[:2])
    with Image.open(checkout / 'assets/logo/harda-logo-full.png') as logo:
        canvas.alpha_composite(logo.convert('RGBA').resize((218,71), Image.Resampling.LANCZOS), (48,19))
    output = checkout / job['file']
    canvas.convert('RGB').save(output, format='PNG')
    with Image.open(output) as saved:
        if saved.size != (1080,1350) or saved.mode != 'RGB':
            raise RuntimeError('Expected opaque 1080x1350 RGB export')
    job['attempts'][-1].update(status='succeeded', finished_at=now,
        raw_result_file=str(raw_path), raw_result_format=raw_format,
        result_file=job['file'], export=dict(size=[1080,1350], mode='RGB', alpha=False))
    job['status'] = 'saved'
    job['user_review'] = 'pending'
    entry['content_version'] = job['content_version']
    entry['user_review'] = 'pending'
    entry['agent_visual_review'] = 'not_performed'
    entry['save_status'] = 'saved_to_repository_checkout'
    if 'status' in entry:
        entry['status'] = 'rebrand_edit_saved_pending_owner_review'
    if 'exact_text' in entry:
        entry['exact_text'] = job['exact_slide_text']
    history_key = 'attempt_history' if 'attempt_history' in entry else 'attempts'
    attempt = dict(job['attempts'][-1])
    attempt.update(operation='owner_requested_Harda_brand_word_edit',
        attempt=len(entry.get(history_key, [])) + 1, user_review='pending',
        source_commit=batch['source_commit'])
    entry.setdefault(history_key, []).append(attempt)
    if 'attempt_count' in entry:
        entry['attempt_count'] = len(entry[history_key])
    entry['harda_rebrand_edit'] = dict(prompt_file=job['prompt_file'],
        source_commit=batch['source_commit'], input_file=job['file'],
        brand_word_rectangle=job['brand_word_rectangle'], replacement_word=job['replacement_word'],
        exact_text=job['new_text'], method='image_gen edits original slide; only brand-word rectangle copied back onto original; original logo composited again',
        other_pixels='original input pixels retained outside brand rectangle and required logo placement; phone, real UI and hand never resampled or regenerated',
        user_review='pending', agent_visual_review='not_performed')
    manifest['harda_rebrand_endings'] = dict(slide=job['slide'],
        content_version=job['content_version'], source_commit=batch['source_commit'],
        status='edited_ending_pending_owner_review', other_slides='unchanged; prior owner approvals remain in force')
    # Carousel-wide acceptance history is preserved; only the edited slide is pending.
    for key in ['approved_slides', 'slides_approved']:
        if isinstance(manifest.get(key), list):
            manifest[key] = [n for n in manifest[key] if n != job['slide']]
    for key in ['pending_review_slides', 'slides_pending_review']:
        if isinstance(manifest.get(key), list):
            manifest[key] = sorted(set(manifest[key] + [job['slide']]))
    mp.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
elif action == 'error':
    error = sys.argv[3]
    job['attempts'][-1].update(status='error', error=error, finished_at=now)
    job['status'] = 'interrupted_no_result'
    batch['status'] = 'incomplete_interrupted'
else:
    raise ValueError('Use start/save/error')
batch['saved_slides'] = [j['carousel_id'] for j in batch['slides'] if j['status'] == 'saved']
batch['remaining_slides'] = [j['carousel_id'] for j in batch['slides'] if j['status'] != 'saved']
if not batch['remaining_slides']:
    batch['status'] = 'all_11_edits_saved_pending_owner_review'
log_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2) + '\n')
if action == 'save':
    archive = next(root.glob('*.zip'))
    tmp = archive.with_suffix('.tmp')
    with zipfile.ZipFile(archive) as src:
        names = src.namelist()
        manifest_name = next((n for n in names if n.endswith('manifest.json')), 'manifest.json')
        prefix = manifest_name.removesuffix('manifest.json')
        filename = Path(job['file']).name
        slide_name = next((n for n in [prefix+'outputs/'+filename, prefix+filename] if n in names), prefix+'outputs/'+filename)
        replacements = {manifest_name: mp.read_bytes(), slide_name: (checkout/job['file']).read_bytes(),
            prefix+'copy.json': (root/'copy.json').read_bytes(),
            prefix+job['prompt_file']: (root/job['prompt_file']).read_bytes()}
        with zipfile.ZipFile(tmp, 'w') as dst:
            for info in src.infolist():
                dst.writestr(info, replacements.pop(info.filename) if info.filename in replacements else src.read(info.filename))
            for name, payload in replacements.items():
                dst.writestr(name, payload, compress_type=zipfile.ZIP_DEFLATED)
    tmp.replace(archive)
print(json.dumps(dict(carousel_id=cid, action=action, status=job['status'], completed=len(batch['saved_slides']))))
