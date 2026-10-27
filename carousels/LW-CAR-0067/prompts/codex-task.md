# Codex task — LW-CAR-0067 "STRUCTURE THE PERFECT ARM DAY" (style S1, original Harda carousel)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S1**). Exact copy: `carousels/LW-CAR-0067/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The arm day part of our STRUCTURE series with the approved **LW-CAR-0002** (push day) and **LW-CAR-0009** (leg day). It must look like their twin: same layouts, positions, sizes, "#N" numbers, underline bars, thin vertical divider between exercises and illustration style. Only the text, the highlighted muscles and the exercises change. 8 slides.

## Visual references (our own approved slides)
| Our slide | Copy the look of |
|---|---|
| 1 cover | `carousels/LW-CAR-0009/outputs/slide-01.png` |
| 2 checklist | `carousels/LW-CAR-0009/outputs/slide-02.png` |
| 3–7 list | `carousels/LW-CAR-0009/outputs/slide-03.png` … `slide-07.png` |
| 8 ending | `carousels/LW-CAR-0009/outputs/slide-08.png` (same hand, phone and real screenshot) |

**Background: `GRID`** on every slide: solid #F0F1EB first, then thin #E1E2DA grid lines, 2 px, every 54 px. **No arch**: the older reference slides may still show it, so ignore it. Opaque, flattened RGB, 1080 x 1350.
**Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.

## Figures
The S1 mannequin, exactly as on the approved S1 slides: bald, faceless, **smooth plastic anatomy mannequin with a featureless pelvis**, fine grey linework, sand #D9CBBE muscles, ivory skin, target muscles #F26445. Full-body figures wear plain short shorts in sand #D9CBBE. **Never the white S2 figure.** Exercise figures have no highlighted muscles (all sand), exactly as on LW-CAR-0009.

## Slides

### Slide 1 — hook (twin of LW-CAR-0009 slide 1)
- Three stacked uppercase lines, heaviest Rubik, same size and position as the template:
  - `STRUCTURE` in #2A2A2A
  - `THE PERFECT` in #2A2A2A
  - `ARM DAY` in #F26445
- Below: the anatomical man doing a standing dumbbell curl, three-quarter front view, mid-rep; biceps and triceps filled #F26445. Figure in the lower half, cropped at the bottom like the template.

### Slide 2 — checklist (twin of LW-CAR-0009 slide 2)
- Top-left, two-line bold title `Your Arm Day` / `Should Include:` + short #F26445 underline bar.
- Left-aligned bullets ("1x" regular, muscle word bold, bracket regular):
  - `1x Biceps (Stretched Curl)`
  - `1x Triceps (Overhead)`
  - `1x Brachialis (Hammer Curl)`
  - `1x Triceps (Pushdown)`
  - `1x Forearms`
- Bottom right, cropped at the right and bottom edges: the **upper body** of the anatomical man (head to waist) in a three-quarter side view, one arm flexed; biceps, triceps, brachialis and forearms filled #F26445.

### Slides 3–7 — list template (twin of LW-CAR-0009 slides 3–7)
- Top-left: big bold `#N` in #F26445 with a short #F26445 underline bar under it. To its right, the title (bold, #2A2A2A), and under the title the sets line (regular, #6B6B6B).
- Under the header, left-aligned: one sentence in regular #6B6B6B, up to two lines.
- Bottom ~55%: two full-body figures doing the exercises side by side, separated by a thin vertical #F26445 line. Labels under each, regular #2A2A2A.

| Slide | Number | Title | Sets line | Sentence (exact) | Left — label | Right — label |
|---|---|---|---|---|---|---|
| 3 | `#1` | `Biceps` | `2-3 sets x 8-12 reps` | `Choose one of these exercises to build your biceps:` | seated on an incline bench, arms hanging back, curling two dumbbells, side view — `Incline Dumbbell Curl` | seated at a preacher bench, curling an EZ bar, side view — `Preacher Curl` |
| 4 | `#2` | `Overhead Triceps` | `2-3 sets x 8-12 reps` | `Choose one of these exercises to stretch your triceps:` | facing away from a cable with a rope, extending the arms forward and up overhead, side view — `Overhead Cable Extension` | seated, one dumbbell held overhead in both hands, lowered behind the head, side view — `Dumbbell Overhead Extension` |
| 5 | `#3` | `Brachialis` | `2-3 sets x 10-12 reps` | `Choose one of these exercises to thicken your arms:` | standing hammer curl with dumbbells, palms facing in, front view — `Hammer Curl` | standing at a low cable with a rope, curling with palms facing in, front view — `Rope Hammer Curl` |
| 6 | `#4` | `Triceps` | `2-3 sets x 10-15 reps` | `Choose one of these exercises to finish your triceps:` | standing rope pushdown at a high pulley, elbows at the sides, front view — `Rope Pushdown` | standing straight-bar pushdown at a high pulley, elbows at the sides, front view — `Bar Pushdown` |
| 7 | `#5` | `Forearms` | `2-3 sets x 12-20 reps` | `Choose one of these exercises to grow your forearms:` | seated, forearms resting on the thighs, curling a dumbbell with the wrist, side view — `Wrist Curl` | standing EZ-bar curl with an overhand grip, front view — `Reverse Curl` |

### Slide 8 — product ending (twin of LW-CAR-0009 slide 8)
Copy the approved slide's composition: Harda logo, short #F26445 bar, two-line left-aligned headline in heaviest Rubik, the hand holding the tall phone. No arch.
- `Track Your Arm Day.` in #2A2A2A
- `See If Your Arms Keep Up.` in #F26445
- Phone: the same **real Harda Muscle balance screenshot** as on the approved LW-CAR-0009 slide 8 (radar with an Arms axis), true proportions, never squashed, may run off the bottom edge. Never generate, redraw or imitate UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides; the approved slides above are the visual reference. Then write the manifest (`agent_visual_review: not_performed`, `user_review: pending`), the caption and the ZIP, and commit and push the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
