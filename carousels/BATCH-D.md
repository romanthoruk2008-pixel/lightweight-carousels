# Codex batch D — fix 7 endings, then 5 new carousels, all in one run

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

Read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` once.

## Step 0 — fix the old endings first
Do `carousels/FIX-ENDINGS.md` exactly (seven ending slides where the phone covers the body text). Commit and push those fixes in one commit before starting the new carousels. If FIX-ENDINGS has already been done (the manifests record it), skip this step.

## Then these carousels, in this order, each by its own task file

1. **LW-CAR-0038** — gym red flags (9 slides, style S2): `carousels/LW-CAR-0038/prompts/codex-task.md`
2. **LW-CAR-0039** — unwritten gym rules (9 slides, style S2): `carousels/LW-CAR-0039/prompts/codex-task.md`
3. **LW-CAR-0040** — why you keep quitting the gym (9 slides, style S2): `carousels/LW-CAR-0040/prompts/codex-task.md`
4. **LW-CAR-0041** — types of people at the gym (9 slides, style S2): `carousels/LW-CAR-0041/prompts/codex-task.md`
5. **LW-CAR-0042** — muscles that make you look bigger in a t-shirt (8 slides, style S2): `carousels/LW-CAR-0042/prompts/codex-task.md`

## Rules for the whole batch
- **Do not stop for the owner** between slides or between carousels. The owner has already approved the look; the approved carousels named in each task file (LW-CAR-0022, LW-CAR-0029) are the visual reference. Generate every slide of every carousel in this batch.
- Every word, number and exercise comes from that carousel's `copy.json`. Never copy words from other carousels or from references.
- Harda logo file on every slide, as each task file says. Opaque flattened RGB PNG, 1080 x 1350. White S2 figure only.
- **Ending slides:** measure where the body text ends and place the phone below it with a gap of at least 40 px. Never place the phone at a fixed height. Every word of the body text must be visible.
- **Finish one carousel completely before starting the next:** all slides, `manifest.json` (`agent_visual_review: not_performed`, `user_review: pending`), `caption.txt`, the ZIP. Then **commit and push that carousel in one commit**, so finished work is safe even if the run stops later.
- If a limit or error interrupts you, push what exists immediately, mark that carousel incomplete in its manifest with the next slide to generate, and stop.
- No automatic QA, OCR or regeneration passes. The owner reviews all carousels at the end.
