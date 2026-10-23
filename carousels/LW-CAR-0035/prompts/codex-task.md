# Codex task — LW-CAR-0035 "home workout tier list" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0035/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A tier list of 12 bodyweight exercises you can do at home (a chair, a table and a doorway bar at most). 19 slides. **Same layouts, type, colours, tier tiles and stars as the approved LW-CAR-0022 (legs tier list)**: cover → its slide 1, tier dividers → its slide 2, exercise slides → its slide 3, ending → its slide 19. Every word comes from this file and copy.json.

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
- **Home setting:** no gym machines anywhere. Props only as the table says: a mat, a sturdy plain chair, a plain table, a doorway pull-up bar. Keep the background the same clean #F0F1EB (no room, no furniture beyond the prop).

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `home workout` / `tier list` (marker) / `(no gym needed)` | front view from the thighs up, standing on a simple mat, hands on hips, chest, shoulders and arms filled #F26445 |
| 2 | tier | tile `F` + `tier` / `skip these` | — |
| 3 | exercise | `#12` `jumping jacks` / `good cardio, but they won’t build muscle.` / stars 1 | jumping jack, arms overhead and legs apart, front view |
| 4 | exercise | `#11` `arm circles` / `a warm-up, not a workout.` / stars 1 | standing, arms straight out to the sides making small circles, front view |
| 5 | tier | tile `C` + `tier` / `you can do better` | — |
| 6 | exercise | `#10` `crunches` / `they work, but the range is tiny.` / stars 2.5 | crunch on a mat, shoulders lifted, side view |
| 7 | exercise | `#9` `glute bridge` / `great to start, but it gets easy fast.` / stars 2.5 | glute bridge on a mat, hips lifted, side view |
| 8 | tier | tile `B` + `tier` / `solid picks` | — |
| 9 | exercise | `#8` `plank` / `good for your core, but holding longer stops helping.` / stars 3 | forearm plank on a mat, side view |
| 10 | exercise | `#7` `lunges` / `solid for legs, but balance limits how hard you push.` / stars 3.5 | bodyweight reverse lunge, back knee near the floor, side view |
| 11 | exercise | `#6` `pike push-ups` / `the best shoulder move you can do at home.` / stars 3.5 | pike push-up, hips high, head lowering toward the floor, side view |
| 12 | tier | tile `A` + `tier` / `worth your time` | — |
| 13 | exercise | `#5` `chair dips` / `chest and triceps with just a sturdy chair.` / stars 4 | dips with hands on the edge of a sturdy chair behind the body, legs out in front, side view |
| 14 | exercise | `#4` `table rows` / `your back needs pulling, and a table works.` / stars 4 | lying under a sturdy table, holding its edge, pulling the chest up to it, body straight, side view |
| 15 | exercise | `#3` `bulgarian split squat` / `the hardest leg move you can do at home.` / stars 4.5 | bulgarian split squat, rear foot on a chair, bodyweight only, side view |
| 16 | tier | tile `S` + `tier` / `build your body on these` | — |
| 17 | exercise | `#2` `push-ups` / `slow them down or add a backpack and they keep working.` / stars 5 | push-up, side view, strong and controlled |
| 18 | exercise | `#1` `pull-ups` / `the best upper body move. a doorway bar is all you need.` / stars 5 | pull-up on a doorway pull-up bar, chin over the bar, rear view |
| 19 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you do` and `at home or in the gym`:
  `harda tracks every set you do, at home or in the gym.`
- Body, regular #2A2A2A: `log your workouts and watch your reps go up.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Place the hand and phone low enough that every line of body text is fully visible with a clear gap above the phone; it may run off the bottom edge.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
