# Codex task — rebrand the ending slides: Lightweight → Harda

Read `carousels/CODEX-SERIES-RULES.md` first. The app is now called **Harda**. Claude has already replaced the logo on every generated slide with `assets/logo/harda-logo-full.png`. Only these ending slides still say "Lightweight" in their text. Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

## What to do
For each slide below, **edit the existing slide image** (use it as the input image). Change only the brand word in the text: `Lightweight` → `Harda` (and lowercase `lightweight` → `harda` on LW-CAR-0020 / 0021). Everything else must stay identical: layout, every other word, line breaks where possible, font, sizes, colours, marker bars, background, the hand, the phone and the real screenshot on it. The new word is shorter, so the line may get shorter; do not stretch or re-flow the rest. After editing, paste the logo file again at x 48, y 19, 218 x 71 so it stays pixel-exact, and keep the real app screenshot pixel-exact (paste it back from the input slide if the edit touched it).

| Carousel | Slide | File (input and output) | New text (exact) | copy.json version |
|---|---|---|---|---|
| LW-CAR-0001 | 8 | `carousels/LW-CAR-0001/outputs/slide-08.png` | `Check your progress in Harda to make sure you’re still growing.` | 1.1 |
| LW-CAR-0007 | 8 | `carousels/LW-CAR-0007/outputs/slide-08.png` | `Harda counts your working sets and shows how they're split across every muscle group.` | 1.2 |
| LW-CAR-0008 | 8 | `carousels/LW-CAR-0008/outputs/slide-08.png` | `Log your workouts in Harda.` | 1.1 |
| LW-CAR-0010 | 10 | `carousels/LW-CAR-0010/outputs/slide-10.png` | `Log every workout in Harda and try to beat last week's numbers.` | 1.1 |
| LW-CAR-0012 | 8 | `carousels/LW-CAR-0012/outputs/slide-08.png` | `Log every set in Harda and beat your last session.` | 1.1 |
| LW-CAR-0013 | 9 | `carousels/LW-CAR-0013/outputs/slide-09.png` | `Log every set in Harda. Next time, you'll know exactly what to beat.` | 1.1 |
| LW-CAR-0014 | 9 | `carousels/LW-CAR-0014/outputs/slide-09.png` | `Log every workout in Harda, at home or in the gym.` | 1.1 |
| LW-CAR-0015 | 8 | `carousels/LW-CAR-0015/outputs/slide-08.png` | `Log your workouts in Harda.` | 1.1 |
| LW-CAR-0016 | 9 | `carousels/LW-CAR-0016/outputs/slide-09.png` | `Log your sets in Harda and watch the reps add up.` | 1.1 |
| LW-CAR-0020 | 19 | `carousels/LW-CAR-0020/outputs/slide-19.png` | `harda tracks every set you lift and shows which muscles you’re forgetting.` | 1.2 |
| LW-CAR-0021 | 19 | `carousels/LW-CAR-0021/outputs/slide-19.png` | `harda tracks every set you lift and shows if your back gets enough work.` | 1.1 |

Not in this task: LW-CAR-0005 slide 8 and LW-CAR-0006 slide 8 still wait for the owner's Distribution screenshot; their copy.json already says Harda.

## Saving
Overwrite the slide file in `outputs/`, record the edit in that carousel's `manifest.json` (slide, prompt, attempts, `user_review: pending` for this slide only), rebuild that carousel's ZIP with the new slide, and commit all carousels in **one commit**. Flattened RGB PNG, 1080 x 1350, no transparency. If a limit interrupts you, push what exists and list the slides still to do. No automatic QA or extra regenerations; the owner reviews.
