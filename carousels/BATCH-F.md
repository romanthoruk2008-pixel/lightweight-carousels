# Codex batch F — 6 carousels, generate everything in one run

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

Read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` once. Then do these carousels **in this order**, each by its own task file:

1. **LW-CAR-0048** — the 5 stages of leg day (7 slides, style S2): `carousels/LW-CAR-0048/prompts/codex-task.md`
2. **LW-CAR-0049** — gym excuses tier list (17 slides, style S2): `carousels/LW-CAR-0049/prompts/codex-task.md`
3. **LW-CAR-0050** — gym pet peeves (9 slides, style S2): `carousels/LW-CAR-0050/prompts/codex-task.md`
4. **LW-CAR-0051** — what your gym outfit says about you (9 slides, style S2): `carousels/LW-CAR-0051/prompts/codex-task.md`
5. **LW-CAR-0052** — muscles people notice first (7 slides, style S2): `carousels/LW-CAR-0052/prompts/codex-task.md`
6. **LW-CAR-0053** — types of gyms tier list (17 slides, style S2): `carousels/LW-CAR-0053/prompts/codex-task.md`

## Rules for the whole batch
- **Do not stop for the owner** between slides or between carousels. The owner has already approved the look; the approved carousels named in each task file (LW-CAR-0022, 0029, 0042) are the visual reference. Generate every slide of every carousel in this batch.
- Every word comes from that carousel's `copy.json`. Never copy words from other carousels or from references. Keep curly quotes where the text has them.
- Harda logo file on every slide. Opaque flattened RGB PNG, 1080 x 1350. White S2 figure; clothes only on LW-CAR-0051, as its task file says.
- **Ending slides:** measure where the body text ends and place the phone below it with a gap of at least 40 px. Never a fixed height. Every word of the body text must be visible.
- **Finish one carousel completely before starting the next:** all slides, `manifest.json` (`agent_visual_review: not_performed`, `user_review: pending`), `caption.txt`, the ZIP. Then **commit and push that carousel in one commit**.
- If a limit or error interrupts you, push what exists immediately, mark that carousel incomplete in its manifest with the next slide to generate, and stop.
- No automatic QA, OCR or regeneration passes. The owner reviews all carousels at the end.
