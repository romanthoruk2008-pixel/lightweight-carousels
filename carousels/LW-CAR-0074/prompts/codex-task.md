# Codex task — LW-CAR-0074 "types of gym buddies" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0074/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 types of gym buddies, light humour, each one slide. 9 slides. Every word comes from this file and copy.json.

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
- Most slides show **two white figures**; draw both in the same S2 style. No coloured muscles. Keep the humour friendly; nobody looks mocked.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `types of` / `gym buddies` (marker) / `(tag yours)` | two figures from the thighs up, front view, giving each other a fist bump, a towel over one shoulder |
| 2 | item | `#1` `the hype man` (marker) / `screams ‘one more’ when you’ve already done three more.` | one figure shouting encouragement with both fists up, next to a second figure doing a flat barbell bench press, side three-quarter view |
| 3 | item | `#2` `the one who always cancels` (marker) / `‘can’t today, bro.’ every single time.` | standing alone next to a squat rack, looking down at a phone held in one hand (screen not visible), disappointed posture, front view |
| 4 | item | `#3` `the coach` (marker) / `has a tip for every rep you do. asked or not.` | one figure pointing and explaining to a second figure doing a goblet squat, front view |
| 5 | item | `#4` `the talker` (marker) / `one set, twenty minutes of conversation.` | two figures sitting on a flat bench chatting, a pair of dumbbells untouched on the floor, front view |
| 6 | item | `#5` `the competitor` (marker) / `whatever you lift, they add a plate.` | two figures at two side-by-side squat racks, one sliding an extra plate onto the bar while glancing at the other, front view |
| 7 | item | `#6` `the silent one` (marker) / `headphones in, no words, best workout of your week.` | two figures training side by side, both wearing plain black over-ear headphones, focused, one doing a dumbbell row and one a dumbbell curl, front view |
| 8 | item | `#7` `the perfect one` (marker) / `shows up on time, spots you, re-racks, goes home.` | one figure calmly spotting a second figure doing a flat barbell bench press, side three-quarter view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `your buddy cancels`:
  `harda tracks every set you lift, even when your buddy cancels.`
- Body, regular #2A2A2A: `log your workouts and keep showing up.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
