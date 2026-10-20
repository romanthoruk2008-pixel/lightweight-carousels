"""Package actual saved outputs for a complete or interrupted cloud checkpoint."""
import json
import zipfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
p = root / 'manifest.json'
m = json.loads(p.read_text())
saved = [s['slide'] for s in m['slides'] if s['save_status'] == 'saved_to_repository_checkout']
complete = len(saved) == 12
m['generated_images'] = len(saved)
m['carousel_complete'] = complete
m['pending_review_slides'] = [n for n in saved if n not in m['approved_slides']]
if complete:
    m['status'] = 'generated_12_of_12_awaiting_owner_review_of_slides_4_12'
    m['next_slide_to_generate'] = None
    m['next_action'] = 'Owner reviews new slides 4-12; slides 1-3 approved and unchanged. No automatic corrections.'
    m['archive'] = 'LW-CAR-0024-1080x1350.zip'
else:
    m['status'] = 'incomplete_generation_interrupted'
    m['archive'] = 'LW-CAR-0024-incomplete-1080x1350.zip'
m['remote_save'].update(status='pushed_to_target_branch',
    commit_lookup='git log -1 -- carousels/LW-CAR-0024/manifest.json')
p.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n')
(root / 'handoff.md').write_text(f'''# LW-CAR-0024 v1.0 — {'complete' if complete else 'interrupted'}

Saved {len(saved)} of 12 ordered opaque 1080 × 1350 RGB PNGs. Exact text from copy.json v1.0. Original Harda PNG composited at x48 y19, 218×71 with its own transparency, no backing patch. Caption is verbatim.

Owner approved initial slides 1–3 from 6d83188204e06e7c3a4cedf79fab334ee2e195dc and authorized the remaining slides. Accepted PNGs remain unchanged. New saved slides 4–12 remain user_review=pending. Prompts, actual generation calls, returned paths and any errors are in manifest.json. No automatic retries or corrections.

Slide 12, if saved, reuses the original phone, real Muscle balance UI and white hand bitmap from approved LW-CAR-0022 slide 19, crop [0,720,1080,1350] pasted at [0,720] at 1:1 scale. UI not generated, retyped, redrawn or rescaled.

agent_visual_review=not_performed. Only export-format metadata checked; no visual QA, OCR, anatomy audits or reviewer calls.

Status: {m['status']}.
Next action: {m['next_action']}
Next slide to generate: {m['next_slide_to_generate']}.
''')
with zipfile.ZipFile(root / m['archive'], 'w', compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file() and p.suffix != '.zip' and '__pycache__' not in p.parts:
            z.write(p, p.relative_to(root))
old = root / 'LW-CAR-0024-initial-slides-01-03-1080x1350.zip'
if old.exists():
    old.unlink()
print(json.dumps(dict(saved_slides=saved, complete=complete, archive=m['archive'])))
