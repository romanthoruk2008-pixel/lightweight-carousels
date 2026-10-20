# Codex task — LW-CAR-0024 "1 exercise per muscle" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0024/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A new S2 format, not a tier list: for 10 muscles, the one exercise we would keep if we could only pick one. 12 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Muscle slide layout (slides 2–11, one identical layout)
- Top-left under the logo area: the **muscle name** as a small bold lowercase heading in #6B6B6B (for example `chest`).
- Under it, the **exercise name** large, heaviest grotesk, lowercase, #2A2A2A, with the #F26445 marker bar behind it, exactly like the exercise names on LW-CAR-0022.
- Under it, the body line, regular #2A2A2A, up to two lines. No stars on these slides.
- Lower ~60%: the big white figure doing the exercise. **On these slides the target muscle is filled #F26445** on the figure, so the viewer sees at once which muscle the slide is about. Everything else on the figure stays white / light grey.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `1 exercise` / `per muscle` (marker) / `(if you could only pick one)` | front view, full body standing, arms relaxed slightly away from the body, chest, shoulders, arms, abs and quads filled #F26445 (the whole body lit up) |
| 2 | muscle | `chest` / `incline smith press` (marker) / `hits your whole chest, and it’s easy to add weight every week.` | incline bench press in a Smith machine, front three-quarter view; **chest filled #F26445** |
| 3 | muscle | `back` / `pull-ups` (marker) / `width and thickness in one move, and you can do them anywhere.` | pull-up on a bar, chin near the bar, rear view; **lats and upper back filled #F26445** |
| 4 | muscle | `shoulders` / `lateral raise` (marker) / `side delts make you look wider, and your presses barely touch them.` | standing dumbbell lateral raise, arms at shoulder height, front view; **side delts filled #F26445** |
| 5 | muscle | `biceps` / `bayesian cable curl` (marker) / `arm behind your body, a big stretch and tension the whole way.` | standing with the back to a low cable pulley, one arm behind the body curling the handle forward, side view; **biceps filled #F26445** |
| 6 | muscle | `triceps` / `overhead cable extension` (marker) / `trains the long head in a big stretch, the part most people miss.` | standing facing away from a cable station, rope held behind the head, extending the arms overhead, side view; **triceps filled #F26445** |
| 7 | muscle | `quads` / `leg press` (marker) / `heavy and stable, so your quads do all the work.` | seated 45-degree leg press machine, knees bent, side view; **quads filled #F26445** |
| 8 | muscle | `hamstrings` / `romanian deadlift` (marker) / `stretches and loads your hamstrings and glutes together.` | barbell romanian deadlift, hips back, bar at the knees, side view; **hamstrings and glutes filled #F26445** |
| 9 | muscle | `glutes` / `hip thrust` (marker) / `your glutes do the work, and it’s easy to go heavy.` | barbell hip thrust, upper back on a bench, hips up at the top, side view; **glutes filled #F26445** |
| 10 | muscle | `calves` / `standing calf raise` (marker) / `slow reps and a full stretch at the bottom. that’s the whole secret.` | standing calf raise machine, up on the toes, side view; **calves filled #F26445** |
| 11 | muscle | `abs` / `hanging leg raise` (marker) / `a big range for your abs, and no machine needed.` | hanging from a pull-up bar, straight legs raised to hip height, side view; **abs filled #F26445** |
| 12 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `which muscles fall behind`:
  `harda tracks every set you lift and shows which muscles fall behind.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance, so no muscle gets left out.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long name may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate slides 1, 2 and 3 first, show them to the owner and wait for OK, then the rest. Commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
