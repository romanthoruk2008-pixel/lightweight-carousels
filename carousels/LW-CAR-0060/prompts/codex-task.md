# Codex task — LW-CAR-0060 "post-workout meals tier list" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0060/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A tier list of what to eat after a workout. Opinions only. 17 slides. **Same layouts, type, colours, tier tiles and stars as the approved LW-CAR-0022 (legs tier list)**: cover → its slide 1, tier dividers → its slide 2, item slides → its slide 3, ending → its slide 19. Every word comes from this file and copy.json.

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
- **No coloured muscles on the figures. No brand names, logos or text on any food, can, bar or shaker.** Keep settings minimal: a plain table or bench and the food.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `post-workout meals` / `tier list` (marker) / `(ranked worst to best)` | front view from the thighs up, holding a plate with a fork and knife, hungry posture |
| 2 | tier | tile `F` + `tier` / `skip these` | — |
| 3 | item | `#10` `nothing at all` / `you just trained. eat something.` / stars 1 | sitting on a gym bench with an empty plate in the hands, front view |
| 4 | item | `#9` `energy drink only` / `caffeine isn’t a meal.` / stars 1 | holding a plain unbranded can, unimpressed, front view |
| 5 | tier | tile `C` + `tier` / `you can do better` | — |
| 6 | item | `#8` `pizza` / `tasty, and fine sometimes. not every day.` / stars 2 | holding a slice of pizza, guilty posture, front view |
| 7 | item | `#7` `protein bar` / `handy on the go, but not a real meal.` / stars 2.5 | holding a plain unbranded bar while walking with a gym bag, side view |
| 8 | tier | tile `B` + `tier` / `solid picks` | — |
| 9 | item | `#6` `yogurt and fruit` / `quick, light and easy to keep up.` / stars 3 | eating from a bowl of yogurt with fruit, sitting, front view |
| 10 | item | `#5` `shake and a banana` / `fast and simple when you’re busy.` / stars 3.5 | holding a plain shaker and a banana, front view |
| 11 | tier | tile `A` + `tier` / `worth your time` | — |
| 12 | item | `#4` `eggs on toast` / `simple, filling and full of protein.` / stars 4 | sitting at a table with a plate of eggs on toast, side view |
| 13 | item | `#3` `burrito bowl` / `rice, protein, beans and veg in one bowl.` / stars 4.5 | sitting at a table with a big bowl, side view |
| 14 | tier | tile `S` + `tier` / `the best of the best` | — |
| 15 | item | `#2` `salmon, potatoes and veg` / `a complete meal that fills you up properly.` / stars 5 | sitting at a table with a plate of salmon, potatoes and vegetables, side view |
| 16 | item | `#1` `chicken and rice` / `the classic for a reason. simple and complete.` / stars 5 | sitting at a table with a large plate of chicken, rice and vegetables, front three-quarter view |
| 17 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `up to you`:
  `harda tracks every set you lift. what you eat after is up to you.`
- Body, regular #2A2A2A: `log your workouts and keep your training consistent.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
