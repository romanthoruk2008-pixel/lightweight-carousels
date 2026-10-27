# Codex task — LW-CAR-0066 "STRUCTURE THE PERFECT UPPER DAY" (style S1, original Harda carousel)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S1**). Exact copy: `carousels/LW-CAR-0066/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The upper day part of our STRUCTURE series with the approved **LW-CAR-0002** (push day) and **LW-CAR-0009** (leg day). It must look like their twin: same layouts, positions, sizes, "#N" numbers, underline bars, thin vertical divider between exercises and illustration style. Only the text, the highlighted muscles and the exercises change. 8 slides.

## Visual references (our own approved slides)
| Our slide | Copy the look of |
|---|---|
| 1 cover | `carousels/LW-CAR-0009/outputs/slide-01.png` |
| 2 checklist | `carousels/LW-CAR-0009/outputs/slide-02.png` |
| 3–7 list | `carousels/LW-CAR-0009/outputs/slide-03.png` … `slide-07.png` |
| 8 ending | `carousels/LW-CAR-0009/outputs/slide-08.png` (same hand, phone and real screenshot) |

**Background: `CLEAN`** on every slide: plain solid #F0F1EB. **No arch**: the older reference slides may still show it, so ignore it. Opaque, flattened RGB, 1080 x 1350.
**Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.

## Figures
The S1 mannequin, exactly as on the approved S1 slides: bald, faceless, **smooth plastic anatomy mannequin with a featureless pelvis**, fine grey linework, sand #D9CBBE muscles, ivory skin, target muscles #F26445. Full-body figures wear plain short shorts in sand #D9CBBE. **Never the white S2 figure.** Exercise figures have no highlighted muscles (all sand), exactly as on LW-CAR-0009.

## Slides

### Slide 1 — hook (twin of LW-CAR-0009 slide 1)
- Three stacked uppercase lines, heaviest Rubik, same size and position as the template:
  - `STRUCTURE` in #2A2A2A
  - `THE PERFECT` in #2A2A2A
  - `UPPER DAY` in #F26445
- Below: the anatomical man doing an incline dumbbell press on an incline bench, three-quarter front view, mid-rep; chest and front delts filled #F26445. Figure in the lower half, cropped at the bottom like the template.

### Slide 2 — checklist (twin of LW-CAR-0009 slide 2)
- Top-left, two-line bold title `Your Upper Day` / `Should Include:` + short #F26445 underline bar.
- Left-aligned bullets ("1x" regular, muscle word bold, bracket regular):
  - `1x Chest (Press)`
  - `1x Upper Back (Row)`
  - `1x Lats (Vertical Pull)`
  - `1x Side Delts (Raise)`
  - `1x Arms (Curl + Pushdown)`
- Bottom right, cropped at the right and bottom edges: the **upper body** of the anatomical man (head to waist) in a three-quarter rear view, arms slightly away from the body; chest edge, upper back, lats, side delts and arms filled #F26445.

### Slides 3–7 — list template (twin of LW-CAR-0009 slides 3–7)
- Top-left: big bold `#N` in #F26445 with a short #F26445 underline bar under it. To its right, the title (bold, #2A2A2A), and under the title the sets line (regular, #6B6B6B).
- Under the header, left-aligned: one sentence in regular #6B6B6B, up to two lines.
- Bottom ~55%: two full-body figures doing the exercises side by side, separated by a thin vertical #F26445 line. Labels under each, regular #2A2A2A.

| Slide | Number | Title | Sets line | Sentence (exact) | Left — label | Right — label |
|---|---|---|---|---|---|---|
| 3 | `#1` | `Chest` | `2-3 sets x 6-10 reps` | `Choose one of these exercises to build your chest:` | dumbbell press on an incline bench, front three-quarter view — `Incline Dumbbell Press` | seated chest press machine, handles pressed forward, side view — `Machine Chest Press` |
| 4 | `#2` | `Upper Back` | `2-3 sets x 8-12 reps` | `Choose one of these exercises to thicken your back:` | lying chest-down on an incline bench, rowing two dumbbells, side view — `Chest-Supported Row` | seated cable row with a V-handle, side view — `Seated Cable Row` |
| 5 | `#3` | `Lats` | `2-3 sets x 8-12 reps` | `Choose one of these exercises to widen your back:` | seated lat pulldown, wide bar pulled to the upper chest, rear view — `Lat Pulldown` | pull-up on a bar, chin over the bar, rear view — `Pull-Ups` |
| 6 | `#4` | `Side Delts` | `2-3 sets x 12-20 reps` | `Choose one of these exercises to widen your shoulders:` | standing dumbbell lateral raise, arms out at shoulder height, front view — `Dumbbell Lateral Raise` | standing side-on to a low cable, raising one arm out to the side, front view — `Cable Lateral Raise` |
| 7 | `#5` | `Arms` | `2-3 sets x 10-15 reps` | `Finish with one curl and one pushdown:` | standing cable curl with a straight bar at a low pulley, front view — `Cable Curl` | standing rope pushdown at a high pulley, elbows at the sides, front view — `Rope Pushdown` |

### Slide 8 — product ending (twin of LW-CAR-0009 slide 8)
Copy the approved slide's composition: Harda logo, short #F26445 bar, two-line left-aligned headline in heaviest Rubik, the hand holding the tall phone. No arch.
- `Track Your Upper Day.` in #2A2A2A
- `See If Every Muscle Keeps Up.` in #F26445
- Phone: the same **real Harda Muscle balance screenshot** as on the approved LW-CAR-0009 slide 8 (radar with Chest, Back, Shoulders and Arms axes), true proportions, never squashed, may run off the bottom edge. Never generate, redraw or imitate UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides; the approved slides above are the visual reference. Then write the manifest (`agent_visual_review: not_performed`, `user_review: pending`), the caption and the ZIP, and commit and push the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
