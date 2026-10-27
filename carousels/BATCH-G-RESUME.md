# Codex batch G — resume (6 carousels left)

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`. Run `git pull` first.

Batch G stopped after a GitHub push timeout (HTTP 408), not because of a generation problem.

## Already done — do not regenerate
- **LW-CAR-0054** if muscles were people: 9/9 slides, caption, ZIP. Done.
- **LW-CAR-0055** gym playlist says about you: 9/9 slides, caption, ZIP. The slides are fine. Only its `manifest.json` still says `"status": "incomplete"` and `"batch_status": "stopped_after_error"`. Change those to `"status": "complete"` and `"batch_status": "resumed"`, set `next_carousel_to_generate` to `null`, and do not touch any image.

## Still to do, in this order
Read `carousels/BATCH-G.md` (rules for the whole batch), `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` once. Then do each carousel by its own task file:

1. **LW-CAR-0056** — most skipped muscles tier list (17 slides): `carousels/LW-CAR-0056/prompts/codex-task.md`
2. **LW-CAR-0057** — gym zodiac signs (14 slides): `carousels/LW-CAR-0057/prompts/codex-task.md`
3. **LW-CAR-0058** — what your favorite day says about you (9 slides): `carousels/LW-CAR-0058/prompts/codex-task.md`
4. **LW-CAR-0059** — cardio tier list (17 slides): `carousels/LW-CAR-0059/prompts/codex-task.md`
5. **LW-CAR-0060** — post-workout meals tier list (17 slides): `carousels/LW-CAR-0060/prompts/codex-task.md`
6. **LW-CAR-0061** — what your gym time says about you (8 slides): `carousels/LW-CAR-0061/prompts/codex-task.md`

All rules from `carousels/BATCH-G.md` still apply:
- Do not stop for review.
- Words only from `copy.json`.
- Use the Harda logo file.
- Images are opaque RGB, 1080 x 1350.
- On ending slides, put the phone at least 40 px below the body text.
- Finish, commit and push one carousel at a time.
- No automatic QA.

Visual reference for the look: the finished LW-CAR-0049 and LW-CAR-0053 for tier lists; LW-CAR-0054 and LW-CAR-0055 for item slides.

## Music notes and props
Small #F26445 music notes appear **only** where a task file names them. Do not add them to other slides.

## If a push fails (this is what stopped the batch)
A failed push is **not** a reason to stop generating.
1. Retry the push up to 4 times, waiting 2, 4, 8 and 16 s: `git -c http.postBuffer=524288000 push -u origin claude/charming-einstein-xgejky`.
2. If it still fails, split the carousel into smaller commits and push each one:
   1. `outputs/` + `caption.txt` + `manifest.json`
   2. the ZIP
   3. `production-assets/`
3. If even small pushes fail, keep the commits locally and continue with the next carousel. Retry pushing everything after each later carousel.
4. Stop only if generation itself fails. Then push what exists, mark that carousel incomplete in its manifest with the next slide to generate, and stop.

At the end, `git status` must show the branch up to date with `origin`.
