# Codex task — LW-CAR-0031 "WEAK CORE?" (style S1, original Harda carousel)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S1**). Exact copy: `carousels/LW-CAR-0031/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The core version of our approved **WEAK BACK?** (LW-CAR-0001) and **WEAK CHEST?** (LW-CAR-0008). Same layouts, sizes, badges, underline bars and illustration style. 8 slides. Every word comes from this file and copy.json.

## Visual references (our own approved slides)
| Our slide | Copy the look of |
|---|---|
| 1 cover | `carousels/LW-CAR-0008/outputs/slide-01.png` |
| 2 map | `carousels/LW-CAR-0008/outputs/slide-02.png` |
| 3–6 list | `carousels/LW-CAR-0008/outputs/slide-03.png` … `slide-06.png` (badge, title, sets line, short "why" line, close-up, two exercises with OR) |
| 7 bonus tip | `carousels/LW-CAR-0008/outputs/slide-07.png` |
| 8 ending | `carousels/LW-CAR-0008/outputs/slide-08.png` (same hand, phone and real screenshot) |

**Background: `DOTS`**, as on the approved `carousels/LW-CAR-0014/outputs/`: solid #F0F1EB first, then small #D4D4CC dots every 45 px. **No arch**: LW-CAR-0008 still shows the old arch, so ignore it. Opaque, flattened RGB.
**Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency, as on LW-CAR-0014. Top 110 px free of everything else.

## Figures
The S1 mannequin, exactly as on LW-CAR-0008: bald, faceless, **smooth plastic anatomy mannequin with a featureless pelvis**, fine grey linework, sand #D9CBBE muscles, ivory skin, target muscles #F26445. Full-body figures wear plain short shorts in sand #D9CBBE. Never the white S2 figure.

## Slides

### Slide 1 — hook (twin of LW-CAR-0008 slide 1)
- `WEAK` in #2A2A2A and `CORE?` in #F26445, heaviest Rubik, uppercase, soft grey offset shadow, same position and scale, with the small #F26445 paint-splat dot under and right of the "?".
- Below: the man from the hips up, **front view**, hands behind the head, abs and obliques filled #F26445. Head slightly overlapping the bottom of the headline, cropped at the bottom edge.

### Slide 2 — map (twin of LW-CAR-0008 slide 2)
- Title centered at top: `Let's Fix That` (bold, #2A2A2A) + short #F26445 underline bar.
- Center: large front-view torso (head to hips) with abs, obliques filled #F26445.
- Four rounded thumbnail cards with dark label bars and white caps, in the template's positions, each a mini torso with only that part in #F26445: top-left `UPPER ABS`, top-right `LOWER ABS`, bottom-left `OBLIQUES`, bottom-right `LOWER BACK` (a mini rear view).
- Thin black leader lines with dot ends from each card to that part on the big figure.

### Slides 3–6 — list template (twin of LW-CAR-0008 slides 3–6)
| Slide | Badge | Title | Subtitle | Why line (exact) | Close-up, highlighted | Left — label | Right — label |
|---|---|---|---|---|---|---|---|
| 3 | 1 | `Upper Abs` | `2-3 Sets x 10-15 Reps` | `Curl your ribs down toward your hips. Don't just pull on your neck.` | front torso, upper half of the six-pack | kneeling below a high cable, rope by the head, crunching down — `Cable Crunch` | crunch on a mat, hands by the ears, shoulders lifted — `Crunch` |
| 4 | 2 | `Lower Abs` | `2-3 Sets x 10-15 Reps` | `Tilt your pelvis up. Just swinging your legs works your hip flexors.` | front torso, lower half of the six-pack | hanging from a pull-up bar, straight legs raised to hip height — `Hanging Leg Raise` | lying on a mat, knees pulled toward the chest, hips lifting off the floor — `Reverse Crunch` |
| 5 | 3 | `Obliques` | `2-3 Sets x 10-12 Reps` | `They turn and brace your torso. Train both sides.` | front three-quarter torso, the obliques on the sides of the waist | standing at a high cable, rotating it down and across the body — `Cable Woodchop` | side plank on one forearm, hips dipping down and lifting up — `Side Plank Dips` |
| 6 | 4 | `Lower Back` | `2-3 Sets x 10-15 Reps` | `A strong lower back keeps your core solid under heavy weights.` | rear torso, the erectors in a V at the lower back | 45-degree back extension bench, torso in line with the legs at the top — `Back Extension` | on all fours, one arm and the opposite leg reaching out straight — `Bird Dog` |

### Slide 7 — bonus tip (twin of LW-CAR-0008 slide 7)
- Top-left: `Bonus Tip` (bold, #F26445) + short #F26445 underline bar.
- Under it, regular #6B6B6B, left-aligned: `Abs show when your body fat drops. Train them hard and keep your diet in check.`
- Lower ~60%: the man holding a forearm plank, side view, body in a straight line, abs filled #F26445.

### Slide 8 — product ending (twin of LW-CAR-0008 slide 8)
- Headline: `Is Your Core Getting Enough Work?` (bold, #2A2A2A, two lines if needed) + short #F26445 underline bar.
- Body, two paragraphs, regular #6B6B6B: `Log your workouts in Harda.` / `See how many sets your core gets compared to every other muscle.`
- Phone: the **real Harda Muscle balance screenshot** (radar with a Core axis), the same as the approved LW-CAR-0008 slide 8, true proportions, never squashed. All body text fully visible above the phone. Never generate, redraw or imitate UI.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides; the approved slides above are the visual reference. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
