# Codex task — LW-CAR-0034 "you’re not a beginner anymore if…" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0034/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A 7-point self-check list. People count how many apply to them. 9 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Point slide layout (slides 2–8, one identical layout)
- Top-left under the logo area: a **large rounded checkbox** (about 70 px, thin #2A2A2A outline, white fill) with a bold **#F26445 tick** inside, as if just ticked off.
- Next to it / under it: the point in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind it (as the exercise names on LW-CAR-0022). Then the body line in regular #2A2A2A.
- Lower ~55%: the big white figure from the table. No coloured muscles on these slides.
- Bottom-right corner, small italic #6B6B6B counter: `1/7`, `2/7` … `7/7` (slide 2 = `1/7`).

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `you’re not a` / `beginner anymore if…` (marker) / `(count how many)` | front view from the thighs up, arms crossed, confident, chest and arms filled #F26445 |
| 2 | point | empty checkbox ticked #F26445 / `you have a favorite exercise` (marker) / `and very strong opinions about it.` | standing, holding a barbell across the back, about to squat, confident, front three-quarter view |
| 3 | point | empty checkbox ticked #F26445 / `you warm up without being told` (marker) / `a few light sets before the heavy ones, every time.` | doing a light bodyweight squat with arms forward, relaxed, side view |
| 4 | point | empty checkbox ticked #F26445 / `you plan before you walk in` (marker) / `you know every exercise before you touch a weight.` | standing, looking at a phone held in one hand (screen not visible), calm, front three-quarter view |
| 5 | point | empty checkbox ticked #F26445 / `you feel the right muscle working` (marker) / `not just moving the weight from a to b.` | seated cable row, squeezing the shoulder blades together, side view |
| 6 | point | empty checkbox ticked #F26445 / `you stopped ego lifting` (marker) / `lighter weight, cleaner reps, better results.` | dumbbell bench press with controlled moderate dumbbells, front view |
| 7 | point | empty checkbox ticked #F26445 / `you rest on purpose` (marker) / `you know how long you need between sets.` | sitting on a flat bench between sets, towel over one shoulder, breathing, side view |
| 8 | point | empty checkbox ticked #F26445 / `you track every workout` (marker) / `you know exactly what to beat next time.` | standing next to a squat rack, looking down at a phone held in both hands (screen not visible) |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `what to beat next time`:
  `harda tracks every set you lift, so you always know what to beat next time.`
- Body, regular #2A2A2A: `log your workouts and keep leveling up.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Place the hand and phone low enough that every line of body text is fully visible with a clear gap above the phone; it may run off the bottom edge.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
