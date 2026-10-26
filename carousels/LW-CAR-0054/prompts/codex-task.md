# Codex task — LW-CAR-0054 "if muscles were people" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0054/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 muscles described as people with personalities, each one slide. 9 slides. Every word comes from this file and copy.json.

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
- Each slide shows the white figure acting out the muscle’s personality, **with that muscle filled #F26445**.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `if muscles` / `were people` (marker) / `(which one are you?)` | front view from the thighs up, flexing one arm and confident posture; biceps, shoulders and abs filled #F26445 |
| 2 | item | `#1` `biceps` (marker) / `the show-off. flexes in every mirror and every photo.` | front double biceps pose, proud; **biceps filled #F26445** |
| 3 | item | `#2` `calves` (marker) / `the stubborn one. you train them for years and they don’t care.` | rear view, standing on the toes, arms crossed, stubborn posture; **calves filled #F26445** |
| 4 | item | `#3` `abs` (marker) / `the shy one. always there, just hiding.` | front view, one arm half covering the stomach, shy posture; **abs filled #F26445** |
| 5 | item | `#4` `lower back` (marker) / `the complainer. one bad deadlift and you hear about it all week.` | standing with one hand on the lower back, wincing, side view; **lower back erectors filled #F26445** |
| 6 | item | `#5` `shoulders` (marker) / `the one carrying everyone. in every push and every pull.` | standing barbell overhead press at the top, front view; **delts filled #F26445** |
| 7 | item | `#6` `glutes` (marker) / `the quiet worker. does the heavy lifting while nobody’s looking.` | barbell back squat at the bottom, rear view; **glutes filled #F26445** |
| 8 | item | `#7` `forearms` (marker) / `the loyal friend. at every workout, never gets the credit.` | holding a heavy barbell at the top of a deadlift, grip clearly shown, front view; **forearms filled #F26445** |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `which muscles you’re ignoring`:
  `harda tracks every set you lift and shows which muscles you’re ignoring.`
- Body, regular #2A2A2A: `log your workouts and give every muscle its turn.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
