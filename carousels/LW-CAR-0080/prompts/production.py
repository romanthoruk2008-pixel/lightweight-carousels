"""Batch J production and exact-file layers; no visual QA or OCR; at most two additional failure attempts."""
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
        raise RuntimeError('Reconcile existing results before starting; never overwrite')
    copy=json.loads((root/'copy.json').read_text())
    task=(root/'prompts/codex-task.md').read_text()
    if copy['design_style']!='S2': raise RuntimeError('Batch J requires S2')
    (root/'outputs').mkdir(exist_ok=True);(root/'production-assets').mkdir(exist_ok=True)
    shutil.copyfile(__file__,root/'prompts/production.py')
    previous=repo/'carousels/LW-CAR-0069/production-assets/approved-phone-hand-foreground.png'
    previous_manifest=json.loads((repo/'carousels/LW-CAR-0069/manifest.json').read_text())
    shutil.copyfile(previous,root/'production-assets/approved-phone-hand-foreground.png')
    source_phone=previous_manifest['phone_source']
    layout_sections=re.findall(r'^## (?:Layouts?|Item slide layout)[^\n]*\n.*?(?=^## |\Z)',task,flags=re.M|re.S)
    shared_layout='\n'.join(layout_sections)
    ending_section=re.search(r'^### Ending[^\n]*\n.*?(?=^## |\Z)',task,flags=re.M|re.S)
    if ending_section is None: raise RuntimeError('Read missing ending instructions before generating')
    common='''Produce ONE Harda S2 fitness carousel slide, portrait for final opaque RGB PNG export1080x1350. Approved reference images supply DESIGN ONLY: extremely heavy tightly spaced lowercase grotesk headlines, coral#F26445 marker bars behind the lower half of requested headline words, dark#2A2A2A clean regular body text, regular italic grey#6B6B6B sets/subtitle lines. Solid opaque CLEAN#F0F1EB background with NO texture, arch, gradient, progress bar, slide counter, watermark or signature. Do not use the sand S1 figure or uppercase Rubik design.
Keep the top110px completely empty of foreground: no logo, icon, text, badges or figures there. The original transparent Harda logo PNG is composited later at x48,y19,size218x71, own alpha with no patch. Do not draw a wordmark or logo.
S2 figures: adult nonhuman WHITE/LIGHT-GREY realistic anatomical teaching mannequins, bald faceless heads, fine grey shading, smooth featureless pelvis. Every figure wears opaque loose charcoal#2A2A2A gym shorts fully covering hips. Show only neutral standing poses or the assigned exercise, never a close physique pose. Equipment plain black/grey with no readable labels. Highlight muscles coral ONLY when the current task row explicitly requests it; otherwise all muscles white/light-grey. Do not copy reference poses, exercise choices or muscle highlights.
All visible words must be the EXACT current-slide copy.json strings below. Preserve lowercase, hyphens, curly apostrophes, colons, question marks, commas and periods exactly. No words, stars, ratings or label lines from references unless explicitly present in the current copy. Every line fully visible within safe margins, separate from figures; long labels may wrap but never shorten text. Generate only this one requested slide, not all layouts or slides described in context.
'''
    entries=[]
    for s in copy['slides']:
        n,role=s['n'],s['role']
        row=next((line for line in task.splitlines() if re.match(r'\|\s*'+str(n)+r'\s*\|',line)),None)
        if row is None: raise RuntimeError(f'Missing exact task row {n}')
        illustration=s.get('illustration',row.split('|')[-2].strip())
        if role=='hook':
            refs=['carousels/LW-CAR-0022/outputs/slide-01.png']
            detail='COVER: use the centered heavy lowercase lines, coral marker on the specified line and italic subtitle of the cover reference, with the CURRENT exercise/neutral figure below. Preserve explicit headline lines from copy.json and all words. Current task table row:\n'+row
        elif role=='product ending':
            refs=['carousels/LW-CAR-0022/outputs/slide-19.png']
            detail=ending_section.group(0)+'''\nEXACT-PIXEL ASSEMBLY: generate ONLY the headline and body on the plain clean background. NO phone, hand, app UI, chart, icon, mockup or placeholder. Ignore the phone in the supplied reference during generation. Original phone/white-hand/real Muscle balance pixels are composited later at unchanged1:1 scale, below the MEASURED last text row with50px gap. Headline begins below y150, comfortably wraps to3–5 lines when needed; body regular dark below, every word complete, all text comfortably above y900. Below the last line leave empty plain background. Never generate or redraw UI, and never put the phone at a fixed height.'''
        elif role=='checklist':
            refs=['carousels/LW-CAR-0029/outputs/slide-02.png','carousels/LW-CAR-0022/outputs/slide-01.png']
            detail='CHECKLIST: two-line heavy lowercase title top-left with marker behind line2 ONLY. Bullets left-aligned with generous line spacing: 1x bold coral, muscle phrase bold dark, bracket phrase regular grey. Big white figure bottom-right, cropped at right/bottom as specified. Keep figure clear of all text. Current task row:\n'+row
        elif role.startswith('slot'):
            refs=['carousels/LW-CAR-0029/outputs/slide-02.png','carousels/LW-CAR-0022/outputs/slide-03.png']
            detail='SLOT: unhighlighted dark #N before the heavy lowercase headline with coral marker behind HEADLINE ONLY. Sets line italic regular grey below; then the exact sentence in regular dark. Lower55%: TWO white exercise figures SIDE BY SIDE, separated by a thin vertical CORAL LINE, each with its exact bold lowercase label underneath. NO coral muscles on these exercise figures. No OR or vs badge, stars, extra anatomy inset or label line. Preserve left/right exercise order. Current task row:\n'+row
        else:
            refs=['carousels/LW-CAR-0029/outputs/slide-02.png','carousels/LW-CAR-0052/outputs/slide-02.png'] if any(t['string']=='do:' for t in s['text']) else ['carousels/LW-CAR-0029/outputs/slide-02.png','carousels/LW-CAR-0022/outputs/slide-03.png']
            detail='CURRENT SLIDE TYPE: '+role+'. Follow only its applicable layout from the task context below. Use ONLY the current exact copy; do not add a fix:, do:, star row or badge if absent from copy. Figures/props and left/right order are exactly this task table row:\n'+row
        prompt=common+'\nTASK LAYOUT CONTEXT (use only the applicable current-slide layout):\n'+shared_layout+'\n\nCURRENT SLIDE:\n'+detail+'\n\nAUTHORITATIVE EXACT COPY AND STYLES:\n'+'\n'.join(json.dumps(t,ensure_ascii=False) for t in s['text'])+'\nReturn one complete slide, no variants.\n'
        pf=f'prompts/slide-{n:02d}.txt';(root/pf).write_text(prompt)
        entries.append(dict(slide=n,role=role,content_version=copy['content_version'],exact_text=[t['string'] for t in s['text']],file=f'outputs/slide-{n:02d}.png',prompt_file=pf,references=refs,illustration=illustration,attempts=[],errors=[],save_status='not_started',agent_visual_review='not_performed',user_review='pending'))
    m=dict(carousel_id=cid,content_version=copy['content_version'],source_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),batch='BATCH-J',batch_status='running',design_style='S2',background='CLEAN',brand='Harda',status='in_progress',carousel_complete=False,generated_images=0,next_slide_to_generate=1,next_action='Generate all assigned slides in order with at most two additional attempts after failure; package/commit/pull --rebase/push each carousel and continue Batch J.',agent_visual_review='not_performed',user_review='pending',logo=dict(file='assets/logo/harda-logo-full.png',placement=[48,19,218,71],method='original PNG with own alpha; no backing patch'),phone_source=dict(**source_phone,retained_foreground='carousels/LW-CAR-0069/production-assets/approved-phone-hand-foreground.png'),remote_save=dict(remote='origin',branch='claude/charming-einstein-xgejky',status='not_yet_pushed'),slides=entries)
    (root/'caption.txt').write_text(copy['caption']['text']+'\n');write(m)
    print(json.dumps(dict(carousel=cid,slides=len(entries),style='S2',batch='BATCH-J')))
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
                correction = 'Use an adult nonhuman sports teaching mannequin fully dressed in an opaque light-grey long-sleeve athletic top and full-length charcoal sports leggings. All hips, torso and legs are covered by fabric. Show specified target muscles only as flat coral instructional patches ON TOP OF CLOTHING. Preserve the exact specified exercise, neutral side/front view, layout, S2 white/light-grey linework/palette and every word. No exposed anatomical body or realistic skin.'
            else:
                correction = 'Use a simple neutral sports-instruction drawing of a faceless adult plastic figurine in a fully covering opaque light-grey tracksuit, full-length trousers and athletic shoes, with simplified joints and fine grey outlines. Use a flat coral patch on the clothing for the specified muscle target. Keep the same requested ordinary gym movement and equipment, shown neutrally from the side, the same layout and ALL exact copy. No exposed anatomy or skin. This is an exercise diagram, not a realistic human body.'
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
        m.update(batch_status='carousel_complete',next_action='Continue next BATCH-J carousel without review pause. Owner reviews at end.')
    m['missing_slides']=[s['slide'] for s in m['slides'] if s['save_status']!='saved_to_repository_checkout']
    m['retry_policy']={'max_additional_attempts':2,'max_total_attempts':3,'continue_after_exhaustion':True,'owner_directive':'2026-10-30'}
    m['next_action']='BATCH-J generation complete; owner reviews returned results. Do not start unassigned batches.' if cid=='LW-CAR-0084' and complete else 'Continue next assigned BATCH-J carousel. Preserve missing slides for later recovery; no review pause.'
    m['remote_save'].update(status='commit_and_push_requested',commit_lookup='git log -1 -- carousels/'+cid+'/manifest.json')
    write(m)
    (root/'handoff.md').write_text(f"# {cid} — BATCH-J\n\nSaved {m['generated_images']}/{len(m['slides'])} opaque RGB 1080x1350 slides from frozen copy v{m['content_version']}. Original Harda logo composited with own alpha, no patch. Caption verbatim. Actual prompts, source references, tool attempts, returned paths, errors and export status are in manifest.json.\n\nWhen generated, the ending must use original S2 phone/hand/real UI pixels at 1:1 below the measured text boundary with a 50px gap. An ungenerated ending is not claimed as saved.\n\nStatus: {m['status']}. agent_visual_review=not_performed; user_review=pending. No OCR, visual QA or reviewer pass. At most two additional attempts after failure; successful slides are never automatically regenerated.\n\nNext slide: {m['next_slide_to_generate']}. {m['next_action']}\n")
    with zipfile.ZipFile(root/m['archive'],'w',compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob('*')):
            if path.is_file() and path.suffix!='.zip' and '__pycache__' not in path.parts:
                archive.write(path,path.relative_to(root))
    print(json.dumps(dict(carousel=cid,complete=complete,archive=m['archive'])))
else:
    raise ValueError('Use init/start/save/error/package')
