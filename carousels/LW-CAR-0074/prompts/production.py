"""Batch I: record actual generation calls and required PNG/logo compositing.

No OCR, visual QA, review calls, or automatic regeneration.
"""
import json
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
MANIFEST = ROOT / 'manifest.json'


def now():
    return datetime.now(timezone.utc).isoformat()


def write(data):
    MANIFEST.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')


action = sys.argv[1]
if action == 'init':
    if MANIFEST.exists() or list((ROOT / 'outputs').glob('*.png')):
        raise RuntimeError('Reconcile existing attempts before initializing')
    copy = json.loads((ROOT / 'copy.json').read_text())
    (ROOT / 'outputs').mkdir(exist_ok=True)
    (ROOT / 'production-assets').mkdir(exist_ok=True)
    with Image.open(REPO / 'carousels/LW-CAR-0022/outputs/slide-19.png') as original:
        original.convert('RGBA').crop((0, 720, 1080, 1350)).save(ROOT / 'production-assets/approved-phone-hand.png')
    common = 'Create ONE complete 1080 x 1350 portrait Harda S2 carousel slide. Attached approved slide is a VISUAL template ONLY, never the text source. EXACT text below comes solely from frozen copy.json; preserve all lowercase, curly quotes/apostrophes, hyphens and punctuation. S2 style: very heavy tight lowercase grotesk headline #2A2A2A; solid coral #F26445 MARKER BARS behind the LOWER part of the specified words only. Clean regular sans body #2A2A2A; small subtitle italic regular #6B6B6B. Solid opaque CLEAN #F0F1EB background, no texture, arch, rings, dots, grid, panels, gradients, counter, watermark or signatures. Leave entire TOP 110px empty background: NO generated logo, name or icon. The ORIGINAL Harda PNG is composited later at x48,y19,218x71 using its own transparency without backing patch. S2 FIGURE: realistic WHITE/LIGHT-GREY bald faceless anatomical mannequin, fine grey shading and muscle fibres, smooth featureless pelvis covered by opaque loose CHARCOAL #2A2A2A gym shorts. Never beige/sand S1, cartoon or clay. Equipment black/grey, props plain/unbranded. No readable labels on equipment, no invented UI. NO COLOURED MUSCLES on any figure in this carousel; ignore reference highlights. Keep friendly humour, nobody mocked. Only exact provided text; no inherited fix:, do:, stars, tier letters, badges or speech-bubble words. Every word fully visible inside slide, no overlap.\n'
    scenes = ['COVER: match attached LW-CAR-0022/01 centered huge two-line headline, coral marker behind second headline line only, centered italic subtitle, and lower large figure proportions. Replace all old text. TWO white S2 figures from thighs up, front view, giving each other a fist bump; towel over one shoulder. No highlights.', 'ITEM: exact attached LW-CAR-0029/02 layout: heavy black #N BEFORE heavy lowercase headline; coral marker behind HEADLINE ONLY, not number. Body regular dark below. No fix:/do: extra line, no stars. Long headline may wrap with marker under each line, never shorten. Lower ~55% large figure/figures with required equipment: one figure shouting encouragement with both fists up, next to a second figure doing a flat barbell bench press, side three-quarter view. All figures WHITE S2, charcoal opaque shorts, no coloured muscles. Only props and gestures specified.', 'ITEM: exact attached LW-CAR-0029/02 layout: heavy black #N BEFORE heavy lowercase headline; coral marker behind HEADLINE ONLY, not number. Body regular dark below. No fix:/do: extra line, no stars. Long headline may wrap with marker under each line, never shorten. Lower ~55% large figure/figures with required equipment: standing alone next to a squat rack, looking down at a phone held in one hand (screen not visible), disappointed posture, front view. All figures WHITE S2, charcoal opaque shorts, no coloured muscles. Only props and gestures specified.', 'ITEM: exact attached LW-CAR-0029/02 layout: heavy black #N BEFORE heavy lowercase headline; coral marker behind HEADLINE ONLY, not number. Body regular dark below. No fix:/do: extra line, no stars. Long headline may wrap with marker under each line, never shorten. Lower ~55% large figure/figures with required equipment: one figure pointing and explaining to a second figure doing a goblet squat, front view. All figures WHITE S2, charcoal opaque shorts, no coloured muscles. Only props and gestures specified.', 'ITEM: exact attached LW-CAR-0029/02 layout: heavy black #N BEFORE heavy lowercase headline; coral marker behind HEADLINE ONLY, not number. Body regular dark below. No fix:/do: extra line, no stars. Long headline may wrap with marker under each line, never shorten. Lower ~55% large figure/figures with required equipment: two figures sitting on a flat bench chatting, a pair of dumbbells untouched on the floor, front view. All figures WHITE S2, charcoal opaque shorts, no coloured muscles. Only props and gestures specified.', 'ITEM: exact attached LW-CAR-0029/02 layout: heavy black #N BEFORE heavy lowercase headline; coral marker behind HEADLINE ONLY, not number. Body regular dark below. No fix:/do: extra line, no stars. Long headline may wrap with marker under each line, never shorten. Lower ~55% large figure/figures with required equipment: two figures at two side-by-side squat racks, one sliding an extra plate onto the bar while glancing at the other, front view. All figures WHITE S2, charcoal opaque shorts, no coloured muscles. Only props and gestures specified.', 'ITEM: exact attached LW-CAR-0029/02 layout: heavy black #N BEFORE heavy lowercase headline; coral marker behind HEADLINE ONLY, not number. Body regular dark below. No fix:/do: extra line, no stars. Long headline may wrap with marker under each line, never shorten. Lower ~55% large figure/figures with required equipment: two figures training side by side, both wearing plain black over-ear headphones, focused, one doing a dumbbell row and one a dumbbell curl, front view. All figures WHITE S2, charcoal opaque shorts, no coloured muscles. Only props and gestures specified.', 'ITEM: exact attached LW-CAR-0029/02 layout: heavy black #N BEFORE heavy lowercase headline; coral marker behind HEADLINE ONLY, not number. Body regular dark below. No fix:/do: extra line, no stars. Long headline may wrap with marker under each line, never shorten. Lower ~55% large figure/figures with required equipment: one figure calmly spotting a second figure doing a flat barbell bench press, side three-quarter view. All figures WHITE S2, charcoal opaque shorts, no coloured muscles. Only props and gestures specified.', 'PRODUCT ENDING: attached LW-CAR-0022/19 typography/layout only. Generate ONLY headline and body on plain background. Left-aligned large heavy lowercase headline; coral markers only under every set you lift and your buddy cancels, wrapping if needed. Regular dark exact body under headline, may wrap into two lines. All text comfortably above y850, completely visible. Everything below final body line plain empty background. NO phone, hand, screen, app UI, chart, icons, placeholder or lower objects. Original approved white-hand/phone with REAL Muscle balance UI bitmap will be inserted without resampling below measured final body-text row, at least 40px clear gap, never fixed height.']
    entries = []
    for slide, scene in zip(copy['slides'], scenes):
        n = slide['n']
        ref = "carousels/LW-CAR-0022/outputs/slide-01.png" if n == 1 else "carousels/LW-CAR-0022/outputs/slide-19.png" if n == 9 else "carousels/LW-CAR-0029/outputs/slide-02.png"
        layout = ""
        prompt = common + '\n' + layout + scene + '\n\nEXACT TEXT AND STYLES, authoritative copy.json:\n' + '\n'.join(json.dumps(t, ensure_ascii=False) for t in slide['text']) + '\nReturn one opaque slide, never a contact sheet.\n'
        pf = f'prompts/slide-{n:02d}.txt'
        (ROOT / pf).write_text(prompt)
        entries.append(dict(slide=n, role=slide['role'], exact_text=[t['string'] for t in slide['text']], prompt_file=pf, references=[ref], file=f'outputs/slide-{n:02d}.png', attempts=[], errors=[], save_status='not_started', agent_visual_review='not_performed', user_review='pending'))
    write(dict(carousel_id=copy['carousel_id'], batch='BATCH-I', content_version=copy['content_version'], source_commit=subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', 'HEAD'], text=True).strip(), status='in_progress', carousel_complete=False, design_style='S2', background='CLEAN', brand='Harda', generated_images=0, next_slide_to_generate=1, agent_visual_review='not_performed', user_review='pending', remote_save=dict(remote='origin', branch='claude/charming-einstein-xgejky', status='not_yet_pushed'), slides=entries))
    (ROOT / 'caption.txt').write_text(copy['caption']['text'] + '\n')
    print('Initialized LW-CAR-0074: 9 exact-copy prompts and manifest')
    sys.exit()

m = json.loads(MANIFEST.read_text())
if action in ('start', 'save', 'error'):
    n = int(sys.argv[2])
    slide = m['slides'][n - 1]
    if action == 'start':
        if slide['attempts'] or slide['save_status'] != 'not_started':
            raise RuntimeError('Do not repeat or overwrite an existing generation attempt')
        slide['attempts'].append(dict(attempt=1, tool='image_gen.imagegen', status='in_progress', started_at=now(), prompt_file=slide['prompt_file'], referenced_image_paths=slide['references'], transparent_background=False))
        slide['save_status'] = 'generation_in_progress'
    elif action == 'error':
        message = sys.argv[3]
        slide['errors'].append(message)
        slide['attempts'][-1].update(status='error', finished_at=now(), error=message)
        slide['save_status'] = 'generation_failed'
        m['status'] = 'incomplete_generation_failed'
        m['next_action'] = f'Stop Batch I per BATCH-I.md; resume this carousel at slide {n} after the recorded generation blocker is resolved. Do not start LW-CAR-0075.'
    else:
        raw_path = Path(sys.argv[3])
        asset = ROOT / f'production-assets/slide-{n:02d}-generated.png'
        shutil.copyfile(raw_path, asset)
        with Image.open(raw_path) as raw:
            im = Image.new('RGBA', raw.size, '#F0F1EB')
            im.alpha_composite(raw.convert('RGBA'))
            im = im.resize((1080, 1350), Image.Resampling.LANCZOS)
        if slide['role'] == 'product ending':
            # Required layout measurement only; no OCR or visual review.
            bounds = im.convert('L').point(lambda p: 255 if p < 180 else 0).crop((0, 110, 1080, 1350)).getbbox()
            if bounds is None:
                raise RuntimeError('No text extent available for required phone placement')
            bottom = 110 + bounds[3]
            phone_y = bottom + 50
            foreground = ROOT / 'production-assets/approved-phone-hand.png'
            with Image.open(foreground) as phone:
                crop = phone.crop(phone.getbbox())
                im.alpha_composite(crop, (phone.getbbox()[0], phone_y))
            slide['phone_compositing'] = dict(source=str(foreground.relative_to(REPO)), text_bottom=bottom, phone_top=phone_y, gap_px=50, scale='1:1 original pixels', ui_generated=False)
        with Image.open(REPO / 'assets/logo/harda-logo-full.png') as logo:
            im.alpha_composite(logo.convert('RGBA').resize((218, 71), Image.Resampling.LANCZOS), (48, 19))
        im.convert('RGB').save(ROOT / slide['file'])
        slide['attempts'][-1].update(status='succeeded', finished_at=now(), raw_result_file=str(raw_path), preserved_raw_file=str(asset.relative_to(ROOT)), result_file=slide['file'])
        slide['save_status'] = 'saved_in_cloud_checkout'
    m['generated_images'] = sum(s['save_status'] == 'saved_in_cloud_checkout' for s in m['slides'])
    m['next_slide_to_generate'] = next((s['slide'] for s in m['slides'] if s['save_status'] != 'saved_in_cloud_checkout'), None)
    write(m)
    print(f'{action}: LW-CAR-0074 slide {n}; {m["generated_images"]}/9 saved')
elif action == 'package':
    complete = m['generated_images'] == len(m['slides'])
    m['carousel_complete'] = complete
    if complete:
        m.update(status='complete_pending_owner_review', next_action='Commit and push this carousel, then continue LW-CAR-0075 without review pause.')
    m['archive'] = 'LW-CAR-0074' + ('' if complete else '-incomplete') + '-1080x1350.zip'
    m['remote_save'].update(status='prepared_for_commit_and_push', commit_lookup='git log -1 -- carousels/LW-CAR-0074/manifest.json')
    write(m)
    with zipfile.ZipFile(ROOT / m['archive'], 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in [*sorted((ROOT / 'outputs').glob('slide-*.png')), ROOT / 'caption.txt', MANIFEST]:
            archive.write(path, path.relative_to(ROOT))
    print(f'Packaged {m["generated_images"]}/9 images; {m["status"]}')
else:
    raise RuntimeError(f'Unknown action {action}')
