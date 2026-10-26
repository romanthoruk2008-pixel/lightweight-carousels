import json, sys, shutil, subprocess
from pathlib import Path
from datetime import datetime, timezone
from zipfile import ZipFile, ZIP_DEFLATED
from PIL import Image, ImageOps
import numpy as np
ROOT=Path('/workspace/lightweight-carousels')
COMMON='''Create ONE finished Harda S2 portrait carousel slide, 1080 x 1350, 4:5. Precisely match supplied owner-approved S2 references for the very heavy tight lowercase grotesk headlines, clean regular sans body, regular italic grey subtitle, flat coral markers, and realistic WHITE/LIGHT-GREY anatomy mannequin: adult athletic, bald and faceless, fine grey shading, opaque black #2A2A2A shorts, smooth featureless pelvis. Equipment black/grey. No sand/green muscle colors. Highlight only the muscle groups expressly specified for this slide. Use references for DESIGN ONLY and replace ALL their words/poses with the exact instructions below. Solid opaque CLEAN #F0F1EB background, no arch, texture, dots or grid. Main text #2A2A2A, secondary #6B6B6B, coral #F26445, white #FFFFFF. Entire top 110px empty for the actual transparent Harda logo, to be composited afterward at x=48,y=19,size=218x71. Do not generate a logo, brand wordmark, watermark, signature, counter, progress bar, border, panels or additional text. Preserve every supplied word, number, capitalization, apostrophe, hyphen, punctuation and symbol exactly. Every line fully visible and separated from figures/equipment. Long headlines may wrap to two lines with a marker behind each line. No automatic changes to copy.\n\n'''
PHONE={'file':'production-assets/approved-phone-hand-strip.png','position':None,'placement':'Measured from final rendered body ink; minimum gap 40px, actual reserved gap50px. No fixed y.','source_file':'carousels/LW-CAR-0022/outputs/slide-19.png','source_crop':[0,720,1080,1350],'description':'Exact owner-approved S2 phone AND white hand pixels, original scale, original proportions, translated below measured text bottom +50px; no regenerated UI.'}
def ending(headline,body,markers):
    return 'PRODUCT ENDING — generate ONLY TEXT AND CLEAN BACKGROUND. Match approved ending typography, left alignment, marker bars and spacing, using ONLY the supplied words. Do NOT draw phone, hand, UI, icons, placeholders, frames, charts or any other objects. The exact approved real phone AND hand pixels will be inserted after measuring the actual rendered last body line. There is NO fixed phone height. Keep the headline compact and complete, around 80–95px heavy grotesk, below the empty logo area. EXACT headline with these line breaks:\n'+headline+'\nCoral marker bars behind ONLY these phrases: '+', '.join('`'+m+'`' for m in markers)+'. EXACT regular dark #2A2A2A body, around40–44px, below the headline with clear spacing, preserving every word, in these lines:\n'+body+'\nMake all body text fully visible and keep the remaining lower canvas empty off-white #F0F1EB. Prefer all text ending by y750, shrinking headline slightly if needed; never omit or crop text. We will measure actual text ink bounds and put the unscaled phone at least40px lower, allowing it to extend off the bottom. Return text/background only; do not reserve a fixed-height panel and do not imitate any screenshot.'

def prepare(car,details,note):
    folder=ROOT/'carousels'/car;c=json.loads((folder/'copy.json').read_text())
    if (folder/'manifest.json').exists():raise RuntimeError('Existing manifest: reconcile before preparing again')
    for sub in ('outputs','production-assets'):(folder/sub).mkdir(exist_ok=True)
    shutil.copy2(__file__,folder/'prompts/production.py')
    source=subprocess.run(['git','rev-parse','HEAD'],cwd=ROOT,capture_output=True,text=True,check=True).stdout.strip()
    slides=[];requests=[]
    for s in c['slides']:
        n=s['n'];detail,refs=details[n];prompt=COMMON+detail
        pf=f'prompts/slide-{n:02d}.txt';(folder/pf).write_text(prompt+'\n')
        slides.append({'slide':n,'content_version':c['content_version'],'role':s['role'],'exact_text':[t['string'] for t in s['text']],'file':f'outputs/slide-{n:02d}.png','prompt':prompt,'prompt_file':pf,'reference':refs,'attempts':[],'errors':[],'save_status':'not_generated','agent_visual_review':'not_performed','user_review':'pending'})
        requests.append({'n':n,'prompt':prompt,'refs':[str(ROOT/p) for p in refs]})
    d={'carousel_id':car,'content_version':c['content_version'],'source_commit':source,'branch':'claude/charming-einstein-xgejky','target_branch':'claude/charming-einstein-xgejky','batch':'G','batch_task':'carousels/BATCH-G.md','design_style':'S2','status':'in_progress','carousel_complete':False,'scope':{'total_slides':len(slides),'authorized_slides':list(range(1,len(slides)+1))},'reference_id':None,'reference_use':note,'font_family':c['font_family'],'background':'CLEAN #F0F1EB','logo':{'file':'assets/logo/harda-logo-full.png','position':[48,19],'size':[218,71],'old_lightweight_logo_used':False},'phone_composite':PHONE,'generated_images':[],'blocked_slides':[],'next_slide_to_generate':1,'approved_slides':[],'pending_review_slides':[],'user_review':'pending','agent_visual_review':'not_performed','next_action':'Generate the whole carousel without review stops, package, commit and push before starting the next Batch G carousel.','caption':'caption.txt','remote_save':{'status':'not_pushed','remote':'origin','branch':'claude/charming-einstein-xgejky'},'slides':slides}
    (folder/'manifest.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');(folder/'caption.txt').write_text(c['caption']['text']+'\n')
    with Image.open(ROOT/PHONE['source_file']) as im:im.crop(tuple(PHONE['source_crop'])).save(folder/PHONE['file'])
    return requests

def main():
    action,car=sys.argv[1:3];folder=ROOT/'carousels'/car;mp=folder/'manifest.json';d=json.loads(mp.read_text())
    def save():mp.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
    def now():return datetime.now(timezone.utc).isoformat()
    if action=='start':
        n=int(sys.argv[3]);s=d['slides'][n-1]
        if (folder/s['file']).exists():raise RuntimeError('Output already exists; do not repeat')
        s['attempts'].append({'attempt':len(s['attempts'])+1,'tool':'image_gen.imagegen','status':'in_progress','started_at':now(),'transparent_background':False,'referenced_image_paths':s['reference'],'prompt':s['prompt'],'prompt_file':s['prompt_file']});d['next_slide_to_generate']=n;save()
    elif action=='export':
        n=int(sys.argv[3]);raw=Path(sys.argv[4]);s=d['slides'][n-1];a=s['attempts'][-1];preserved=folder/f'production-assets/slide-{n:02d}-generated.png';shutil.copy2(raw,preserved)
        a.update(status='generation_succeeded_export_in_progress',raw_result_file=str(raw),preserved_raw_file=preserved.relative_to(folder).as_posix());save()
        with Image.open(raw) as im:
            raw_size=list(im.size);layer=ImageOps.contain(im.convert('RGBA'),(1080,1350),Image.Resampling.LANCZOS)
        canvas=Image.new('RGBA',(1080,1350),'#F0F1EB');canvas.alpha_composite(layer,((1080-layer.width)//2,(1350-layer.height)//2))
        if s['role']=='product ending':
            cfg=d['phone_composite']
            arr=np.asarray(canvas.convert('RGB'));rows=np.flatnonzero((arr.max(axis=2)<135).sum(axis=1)>5)
            if not len(rows):raise RuntimeError('No text ink for required phone placement measurement')
            body_bottom=int(rows[-1]+1);phone_top=body_bottom+50
            if phone_top>=1300:raise RuntimeError('Rendered text leaves no phone space; checkpoint raw result')
            cfg.update(position=[0,phone_top],body_ink_bottom_y=body_bottom,gap_px=50,measurement='Last dark text ink row on text-only plate, before phone/logo compositing. Required layout measurement only, no OCR or visual QA.')
            a['ending_placement']={'body_ink_bottom_y':body_bottom,'phone_layer_top_y':phone_top,'gap_px':50}
            with Image.open(folder/cfg['file']) as phone:canvas.alpha_composite(phone.convert('RGBA'),tuple(cfg['position']))
            a['post_generation_layers']=[cfg['description']]
        with Image.open(ROOT/'assets/logo/harda-logo-full.png') as logo:canvas.alpha_composite(logo.convert('RGBA').resize((218,71),Image.Resampling.LANCZOS),(48,19))
        output=folder/s['file'];canvas.convert('RGB').save(output)
        with Image.open(output) as im:
            if im.size!=(1080,1350) or im.mode!='RGB':raise RuntimeError('Required export metadata mismatch')
        a.update(status='succeeded',finished_at=now(),result_file=s['file'],export={'raw_size':raw_size,'uniform_fit_size':list(layer.size),'size':[1080,1350],'mode':'RGB','has_alpha':False,'logo':'Actual transparent Harda PNG x48,y19,218x71, own alpha, no backing patch.'})
        s['save_status']='saved_in_cloud_workspace';generated=[v for v in d['slides'] if (folder/v['file']).exists()];d.update(generated_images=[v['file'] for v in generated],pending_review_slides=[v['slide'] for v in generated],next_slide_to_generate=n+1 if n<len(d['slides']) else None);save();print(f'{car}: slide {n}/{len(d["slides"])} saved, 1080x1350 RGB, official Harda logo.')
    elif action=='fail':
        n=int(sys.argv[3]);err=sys.argv[4];s=d['slides'][n-1];s['errors'].append(err)
        if s['attempts']:s['attempts'][-1].update(status='interrupted',finished_at=now(),error=err)
        d.update(status='incomplete',carousel_complete=False,next_slide_to_generate=n,interruption={'slide':n,'error':err},next_action=f'Stop Batch G after pushing checkpoint. Resume slide {n} only after reconciling raw and exported files; no automatic retry.');save()
    elif action=='package':
        complete=sys.argv[3]=='complete';generated=[v for v in d['slides'] if (folder/v['file']).exists()]
        if complete and len(generated)!=len(d['slides']):raise RuntimeError('Missing outputs')
        d.update(status='complete' if complete else 'incomplete',carousel_complete=complete,user_review='pending',agent_visual_review='not_performed',archive=f'{car}-1080x1350.zip',generated_images=[v['file'] for v in generated],pending_review_slides=[v['slide'] for v in generated])
        if complete:d.update(next_slide_to_generate=None,next_action='Owner reviews all generated slides at the end of Batch G.')
        for s in generated:s['save_status']='pushed_to_target_branch'
        d['remote_save']={'remote':'origin','branch':'claude/charming-einstein-xgejky','status':'pushed_to_target_branch','method':'Complete carousel commit and immediate push under BATCH-G.md.' if complete else 'Immediate incomplete checkpoint after interruption.','commit_lookup':f'git log -1 -- carousels/{car}/manifest.json'}
        d['export_format']={'images':len(generated),'width':1080,'height':1350,'mode':'RGB','alpha':False,'check':'Required export metadata only; no visual QA, OCR or automatic regeneration.'};save()
        (folder/'handoff.md').write_text(f'# {car}\n\nBatch G: {len(generated)}/{len(d["slides"])} generated from copy.json v{d["content_version"]}.\nStatus: {d["status"]}; user_review=pending; agent_visual_review=not_performed.\nNext action: {d["next_action"]}\nOpaque 1080x1350 RGB; official Harda logo as transparent layer.\nEnding: {d["phone_composite"]["description"]}\n')
        archive=folder/d['archive']
        with ZipFile(archive,'w',compression=ZIP_DEFLATED,compresslevel=6) as z:
            for path in sorted(folder.rglob('*')):
                if path.is_file() and path.suffix!='.zip':z.write(path,path.relative_to(folder).as_posix())
        print(f'{car}: {d["status"]}, {len(generated)} slides; ZIP {archive.stat().st_size} bytes.')
    else:raise RuntimeError('Unknown action')
if __name__=='__main__':main()
