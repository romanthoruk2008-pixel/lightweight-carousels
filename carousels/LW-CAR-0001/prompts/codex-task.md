# Codex task — LW-CAR-0001 "WEAK BACK?" (pilot)

You are the visual producer for Harda, a fitness app. Generate one TikTok photo carousel that reproduces the reference carousel REF-007 as closely as possible: the same slides, same order, same text, same composition, same illustrations and poses. Change only what is listed under "Substitutions". Do not add, remove, rewrite or "improve" anything else, including copy that looks wrong. The owner wants it 1:1.

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`. The exact copy is in `carousels/LW-CAR-0001/copy.json` (content_version 1.1). It matches this prompt; if they ever differ, copy.json wins.

## Reference images (slide order)
1. https://github.com/user-attachments/assets/665b9bc5-d7f3-44ef-ba52-e8ea4be6106a
2. https://github.com/user-attachments/assets/9ee19fd9-ef3c-426c-bfaf-8628c5b6b0b7
3. https://github.com/user-attachments/assets/278e33bf-3d2f-42c6-b0fa-5eb5ee7db450
4. https://github.com/user-attachments/assets/9d88a5f8-c9f1-4941-bb29-3893c1b346ac
5. https://github.com/user-attachments/assets/6272b431-ffd9-4b4f-b68b-ef49e9c51226
6. https://github.com/user-attachments/assets/d6056f91-fdad-465b-8f62-3e3319a46686
7. https://github.com/user-attachments/assets/123a918f-53f9-4db2-bb21-569d90cfd3ab
8. https://github.com/user-attachments/assets/a6645f77-62e7-4284-9cf3-ef2d1e527897

These are screenshots of the TikTok web viewer. The slide is the left part. Ignore all TikTok UI: the search bar "Знайти схожий контент" at the top, the arrows and dots at the bottom, the dark right-hand panel with caption and comments. The bottom few percent of each slide are hidden behind the TikTok pager, so keep labels fully visible in your version.

Before generating, open the images and check you can see them. If you cannot open them, stop and tell the owner exactly which slide failed. Do not guess the composition.

## Substitutions (the only changes allowed)
- Accent color: everything bright green in the original becomes **#F26445**. That covers the highlighted muscles, the word "BACK?", the splat under "?", underline bars, number badges, "OR" badges.
- The large pale-green arch shape in the background becomes a pale tint of the accent: **#FBE3DD**.
- Dark text: **#2A2A2A**. Grey body text: **#6B6B6B**. Background stays off-white **#F0F1EB**.
- Font: **Rubik** for all text. Use the heaviest weight for the cover, bold for titles, regular for parentheticals and body. Rubik is wider than the original condensed cover font. Keep the same two-line stacked cover, scale it to fit, and tell the owner if the layout cannot match.
- Logo: place the Harda logo small in the top-left corner of every slide, **only if the owner gives you the logo file**. Never draw or invent a logo. Without the file, leave it out and say so.
- Non-highlighted muscles: warm sand **#D9CBBE** (darker shades of the same sand for shading). No green or sage tint anywhere on the figures. Skin and tendons stay light ivory (about #F5F0E5).
- Slide 8: the Arrow app screen is replaced by a real Harda screenshot (see slide 8).

## Format
- Size: 1080 x 1350 px (4:5), one PNG per slide. The original ratio measured from the screenshots is about 0.79. If the owner says another size, use that.
- All 8 slides must look like one series: same background, arch shape, illustration style, line weights, type sizes and positions.
- Text must be exactly the strings below: spelling, capitalization, punctuation. No extra words, watermarks or signatures.

## Order of work
1. Generate **slide 1**, then **slide 3**: the cover and the list template. Show both to the owner and wait for OK or corrections.
2. After OK, generate slides 2, 4, 5, 6, 7 using slide 3 as the visual master.
3. Slide 8 only after the owner gives the Harda app screenshot and confirms the last line of text.
4. After each slide, record in `carousels/LW-CAR-0001/manifest.json` (create it if it does not exist): slide number, content_version 1.1, the prompt you used, the result file or link, attempt count, errors, save status. Set `agent_visual_review` to `not_performed` and `user_review` to `pending`. No automatic QA, no extra review passes, no automatic regenerations. Only redo a slide when the owner asks.
5. If you hit the image limit, stop, record where you stopped, and tell the owner the next slide to generate.

## Slides

### Global style (all slides)
Off-white background #F0F1EB. A very large pale #FBE3DD rounded arch shape rises in the right half behind the content. Illustrations are semi-realistic anatomical "écorché" renders of a bald, faceless male mannequin: fine linework, non-target muscles warm sand #D9CBBE with ivory skin and tendons, target muscles filled flat #F26445. Gym equipment is realistic black / grey / white. Clean, premium, lots of empty space.

### Slide 1 — hook
- Text, stacked, uppercase, huge, top ~45% of the slide, slightly left of center, with a soft drop shadow:
  - line 1 `WEAK` in #2A2A2A
  - line 2 `BACK?` in #F26445, with a small #F26445 paint-splat dot just under and right of the "?"
- Illustration: rear view of the anatomical man from the hips up in the lower ~60%, overlapping the bottom of the headline a little. His right arm (viewer's right) is raised and flexed in a back double-biceps pose; the other hand rests on the hip. Lats, traps, rear delts and teres are filled #F26445; everything else warm sand #D9CBBE / ivory. Cropped at the bottom edge.
- No other text.

### Slide 2 — map of the back
- Title centered at top: `Let’s Fix That` (bold, #2A2A2A), with a short #F26445 underline bar under it.
- Center: large rear-view torso of the man (head to glutes) with the whole back filled #F26445.
- Four small rounded-rectangle thumbnail cards with thin dark outlines, two on each side. Each shows a mini rear-view upper body with only one muscle in #F26445 and a dark label bar at its bottom with white caps text:
  - top-left `REAR DELTS`
  - top-right `TRAPS`
  - bottom-left `LATS`
  - bottom-right `ERECTORS`
- Thin black leader lines with dot ends connect each card to that muscle on the big figure.

### Slides 3–7 — list template (identical layout)
- Top center: #F26445 circle badge with a white number.
- Below it, centered title in #2A2A2A: muscle name bold, any parenthetical in regular weight.
- Below it, centered subtitle `2-3 Sets x N-N Reps` (semibold, #2A2A2A) with a short #F26445 underline bar under it.
- Middle: cropped rear-view upper back (shoulders to mid-back, no head), centered, with only the target muscle filled #F26445.
- Bottom: two full-body figures doing the exercises, left and right. Between them, a #F26445 circle badge with white `OR`. Under each figure, its label (semibold, #2A2A2A).

| Slide | Badge | Title | Subtitle | Highlighted muscle | Left exercise (label) | Right exercise (label) |
|---|---|---|---|---|---|---|
| 3 | 1 | `Lats (Adduction)` | `2-3 Sets x 6-10 Reps` | lats | seated at a lat pulldown machine, rear view, wide grip — `Lat Pulldown` | hanging pull-up from a bar, rear view, dip belt with a weight plate — `Weighted Pull-ups` |
| 4 | 2 | `Lats (Extension)` | `2-3 Sets x 6-10 Reps` | lats (same crop as slide 3) | seated cable row on a flat bench, side view, close-grip V-handle — `Close-Grip Cable Row` | seated black plate-loaded row machine with chest pad, side view — `Close-Grip Machine Row` |
| 5 | 3 | `Traps` | `2-3 Sets x 6-10 Reps` | upper traps (diamond from neck to mid-back) | chest-supported plate-loaded T-bar row, black frame — `T-Bar Row` | seated white selectorized wide-grip row machine, rear three-quarter view — `Wide-Grip Row` |
| 6 | 4 | `Rear Deltoids` | `2-3 Sets x 8-12 Reps` | rear delts | standing cable reverse fly, crossed cables, rear view, arms out in a T — `Cable Reverse Fly` | seated reverse pec-deck machine, rear view — `Reverse Pec Dec` |
| 7 | 5 | `Erectors` | `2-3 Sets x 8-12 Reps` | lower-back erectors (V at the lumbar area) | 45° hyperextension bench, side view, hands behind head — `Hyperextensions` | barbell hip hinge / Romanian deadlift inside a rack, front three-quarter view — `Hinge Movement`, with a small italic footnote under it: `*Performed on leg day` |

### Slide 8 — product ending (BLOCKED until the owner provides the screenshot)
- Left-aligned headline at top: `Trying to Build Muscle?` (bold, #2A2A2A), short #F26445 underline bar under it.
- Body, two paragraphs, regular, #6B6B6B:
  - `Then you need to be consistently progress overloading.`
  - `Check your progress in Harda to make sure you’re still growing.` (draft; the owner confirms the final wording)
- Lower ~60%: a sketch-style line-art hand (same drawing style as the figures) holds a black smartphone, slightly tilted, from the bottom right. The phone screen shows the **real Harda screenshot** the owner provides, placed into the screen. Do not generate, redraw or imitate app UI, scores or coach cards. If you cannot insert the real screenshot cleanly, say so instead of faking it.

## Caption (for the owner to post, not on any slide)
`The simpliest guide for you to build your entire back! #backday #backworkout #gymtips`
