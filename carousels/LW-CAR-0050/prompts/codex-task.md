# Codex task — LW-CAR-0050 "gym pet peeves" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0050/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 things that annoy everyone at the gym, each one slide. 9 slides. Every word comes from this file and copy.json.

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
- No coloured muscles on the figures. Small #F26445 effect lines only where the table says so. Friendly humour; nobody looks ugly.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `gym` / `pet peeves` (marker) / `(what annoys everyone)` | front view from the thighs up, arms crossed, deeply unimpressed expression in the posture, one eyebrow raised |
| 2 | item | `#1` `blocking the dumbbell rack` (marker) / `standing right in front of it for the whole set.` | doing a dumbbell curl directly in front of a dumbbell rack while a second figure waits behind him, front view |
| 3 | item | `#2` `sweat left on the bench` (marker) / `a towel exists for a reason.` | pointing at a flat bench with a few drawn sweat drops on it, disgusted, side view |
| 4 | item | `#3` `video calls at full volume` (marker) / `the whole gym is now in the meeting.` | sitting on a bench holding a phone up at arm’s length as if on a video call (screen not visible), small #F26445 sound lines, front view |
| 5 | item | `#4` `one person, three machines` (marker) / `a bench, a rack and a cable, all ‘in use’.` | standing between a flat bench, a squat rack and a cable machine with a towel or bottle on each, arms spread to claim them, front view |
| 6 | item | `#5` `weights left everywhere` (marker) / `plates on the bar, dumbbells on the floor.` | a loaded barbell left in a rack and dumbbells scattered on the floor, a figure walking away whistling, side view |
| 7 | item | `#6` `dropping weights for attention` (marker) / `the loud drop after a light set.` | dropping two light dumbbells to the floor from shoulder height, small #F26445 impact lines, front view |
| 8 | item | `#7` `curls in the squat rack` (marker) / `the only rack in the gym, used for curls.` | doing a barbell curl inside a squat rack while a second figure waits nearby with arms crossed, front view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `short and focused`:
  `harda tracks every set you lift, so your sessions stay short and focused.`
- Body, regular #2A2A2A: `log your workouts and get in and out.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
