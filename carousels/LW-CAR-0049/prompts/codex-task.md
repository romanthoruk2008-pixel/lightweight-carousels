# Codex task — LW-CAR-0049 "gym excuses tier list" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0049/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A tier list of gym excuses, from the worst (F) to the actually valid (S); the stars rate how valid each excuse is. 17 slides. **Same layouts, type, colours, tier tiles and stars as the approved LW-CAR-0022 (legs tier list)**: cover → its slide 1, tier dividers → its slide 2, item slides → its slide 3, ending → its slide 19. Every word comes from this file and copy.json.

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
- Item headlines are the excuses in curly quotes; keep the quotes.
- **No coloured muscles on the figures.** Settings stay minimal on the clean #F0F1EB background: only the props the table names.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `gym excuses` / `tier list` (marker) / `(from worst to actually valid)` | front view from the thighs up, holding a gym bag but leaning away from it, one hand raised as if making an excuse, a speech bubble with three dots |
| 2 | tier | tile `F` + `tier` / `not even close` | — |
| 3 | item | `#10` `“it’s cold outside”` / `the gym has a roof and heating.` / stars 1 | standing at a window looking out at snow, wrapped in a blanket, side view |
| 4 | item | `#9` `“i’ll start on monday”` / `which monday, exactly?` / stars 1 | lying on a bench at home looking at a wall calendar, relaxed, side view |
| 5 | tier | tile `C` + `tier` / `we’ve all said it` | — |
| 6 | item | `#8` `“i’m too tired”` / `a light session usually wakes you up.` / stars 2 | slumped on a sofa-like plain bench, yawning, front view |
| 7 | item | `#7` `“i’m still sore”` / `train a different muscle today.` / stars 2.5 | holding one sore thigh with both hands, small #F26445 ache lines, front view |
| 8 | tier | tile `B` + `tier` / `almost believable` | — |
| 9 | item | `#6` `“i don’t have time”` / `a short workout still counts.` / stars 3 | looking at a wristwatch, holding a gym bag, in a hurry, front three-quarter view |
| 10 | item | `#5` `“the gym is too busy”` / `go earlier, or train with what’s free.` / stars 3 | standing in front of a squat rack that is in use by another figure, waiting, front view |
| 11 | tier | tile `A` + `tier` / `fair enough` | — |
| 12 | item | `#4` `“big deadline tomorrow”` / `skip it, then come back the next day.` / stars 4 | sitting at a plain desk with a laptop, focused, side view (screen not visible) |
| 13 | item | `#3` `“i barely slept”` / `rest or go light. sleep wins.` / stars 4.5 | sitting on the edge of a plain bed rubbing the eyes, side view |
| 14 | tier | tile `S` + `tier` / `valid. stay home.` | — |
| 15 | item | `#2` `“i’m actually sick”` / `rest. the gym will still be there.` / stars 5 | sitting wrapped in a blanket with a mug, holding a tissue, front view |
| 16 | item | `#1` `“i’m injured”` / `see a professional and let it heal.` / stars 5 | sitting on a bench with one ankle wrapped in a bandage, side view |
| 17 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every workout` and `the excuses start winning`:
  `harda tracks every workout, so you see when the excuses start winning.`
- Body, regular #2A2A2A: `log your workouts and keep showing up.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
