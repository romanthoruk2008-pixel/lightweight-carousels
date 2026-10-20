# Codex task — LW-CAR-0026 "hardest muscles to grow (ranked)" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0026/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A new S2 format: a countdown of the 7 hardest muscles to grow, #7 → #1, each with a difficulty meter and a quick fix. No tiers, no stars. 9 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Rank slide layout (slides 2–8, one identical layout)
- Top-left under the logo area: the number and the muscle as on the exercise slides of LW-CAR-0022, e.g. `#7` and `side delts` in the heaviest lowercase grotesk, with the #F26445 marker bar behind the muscle name only.
- Under it, the **difficulty meter** in the place where the stars sit on LW-CAR-0022: the small lowercase label `difficulty` in #6B6B6B, then **5 short rounded bars in a row**; the first N bars filled #F26445, the rest #D6D6D2 (N from the table). No numbers on the meter.
- Under it, the body line, regular #2A2A2A, up to two lines.
- Under it, one line: `fix:` in bold #F26445, followed by the fix text in regular #2A2A2A.
- Lower ~55%: a big white anatomical figure in the view from the table, standing, **with only that muscle filled #F26445**.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `hardest muscles` / `to grow` (marker) / `(ranked)` | rear three-quarter view, full body, lats, hamstrings, forearms and calves filled #F26445 |
| 2 | rank | `#7` `side delts` (marker) / meter `difficulty` 3 of 5 / `they respond well, but most people never train them directly.` / `fix:` `lateral raises, slow and out to the side.` | front view from the thighs up, arms relaxed, side delts filled #F26445 |
| 3 | rank | `#6` `upper chest` (marker) / meter `difficulty` 3 of 5 / `flat pressing barely reaches it, so it lags behind.` / `fix:` `start your chest day with an incline press.` | front view from the thighs up, upper chest filled #F26445 |
| 4 | rank | `#5` `hamstrings` (marker) / meter `difficulty` 4 of 5 / `squats don’t cover them. they need their own work.` / `fix:` `add romanian deadlifts and leg curls.` | rear view, full body, hamstrings filled #F26445 |
| 5 | rank | `#4` `lats` (marker) / meter `difficulty` 4 of 5 / `hard to feel at first, so most people pull with their arms.` / `fix:` `think elbows down, not hands down.` | rear view from the thighs up, arms slightly away from the body, lats filled #F26445 |
| 6 | rank | `#3` `abs` (marker) / meter `difficulty` 4 of 5 / `you can train them, but they only show at low body fat.` / `fix:` `train them hard and keep your diet in check.` | front view from the thighs up, abs filled #F26445 |
| 7 | rank | `#2` `forearms` (marker) / meter `difficulty` 5 of 5 / `tough, used all day, and slow to change.` / `fix:` `hammer curls, reverse curls and heavy holds.` | front view from the thighs up, one arm bent showing the forearm, forearms filled #F26445 |
| 8 | rank | `#1` `calves` (marker) / meter `difficulty` 5 of 5 / `you walk on them all day. they need heavy, slow reps.` / `fix:` `slow reps with a pause at the bottom, trained often.` | rear view, full body standing on the toes, calves filled #F26445 |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set` and `the least work`:
  `harda tracks every set and shows which muscles get the least work.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance, so the hard ones get enough too.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long name may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate slides 1, 2 and 3 first, show them to the owner and wait for OK, then the rest. Commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
