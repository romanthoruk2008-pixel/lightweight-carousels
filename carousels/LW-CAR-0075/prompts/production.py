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
    common = 'Create ONE complete 1080 x 1350 portrait Harda S2 carousel slide. Attached approved slide is a VISUAL template ONLY, never the text source. EXACT text below comes solely from frozen copy.json; preserve all lowercase, curly quotes/apostrophes, hyphens and punctuation. S2 style: very heavy tight lowercase grotesk headline #2A2A2A; solid coral #F26445 MARKER BARS behind the LOWER part of the specified words only. Clean regular sans body #2A2A2A; small subtitle italic regular #6B6B6B. Solid opaque CLEAN #F0F1EB background, no texture, arch, rings, dots, grid, panels, gradients, counter, watermark or signatures. Leave entire TOP 110px empty background: NO generated logo, name or icon. The ORIGINAL Harda PNG is composited later at x48,y19,218x71 using its own transparency without backing patch. S2 FIGURE: realistic WHITE/LIGHT-GREY bald faceless anatomical mannequin, fine grey shading and muscle fibres, smooth featureless pelvis covered by opaque loose CHARCOAL #2A2A2A gym shorts. Never beige/sand S1, cartoon or clay. Equipment black/grey, props plain/unbranded. No readable labels on equipment, no invented UI. Only target muscles specified for THIS slide are coral #F26445; every other muscle stays white/light-grey. No exercise equipment on muscle item slides. Tier tiles and stars ONLY where the specific layout below requests them. Only exact provided text, no inherited fix:, do:, extra badges or speech-bubble words. Every word fully visible inside slide, no overlap.\n'
    scenes = ['COVER twin of attached LW-CAR-0022/01: two stacked centered heavy lowercase headline strings, first exact string on ONE line scaled to fit, second exact string on coral marker bar; centered italic subtitle underneath. Lower large S2 white figure, front view FROM THIGHS UP, relaxed confident stance; shoulders, chest, arms and abs coral. Charcoal shorts remain opaque. No equipment. Replace all old words and pose; no stars.', 'TIER DIVIDER identical centered layout, spacing, sizes as attached LW-CAR-0022/02: rounded square tile #5BDCE3, HUGE white bold F with soft shadow, huge black lowercase tier to its right. Centered italic grey exact subtitle below. No figure, equipment, stars, marker bars, number or other text. The tile colour for this slide is #5BDCE3.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 1 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: rear view, standing relaxed, lower back erectors filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 1.5 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: rear view, standing, one leg slightly back, hamstrings filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'TIER DIVIDER identical centered layout, spacing, sizes as attached LW-CAR-0022/02: rounded square tile #3FCF5E, HUGE white bold C with soft shadow, huge black lowercase tier to its right. Centered italic grey exact subtitle below. No figure, equipment, stars, marker bars, number or other text. The tile colour for this slide is #3FCF5E.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 2 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: rear view, standing on the toes, calves filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 2.5 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: front view from the waist up, one fist clenched in front of the body, forearms filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'TIER DIVIDER identical centered layout, spacing, sizes as attached LW-CAR-0022/02: rounded square tile #FFD95A, HUGE white bold B with soft shadow, huge black lowercase tier to its right. Centered italic grey exact subtitle below. No figure, equipment, stars, marker bars, number or other text. The tile colour for this slide is #FFD95A.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 3 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: front view, standing, one leg forward and flexed, quads filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 3 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: rear view from the waist up, arms relaxed, traps filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 3.5 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: rear three-quarter view, standing, glutes filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'TIER DIVIDER identical centered layout, spacing, sizes as attached LW-CAR-0022/02: rounded square tile #FF9A52, HUGE white bold A with soft shadow, huge black lowercase tier to its right. Centered italic grey exact subtitle below. No figure, equipment, stars, marker bars, number or other text. The tile colour for this slide is #FF9A52.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 4 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: front view from the waist up, hands on hips, chest filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 4 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: front view from the waist up, front double biceps pose, biceps and triceps filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 4.5 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: front view from the thighs up, hands behind the head, abs filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'TIER DIVIDER identical centered layout, spacing, sizes as attached LW-CAR-0022/02: rounded square tile #F26445, HUGE white bold S with soft shadow, huge black lowercase tier to its right. Centered italic grey exact subtitle below. No figure, equipment, stars, marker bars, number or other text. The tile colour for this slide is #F26445.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 5 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: rear view from the waist up, rear lat spread pose, lats and upper back filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'RANKED MUSCLE ITEM twin of attached LW-CAR-0022/03: heavy dark #N then heavy lowercase muscle headline with coral marker behind HEADLINE ONLY. Under title EXACTLY FIVE five-point stars, rating 5 out of 5: filled stars #F26445, empty #D6D6D2, half rating shows one star HALF coral/HALF grey. Do not write numeric rating or add words. Then exact regular dark body, up to two lines. Lower ~55% ONE large posed white S2 anatomy figure with opaque charcoal shorts. Figure and highlighted muscle: front view from the waist up, arms slightly away from the body, all three delts filled #F26445. Fill only target muscle coral, rest white/light-grey. No exercise equipment, no extra figures.', 'PRODUCT ENDING twin of attached LW-CAR-0022/19, typography only. Large left-aligned heavy lowercase headline, marker bars ONLY under every set you lift and every muscle gets its turn, each phrase can wrap with marker under its line. Regular exact body below. Keep all text comfortably above y850. Generate ONLY TEXT on plain background: NO phone, hand, app UI, screen, chart, icon, placeholder or lower objects. Original white hand/phone with REAL Muscle balance screenshot inserted unchanged after measuring bottom of final body line, at least 40px gap. Never fixed phone height.']
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
    print('Initialized LW-CAR-0075: 19 exact-copy prompts and manifest')
    sys.exit()

m = json.loads(MANIFEST.read_text())
if action in ('start', 'retry', 'save', 'error'):
    n = int(sys.argv[2])
    slide = m['slides'][n - 1]
    if action in ('start', 'retry'):
        if action == 'start' and (slide['attempts'] or slide['save_status'] != 'not_started'):
            raise RuntimeError('Do not repeat or overwrite an existing generation attempt')
        if action == 'retry' and (slide['save_status'] != 'generation_failed' or len(slide['attempts']) >= 3 or (ROOT / slide['file']).exists()):
            raise RuntimeError('Only an explicitly authorized retry of a failed, unsaved slide is allowed (two additional attempts maximum)')
        slide['attempts'].append(dict(attempt=len(slide['attempts']) + 1, tool='image_gen.imagegen', status='in_progress', started_at=now(), prompt_file=slide['prompt_file'], referenced_image_paths=slide['references'], transparent_background=False))
        slide['save_status'] = 'generation_in_progress'
        m['status'] = 'in_progress'
    elif action == 'error':
        message = sys.argv[3]
        slide['errors'].append(message)
        slide['attempts'][-1].update(status='error', finished_at=now(), error=message)
        slide['save_status'] = 'generation_failed'
        m['status'] = 'incomplete_generation_failed'
        m['next_action'] = f'Stop Batch I per BATCH-I.md; resume this carousel at slide {n} after the recorded generation blocker is resolved. Do not start LW-CAR-0076.'
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
    print(f'{action}: LW-CAR-0075 slide {n}; {m["generated_images"]}/19 saved')
elif action == 'package':
    complete = m['generated_images'] == len(m['slides'])
    m['carousel_complete'] = complete
    if complete:
        m.update(status='complete_pending_owner_review', next_action='Commit and push this carousel, then continue LW-CAR-0076 without review pause.')
    m['archive'] = 'LW-CAR-0075' + ('' if complete else '-incomplete') + '-1080x1350.zip'
    m['remote_save'].update(status='prepared_for_commit_and_push', commit_lookup='git log -1 -- carousels/LW-CAR-0075/manifest.json')
    write(m)
    with zipfile.ZipFile(ROOT / m['archive'], 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in [*sorted((ROOT / 'outputs').glob('slide-*.png')), ROOT / 'caption.txt', MANIFEST]:
            archive.write(path, path.relative_to(ROOT))
    print(f'Packaged {m["generated_images"]}/19 images; {m["status"]}')
else:
    raise RuntimeError(f'Unknown action {action}')
