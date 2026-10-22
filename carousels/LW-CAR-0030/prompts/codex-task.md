# Codex task — LW-CAR-0030 "underrated exercises (nobody does these)" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0030/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 exercises few people do, one per slide. 9 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

- The exercise slides use exactly the layout of the approved `carousels/LW-CAR-0024/outputs/slide-02.png` … `slide-11.png`: small grey muscle heading, exercise name with the marker bar, body line, big white figure with the target muscle filled #F26445.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `underrated` / `exercises` (marker) / `(nobody does these)` | front view, full body, walking forward with a heavy dumbbell in each hand (farmer’s carry), forearms and traps filled #F26445 |
| 2 | exercise | `hamstrings` / `seated leg curl` (marker) / `the stretch at your hip makes it a better curl than the lying one.` | seated leg curl machine, legs curled under the seat, side view; **hamstrings filled #F26445** |
| 3 | exercise | `side delts` / `cable lateral raise` (marker) / `tension right at the bottom, where dumbbells give you nothing.` | standing single-arm cable lateral raise from a low pulley, front view; **side delts filled #F26445** |
| 4 | exercise | `chest` / `deficit push-ups` (marker) / `a deeper stretch than normal push-ups, and no gym needed.` | push-up with each hand on a raised block or weight plate, chest lowered below the hands, side view; **chest filled #F26445** |
| 5 | exercise | `quads` / `reverse nordic` (marker) / `loads your quads in a big stretch with just your bodyweight.` | kneeling upright on a mat, leaning the whole straight body backwards from the knees, side view; **quads filled #F26445** |
| 6 | exercise | `grip & traps` / `farmer’s carry` (marker) / `grip, traps and core in one walk.` | walking forward holding a heavy dumbbell in each hand at the sides, front three-quarter view; **forearms and traps filled #F26445** |
| 7 | exercise | `shins` / `tibialis raise` (marker) / `the front of your shins. almost nobody trains them.` | standing with the back against a wall, heels on the floor, lifting the toes up, side view; **tibialis (front of the shins) filled #F26445** |
| 8 | exercise | `inner thighs` / `copenhagen plank` (marker) / `your inner thighs and core, no equipment at all.` | side plank with the top leg resting on a flat bench and the bottom leg hanging free, front three-quarter view; **adductors (inner thighs) filled #F26445** |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `a fair test`:
  `harda tracks every set you lift, so a new exercise gets a fair test.`
- Body, regular #2A2A2A: `add one to your next workout and see how your numbers grow.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long name may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
