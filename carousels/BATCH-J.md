# Codex batch J — 8 carousels, all in S2, generate everything in one run

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`. Run `git pull` first.

Read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` once. **Every carousel in this batch is style S2**: the white / light-grey anatomical mannequin in opaque #2A2A2A shorts, heavy lowercase grotesk, #F26445 marker bars, solid #F0F1EB, exactly like the approved S2 tier lists (LW-CAR-0020 … 0023). Some carousels reuse the **slide structure** of our older S1 series (STRUCTURE, BEST EXERCISES); draw that structure in the S2 look. Never the sand S1 figure, never Rubik uppercase, never an arch.

Do these carousels **in this order**, each by its own task file:

1. **LW-CAR-0077** — structure the perfect chest day (8 slides): `carousels/LW-CAR-0077/prompts/codex-task.md`
2. **LW-CAR-0078** — structure the perfect back day (8 slides): `carousels/LW-CAR-0078/prompts/codex-task.md`
3. **LW-CAR-0079** — structure the perfect arm day (8 slides): `carousels/LW-CAR-0079/prompts/codex-task.md`
4. **LW-CAR-0080** — how to build a v-taper (7 slides): `carousels/LW-CAR-0080/prompts/codex-task.md`
5. **LW-CAR-0081** — best exercises for every muscle group (dumbbells only) (9 slides): `carousels/LW-CAR-0081/prompts/codex-task.md`
6. **LW-CAR-0082** — best exercises for every muscle group (arm day edition) (8 slides): `carousels/LW-CAR-0082/prompts/codex-task.md`
7. **LW-CAR-0083** — machine taken? do this instead (9 slides): `carousels/LW-CAR-0083/prompts/codex-task.md`
8. **LW-CAR-0084** — how to get wider (7 slides): `carousels/LW-CAR-0084/prompts/codex-task.md`

## Rules for the whole batch
- **Do not stop for the owner** between slides or between carousels. Visual reference: LW-CAR-0022 (cover, ending), LW-CAR-0029 and 0052 (headline + body + label line). Generate every slide of every carousel in this batch.
- Every word comes from that carousel's `copy.json`. Never copy words from other carousels or from references. Keep lowercase, curly apostrophes, hyphens, colons and question marks exactly.
- Harda logo file on every slide. Opaque flattened RGB PNG, 1080 x 1350.
- Figures always wear the opaque #2A2A2A shorts and are shown doing an exercise or standing in a neutral pose, never in a close physique pose.
- **Ending slides:** measure where the body text ends and place the phone below it with a gap of at least 40 px. Never a fixed height. Every word must be visible. The phone shows the real Harda screenshot named in the task file; never generate or redraw app UI.
- **Failed generations:** follow the owner retry rule in `carousels/CODEX-SERIES-RULES.md` (up to two more attempts per failed slide with a meaningful supported correction; then record the slide as failed and continue). This overrides any older "stop the batch" wording in the task files.
- **Finish one carousel completely before starting the next:** all slides, `manifest.json` (`agent_visual_review: not_performed`, `user_review: pending`), `caption.txt`, the ZIP. Then **commit and push that carousel in one commit**. Before every push run `git pull --rebase origin claude/charming-einstein-xgejky`.
- **If a push fails:** retry up to 4 times (2, 4, 8, 16 s) with `git -c http.postBuffer=524288000 push`; if it still fails, split the commit (outputs + caption + manifest, then the ZIP, then production-assets) and keep generating.
- No automatic QA, OCR or regeneration of successful slides. The owner reviews all carousels at the end.
