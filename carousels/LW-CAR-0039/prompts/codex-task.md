# Codex task — LW-CAR-0039 "unwritten gym rules" (style S2)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0039/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** 7 unwritten gym etiquette rules, each one slide. 9 slides. Every word comes from this file and copy.json.

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
- The label before each headline is `rule #1` … `rule #7` in small bold lowercase #F26445; the rule itself is the headline with the marker bar. No coloured muscles on the figures.

## Slides (exact text)
| # | Type | Text | Figure |
|---|---|---|---|
| 1 | cover | `unwritten` / `gym rules` (marker) / `(nobody tells you these)` | front view from the thighs up, holding a small open rule book in one hand, the other hand raised with one finger up, calm |
| 2 | item | `rule #1` `re-rack your weights` (marker) / `if you can lift it, you can put it back.` | sliding two weight plates back onto a weight tree, front three-quarter view |
| 3 | item | `rule #2` `wipe down the bench` (marker) / `nobody wants to lie in your sweat.` | wiping a flat bench with a small towel, side view |
| 4 | item | `rule #3` `give people space` (marker) / `don’t stand right behind someone mid-set.` | front view: one figure squatting under a bar in a rack, a second figure standing at a respectful distance with a clear gap |
| 5 | item | `rule #4` `ask how many sets are left` (marker) / `then wait or work in. never just hover.` | standing next to a cable machine with one hand raised in a friendly ask, a second figure seated using it, front three-quarter view |
| 6 | item | `rule #5` `don’t camp on a machine` (marker) / `rest somewhere else so others can use it.` | standing up from a leg press machine, stepping away with a water bottle, side view |
| 7 | item | `rule #6` `no advice nobody asked for` (marker) / `unless someone is about to get hurt.` | one figure pointing and talking at a second figure who is doing a dumbbell curl and looking annoyed, front view |
| 8 | item | `rule #7` `don’t film other people` (marker) / `film yourself, not strangers.` | a phone on a small tripod pointed only at the figure doing a dumbbell press on a bench, side view |
| 9 | ending | see below | hand + phone |

### Ending — product slide (same composition as LW-CAR-0022 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and `before you walk in`:
  `harda tracks every set you lift, so you know your plan before you walk in.`
- Body, regular #2A2A2A: `log your workouts and keep every session simple.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0022 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

Keep lowercase, hyphens, colons and apostrophes exactly. Do not add capitals or punctuation. A long line may wrap onto two lines with the marker bar under each line.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides. Use the approved carousels named above as the visual reference instead. Then write the manifest, the caption and the ZIP, and commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
