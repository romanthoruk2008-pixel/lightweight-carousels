# Codex task — LW-CAR-0076 "gym fails tier list" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0076/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A tier list of gym fails from least to most embarrassing. The stars show how embarrassing each one is. 17 slides. **Same layouts, type, colours, tier tiles and stars as the approved LW-CAR-0022 (legs tier list)**: cover → its slide 1, tier dividers → its slide 2, item slides → its slide 3, ending → its slide 19. Every word comes from this file and copy.json.

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
- **No coloured muscles on the figures.** Small #F26445 effect marks only where the table says so. Keep the humour friendly; nobody gets hurt on the slides.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `gym fails` / `tier list` (marker) / `(least to most embarrassing)` | front view from the thighs up, one hand covering the face in embarrassment, a dropped dumbbell on the floor |
| 2 | tier | tile `F` + `tier` / `happens to everyone` | — |
| 3 | item | `#10` `forgetting your headphones` / `the longest workout of your life.` / stars 1 | standing in the gym patting the empty shorts pockets, worried, front view |
| 4 | item | `#9` `waving back at someone` / `they were waving at the person behind you.` / stars 1.5 | waving with one hand, while a second figure in the background waves past them, front view |
| 5 | tier | tile `C` + `tier` / `a little awkward` | — |
| 6 | item | `#8` `taking someone’s machine` / `they were just drinking water. you didn’t know.` / stars 2 | sitting on a cable machine seat while a second figure holding a water bottle stands beside it, front view |
| 7 | item | `#7` `pushing a pull door` / `in front of the whole gym, through the glass.` / stars 2.5 | pushing a plain glass door with a handle, confused posture, side view |
| 8 | tier | tile `B` + `tier` / `people noticed` | — |
| 9 | item | `#6` `forgetting the clips` / `one side slides off. everyone hears it.` / stars 3 | plates sliding off one end of a barbell in a rack, small #F26445 motion lines, front view |
| 10 | item | `#5` `loading the bar unevenly` / `one side heavier. the bar tells everyone.` / stars 3.5 | barbell back squat, the bar tilting to one side, puzzled posture, front view |
| 11 | tier | tile `A` + `tier` / `everyone saw it` | — |
| 12 | item | `#4` `dropping a dumbbell` / `the whole gym turns around.` / stars 4 | a dumbbell bouncing on the floor next to the figure, small #F26445 impact lines, front view |
| 13 | item | `#3` `failing a rep with no spotter` / `just you, the bar and a long slow roll.` / stars 4.5 | lying on a flat bench, the barbell resting low on the body, about to roll it down, side view |
| 14 | tier | tile `S` + `tier` / `legendary` | — |
| 15 | item | `#2` `ripping your shorts on a squat` / `loud, sudden and unforgettable.` / stars 5 | barbell back squat at the bottom, small #F26445 tear marks on the shorts, side view |
| 16 | item | `#1` `falling off the treadmill` / `you will never forget it. neither will they.` / stars 5 | stumbling backwards off the end of a running treadmill, arms out, side view |
| 17 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `stay between us`:
  `harda tracks every set you lift. the fails stay between us.`
- Body, regular #2A2A2A: `log your workouts and keep coming back.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
