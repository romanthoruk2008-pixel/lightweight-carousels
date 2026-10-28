# Codex task — LW-CAR-0075 "most aesthetic muscles tier list" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0075/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A tier list of muscles by how good they look, in our opinion. The stars show how much each one adds to a physique. 19 slides. **Same layouts, type, colours, tier tiles and stars as the approved LW-CAR-0022 (legs tier list)**: cover → its slide 1, tier dividers → its slide 2, item slides → its slide 3, ending → its slide 19. Every word comes from this file and copy.json.

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
- On item slides the figure **poses to show that muscle, filled #F26445**, as the table says. No exercise equipment.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `most aesthetic muscles` / `tier list` (marker) / `(in our opinion)` | front view from the thighs up, relaxed confident stance, shoulders, chest, arms and abs filled #F26445 |
| 2 | tier | tile `F` + `tier` / `nobody notices` | — |
| 3 | item | `#12` `lower back` / `important for every lift, but nobody sees it.` / stars 1 | rear view, standing relaxed, lower back erectors filled #F26445 |
| 4 | item | `#11` `hamstrings` / `they make strong legs, but shorts hide them.` / stars 1.5 | rear view, standing, one leg slightly back, hamstrings filled #F26445 |
| 5 | tier | tile `C` + `tier` / `nice bonus` | — |
| 6 | item | `#10` `calves` / `great in shorts. invisible in jeans.` / stars 2 | rear view, standing on the toes, calves filled #F26445 |
| 7 | item | `#9` `forearms` / `show up every time you roll up your sleeves.` / stars 2.5 | front view from the waist up, one fist clenched in front of the body, forearms filled #F26445 |
| 8 | tier | tile `B` + `tier` / `solid picks` | — |
| 9 | item | `#8` `quads` / `big quads look strong in any shorts.` / stars 3 | front view, standing, one leg forward and flexed, quads filled #F26445 |
| 10 | item | `#7` `traps` / `give your neck and shoulders a strong frame.` / stars 3 | rear view from the waist up, arms relaxed, traps filled #F26445 |
| 11 | item | `#6` `glutes` / `make every pair of jeans fit better.` / stars 3.5 | rear three-quarter view, standing, glutes filled #F26445 |
| 12 | tier | tile `A` + `tier` / `turn heads` | — |
| 13 | item | `#5` `chest` / `fills out every t-shirt you own.` / stars 4 | front view from the waist up, hands on hips, chest filled #F26445 |
| 14 | item | `#4` `arms` / `the first thing people look at in a t-shirt.` / stars 4 | front view from the waist up, front double biceps pose, biceps and triceps filled #F26445 |
| 15 | item | `#3` `abs` / `need low body fat, and everyone notices them.` / stars 4.5 | front view from the thighs up, hands behind the head, abs filled #F26445 |
| 16 | tier | tile `S` + `tier` / `the dream` | — |
| 17 | item | `#2` `back` / `the V shape from every angle.` / stars 5 | rear view from the waist up, rear lat spread pose, lats and upper back filled #F26445 |
| 18 | item | `#1` `shoulders` / `wide shoulders change your whole outline.` / stars 5 | front view from the waist up, arms slightly away from the body, all three delts filled #F26445 |
| 19 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `every muscle gets its turn`:
  `harda tracks every set you lift, so every muscle gets its turn.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
