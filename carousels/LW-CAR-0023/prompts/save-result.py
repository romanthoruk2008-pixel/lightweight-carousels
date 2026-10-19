"""Checkpoint one generation; insert the original Harda logo and export RGB.

Run from carousels/LW-CAR-0023:
  python3 prompts/save-result.py start 1
  python3 prompts/save-result.py save 1 /absolute/returned/image.png

No text rendering, visual QA, OCR, or automatic retries are performed.
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
    if int(number) not in manifest.get('authorized_slides', [1, 2, 3]) or entry['attempts']:
        raise RuntimeError('Slide outside current owner authorization or an attempt already exists')
    entry['save_status'] = 'generation_in_progress'
    entry['attempts'].append({'attempt': 1, 'tool': 'image_gen.imagegen',
        'started_at': now, 'status': 'in_progress', 'transparent_background': False,
        'referenced_image_paths': [str(checkout / r) for r in entry['references']]})
elif action == 'save':
    raw_path = Path(sys.argv[3])
    with Image.open(raw_path) as raw:
        raw_format = {'size': list(raw.size), 'mode': raw.mode}
        canvas = Image.new('RGBA', raw.size, '#F0F1EB')
        canvas.alpha_composite(raw.convert('RGBA'))
        canvas = canvas.resize((1080, 1350), Image.Resampling.LANCZOS)
    if int(number) == 19:
        # Preserve the approved real app UI and white hand bitmap at 1:1 scale.
        import shutil
        shutil.copyfile(raw_path, carousel / 'production-assets/slide-19-generated-text.png')
        with Image.open(carousel / 'production-assets/approved-phone-hand-strip.png') as strip:
            canvas.paste(strip.convert('RGBA'), (0, 740))
        entry['source_ui'] = {
            'source': 'carousels/LW-CAR-0021/outputs/slide-19.png',
            'strip': 'production-assets/approved-phone-hand-strip.png',
            'source_crop': [0, 740, 1080, 1350], 'placement': [0, 740],
            'scale': '1:1, no resampling', 'ui_generated_or_retyped': False,
        }
    with Image.open(checkout / manifest['logo']['file']) as logo_source:
        logo = logo_source.convert('RGBA').resize((218, 71), Image.Resampling.LANCZOS)
        canvas.alpha_composite(logo, (48, 19))
    output = carousel / entry['file']
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert('RGB').save(output, format='PNG')
    # Required export-format check only; no image content evaluation.
    with Image.open(output) as saved:
        if saved.size != (1080, 1350) or saved.mode != 'RGB':
            raise RuntimeError('Expected 1080 x 1350 RGB PNG without alpha')
    entry['save_status'] = 'saved_to_repository_checkout'
    entry['attempts'][-1].update({'status': 'succeeded', 'finished_at': now,
        'raw_result_file': str(raw_path), 'raw_result_format': raw_format,
        'result_file': entry['file'], 'export': {'size': [1080, 1350],
        'mode': 'RGB', 'has_alpha': False,
        'logo': 'original harda-logo-full.png, x48,y19,218x71, own alpha, no backing patch'}})
    manifest['generated_images'] = sum(s['save_status'] == 'saved_to_repository_checkout'
                                        for s in manifest['slides'])
else:
    raise ValueError('Use start or save')
path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'slide': int(number), 'action': action,
                  'save_status': entry['save_status'], 'file': entry['file']}))
