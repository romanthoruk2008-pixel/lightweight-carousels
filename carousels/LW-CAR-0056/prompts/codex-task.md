# Codex task — LW-CAR-0056 "most skipped muscles tier list" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0056/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A tier list of muscles from least skipped (F) to most skipped (S). The stars show how often people skip each one. 17 slides. **Same layouts, type, colours, tier tiles and stars as the approved LW-CAR-0022 (legs tier list)**: cover → its slide 1, tier dividers → its slide 2, item slides → its slide 3, ending → its slide 19. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.
- **Tier tiles:** rounded square, big white bold letter with a soft shadow: `S` **#F26445**, `A` #FF9A52, `B` #FFD95A, `C` #3FCF5E, `F` #5BDCE3. Stars: filled #F26445, empty #D6D6D2, a half star half filled.
- On item slides the figure has **that muscle filled #F26445**, as the table says.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `most skipped muscles` / `tier list` (marker) / `(least skipped to most skipped)` | rear three-quarter view, full body, standing, calves, rear delts and forearms filled #F26445, looking over the shoulder at them |
| 2 | tier | tile `F` + `tier` / `everyone trains these` | — |
| 3 | item | `#10` `chest` / `never skipped. it’s monday.` / stars 1 | flat barbell bench press, front three-quarter view; chest filled #F26445 |
| 4 | item | `#9` `biceps` / `trained by someone, somewhere, right now.` / stars 1 | standing dumbbell curl, front view; biceps filled #F26445 |
| 5 | tier | tile `C` + `tier` / `sometimes forgotten` | — |
| 6 | item | `#8` `back` / `you can’t see it, so it gets less love.` / stars 2.5 | seated lat pulldown, rear view; lats filled #F26445 |
| 7 | item | `#7` `abs` / `done ‘at the end’, which usually means never.` / stars 2.5 | hanging leg raise, side view; abs filled #F26445 |
| 8 | tier | tile `B` + `tier` / `often skipped` | — |
| 9 | item | `#6` `legs` / `the classic. everyone knows it.` / stars 3 | barbell back squat at the bottom, side view; quads filled #F26445 |
| 10 | item | `#5` `rear delts` / `the back of your shoulders. most people forget they exist.` / stars 3.5 | seated reverse pec deck, rear view; rear delts filled #F26445 |
| 11 | tier | tile `A` + `tier` / `mostly skipped` | — |
| 12 | item | `#4` `forearms` / `only trained by accident when you hold things.` / stars 4 | farmer’s carry with heavy dumbbells, front view; forearms filled #F26445 |
| 13 | item | `#3` `lower back` / `ignored until it starts to hurt.` / stars 4 | 45-degree back extension, side view; lower back erectors filled #F26445 |
| 14 | tier | tile `S` + `tier` / `who even trains these?` | — |
| 15 | item | `#2` `calves` / `‘they’re genetic’ is not a training plan.` / stars 5 | standing calf raise machine, up on the toes, side view; calves filled #F26445 |
| 16 | item | `#1` `shins` / `most people don’t know it’s a muscle.` / stars 5 | tibialis raise with the back against a wall, toes lifted, side view; tibialis filled #F26445 |
| 17 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set` and `which muscles you skip`:
  `harda tracks every set and shows exactly which muscles you skip.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
