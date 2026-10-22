# Codex batch A — 3 carousels, generate everything in one run

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

Read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` once. Then do these carousels **in this order**, each by its own task file:

1. **LW-CAR-0027** — glutes tier list (own ranking) (19 slides, style S2): `carousels/LW-CAR-0027/prompts/codex-task.md`
2. **LW-CAR-0028** — stop doing this. do this instead (8 slides, style S2): `carousels/LW-CAR-0028/prompts/codex-task.md`
3. **LW-CAR-0029** — why you’re not growing (9 slides, style S2): `carousels/LW-CAR-0029/prompts/codex-task.md`

## Rules for the whole batch
- **Do not stop for the owner** between slides or between carousels. The owner has already approved the look; the approved carousels named in each task file are the visual reference. Generate every slide of every carousel in this batch.
- Every word, number and exercise comes from that carousel's `copy.json`. Never copy words from other carousels or from references.
- Harda logo file on every slide, as each task file says. Opaque flattened RGB PNG, 1080 x 1350.
- **Finish one carousel completely before starting the next:** all slides, `manifest.json` (`agent_visual_review: not_performed`, `user_review: pending`), `caption.txt`, the ZIP. Then **commit and push that carousel in one commit**, so finished work is safe even if the run stops later.
- If a limit or error interrupts you, push what exists immediately, mark that carousel incomplete in its manifest with the next slide to generate, and stop.
- No automatic QA, OCR or regeneration passes. The owner reviews all carousels at the end.
