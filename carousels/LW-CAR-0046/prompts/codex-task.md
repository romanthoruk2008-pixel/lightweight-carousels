# Codex task — LW-CAR-0046 "gym green flags" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0046/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 gym green flags, the positive sister of the approved LW-CAR-0038, each one slide. 9 slides. Every word comes from this file and copy.json.

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
- Next to the number, a small solid flag icon in **#3FCF5E green** (the C-tier green of our tier lists): a simple flag on a short pole. Draw it; never use an emoji. No coloured muscles on the figures.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `gym` / `green flags` (marker) / `(be this person)` | front view from the thighs up, smiling posture, one thumb up, holding a large solid #3FCF5E green flag on a short pole next to him |
| 2 | item | `#1` `re-racks every weight` (marker) / `leaves the gym better than they found it.` | sliding a weight plate back onto a weight tree, front three-quarter view |
| 3 | item | `#2` `trains legs every week` (marker) / `no skipping, no excuses.` | barbell back squat in a rack, bottom position, side view |
| 4 | item | `#3` `helps beginners` (marker) / `only when they ask, and always kindly.` | one figure calmly showing a second, slimmer figure how to hold a dumbbell, both friendly, front view |
| 5 | item | `#4` `warms up first` (marker) / `light sets before the heavy ones, every time.` | barbell back squat with an empty bar, relaxed, side view |
| 6 | item | `#5` `shares the equipment` (marker) / `lets you work in between sets.` | one figure stepping away from a cable machine and gesturing to a second figure to use it, front view |
| 7 | item | `#6` `hypes up other people` (marker) / `cheers on strangers like old friends.` | clapping next to a second figure who just finished a deadlift at the top, front view |
| 8 | item | `#7` `tracks every workout` (marker) / `knows their numbers without guessing.` | standing next to a squat rack, looking down at a phone held in both hands (screen not visible), calm, front view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `be the green flag` and `every set`:
  `be the green flag. track every set in harda.`
- Body, regular #2A2A2A: `log your workouts and always know what to beat next time.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
