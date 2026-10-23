# Codex task — LW-CAR-0037 "beginner vs advanced: how they train" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0037/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 6 side-by-side comparisons of how a beginner and an advanced gym-goer train. 8 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.
- Two-figure slides follow the look of the approved `carousels/LW-CAR-0025/outputs/slide-02.png` (two white figures side by side on one ground line, labels under them), but there is **no answer slide**: each comparison is complete on one slide.

## Two figures, the same on every slide
- **beginner:** the white mannequin, a little slimmer and less muscular, posture a bit unsure. No coloured muscles.
- **advanced:** the same white mannequin, clearly more muscular and confident. No coloured muscles (only the cover uses #F26445 on the figure).

## Comparison slide layout (slides 2–7, one identical layout)
- Top-left under the logo area: the round's headline in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind it.
- Lower ~70%: the two figures side by side, the same size and on the same ground line, each acting out its line (see table).
- Above each figure, its column label: `beginner` in bold lowercase #6B6B6B on the left, `advanced` in bold lowercase #F26445 on the right.
- Under each figure, its line: the beginner line in regular #6B6B6B, the advanced line in regular #2A2A2A. Up to two lines each, fully visible above the bottom edge.
- A thin vertical #D6D6D2 line between the two halves.

Figure ideas per slide (keep them simple and readable): 2 the plan — beginner looking lost between machines / advanced holding a phone like a plan; 3 the weight — beginner swinging a too-heavy barbell curl / advanced doing a clean controlled curl; 4 the rest — beginner sitting slumped scrolling a phone / advanced sitting upright checking a watch; 5 last week — beginner scratching the head / advanced looking at a phone (screens never visible); 6 the muscles — beginner doing a dumbbell curl / advanced doing a squat; 7 the goal — beginner pointing at a calendar page with one week / advanced walking forward calmly.

## Slides (exact text)
| # | Type | Text | Figures |
|---|---|---|---|
| 1 | cover | `beginner vs` / `advanced` (marker) / `(how they really train)` | two white figures side by side on one ground line: left a slimmer, less muscular beginner looking unsure; right a more muscular, confident advanced figure, whose chest and arms are filled #F26445; a round #F26445 `vs` badge with white bold lowercase text between them |
| 2 | round | headline `the plan` (marker) / left `beginner`: `a random workout every day` / right `advanced`: `the same plan for months` | left: the beginner figure acting out the left line; right: the advanced figure acting out the right line |
| 3 | round | headline `the weight` (marker) / left `beginner`: `max weight, messy reps` / right `advanced`: `a weight they can control` | left: the beginner figure acting out the left line; right: the advanced figure acting out the right line |
| 4 | round | headline `the rest` (marker) / left `beginner`: `rests until they feel like it` / right `advanced`: `rests on purpose` | left: the beginner figure acting out the left line; right: the advanced figure acting out the right line |
| 5 | round | headline `last week` (marker) / left `beginner`: `guesses what they lifted` / right `advanced`: `knows every number` | left: the beginner figure acting out the left line; right: the advanced figure acting out the right line |
| 6 | round | headline `the muscles` (marker) / left `beginner`: `chest and arms, every day` / right `advanced`: `every muscle, every week` | left: the beginner figure acting out the left line; right: the advanced figure acting out the right line |
| 7 | round | headline `the goal` (marker) / left `beginner`: `wants results in a month` / right `advanced`: `plays the long game` | left: the beginner figure acting out the left line; right: the advanced figure acting out the right line |
| 8 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `advanced from day one`:
  `harda tracks every set you lift, so you train like you’re advanced from day one.`
- Body, regular #2A2A2A: `log your workouts and know every number.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Place the hand and phone low enough that every line of body text is fully visible with a clear gap above the phone; it may run off the bottom edge.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
