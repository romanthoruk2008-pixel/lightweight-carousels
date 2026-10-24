# Codex task — LW-CAR-0048 "the 5 stages of leg day" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0048/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The five stages of grief, told as leg day. Light humour, one stage per slide. 7 slides. Every word comes from this file and copy.json.

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
- The label before each headline is `stage 1` … `stage 5` in small bold lowercase #F26445. The body lines in curly quotes are what the figure is thinking; keep the quotes. No coloured muscles on the figures.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `the 5 stages` / `of leg day` (marker) / `(you know them all)` | front view, full body, standing in front of a squat rack, legs slightly trembling, looking nervously at the loaded barbell, small #F26445 shake lines near the knees |
| 2 | item | `stage 1` `denial` (marker) / `“my legs get enough work from walking.”` | sitting on a flat bench, turned away from a squat rack, waving it off with one hand, side view |
| 3 | item | `stage 2` `anger` (marker) / `“who even invented squats?”` | under a loaded barbell in a squat rack, frowning and gripping the bar hard, small #F26445 anger lines near the head, front view |
| 4 | item | `stage 3` `bargaining` (marker) / `“okay, just leg press. and we skip calves.”` | sitting on a 45-degree leg press machine, holding up one finger as if negotiating, side view |
| 5 | item | `stage 4` `depression` (marker) / `the stairs. every single one.` | walking down a few plain steps, holding the rail, slumped, knees wobbly, small #F26445 shake lines near the legs, side view |
| 6 | item | `stage 5` `acceptance` (marker) / `“see you next week, leg day.”` | sitting calmly on a flat bench with a towel over the shoulder, giving a small nod toward a squat rack, side view |
| 7 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every leg day` and `didn’t skip it`:
  `harda tracks every leg day, so you can’t pretend you didn’t skip it.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
