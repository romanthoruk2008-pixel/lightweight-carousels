# Series rules for every Lightweight carousel (Codex)

Read this before any `carousels/LW-CAR-XXXX/prompts/codex-task.md`. The task file adds that carousel's slides. If the two ever disagree, the task file and its `copy.json` win.

## Goal
Reproduce the assigned reference carousel 1:1: same slides, order, text, layout, illustrations, poses and equipment. Change only what is listed under "Substitutions". Do not add, remove, rewrite or "improve" anything, including copy that looks wrong. Owner decision: the source's spelling, grammar and debatable fitness claims stay exactly as they are.

## Series master
The approved slides of LW-CAR-0001 (`carousels/LW-CAR-0001/outputs/slide-01.png` … `slide-08.png`, warm-sand version). Match them for colors, Rubik type, the Lightweight wordmark (size and top-left position), illustration style, line weights and the phone ending. Take each slide's **layout** from the assigned reference, because different references are laid out differently.

## Reference images
Each task file lists the reference slide URLs in the **real** order. Use that order, not the order in `references/CAROUSELS.md`. The images are TikTok web-viewer screenshots. The slide is the tall off-white image on the left. Ignore all TikTok UI: the search bar "Знайти схожий контент", the arrows and dots at the bottom, and the dark right panel. The bottom few percent of a slide can be hidden behind the pager, so keep all labels fully visible in your version. Before generating, open the images and confirm you can see them. If you cannot, stop and tell the owner exactly which slide failed. Do not guess.

## Substitutions (approved palette, 2026-10-18)
- Everything bright green in the source → accent **#F26445**. That covers highlighted target muscles, accent words in headlines, "#N" numbers and number badges, short underline bars, dividers, arrows, "OR" badges and "Bonus Tip".
- **Background (owner decision 2026-10-19): no arch.** The big pale arch from the references and from our older slides is the competitor's signature shape, so it is dropped. When a template slide shows the arch, ignore it. Each task file names one of four backgrounds, and the whole carousel uses it. The texture sits behind everything (text, figures, phone):
  - `GRID`: background #F0F1EB with thin grid lines #E1E2DA, 2 px, every 54 px across the whole slide, like a training-log notebook.
  - `DOTS`: background #F0F1EB with small dots #D4D4CC, 6 px diameter, every 45 px.
  - `CLEAN`: plain #F0F1EB, nothing else.
  - `PLATES`: background #F0F1EB with three concentric rings in #EAE0D6 (stroke 26 / 22 / 18 px, radius 520 / 400 / 280 px) centred near the bottom-right corner (x 1010, y 1290), mostly off the canvas, like a weight plate.
  - **Every background is solid and opaque.** First fill the whole 1080 × 1350 canvas with the solid colour **#F0F1EB** (the same off-white as the GRID slides). Then draw the dots / grid lines / rings on top of it. Never leave the background transparent, and never draw a grey-and-white checkerboard (that is how transparency looks in editors). TikTok does not accept transparent images.
  - **Export check before saving:** every PNG must be flattened RGB with no alpha channel and no transparent pixels. If the image tool returns an image with transparency, put it on a solid #F0F1EB layer and flatten it before saving. This applies to the file in `outputs/`, to the ZIP and to anything you show the owner.
  - No progress bar or slide counter on any background.
  - Already generated carousels with the arch (LW-CAR-0001…0010, 0012, 0013) stay as they are. Do not repaint their backgrounds.
- Non-highlighted muscles → warm sand **#D9CBBE**, with darker shades of the same sand for shading. No green or sage tint anywhere on the figures. Skin and tendons light ivory (about #F5F0E5). Fine grey linework.
- **Figure (owner decision 2026-10-19), from LW-CAR-0020 on:** a realistic **white / light-grey** anatomical mannequin (bald, faceless, featureless smooth pelvis, fine grey shading), shorts #2A2A2A, as in REF-008. Target muscles #F26445 only where the task file asks for them. Never mix the white figure and the sand figure in one carousel. Carousels already generated with the sand figure stay as they are.
- Text: dark **#2A2A2A**, grey body **#6B6B6B**, white **#FFFFFF** on badges.
- Font: **Rubik** for all text. Covers use the heaviest weight, titles bold, body regular. Rubik is wider than the sources' condensed cover font. Keep the same line breaks, scale to fit, and tell the owner if a layout cannot match. Never shorten text.
- The Lightweight wordmark goes small in the top-left of every slide, exactly as on LW-CAR-0001, from the owner's wordmark file. Never draw or invent a logo.
- **Logo file (2026-10-19):** the full logo (wordmark + app icon) is `assets/logo/lightweight-logo-full.png` (transparent PNG). Place it top-left at x 48, y 19, 341 x 71 px on a 1080 x 1350 slide, as on LW-CAR-0014. Insert the file as a layer; never redraw it. Paste it with its own transparency only: no background box or patch under it. Keep the top 110 px of every slide free of other text, pills and badges so nothing touches the logo.
- The brand name "Arrow" in slide text → "Lightweight", only where the task file says so.

## Product ending (phone slides)
- The phone shows a **real Lightweight screenshot** the owner supplied. It is never generated, redrawn or imitated UI.
- Default screen: the same Progress / "Muscle balance" screenshot used in the approved LW-CAR-0001 slide 8, unless the task file or the owner gives another one.
- Keep the screenshot's original proportions and scale it evenly. The phone is a naturally tall real phone held by the sketch-style line-art hand, and it may run off the bottom edge. Never squash the screen to fit it all in (owner feedback on LW-CAR-0001).
- If you cannot insert the real screenshot cleanly, say so instead of faking it.

## Format and saving
- 1080 × 1350 px PNG per slide, `carousels/LW-CAR-XXXX/outputs/slide-01.png`, `slide-02.png` … in slide order.
- Text must be exactly the strings in copy.json: no extra words, no added punctuation (for example no period after a title that has none), no watermarks or signatures.
- Every line of text must be fully visible, never clipped by the phone, an illustration or the slide edge. If something does not fit, move or shrink the illustration or phone, never the text.
- Commit **one carousel = one commit**: all slides, prompts, `manifest.json`, `caption.txt`, ZIP. If a limit interrupts you, push what exists marked incomplete and record the next slide to generate.
- Manifest per slide: prompt, result file, attempts, errors, save status. Set `agent_visual_review` to `not_performed` and `user_review` to `pending`. Mark `approved` only after the owner says so.
- No automatic QA, OCR, reviewer passes or automatic regenerations. Redo a slide only when the owner asks, and only that slide.
- Slides marked BLOCKED in the task file wait for the owner. Generate everything else.
