# Codex fix — ending slides where the phone covers the body text

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`. Read `carousels/CODEX-SERIES-RULES.md` first.

**The problem.** On the ending slides below, the phone is placed at a fixed height, but the headline is one line longer than on the approved LW-CAR-0022 slide 19. The body text then runs under the phone: on some slides it is cut in half, on LW-CAR-0034 and LW-CAR-0037 it is not visible at all.

**The reference that is right:** `carousels/LW-CAR-0022/outputs/slide-19.png`. Headline, then the full body text, then a clear gap, then the phone.

## Fix each slide
Edit the existing slide (use it as the input image). Keep the headline, the marker bars, the Harda logo, the hand, the phone and the real screenshot exactly as they are. Change only the layout so that:
1. **Every word of the body text is fully visible**, in regular #2A2A2A (#6B6B6B on the S1 slide LW-CAR-0031), exactly as written in the table.
2. There is a **clear gap of at least 40 px** between the last line of body text and the top edge of the phone.
3. To make room, **move the hand and phone down** (they may run off the bottom edge; the screen may be cut at the bottom). If that is still not enough, make the headline slightly smaller. Never shorten or drop text, never squash the screenshot.

| Carousel | File (input and output) | Body text (exact) |
|---|---|---|
| LW-CAR-0029 | `carousels/LW-CAR-0029/outputs/slide-09.png` | `log your workouts, beat last week, and keep every muscle in balance.` |
| LW-CAR-0031 | `carousels/LW-CAR-0031/outputs/slide-08.png` | `Log your workouts in Harda.` / `See how many sets your core gets compared to every other muscle.` |
| LW-CAR-0033 | `carousels/LW-CAR-0033/outputs/slide-09.png` | `log your workouts and compare this month with the last one.` |
| LW-CAR-0034 | `carousels/LW-CAR-0034/outputs/slide-09.png` | `log your workouts and keep leveling up.` |
| LW-CAR-0035 | `carousels/LW-CAR-0035/outputs/slide-19.png` | `log your workouts and watch your reps go up.` |
| LW-CAR-0036 | `carousels/LW-CAR-0036/outputs/slide-09.png` | `log your workouts and spot what’s holding you back.` |
| LW-CAR-0037 | `carousels/LW-CAR-0037/outputs/slide-08.png` | `log your workouts and know every number.` |

After each fix: paste `assets/logo/harda-logo-full.png` again at x 48, y 19, 218 x 71, keep the screenshot pixels exact, record the edit in that carousel's `manifest.json` (`user_review: pending` for this slide), rebuild that carousel's ZIP. Commit all seven fixes in **one commit**. Opaque flattened RGB PNG, 1080 x 1350. No other slides change.

## For all future carousels
Before placing the phone, measure where the body text ends and put the phone below it. Never place the phone at a fixed height.
