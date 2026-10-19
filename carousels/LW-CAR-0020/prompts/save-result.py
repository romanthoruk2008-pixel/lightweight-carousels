"""Checkpoint an image_gen attempt; export RGB and paste the original logo.

Run from carousels/LW-CAR-0020:
  python3 prompts/save-result.py start 1
  python3 prompts/save-result.py save 1 /absolute/returned/image.png

No text rendering, visual QA, OCR, or automatic regeneration is performed.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

carousel = Path(__file__).resolve().parents[1]
checkout = carousel.parents[1]
manifest_path = carousel / 'manifest.json'
manifest = json.loads(manifest_path.read_text())
action, number = sys.argv[1:3]
entry = next(s for s in manifest['slides'] if s['slide'] == int(number))
now = datetime.now(timezone.utc).isoformat()

if action == 'start':
    if int(number) not in [1, 2, 3]:
        raise RuntimeError('Only the initial three slides are authorized before owner approval')
    if entry['attempts']:
        raise RuntimeError('Existing attempt: reconcile instead of automatically retrying')
    entry['save_status'] = 'generation_in_progress'
    entry['attempts'].append({
        'attempt': 1, 'tool': 'image_gen.imagegen', 'started_at': now,
        'status': 'in_progress', 'transparent_background': False,
        'referenced_image_paths': [str(checkout / entry['reference'])],
    })
elif action == 'save':
    raw_path = Path(sys.argv[3])
    with Image.open(raw_path) as raw:
        raw_metadata = {'size': list(raw.size), 'mode': raw.mode}
        canvas = Image.new('RGBA', raw.size, '#F0F1EB')
        canvas.alpha_composite(raw.convert('RGBA'))
        canvas = canvas.resize((1080, 1350), Image.Resampling.LANCZOS)
    with Image.open(checkout / 'assets/logo/lightweight-logo-full.png') as original_logo:
        logo = original_logo.convert('RGBA').resize((341, 71), Image.Resampling.LANCZOS)
        canvas.alpha_composite(logo, (48, 19))
    output = carousel / entry['file']
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert('RGB').save(output, format='PNG')
    # Only the expressly required export-format check, not content evaluation.
    with Image.open(output) as saved:
        if saved.size != (1080, 1350) or saved.mode != 'RGB':
            raise RuntimeError('Export must be 1080 x 1350 RGB without alpha')
    entry['save_status'] = 'saved_to_repository_checkout'
    entry['attempts'][-1].update({
        'status': 'succeeded', 'finished_at': now,
        'raw_result_file': str(raw_path), 'raw_result_format': raw_metadata,
        'result_file': entry['file'],
        'export': {'size': [1080, 1350], 'mode': 'RGB', 'has_alpha': False,
                   'logo': 'original_file_composited_at_48_19_341_71_without_backing_patch'},
    })
    manifest['generated_images'] = sum(
        s['save_status'] == 'saved_to_repository_checkout' for s in manifest['slides']
    )
else:
    raise ValueError('Use start or save')

manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'slide': int(number), 'action': action,
                  'save_status': entry['save_status'], 'file': entry['file']}))
