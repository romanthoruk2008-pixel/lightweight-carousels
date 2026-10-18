# Lightweight carousel production

Read docs/BRAND.md, docs/DECISIONS.md, docs/WORKFLOW.md, docs/handoff.md and data/carousel-progress.json before work. Task templates live in docs/AGENT-PROMPTS.md. Claude also reads CLAUDE.md.

## Current state — binding owner clarification

THE VISUAL STYLE IS NOT APPROVED. Only the base palette has been recorded. The six-slide Best Arm Day sample is an experiment, not an approved master. Do not infer approval from positive preliminary feedback. approved_style_version remains null.

We are designing the workflow and agent instructions. No agents, Claude integration, scheduled workflow or cloud image-generation pipeline have been launched or configured. No production assets are stored here yet.

## Remote-only execution

The owner requested that nothing be downloaded or cloned to their computer. Work directly through GitHub or an explicitly selected cloud environment. No local checkout, installation or asset download to the owner's device.

## Roles

- Owner: creative direction, explicit style/result acceptance and publishing.
- Coordinator: assigns stable carousel IDs and batches; integrates results and updates the global summary.
- Claude / copywriter: owns brief.md and versioned copy.json, including a topic-relevant Lightweight ending.
- Codex / visual producer: owns prompts and outputs for a whole assigned carousel; preserves approved copy verbatim.
- Reviewer: one defined pass over content, anatomy, equipment mechanics, text accuracy, consistency and CTA relevance.

These are proposed workflow roles, not authorization to start agents, connect accounts or trigger mass production.

## Handoffs and consistency

One directory and working branch per carousel. One visual producer per carousel. Each slide needs an ID, purpose, exact text and visual brief. Freeze a specific copy version/commit before visual production. A copy change creates a new version.

The assigned worker owns its carousel manifest; the coordinator owns data/carousel-progress.json. This ownership is procedural, not an installed lock service. Merge the copy handoff before visual work branches from it. Distinguish branch-only results from main.

## Progress and recovery

Keep actual attempts, prompts, references, style/content versions, output paths, hashes and errors. Update after every slide; checkpoint after a complete carousel. Preparation is not a generation attempt. Before resuming, reconcile manifests with actual outputs; do not blindly repeat in_progress calls.

Separate technical_check, content_review, agent_visual_review, user_review and remote_backup. Do not invent a check or mark user approval yourself. A temporary cloud file is not durable backup. Mark remote verification only after checking the real saved file.

## Generation boundaries

Use the built-in image generator only where actually available. No agreed paid API fallback exists. On quota or unavailable tools, stop the package and write a handoff instead of repeatedly calling or switching providers.

Review and retry limits must be explicit in the task package. Otherwise report required corrections without automatic regeneration. Never replace accepted outputs silently.

Do not invent features, app screens, logos, citations, unavailable reference fidelity or social performance. Seriozha is not an AI coach. Keep secrets and private data out of this public repository. Do not auto-publish social posts.

The final slide must connect the carousel topic to a real Lightweight capability; merely adding the brand name to a generic save prompt is insufficient. No specific final-slide design or copy is approved yet.

Record owner feedback in docs/DECISIONS.md without erasing earlier history.
