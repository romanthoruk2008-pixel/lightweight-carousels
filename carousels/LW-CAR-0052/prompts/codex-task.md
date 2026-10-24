# Codex task — LW-CAR-0052 "muscles people notice first" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0052/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 5 muscles people notice first (our opinion), each with one exercise. 7 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Item slide layout (slides 2–6, one identical layout)
- Copy the layout of the approved `carousels/LW-CAR-0029/outputs/slide-02.png`: label and headline in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind the headline only, body line in regular #2A2A2A, then (where the table has one) the small bold #F26445 label followed by its text in regular #2A2A2A. Lower ~55%: the big white figure from the table.
- After the body line, the small bold #F26445 label `do:` followed by the exercise in regular #2A2A2A.
- The figure does that exercise **with the target muscle filled #F26445**, shirtless as usual. Same layout as the approved `carousels/LW-CAR-0042/outputs/slide-02.png`.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `muscles people` / `notice first` (marker) / `(in our opinion)` | front view from the thighs up, shirtless, relaxed confident stance, shoulders, arms and chest filled #F26445 |
| 2 | item | `#1` `shoulders` (marker) / `they set your whole outline before anything else.` / `do:` `lateral raise` | standing dumbbell lateral raise, arms at shoulder height, front view; **side delts filled #F26445** |
| 3 | item | `#2` `arms` (marker) / `the part people see every time you wear a t-shirt.` / `do:` `chin-ups` | chin-up on a bar with an underhand grip, chin over the bar, front view; **biceps filled #F26445** |
| 4 | item | `#3` `chest` (marker) / `the first thing people see when you face them.` / `do:` `incline db press` | dumbbell press on an incline bench, front three-quarter view; **upper chest filled #F26445** |
| 5 | item | `#4` `back` (marker) / `the shape people see when you walk away.` / `do:` `seated cable row` | seated cable row with a V-handle, rear three-quarter view; **lats and mid back filled #F26445** |
| 6 | item | `#5` `abs` (marker) / `they show when your body fat is low, and people notice.` / `do:` `cable crunch` | kneeling below a high cable, rope by the head, crunching down, side view; **abs filled #F26445** |
| 7 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `get the work`:
  `harda tracks every set you lift, so the muscles people notice get the work.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
