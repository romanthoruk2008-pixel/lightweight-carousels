# Codex task — LW-CAR-0062 "gym things that feel illegal" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0062/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 small gym moments that feel too good to be allowed, each one slide. 9 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Item slide layout (slides 2–8, one identical layout)
- Copy the layout of the approved `carousels/LW-CAR-0029/outputs/slide-02.png`: label and headline in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind the headline only, body line in regular #2A2A2A, then (where the table has one) the small bold #F26445 label followed by its text in regular #2A2A2A. Lower ~55%: the big white figure from the table.
- No coloured muscles on the figures. Small #F26445 effect marks only where the table says so. Where the table names a clock, draw a simple round wall clock that shows only the time; no text on it.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `gym things that` / `feel illegal` (marker) / `(but totally allowed)` | front view from the thighs up, standing next to an empty squat rack, one finger raised in front of the face in a sneaky 'shh' gesture, sneaky posture |
| 2 | item | `#1` `an empty squat rack at 6pm` (marker) / `you look around. nobody’s coming. it’s yours.` | standing in front of an empty squat rack with a loaded bar, looking left and right in disbelief, a simple wall clock showing 6:00, front view |
| 3 | item | `#2` `the whole gym to yourself` (marker) / `just you, your music and every machine.` | standing alone in a wide empty gym with the arms spread open, plain black over-ear headphones, front view |
| 4 | item | `#3` `brand new plates` (marker) / `no scratches, no rust. you almost don’t want to use them.` | holding a shiny new weight plate in both hands and admiring it, small #F26445 sparkle marks, side three-quarter view |
| 5 | item | `#4` `the perfect pump` (marker) / `your arms look twice as big. for about twenty minutes.` | flexing one arm and staring at it in disbelief, front view |
| 6 | item | `#5` `grinding out the last rep` (marker) / `slow, shaking, and it still went up.` | flat barbell bench press with the bar halfway up, arms shaking, small #F26445 shake lines, side three-quarter view |
| 7 | item | `#6` `adding a plate you couldn’t lift last month` (marker) / `same bar, more weight. that’s progress.` | sliding one more plate onto an already loaded barbell, proud posture, side view |
| 8 | item | `#7` `the dumbbells you need, right where they belong` (marker) / `in order, in pairs, on the rack. a miracle.` | reaching for a dumbbell on a neatly ordered dumbbell rack, surprised posture, front three-quarter view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `on record`:
  `harda tracks every set you lift, so every new plate is on record.`
- Body, regular #2A2A2A: `log your workouts and watch the weight go up.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
