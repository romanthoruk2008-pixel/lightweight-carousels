# Codex task — LW-CAR-0021 "back tier list" (style S2, our own ranking)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0021/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The sister carousel of LW-CAR-0020 (chest tier list), now for the back. **Same look, same layouts, same type, colours and figure as LW-CAR-0020.** Every word and every exercise comes from this file and copy.json.

## Templates
- LW-CAR-0020 is **owner-approved** and is the S2 master. Match `carousels/LW-CAR-0020/outputs/` exactly: cover → its slide 1, tier dividers → its slide 2, exercise slides → its slide 3, ending → its slide 19. The two carousels must look like one series.
- Do not use the REF-008 screenshots; the approved LW-CAR-0020 slides are the template.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/lightweight-logo-full.png` at x 48, y 19, 341 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. No coloured muscles on the exercise slides. On the cover the back is filled **#F26445**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words, filled stars. Empty stars #D6D6D2; a half star is half filled.
- **Tier tiles:** rounded square, big white bold letter with a soft shadow: `S` **#F26445**, `A` #FF9A52, `B` #FFD95A, `C` #3FCF5E, `F` #5BDCE3.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Marker bar behind the exercise name only, not behind the `#12`. Body clean regular sans, #2A2A2A, left-aligned. Tier lines and cover subtitle italic regular #6B6B6B, centered.

## Slides (exact text)
| # | Type | Text | Stars | Figure |
|---|---|---|---|---|
| 1 | cover | `back` / `tier list` (marker) / `(ranked worst to best)` | — | **rear view** from the thighs up, arms slightly away from the body (relaxed lat spread), lats, traps, rear delts and rhomboids filled #F26445 |
| 2 | tier | tile `F` + `tier` / `skip these` | — | — |
| 3 | exercise | `#12` `upright row` / `mostly traps and shoulders, and it’s hard on a lot of joints.` | 1 | standing, barbell pulled up to chest height with elbows high, front view |
| 4 | exercise | `#11` `behind-the-neck pulldown` / `awkward on the shoulders, and the front version works just as well.` | 1.5 | seated at a lat pulldown machine, bar pulled down behind the head, rear view |
| 5 | tier | tile `C` + `tier` / `you can do better` | — | — |
| 6 | exercise | `#10` `straight-arm pulldown` / `nice lat feel, but it’s a finisher, not a builder.` | 2.5 | standing at a cable station with a slight hip hinge, straight arms pushing a bar down to the thighs, side view |
| 7 | exercise | `#9` `inverted rows` / `perfect for beginners, but hard to load as you get stronger.` | 2.5 | under a low bar in a rack, body straight, heels on the floor, chest pulled up to the bar, side view |
| 8 | tier | tile `B` + `tier` / `solid picks` | — | — |
| 9 | exercise | `#8` `deadlift` / `amazing for strength. for back size, it costs a lot of energy.` | 3 | conventional barbell deadlift, standing tall at the top, side three-quarter view |
| 10 | exercise | `#7` `barbell row` / `builds a thick back, but your lower back often gives out first.` | 3.5 | bent-over barbell row, torso hinged forward, bar pulled to the lower chest, side view |
| 11 | exercise | `#6` `single-arm db row` / `easy to load and great for fixing a weaker side.` | 3.5 | one knee and one hand on a flat bench, rowing a dumbbell with the other arm, side view |
| 12 | tier | tile `A` + `tier` / `worth your time` | — | — |
| 13 | exercise | `#5` `pull-ups` / `the king of bodyweight back work. add weight once they get easy.` | 4 | pull-up on a bar, chin near the bar, rear view |
| 14 | exercise | `#4` `seated cable row` / `constant tension and a big stretch for your mid back.` | 4 | seated cable row with a V-handle, side view |
| 15 | exercise | `#3` `lat pulldown` / `easy to learn, easy to load, and great for lat width.` | 4.5 | seated lat pulldown, wide bar pulled to the upper chest, rear view |
| 16 | tier | tile `S` + `tier` / `build your back on these` | — | — |
| 17 | exercise | `#2` `chest-supported t-bar row` / `heavy rows without your lower back doing the work.` | 5 | lying chest-down on a plate-loaded chest-supported T-bar row machine, side three-quarter view |
| 18 | exercise | `#1` `chest-supported machine row` / `nothing to balance, nothing to cheat. just your back pulling.` | 5 | seated chest-supported row machine, chest on the pad, handles pulled back, side view |
| 19 | ending | see below | — | hand + phone |

Keep lowercase, hyphens and apostrophes (`it’s`) exactly. Do not add capitals or punctuation. Long exercise names (`behind-the-neck pulldown`, `chest-supported machine row`) may wrap onto two lines, with the marker bar under each line; never shrink them so far that they look different from the other slides.

### Slide 19 — product ending (same composition as LW-CAR-0020 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone, so the phone never touches the text.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and under `your back gets enough work`:
  `lightweight tracks every set you lift and shows if your back gets enough work.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance, so your back never falls behind.`
- Phone: the **real Lightweight Progress / Muscle balance screenshot** (radar with a Back axis), the same one as on the approved LW-CAR-0001 slide 8, true proportions, never squashed. Never generate, redraw or imitate app UI.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate slides 1, 2 and 3 first, show them to the owner and wait for OK, then the rest. Commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
