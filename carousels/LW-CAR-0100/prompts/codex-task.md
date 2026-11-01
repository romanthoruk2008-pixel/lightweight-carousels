# Codex task — LW-CAR-0100 "structure the perfect 4-day week" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0100/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A full 4-day training week in the S2 look. 7 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Layouts (S2 look)
- **Cover:** as LW-CAR-0022 slide 1: line 1 heavy lowercase, line 2 on the #F26445 marker bar, italic #6B6B6B subtitle, big white figure below.
- **Overview (slide 2):** two-line heavy lowercase title top-left, the marker bar behind line 2 only. Under it, one row per day, left-aligned, generous spacing: the day in bold #F26445, then the workout in bold #2A2A2A; rest days in regular italic #6B6B6B. Small white figure bottom right.
- **Day slides:** top-left `day N` and the workout name in the heaviest lowercase grotesk with the marker bar behind the name only (as LW-CAR-0029 slide 2). Under it, a clean list of five rows separated by thin #D6D6D2 lines: exercise name in bold lowercase #2A2A2A on the left, sets in regular #6B6B6B right-aligned on the same row. Lower ~45%: one big white figure doing the first exercise of the day. No coloured muscles.
- **Figures always wear the opaque #2A2A2A shorts and are shown doing an exercise or standing in a neutral pose**, never in a close physique pose. If a slide is rejected by the safety system, follow the retry rule in `carousels/CODEX-SERIES-RULES.md`.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `structure the perfect` / `4-day week` (marker) / `(upper / lower, twice a week)` | front view from the thighs up, standing next to a squat rack holding a small weekly calendar card; no coloured muscles |
| 2 | overview | `your 4-day` / `week:` (marker) / rows: `mon: upper a`, `tue: lower a`, `wed: rest`, `thu: upper b`, `fri: lower b`, `sat + sun: rest` | small white figure bottom right, standing relaxed with a towel over one shoulder |
| 3 | day | `day 1` `upper a` (marker) / rows: `bench press` — `3 x 6-8`, `barbell row` — `3 x 6-10`, `seated db press` — `2 x 8-12`, `lat pulldown` — `2 x 8-12`, `cable curl` — `2 x 10-15` | barbell bench press in a rack, side three-quarter view |
| 4 | day | `day 2` `lower a` (marker) / rows: `back squat` — `3 x 6-8`, `romanian deadlift` — `3 x 8-10`, `leg extension` — `2 x 10-15`, `standing calf raise` — `2 x 10-15`, `cable crunch` — `2 x 10-15` | barbell back squat in a rack, side view |
| 5 | day | `day 3` `upper b` (marker) / rows: `incline db press` — `3 x 8-12`, `pull-ups` — `3 x 6-10`, `cable fly` — `2 x 10-15`, `chest-supported row` — `2 x 8-12`, `rope pushdown` — `2 x 10-15` | dumbbell press on an incline bench, front three-quarter view |
| 6 | day | `day 4` `lower b` (marker) / rows: `leg press` — `3 x 8-12`, `hip thrust` — `3 x 8-12`, `lying leg curl` — `2 x 10-15`, `bulgarian split squat` — `2 x 8-12`, `seated calf raise` — `2 x 10-15` | seated 45-degree leg press, side view |
| 7 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set of your week` and `every muscle keeps up`:
  `harda tracks every set of your week and shows if every muscle keeps up.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
