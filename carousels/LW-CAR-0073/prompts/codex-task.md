# Codex task — LW-CAR-0073 "STRUCTURE THE PERFECT GLUTE DAY" (style S1, original Harda carousel)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S1**). Exact copy: `carousels/LW-CAR-0073/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The glute day part of our STRUCTURE series with the approved **LW-CAR-0002** (push day) and **LW-CAR-0009** (leg day). It must look like their twin: same layouts, positions, sizes, "#N" numbers, underline bars, thin vertical divider between exercises and illustration style. Only the text, the highlighted muscles and the exercises change. 8 slides.

## Visual references (our own approved slides)
| Our slide | Copy the look of |
|---|---|
| 1 cover | `carousels/LW-CAR-0009/outputs/slide-01.png` |
| 2 checklist | `carousels/LW-CAR-0009/outputs/slide-02.png` |
| 3–7 list | `carousels/LW-CAR-0009/outputs/slide-03.png` … `slide-07.png` |
| 8 ending | `carousels/LW-CAR-0009/outputs/slide-08.png` (same hand, phone and real screenshot) |

**Background: `CLEAN`** on every slide: plain solid #F0F1EB. **No arch**: the older reference slides may still show it, so ignore it. Opaque, flattened RGB, 1080 x 1350.
**Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.

## Figures
The S1 mannequin, exactly as on the approved S1 slides: bald, faceless, **smooth plastic anatomy mannequin with a featureless pelvis**, fine grey linework, sand #D9CBBE muscles, ivory skin, target muscles #F26445. Full-body figures wear plain short shorts in sand #D9CBBE. **Never the white S2 figure.** Exercise figures have no highlighted muscles (all sand), exactly as on LW-CAR-0009.

## Slides

### Slide 1 — hook (twin of LW-CAR-0009 slide 1)
- Three stacked uppercase lines, heaviest Rubik, same size and position as the template:
  - `STRUCTURE` in #2A2A2A
  - `THE PERFECT` in #2A2A2A
  - `GLUTE DAY` in #F26445
- Below: the anatomical man on a black / grey plate-loaded hip thrust machine, side three-quarter view, hips at the top; glutes filled #F26445 (smooth featureless mannequin, no shorts on this cover). Figure in the lower half, cropped at the bottom like the template.

### Slide 2 — checklist (twin of LW-CAR-0009 slide 2)
- Top-left, two-line bold title `Your Glute Day` / `Should Include:` + short #F26445 underline bar.
- Left-aligned bullets ("1x" regular, muscle word bold, bracket regular):
  - `1x Glute Max (Hip Thrust)`
  - `1x Glutes (Lunge)`
  - `1x Hamstrings (Hinge)`
  - `1x Glute Medius (Abduction)`
  - `1x Glutes (Finisher)`
- Bottom right, cropped at the right and bottom edges: the **lower body** of the anatomical man (waist to feet) in a three-quarter rear view, one leg slightly forward, no shorts (smooth featureless mannequin); glutes, glute medius and hamstrings filled #F26445.

### Slides 3–7 — list template (twin of LW-CAR-0009 slides 3–7)
- Top-left: big bold `#N` in #F26445 with a short #F26445 underline bar under it. To its right, the title (bold, #2A2A2A), and under the title the sets line (regular, #6B6B6B).
- Under the header, left-aligned: one sentence in regular #6B6B6B, up to two lines.
- Bottom ~55%: two full-body figures doing the exercises side by side, separated by a thin vertical #F26445 line. Labels under each, regular #2A2A2A.

| Slide | Number | Title | Sets line | Sentence (exact) | Left — label | Right — label |
|---|---|---|---|---|---|---|
| 3 | `#1` | `Glute Max` | `2-3 sets x 6-10 reps` | `Choose one of these exercises to build your glutes:` | upper back on a bench, barbell across the hips, hips at the top, side view — `Barbell Hip Thrust` | seated in a plate-loaded hip thrust machine, hips at the top, side view — `Hip Thrust Machine` |
| 4 | `#2` | `Glutes` | `2-3 sets x 8-12 reps` | `Choose one of these exercises to train your glutes in a deep stretch:` | rear foot up on a bench, front knee bent deep, torso leaning forward, dumbbells in hands, side view — `Bulgarian Split Squat` | mid-stride walking lunge with dumbbells, torso leaning slightly forward, side view — `Walking Lunges` |
| 5 | `#3` | `Hamstrings` | `2-3 sets x 8-12 reps` | `Choose one of these exercises to hinge with your hips:` | barbell hip hinge with a flat back, bar at mid-shin, side view — `Romanian Deadlift` | 45-degree back extension bench, upper back slightly rounded, hips doing the work, side view — `45° Back Extension` |
| 6 | `#4` | `Glute Medius` | `2-3 sets x 12-20 reps` | `Choose one of these exercises to train the side of your hips:` | seated hip abductor machine, legs pushing out, torso leaning slightly forward, front view — `Abductor Machine` | standing side-on to a low cable, ankle strap, lifting the leg out to the side, front view — `Cable Hip Abduction` |
| 7 | `#5` | `Glutes` | `2-3 sets x 15-20 reps` | `Finish with one of these for a burn:` | standing facing a low cable, ankle strap, kicking one leg straight back, side view — `Cable Kickback` | lying on the floor, knees bent, hips lifted, side view — `Glute Bridge` |

### Slide 8 — product ending (twin of LW-CAR-0009 slide 8)
Copy the approved slide's composition: Harda logo, short #F26445 bar, two-line left-aligned headline in heaviest Rubik, the hand holding the tall phone. No arch.
- `Track Your Glute Day.` in #2A2A2A
- `See If Your Legs Keep Up.` in #F26445
- Phone: the same **real Harda Muscle balance screenshot** as on the approved LW-CAR-0009 slide 8 (radar with a Legs axis; there is no separate Glutes axis, so the text speaks about legs), true proportions, never squashed, may run off the bottom edge. Never generate, redraw or imitate UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides; the approved slides above are the visual reference. Then write the manifest (`agent_visual_review: not_performed`, `user_review: pending`), the caption and the ZIP, and commit and push the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
