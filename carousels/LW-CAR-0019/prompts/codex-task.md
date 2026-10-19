# Codex task — LW-CAR-0019 "WEAK BACK?" — minimal figure style test

First read `carousels/CODEX-SERIES-RULES.md`. It covers palette, Rubik, the logo file, phone ending, format, saving, manifest, no added punctuation, no clipped text, and the **backgrounds** (solid and opaque, never transparent). Exact copy: `carousels/LW-CAR-0019/copy.json` (content_version 1.0, the same text as the approved LW-CAR-0001). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**This task overrides one series rule: the figure style.** The owner wants the **body drawn more minimally**. Everything else stays as on the approved LW-CAR-0001: the same slides, text, layout, type, colours, equipment, poses and the phone ending. The slides themselves do not get emptier; only the way the body is drawn changes.

**Background: `GRID`** on every slide: solid #F0F1EB first, then the grid lines. No arch: LW-CAR-0001 still shows the old arch, so ignore it.
**Logo:** the full logo file `assets/logo/lightweight-logo-full.png` top-left at x 48, y 19, 341 x 71 px, pasted with its own transparency only (no box or patch). Keep the top 110 px free of anything else, so the title block of slides 3–7 starts below y 110.

## Layout templates
Slide N of this carousel takes its layout, poses and equipment from `carousels/LW-CAR-0001/outputs/slide-0N.png` and its description in `carousels/LW-CAR-0001/prompts/codex-task.md` (section "Slides"). Only the figures are drawn differently.

## What stays in every variant
- The figure is the same bald, faceless male mannequin with a **featureless pelvis**, same proportions, same poses as on LW-CAR-0001. Athletic, natural build.
- The **target muscle is still the clearest thing on the figure**, filled flat **#F26445**. A viewer must see in one second which muscle the slide is about.
- Non-target body in warm sand **#D9CBBE** / light ivory (about #F5F0E5). No green or sage tint.
- Gym equipment stays recognisable but is simplified to match the figure (fewer details, same colours: black / grey / white).

## Step 1 — style test (do this first, then stop)
Generate **slide 1 and slide 3** in each of the three variants below: 6 images. Save them as `carousels/LW-CAR-0019/outputs/style-test/A-slide-01.png`, `A-slide-03.png`, `B-slide-01.png`, `B-slide-03.png`, `C-slide-01.png`, `C-slide-03.png` (1080 × 1350, flattened RGB). Commit the 6 images with their prompts and the manifest in one commit, then show them to the owner and **wait for the owner to choose**. Do not generate other slides yet.

### Variant A — flat shapes
- The body is built from **flat colour shapes**, like a modern app illustration: sand #D9CBBE body with slightly lighter ivory areas for skin, **no outlines, no shading, no gradients, no muscle fibres**.
- Muscle groups are only suggested by a few simple flat shapes with clean edges (shoulders, chest/back blocks). At most a handful of separations per figure.
- The target muscle is one bold, clean flat #F26445 shape.

### Variant B — clean line art
- The body is **ivory #F5F0E5 with one even dark outline** (#2A2A2A, about 3 px at full size; thinner on the small exercise figures), like a clean vector icon. **No shading, no hatching, no muscle fibres.**
- Inside the body, only a few thin lines hint at the main muscles (spine, shoulder blade, deltoid edge), at most 4–6 lines per figure.
- The target muscle is outlined and filled flat #F26445.

### Variant C — soft matte mannequin
- The body is a **smooth matte figure in sand #D9CBBE**, like a soft clay or vinyl toy: rounded simplified forms, **one very soft light and gentle shadow**, no linework, no fibres, no visible individual small muscles.
- Big muscle groups read only as soft volumes.
- The target muscle is a smooth matte #F26445 area with the same soft shading, clearly separated from the sand.

For each variant, record in `carousels/LW-CAR-0019/manifest.json`: variant, slide, prompt, file, attempts, errors, save status, `agent_visual_review: not_performed`, `user_review: pending`.

## Step 2 — full carousel (only after the owner picks a variant)
Generate slides 1–8 in the chosen variant into `carousels/LW-CAR-0019/outputs/slide-01.png` … `slide-08.png`. You may reuse the chosen test images for slides 1 and 3 if the owner approved them as they are. Slide 8 is the product ending: same composition, text and real Lightweight screenshot as the approved `carousels/LW-CAR-0001/outputs/slide-08.png`; the hand holding the phone is drawn in the chosen style. Never generate, redraw or imitate the app UI. Write `caption.txt` from `copy.json` → `caption`, verbatim, build the ZIP, and commit the whole carousel in one commit.
