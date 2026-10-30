# Codex task — LW-CAR-0077 "structure the perfect chest day" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0077/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** Our STRUCTURE series in the new S2 design: the same slide structure as LW-CAR-0002 push day and LW-CAR-0009 leg day, drawn as S2. 8 slides. Every word comes from this file and copy.json.

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
The **structure** is our old STRUCTURE series (LW-CAR-0002 push day and LW-CAR-0009 leg day): cover, a checklist slide, one slide per slot with two exercise choices, product ending. The **look** is S2, exactly like the approved S2 tier lists: white figure, heavy lowercase grotesk, coral marker bars, solid #F0F1EB. Never the sand S1 figure, never Rubik uppercase, never an arch.
- **Cover:** as LW-CAR-0022 slide 1: line 1 heavy lowercase, line 2 on the #F26445 marker bar, italic #6B6B6B subtitle, big white figure below.
- **Checklist (slide 2):** two-line heavy lowercase title top-left, the marker bar behind line 2 only. Under it, left-aligned bullets, one per line, generous spacing: `1x` bold #F26445, the muscle word bold #2A2A2A, the bracket regular #6B6B6B. Bottom right, cropped at the right and bottom edges: the big white figure from the table with the listed muscles filled #F26445.
- **Slot slides:** top-left `#N` and the headline in the heaviest lowercase grotesk with the marker bar behind the headline only (as LW-CAR-0029 slide 2). Under it the sets line in italic #6B6B6B, then the sentence in regular #2A2A2A. Lower ~55%: **two white figures side by side**, each doing its exercise, separated by a thin vertical #F26445 line; under each, its label in bold lowercase #2A2A2A. No coloured muscles on these exercise figures.
- **Figures always wear the opaque #2A2A2A shorts and are shown doing an exercise or standing in a neutral pose**, never in a close physique pose. If a slide is rejected by the safety system, follow the retry rule in `carousels/CODEX-SERIES-RULES.md`.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `structure the perfect` / `chest day` (marker) / `(pick one from each slot)` | front view from the thighs up, doing a dumbbell incline press at the top, sitting on an incline bench; chest filled #F26445 |
| 2 | checklist | `your chest day` / `should include:` (marker) / bullets: `1x upper chest (incline press)`, `1x mid chest (flat press)`, `1x lower chest (dips)`, `1x chest squeeze (fly)`, `1x triceps (pushdown)` | the white figure from the waist up, front three-quarter view, arms slightly away from the body; upper, mid and lower chest and triceps filled #F26445 |
| 3 | slot | `#1` `upper chest` (marker) / `2-3 sets x 6-10 reps` / `choose one of these to build your upper chest:` | left: dumbbell press on an incline bench, front three-quarter view — `incline db press`; right: incline bench press in a Smith machine, side view — `incline smith press` |
| 4 | slot | `#2` `mid chest` (marker) / `2-3 sets x 6-10 reps` / `choose one of these to build your whole chest:` | left: barbell bench press in a rack, front three-quarter view — `barbell bench press`; right: seated chest press machine, handles pressed forward, side view — `machine chest press` |
| 5 | slot | `#3` `lower chest` (marker) / `2-3 sets x 8-12 reps` / `choose one of these to build your lower chest:` | left: dip on parallel bars, torso leaning forward, side view — `dips`; right: standing in a cable crossover frame, pulling high handles down and together in front of the hips, front view — `high-to-low cable fly` |
| 6 | slot | `#4` `chest squeeze` (marker) / `2-3 sets x 10-15 reps` / `choose one of these to finish your chest:` | left: seated pec deck machine, front view — `pec deck`; right: seated cable fly on a bench inside a cable crossover frame, front view — `seated cable fly` |
| 7 | slot | `#5` `triceps` (marker) / `2-3 sets x 10-15 reps` / `choose one of these to finish your triceps:` | left: standing rope pushdown at a high pulley, elbows at the sides, front view — `rope pushdown`; right: facing away from a cable with a rope, extending the arms up overhead, side view — `overhead cable extension` |
| 8 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set` and `your chest keeps up`:
  `harda tracks every set of your chest day and shows if your chest keeps up.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
