"""Checkpoint one image_gen call; insert original Harda PNG; flatten export.

No text rendering, visual QA, OCR or retries. Run start/save/error from cloud.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image

carousel = Path(__file__).resolve().parents[1]
checkout = carousel.parents[1]
path = carousel / 'manifest.json'
manifest = json.loads(path.read_text())
action, number = sys.argv[1:3]
entry = next(s for s in manifest['slides'] if s['slide'] == int(number))
now = datetime.now(timezone.utc).isoformat()
if action == 'start':
    if int(number) not in manifest['authorized_slides'] or entry['attempts']:
        raise RuntimeError('Outside authorized batch or attempt already recorded')
    entry['save_status'] = 'generation_in_progress'
    entry['attempts'].append(dict(attempt=1, tool='image_gen.imagegen',
        status='in_progress', started_at=now, prompt_file=entry['prompt_file'],
        transparent_background=False,
        referenced_image_paths=[str(checkout / r) for r in entry['references']]))
elif action == 'save':
    raw_path = Path(sys.argv[3])
    with Image.open(raw_path) as raw:
        raw_format = dict(size=list(raw.size), mode=raw.mode)
        canvas = Image.new('RGBA', raw.size, '#F0F1EB')
        canvas.alpha_composite(raw.convert('RGBA'))
        canvas = canvas.resize((1080, 1350), Image.Resampling.LANCZOS)
    if int(number) == 12:
        import shutil
        shutil.copyfile(raw_path, carousel / 'production-assets/slide-12-generated-text.png')
        with Image.open(carousel / 'production-assets/approved-phone-hand-strip.png') as strip:
            canvas.paste(strip.convert('RGBA'), (0, 720))
        entry['source_ui'] = dict(source='carousels/LW-CAR-0022/outputs/slide-19.png',
            source_commit=manifest['continuation_source_commit'],
            strip='production-assets/approved-phone-hand-strip.png',
            source_crop=[0,720,1080,1350], placement=[0,720],
            scale='1:1, no resampling', ui_generated_or_retyped=False)
    with Image.open(checkout / manifest['logo']['file']) as original:
        logo = original.convert('RGBA').resize((218, 71), Image.Resampling.LANCZOS)
        canvas.alpha_composite(logo, (48, 19))
    output = carousel / entry['file']
    canvas.convert('RGB').save(output, format='PNG')
    with Image.open(output) as saved:
        if saved.size != (1080, 1350) or saved.mode != 'RGB':
            raise RuntimeError('Expected opaque 1080x1350 RGB PNG')
    entry['save_status'] = 'saved_to_repository_checkout'
    entry['attempts'][-1].update(status='succeeded', finished_at=now,
        raw_result_file=str(raw_path), raw_result_format=raw_format,
        result_file=entry['file'], export=dict(size=[1080,1350], mode='RGB',
            has_alpha=False, logo='original Harda PNG, x48 y19 218x71, own alpha, no backing patch'))
    manifest['generated_images'] = sum(s['save_status'] == 'saved_to_repository_checkout' for s in manifest['slides'])
    manifest['pending_review_slides'] = [s['slide'] for s in manifest['slides'] if s['save_status'] == 'saved_to_repository_checkout' and s['user_review'] != 'approved']
    manifest['next_slide_to_generate'] = next((s['slide'] for s in manifest['slides'] if s['save_status'] == 'not_started'), None)
elif action == 'error':
    error = sys.argv[3]
    entry['save_status'] = 'generation_interrupted_no_result'
    entry['attempts'][-1].update(status='error', finished_at=now, error=error)
    entry['errors'].append(error)
    manifest['status'] = 'incomplete_generation_interrupted'
    manifest['next_slide_to_generate'] = int(number)
    manifest['next_action'] = 'Stop on error; push existing outputs immediately. Owner authorization required before another attempt.'
else:
    raise ValueError('Use start, save or error')
path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(dict(slide=int(number), action=action, save_status=entry['save_status'])))
