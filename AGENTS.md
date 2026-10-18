# Lightweight carousel production

Read docs/BRAND.md, docs/DECISIONS.md, docs/WORKFLOW.md, docs/handoff.md and data/carousel-progress.json. Task templates: docs/AGENT-PROMPTS.md. Claude also reads CLAUDE.md.

## Binding current decisions

The owner confirmed the direction: reproduce the assigned reference carousel as closely as possible, including topic, exact copy/voice, illustrations, composition and slide order. Change only Lightweight accent colors and its actual font, plus the previously required Lightweight-specific product ending. Read docs/BRAND.md and docs/CONTENT-BRIEF.md for the latest directive. An output master is not yet approved; approved_style_version=null. The earlier Best Arm Day experiment is not a master.

The owner removed the reviewer role and automatic post-generation review. Do NOT run visual QA, OCR, anatomy audits, additional reviewer agents or paid evaluation calls after generation. Set agent_visual_review=not_performed. The owner reviews results. Prepare factually sound copy and exercise prompts before generation; do not add a separate downstream review stage.

We are designing the workflow. Claude, cloud image generation, remote output transfer and scheduled runs are not configured. Do not claim otherwise.

## Remote-only

Nothing may be downloaded, cloned or installed on the owner's computer. Use GitHub or an explicitly selected cloud environment. No local checkout or media downloads.

## Shared references

references/CAROUSELS.md is the shared reference board. One REF-XXX section = one carousel; top-to-bottom image links = slide order. Read only assigned sections. Record source commit, REF-ID, ordered image URLs and a concise extracted brief.

A file containing image URLs does not itself grant pixel access to a model. Confirm needed references open in the actual execution environment before claiming fidelity. Report a precise blocker when they do not. Do not repeatedly ask the owner to reattach an already accessible reference.

## Three working roles

- Coordinator: stable carousel IDs, small packages, ownership, handoffs and global progress.
- Claude / copywriter: brief.md, versioned copy.json, useful content and a topic-relevant Lightweight ending.
- Codex/ChatGPT / visual producer: one complete carousel from frozen copy and selected references; prompts, actual outputs and save status.
- Owner: style choice, feedback and acceptance.

Do not launch agents, connect accounts or start bulk generation based only on these role descriptions.

## Handoffs and progress

One directory and working branch per carousel. One visual producer owns the whole series. Only the assigned worker edits its manifest; coordinator edits the global summary. These are procedural conventions, not an installed lock service.

Freeze exact text at a known content version/commit. Do not silently rewrite Claude's copy. Record actual calls, reference/style/content versions, outputs and errors after each slide; checkpoint after a carousel or interruption.

Before resuming, reconcile the log with actual outputs; do not blindly repeat in_progress calls. Separate generated, remotely saved and owner-approved. Skip existing/accepted outputs unless explicitly asked to correct them.

No default audit scripts or checksum passes are required. Record the output actually returned and whether its remote save succeeded. Keep not_run/not_performed for checks that did not happen. A successful save is not a visual review or owner approval. Temporary cloud paths are not durable storage.

## Generation boundaries

Use built-in image_gen only where actually available. No paid API fallback has been agreed. On quota/unavailable tools, stop the package and save the exact next step. No automatic correction passes.

Do not invent product features, app screens, logos, citations, unavailable reference fidelity or social performance. Seriozha is not an AI coach. Keep secrets/private data out of this public repository. Do not auto-publish social posts.

The final slide connects its topic to a real Lightweight capability. Generic save copy with a brand wordmark is insufficient; no exact final-slide copy/layout is approved.

Record owner feedback in docs/DECISIONS.md and preserve earlier decisions as history.

## Authentic product screens

references/APP-SCREENS.md is the shared board for original Lightweight UI screenshots. APP-XXX identifies one screen/state. Empty placeholders are not assets or proof of a feature. Record exact APP-ID, source commit and actual image URL in the brief.

Select an app screen that supports the carousel's actual message and product feature. Never invent UI or claim a generative recreation preserves the original exactly. For exact UI, the proposed workflow separates scene generation from insertion of the original screenshot with perspective/masking; this compositing stage is not configured yet. Report a capability blocker if exact insertion is unavailable. Phone/hand mockups are optional, and no final-slide style is approved.

## Reference fidelity is the priority

Claude must preserve the chosen reference's topic, hook, wording, text density and voice rather than invent a new gym-bro script. The visual producer preserves its composition, asset choices, anatomy/poses, hierarchy and sequencing. Do not introduce unsolicited creative variations. Record exact reference IDs/commit and the limited brand substitutions. The owner states the reference owner permitted this use. The Lightweight font is Rubik (owner, 2026-10-18). Fitness claims, exercise-to-muscle mappings and debatable statements in the assigned reference are kept verbatim by owner decision: they are deliberate engagement triggers. Do not "correct" them and do not add new claims of your own. Current task is documentation only, no generation.
