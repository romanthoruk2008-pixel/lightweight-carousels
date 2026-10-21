# Harda ending rebrand — 11 requested edits complete

Task: carousels/HARDA-REBRAND-ENDINGS.md. All 11 listed existing slides were used as image_gen inputs, once each. Only Lightweight → Harda (lightweight → harda for 0020/0021) was requested. Exact frozen copy versions and actual prompts, source commit, calls and returned paths are recorded in manifest.json and each carousel manifest.

The brand-word rectangles were selected on the original input images before generation. Each exported slide starts from its original bitmap: only the generated brand-word rectangle is copied back. Every other text element and its position, marker bars, background outside the rectangle, hand, phone and real UI remain the original input pixels. Original Harda PNG composited again at x48 y19, 218×71, own transparency. No screenshot rescaling or UI generation. Output is flattened 1080×1350 RGB PNG.

Each affected carousel ZIP is rebuilt with the replacement slide, current manifest, copy and new edit prompt. Other numbered slides remain unchanged. Only these 11 edited slides have user_review=pending; prior acceptance of all other slides is retained.

No errors or additional attempts. agent_visual_review=not_performed. No automatic visual QA, OCR, anatomy audit or reviewer passes. Owner reviews edits.

All changes belong to one commit. No slides from LW-CAR-0005 or LW-CAR-0006 were edited.
