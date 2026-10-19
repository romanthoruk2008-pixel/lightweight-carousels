# Codex task — LW-CAR-0020 "chest tier list" v1.1 (REF-008 look, our own ranking)

First read `carousels/CODEX-SERIES-RULES.md` for format, saving, manifest, logo file, backgrounds (solid, never transparent), the **white figure rule**, phone ending, no added punctuation and no clipped text. Exact copy: `carousels/LW-CAR-0020/copy.json` (**content_version 1.2**). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** We take the **look and format** of REF-008 (a chest exercise tier list), but the exercises, ranking, text and caption are **our own**. Copy the design from the reference. Take every word and every exercise from this file and copy.json, never from the reference. Where this task differs from the series rules (typography), this task wins.

## Reference images (design only)
`references/images/REF-008/slide-NN.jpg`. They are TikTok web-viewer screenshots: the slide is the tall white area on the left (about x 139–1073). Ignore all TikTok UI (search bar, arrows, pager dots, the dark right panel).

| Our slide type | Copy the layout of |
|---|---|
| cover | `slide-01.jpg` |
| tier divider | `slide-02.jpg` (same for every tier) |
| exercise | `slide-03.jpg` (headline, stars, text, big figure) |

Some of our exercises also appear in the reference; for those you may use the reference slide as a pose guide: db flys `slide-06.jpg`, push-ups `slide-07.jpg`, barbell bench press `slide-10.jpg`, seated cable fly `slide-14.jpg`, incline smith press `slide-16.jpg`, pec deck `slide-17.jpg`.

## Look
- **Background:** solid **#F0F1EB** (`CLEAN`), no texture, opaque.
- **Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, pasted with its own transparency. Keep the top 110 px free of everything else.
- **Figure:** as in the reference: a realistic **white / light-grey** anatomical mannequin, bald and faceless, fine grey shading, **featureless smooth pelvis**, shorts **#2A2A2A**. On exercise slides no muscle is coloured. On the cover the chest is filled **#F26445**. Equipment black / grey.
- **Accent:** **#F26445** for the marker bars behind words and the filled stars. Empty stars #D6D6D2; a half star is half filled.
- **Tier tiles:** rounded square, big white bold letter with a soft shadow. `S` **#F26445**, `A` #FF9A52, `B` #FFD95A, `C` #3FCF5E, `F` #5BDCE3.
- **Type (match the reference):** headlines very heavy grotesk with tight letter spacing, lowercase exactly as written, #2A2A2A. The marker bar is a flat #F26445 rectangle behind the lower part of the exercise name only, not behind the `#12`. Body lines clean regular sans, #2A2A2A, left-aligned. Tier lines and the cover subtitle italic regular #6B6B6B, centered.

## Slides (exact text)
| # | Type | Text | Stars | Figure |
|---|---|---|---|---|
| 1 | cover | `chest` / `tier list` (marker) / `(ranked worst to best)` | — | front view from the thighs up, hands on hips, chest #F26445 |
| 2 | tier | tile `F` + `tier` / `skip these` | — | — |
| 3 | exercise | `#12` `svend press` / `you feel a burn, but there’s almost no load on your chest.` | 1 | standing, squeezing two small weight plates together in front of the chest, arms extended forward |
| 4 | exercise | `#11` `db pullover` / `more of a lat and shoulder move than a chest builder.` | 1.5 | lying across a flat bench, one dumbbell held with both hands behind the head, arms extended |
| 5 | tier | tile `C` + `tier` / `you can do better` | — | — |
| 6 | exercise | `#10` `db flys` / `the stretch is great, but the top half does almost nothing.` | 2.5 | dumbbell fly on a flat bench, arms wide open |
| 7 | exercise | `#9` `floor press` / `safe and simple, but the short range holds you back.` | 2.5 | lying on the floor, knees bent, pressing two dumbbells up, upper arms near the floor |
| 8 | tier | tile `B` + `tier` / `solid picks` | — | — |
| 9 | exercise | `#8` `push-ups` / `free and anywhere. add a vest or slow reps once they get easy.` | 3 | push-up, side view, low in the frame |
| 10 | exercise | `#7` `barbell bench press` / `great for strength. for pure chest growth, a few options beat it.` | 3.5 | barbell bench press in a rack, front three-quarter view |
| 11 | exercise | `#6` `low-to-high cable fly` / `hits your upper chest and keeps tension the whole rep.` | 3.5 | standing in a cable crossover frame, handles from the low pulleys raised up and together to upper-chest height, front view |
| 12 | tier | tile `A` + `tier` / `worth your time` | — | — |
| 13 | exercise | `#5` `dips` / `huge stretch and easy to load. lean forward for more chest.` | 4 | dip on parallel bars, torso leaning forward, side view |
| 14 | exercise | `#4` `incline db press` / `natural path, and each side has to pull its own weight.` | 4 | dumbbell press on an incline bench, front three-quarter view |
| 15 | exercise | `#3` `seated cable fly` / `steady tension from start to finish, and easy to load.` | 4.5 | seated cable fly on a bench inside a cable crossover frame, front view |
| 16 | tier | tile `S` + `tier` / `build your chest on these` | — | — |
| 17 | exercise | `#2` `incline smith press` / `stable path, so you can add weight week after week.` | 5 | incline bench press in a Smith machine |
| 18 | exercise | `#1` `pec deck` / `the hardest chest squeeze you can get. tension never drops.` | 5 | seated pec deck machine, front view |
| 19 | ending | see below | — | hand + phone |

Keep lowercase and apostrophes (`there’s`) exactly. Do not add capitals or punctuation.

### Slide 19 — product ending
- Composition of the approved `carousels/LW-CAR-0001/outputs/slide-08.png`: text on top, a sketch-style hand holding the tall phone from the bottom right, the phone may run off the bottom edge. Draw the hand in the white style of this carousel.
- Headline, large, lowercase, heaviest grotesk, #2A2A2A, left-aligned, with **#F26445 marker bars** under `every set you lift` and under `which muscles you’re forgetting`:
  `harda tracks every set you lift and shows which muscles you’re forgetting.`
- Body, regular #2A2A2A: `log your workouts and check your muscle balance, so you keep making progress.`
- Phone: the **real Harda Progress / Muscle balance screenshot**, the same one as on the approved LW-CAR-0001 slide 8, true proportions, never squashed. Never generate, redraw or imitate app UI. All text fully visible.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate slides 1, 2 and 3 first, show them to the owner and wait for OK. Then the rest. Commit the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
