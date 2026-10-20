# Codex task — LW-CAR-0025 "this or that? (gym edition)" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0025/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A new S2 format, not a tier list: 6 rounds of two exercises. Each round is a question slide and then a verdict slide, so viewers guess before they swipe. 14 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Round question slide layout (slides 2, 4, 6, 8, 10, 12, one identical layout)
- Top-left under the logo area: `round N` in the heaviest lowercase grotesk, #2A2A2A (no marker bar on this one).
- Under it, the question, regular #2A2A2A, one line.
- Lower ~65%: **two white figures side by side**, the same size and on the same ground line, each doing its exercise. No coloured muscles. Under each figure, its label in bold lowercase #2A2A2A.
- Between the two figures, a round **#F26445 badge** with white bold lowercase `vs`.
- Bottom center, small italic #6B6B6B: `(answer on the next slide)`. Keep it fully visible above the bottom edge.

## Verdict slide layout (slides 3, 5, 7, 9, 11, 13, one identical layout)
- Top-left: `winner:` in the heaviest lowercase grotesk, #2A2A2A; on the next line the winning exercise, heaviest lowercase, with the #F26445 marker bar behind it (as the exercise names on LW-CAR-0022).
- Under it, the body line, regular #2A2A2A, up to two lines.
- Lower ~60%: the winning exercise as one big white figure, the same pose as on the question slide. No coloured muscles.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `this or` / `that?` (marker) / `(gym edition)` | two white mannequins side by side, the left one holding a barbell across the thighs, the right one holding two dumbbells at the sides, a round #F26445 `vs` badge with white bold lowercase text between them |
| 2 | round 1 | `round 1` / `which builds more chest?` / left label `barbell bench` / badge `vs` / right label `incline db press` / bottom `(answer on the next slide)` | left: barbell bench press in a rack, front three-quarter view; right: dumbbell press on an incline bench, front three-quarter view; same size, side by side |
| 3 | verdict 1 | `winner:` / `incline db press` (marker) / `natural path and more upper chest. the barbell is better for strength.` | the winner, large: dumbbell press on an incline bench, front three-quarter view |
| 4 | round 2 | `round 2` / `which builds bigger quads?` / left label `leg press` / badge `vs` / right label `back squat` / bottom `(answer on the next slide)` | left: seated 45-degree leg press machine, knees bent, side view; right: barbell back squat in a rack, bottom position, side view; same size, side by side |
| 5 | verdict 2 | `winner:` / `leg press` (marker) / `big quad growth with way less lower back fatigue.` | the winner, large: seated 45-degree leg press machine, knees bent, side view |
| 6 | round 3 | `round 3` / `which builds a wider back?` / left label `pull-ups` / badge `vs` / right label `lat pulldown` / bottom `(answer on the next slide)` | left: pull-up on a bar, chin near the bar, rear view; right: seated lat pulldown, wide bar pulled to the upper chest, rear view; same size, side by side |
| 7 | verdict 3 | `winner:` / `lat pulldown` (marker) / `easier to load and to push close to failure. pull-ups are a close second.` | the winner, large: seated lat pulldown, wide bar pulled to the upper chest, rear view |
| 8 | round 4 | `round 4` / `which builds bigger biceps?` / left label `cable curl` / badge `vs` / right label `barbell curl` / bottom `(answer on the next slide)` | left: standing cable curl from a low pulley with a straight bar, front view; right: standing barbell curl, bar at chest height, front view; same size, side by side |
| 9 | verdict 4 | `winner:` / `cable curl` (marker) / `tension from bottom to top, and no swinging the weight up.` | the winner, large: standing cable curl from a low pulley with a straight bar, front view |
| 10 | round 5 | `round 5` / `which builds more chest?` / left label `dips` / badge `vs` / right label `push-ups` / bottom `(answer on the next slide)` | left: dip on parallel bars, torso leaning forward, side view; right: push-up, side view; same size, side by side |
| 11 | verdict 5 | `winner:` / `dips` (marker) / `a bigger stretch and easy to add weight. push-ups get too easy.` | the winner, large: dip on parallel bars, torso leaning forward, side view |
| 12 | round 6 | `round 6` / `which is better for your hamstrings?` / left label `deadlift` / badge `vs` / right label `romanian deadlift` / bottom `(answer on the next slide)` | left: conventional barbell deadlift, standing tall at the top, side view; right: barbell romanian deadlift, hips back, bar at the knees, side view; same size, side by side |
| 13 | verdict 6 | `winner:` / `romanian deadlift` (marker) / `more stretch for your hamstrings and glutes, with less fatigue.` | the winner, large: barbell romanian deadlift, hips back, bar at the knees, side view |
| 14 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `harda tracks every set` and `test both`:
  `not sure which works for you? harda tracks every set, so you can test both.`
- Body, regular #2A2A2A: `log your workouts and see which one actually moves your numbers.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long name may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate slides 1, 2 and 3 first, show them to the owner and wait for OK, then the rest. Commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
