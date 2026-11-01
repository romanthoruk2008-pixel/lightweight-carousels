# Codex task — LW-CAR-0102 "best exercises for every muscle group (pull day edition)" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0102/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** Our BEST EXERCISES series in the new S2 design: the same slide structure as LW-CAR-0005 / 0070 / 0071, drawn as S2. 8 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Layouts (the old BEST EXERCISES structure, drawn in the S2 look)
The **structure** is our old BEST EXERCISES series (LW-CAR-0005, 0070, 0071): cover, one "A or B" slide per muscle, product ending. The **look** is S2, exactly like the approved S2 tier lists: white figure, heavy lowercase grotesk, coral marker bars, solid #F0F1EB. Never the sand S1 figure, never Rubik uppercase, never an arch.
- **Cover:** as LW-CAR-0022 slide 1: line 1 heavy lowercase, line 2 on the #F26445 marker bar, italic #6B6B6B subtitle, big white figure below.
- **Muscle slides (one identical layout):** top-left `#N` and the muscle name in the heaviest lowercase grotesk with the marker bar behind the name only. Upper middle: a **close-up of the white mannequin** showing that body region, with only the target muscle filled #F26445. Two thin curved #F26445 arrows lead down from the close-up, one to each exercise figure. Lower half: **two white figures** doing the exercises, left and right, with a #F26445 circle badge with white lowercase `or` between them; labels under each in bold lowercase #2A2A2A. No coloured muscles on the exercise figures.
- **Figures always wear the opaque #2A2A2A shorts and are shown doing an exercise or standing in a neutral pose**, never in a close physique pose. If a slide is rejected by the safety system, follow the retry rule in `carousels/CODEX-SERIES-RULES.md`.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `best exercises` / `for every muscle group` (marker) / `(pull day edition)` | rear view from the thighs up, doing a lat pulldown; lats filled #F26445 |
| 2 | muscle | `#1` `lats` (marker) | close-up: rear torso, the lats; left: doing a lat pulldown, clear side or front view — `lat pulldown`; right: doing a single-arm cable pulldown, clear side or front view — `single-arm cable pulldown` |
| 3 | muscle | `#2` `upper back` (marker) | close-up: rear torso, the middle of the back; left: doing a chest-supported t-bar row, clear side or front view — `chest-supported t-bar row`; right: doing a seated cable row, clear side or front view — `seated cable row` |
| 4 | muscle | `#3` `rear delts` (marker) | close-up: shoulder from behind, the rear delt; left: doing a reverse pec deck, clear side or front view — `reverse pec deck`; right: doing a cable reverse fly, clear side or front view — `cable reverse fly` |
| 5 | muscle | `#4` `traps` (marker) | close-up: upper back and neck, the traps; left: doing a db shrug, clear side or front view — `db shrug`; right: doing a farmer’s carry, clear side or front view — `farmer’s carry` |
| 6 | muscle | `#5` `biceps` (marker) | close-up: front upper arm, the biceps; left: doing a preacher curl, clear side or front view — `preacher curl`; right: doing a cable curl, clear side or front view — `cable curl` |
| 7 | muscle | `#6` `brachialis` (marker) | close-up: side of the upper arm; left: doing a hammer curl, clear side or front view — `hammer curl`; right: doing a rope hammer curl, clear side or front view — `rope hammer curl` |
| 8 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set` and `your back keeps up`:
  `harda tracks every set of your pull day and shows if your back keeps up.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
