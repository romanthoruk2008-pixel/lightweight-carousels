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
    common = 'Create ONE complete 1080 x 1350 portrait Harda S2 fitness-humour carousel slide. Use the attached approved reference ONLY for layout, typography, spacing and colours, never its words or outfit. Heavy tight lowercase black #2A2A2A headlines with solid coral #F26445 marker bars behind the LOWER part of headline words only. Clean regular dark body, grey #6B6B6B italic subtitle. Solid opaque CLEAN #F0F1EB background, no texture, arch, rings, dots, grid, panel, slide counter, border, watermark or signature. Top 110px entirely empty for the ORIGINAL Harda PNG to be composited later at x48,y19,218x71; do not generate a logo. FIGURES: adult white/light-grey faceless sports display mannequins in OPAQUE WHITE CREW-NECK SPORTS T-SHIRTS with sleeves and loose CHARCOAL #2A2A2A athletic shorts. Shirts fully cover torsos. Neutral friendly sports-catalogue illustration, fine grey shading. Keep all clothing opaque and covering the body. No coloured muscles. Equipment black/grey and unbranded, no extra readable labels. Friendly harmless gym humour: nobody hurt, no injuries. Coral effect marks only when this slide explicitly specifies them. Preserve exact copy, all lowercase, curly apostrophes and punctuation. All words fully visible and separate from figures.\n'
    scenes = ['COVER twin of approved LW-CAR-0022/01 typography: centered huge two-line headline, coral marker behind second headline only, italic exact subtitle below. Large white/light-grey sports mannequin in T-shirt and charcoal shorts below, front view, one hand covering face in a friendly embarrassed gesture, a dropped dumbbell resting on floor near bottom. No stars, no injury.', 'TIER DIVIDER twin of LW-CAR-0022/02: centered rounded-square tile #5BDCE3, huge white bold letter F with soft shadow, huge black lowercase tier to its right. Center exact italic grey subtitle below. No figures, equipment, stars, marker bars, number or other text.', 'RANKED ITEM twin of LW-CAR-0022/03: heavy black #N followed by lowercase heavy headline; coral marker behind HEADLINE ONLY, not number. Long headline may wrap with marker per line. Under title exactly FIVE five-point stars, rating 1 of 5: filled #F26445, empty #D6D6D2, half rating means one half-coral/half-grey star. No written numeric rating. Then exact regular dark body, up to two lines. Lower ~55% required scene: standing in the gym patting the empty shorts pockets, worried, front view. Every figure wears the opaque sports T-shirt and shorts specified above. No muscle highlights, no extra figures, gestures or props beyond the required scene.', 'RANKED ITEM twin of LW-CAR-0022/03: heavy black #N followed by lowercase heavy headline; coral marker behind HEADLINE ONLY, not number. Long headline may wrap with marker per line. Under title exactly FIVE five-point stars, rating 1.5 of 5: filled #F26445, empty #D6D6D2, half rating means one half-coral/half-grey star. No written numeric rating. Then exact regular dark body, up to two lines. Lower ~55% required scene: waving with one hand, while a second figure in the background waves past them, front view. Every figure wears the opaque sports T-shirt and shorts specified above. No muscle highlights, no extra figures, gestures or props beyond the required scene.', 'TIER DIVIDER twin of LW-CAR-0022/02: centered rounded-square tile #3FCF5E, huge white bold letter C with soft shadow, huge black lowercase tier to its right. Center exact italic grey subtitle below. No figures, equipment, stars, marker bars, number or other text.', 'RANKED ITEM twin of LW-CAR-0022/03: heavy black #N followed by lowercase heavy headline; coral marker behind HEADLINE ONLY, not number. Long headline may wrap with marker per line. Under title exactly FIVE five-point stars, rating 2 of 5: filled #F26445, empty #D6D6D2, half rating means one half-coral/half-grey star. No written numeric rating. Then exact regular dark body, up to two lines. Lower ~55% required scene: sitting on a cable machine seat while a second figure holding a water bottle stands beside it, front view. Every figure wears the opaque sports T-shirt and shorts specified above. No muscle highlights, no extra figures, gestures or props beyond the required scene.', 'RANKED ITEM twin of LW-CAR-0022/03: heavy black #N followed by lowercase heavy headline; coral marker behind HEADLINE ONLY, not number. Long headline may wrap with marker per line. Under title exactly FIVE five-point stars, rating 2.5 of 5: filled #F26445, empty #D6D6D2, half rating means one half-coral/half-grey star. No written numeric rating. Then exact regular dark body, up to two lines. Lower ~55% required scene: pushing a plain glass door with a handle, confused posture, side view. Every figure wears the opaque sports T-shirt and shorts specified above. No muscle highlights, no extra figures, gestures or props beyond the required scene.', 'TIER DIVIDER twin of LW-CAR-0022/02: centered rounded-square tile #FFD95A, huge white bold letter B with soft shadow, huge black lowercase tier to its right. Center exact italic grey subtitle below. No figures, equipment, stars, marker bars, number or other text.', 'RANKED ITEM twin of LW-CAR-0022/03: heavy black #N followed by lowercase heavy headline; coral marker behind HEADLINE ONLY, not number. Long headline may wrap with marker per line. Under title exactly FIVE five-point stars, rating 3 of 5: filled #F26445, empty #D6D6D2, half rating means one half-coral/half-grey star. No written numeric rating. Then exact regular dark body, up to two lines. Lower ~55% required scene: plates sliding off one end of a barbell in a rack, small #F26445 motion lines, front view. Every figure wears the opaque sports T-shirt and shorts specified above. No muscle highlights, no extra figures, gestures or props beyond the required scene. EQUIPMENT-ONLY SCENE: plates sliding off one end of racked barbell with small coral motion lines; no mannequin is needed. Clear empty area around falling plates; nobody struck.', 'RANKED ITEM twin of LW-CAR-0022/03: heavy black #N followed by lowercase heavy headline; coral marker behind HEADLINE ONLY, not number. Long headline may wrap with marker per line. Under title exactly FIVE five-point stars, rating 3.5 of 5: filled #F26445, empty #D6D6D2, half rating means one half-coral/half-grey star. No written numeric rating. Then exact regular dark body, up to two lines. Lower ~55% required scene: barbell back squat, the bar tilting to one side, puzzled posture, front view. Every figure wears the opaque sports T-shirt and shorts specified above. No muscle highlights, no extra figures, gestures or props beyond the required scene. Depict a harmless awkward moment, nobody injured or trapped, no blood or distress. Props never cover text.', 'TIER DIVIDER twin of LW-CAR-0022/02: centered rounded-square tile #FF9A52, huge white bold letter A with soft shadow, huge black lowercase tier to its right. Center exact italic grey subtitle below. No figures, equipment, stars, marker bars, number or other text.', 'RANKED ITEM twin of LW-CAR-0022/03: heavy black #N followed by lowercase heavy headline; coral marker behind HEADLINE ONLY, not number. Long headline may wrap with marker per line. Under title exactly FIVE five-point stars, rating 4 of 5: filled #F26445, empty #D6D6D2, half rating means one half-coral/half-grey star. No written numeric rating. Then exact regular dark body, up to two lines. Lower ~55% required scene: a dumbbell bouncing on the floor next to the figure, small #F26445 impact lines, front view. Every figure wears the opaque sports T-shirt and shorts specified above. No muscle highlights, no extra figures, gestures or props beyond the required scene. Depict a harmless awkward moment, nobody injured or trapped, no blood or distress. Props never cover text.', 'RANKED ITEM twin of LW-CAR-0022/03: heavy black #N followed by lowercase heavy headline; coral marker behind HEADLINE ONLY, not number. Long headline may wrap with marker per line. Under title exactly FIVE five-point stars, rating 4.5 of 5: filled #F26445, empty #D6D6D2, half rating means one half-coral/half-grey star. No written numeric rating. Then exact regular dark body, up to two lines. Lower ~55% required scene: lying on a flat bench, the barbell resting low on the body, about to roll it down, side view. Every figure wears the opaque sports T-shirt and shorts specified above. No muscle highlights, no extra figures, gestures or props beyond the required scene. Depict a harmless awkward moment, nobody injured or trapped, no blood or distress. Props never cover text.', 'TIER DIVIDER twin of LW-CAR-0022/02: centered rounded-square tile #F26445, huge white bold letter S with soft shadow, huge black lowercase tier to its right. Center exact italic grey subtitle below. No figures, equipment, stars, marker bars, number or other text.', 'RANKED ITEM twin of LW-CAR-0022/03: heavy black #N followed by lowercase heavy headline; coral marker behind HEADLINE ONLY, not number. Long headline may wrap with marker per line. Under title exactly FIVE five-point stars, rating 5 of 5: filled #F26445, empty #D6D6D2, half rating means one half-coral/half-grey star. No written numeric rating. Then exact regular dark body, up to two lines. Lower ~55% required scene: barbell back squat at the bottom, small #F26445 tear marks on the shorts, side view. Every figure wears the opaque sports T-shirt and shorts specified above. No muscle highlights, no extra figures, gestures or props beyond the required scene. The small coral tear marks are purely comic drawn EFFECT STROKES on the outer side seam of the shorts. Keep the actual shorts intact and opaque, no opening, no exposed body through clothing.', 'RANKED ITEM twin of LW-CAR-0022/03: heavy black #N followed by lowercase heavy headline; coral marker behind HEADLINE ONLY, not number. Long headline may wrap with marker per line. Under title exactly FIVE five-point stars, rating 5 of 5: filled #F26445, empty #D6D6D2, half rating means one half-coral/half-grey star. No written numeric rating. Then exact regular dark body, up to two lines. Lower ~55% required scene: stumbling backwards off the end of a running treadmill, arms out, side view. Every figure wears the opaque sports T-shirt and shorts specified above. No muscle highlights, no extra figures, gestures or props beyond the required scene. Depict a harmless awkward moment, nobody injured or trapped, no blood or distress. Props never cover text.', 'PRODUCT ENDING twin of LW-CAR-0022/19 typography only. Left-aligned large heavy lowercase exact headline, coral marker bars ONLY under every set you lift and stay between us; wrap naturally without dropping words. Exact regular dark body below. All text comfortably above y850. Generate ONLY TEXT on plain background; NO phone, hand, screenshot, app UI, icons, charts, placeholders or lower objects. Original approved white-hand/phone with real Muscle balance bitmap inserted afterward at unchanged proportions, below measured final body row with at least 40px gap, never at fixed height.']
    entries = []
    for slide, scene in zip(copy['slides'], scenes):
        n = slide['n']
        ref = "carousels/LW-CAR-0022/outputs/slide-01.png" if n == 1 else "carousels/LW-CAR-0022/outputs/slide-19.png" if slide["role"] == "product ending" else "carousels/LW-CAR-0022/outputs/slide-02.png" if slide["role"].startswith("tier divider") else "carousels/LW-CAR-0022/outputs/slide-03.png"
        layout = ""
        prompt = common + '\n' + layout + scene + '\n\nEXACT TEXT AND STYLES, authoritative copy.json:\n' + '\n'.join(json.dumps(t, ensure_ascii=False) for t in slide['text']) + '\nReturn one opaque slide, never a contact sheet.\n'
        pf = f'prompts/slide-{n:02d}.txt'
        (ROOT / pf).write_text(prompt)
        entries.append(dict(slide=n, role=slide['role'], rating_stars=slide.get('rating_stars'), exact_text=[t['string'] for t in slide['text']], prompt_file=pf, references=[ref], file=f'outputs/slide-{n:02d}.png', attempts=[], errors=[], save_status='not_started', agent_visual_review='not_performed', user_review='pending'))
    write(dict(carousel_id=copy['carousel_id'], batch='BATCH-I', content_version=copy['content_version'], source_commit=subprocess.check_output(['git', '-C', str(REPO), 'rev-parse', 'HEAD'], text=True).strip(), status='in_progress', carousel_complete=False, design_style='S2', background='CLEAN', brand='Harda', generated_images=0, next_slide_to_generate=1, agent_visual_review='not_performed', user_review='pending', remote_save=dict(remote='origin', branch='claude/charming-einstein-xgejky', status='not_yet_pushed'), slides=entries))
    (ROOT / 'caption.txt').write_text(copy['caption']['text'] + '\n')
    print('Initialized LW-CAR-0076: 17 exact-copy prompts and manifest')
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
        m['next_action'] = f'Stop Batch I per BATCH-I.md; resume this carousel at slide {n} after the recorded generation blocker is resolved. Record the blocker and await an explicit next action.'
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
    print(f'{action}: LW-CAR-0076 slide {n}; {m["generated_images"]}/17 saved')
elif action == 'package':
    complete = m['generated_images'] == len(m['slides'])
    m['carousel_complete'] = complete
    if complete:
        m.update(status='complete_pending_owner_review', next_action='Commit and push this carousel. Batch I generation is complete; owner review remains pending.')
    m['archive'] = 'LW-CAR-0076' + ('' if complete else '-incomplete') + '-1080x1350.zip'
    m['remote_save'].update(status='prepared_for_commit_and_push', commit_lookup='git log -1 -- carousels/LW-CAR-0076/manifest.json')
    write(m)
    with zipfile.ZipFile(ROOT / m['archive'], 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in [*sorted((ROOT / 'outputs').glob('slide-*.png')), ROOT / 'caption.txt', MANIFEST]:
            archive.write(path, path.relative_to(ROOT))
    print(f'Packaged {m["generated_images"]}/17 images; {m["status"]}')
else:
    raise RuntimeError(f'Unknown action {action}')
