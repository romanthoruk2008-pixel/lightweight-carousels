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
    common = '''Create ONE complete 1080 x 1350 portrait Harda fitness carousel slide. The attached approved slide is a VISUAL template only, never the source of words. Exact text below comes only from frozen copy.json. Preserve every capital, hyphen, apostrophe and punctuation. Rubik type: heaviest cover, bold title, regular labels/body. Dark #2A2A2A, body #6B6B6B, accent #F26445. BACKGROUND: entire canvas solid opaque #F0F1EB, then thin #E1E2DA GRID lines 2px every 54px. Absolutely NO ARCH, rings, dots, gradient, progress bar, counter, transparency checkerboard, watermark or signature. Leave the top 110px empty except the grid: do NOT draw a logo, brand name or icon there. The ORIGINAL Harda PNG is composited later at x48,y19,218x71 using its own alpha. S1 FIGURES ONLY: bald faceless smooth plastic anatomy teaching mannequin with warm-sand #D9CBBE muscles, darker sand shading, ivory #F5F0E5 tendons, fine grey linework, smooth featureless pelvis covered by opaque plain sand short shorts on full-body figures. Never white S2 figures, green, sage, real human nudity, invented equipment or extra copy. Equipment black/grey. Every word fully visible inside slide edges, no overlap.\n'''
    scenes = [
        'COVER twin of the attached LW-CAR-0005/01: huge three stacked lines in the upper ~55%: BEST EXERCISES coral; FOR EVERY dark; MUSCLE GROUP dark. Small bold italic (Pull Day Edition) centered underneath. Lower portion: S1 anatomical man SEATED at black/grey LAT PULLDOWN machine, REAR VIEW, gripping wide bar pulled to upper chest. Both lats coral. Preserve approved cover headline hierarchy and figure scale. Replace the reference push machine and figure with this pull machine and figure; no arch.',
        'Lats. Upper anatomical close-up: rear torso, only lats in a V highlighted coral. Bottom left seated lat pulldown, wide bar pulled to upper chest, rear view. Bottom right pull-up on a bar, chin over bar, rear view.',
        'Upper Back. Upper anatomical close-up: rear torso, only traps, rhomboids and middle back highlighted coral. Bottom left lying chest-down on a plate-loaded chest-supported row machine, rowing, side view. Bottom right seated cable row with wide bar, elbows out, side view.',
        'Rear Deltoid. Upper anatomical close-up: shoulder from behind, only rear deltoid highlighted coral. Bottom left seated reverse pec deck, arms opening wide, rear view. Bottom right standing at high cable with rope, pulling it toward face, elbows high and wide, side view.',
        'Traps. Upper anatomical close-up: upper back and neck from behind, only upper traps coral. Bottom left standing heavy dumbbells at sides, shoulders shrugged up, front view. Bottom right standing between two low cables, shrugging handles up, front view.',
        'Biceps. Upper anatomical close-up: front upper arm, only biceps coral. Bottom left standing EZ-bar curl, front view. Bottom right facing away from low cable, one arm behind body, curling handle forward, side view.',
        'Brachialis. Upper anatomical close-up: side upper arm, only brachialis and top forearm coral. Bottom left standing dumbbell hammer curl, palms facing in, front view. Bottom right standing EZ-bar curl, OVERHAND grip, front view.',
        'PRODUCT ENDING twin of attached LW-CAR-0031/08: left-aligned bold dark headline, short coral underline, then two separate grey regular body paragraphs. Generate ONLY TEXT and GRID background. Do NOT generate phone, hand, UI, screenshot, chart, placeholder, or any lower objects. The exact approved phone and real Muscle balance UI are inserted as unchanged bitmap pixels AFTER measuring the bottom of all body text; at least 40px gap. Headline may be two lines. Body second paragraph may wrap to two or three lines; include every word. Keep entire text comfortably above y800; remaining lower area only uniform grid background.'
    ]
    entries = []
    for slide, scene in zip(copy['slides'], scenes):
        n = slide['n']
        ref = f"carousels/LW-CAR-{'0005' if n < 8 else '0031'}/outputs/slide-{'01' if n == 1 else '08' if n == 8 else '02'}.png"
        layout = '' if n in (1, 8) else '''A OR B template: top centered coral underlined #N and bold dark muscle title on SAME LINE, immediately below top clear area. Under title: upper anatomy close-up. Two thin curved coral arrows lead down to separate left/right exercise figures. Both exercise figures entirely sand/ivory with NO highlighted muscles. Coral circle badge with white OR between them. Exact left/right regular labels under figures, keep full labels visible. Same spacing and proportions as attached approved LW-CAR-0005/02, replace ALL words/figures.\n'''
        prompt = common + '\n' + layout + scene + '\n\nEXACT TEXT AND STYLES, authoritative copy.json:\n' + '\n'.join(json.dumps(t, ensure_ascii=False) for t in slide['text']) + '\nReturn one opaque slide, never a contact sheet.\n'
        pf = f'prompts/slide-{n:02d}.txt'
        (ROOT / pf).write_text(prompt)
        entries.append(dict(slide=n, role=slide['role'], exact_text=[t['string'] for t in slide['text']], prompt_file=pf, references=[ref], file=f'outputs/slide-{n:02d}.png', attempts=[], errors=[], save_status='not_started', agent_visual_review='not_performed', user_review='pending'))
    write(dict(carousel_id=copy['carousel_id'], batch='BATCH-I', content_version=copy['content_version'], source_commit=subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', 'HEAD'], text=True).strip(), status='in_progress', carousel_complete=False, design_style='S1', background='GRID', brand='Harda', generated_images=0, next_slide_to_generate=1, agent_visual_review='not_performed', user_review='pending', remote_save=dict(remote='origin', branch='claude/charming-einstein-xgejky', status='not_yet_pushed'), slides=entries))
    (ROOT / 'caption.txt').write_text(copy['caption']['text'] + '\n')
    print('Initialized LW-CAR-0070: 8 exact-copy prompts and manifest')
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
        m['next_action'] = f'Stop Batch I per BATCH-I.md; resume this carousel at slide {n} after the recorded generation blocker is resolved. Do not start LW-CAR-0071.'
    else:
        raw_path = Path(sys.argv[3])
        asset = ROOT / f'production-assets/slide-{n:02d}-generated.png'
        shutil.copyfile(raw_path, asset)
        with Image.open(raw_path) as raw:
            im = Image.new('RGBA', raw.size, '#F0F1EB')
            im.alpha_composite(raw.convert('RGBA'))
            im = im.resize((1080, 1350), Image.Resampling.LANCZOS)
        if n == 8:
            # Required layout measurement only; no OCR or visual review.
            bounds = im.convert('L').point(lambda p: 255 if p < 180 else 0).crop((0, 110, 1080, 1350)).getbbox()
            if bounds is None:
                raise RuntimeError('No text extent available for required phone placement')
            bottom = 110 + bounds[3]
            phone_y = bottom + 50
            foreground = REPO / 'carousels/LW-CAR-0031/production-assets/approved-phone-hand-foreground.png'
            with Image.open(foreground) as phone:
                crop = phone.crop(phone.getbbox())
                im.alpha_composite(crop, (73, phone_y))
            slide['phone_compositing'] = dict(source=str(foreground.relative_to(REPO)), text_bottom=bottom, phone_top=phone_y, gap_px=50, scale='1:1 original pixels', ui_generated=False)
        with Image.open(REPO / 'assets/logo/harda-logo-full.png') as logo:
            im.alpha_composite(logo.convert('RGBA').resize((218, 71), Image.Resampling.LANCZOS), (48, 19))
        im.convert('RGB').save(ROOT / slide['file'])
        slide['attempts'][-1].update(status='succeeded', finished_at=now(), raw_result_file=str(raw_path), preserved_raw_file=str(asset.relative_to(ROOT)), result_file=slide['file'])
        slide['save_status'] = 'saved_in_cloud_checkout'
    m['generated_images'] = sum(s['save_status'] == 'saved_in_cloud_checkout' for s in m['slides'])
    m['next_slide_to_generate'] = next((s['slide'] for s in m['slides'] if s['save_status'] != 'saved_in_cloud_checkout'), None)
    write(m)
    print(f'{action}: LW-CAR-0070 slide {n}; {m["generated_images"]}/8 saved')
elif action == 'package':
    complete = m['generated_images'] == len(m['slides'])
    m['carousel_complete'] = complete
    if complete:
        m.update(status='complete_pending_owner_review', next_action='Commit and push this carousel, then continue LW-CAR-0071 without review pause.')
    m['archive'] = 'LW-CAR-0070' + ('' if complete else '-incomplete') + '-1080x1350.zip'
    m['remote_save'].update(status='prepared_for_commit_and_push', commit_lookup='git log -1 -- carousels/LW-CAR-0070/manifest.json')
    write(m)
    with zipfile.ZipFile(ROOT / m['archive'], 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in [*sorted((ROOT / 'outputs').glob('slide-*.png')), ROOT / 'caption.txt', MANIFEST]:
            archive.write(path, path.relative_to(ROOT))
    print(f'Packaged {m["generated_images"]}/8 images; {m["status"]}')
else:
    raise RuntimeError(f'Unknown action {action}')
