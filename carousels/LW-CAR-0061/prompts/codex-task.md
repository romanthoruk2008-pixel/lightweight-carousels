# Codex task — LW-CAR-0061 "what your gym time says about you" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0061/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 6 gym times and what they say about the person, each one slide. 8 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Item slide layout (slides 2–7, one identical layout)
- Copy the layout of the approved `carousels/LW-CAR-0029/outputs/slide-02.png`: label and headline in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind the headline only, body line in regular #2A2A2A, then (where the table has one) the small bold #F26445 label followed by its text in regular #2A2A2A. Lower ~55%: the big white figure from the table.
- Where the table names a time, draw a simple round wall clock showing it. No coloured muscles on the figures.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `what your gym time` / `says about you` (marker) / `(5am people, we see you)` | front view from the thighs up, holding a large simple round alarm clock, eyebrows raised |
| 2 | item | `#1` `5am` (marker) / `empty gym, strong coffee, nobody can stop you.` | squatting in an empty gym, a simple wall clock showing 5:00, side view |
| 3 | item | `#2` `lunch break` (marker) / `forty minutes, no small talk, back at the desk on time.` | doing a quick dumbbell press on a bench, a simple wall clock showing 12:30, front three-quarter view |
| 4 | item | `#3` `6pm after work` (marker) / `every rack taken, but you came anyway.` | waiting next to a busy squat rack used by another figure, a wall clock showing 6:00, front view |
| 5 | item | `#4` `10pm` (marker) / `quiet gym, loud music, slightly unhinged.` | heavy deadlift alone, plain black over-ear headphones, a wall clock showing 10:00, side view |
| 6 | item | `#5` `sunday morning` (marker) / `everyone else is asleep. you are building.` | seated cable row, calm, a wall clock showing 8:00, side view |
| 7 | item | `#6` `whenever i feel like it` (marker) / `no schedule, all vibes. still shows up.` | walking in with a gym bag, relaxed, shrugging, front view |
| 8 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `whenever you train` and `every set you lift`:
  `whenever you train, harda tracks every set you lift.`
- Body, regular #2A2A2A: `log your workouts at 5am or 10pm.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
