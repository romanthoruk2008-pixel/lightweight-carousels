# Codex batch H — 8 carousels, generate everything in one run

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`. Run `git pull` first.

**Start only after batch G is finished** (LW-CAR-0056 … 0061 pushed; see `carousels/BATCH-G-RESUME.md`). If batch G is not finished, finish it first.

Read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` once. This batch mixes two styles: **S2** (white figure, LW-CAR-0062 and 0069) and **S1** (sand anatomy mannequin, Rubik, LW-CAR-0063 … 0068). Each task file names its style, background and approved reference slides. Never mix the figures between styles.

Do these carousels **in this order**, each by its own task file:

1. **LW-CAR-0062** — gym things that feel illegal (9 slides, style S2): `carousels/LW-CAR-0062/prompts/codex-task.md`
2. **LW-CAR-0063** — WEAK LEGS? (8 slides, style S1, GRID): `carousels/LW-CAR-0063/prompts/codex-task.md`
3. **LW-CAR-0064** — WEAK SHOULDERS? (8 slides, style S1, DOTS): `carousels/LW-CAR-0064/prompts/codex-task.md`
4. **LW-CAR-0065** — WEAK GLUTES? (8 slides, style S1, PLATES): `carousels/LW-CAR-0065/prompts/codex-task.md`
5. **LW-CAR-0066** — STRUCTURE THE PERFECT UPPER DAY (8 slides, style S1, CLEAN): `carousels/LW-CAR-0066/prompts/codex-task.md`
6. **LW-CAR-0067** — STRUCTURE THE PERFECT ARM DAY (8 slides, style S1, GRID): `carousels/LW-CAR-0067/prompts/codex-task.md`
7. **LW-CAR-0068** — STRUCTURE THE PERFECT FULL BODY DAY (8 slides, style S1, DOTS): `carousels/LW-CAR-0068/prompts/codex-task.md`
8. **LW-CAR-0069** — gym tips that feel illegal to know (9 slides, style S2): `carousels/LW-CAR-0069/prompts/codex-task.md`

## Rules for the whole batch
- **Do not stop for the owner** between slides or between carousels. The approved carousels named in each task file are the visual reference: LW-CAR-0044 / 0052 / 0022 for S2, LW-CAR-0031 for WEAK ___?, LW-CAR-0009 for STRUCTURE. Generate every slide of every carousel in this batch.
- Every word comes from that carousel's `copy.json`. Never copy words from other carousels or from references. Keep capitals exactly as written: lowercase in S2, Title Case and UPPERCASE in S1.
- Harda logo file on every slide. Opaque flattened RGB PNG, 1080 x 1350. **No arch** on any S1 slide, even where an older reference still shows one.
- **Ending slides:** measure where the body text ends and place the phone below it with a gap of at least 40 px. Never a fixed height. Every word must be visible. The phone shows the real Harda screenshot named in the task file; never generate or redraw app UI.
- **Finish one carousel completely before starting the next:** all slides, `manifest.json` (`agent_visual_review: not_performed`, `user_review: pending`), `caption.txt`, the ZIP. Then **commit and push that carousel in one commit**.
- **If a push fails:** retry up to 4 times (2, 4, 8, 16 s) with `git -c http.postBuffer=524288000 push`. If it still fails, split the commit (outputs + caption + manifest, then the ZIP, then production-assets) and keep generating. A failed push is not a reason to stop.
- If generation itself fails, push what exists, mark that carousel incomplete in its manifest with the next slide to generate, and stop.
- No automatic QA, OCR or regeneration passes. The owner reviews all carousels at the end.
