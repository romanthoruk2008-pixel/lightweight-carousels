# Codex batch I — 7 carousels, generate everything in one run

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`. Run `git pull` first.

**This batch is separate from batch H.** Another agent may be generating batch H (LW-CAR-0062 … 0069) at the same time. Never touch batch H files. Before every push, run `git pull --rebase origin claude/charming-einstein-xgejky`. Your commits only add files inside your own carousel folders, so a rebase never conflicts.

Read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` once. This batch mixes two styles: **S1** (sand anatomy mannequin, Rubik, LW-CAR-0070 … 0073) and **S2** (white figure, LW-CAR-0074 … 0076). Each task file names its style, background and reference slides. Never mix the figures between styles.

Do these carousels **in this order**, each by its own task file:

1. **LW-CAR-0070** — BEST EXERCISES FOR EVERY MUSCLE GROUP (Pull Day Edition) (8 slides, style S1, GRID): `carousels/LW-CAR-0070/prompts/codex-task.md`
2. **LW-CAR-0071** — BEST EXERCISES FOR EVERY MUSCLE GROUP (Leg Day Edition) (8 slides, style S1, DOTS): `carousels/LW-CAR-0071/prompts/codex-task.md`
3. **LW-CAR-0072** — STRUCTURE THE PERFECT PULL DAY (9 slides, style S1, PLATES): `carousels/LW-CAR-0072/prompts/codex-task.md`
4. **LW-CAR-0073** — STRUCTURE THE PERFECT GLUTE DAY (8 slides, style S1, CLEAN): `carousels/LW-CAR-0073/prompts/codex-task.md`
5. **LW-CAR-0074** — types of gym buddies (9 slides, style S2): `carousels/LW-CAR-0074/prompts/codex-task.md`
6. **LW-CAR-0075** — most aesthetic muscles tier list (19 slides, style S2): `carousels/LW-CAR-0075/prompts/codex-task.md`
7. **LW-CAR-0076** — gym fails tier list (17 slides, style S2): `carousels/LW-CAR-0076/prompts/codex-task.md`

LW-CAR-0072 replaces the old, never-generated LW-CAR-0004. Do not generate LW-CAR-0004.

## Rules for the whole batch
- **Do not stop for the owner** between slides or between carousels. The approved carousels named in each task file are the visual reference: LW-CAR-0005 and 0031 for BEST EXERCISES, LW-CAR-0009 for STRUCTURE, LW-CAR-0041 / 0022 / 0049 for S2. Generate every slide of every carousel in this batch.
- Every word comes from that carousel's `copy.json`. Never copy words from other carousels or from references. Keep capitals exactly as written: lowercase in S2, Title Case and UPPERCASE in S1. Keep curly quotes and apostrophes.
- Harda logo file on every slide. Opaque flattened RGB PNG, 1080 x 1350. **No arch** on any S1 slide, even where an older reference still shows one.
- **Ending slides:** measure where the body text ends and place the phone below it with a gap of at least 40 px. Never a fixed height. Every word must be visible. The phone shows the real Harda screenshot named in the task file; never generate or redraw app UI.
- **Finish one carousel completely before starting the next:** all slides, `manifest.json` (`agent_visual_review: not_performed`, `user_review: pending`), `caption.txt`, the ZIP. Then **commit and push that carousel in one commit**.
- **If a push fails:** `git pull --rebase`, then retry up to 4 times (2, 4, 8, 16 s) with `git -c http.postBuffer=524288000 push`. If it still fails, split the commit (outputs + caption + manifest, then the ZIP, then production-assets) and keep generating. A failed push is not a reason to stop.
- If generation itself fails, push what exists, mark that carousel incomplete in its manifest with the next slide to generate, and stop.
- No automatic QA, OCR or regeneration passes. The owner reviews all carousels at the end.
