# Codex task — LW-CAR-0089 "structure the perfect leg day" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0089/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** Our STRUCTURE series in the new S2 design: the same slide structure as the old S1 LW-CAR-0009 leg day had a different plan, drawn as S2. 8 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Layouts (the old STRUCTURE structure, drawn in the S2 look)
The **structure** is our old STRUCTURE series (the old S1 LW-CAR-0009 leg day had a different plan): cover, a checklist slide, one slide per slot with two exercise choices, product ending. The **look** is S2, exactly like the approved S2 tier lists: white figure, heavy lowercase grotesk, coral marker bars, solid #F0F1EB. Never the sand S1 figure, never Rubik uppercase, never an arch.
- **Cover:** as LW-CAR-0022 slide 1: line 1 heavy lowercase, line 2 on the #F26445 marker bar, italic #6B6B6B subtitle, big white figure below.
- **Checklist (slide 2):** two-line heavy lowercase title top-left, the marker bar behind line 2 only. Under it, left-aligned bullets, one per line, generous spacing: `1x` bold #F26445, the muscle word bold #2A2A2A, the bracket regular #6B6B6B. Bottom right, cropped at the right and bottom edges: the big white figure from the table with the listed muscles filled #F26445.
- **Slot slides:** top-left `#N` and the headline in the heaviest lowercase grotesk with the marker bar behind the headline only (as LW-CAR-0029 slide 2). Under it the sets line in italic #6B6B6B, then the sentence in regular #2A2A2A. Lower ~55%: **two white figures side by side**, each doing its exercise, separated by a thin vertical #F26445 line; under each, its label in bold lowercase #2A2A2A. No coloured muscles on these exercise figures.
- **Figures always wear the opaque #2A2A2A shorts and are shown doing an exercise or standing in a neutral pose**, never in a close physique pose. If a slide is rejected by the safety system, follow the retry rule in `carousels/CODEX-SERIES-RULES.md`.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `structure the perfect` / `leg day` (marker) / `(pick one from each slot)` | front view from the thighs up, standing on a hack squat machine, knees bent; quads filled #F26445 |
| 2 | checklist | `your leg day` / `should include:` (marker) / bullets: `1x quads (squat)`, `1x hamstrings (hinge)`, `1x hamstrings (curl)`, `1x quads (extension)`, `1x calves` | the white figure from the waist down, three-quarter rear view; quads, hamstrings, glutes and calves filled #F26445 |
| 3 | slot | `#1` `quads` (marker) / `2-3 sets x 6-10 reps` / `choose one of these to build your quads:` | left: doing a hack squat, side view — `hack squat`; right: doing a leg press, side view — `leg press` |
| 4 | slot | `#2` `hamstrings` (marker) / `2-3 sets x 8-12 reps` / `choose one of these to hinge:` | left: doing a romanian deadlift, side view — `romanian deadlift`; right: doing a single-leg rdl, side view — `single-leg rdl` |
| 5 | slot | `#3` `hamstrings` (marker) / `2-3 sets x 10-15 reps` / `choose one of these to curl:` | left: doing a seated leg curl, side view — `seated leg curl`; right: doing a lying leg curl, side view — `lying leg curl` |
| 6 | slot | `#4` `quads` (marker) / `2-3 sets x 10-15 reps` / `choose one of these to finish your quads:` | left: doing a leg extension, side view — `leg extension`; right: doing a bulgarian split squat, side view — `bulgarian split squat` |
| 7 | slot | `#5` `calves` (marker) / `2-3 sets x 10-15 reps` / `choose one of these to grow your calves:` | left: doing a standing calf raise, side view — `standing calf raise`; right: doing a seated calf raise, side view — `seated calf raise` |
| 8 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set` and `your legs keep up`:
  `harda tracks every set of your leg day and shows if your legs keep up.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
