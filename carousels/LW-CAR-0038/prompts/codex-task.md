# Codex task — LW-CAR-0038 "gym red flags" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0038/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 gym red flags with light humour, each one slide. 9 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Item slide layout (slides 2–8, one identical layout)
- Copy the layout of the approved `carousels/LW-CAR-0029/outputs/slide-02.png`: label and headline in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind the headline only, body line in regular #2A2A2A, then (where the table has one) the small bold #F26445 label followed by its text in regular #2A2A2A. Lower ~55%: the big white figure from the table.
- Next to the number, a small **#F26445 flag icon** (a simple solid flag on a short pole). Draw the flag; never use an emoji. No coloured muscles on the figures.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `gym` / `red flags` (marker) / `(send this to someone)` | front view from the thighs up, arms crossed, raising one eyebrow, with a large solid #F26445 flag on a short pole planted next to him |
| 2 | item | `#1` `ego lifting` (marker) / `the weight goes up, the form goes home.` | standing barbell curl with a far too heavy bar, swinging the whole body back, side view |
| 3 | item | `#2` `no warm-up` (marker) / `straight to the heaviest set, every single time.` | walking straight up to a heavily loaded barbell on the floor, cracking the knuckles, side view |
| 4 | item | `#3` `machine hostage` (marker) / `ten minutes on the machine, zero sets, full scroll.` | sitting on a chest press machine scrolling a phone (screen not visible), not pushing, front three-quarter view |
| 5 | item | `#4` `never leg day` (marker) / `big upper body, every week, no legs in sight.` | front view, standing: very muscular chest and arms, clearly thin legs, flexing proudly (comic) |
| 6 | item | `#5` `no plan at all` (marker) / `a random workout every day, just vibes.` | standing in the middle of the gym between a rack and a cable machine, looking around confused, front view |
| 7 | item | `#6` `training through sharp pain` (marker) / `pushing through pain that isn’t normal.` | holding the lower back with one hand next to a loaded barbell, wincing, side view |
| 8 | item | `#7` `no idea what they lifted` (marker) / `ask about last week and you get a shrug.` | standing next to a squat rack, shrugging with both palms up, front view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `green flag` and `every set`:
  `green flag: you track every set in harda.`
- Body, regular #2A2A2A: `log your workouts and know exactly what you lifted last week.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
