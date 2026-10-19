# Codex task — LW-CAR-0023 "biceps tier list" (style S2, our own ranking)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0023/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The next carousel in our tier-list series after LW-CAR-0020 (chest) and LW-CAR-0021 (back), now for biceps. **Same look, same layouts, same type, colours and figure as LW-CAR-0020 and LW-CAR-0021.** Every word and every exercise comes from this file and copy.json.

## Templates
- LW-CAR-0020 and LW-CAR-0021 are **owner-approved** S2 carousels. Match `carousels/LW-CAR-0020/outputs/` exactly: cover → its slide 1, tier dividers → its slide 2, exercise slides → its slide 3, ending → its slide 19. Use `carousels/LW-CAR-0021/outputs/` as a second example (for example how a long exercise name wraps onto two lines). All three carousels must look like one series.
- The tier divider slides have the same text as in LW-CAR-0020 except `S`; you may reuse its F, C, B and A divider slides unchanged.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/lightweight-logo-full.png` at x 48, y 19, 341 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. No coloured muscles on the exercise slides. On the cover the biceps are filled **#F26445**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words, filled stars. Empty stars #D6D6D2; a half star is half filled.
- **Tier tiles:** rounded square, big white bold letter with a soft shadow: `S` **#F26445**, `A` #FF9A52, `B` #FFD95A, `C` #3FCF5E, `F` #5BDCE3.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Marker bar behind the exercise name only, not behind the `#12`. Body clean regular sans, #2A2A2A, left-aligned. Tier lines and cover subtitle italic regular #6B6B6B, centered.

## Slides (exact text)
| # | Type | Text | Stars | Figure |
|---|---|---|---|---|
| 1 | cover | `biceps` / `tier list` (marker) / `(ranked worst to best)` | — | front view from the thighs up, front double biceps pose with both arms flexed, biceps filled #F26445 |
| 2 | tier | tile `F` + `tier` / `skip these` | — | — |
| 3 | exercise | `#12` `band curl` / `almost no tension at the bottom, where your biceps need it.` | 1 | standing on a resistance band, curling the handles, front view |
| 4 | exercise | `#11` `21s` / `a fun burn, but the weight is too light to grow.` | 1.5 | standing barbell curl with a light bar, halfway up, front view |
| 5 | tier | tile `C` + `tier` / `you can do better` | — | — |
| 6 | exercise | `#10` `concentration curl` / `great squeeze, but one arm at a time takes forever.` | 2.5 | seated on a bench, elbow on the inner thigh, curling one dumbbell, front three-quarter view |
| 7 | exercise | `#9` `reverse curl` / `more forearms than biceps.` | 2.5 | standing barbell curl with an overhand grip, halfway up, front view |
| 8 | tier | tile `B` + `tier` / `solid picks` | — | — |
| 9 | exercise | `#8` `barbell curl` / `classic and heavy, but way too easy to swing the weight up.` | 3 | standing barbell curl, bar at chest height, front view |
| 10 | exercise | `#7` `hammer curl` / `makes your arms look thicker, but it’s more brachialis than biceps.` | 3.5 | standing hammer curl with dumbbells, neutral grip, one arm up, front view |
| 11 | exercise | `#6` `chin-ups` / `back and biceps in one move, and no gym needed.` | 3.5 | chin-up on a bar with an underhand grip, chin over the bar, front view |
| 12 | tier | tile `A` + `tier` / `worth your time` | — | — |
| 13 | exercise | `#5` `ez-bar curl` / `easier on your wrists than a straight bar, and just as heavy.` | 4 | standing ez-bar curl, bar at chest height, front view |
| 14 | exercise | `#4` `incline db curl` / `a huge stretch on your biceps. humbling, but it works.` | 4 | seated on an incline bench, arms hanging back, curling two dumbbells, side view |
| 15 | exercise | `#3` `preacher curl` / `no swinging, no cheating. just your biceps.` | 4.5 | seated preacher curl bench, arms on the pad, curling an ez-bar, side view |
| 16 | tier | tile `S` + `tier` / `build your biceps on these` | — | — |
| 17 | exercise | `#2` `cable curl` / `tension from bottom to top, on every single rep.` | 5 | standing cable curl from a low pulley with a straight bar, front view |
| 18 | exercise | `#1` `bayesian cable curl` / `arm behind your body, a big stretch and tension the whole way.` | 5 | standing with the back to a low cable pulley, one arm behind the body curling the handle forward, side view |
| 19 | ending | see below | — | hand + phone |

Keep lowercase, hyphens and apostrophes exactly. Do not add capitals or punctuation. A long exercise name may wrap onto two lines, with the marker bar under each line, as on LW-CAR-0021; never shrink it so far that it looks different from the other slides.

### Slide 19 — product ending (same composition as LW-CAR-0020 / 0021 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone, so the phone never touches the text.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and under `your arms get enough work`:
  `lightweight tracks every set you lift and shows if your arms get enough work.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance, so your arms keep growing.`
- Phone: the **real Lightweight Progress / Muscle balance screenshot** (radar with a Arms axis), the same one as on the approved LW-CAR-0020 / 0021 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate slides 1, 2 and 3 first, show them to the owner and wait for OK, then the rest. Commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
