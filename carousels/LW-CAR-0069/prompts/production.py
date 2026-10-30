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
    if copy['design_style']!='S2': raise RuntimeError('S2 required')
    (root/'outputs').mkdir(exist_ok=True);(root/'production-assets').mkdir(exist_ok=True)
    shutil.copyfile(__file__,root/'prompts/production.py')
    from PIL import ImageDraw
    phone_source='carousels/LW-CAR-0022/outputs/slide-19.png'
    with Image.open(repo/phone_source) as source:
        phone=source.convert('RGBA').crop((0,720,1080,1350))
        barrier=phone.convert('L').point(lambda v:0 if v<170 else 255)
        w,h=barrier.size
        for x in range(w):
            if barrier.getpixel((x,0))==255: ImageDraw.floodfill(barrier,(x,0),128)
        for y in range(h):
            for x in (0,w-1):
                if barrier.getpixel((x,y))==255: ImageDraw.floodfill(barrier,(x,y),128)
        alpha=barrier.point(lambda v:0 if v==128 else 255);phone.putalpha(alpha)
        bounds=alpha.getbbox()
        if bounds is None: raise RuntimeError('Empty original phone foreground')
        phone.crop((0,bounds[1],1080,phone.height)).save(root/'production-assets/approved-phone-hand-foreground.png')
    common='''Create ONE Harda S2 fitness carousel slide, portrait for final opaque RGB PNG export1080x1350. Attached owner-approved slides give only DESIGN: the same heavy tight lowercase grotesk, flat coral#F26445 marker behind lower half of headline words, dark#2A2A2A text, clean regular dark body type, italic regular grey#6B6B6B subtitles. Solid opaque CLEAN#F0F1EB background, no arch, texture, card behind text, gradient, slide counter, signature or watermark.
Keep top110px completely empty of foreground objects, text and logos. Do not draw any logo or wordmark: the exact original transparent Harda PNG is composited at x48,y19,size218x71 afterward, own alpha and no patch.
S2 mannequin is nonhuman, realistic WHITE/LIGHT-GREY, bald smooth faceless head, fine grey anatomical shading/linework, featureless smooth pelvis, opaque loose charcoal#2A2A2A shorts fully covering hips. Equipment black/grey. No sand/beige S1 figure, no coloured muscles, no clothing or decorative props inherited from reference. Only explicitly specified arrows or effect marks may be coral. Plain unlabelled props. Phones in exercise scenes show their BACK, never any screen or UI.
Preserve every exact string from copy.json including lowercase, curly apostrophes, commas, periods, colon, parentheses and hyphens. Render NO other words or numbers; never copy reference wording. All text fully visible within generous safe margins, keep figures below text. Long headline may wrap onto two lines, with a coral marker under each line; never abbreviate copy. No stars or rating icons, music notes, extra labels, OR badges or counters.
'''
    entries=[]
    for s in copy['slides']:
        n,role=s['n'],s['role']
        row=next(line for line in task.splitlines() if line.startswith(f'| {n} |'))
        illustration=s.get('illustration',row.split('|')[-2].strip())
        if role=='hook':
            refs=['carousels/LW-CAR-0022/outputs/slide-01.png']
            detail='COVER: centered very heavy two-line lowercase headline, marker on the second line, then centered italic grey parenthetical subtitle. Match cover reference proportions and hierarchy; replace ALL old words and its figure. Lower half: '+illustration+'. No coloured muscles or additional props.'
        elif role=='product ending':
            refs=['carousels/LW-CAR-0022/outputs/slide-19.png']
            detail='PRODUCT ENDING: render ONLY the exact headline and body on clean background. Left-aligned heavy lowercase headline below y150, coral marker bars ONLY on phrases specified in copy.json styles, regular dark body below. Every word complete, comfortably above y850, ample spacing. Do NOT generate any phone, hand, app UI, chart, icon or placeholder. Leave lower foreground entirely empty. The ORIGINAL white hand/phone/real Muscle balance screenshot pixels from the approved reference are composited at1:1 after measuring the bottom of actual text, with50px gap below it. Never imitate UI, squash the phone or position at a fixed height.'
        else:
            refs=['carousels/LW-CAR-0029/outputs/slide-02.png','carousels/LW-CAR-0052/outputs/slide-02.png']
            detail='ITEM: same layout every time. Unhighlighted heavy dark #N number precedes very heavy lowercase headline with coral marker behind HEADLINE ONLY. Regular dark body below. Then a small BOLD CORAL do: label followed by the exact tip in regular dark text, as in second reference. No fix: label, no words from references. Lower55%: big white S2 figure with only these required equipment/props: '+illustration+'. No coloured muscles. Keep ALL three text components clear of illustration and within edges.'
        prompt=common+'\nCURRENT SLIDE LAYOUT:\n'+detail+'\n\nAUTHORITATIVE EXACT COPY AND STYLES:\n'+'\n'.join(json.dumps(t,ensure_ascii=False) for t in s['text'])+'\nReturn one complete slide, not a contact sheet.\n'
        pf=f'prompts/slide-{n:02d}.txt';(root/pf).write_text(prompt)
        entries.append(dict(slide=n,role=role,content_version=copy['content_version'],exact_text=[t['string'] for t in s['text']],file=f'outputs/slide-{n:02d}.png',prompt_file=pf,references=refs,illustration=illustration,attempts=[],errors=[],save_status='not_started',agent_visual_review='not_performed',user_review='pending'))
    m=dict(carousel_id=cid,content_version=copy['content_version'],source_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),batch='BATCH-H',batch_status='running',design_style='S2',background='CLEAN',brand='Harda',status='in_progress',carousel_complete=False,generated_images=0,next_slide_to_generate=1,next_action='Process all slides with at most two additional attempts after failure, package/commit/push actual results, then complete BATCH-H.',agent_visual_review='not_performed',user_review='pending',logo=dict(file='assets/logo/harda-logo-full.png',placement=[48,19,218,71],method='original PNG with own alpha, no backing patch'),phone_source=dict(file=phone_source,crop=[0,720+bounds[1],1080,1350],scale='1:1',mask='External background flood-filled outside original dark silhouette; original foreground RGB unchanged; no UI generation'),remote_save=dict(remote='origin',branch='claude/charming-einstein-xgejky',status='not_yet_pushed'),slides=entries)
    (root/'caption.txt').write_text(copy['caption']['text']+'\n');write(m)
    print(json.dumps(dict(carousel=cid,count=len(entries),style='S2')))
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
        m.update(batch_status='carousel_complete',next_action='Continue next BATCH-H carousel without review pause. Owner reviews at end.')
    m['missing_slides']=[s['slide'] for s in m['slides'] if s['save_status']!='saved_to_repository_checkout']
    m['retry_policy']={'max_additional_attempts':2,'max_total_attempts':3,'continue_after_exhaustion':True,'owner_directive':'2026-10-30'}
    m['next_action']='BATCH-H generation complete; owner reviews returned results. Do not start unassigned batches.' if cid=='LW-CAR-0069' and complete else 'Continue next assigned BATCH-H carousel. Preserve missing slides for later recovery; no review pause.'
    m['remote_save'].update(status='commit_and_push_requested',commit_lookup='git log -1 -- carousels/'+cid+'/manifest.json')
    write(m)
    (root/'handoff.md').write_text(f"# {cid} — BATCH-H\n\nSaved {m['generated_images']}/{len(m['slides'])} opaque RGB 1080x1350 slides from frozen copy v{m['content_version']}. Original Harda logo composited with own alpha, no patch. Caption verbatim. Actual prompts, source references, tool attempts, returned paths, errors and export status are in manifest.json.\n\nWhen generated, the ending must use original S2 phone/hand/real UI pixels at 1:1 below the measured text boundary with a 50px gap. An ungenerated ending is not claimed as saved.\n\nStatus: {m['status']}. agent_visual_review=not_performed; user_review=pending. No OCR, visual QA or reviewer pass. At most two additional attempts after failure; successful slides are never automatically regenerated.\n\nNext slide: {m['next_slide_to_generate']}. {m['next_action']}\n")
    with zipfile.ZipFile(root/m['archive'],'w',compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob('*')):
            if path.is_file() and path.suffix!='.zip' and '__pycache__' not in path.parts:
                archive.write(path,path.relative_to(root))
    print(json.dumps(dict(carousel=cid,complete=complete,archive=m['archive'])))
else:
    raise ValueError('Use init/start/save/error/package')
