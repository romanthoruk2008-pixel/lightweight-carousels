# Codex task — LW-CAR-0022 "legs tier list" (style S2, our own ranking)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S2**). Exact copy: `carousels/LW-CAR-0022/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The next carousel in our tier-list series after LW-CAR-0020 (chest) and LW-CAR-0021 (back), now for legs. **Same look, same layouts, same type, colours and figure as LW-CAR-0020 and LW-CAR-0021.** Every word and every exercise comes from this file and copy.json.

## Templates
- LW-CAR-0020 and LW-CAR-0021 are **owner-approved** S2 carousels. Match `carousels/LW-CAR-0020/outputs/` exactly: cover → its slide 1, tier dividers → its slide 2, exercise slides → its slide 3, ending → its slide 19. Use `carousels/LW-CAR-0021/outputs/` as a second example (for example how a long exercise name wraps onto two lines). All three carousels must look like one series.
- The tier divider slides have the same text as in LW-CAR-0020 except `S`; you may reuse its F, C, B and A divider slides unchanged.

## Look (S2)
- **Background:** solid **#F0F1EB** (`CLEAN`), opaque, no texture.
- **Logo:** `assets/logo/lightweight-logo-full.png` at x 48, y 19, 341 x 71, with its own transparency. Top 110 px free of everything else.
- **Figure:** realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. No coloured muscles on the exercise slides. On the cover the quads, adductors and calves are filled **#F26445**. Equipment black / grey.
- **Accent #F26445:** marker bars behind words, filled stars. Empty stars #D6D6D2; a half star is half filled.
- **Tier tiles:** rounded square, big white bold letter with a soft shadow: `S` **#F26445**, `A` #FF9A52, `B` #FFD95A, `C` #3FCF5E, `F` #5BDCE3.
- **Type:** headlines very heavy grotesk, tight spacing, lowercase exactly as written, #2A2A2A. Marker bar behind the exercise name only, not behind the `#12`. Body clean regular sans, #2A2A2A, left-aligned. Tier lines and cover subtitle italic regular #6B6B6B, centered.

## Slides (exact text)
| # | Type | Text | Stars | Figure |
|---|---|---|---|---|
| 1 | cover | `legs` / `tier list` (marker) / `(ranked worst to best)` | — | front view, full body standing, hands on hips, quads, adductors and calves filled #F26445 |
| 2 | tier | tile `F` + `tier` / `skip these` | — | — |
| 3 | exercise | `#12` `bosu ball squat` / `you’re training balance, not legs. the load is way too light.` | 1 | squatting on an upturned bosu ball, arms forward for balance, front three-quarter view |
| 4 | exercise | `#11` `wall sit` / `burns like crazy, but builds very little muscle.` | 1.5 | back flat against a wall, knees bent at 90 degrees, side view |
| 5 | tier | tile `C` + `tier` / `you can do better` | — | — |
| 6 | exercise | `#10` `goblet squat` / `perfect to learn the squat, but your arms give out before your legs.` | 2.5 | goblet squat holding one dumbbell at the chest, bottom position, front three-quarter view |
| 7 | exercise | `#9` `walking lunges` / `they work, but balance limits how hard you can push.` | 2.5 | walking lunge with dumbbells at the sides, mid-step, side view |
| 8 | tier | tile `B` + `tier` / `solid picks` | — | — |
| 9 | exercise | `#8` `back squat` / `a great classic, but it takes a lot out of your lower back and recovery.` | 3 | barbell back squat in a rack, bottom position, side three-quarter view |
| 10 | exercise | `#7` `bulgarian split squat` / `brutal and effective. everyone hates them for a reason.` | 3.5 | bulgarian split squat, rear foot on a flat bench, dumbbells at the sides, side view |
| 11 | exercise | `#6` `lying leg curl` / `the simplest way to isolate your hamstrings.` | 3.5 | lying face down on a leg curl machine, heels pulled up, side view |
| 12 | tier | tile `A` + `tier` / `worth your time` | — | — |
| 13 | exercise | `#5` `romanian deadlift` / `huge stretch for your hamstrings and glutes, and easy to load.` | 4 | barbell romanian deadlift, hips back, bar at the knees, side view |
| 14 | exercise | `#4` `leg extension` / `nothing isolates your quads better. a perfect finisher.` | 4 | seated leg extension machine, legs straight, side view |
| 15 | exercise | `#3` `hip thrust` / `the easiest way to load your glutes heavy.` | 4.5 | barbell hip thrust, upper back on a bench, hips up at the top, side view |
| 16 | tier | tile `S` + `tier` / `build your legs on these` | — | — |
| 17 | exercise | `#2` `hack squat` / `all the squat benefits, with a back pad keeping you stable.` | 5 | hack squat machine, back on the pad, bottom position, side three-quarter view |
| 18 | exercise | `#1` `leg press` / `heavy, stable and easy to push hard every set.` | 5 | seated 45-degree leg press machine, knees bent, side view |
| 19 | ending | see below | — | hand + phone |

Keep lowercase, hyphens and apostrophes exactly. Do not add capitals or punctuation. A long exercise name may wrap onto two lines, with the marker bar under each line, as on LW-CAR-0021; never shrink it so far that it looks different from the other slides.

### Slide 19 — product ending (same composition as LW-CAR-0020 / 0021 slide 19)
- Text on top, the sketch-style hand in the white style holding the tall phone from the bottom right; the phone may run off the bottom edge. Leave a clear gap between the last line of body text and the top of the phone, so the phone never touches the text.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and under `your legs get enough work`:
  `lightweight tracks every set you lift and shows if your legs get enough work.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance, so you never skip leg day again.`
- Phone: the **real Lightweight Progress / Muscle balance screenshot** (radar with a Legs axis), the same one as on the approved LW-CAR-0020 / 0021 slide 19, true proportions, never squashed. Never generate, redraw or imitate app UI.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate slides 1, 2 and 3 first, show them to the owner and wait for OK, then the rest. Commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
