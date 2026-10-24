# Codex task — LW-CAR-0053 "types of gyms tier list" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0053/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A tier list of the kinds of gyms people train in. 17 slides. **Same layouts, type, colours, tier tiles and stars as the approved LW-CAR-0022 (legs tier list)**: cover → its slide 1, tier dividers → its slide 2, item slides → its slide 3, ending → its slide 19. Every word comes from this file and copy.json.

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
- **No coloured muscles on the figures.** Settings stay minimal on the clean #F0F1EB background: only the equipment the table names, no walls or rooms beyond a simple hint.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `types of gyms` / `tier list` (marker) / `(where do you train?)` | front view from the thighs up, holding a gym bag and pointing at the viewer, as if asking where they train |
| 2 | tier | tile `F` + `tier` / `skip these` | — |
| 3 | item | `#10` `hotel gym` / `two dumbbells and a treadmill from 2009.` / stars 1 | standing in a tiny room with one treadmill and a pair of small dumbbells, shrugging, front view |
| 4 | item | `#9` `apartment building gym` / `one bench, a broken cable and a yoga ball.` / stars 1.5 | standing next to a single flat bench, a cable machine with a drooping cable and a yoga ball, looking unimpressed, front view |
| 5 | tier | tile `C` + `tier` / `it’ll do` | — |
| 6 | item | `#8` `just dumbbells at home` / `great to start, but you outgrow it fast.` / stars 2.5 | doing a dumbbell curl next to a small rack of light dumbbells on a mat, front view |
| 7 | item | `#7` `packed budget gym` / `cheap, but you queue for everything at 6pm.` / stars 2.5 | standing in a short queue of three figures waiting for one squat rack, front view |
| 8 | tier | tile `B` + `tier` / `solid` | — |
| 9 | item | `#6` `crossfit box` / `great community, but not built for bodybuilding.` / stars 3 | swinging a kettlebell in front of a pull-up rig and a stack of boxes, front three-quarter view |
| 10 | item | `#5` `24/7 chain gym` / `open whenever you are, with all the basics.` / stars 3.5 | walking past a row of cable machines and a rack, a simple wall clock showing late night, side view |
| 11 | tier | tile `A` + `tier` / `worth it` | — |
| 12 | item | `#4` `university gym` / `cheap, decent kit and quiet in the morning.` / stars 4 | squatting in a rack in an almost empty room, calm, side view |
| 13 | item | `#3` `full home gym` / `no queue, your music, your rack.` / stars 4.5 | squatting in a power rack in a simple garage setting with plates on a tree, side view |
| 14 | tier | tile `S` + `tier` / `the dream` | — |
| 15 | item | `#2` `old-school hardcore gym` / `chalk, heavy plates and nobody on their phone.` / stars 5 | chalking the hands next to a heavily loaded deadlift bar, a little chalk dust in the air, front view |
| 16 | item | `#1` `big gym with everything` / `every machine, every rack and room to train.` / stars 5 | standing confidently in front of a row of different machines and two racks, arms open, front view |
| 17 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `whatever gym you train in` and `every set you lift`:
  `whatever gym you train in, harda tracks every set you lift.`
- Body, regular #2A2A2A: `log your workouts at home, in a hotel or in the gym.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
