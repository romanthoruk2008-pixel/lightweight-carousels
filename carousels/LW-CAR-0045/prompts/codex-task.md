# Codex task — LW-CAR-0045 "gym bro translator" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0045/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 classic gym-bro phrases and what they really mean, each one slide. 9 slides. Every word comes from this file and copy.json.

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
- Layout per slide: the small bold #F26445 label `they say:`, then the quote as the headline in the heaviest lowercase grotesk with the marker bar (keep the curly quotes), then the small bold #F26445 label `means:` followed by the translation in regular #2A2A2A.
- No coloured muscles on the figures. Friendly humour.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `gym bro` / `translator` (marker) / `(what they say vs what they mean)` | front view from the thighs up, holding a small open dictionary book in one hand, the other hand raised as if explaining, a speech bubble with three dots next to the head |
| 2 | item | `they say:` `“light weight, baby”` (marker) / `means:` `this is the heaviest thing i’ve ever lifted.` | barbell back squat with a very heavily loaded bar, face straining, side view |
| 3 | item | `they say:` `“just warming up”` (marker) / `means:` `this is my max. please don’t ask.` | flat barbell bench press, arms shaking, small #F26445 shake lines, side three-quarter view |
| 4 | item | `they say:` `“i’m on a cut”` (marker) / `means:` `i ate a whole pizza yesterday.` | sitting on a gym bench holding a protein shaker, looking away guiltily, side view |
| 5 | item | `they say:` `“it’s a deload week”` (marker) / `means:` `i didn’t feel like going heavy.` | lifting a very light pair of dumbbells, relaxed, front view |
| 6 | item | `they say:` `“i don’t need a spotter”` (marker) / `means:` `please stay close. just in case.` | lying on a flat bench under a loaded bar, glancing sideways at a second figure standing nearby, side view |
| 7 | item | `they say:` `“one more rep”` (marker) / `means:` `four more reps.` | standing dumbbell curl, holding up one finger with the free hand, front view |
| 8 | item | `they say:` `“i train for strength, not looks”` (marker) / `means:` `still checks the mirror after every set.` | standing next to a squat rack, glancing at a plain mirror and flexing slightly, side view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `never need translating`:
  `harda tracks every set you lift, so your numbers never need translating.`
- Body, regular #2A2A2A: `log your workouts and know what you really lifted.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
