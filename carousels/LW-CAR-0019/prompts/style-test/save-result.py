"""Export a returned image, insert the original logo, and checkpoint the manifest.

This performs the requested file export only, not visual QA or regeneration.
Usage: python3 prompts/style-test/save-result.py A-slide-01 /absolute/raw/image.png
Run from carousels/LW-CAR-0019.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

carousel = Path(__file__).resolve().parents[2]
checkout = carousel.parents[1]
identifier, raw_path = sys.argv[1:]
variant, _, number = identifier.split('-')
manifest_path = carousel / 'manifest.json'
manifest = json.loads(manifest_path.read_text())
entry = next(s for s in manifest['slides'] if s['variant'] == variant and s['slide'] == int(number))

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

# Required export-format check only: do not inspect content, OCR, or anatomy.
with Image.open(output) as saved:
    if saved.size != (1080, 1350) or saved.mode != 'RGB':
        raise RuntimeError('Export must be 1080 x 1350 RGB without alpha')

entry['save_status'] = 'saved_to_repository_checkout'
entry['attempts'][-1].update({
    'status': 'succeeded',
    'finished_at': datetime.now(timezone.utc).isoformat(),
    'raw_result_file': str(raw_path),
    'raw_result_format': raw_metadata,
    'result_file': entry['file'],
    'export': {'size': [1080, 1350], 'mode': 'RGB', 'has_alpha': False,
               'logo': 'original_file_composited_at_48_19_341_71_without_backing_patch'},
})
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'id': identifier, 'file': str(output), 'mode': 'RGB', 'size': [1080, 1350]}))
