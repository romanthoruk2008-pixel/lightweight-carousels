# Lightweight carousel production

Read this file, docs/BRAND.md, docs/WORKFLOW.md and docs/DECISIONS.md before starting work.

## Current phase

Repository foundation. No scheduled workflow, provider authentication, Claude integration or image-generation automation has been configured. Do not describe the pipeline as operational until an end-to-end task has passed.

## Remote-only execution

The owner requested that nothing be downloaded or cloned to their computer. Work directly through GitHub or an explicitly selected cloud environment. Do not create a local checkout, install software locally or download assets to the owner's device without a new instruction.

## Responsibilities

- Owner: creative direction, feedback, final approval and publishing.
- Claude / copywriter: topics, hooks, slide copy, captions and topic-relevant Lightweight CTA. Owns draft copy.
- Codex / visual producer: layout, asset selection, image-generation prompts, rendering and visual review. Preserve approved copy verbatim.
- Reviewer role: inspect training claims, copy completeness, anatomy, equipment mechanics, text accuracy, brand consistency and CTA relevance. This may be a separate pass, not necessarily another always-running agent.

These are workflow roles, not authorization to launch agents, contact other services or connect accounts.

## Handoffs

Give every carousel a stable ID such as LW-CAR-0001. Keep its brief, slide copy, image prompts, results and review under its own directory in carousels/. Work on one carousel per branch. Avoid simultaneous edits to the same files.

Content contract: each slide needs an index, purpose, headline, body, visual brief and optional exercise data. Store source references and target audience with the carousel. Frozen copy must be approved before image generation; a copy change requires a new version.

## Boundaries

Do not invent product features, app screenshots, logos, study citations or performance results. Reference files must actually be accessible before claiming visual fidelity. Reuse verified assets where appropriate; label newly generated anatomy as requiring review. Do not auto-publish social posts.

Never commit API keys, tokens, private user information or unlicensed third-party assets. Public reference links are acceptable; don't assume competitor screenshots can be redistributed.

User feedback belongs in docs/DECISIONS.md. Do not overwrite decisions silently.
