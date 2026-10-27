# Codex task — LW-CAR-0063 "WEAK LEGS?" (style S1, original Harda carousel)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S1**). Exact copy: `carousels/LW-CAR-0063/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The legs version of our approved **WEAK BACK?** (LW-CAR-0001), **WEAK CHEST?** (LW-CAR-0008) and **WEAK CORE?** (LW-CAR-0031). Same layouts, sizes, badges, underline bars and illustration style. 8 slides. Every word comes from this file and copy.json.

## Visual references (our own approved slides)
| Our slide | Copy the look of |
|---|---|
| 1 cover | `carousels/LW-CAR-0031/outputs/slide-01.png` |
| 2 map | `carousels/LW-CAR-0031/outputs/slide-02.png` |
| 3–6 list | `carousels/LW-CAR-0031/outputs/slide-03.png` … `slide-06.png` (badge, title, sets line, short "why" line, close-up, two exercises with OR) |
| 7 bonus tip | `carousels/LW-CAR-0031/outputs/slide-07.png` |
| 8 ending | `carousels/LW-CAR-0031/outputs/slide-08.png` (same hand, phone and real screenshot) |

**Background: `GRID`** on every slide: solid #F0F1EB first, then thin #E1E2DA grid lines, 2 px, every 54 px. **No arch.** Opaque, flattened RGB, 1080 x 1350.
**Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.

## Figures
The S1 mannequin, exactly as on the approved S1 slides: bald, faceless, **smooth plastic anatomy mannequin with a featureless pelvis**, fine grey linework, sand #D9CBBE muscles, ivory skin, target muscles #F26445. Full-body figures wear plain short shorts in sand #D9CBBE. **Never the white S2 figure.**

## Slides

### Slide 1 — hook (twin of LW-CAR-0031 slide 1)
- `WEAK` in #2A2A2A and `LEGS?` in #F26445, heaviest Rubik, uppercase, soft grey offset shadow, same position and scale, with the small #F26445 paint-splat dot under and right of the "?".
- Below: the man in full body, front view, standing tall, quads, adductors and calves filled #F26445; he may be cropped at the shins. Head slightly overlapping the bottom of the headline, cropped at the bottom edge.

### Slide 2 — map (twin of LW-CAR-0031 slide 2)
- Title centered at top: `Let's Fix That` (bold, #2A2A2A) + short #F26445 underline bar.
- Center: a large full-body figure in a three-quarter view from behind and the side, so both the front and the back of the legs read; quads, hamstrings, adductors and calves filled #F26445.
- Four rounded thumbnail cards with dark label bars and white caps, in the template's positions, each a mini figure with only that part in #F26445: top-left `QUADS` (a mini front view), top-right `HAMSTRINGS` (a mini rear view), bottom-left `ADDUCTORS` (a mini front view, inner thigh), bottom-right `CALVES` (a mini rear view).
- Thin black leader lines with dot ends from each card to that part on the big figure.

### Slides 3–6 — list template (twin of LW-CAR-0031 slides 3–6)
| Slide | Badge | Title | Subtitle | Why line (exact) | Close-up, highlighted | Left — label | Right — label |
|---|---|---|---|---|---|---|---|
| 3 | 1 | `Quads` | `2-3 Sets x 6-10 Reps` | `Let your knees travel forward and sit deep. Half reps cheat your quads.` | front of the thigh | seated 45-degree leg press, knees deeply bent, side view — `Leg Press` | goblet squat holding one dumbbell at the chest, bottom position, side view — `Goblet Squat` |
| 4 | 2 | `Hamstrings` | `2-3 Sets x 8-12 Reps` | `They bend your knee and hinge your hip. Train both moves.` | back of the thigh | barbell hip hinge with a flat back, bar at mid-shin, side view — `Romanian Deadlift` | lying face down on a leg curl machine, heels curled toward the glutes, side view — `Lying Leg Curl` |
| 5 | 3 | `Adductors` | `2-3 Sets x 10-15 Reps` | `Your inner thighs are a big part of your legs. Most people skip them.` | inner thigh, front view | seated hip adductor machine, legs squeezing in, front view — `Adductor Machine` | side plank on one forearm, the top foot resting on a flat bench, hips lifted, front view — `Copenhagen Plank` |
| 6 | 4 | `Calves` | `2-3 Sets x 10-15 Reps` | `Pause in the bottom stretch. Bouncing lets your tendons do the work.` | lower leg from behind | standing calf raise machine, up on the toes, side view — `Standing Calf Raise` | seated calf raise machine, pad on the knees, up on the toes, side view — `Seated Calf Raise` |

Exercise figures are full-body S1 mannequins with no highlighted muscles, as on the template.

### Slide 7 — bonus tip (twin of LW-CAR-0031 slide 7)
- Top-left: `Bonus Tip` (bold, #F26445) + short #F26445 underline bar.
- Under it, regular #6B6B6B, left-aligned: `Leg day is the day most people skip. Just showing up every week puts you ahead.`
- Lower ~60%: the man in a barbell back squat at the bottom, side view, quads and calves filled #F26445.

### Slide 8 — product ending (twin of LW-CAR-0031 slide 8)
- Headline: `Are Your Legs Getting Enough Work?` (bold, #2A2A2A, two lines if needed) + short #F26445 underline bar.
- Body, two paragraphs, regular #6B6B6B: `Log your workouts in Harda.` / `See how many sets your legs get compared to every other muscle.`
- Phone: the **real Harda Muscle balance screenshot**, the same as on the approved LW-CAR-0031 slide 8 (radar with a Legs axis), true proportions, never squashed. Never generate, redraw or imitate UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides; the approved slides above are the visual reference. Then write the manifest (`agent_visual_review: not_performed`, `user_review: pending`), the caption and the ZIP, and commit and push the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
