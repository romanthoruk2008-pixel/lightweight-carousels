# Codex task — LW-CAR-0069 "gym tips that feel illegal to know" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0069/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 simple gym tips that feel too good to be allowed, each with a 'do:' line. 9 slides. Every word comes from this file and copy.json.

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
- After the body line, the small bold #F26445 label `do:` followed by the tip in regular #2A2A2A, as on the approved `carousels/LW-CAR-0052/outputs/slide-02.png`.
- No coloured muscles on the figures. Small #F26445 marks only where the table says so. Phones show no screen.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `gym tips that feel` / `illegal to know` (marker) / `(save this before your next workout)` | front view from the thighs up, holding a small closed notebook to the chest and looking around sneakily, one finger raised in front of the face in a 'shh' gesture |
| 2 | item | `#1` `slow down the way down` (marker) / `same weight, way harder. no extra plates needed.` / `do:` `take two seconds to lower every rep.` | flat dumbbell bench press, lowering the dumbbells slowly, small #F26445 down arrow beside the arms, side three-quarter view |
| 3 | item | `#2` `film one set from the side` (marker) / `your form looks different from how it feels.` / `do:` `check your depth and your back on video.` | barbell back squat at the bottom, a phone on a small tripod filming from the side (screen not visible), side view |
| 4 | item | `#3` `write down every set` (marker) / `you can’t beat last week if you don’t remember it.` / `do:` `log the weight and reps after each set.` | sitting on a flat bench between sets, typing on a phone held in both hands (screen not visible), front three-quarter view |
| 5 | item | `#4` `add a rep before you add weight` (marker) / `small wins every week turn into big ones.` / `do:` `hit the top of your rep range, then go heavier.` | seated cable row, finishing a rep, focused, side view |
| 6 | item | `#5` `rest longer on big lifts` (marker) / `rushing makes your next set weaker.` / `do:` `rest two to three minutes on squats and presses.` | sitting on a bench next to a loaded squat rack, calm, drinking from a plain water bottle, front view |
| 7 | item | `#6` `train your weakest muscle first` (marker) / `you have the most energy at the start.` / `do:` `put the muscle you skip at the top of your workout.` | standing calf raise machine, up on the toes, side view |
| 8 | item | `#7` `leave one rep in the tank` (marker) / `most sets don’t need to go to failure to work.` / `do:` `stop when the next rep would break your form.` | standing barbell curl, the bar at the top, controlled, front view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `what to beat`:
  `harda tracks every set you lift, so you always know what to beat.`
- Body, regular #2A2A2A: `log your workouts and add one rep next time.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
