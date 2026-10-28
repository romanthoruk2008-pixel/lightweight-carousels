"""Batch H production: exact copy, one image_gen attempt per slide, cloud saves.

The required ending placement uses a raster ink boundary solely for compositing.
No OCR, content evaluation, visual QA, reviewer pass or regeneration is run.
"""
import json
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

def task_row(n):
    for line in (root / 'prompts/codex-task.md').read_text().splitlines():
        cells = [x.strip() for x in line.split('|')[1:-1]]
        if cells and cells[0] == str(n):
            return cells
    raise RuntimeError(f'Missing task table row {n}')

if action == 'init':
    if mp.exists() or list((root / 'outputs').glob('*.png')):
        raise RuntimeError('Existing manifest/output requires reconciliation; never overwrite blindly')
    copy = json.loads((root / 'copy.json').read_text())
    (root / 'outputs').mkdir(exist_ok=True)
    (root / 'production-assets').mkdir(exist_ok=True)
    shutil.copyfile(__file__, root / 'prompts/production.py')
    with Image.open(repo / 'carousels/LW-CAR-0022/outputs/slide-19.png') as source:
        source.crop((0,720,1080,1350)).save(root / 'production-assets/approved-phone-hand-strip.png')
    common = '''Produce ONE 1080 x 1350 portrait fitness carousel slide for Harda. Attached owner-approved images are the visual templates, not the text source. Match S2 exactly: extremely heavy tight lowercase grotesk headlines #2A2A2A; flat coral #F26445 marker behind the LOWER part of headline words only; clean regular dark body type; secondary subtitle italic regular #6B6B6B. Solid opaque CLEAN #F0F1EB, no texture, arch, panel, gradient, slide counter, watermark or extra copy. Leave the top 110 pixels entirely EMPTY background: generate NO logo or wordmark; the ORIGINAL Harda PNG is inserted at x48,y19,218x71 later using its own alpha, no patch. Mannequin is a realistic WHITE/LIGHT-GREY nonhuman anatomical teaching model, bald, smooth faceless head, fine grey shading/muscle fibres, opaque loose charcoal #2A2A2A athletic shorts with full coverage. Other clothing only when explicitly required by this slide. Equipment black/grey. Same rendering as the references, not beige, cartoon or clay. Preserve every exact string below, curly quotes, case, apostrophes and punctuation. Only the requested strings may be visible; no extra words or equipment labels. All text completely readable within slide edges; keep figure below text.\n'''
    entries = []
    for s in copy['slides']:
        n = s['n']; role = s['role']; row = task_row(n)
        texts = [t['string'] for t in s['text']]
        styles = '\n'.join(json.dumps(t,ensure_ascii=False) for t in s['text'])
        illustration = s.get('illustration', row[-1])
        if role == 'hook':
            refs = ['carousels/LW-CAR-0022/outputs/slide-01.png']
            layout = 'COVER: copy the centered two-line heavy headline, second-line coral marker, italic centered subtitle, and large lower figure proportions of the cover reference. Keep the explicit two headline lines from copy, scale a long line to fit rather than shorten it. Figure: ' + illustration
        elif 'tier divider' in role:
            refs = ['carousels/LW-CAR-0049/outputs/slide-02.png', 'carousels/LW-CAR-0022/outputs/slide-02.png']
            color = dict(F='#5BDCE3',C='#3FCF5E',B='#FFD95A',A='#FF9A52',S='#F26445')[texts[0]]
            layout = f'TIER DIVIDER: same centered layout, spacing, proportions and typography as attached divider. Rounded square tile {color}, huge white bold letter {texts[0]} with soft shadow, large black tier beside it; italic regular grey subtitle centered below. No figure, equipment, stars or marker strips.'
        elif role == 'product ending':
            refs = ['carousels/LW-CAR-0022/outputs/slide-19.png']
            layout = '''PRODUCT ENDING: use reference only for its exact typography, marker style and left-aligned hierarchy. Generate ONLY headline and body on plain background. Do NOT generate any phone, screen, app UI, hand, chart, icon or other object, even a placeholder. Original phone/real UI/white hand bitmap is inserted later at unchanged 1:1 proportions. Headline begins x60 about y150, heavy lowercase, marker only under the phrases specified in text styles. Allow 3–5 readable lines around 85–100 px size as necessary. Body regular dark about 38–42 px below headline, fully visible; keep entire text comfortably above y850 so there is room below. Everything after the final body line must be completely empty uniform #F0F1EB, no decoration or shadows. Production measures the lowest text-ink row and puts the original phone below that measured boundary with at least 40px gap, NEVER at a fixed height. Include every word of body text. Do not reproduce old reference text.'''
        elif 'rating_stars' in s:
            refs = ['carousels/LW-CAR-0053/outputs/slide-03.png', 'carousels/LW-CAR-0049/outputs/slide-03.png']
            layout = f'''RANKED ITEM: exact attached item layout, number unhighlighted followed by the name with coral marker. Long name can wrap with marker per line. Body regular dark up to two lines below the star row. Exactly five five-point stars: rating {s['rating_stars']} of 5; filled coral #F26445, empty #D6D6D2; a half rating is half filled. Lower ~55% a big figure and only the required props. Minimal setting hints, never a room filling the background. Figure: {illustration}. Highlight a muscle only if the task figure explicitly specifies it; otherwise none.'''
        else:
            refs = ['carousels/LW-CAR-0029/outputs/slide-02.png']
            layout = f'''ITEM: same left-aligned headline/body/figure layout as attached item template. Number or stage label precedes headline; marker behind HEADLINE ONLY. Stage labels small bold coral; numbers bold dark. Body regular dark, up to two lines. Add a small bold coral 'do:' line followed by regular exercise text ONLY if present in exact copy; do not copy the reference's 'fix:' or 'do:' if this slide does not have it. NO STARS. Long headline may wrap to two lines with marker under each. Lower ~55% a large figure with equipment/props: {illustration}.'''
        if cid == 'LW-CAR-0056' and role != 'product ending' and 'tier divider' not in role:
            layout += ' MUSCLE HIGHLIGHT: fill only the target muscle group(s) #F26445 exactly as this task-table figure says: ' + row[-1] + '. Everything else on the white mannequin stays white/light-grey. Charcoal opaque shorts remain fully covering the pelvis.'
        elif role != 'product ending':
            layout += ' No coloured muscles; ignore all muscle colours on references. Charcoal shorts stay opaque and loose. Only the specified props and gestures.'
        if cid == 'LW-CAR-0057' and role != 'product ending':
            symbols = ['♈','♉','♊','♋','♌','♍','♎','♏','♐','♑','♒','♓']
            if role == 'hook':
                layout += ' Draw twelve small simple coral astrological LINE ICONS in a ring around the head: ' + ' '.join(symbols) + '. Never emoji or coloured emoji tiles.'
            else:
                layout += ' Beside this sign name draw its simple solid coral astrological LINE ICON: ' + symbols[n-2] + '. Draw a line symbol; never emoji.'
        layout += ' NO music notes or musical-note symbols: none are specified for these remaining carousels. Do not inherit music notes, clothing, bubbles, old words or extra figures from references. Props, food packages, cans, bars, shakers, calendar pages, headphone shells and equipment are PLAIN, no logos, brand names or readable labels. Only clock faces explicitly named by this task may carry time markings. Food on 0060 remains recognisable, with restrained natural food colours on plain plates; mannequin stays white.'
        prompt = common + '\n' + layout + '\n\nAUTHORITATIVE TEXT AND STYLES FROM copy.json:\n' + styles + '\n\nReturn one complete opaque slide, not a contact sheet.\n'
        pf = f'prompts/slide-{n:02d}.txt'; (root/pf).write_text(prompt)
        entries.append(dict(slide=n,content_version=copy['content_version'],role=role,exact_text=texts,
            file=f'outputs/slide-{n:02d}.png',prompt_file=pf,references=refs,
            illustration=illustration,rating_stars=s.get('rating_stars'),attempts=[],errors=[],
            save_status='not_started',agent_visual_review='not_performed',user_review='pending'))
    m = dict(carousel_id=cid,content_version=copy['content_version'],source_commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
        batch='BATCH-H',batch_status='running',instructions='prompts/codex-task.md',design_style='S2',brand='Harda',
        status='in_progress',carousel_complete=False,generated_images=0,next_slide_to_generate=1,
        next_action='Generate every slide in order; commit and push this carousel immediately when complete, then continue next Batch H carousel. Stop and push on any error/limit.',
        agent_visual_review='not_performed',user_review='pending',
        logo=dict(file='assets/logo/harda-logo-full.png',x=48,y=19,width=218,height=71,method='original file composited with own alpha, no backing patch'),
        remote_save=dict(remote='origin',branch='claude/charming-einstein-xgejky',status='not_yet_pushed'),slides=entries)
    (root/'caption.txt').write_text(copy['caption']['text']+'\n'); write(m)
    print(json.dumps(dict(carousel=cid,count=len(entries))))
    sys.exit()

m = json.loads(mp.read_text())
if action in ['start','save','error']:
    n = int(sys.argv[3]); s = next(s for s in m['slides'] if s['slide']==n)
    if action == 'start':
        if s['attempts'] or s['save_status'] != 'not_started':
            raise RuntimeError('No automatic retry or overwrite of existing output')
        s['save_status']='generation_in_progress'
        s['attempts'].append(dict(attempt=1,tool='image_gen.imagegen',status='in_progress',started_at=now,
            prompt_file=s['prompt_file'],transparent_background=False,
            referenced_image_paths=[str(repo/r) for r in s['references']]))
    elif action == 'save':
        raw_path = Path(sys.argv[4])
        with Image.open(raw_path) as raw:
            raw_meta=dict(size=list(raw.size),mode=raw.mode)
            im=Image.new('RGBA',raw.size,'#F0F1EB');im.alpha_composite(raw.convert('RGBA'))
            im=im.resize((1080,1350),Image.Resampling.LANCZOS)
        if s['role']=='product ending':
            shutil.copyfile(raw_path,root/'production-assets/ending-generated-text.png')
            # Layout measurement explicitly required by BATCH-H; no recognition or review.
            ink=im.convert('L').point(lambda v:255 if v<190 else 0).crop((0,110,1080,1350))
            bounds=ink.getbbox()
            if not bounds:
                raise RuntimeError('Ending has no measurable text ink')
            text_bottom=110+bounds[3]
            phone_y=text_bottom+50
            if phone_y>=1300:
                raise RuntimeError('Ending text leaves insufficient space for phone placement')
            with Image.open(root/'production-assets/approved-phone-hand-strip.png') as phone:
                im.paste(phone.convert('RGBA'),(0,phone_y))
            s['phone_compositing']=dict(source='carousels/LW-CAR-0022/outputs/slide-19.png',
                source_commit=m['source_commit'],source_crop=[0,720,1080,1350],
                asset='production-assets/approved-phone-hand-strip.png',
                measured_text_bottom_exclusive=text_bottom,placement=[0,phone_y],minimum_gap=50,
                measurement='raster text-ink bounding extent on generated text-only plate; no OCR or visual QA',
                scale='1:1, no resampling',real_ui_generated=False)
        with Image.open(repo/'assets/logo/harda-logo-full.png') as logo:
            im.alpha_composite(logo.convert('RGBA').resize((218,71),Image.Resampling.LANCZOS),(48,19))
        output=root/s['file'];im.convert('RGB').save(output,format='PNG')
        with Image.open(output) as saved:
            if saved.size!=(1080,1350) or saved.mode!='RGB':raise RuntimeError('Expected opaque 1080x1350 RGB PNG')
        s['save_status']='saved_to_repository_checkout'
        s['attempts'][-1].update(status='succeeded',finished_at=now,raw_result_file=str(raw_path),raw_result_format=raw_meta,
            result_file=s['file'],export=dict(size=[1080,1350],mode='RGB',alpha=False,logo='original PNG, x48 y19, 218x71'))
    else:
        error=sys.argv[4];s['errors'].append(error);s['save_status']='interrupted'
        s['attempts'][-1].update(status='error',finished_at=now,error=error)
        m['status']='incomplete_interrupted';m['next_action']='Stop Batch H; push current progress immediately. Next slide: '+str(n)
    m['generated_images']=sum(s['save_status']=='saved_to_repository_checkout' for s in m['slides'])
    m['next_slide_to_generate']=next((s['slide'] for s in m['slides'] if s['save_status']!='saved_to_repository_checkout'),None)
    write(m)
    print(json.dumps(dict(carousel=cid,slide=n,action=action,saved=m['generated_images'],total=len(m['slides']))))
elif action=='package':
    complete=m['generated_images']==len(m['slides']);m['carousel_complete']=complete
    m['status']='complete_pending_owner_review' if complete else 'incomplete_interrupted'
    if complete:m['next_action']='Owner reviews all Batch H carousels at the end. Continue the next assigned carousel without review pause.'
    m['archive']=cid+'-1080x1350.zip'
    m['remote_save'].update(status='commit_and_push_requested',commit_lookup='git log -1 -- carousels/'+cid+'/manifest.json')
    write(m)
    (root/'handoff.md').write_text(f'''# {cid} — Batch H

Saved {m['generated_images']} of {len(m['slides'])} opaque 1080×1350 RGB PNGs from frozen copy.json v{m['content_version']}. Harda logo composited from original PNG, x48 y19, 218×71, own alpha, no backing patch. Caption verbatim. Actual prompts, input references, attempts, returned paths and errors recorded per slide in manifest.json.

Ending, if saved: generated text-only plate; final text-ink boundary measured solely for layout, then original 0022/19 phone/real UI/white-hand strip placed below it with 50px gap, at 1:1 scale, no UI generation or resampling. Actual measured coordinates recorded. No fixed phone height.

Status: {m['status']}. agent_visual_review=not_performed; user_review=pending. No visual QA, OCR, reviewer passes or automatic retries. Owner reviews after batch.

Next slide: {m['next_slide_to_generate']}. Next action: {m['next_action']}
''')
    with zipfile.ZipFile(root/m['archive'],'w',compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(root.rglob('*')):
            if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts:z.write(p,p.relative_to(root))
    print(json.dumps(dict(carousel=cid,complete=complete,archive=m['archive'])))
else:
    raise ValueError('Use init/start/save/error/package')
