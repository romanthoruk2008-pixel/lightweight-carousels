# Codex task — LW-CAR-0084 "how to get wider" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0084/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 5 exercises that add width, each with a 'do:' cue. 7 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Item slide layout (slides 2–6, one identical layout)
- Copy the layout of the approved `carousels/LW-CAR-0029/outputs/slide-02.png`: label and headline in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind the headline only, body line in regular #2A2A2A, then (where the table has one) the small bold #F26445 label followed by its text in regular #2A2A2A. Lower ~55%: the big white figure from the table.
- After the body line, the small bold #F26445 label `do:` followed by the cue in regular #2A2A2A, as on the approved `carousels/LW-CAR-0052/outputs/slide-02.png`.
- The figure does the exercise **with the named muscle filled #F26445**.
- **Figures always wear the opaque #2A2A2A shorts and are shown doing an exercise or standing in a neutral pose**, never in a close physique pose. If a slide is rejected by the safety system, follow the retry rule in `carousels/CODEX-SERIES-RULES.md`.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `how to get` / `wider` (marker) / `(5 moves that add width)` | front view from the thighs up, doing a dumbbell lateral raise at the top; side delts filled #F26445 |
| 2 | item | `#1` `cable lateral raise` (marker) / `constant tension on your side delts the whole rep.` / `do:` `stand side-on and lead with your elbow.` | standing side-on to a low cable, raising one arm out to the side, front view; **side delts filled #F26445** |
| 3 | item | `#2` `dumbbell lateral raise` (marker) / `the classic width builder.` / `do:` `light weight, stop at shoulder height, no swinging.` | standing dumbbell lateral raise at the top, front view; **side delts filled #F26445** |
| 4 | item | `#3` `wide-grip pull-ups` (marker) / `they build the lats that spread your back.` / `do:` `pull your elbows down to your sides.` | wide-grip pull-up at the top, rear view; **lats filled #F26445** |
| 5 | item | `#4` `single-arm cable pulldown` (marker) / `each lat works on its own through a big range.` / `do:` `drive your elbow down to your hip.` | kneeling below a high cable, pulling a single handle down to the side, rear three-quarter view; **lats filled #F26445** |
| 6 | item | `#5` `reverse pec deck` (marker) / `rear delts round out your shoulders from the side.` / `do:` `pull out wide, not back.` | seated reverse pec deck, arms opening wide, rear view; **rear delts filled #F26445** |
| 7 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set` and `never gets skipped`:
  `harda tracks every set, so your width work never gets skipped.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
