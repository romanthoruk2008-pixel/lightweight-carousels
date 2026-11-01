# Codex task — LW-CAR-0096 "how to build a bigger upper chest" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0096/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 5 practical tips to build a bigger upper chest, each with a 'do:' line. 7 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Item slide layout (slides 2–6, one identical layout)
- Copy the layout of the approved `carousels/LW-CAR-0029/outputs/slide-02.png`: label and headline in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind the headline only, body line in regular #2A2A2A, then (where the table has one) the small bold #F26445 label followed by its text in regular #2A2A2A. Lower ~55%: the big white figure from the table.
- After the body line, the small bold #F26445 label `do:` followed by the tip in regular #2A2A2A, as on the approved `carousels/LW-CAR-0052/outputs/slide-02.png`.
- The figure does the exercise **with the named muscle filled #F26445**.
- **Figures always wear the opaque #2A2A2A shorts and are shown doing an exercise or standing in a neutral pose**, never in a close physique pose. If a slide is rejected by the safety system, follow the retry rule in `carousels/CODEX-SERIES-RULES.md`.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `how to build` / `a bigger upper chest` (marker) / `(save this for chest day)` | front view from the thighs up, doing a low-to-high cable fly at the top; upper chest filled #F26445 |
| 2 | item | `#1` `use a low incline` (marker) / `a steep bench turns it into a shoulder press.` / `do:` `set the bench low, not steep.` | dumbbell press on a low incline bench, front three-quarter view; **upper chest filled #F26445** |
| 3 | item | `#2` `press it first` (marker) / `you are strongest at the start.` / `do:` `start chest day with an incline press.` | incline barbell bench press, side view; **upper chest filled #F26445** |
| 4 | item | `#3` `fly from low to high` (marker) / `the upper chest lifts your arms up and in.` / `do:` `bring the handles up to chin height.` | standing in a cable crossover frame, raising low handles up and together, front view; **upper chest filled #F26445** |
| 5 | item | `#4` `tuck your elbows a little` (marker) / `flared elbows load your shoulders.` / `do:` `keep your elbows at about 45 degrees.` | incline dumbbell press, elbows slightly tucked, front view; **upper chest filled #F26445** |
| 6 | item | `#5` `add weight on a smith machine` (marker) / `a fixed path makes progress easy to track.` / `do:` `add a rep or a little weight every week.` | incline bench press in a Smith machine, side view; **upper chest filled #F26445** |
| 7 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set` and `your chest keeps up`:
  `harda tracks every set and shows if your chest keeps up.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
