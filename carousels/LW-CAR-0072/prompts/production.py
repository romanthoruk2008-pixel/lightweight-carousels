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
    import numpy as np
    from scipy import ndimage
    phone_source = REPO / 'carousels/LW-CAR-0009/outputs/slide-08.png'
    with Image.open(phone_source) as original:
        phone = original.convert('RGBA').crop((0, 420, 1080, 1350))
    barrier = np.array(phone)[:, :, :3].mean(axis=2) < 160
    barrier = ndimage.binary_closing(barrier, iterations=1)
    barrier[-2:, 20:970] = True
    filled = ndimage.binary_fill_holes(barrier)
    labels, count = ndimage.label(filled)
    sizes = ndimage.sum(filled, labels, range(1, count + 1))
    phone.putalpha(Image.fromarray((labels == int(np.argmax(sizes)) + 1).astype(np.uint8) * 255))
    phone.save(ROOT / 'production-assets/approved-phone-hand.png')
    common = '''Create ONE complete 1080 x 1350 portrait Harda fitness carousel slide. The attached approved slide is a VISUAL template only, never the source of words. Exact text below comes only from frozen copy.json. Preserve every capital, hyphen, apostrophe and punctuation. Rubik type: heaviest cover, bold title, regular labels/body. Dark #2A2A2A, body #6B6B6B, accent #F26445. BACKGROUND: entire canvas solid opaque #F0F1EB, then three concentric #EAE0D6 rings of stroke 26/22/18px and radius 520/400/280px centered at x1010,y1290, mostly off-canvas like weight plates. Absolutely NO ARCH, grid, dots, gradient, progress bar, counter, transparency checkerboard, watermark or signature. Leave the top 110px empty except the background: do NOT draw a logo, brand name or icon there. The ORIGINAL Harda PNG is composited later at x48,y19,218x71 using its own alpha. S1 FIGURES ONLY: bald faceless smooth plastic anatomy teaching mannequin with warm-sand #D9CBBE muscles, darker sand shading, ivory #F5F0E5 tendons, fine grey linework, smooth featureless pelvis covered by opaque plain sand short shorts on full-body figures. Never white S2 figures, green, sage, real human nudity, invented equipment or extra copy. Equipment black/grey. Every word fully visible inside slide edges, no overlap.\n'''
    scenes = ['COVER twin of attached LW-CAR-0009/01: three very large stacked UPPERCASE Rubik lines: STRUCTURE dark; THE PERFECT dark; PULL DAY coral. Lower half anatomy mannequin doing a PULL-UP on a bar, REAR VIEW, chin OVER bar; lats and upper back coral. Lower edge may crop like template. No arch.', 'CHECKLIST twin of attached LW-CAR-0009/02: top-left two-line bold exact title, short coral underline; six left-aligned bulleted lines with 1x regular, muscle name bold, brackets regular. At bottom-right cropped at right and bottom, UPPER BODY head to waist REAR VIEW, one arm flexed in double-biceps-style pose; lats, traps, rear delts and biceps coral. Replace reference legs with this upper body. Keep full text visible.', 'LIST twin of attached LW-CAR-0009/03: top-left large coral #N, short coral underline, title bold dark to its right and regular grey sets line under title. Under header left-aligned exact grey sentence, up to two or three lines if needed. Bottom ~55% two full-body exercise figures, both entirely sand/ivory WITHOUT muscle highlights, thin vertical coral divider between them. Regular dark exact exercise labels under each figure, long labels wrap without shortening. NO OR badge, no arrows or close-up. Slide specification from task table: `#1` | `Lats` | `2-3 sets x 6-10 reps` | `Choose one of these exercises to widen your back:` | seated lat pulldown, wide bar pulled to the upper chest, rear view — `Lat Pulldown` | pull-up on a bar, chin over the bar, rear view — `Pull-Ups`', 'LIST twin of attached LW-CAR-0009/03: top-left large coral #N, short coral underline, title bold dark to its right and regular grey sets line under title. Under header left-aligned exact grey sentence, up to two or three lines if needed. Bottom ~55% two full-body exercise figures, both entirely sand/ivory WITHOUT muscle highlights, thin vertical coral divider between them. Regular dark exact exercise labels under each figure, long labels wrap without shortening. NO OR badge, no arrows or close-up. Slide specification from task table: `#2` | `Upper Back` | `2-3 sets x 6-10 reps` | `Choose one of these exercises to thicken your upper back:` | lying chest-down on a plate-loaded T-bar row machine, rowing, side three-quarter view — `T-Bar Row` | seated wide-grip machine row, elbows out, side view — `Wide-Grip Machine Row`', 'LIST twin of attached LW-CAR-0009/03: top-left large coral #N, short coral underline, title bold dark to its right and regular grey sets line under title. Under header left-aligned exact grey sentence, up to two or three lines if needed. Bottom ~55% two full-body exercise figures, both entirely sand/ivory WITHOUT muscle highlights, thin vertical coral divider between them. Regular dark exact exercise labels under each figure, long labels wrap without shortening. NO OR badge, no arrows or close-up. Slide specification from task table: `#3` | `Lats` | `2-3 sets x 8-12 reps` | `Choose one of these exercises to pull your elbows back to your hips:` | seated cable row with a close V-handle, elbows tight to the body, side view — `Close-Grip Seated Row` | standing at a high cable, straight arms pushing a bar down to the thighs, side view — `Lat Pullover`', 'LIST twin of attached LW-CAR-0009/03: top-left large coral #N, short coral underline, title bold dark to its right and regular grey sets line under title. Under header left-aligned exact grey sentence, up to two or three lines if needed. Bottom ~55% two full-body exercise figures, both entirely sand/ivory WITHOUT muscle highlights, thin vertical coral divider between them. Regular dark exact exercise labels under each figure, long labels wrap without shortening. NO OR badge, no arrows or close-up. Slide specification from task table: `#4` | `Rear Delts` | `2-3 sets x 12-20 reps` | `Choose one of these exercises to isolate your rear delts:` | seated reverse pec deck, arms opening wide, rear view — `Reverse Pec Dec` | standing between two high cables, arms crossed, pulling the handles out wide, rear view — `Cable Reverse Fly`', 'LIST twin of attached LW-CAR-0009/03: top-left large coral #N, short coral underline, title bold dark to its right and regular grey sets line under title. Under header left-aligned exact grey sentence, up to two or three lines if needed. Bottom ~55% two full-body exercise figures, both entirely sand/ivory WITHOUT muscle highlights, thin vertical coral divider between them. Regular dark exact exercise labels under each figure, long labels wrap without shortening. NO OR badge, no arrows or close-up. Slide specification from task table: `#5` | `Biceps` | `2-3 sets x 8-12 reps` | `Choose one of these exercises to isolate your biceps:` | seated at a preacher bench, curling an EZ bar, side view — `Preacher Curl` | standing cable curl with a straight bar at a low pulley, front view — `Cable Curl`', 'LIST twin of attached LW-CAR-0009/03: top-left large coral #N, short coral underline, title bold dark to its right and regular grey sets line under title. Under header left-aligned exact grey sentence, up to two or three lines if needed. Bottom ~55% two full-body exercise figures, both entirely sand/ivory WITHOUT muscle highlights, thin vertical coral divider between them. Regular dark exact exercise labels under each figure, long labels wrap without shortening. NO OR badge, no arrows or close-up. Slide specification from task table: `#6` | `Forearms` | `2-3 sets x 10-15 reps` | `Choose one of these exercises to train your forearms:` | standing at a low cable with a rope, curling with palms facing in, front view — `Cable Hammer Curl` | standing at a low cable with a straight bar, curling with an overhand grip, front view — `Cable Reverse Curl`', 'PRODUCT ENDING twin of attached LW-CAR-0009/08: short coral bar ABOVE left-aligned two-line heaviest Rubik headline; first exact string dark, second exact string coral. Only these TWO strings of text. Generate ONLY text and PLATES background. NO phone, hand, UI, chart, screen, icons, placeholders or lower objects: original approved phone/hand with real Muscle balance UI is inserted afterward without resampling, below measured last text line with at least 40px gap. Keep headline comfortably above y650, lower area only requested background. No arch.']
    entries = []
    for slide, scene in zip(copy['slides'], scenes):
        n = slide['n']
        ref = f"carousels/LW-CAR-0009/outputs/slide-{'01' if n == 1 else '02' if n == 2 else '08' if n == 9 else '03'}.png"
        layout = ""
        prompt = common + '\n' + layout + scene + '\n\nEXACT TEXT AND STYLES, authoritative copy.json:\n' + '\n'.join(json.dumps(t, ensure_ascii=False) for t in slide['text']) + '\nReturn one opaque slide, never a contact sheet.\n'
        pf = f'prompts/slide-{n:02d}.txt'
        (ROOT / pf).write_text(prompt)
        entries.append(dict(slide=n, role=slide['role'], exact_text=[t['string'] for t in slide['text']], prompt_file=pf, references=[ref], file=f'outputs/slide-{n:02d}.png', attempts=[], errors=[], save_status='not_started', agent_visual_review='not_performed', user_review='pending'))
    write(dict(carousel_id=copy['carousel_id'], batch='BATCH-I', content_version=copy['content_version'], source_commit=subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', 'HEAD'], text=True).strip(), status='in_progress', carousel_complete=False, design_style='S1', background='PLATES', brand='Harda', generated_images=0, next_slide_to_generate=1, agent_visual_review='not_performed', user_review='pending', remote_save=dict(remote='origin', branch='claude/charming-einstein-xgejky', status='not_yet_pushed'), slides=entries))
    (ROOT / 'caption.txt').write_text(copy['caption']['text'] + '\n')
    print('Initialized LW-CAR-0072: 9 exact-copy prompts and manifest')
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
        m['next_action'] = f'Stop Batch I per BATCH-I.md; resume this carousel at slide {n} after the recorded generation blocker is resolved. Do not start LW-CAR-0073.'
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
    print(f'{action}: LW-CAR-0072 slide {n}; {m["generated_images"]}/9 saved')
elif action == 'package':
    complete = m['generated_images'] == len(m['slides'])
    m['carousel_complete'] = complete
    if complete:
        m.update(status='complete_pending_owner_review', next_action='Commit and push this carousel, then continue LW-CAR-0073 without review pause.')
    m['archive'] = 'LW-CAR-0072' + ('' if complete else '-incomplete') + '-1080x1350.zip'
    m['remote_save'].update(status='prepared_for_commit_and_push', commit_lookup='git log -1 -- carousels/LW-CAR-0072/manifest.json')
    write(m)
    with zipfile.ZipFile(ROOT / m['archive'], 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in [*sorted((ROOT / 'outputs').glob('slide-*.png')), ROOT / 'caption.txt', MANIFEST]:
            archive.write(path, path.relative_to(ROOT))
    print(f'Packaged {m["generated_images"]}/9 images; {m["status"]}')
else:
    raise RuntimeError(f'Unknown action {action}')
