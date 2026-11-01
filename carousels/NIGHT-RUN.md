# Night run — batches K, L, M (22 carousels, ~171 slides, all S2)

Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`. Run `git pull` first.

**Goal: generate as many slides as possible tonight, until the image-generation limit runs out.** Work through `carousels/BATCH-K.md`, then `carousels/BATCH-L.md`, then `carousels/BATCH-M.md`, carousel by carousel, in order. **Never stop to ask the owner anything and never pause for review.** The owner is asleep and has approved everything in advance.

Read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` once at the start, then follow each carousel's own task file.

## Style (every carousel)
Style **S2**, exactly like the approved S2 tier lists (LW-CAR-0020 … 0023) and batch J (LW-CAR-0077 … 0084): white / light-grey anatomical mannequin in opaque #2A2A2A shorts, heavy lowercase grotesk, #F26445 marker bars, solid #F0F1EB, Harda logo file at x 48, y 19, 218 x 71. Opaque RGB PNG 1080 x 1350. Never the sand S1 figure, never Rubik uppercase, never an arch. Figures always wear shorts and do an exercise or stand neutrally; never a close physique pose.

## Never stop — rules
1. **Only one thing ends the run:** the image tool itself says the generation limit / quota is used up. Then push everything (see 5) and stop.
2. **A failed slide is not a reason to stop.** Retry it at most twice with a meaningful supported correction (as in CODEX-SERIES-RULES.md). If it still fails, record it in the manifest as `failed_after_retries`, skip it, and **continue with the next slide**.
3. **A failed carousel is not a reason to stop.** Mark it incomplete in its manifest with the missing slides and go to the next carousel.
4. **Unclear detail?** Make the most reasonable choice from the task file and the approved S2 references, note it in the manifest, and keep going. Do not ask.
5. **Commit and push after every finished carousel** (slides, `manifest.json` with `agent_visual_review: not_performed` and `user_review: pending`, `caption.txt`, ZIP). Before every push: `git pull --rebase origin claude/charming-einstein-xgejky`. If a push fails, retry 4 times (2, 4, 8, 16 s) with `git -c http.postBuffer=524288000 push`; if it still fails, keep the commit locally, **keep generating**, and push everything together after the next carousel.
6. **When the limit is reached:** finish saving the current slide, write the manifest (incomplete, with the next slide to generate), commit and push everything. Then stop.
7. No automatic QA, OCR or regeneration of successful slides. The owner reviews everything later.

## Two agents at once (optional)
A second agent may run at the same time. To avoid doing the same carousel twice: before starting a carousel, `git pull`; **skip any carousel that already has a `manifest.json`**; when you start one, immediately commit and push a minimal `manifest.json` with `"status": "in_progress"` to claim it. A second agent should go through the batches in reverse order (M, then L, then K).

## Order
1. `carousels/BATCH-K.md` — LW-CAR-0085 … 0092
2. `carousels/BATCH-L.md` — LW-CAR-0093 … 0099
3. `carousels/BATCH-M.md` — LW-CAR-0100 … 0106
