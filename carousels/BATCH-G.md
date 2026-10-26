# Codex batch G — 8 carousels, generate everything in one run

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

Read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` once. Then do these carousels **in this order**, each by its own task file:

1. **LW-CAR-0054** — if muscles were people (9 slides, style S2): `carousels/LW-CAR-0054/prompts/codex-task.md`
2. **LW-CAR-0055** — what your gym playlist says about you (9 slides, style S2): `carousels/LW-CAR-0055/prompts/codex-task.md`
3. **LW-CAR-0056** — most skipped muscles tier list (17 slides, style S2): `carousels/LW-CAR-0056/prompts/codex-task.md`
4. **LW-CAR-0057** — gym zodiac signs (14 slides, style S2): `carousels/LW-CAR-0057/prompts/codex-task.md`
5. **LW-CAR-0058** — what your favorite day says about you (9 slides, style S2): `carousels/LW-CAR-0058/prompts/codex-task.md`
6. **LW-CAR-0059** — cardio tier list (17 slides, style S2): `carousels/LW-CAR-0059/prompts/codex-task.md`
7. **LW-CAR-0060** — post-workout meals tier list (17 slides, style S2): `carousels/LW-CAR-0060/prompts/codex-task.md`
8. **LW-CAR-0061** — what your gym time says about you (8 slides, style S2): `carousels/LW-CAR-0061/prompts/codex-task.md`

## Rules for the whole batch
- **Do not stop for the owner** between slides or between carousels. The owner has already approved the look; the approved carousels named in each task file (LW-CAR-0022, 0029, 0042) are the visual reference. Generate every slide of every carousel in this batch.
- Every word comes from that carousel's `copy.json`. Never copy words from other carousels or from references. Keep curly quotes and apostrophes where the text has them.
- Harda logo file on every slide. Opaque flattened RGB PNG, 1080 x 1350. White S2 figure, bald and faceless, featureless pelvis, shorts #2A2A2A.
- Props (headphones, clocks, food, cans, bars, shakers, calendars) are plain: **no brand names, logos or readable text** on them, except the clock faces the task files name.
- Zodiac symbols on LW-CAR-0057 are drawn as simple #F26445 line icons, never emoji.
- **Ending slides:** measure where the body text ends and place the phone below it with a gap of at least 40 px. Never a fixed height. Every word of the body text must be visible. The phone shows the real Harda screenshot named in the task file; never generate or redraw app UI.
- **Finish one carousel completely before starting the next:** all slides, `manifest.json` (`agent_visual_review: not_performed`, `user_review: pending`), `caption.txt`, the ZIP. Then **commit and push that carousel in one commit**.
- If a limit or error interrupts you, push what exists immediately, mark that carousel incomplete in its manifest with the next slide to generate, and stop.
- No automatic QA, OCR or regeneration passes. The owner reviews all carousels at the end.
