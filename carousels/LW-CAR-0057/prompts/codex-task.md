# Codex task — LW-CAR-0057 "gym zodiac signs" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0057/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The 12 zodiac signs as gym-goers, light humour, one sign per slide. 14 slides. Every word comes from this file and copy.json.

## Templates (design only, never words)
- LW-CAR-0022 (legs tier list) is **owner-approved**, carries the Harda logo and is the S2 reference. Match its look exactly: `carousels/LW-CAR-0022/outputs/`. Cover → its slide 1 (headline, marker, italic subtitle, figure). Text + figure slides → its slide 3 (heavy lowercase headline top-left with a marker bar, body line, big white figure). Ending → its slide 19 (same hand, phone and real screenshot).
- The four approved tier lists (LW-CAR-0020 … 0023) and this carousel must look like one profile.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words and the `vs` badge. Coloured muscles only where the table says so.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Body clean regular sans, #2A2A2A, left-aligned. Subtitles and small hints italic regular #6B6B6B.

## Item slide layout (slides 2–13, one identical layout)
- Copy the layout of the approved `carousels/LW-CAR-0029/outputs/slide-02.png`: label and headline in the heaviest lowercase grotesk #2A2A2A with the #F26445 marker bar behind the headline only, body line in regular #2A2A2A, then (where the table has one) the small bold #F26445 label followed by its text in regular #2A2A2A. Lower ~55%: the big white figure from the table.
- Next to each sign’s name, draw that sign’s simple astrological symbol (♈ ♉ ♊ ♋ ♌ ♍ ♎ ♏ ♐ ♑ ♒ ♓ in order) as a small solid #F26445 line icon. Draw it; never use an emoji. No coloured muscles on the figures.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `gym` / `zodiac signs` (marker) / `(find yours)` | front view from the thighs up, arms crossed, a ring of the twelve small #F26445 zodiac symbols arranged around the head like a halo |
| 2 | item | `#1` `aries` (marker) / `goes for a new max on day one.` | barbell bench press, pushing a very heavy bar, determined, side view |
| 3 | item | `#2` `taurus` (marker) / `same routine for five years. will not change it.` | barbell back squat, calm and stubborn, side view |
| 4 | item | `#3` `gemini` (marker) / `starts a new program every single week.` | standing between a squat rack and a cable machine, looking at both, front view |
| 5 | item | `#4` `cancer` (marker) / `only trains with their gym buddy. alone? never.` | two figures giving each other a high five between sets, front view |
| 6 | item | `#5` `leo` (marker) / `trains for the mirror. and the camera.` | flexing in front of a plain mirror with a phone on a small tripod nearby, side view |
| 7 | item | `#6` `virgo` (marker) / `tracks every set, every rep, every rest.` | standing next to a rack, checking a phone held in both hands (screen not visible), focused, front view |
| 8 | item | `#7` `libra` (marker) / `can’t pick dumbbells or cables, so does both.` | holding a dumbbell in one hand and a cable handle in the other, undecided, front view |
| 9 | item | `#8` `scorpio` (marker) / `headphones in, no talking, terrifying focus.` | heavy deadlift at the top, plain black over-ear headphones on, intense, side view |
| 10 | item | `#9` `sagittarius` (marker) / `skips the gym for a hike and calls it training.` | walking with a small backpack, relaxed, side view |
| 11 | item | `#10` `capricorn` (marker) / `5am. every day. no excuses.` | barbell back squat in an empty gym, a simple wall clock showing 5:00, side view |
| 12 | item | `#11` `aquarius` (marker) / `invents exercises nobody has ever seen.` | doing a strange balance pose with a dumbbell on one leg, playful, front view |
| 13 | item | `#12` `pisces` (marker) / `comes for the vibes and the playlist.` | walking slowly on a treadmill with plain black over-ear headphones, dreamy posture, side view |
| 14 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `be a virgo about it` and `every set you lift`:
  `be a virgo about it. harda tracks every set you lift.`
- Body, regular #2A2A2A: `log your workouts, whatever your sign.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
