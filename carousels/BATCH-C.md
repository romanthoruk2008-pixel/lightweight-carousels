# Codex batch C — 5 carousels, generate everything in one run

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

Read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` once. Then do these carousels **in this order**, each by its own task file:

1. **LW-CAR-0033** — signs you’re actually making progress (9 slides, style S2): `carousels/LW-CAR-0033/prompts/codex-task.md`
2. **LW-CAR-0034** — you’re not a beginner anymore if… (9 slides, style S2): `carousels/LW-CAR-0034/prompts/codex-task.md`
3. **LW-CAR-0035** — home workout tier list (19 slides, style S2): `carousels/LW-CAR-0035/prompts/codex-task.md`
4. **LW-CAR-0036** — secretly killing your gains (9 slides, style S2): `carousels/LW-CAR-0036/prompts/codex-task.md`
5. **LW-CAR-0037** — beginner vs advanced: how they train (8 slides, style S2): `carousels/LW-CAR-0037/prompts/codex-task.md`

## Rules for the whole batch
- **Do not stop for the owner** between slides or between carousels. The owner has already approved the look; the approved carousels named in each task file (LW-CAR-0022, 0025, 0029) are the visual reference. Generate every slide of every carousel in this batch.
- Every word, number and exercise comes from that carousel's `copy.json`. Never copy words from other carousels or from references.
- Harda logo file on every slide, as each task file says. Opaque flattened RGB PNG, 1080 x 1350. White S2 figure only.
- **Ending slides:** the phone must never touch or cover the body text (this went wrong on LW-CAR-0029 and 0031). Keep a clear gap above the phone.
- **Finish one carousel completely before starting the next:** all slides, `manifest.json` (`agent_visual_review: not_performed`, `user_review: pending`), `caption.txt`, the ZIP. Then **commit and push that carousel in one commit**, so finished work is safe even if the run stops later.
- If a limit or error interrupts you, push what exists immediately, mark that carousel incomplete in its manifest with the next slide to generate, and stop.
- No automatic QA, OCR or regeneration passes. The owner reviews all carousels at the end.
