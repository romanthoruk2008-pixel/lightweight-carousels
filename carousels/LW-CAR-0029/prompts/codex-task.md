# Codex task — LW-CAR-0029 "why you’re not growing" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0029/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A new S2 checklist: 7 reasons someone isn't building muscle, each with a fix. 9 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

- The reason slides use the layout of the approved `carousels/LW-CAR-0026/outputs/slide-02.png` (number and headline with marker, body line, `fix:` line, big white figure), **without the difficulty meter**.

## Reason slide layout (slides 2–8, one identical layout)
- Top-left: the number and the headline, heaviest lowercase grotesk #2A2A2A, marker bar behind the headline only.
- Under it, the body line, regular #2A2A2A, up to two lines.
- Under it, one line: `fix:` in bold #F26445, followed by the fix text in regular #2A2A2A.
- Lower ~55%: the big white figure from the table. Coloured muscles only where the table says so.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `why you’re` / `not growing` (marker) / `(7 reasons)` | front view from the thighs up, flexing one arm and looking down at it with the head tilted, a little disappointed; the flexed biceps filled #F26445 |
| 2 | reason | `#1` `you don’t track` (marker) / `if you can’t see last week’s numbers, you can’t beat them.` / `fix:` `write down every set, weight and rep.` | sitting on a flat bench between sets, looking down at a phone held in both hands (the screen is not visible) |
| 3 | reason | `#2` `same weights forever` (marker) / `your muscles have no reason to grow.` / `fix:` `add a rep or a little weight each week.` | standing, curling a very small dumbbell, looking bored |
| 4 | reason | `#3` `sets that are too easy` (marker) / `the last hard reps are the ones that count.` / `fix:` `end most sets 1-3 reps short of failure.` | flat barbell bench press, pushing hard at the end of a set, side three-quarter view; **chest filled #F26445** |
| 5 | reason | `#4` `not enough sets` (marker) / `a set here and there won’t build much.` / `fix:` `give every muscle enough hard sets each week.` | pull-up on a bar, rear view; **lats filled #F26445** |
| 6 | reason | `#5` `skipping muscles` (marker) / `some muscles get all the work, others get none.` / `fix:` `balance your week across every muscle.` | front view, standing, from the thighs up: chest and arms filled #F26445, legs plain white (the imbalance is the point) |
| 7 | reason | `#6` `not eating enough` (marker) / `no extra food, no new muscle.` / `fix:` `eat enough protein and a little more food overall.` | sitting at a table with a large plate of chicken, rice and vegetables, side view, no brand names |
| 8 | reason | `#7` `bad sleep` (marker) / `you grow while you recover, not while you lift.` / `fix:` `get a full night of sleep, every night.` | lying asleep on a simple bed with a pillow, side view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `which muscles you’re skipping`:
  `harda tracks every set you lift and shows which muscles you’re skipping.`
- Body, regular #2A2A2A: `log your workouts, beat last week, and keep every muscle in balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long name may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
