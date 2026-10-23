# Codex task — LW-CAR-0040 "why you keep quitting the gym" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0040/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 reasons people quit the gym, each with a fix. The format of the approved LW-CAR-0029. 9 slides. Every word comes from this file and copy.json.

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


## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `why you keep` / `quitting the gym` (marker) / `(and how to stop)` | front view from the thighs up, holding a gym bag and looking back over the shoulder toward the viewer, half-turned away as if leaving |
| 2 | item | `#1` `you start too hard` (marker) / `five days a week from zero burns you out fast.` / `fix:` `start with 2-3 days a week.` | lying on a mat, exhausted, arms spread out, side view |
| 3 | item | `#2` `you have no plan` (marker) / `you walk in and don’t know what to do.` / `fix:` `follow one simple plan.` | standing in the gym looking around confused, front view |
| 4 | item | `#3` `you can’t see progress` (marker) / `it feels like nothing changes.` / `fix:` `write down every workout and look back each month.` | looking at the own flexed arm in a mirror, unsure, three-quarter view; **biceps filled #F26445** |
| 5 | item | `#4` `you wait for motivation` (marker) / `motivation comes and goes.` / `fix:` `pick fixed days and times, like a meeting.` | sitting on a sofa-like plain bench at home in sports clothes, chin on one hand, not moving, side view |
| 6 | item | `#5` `you compare yourself to others` (marker) / `their year five against your week two.` / `fix:` `compare yourself to last month only.` | two figures side by side: a much bigger one flexing, and a smaller one glancing at him and looking down, front view |
| 7 | item | `#6` `one missed day turns into a month` (marker) / `skipping once quietly becomes the habit.` / `fix:` `never miss twice in a row.` | walking past the gym door with a bag, looking away, side view |
| 8 | item | `#7` `the goal feels too far away` (marker) / `‘look like that’ feels impossible.` / `fix:` `aim for small wins, like one more rep.` | doing a dumbbell curl with a small proud smile-like posture, one more rep, front view; **biceps filled #F26445** |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every workout` and `how far you’ve come`:
  `harda tracks every workout, so you can see how far you’ve come.`
- Body, regular #2A2A2A: `log your workouts and look back at every one you’ve done.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
