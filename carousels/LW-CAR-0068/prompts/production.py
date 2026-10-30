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
    if mp.exists() or list((root/'outputs').glob('*.png')):
        raise RuntimeError('Reconcile existing results; never overwrite')
    copy=json.loads((root/'copy.json').read_text())
    task=(root/'prompts/codex-task.md').read_text()
    if copy['design_style']!='S1': raise RuntimeError('S1 required')
    (root/'outputs').mkdir(exist_ok=True)
    (root/'production-assets').mkdir(exist_ok=True)
    shutil.copyfile(__file__,root/'prompts/production.py')
    # Retain original approved phone/hand pixels; remove only external background.
    from PIL import ImageDraw
    phone_source='carousels/LW-CAR-0009/outputs/slide-08.png'
    with Image.open(repo/phone_source) as source:
        phone=source.convert('RGBA').crop((0,424,1080,1350))
        barrier=phone.convert('L').point(lambda v:0 if v<170 else 255)
        w,h=barrier.size
        for x in range(w):
            if barrier.getpixel((x,0))==255: ImageDraw.floodfill(barrier,(x,0),128)
        for y in range(h):
            for x in (0,w-1):
                if barrier.getpixel((x,y))==255: ImageDraw.floodfill(barrier,(x,y),128)
        alpha=barrier.point(lambda v:0 if v==128 else 255)
        phone.putalpha(alpha)
        bounds=alpha.getbbox()
        if bounds is None: raise RuntimeError('Empty original phone foreground')
        phone=phone.crop((0,bounds[1],1080,phone.height))
        phone.save(root/'production-assets/approved-phone-hand-foreground.png')
    backgrounds={
        'CLEAN':'plain solid background, nothing else',
        'GRID':'thin #E1E2DA grid lines, 2px every 54px, across the canvas',
        'DOTS':'#D4D4CC dots, 6px diameter every 45px across the canvas',
        'PLATES':'three #EAE0D6 rings, radii 520/400/280px, widths26/22/18px, centred x1010 y1290'}
    bg=copy['background']
    common=f'''Create ONE Harda S1 STRUCTURE-series fitness carousel slide, portrait for export at 1080x1350 opaque RGB. Attached approved LW-CAR-0009 slide gives the layout, sizes, type hierarchy, linework and S1 drawing style ONLY. REPLACE every word and exercise with the current authoritative copy and task details below.
BACKGROUND: solid opaque #F0F1EB FIRST, then {backgrounds[bg]}. This carousel uses {bg}. NO ARCH: completely remove the large pale pink arch visible on the OLD reference. No progress bar, slide counter, watermark, signature, gradient or checkerboard.
Leave the top110px empty of all text, figures, badges and logos. Do not draw any logo or wordmark: original transparent Harda PNG is composited later at x48,y19,size218x71 using its own alpha, without a backing patch.
S1 figure: adult bald faceless PLASTIC anatomical teaching mannequin, smooth featureless pelvis, fine grey linework, sand #D9CBBE muscle forms, ivory #F5F0E5 tendons, darker sand shading. Plain opaque sand gym shorts on all exercise/hip-visible figures. Target highlights coral #F26445 ONLY where this slide explicitly requests them; ordinary exercise figures all sand with no highlights. Equipment black/grey, plain and unlabelled. Keep the S1 style, never the white S2 mannequin. Neutral exercise instruction.
Rubik for ALL text: heaviest cover, bold headings, regular body and sets lines. Dark#2A2A2A, body grey#6B6B6B, coral#F26445. Copy EXACT case, punctuation, apostrophes, hyphens, x, plus signs and brackets from copy.json. No extra words from templates. Keep every line inside safe margins, fully visible and separate from illustrations. Long exercise labels may wrap, never shorten them.
'''
    sections=re.split(r'(?=^### )',task,flags=re.M)
    list_section=next((p for p in sections if p.startswith('### Slides 3')),None)
    if list_section is None: raise RuntimeError('Missing STRUCTURE list template')
    list_layout=list_section.split('| Slide |')[0]
    entries=[]
    for s in copy['slides']:
        n,role=s['n'],s['role']
        refs=[f'carousels/LW-CAR-0009/outputs/slide-{n:02d}.png']
        detail=next((p for p in sections if re.match(r'### Slide '+str(n)+r'\b',p)), '')
        if role.startswith('list item'):
            row=next(line for line in task.splitlines() if line.startswith(f'| {n} |'))
            detail=list_layout+'\nCurrent row columns: Slide | Number | Title | Sets line | Sentence | Left exercise/label | Right exercise/label\n'+row
            detail+='\nMatch the template: large coral #N top-left and coral underline under it; title and regular grey sets line to its right. Grey sentence below. Two exercise figures in the lower55%, separated by one THIN VERTICAL CORAL LINE, with labels underneath. No OR badge, circular number badge, close-up muscle inset or additional words. All exercise figures all sand with NO coral muscle highlights.'
        elif role=='product ending':
            detail='''PRODUCT ENDING TEXT PLATE: same left-aligned heading scale and short coral bar as the template. Render ONLY the two exact copy.json strings with their specified colors. First string dark #2A2A2A; second coral #F26445. Keep case, periods and every word. Wrap long headings neatly within safe margins below y150, comfortably above y800. DO NOT generate phone, hand, screen, app UI, chart or placeholder. Leave the entire lower foreground empty. The ORIGINAL approved phone/hand pixels from the reference are composited later at 1:1 scale below the measured last text row with a50px gap. The phone may extend off the bottom edge. No arch.'''
        if not detail: raise RuntimeError(f'Missing slide instructions {n}')
        prompt=common+'\nCURRENT SLIDE:\n'+detail+'\n\nAUTHORITATIVE EXACT COPY AND STYLES:\n'+'\n'.join(json.dumps(t,ensure_ascii=False) for t in s['text'])+'\nReturn one complete slide, no variants.\n'
        pf=f'prompts/slide-{n:02d}.txt';(root/pf).write_text(prompt)
        entries.append(dict(slide=n,role=role,content_version=copy['content_version'],exact_text=[t['string'] for t in s['text']],file=f'outputs/slide-{n:02d}.png',prompt_file=pf,references=refs,attempts=[],errors=[],save_status='not_started',agent_visual_review='not_performed',user_review='pending'))
    m=dict(carousel_id=cid,content_version=copy['content_version'],source_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),batch='BATCH-H',batch_status='running',design_style='S1',background=bg,brand='Harda',status='in_progress',carousel_complete=False,generated_images=0,next_slide_to_generate=1,next_action='Process slides in order with at most two additional attempts after failure, then package/commit/push and continue next assigned carousel.',agent_visual_review='not_performed',user_review='pending',logo=dict(file='assets/logo/harda-logo-full.png',placement=[48,19,218,71],method='original PNG with own alpha, no backing patch'),phone_source=dict(file=phone_source,crop=[0,424+bounds[1],1080,1350],scale='1:1',mask='External background flood-filled outside original dark silhouette; original foreground RGB unchanged; no UI generation'),remote_save=dict(remote='origin',branch='claude/charming-einstein-xgejky',status='not_yet_pushed'),slides=entries)
    (root/'caption.txt').write_text(copy['caption']['text']+'\n');write(m)
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
