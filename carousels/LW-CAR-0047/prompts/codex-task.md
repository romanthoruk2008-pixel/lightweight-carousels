# Codex task — LW-CAR-0047 "look better shirtless" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0047/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 6 muscles that make you look better without a shirt, each with one exercise. 8 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Item slide layout (slides 2–7, one identical layout)
- Copy the layout of the approved `carousels/LW-CAR-0029/outputs/slide-02.png`: label and headline in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind the headline only, body line in regular #2A2A2A, then (where the table has one) the small bold #F26445 label followed by its text in regular #2A2A2A. Lower ~55%: the big white figure from the table.
- After the body line, the small bold #F26445 label `do:` followed by the exercise in regular #2A2A2A.
- The figure does that exercise **with the target muscle filled #F26445**, shirtless as usual. Same layout as the approved `carousels/LW-CAR-0042/outputs/slide-02.png`.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `look better` / `shirtless` (marker) / `(train these 6)` | front view from the thighs up, shirtless, standing relaxed and confident, abs, chest and shoulders filled #F26445 |
| 2 | item | `#1` `abs` (marker) / `the first thing people notice. they show when your body fat is low.` / `do:` `hanging leg raise` | hanging from a pull-up bar, straight legs raised to hip height, side view; **abs filled #F26445** |
| 3 | item | `#2` `chest` (marker) / `a full chest makes your whole torso look stronger.` / `do:` `incline smith press` | incline bench press in a Smith machine, front three-quarter view; **chest filled #F26445** |
| 4 | item | `#3` `shoulders` (marker) / `round shoulders frame everything else.` / `do:` `lateral raise` | standing dumbbell lateral raise, arms at shoulder height, front view; **side delts filled #F26445** |
| 5 | item | `#4` `back` (marker) / `the v-shape people see from behind and from the front.` / `do:` `pull-ups` | pull-up on a bar, chin near the bar, rear view; **lats filled #F26445** |
| 6 | item | `#5` `obliques` (marker) / `sharper lines at the sides of your abs.` / `do:` `cable woodchop` | standing at a high cable, rotating it down and across the body, front three-quarter view; **obliques filled #F26445** |
| 7 | item | `#6` `legs` (marker) / `a big top half on small legs is easy to spot at the beach.` / `do:` `leg press` | seated 45-degree leg press machine, knees bent, side view; **quads filled #F26445** |
| 8 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `no muscle gets left behind`:
  `harda tracks every set you lift, so no muscle gets left behind.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance before summer.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
