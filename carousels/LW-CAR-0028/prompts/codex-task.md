# Codex task — LW-CAR-0028 "stop doing this. do this instead" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0028/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A new S2 format: 6 exercise swaps, one per slide (a worse exercise → a better one). 8 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Swap slide layout (slides 2–7, one identical layout)
- **Top band (about the upper 40 %):** small label `stop:` in bold lowercase #6B6B6B, then the bad exercise name in bold lowercase #6B6B6B with **one thick #F26445 line struck through it**. Beside it, on the right, a **small, faded** white figure (about 40 % opacity) doing that exercise, with a round #2A2A2A badge holding a white `✗`.
- A thin #D6D6D2 divider line across the slide.
- **Bottom band:** small label `do this:` in bold lowercase #F26445, then the good exercise name in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind it (as on LW-CAR-0022), then the body line in regular #2A2A2A. Below, the **large, fully visible** white figure doing it, **with the target muscle filled #F26445**.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `stop doing this.` / `do this instead` (marker) | two white mannequins side by side: left, faded to about 40 % opacity, doing an upright row, with a round #2A2A2A badge holding a white `✗`; right, fully visible, doing a dumbbell lateral raise with the side delts filled #F26445 and a round #F26445 badge holding a white `✓` |
| 2 | swap | `stop:` `upright row` (struck) / `do this:` `lateral raise` (marker) / `same wider shoulders, much easier on your joints.` | top: standing, barbell pulled up to chest height with elbows high, front view (faded, small); bottom: standing dumbbell lateral raise, arms at shoulder height, front view, large, **side delts filled #F26445** |
| 3 | swap | `stop:` `behind-the-neck pulldown` (struck) / `do this:` `lat pulldown to the chest` (marker) / `the same lats, without the awkward shoulder angle.` | top: seated lat pulldown, bar pulled down behind the head, rear view (faded, small); bottom: seated lat pulldown, wide bar pulled to the upper chest, rear view, large, **lats filled #F26445** |
| 4 | swap | `stop:` `db flys` (struck) / `do this:` `seated cable fly` (marker) / `tension the whole rep, not just at the bottom.` | top: dumbbell fly on a flat bench, arms wide open, front three-quarter view (faded, small); bottom: seated cable fly on a bench inside a cable crossover frame, front view, large, **chest filled #F26445** |
| 5 | swap | `stop:` `bosu ball squat` (struck) / `do this:` `leg press` (marker) / `real load for your legs instead of a balance act.` | top: squatting on an upturned bosu ball, arms forward for balance, front three-quarter view (faded, small); bottom: seated 45-degree leg press machine, knees bent, side view, large, **quads filled #F26445** |
| 6 | swap | `stop:` `21s` (struck) / `do this:` `incline db curl` (marker) / `a real stretch and a real weight.` | top: standing barbell curl with a light bar, halfway up, front view (faded, small); bottom: seated on an incline bench, arms hanging back, curling two dumbbells, side view, large, **biceps filled #F26445** |
| 7 | swap | `stop:` `crunches` (struck) / `do this:` `hanging leg raise` (marker) / `a bigger range for your abs, and no neck pulling.` | top: crunch on a mat, hands behind the head, side view (faded, small); bottom: hanging from a pull-up bar, straight legs raised to hip height, side view, large, **abs filled #F26445** |
| 8 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `actually works`:
  `harda tracks every set you lift, so you see which swap actually works for you.`
- Body, regular #2A2A2A: `log your workouts and watch your numbers go up.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long name may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
