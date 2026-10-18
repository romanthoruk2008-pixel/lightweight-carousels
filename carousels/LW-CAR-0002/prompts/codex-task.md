# Codex task — LW-CAR-0002 "STRUCTURE THE PERFECT PUSH DAY"

You are the visual producer for Lightweight. Generate one TikTok photo carousel that reproduces reference REF-001 as closely as possible: same slides, same order, same text, same layout, same illustrations and poses. Change only what is listed under "Substitutions". Do not add, remove, rewrite or "improve" anything, including copy that looks wrong. The owner wants it 1:1.

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`. Exact copy: `carousels/LW-CAR-0002/copy.json` (content_version 1.0); if it ever differs from this prompt, copy.json wins.

**Series master:** the approved slides of LW-CAR-0001 (`carousels/LW-CAR-0001/outputs/slide-01.png` … `slide-07.png`, the warm-sand version). Match them for colors, Rubik type, the Lightweight wordmark (same size and top-left position), illustration style and line weights. Take the **layout** of every slide from REF-001, not from LW-CAR-0001: this source is laid out differently.

## Reference images (real slide order)
1. https://github.com/user-attachments/assets/3ba07508-f8d9-438f-b626-4c09bf2e6c9e
2. https://github.com/user-attachments/assets/63f0c37e-a5e9-49bf-acc9-f506b28a1b0a
3. https://github.com/user-attachments/assets/a2f0fa97-e17c-4351-8619-70e9d9fae13d
4. https://github.com/user-attachments/assets/01a4f31f-2128-4589-aa82-47fc88de873c
5. https://github.com/user-attachments/assets/26896496-ef7d-4dee-9505-ee82e772ff8d
6. https://github.com/user-attachments/assets/a9d5ce22-d17a-471b-be16-3880c2b055c4
7. https://github.com/user-attachments/assets/41384ee6-04dd-4b26-b9dd-9296e03090eb
8. https://github.com/user-attachments/assets/da262fa2-c075-48d1-aa58-8ac9675bf129
9. https://github.com/user-attachments/assets/123f5040-c0c8-41a5-ab3b-3d143053eeb2

Use this order, not the order in CAROUSELS.md: that file lists REF-001 out of order and repeats one slide.

The images are TikTok web-viewer screenshots. The slide is the tall off-white image on the left. Ignore all TikTok UI: the search bar "Знайти схожий контент", the arrows and dots at the bottom, and the dark right panel. Before generating, open the images and confirm you can see them. If you cannot, stop and tell the owner which slide failed. Do not guess.

## Substitutions (the only changes allowed)
- Everything bright green in the original → **#F26445**: highlighted muscles, "PUSH DAY", the "#N" numbers, the short underline bars, the thin vertical divider between the two exercises, "Build Strength & Muscle Faster."
- The pale-green arch in the background → **#FBE3DD**. Background stays **#F0F1EB**.
- Non-highlighted muscles → warm sand **#D9CBBE**, with darker shades of the same sand for shading. No green or sage tint anywhere on the figures. Skin and tendons light ivory (about #F5F0E5).
- Text: dark **#2A2A2A**, grey body **#6B6B6B**.
- Font: **Rubik** for all text. Covers use the heaviest weight, titles bold, body regular. Rubik is wider than the original condensed font. Keep the same line breaks, scale to fit, and tell the owner if the layout cannot match.
- Lightweight wordmark small in the top-left corner of every slide, exactly as on LW-CAR-0001. Never draw or invent a logo.

## Format and saving
- 1080 × 1350 px PNG, one per slide, named `slide-01.png` … `slide-09.png` in `carousels/LW-CAR-0002/outputs/`.
- Keep all labels fully visible. The source has the bottom few percent hidden behind the TikTok pager.
- Text must be exactly the strings below. No extra words, watermarks or signatures.
- Commit the whole carousel as one commit: all slides, prompts, `manifest.json`, `caption.txt`, ZIP. If a limit interrupts you, push what exists marked incomplete and record the next slide.
- Manifest per slide: prompt, result file, attempts, errors, save status. Set `agent_visual_review` to `not_performed` and `user_review` to `pending`. No automatic QA and no automatic regenerations. Redo a slide only when the owner asks.

## Order of work
All 9 slides. Also read `carousels/CODEX-SERIES-RULES.md`: its product-ending rules apply to slide 9.

## Slides

### Global style
Off-white background #F0F1EB with a very large #FBE3DD rounded arch rising in the right half behind the content. Semi-realistic anatomical renders of a bald, faceless male mannequin: fine grey linework, warm sand #D9CBBE muscles, ivory skin and tendons. Equipment is realistic black / grey / white. Clean, lots of empty space.

### Slide 1 — hook
- Three stacked lines of very large uppercase type filling the top ~50%, centered:
  - `STRUCTURE` in #2A2A2A
  - `THE PERFECT` in #2A2A2A
  - `PUSH DAY` in #F26445
- Below: the anatomical man seated on a grey plate-loaded incline/chest press machine with black plates, front view, gripping both handles mid-press. Only the pecs are filled #F26445. Figure in the lower half, cropped at the bottom.

### Slide 2 — checklist
- Top-left, left-aligned two-line bold title `Your Push Day` / `Should Include:` with a short #F26445 underline bar below it.
- Left-aligned bullet list under it, six lines. "1x" regular, the muscle word bold, the bracket regular:
  - `1x Chest (Mid/Low Head)`
  - `1x Chest (Upper Head)`
  - `1x Triceps (Lateral Head)`
  - `1x Triceps (Long Head)`
  - `1x Shoulders (Front Delt)`
  - `1x Shoulders (Side Delt)`
- Bottom right: a half-body front-view figure (head to thighs, one hand on hip, three-quarter view), cropped at the right and bottom edges. Chest and front/side delts filled #F26445.

### Slides 3–8 — list template (identical layout)
- Top-left: big bold `#N` in #F26445 with a short #F26445 underline bar under it.
- To the right of the number: the title, bold, #2A2A2A. Under the title: the sets line, regular, #6B6B6B.
- Under that, full width, left-aligned: one sentence in regular #6B6B6B, wrapping to two lines.
- Bottom ~55%: two full-body figures doing the exercises side by side, separated by a thin vertical #F26445 line (no "OR" badge). Under each, its label in regular #2A2A2A. Exercise figures have no highlighted muscle (all sand), as in the source.

| Slide | Number | Title | Sets line | Sentence | Left figure — label | Right figure — label |
|---|---|---|---|---|---|---|
| 3 | `#1` | `Upper Chest` | `2-3 sets x 6-10 reps` | `Choose one of these exercises to bias your clavicular (upper) chest:` | adjustable incline bench pressing two hex dumbbells — `Incline DB Bench` | plate-loaded incline chest press machine — `Incline Machine Press` |
| 4 | `#2` | `Mid/Low Chest` | `2-3 sets x 6-12 reps` | `Choose one of these exercises to bias your sternocostal (mid/low) chest:` | seated selectorized chest press machine, front view — `Flat Machine Press` | pec deck machine, arms out to the sides — `Pec Dec` |
| 5 | `#3` | `Triceps Lateral Head` | `2-3 sets x 6-12 reps` | `Choose one of these exercises to bias the lateral head of the triceps:` | weighted dips on a dip station, plate on a dip belt — `Triceps Dips` | JM press lying on a flat bench inside a Smith machine — `JM Press` |
| 6 | `#4` | `Triceps Long Head` | `2-3 sets x 8-12 reps` | `Choose one of these exercises to bias the long head of the triceps:` | standing, front view, single-arm cable extension with the elbow at the side — `Triceps Extensions` | standing, rear view, cable overhead extension with a rope — `Overhead Extensions` |
| 7 | `#5` | `Front Delt` | `2-3 sets x 6-10 reps` | `Choose one of these exercises to target your front delts` | seated on an upright bench pressing two dumbbells overhead — `DB Shoulder Press` | plate-loaded seated shoulder press machine — `Machine Shoulder Press` |
| 8 | `#6` | `Side Delt` | `2-3 sets x 8-12 reps` | `Choose one of these exercises to isolate your side delts` | standing, front view, single-arm cable lateral raise from a low pulley — `Cable Lateral Raise` | standing, front view, dumbbell lateral raise, arms out at shoulder height — `DB Lateral Raise` |

Slides 7 and 8 have no colon at the end of the sentence. Keep it that way.

### Slide 9 — product ending
- Top-left: short #F26445 bar, then a two-line left-aligned headline in the heaviest Rubik:
  - `Track Your Workouts.` in #2A2A2A
  - `Build Strength & Muscle Faster.` in #F26445
- Lower ~65%: a sketch-style line-art hand (same drawing style as the figures) holds a black smartphone from the bottom left, slightly tilted. The screen shows the **default real Lightweight screenshot** from the series rules: the Muscle balance screen from approved LW-CAR-0001 slide 8, in its true proportions and never squashed; the phone may run off the bottom edge. If the owner gives a workout-log screenshot, use that instead. Do not generate, redraw or imitate app UI.

## Caption
Write `caption.txt` from copy.json: title, body and hashtags. The 6th item and the hashtags are placeholders; the owner may change them.
