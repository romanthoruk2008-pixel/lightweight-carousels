# Codex task — LW-CAR-0036 "secretly killing your gains" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0036/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A 7-point list of hidden habits that slow muscle growth, each with a fix. The sister of the approved LW-CAR-0029 (why you’re not growing). 9 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Slide layout (slides 2–8, one identical layout)
- Exactly the layout of the approved `carousels/LW-CAR-0029/outputs/slide-02.png`: number and headline in the heaviest lowercase grotesk #2A2A2A with the marker bar behind the headline only, body line in regular #2A2A2A, then `fix:` in bold #F26445 followed by the fix in regular #2A2A2A.
- Lower ~55%: the big white figure from the table. No coloured muscles on these slides.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `secretly killing` / `your gains` (marker) / `(7 things nobody tells you)` | front view from the thighs up, looking down at the own flexed arm with a frown, the flexed biceps filled #F26445, a small #F26445 crack line drawn over the biceps |
| 2 | thing | `#1` `cardio right before lifting` (marker) / `you start your heavy sets already tired.` / `fix:` `lift first. do cardio after, or on another day.` | running on a treadmill, side view |
| 3 | thing | `#2` `rushing every rep` (marker) / `fast reps let momentum do the work.` / `fix:` `control the weight on the way down.` | standing barbell curl, swinging the body back to lift the bar, side view |
| 4 | thing | `#3` `endless phone breaks` (marker) / `rest turns into ten minutes and the workout falls apart.` / `fix:` `set a rest timer and stick to it.` | sitting on a flat bench scrolling a phone (screen not visible), dumbbells untouched on the floor, side view |
| 5 | thing | `#4` `skipping your warm-up` (marker) / `cold muscles mean weaker first sets.` / `fix:` `do a few light sets before the heavy ones.` | barbell back squat in a rack with an empty bar, light warm-up set, side three-quarter view |
| 6 | thing | `#5` `copying someone else’s plan` (marker) / `their plan fits their body, their schedule and their level.` / `fix:` `pick a plan that fits your week.` | standing, holding a phone up and copying the pose shown on it, unsure (screen not visible), front three-quarter view |
| 7 | thing | `#6` `big nights out every weekend` (marker) / `a few heavy nights can undo a week of training.` / `fix:` `keep drinking to the occasional one.` | sitting slumped and tired on a gym bench with the head in one hand, side view |
| 8 | thing | `#7` `training 7 days a week` (marker) / `no rest days means no time to recover.` / `fix:` `take at least one or two rest days a week.` | lying on a mat, exhausted, arms spread out, side view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `actually working`:
  `harda tracks every set you lift, so you can see what’s actually working.`
- Body, regular #2A2A2A: `log your workouts and spot what’s holding you back.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Place the hand and phone low enough that every line of body text is fully visible with a clear gap above the phone; it may run off the bottom edge.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
