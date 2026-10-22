# Codex task — LW-CAR-0032 "ranking every gym split" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0032/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** A ranking of 6 weekly training splits, #6 → #1. 8 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

- Stars exactly as on LW-CAR-0022: filled #F26445, empty #D6D6D2, a half star half filled.

## Split slide layout (slides 2–7, one identical layout)
- Top-left: the number and the split name, heaviest lowercase grotesk #2A2A2A, marker bar behind the name only (as the exercise slides of LW-CAR-0022).
- Under it, the row of 5 stars, then the body line in regular #2A2A2A.
- Under it, one line: `best for:` in bold #F26445, followed by the text in regular #2A2A2A.
- Lower half: **the week strip**, the main visual. Seven rounded white cards in a grid (two rows: mon–thu and fri–sun, or one row if it fits), thin #D6D6D2 border. Each card has the small day label on top (`mon` … `sun`, bold lowercase #6B6B6B) and the training day below it in bold lowercase. Training days in #2A2A2A on white with a thin #F26445 left edge; `rest` days in #6B6B6B on #F0F1EB with no edge. The text in every card must be exact and fully visible.
- Bottom right, small: one white mannequin in a matching pose (doing a bench press, a squat or a pull-up), overlapping nothing.

## Slides (exact text)
| # | Type | Text | Visual |
|---|---|---|---|
| 1 | cover | `ranking every` / `gym split` (marker) / `(worst to best)` | the white mannequin from the thighs up, front view, holding a small notebook open in one hand like a plan, the other hand on the hip, confident |
| 2 | split | `#6` `bro split` (marker) / stars 2 / `every muscle once a week. fun pumps, slower progress.` / `best for:` `you love one big muscle day` | week strip: `mon` `chest` / `tue` `back` / `wed` `shoulders` / `thu` `arms` / `fri` `legs` / `sat` `rest` / `sun` `rest` |
| 3 | split | `#5` `arnold split` (marker) / stars 3 / `lots of volume, but six days a week is a lot.` / `best for:` `you can train 6 days` | week strip: `mon` `chest + back` / `tue` `shoulders + arms` / `wed` `legs` / `thu` `chest + back` / `fri` `shoulders + arms` / `sat` `legs` / `sun` `rest` |
| 4 | split | `#4` `full body` (marker) / stars 3.5 / `every muscle often, but the sessions get long.` / `best for:` `beginners and busy weeks` | week strip: `mon` `full body` / `tue` `rest` / `wed` `full body` / `thu` `rest` / `fri` `full body` / `sat` `rest` / `sun` `rest` |
| 5 | split | `#3` `upper / lower` (marker) / stars 4 / `every muscle twice a week in just 4 days.` / `best for:` `4 days a week` | week strip: `mon` `upper` / `tue` `lower` / `wed` `rest` / `thu` `upper` / `fri` `lower` / `sat` `rest` / `sun` `rest` |
| 6 | split | `#2` `push pull legs` (marker) / stars 4.5 / `simple, balanced, and works at 3 or 6 days.` / `best for:` `3 or 6 days a week` | week strip: `mon` `push` / `tue` `pull` / `wed` `legs` / `thu` `push` / `fri` `pull` / `sat` `legs` / `sun` `rest` |
| 7 | split | `#1` `upper lower + ppl` (marker) / stars 5 / `every muscle twice a week in 5 days, without the 6-day burnout.` / `best for:` `5 days a week` | week strip: `mon` `upper` / `tue` `lower` / `wed` `rest` / `thu` `push` / `fri` `pull` / `sat` `legs` / `sun` `rest` |
| 8 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `set up your split` and `every set you lift`:
  `set up your split in harda and track every set you lift.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance, so every muscle gets its turn.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long name may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
