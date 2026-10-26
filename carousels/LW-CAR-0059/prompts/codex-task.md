# Codex task — LW-CAR-0059 "cardio tier list" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0059/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A tier list of cardio options in the gym. 17 slides. **Same layouts, type, colours, tier tiles and stars as the approved LW-CAR-0022 (legs tier list)**: cover → its slide 1, tier dividers → its slide 2, item slides → its slide 3, ending → its slide 19. Every word comes from this file and copy.json.

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
- **No coloured muscles on the figures.** Keep settings minimal: only the machine or prop the table names.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `cardio` / `tier list` (marker) / `(ranked worst to best)` | front view from the thighs up, a towel over the shoulder, slightly out of breath, standing in front of a treadmill |
| 2 | tier | tile `F` + `tier` / `skip these` | — |
| 3 | item | `#10` `vibration plate` / `standing still while a machine shakes you.` / stars 1 | standing still on a vibration plate machine, bored, front view |
| 4 | item | `#9` `slow elliptical while scrolling` / `it moves, but your heart barely notices.` / stars 1.5 | on an elliptical trainer, looking down at a phone (screen not visible), side view |
| 5 | tier | tile `C` + `tier` / `you can do better` | — |
| 6 | item | `#8` `burpees` / `they work, but nobody keeps them up for long.` / stars 2.5 | mid-burpee jumping up with arms overhead, front view |
| 7 | item | `#7` `elliptical` / `easy on the joints, but easy to coast too.` / stars 2.5 | on an elliptical trainer, moving steadily, side view |
| 8 | tier | tile `B` + `tier` / `solid picks` | — |
| 9 | item | `#6` `running` / `great, but hard on the knees for some people.` / stars 3 | running outdoors on a plain path, side view |
| 10 | item | `#5` `jump rope` / `cheap, fun and good for coordination.` / stars 3.5 | skipping a jump rope, front view |
| 11 | tier | tile `A` + `tier` / `worth your time` | — |
| 12 | item | `#4` `rowing machine` / `full body, low impact, and hard if you push.` / stars 4 | on a rowing machine at the finish of a stroke, side view |
| 13 | item | `#3` `bike` / `easy on the joints and easy to push hard.` / stars 4 | on a stationary bike, pedalling hard, side view |
| 14 | tier | tile `S` + `tier` / `the best of the best` | — |
| 15 | item | `#2` `stairmaster` / `short, brutal and great for your legs.` / stars 4.5 | climbing a stair climber machine, side view |
| 16 | item | `#1` `incline walking` / `low impact, easy to stick with, and you can keep it up for ages.` / stars 5 | walking on a treadmill at a steep incline, relaxed, side view |
| 17 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `never takes over`:
  `harda tracks every set you lift, so cardio never takes over your training.`
- Body, regular #2A2A2A: `log your workouts and keep lifting in your week.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
