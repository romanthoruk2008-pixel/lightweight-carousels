# Codex task — LW-CAR-0064 "WEAK SHOULDERS?" (style S1, original Harda carousel)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S1**). Exact copy: `carousels/LW-CAR-0064/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The shoulders version of our approved **WEAK BACK?** (LW-CAR-0001), **WEAK CHEST?** (LW-CAR-0008) and **WEAK CORE?** (LW-CAR-0031). Same layouts, sizes, badges, underline bars and illustration style. 8 slides. Every word comes from this file and copy.json.

## Visual references (our own approved slides)
| Our slide | Copy the look of |
|---|---|
| 1 cover | `carousels/LW-CAR-0031/outputs/slide-01.png` |
| 2 map | `carousels/LW-CAR-0031/outputs/slide-02.png` |
| 3–6 list | `carousels/LW-CAR-0031/outputs/slide-03.png` … `slide-06.png` (badge, title, sets line, short "why" line, close-up, two exercises with OR) |
| 7 bonus tip | `carousels/LW-CAR-0031/outputs/slide-07.png` |
| 8 ending | `carousels/LW-CAR-0031/outputs/slide-08.png` (same hand, phone and real screenshot) |

**Background: `DOTS`** on every slide: solid #F0F1EB first, then small #D4D4CC dots, 6 px, every 45 px. **No arch.** Opaque, flattened RGB, 1080 x 1350.
**Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.

## Figures
The S1 mannequin, exactly as on the approved S1 slides: bald, faceless, **smooth plastic anatomy mannequin with a featureless pelvis**, fine grey linework, sand #D9CBBE muscles, ivory skin, target muscles #F26445. Full-body figures wear plain short shorts in sand #D9CBBE. **Never the white S2 figure.**

## Slides

### Slide 1 — hook (twin of LW-CAR-0031 slide 1)
- `WEAK` in #2A2A2A and `SHOULDERS?` in #F26445, heaviest Rubik, uppercase, soft grey offset shadow, same position and scale, with the small #F26445 paint-splat dot under and right of the "?".
- Below: the man from the hips up, front view, arms slightly away from the body, front, side and rear delts and traps filled #F26445. Head slightly overlapping the bottom of the headline, cropped at the bottom edge.

### Slide 2 — map (twin of LW-CAR-0031 slide 2)
- Title centered at top: `Let's Fix That` (bold, #2A2A2A) + short #F26445 underline bar.
- Center: a large torso (head to hips) in a three-quarter view from the side, so front, side and rear delts and the traps all read; all of them filled #F26445.
- Four rounded thumbnail cards with dark label bars and white caps, in the template's positions, each a mini figure with only that part in #F26445: top-left `FRONT DELTS` (a mini front view), top-right `SIDE DELTS` (a mini front view, outer shoulder), bottom-left `REAR DELTS` (a mini rear view), bottom-right `TRAPS` (a mini rear view, upper back and neck).
- Thin black leader lines with dot ends from each card to that part on the big figure.

### Slides 3–6 — list template (twin of LW-CAR-0031 slides 3–6)
| Slide | Badge | Title | Subtitle | Why line (exact) | Close-up, highlighted | Left — label | Right — label |
|---|---|---|---|---|---|---|---|
| 3 | 1 | `Front Delts` | `2-3 Sets x 6-10 Reps` | `Every press already hits them. One overhead press is enough.` | front of the shoulder | seated dumbbell shoulder press on an upright bench, front view — `Seated Dumbbell Press` | seated shoulder press machine, handles pressed up, front three-quarter view — `Machine Shoulder Press` |
| 4 | 2 | `Side Delts` | `2-3 Sets x 12-20 Reps` | `They make you look wide. Lead with your elbows, not your hands.` | outer shoulder, front view | standing dumbbell lateral raise, arms out at shoulder height, front view — `Dumbbell Lateral Raise` | standing side-on to a low cable, raising one arm out to the side, front view — `Cable Lateral Raise` |
| 5 | 3 | `Rear Delts` | `2-3 Sets x 12-20 Reps` | `The back of your shoulder. Pull your arms out wide, not back.` | back of the shoulder | seated reverse pec deck, arms opening wide, rear view — `Reverse Pec Deck` | standing at a high cable with a rope, pulling it toward the face, elbows high and wide, side view — `Face Pull` |
| 6 | 4 | `Traps` | `2-3 Sets x 10-15 Reps` | `Shrug straight up and hold the top. Don't roll your shoulders.` | upper back and neck from behind | standing with heavy dumbbells at the sides, shoulders shrugged up, front view — `Dumbbell Shrug` | walking with a heavy dumbbell in each hand, tall posture, side view — `Farmer's Carry` |

Exercise figures are full-body S1 mannequins with no highlighted muscles, as on the template.

### Slide 7 — bonus tip (twin of LW-CAR-0031 slide 7)
- Top-left: `Bonus Tip` (bold, #F26445) + short #F26445 underline bar.
- Under it, regular #6B6B6B, left-aligned: `Light weight, clean reps. Swinging heavy dumbbells turns a lateral raise into a shrug.`
- Lower ~60%: the man doing a dumbbell lateral raise, front view, side delts filled #F26445.

### Slide 8 — product ending (twin of LW-CAR-0031 slide 8)
- Headline: `Are Your Shoulders Getting Enough Work?` (bold, #2A2A2A, two lines if needed) + short #F26445 underline bar.
- Body, two paragraphs, regular #6B6B6B: `Log your workouts in Harda.` / `See how many sets your shoulders get compared to every other muscle.`
- Phone: the **real Harda Muscle balance screenshot**, the same as on the approved LW-CAR-0031 slide 8 (radar with a Shoulders axis), true proportions, never squashed. Never generate, redraw or imitate UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides; the approved slides above are the visual reference. Then write the manifest (`agent_visual_review: not_performed`, `user_review: pending`), the caption and the ZIP, and commit and push the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
