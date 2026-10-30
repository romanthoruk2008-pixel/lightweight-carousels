"""Batch H production and exact-file layers; no visual QA or OCR; at most two additional failure attempts."""
import json
import re
import shutil
import subprocess
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image

repo = Path.cwd()
action, cid = sys.argv[1:3]
root = repo / 'carousels' / cid
mp = root / 'manifest.json'
now = datetime.now(timezone.utc).isoformat()

def write(m):
    mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + '\n')

if action == 'init':
    if mp.exists() or list((root / 'outputs').glob('*.png')):
        raise RuntimeError('Reconcile existing results before starting; never overwrite')
    copy = json.loads((root / 'copy.json').read_text())
    task = (root / 'prompts/codex-task.md').read_text()
    if copy['design_style'] != 'S1':
        raise RuntimeError('This helper is for S1 only')
    (root / 'outputs').mkdir(exist_ok=True)
    (root / 'production-assets').mkdir(exist_ok=True)
    shutil.copyfile(__file__, root / 'prompts/production.py')
    phone_source = 'carousels/LW-CAR-0031/production-assets/approved-phone-hand-foreground.png'
    with Image.open(repo / phone_source) as phone:
        phone = phone.convert('RGBA')
        bounds = phone.getchannel('A').getbbox()
        if bounds is None:
            raise RuntimeError('Approved phone foreground is empty')
        phone.crop((0, bounds[1], phone.width, phone.height)).save(root / 'production-assets/approved-phone-hand-foreground.png')
    backgrounds = {
        'GRID': 'thin #E1E2DA grid lines, 2 px every 54 px, across the whole canvas',
        'DOTS': 'small #D4D4CC dots, 6 px diameter every 45 px, across the whole canvas',
        'PLATES': 'three concentric #EAE0D6 rings, stroke 26 / 22 / 18 px, radius 520 / 400 / 280 px, centred x1010 y1290, mostly off canvas',
        'CLEAN': 'nothing else; plain clean background',
    }
    bg = copy['background']
    common = f'''Create ONE Harda S1 fitness carousel slide for export as 1080 x 1350 opaque RGB PNG. Match the attached approved S1 reference for layout, typography hierarchy, sizes, illustration style, linework, badges and underline bars. Reference supplies DESIGN ONLY; all words must come from the current slide's copy.json entries below.
BACKGROUND: fill entire canvas solid opaque #F0F1EB FIRST, then {backgrounds[bg]}. This background is {bg}, even if the reference shows a different background. NO ARCH, no pink arch, no progress bar, slide counter, watermark, gradient, checkerboard or transparent canvas.
Keep the top 110 px free of all text, badges, figures and logos; the background pattern continues there. Do NOT draw a logo or wordmark: the exact original Harda PNG is composited later at x48 y19, size218x71 using its own alpha, with no patch.
S1 FIGURES: bald faceless smooth PLASTIC anatomy teaching mannequins with featureless pelvis, fine grey linework, ivory skin/tendons about #F5F0E5, muscles warm sand #D9CBBE with darker sand shading; target highlights #F26445 only as specified. No white S2 figure, no green/sage. Exercise figures wear plain opaque sand #D9CBBE gym shorts. For isolated anatomy diagram close-ups and cover/map cutaways, follow the task-specific crop and clothing instructions: rigid nonhuman plastic teaching model, featureless pelvis, no genital detail. These are neutral anatomical diagrams. Equipment realistic black/grey. Do not copy exercises or muscle highlights from reference; use only the current assigned subject.
FONT: Rubik for EVERY word, cover heaviest, titles bold, sets/subtitles/labels semibold, body regular. Text #2A2A2A, body #6B6B6B, accent #F26445, white badge text. Preserve EXACT case, apostrophes, plain hyphens, x and punctuation from copy.json. No other words, no equipment labels. Keep every line fully visible and away from the slide edges; scale illustrations down if needed, never omit or rewrite copy.
'''
    entries = []
    for s in copy['slides']:
        n, role = s['n'], s['role']
        refs = [f'carousels/LW-CAR-0031/outputs/slide-{n:02d}.png']
        sections = re.split(r'(?=^### )', task, flags=re.M)
        detail = next((part for part in sections if re.match(r'### Slide ' + str(n) + r'\b', part)), '')
        if role.startswith('list item'):
            row = next(line for line in task.splitlines() if line.startswith(f'| {n} |'))
            detail = '''LIST TEMPLATE: coral circle with white badge number centered below y110, bold centered muscle title, sets line, short coral underline, centered grey why line below. Middle: large anatomical CLOSE-UP with only specified muscle highlighted. Lower section: TWO full-body exercise mannequins, left and right, CORAL OR circle between them, exercise labels fully visible beneath. Exercise figures have NO muscle highlights: all muscles stay sand. Match reference sizes/spacing, but replace close-up, exercises, labels and every word with the current row. Keep equipment entirely readable and all copy clear.
Columns: Slide | Badge | Title | Subtitle | Why line | Close-up highlighted | Left exercise/label | Right exercise/label
''' + row
        elif role == 'product ending':
            detail += '''\nPRODUCTION OVERRIDE FOR EXACT UI: generate ONLY the headline, its short coral underline, and both body paragraphs on the background. NO phone, hand, screenshot, UI, chart, placeholder or decoration. Lower area remains empty of foreground objects. Headline bold Rubik, left aligned below y150; body regular grey paragraphs below, complete and readable, comfortably above y850. The ORIGINAL transparent S1 hand/phone/real Muscle balance image from the approved reference will be composited at unchanged 1:1 scale AFTER measuring the actual last body-text row, with a 50 px gap below it. Never generate app UI and never place a phone at a fixed height. Ignore the phone in the input image for generation.'''
        elif role == 'hook':
            detail += '\nUse the reference headline scale and two lines, with WEAK dark and the assigned body-part word coral, grey offset shadow and small coral paint-splat dot near the question mark. The isolated anatomy cutaway is cropped exactly as specified, with no head or torso added if not requested. Use only the pose/target muscles specified above, never the reference core pose.'
        if not detail:
            raise RuntimeError(f'Missing slide instructions for {n}')
        prompt = common + '\nCURRENT SLIDE INSTRUCTIONS:\n' + detail + '\n\nAUTHORITATIVE EXACT COPY AND STYLES:\n' + '\n'.join(json.dumps(t,ensure_ascii=False) for t in s['text']) + '\nReturn one complete slide, no variants.\n'
        pf = f'prompts/slide-{n:02d}.txt'
        (root / pf).write_text(prompt)
        entries.append(dict(slide=n,role=role,content_version=copy['content_version'],exact_text=[t['string'] for t in s['text']],file=f'outputs/slide-{n:02d}.png',prompt_file=pf,references=refs,attempts=[],errors=[],save_status='not_started',agent_visual_review='not_performed',user_review='pending'))
    m = dict(carousel_id=cid,content_version=copy['content_version'],source_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),batch='BATCH-H',batch_status='running',design_style='S1',background=bg,brand='Harda',status='in_progress',carousel_complete=False,generated_images=0,next_slide_to_generate=1,next_action='Finish this carousel, commit and push, then continue BATCH-H in order without review pauses. On generation error, push existing progress and stop.',agent_visual_review='not_performed',user_review='pending',logo=dict(file='assets/logo/harda-logo-full.png',placement=[48,19,218,71],method='original PNG with own alpha; no backing patch'),phone_source=dict(file=phone_source,crop=[0,bounds[1],phone.width,phone.height],scale='1:1'),remote_save=dict(remote='origin',branch='claude/charming-einstein-xgejky',status='not_yet_pushed'),slides=entries)
    (root / 'caption.txt').write_text(copy['caption']['text'] + '\n')
    write(m)
    print(json.dumps(dict(carousel=cid,count=len(entries),background=bg)))
    sys.exit()

m = json.loads(mp.read_text())
if action in ('start','save','error'):
    n = int(sys.argv[3])
    s = next(s for s in m['slides'] if s['slide']==n)
    if action == 'start':
        count = len(s['attempts'])
        if (root/s['file']).exists() or s['save_status']=='saved_to_repository_checkout':
            raise RuntimeError('Never regenerate a saved slide automatically')
        if count >= 3 or (count and s['attempts'][-1]['status'] != 'error'):
            raise RuntimeError('Retry budget exhausted or attempt unresolved')
        if not count and s['save_status'] != 'not_started':
            raise RuntimeError('Reconcile unexpected slide state')
        if count:
            original = root/s['attempts'][0]['prompt_file']
            retry_file = f'prompts/slide-{n:02d}-attempt-{count+1:02d}.txt'
            if (root/retry_file).exists():
                raise RuntimeError('Do not overwrite an existing attempt prompt')
            if s['role']=='product ending':
                correction = 'Simplify this to a clean text-only plate, with all exact words and requested hierarchy, ample spacing and no foreground objects below the final text line. The original real UI is inserted later. Do not copy reference text.'
            elif count==1:
                correction = 'Use an adult nonhuman sports teaching mannequin fully dressed in an opaque sand long-sleeve athletic top and full-length sand sports leggings. All hips, torso and legs are covered by fabric. Show specified target muscles only as flat coral instructional patches ON TOP OF CLOTHING. Preserve the exact specified exercise, neutral side/front view, layout, S1 linework/palette and every word. No exposed anatomical body or realistic skin.'
            else:
                correction = 'Use a simple neutral sports-instruction drawing of a faceless adult plastic figurine in a fully covering opaque sand tracksuit, full-length trousers and athletic shoes, with simplified joints and fine grey outlines. Use a flat coral patch on the clothing for the specified muscle target. Keep the same requested ordinary gym movement and equipment, shown neutrally from the side, the same layout and ALL exact copy. No exposed anatomy or skin. This is an exercise diagram, not a realistic human body.'
            (root/retry_file).write_text(original.read_text()+'\nFAILURE RETRY CORRECTION — owner directive 2026-10-30:\n'+correction+'\n')
            s['prompt_file'] = retry_file
        s['save_status'] = 'generation_in_progress'
        s['attempts'].append(dict(attempt=count+1,tool='image_gen.imagegen',status='in_progress',started_at=now,prompt_file=s['prompt_file'],transparent_background=False,referenced_image_paths=[str(repo/p) for p in s['references']],retry_policy='Owner 2026-10-30: at most two additional attempts per failed slide; then continue other slides/packages'))
        m.update(status='in_progress',batch_status='running_with_failure_retries',next_action='Finish remaining slides; after at most two additional failed attempts record the missing slide and continue the next carousel.')
    elif action == 'save':
        raw_path = Path(sys.argv[4])
        with Image.open(raw_path) as raw:
            raw_meta = dict(size=list(raw.size),mode=raw.mode)
            im = Image.new('RGBA',raw.size,'#F0F1EB')
            im.alpha_composite(raw.convert('RGBA'))
            im = im.resize((1080,1350),Image.Resampling.LANCZOS)
        if s['role'] == 'product ending':
            shutil.copyfile(raw_path,root/'production-assets/ending-generated-text.png')
            ink = im.convert('L').point(lambda v:255 if v<190 else 0).crop((0,110,1080,1350))
            bounds = ink.getbbox()
            if bounds is None:
                raise RuntimeError('Ending has no measurable text ink')
            text_bottom = 110 + bounds[3]
            phone_y = text_bottom + 50
            if phone_y >= 1300:
                raise RuntimeError('Insufficient remaining canvas for phone')
            with Image.open(root/'production-assets/approved-phone-hand-foreground.png') as phone:
                im.alpha_composite(phone.convert('RGBA'),(0,phone_y))
            s['phone_compositing'] = dict(source=m['phone_source'],asset='production-assets/approved-phone-hand-foreground.png',measured_text_bottom_exclusive=text_bottom,placement=[0,phone_y],minimum_gap=50,scale='1:1; no resampling',real_ui_generated=False,measurement='raster ink extent solely for requested layout; no OCR or visual QA')
        with Image.open(repo/'assets/logo/harda-logo-full.png') as logo:
            im.alpha_composite(logo.convert('RGBA').resize((218,71),Image.Resampling.LANCZOS),(48,19))
        output = root/s['file']
        im.convert('RGB').save(output,format='PNG')
        with Image.open(output) as saved:
            if saved.size != (1080,1350) or saved.mode != 'RGB':
                raise RuntimeError('Expected opaque RGB 1080x1350 export')
        s['save_status'] = 'saved_to_repository_checkout'
        s['attempts'][-1].update(status='succeeded',finished_at=now,raw_result_file=str(raw_path),raw_result_format=raw_meta,result_file=s['file'],export=dict(size=[1080,1350],mode='RGB',alpha=False))
    else:
        error = sys.argv[4]
        s['errors'].append(error)
        s['save_status'] = 'failed_after_retries' if len(s['attempts'])>=3 else 'interrupted'
        s['attempts'][-1].update(status='error',finished_at=now,error=error)
        m.update(status='in_progress',batch_status='running_with_failure_retries',next_action=f'Retry slide {n} up to three total attempts, then continue remaining slides and carousels; retain missing-slide status.')
    m['generated_images'] = sum(s['save_status']=='saved_to_repository_checkout' for s in m['slides'])
    m['next_slide_to_generate'] = next((s['slide'] for s in m['slides'] if s['save_status']!='saved_to_repository_checkout'),None)
    write(m)
    print(json.dumps(dict(carousel=cid,slide=n,action=action,saved=m['generated_images'],total=len(m['slides']))))
elif action == 'package':
    complete = m['generated_images']==len(m['slides'])
    m.update(carousel_complete=complete,status='complete_pending_owner_review' if complete else 'incomplete_after_retries',archive=cid+'-1080x1350.zip')
    if complete:
        m.update(batch_status='carousel_complete',next_action='Continue next BATCH-H carousel without review pause. Owner reviews at end.')
    m['missing_slides']=[s['slide'] for s in m['slides'] if s['save_status']!='saved_to_repository_checkout']
    m['retry_policy']={'max_additional_attempts':2,'max_total_attempts':3,'continue_after_exhaustion':True,'owner_directive':'2026-10-30'}
    m['next_action']='Continue next assigned BATCH-H carousel. Preserve missing slides for later recovery; no review pause.'
    m['remote_save'].update(status='commit_and_push_requested',commit_lookup='git log -1 -- carousels/'+cid+'/manifest.json')
    write(m)
    (root/'handoff.md').write_text(f"# {cid} — BATCH-H\n\nSaved {m['generated_images']}/{len(m['slides'])} opaque RGB 1080x1350 slides from frozen copy v{m['content_version']}. Original Harda logo composited with own alpha, no patch. Caption verbatim. Actual prompts, source references, tool attempts, returned paths, errors and export status are in manifest.json.\n\nWhen generated, the ending must use original S1 phone/hand/real UI pixels at 1:1 below the measured text boundary with a 50px gap. An ungenerated ending is not claimed as saved.\n\nStatus: {m['status']}. agent_visual_review=not_performed; user_review=pending. No OCR, visual QA or reviewer pass. At most two additional attempts after failure; successful slides are never automatically regenerated.\n\nNext slide: {m['next_slide_to_generate']}. {m['next_action']}\n")
    with zipfile.ZipFile(root/m['archive'],'w',compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob('*')):
            if path.is_file() and path.suffix!='.zip' and '__pycache__' not in path.parts:
                archive.write(path,path.relative_to(root))
    print(json.dumps(dict(carousel=cid,complete=complete,archive=m['archive'])))
else:
    raise ValueError('Use init/start/save/error/package')
