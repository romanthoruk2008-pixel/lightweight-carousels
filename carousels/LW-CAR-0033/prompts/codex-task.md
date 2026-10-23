# Codex task — LW-CAR-0033 "signs you’re actually making progress" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0033/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A positive 7-point checklist, the mirror image of the approved LW-CAR-0029 (why you’re not growing). 9 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Sign slide layout (slides 2–8, one identical layout)
- Copy the layout of the approved `carousels/LW-CAR-0029/outputs/slide-02.png`: number and headline in the heaviest lowercase grotesk #2A2A2A with the marker bar behind the headline, body line under it in regular #2A2A2A. There is **no `fix:` line** here.
- Next to the number, a small round **#F26445 badge with a white check mark** (✓).
- Lower ~55%: the big white figure from the table. Coloured muscles only where the table says so.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `signs you’re actually` / `making progress` (marker) / `(even if the mirror says no)` | front view from the thighs up, flexing both arms in a relaxed front double biceps, smiling posture, biceps and shoulders filled #F26445 |
| 2 | sign | `#1` `your weights keep going up` (marker) / `the same exercise, a little heavier than last month.` | standing barbell curl with a loaded bar, front view; **biceps filled #F26445** |
| 3 | sign | `#2` `you get more reps` (marker) / `same weight, more reps. that counts too.` | push-up, side view, strong and controlled; **chest filled #F26445** |
| 4 | sign | `#3` `your clothes fit differently` (marker) / `tighter in the shoulders and arms, looser at the waist.` | front view from the thighs up, pulling at a tight plain #2A2A2A t-shirt across the shoulders, a little proud; **shoulders filled #F26445** |
| 5 | sign | `#4` `your old weight is your warm-up` (marker) / `what used to be hard now feels light.` | seated dumbbell shoulder press with light dumbbells, relaxed and easy, front view; **side delts filled #F26445** |
| 6 | sign | `#5` `your form looks smoother` (marker) / `more control on every rep means your body is learning.` | barbell romanian deadlift, perfect flat back, hips back, side view; **hamstrings filled #F26445** |
| 7 | sign | `#6` `you bounce back faster` (marker) / `the same workout leaves you less wrecked the next day.` | standing, stretching both arms overhead after waking up, fresh and relaxed, front view |
| 8 | sign | `#7` `you show up without thinking` (marker) / `the gym is just part of your week now.` | walking forward with a gym bag over one shoulder, confident, front three-quarter view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `see your progress`:
  `harda tracks every set you lift, so you can see your progress, not just feel it.`
- Body, regular #2A2A2A: `log your workouts and compare this month with the last one.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Place the hand and phone low enough that every line of body text is fully visible with a clear gap above the phone; it may run off the bottom edge.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
