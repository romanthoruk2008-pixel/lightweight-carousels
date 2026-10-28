# Codex task — LW-CAR-0071 "BEST EXERCISES FOR EVERY MUSCLE GROUP (Leg Day Edition)" (style S1, original Harda carousel)

First read `carousels/CODEX-SERIES-RULES.md` and `docs/DESIGN-STYLES.md` (style **S1**). Exact copy: `carousels/LW-CAR-0071/copy.json` (content_version 1.0). Repository: romanthoruk2008-pixel/lightweight-carousels, branch `claude/charming-einstein-xgejky`.

**What this is.** The leg day edition of our **BEST EXERCISES FOR EVERY MUSCLE GROUP** series. It must look like the twin of LW-CAR-0005 (Push Day Edition): same cover, the same "A OR B" layout, arrows, OR badge and illustration style. Only the text, the highlighted muscles and the exercises change. 8 slides. Every word comes from this file and copy.json.

## Visual references (our own slides)
| Our slide | Copy the look of |
|---|---|
| 1 cover | `carousels/LW-CAR-0005/outputs/slide-01.png` |
| 2–7 "A OR B" | `carousels/LW-CAR-0005/outputs/slide-02.png` … `slide-07.png` (one identical layout) |
| 8 ending | `carousels/LW-CAR-0031/outputs/slide-08.png` (headline + underline bar, two body lines, the same hand, phone and real screenshot) |

**Background: `DOTS`** on every slide: solid #F0F1EB first, then small #D4D4CC dots, 6 px, every 45 px. **No arch**: older reference slides may still show it, so ignore it. Opaque, flattened RGB, 1080 x 1350.
**Logo:** `assets/logo/harda-logo-full.png` at x 48, y 19, 218 x 71, with its own transparency. Top 110 px free of everything else.

## Figures
The S1 mannequin, exactly as on the approved S1 slides: bald, faceless, **smooth plastic anatomy mannequin with a featureless pelvis**, fine grey linework, sand #D9CBBE muscles, ivory skin, target muscles #F26445. Full-body figures wear plain short shorts in sand #D9CBBE. **Never the white S2 figure.** Exercise figures have no highlighted muscles (all sand), as on LW-CAR-0005.

## Slides

### Slide 1 — hook (twin of LW-CAR-0005 slide 1)
- Three stacked uppercase lines, very large, top ~55%: `BEST EXERCISES` in #F26445, `FOR EVERY` and `MUSCLE GROUP` in #2A2A2A. Under them, small bold italic `(Leg Day Edition)` in #2A2A2A.
- Below: the anatomical man on a black / grey plate-loaded 45-degree leg press, three-quarter front view, knees bent; quads filled #F26445.

### Slides 2–7 — "A OR B" template (twin of LW-CAR-0005 slides 2–7, identical layout)
- Top center: `#N` in #F26445 with an #F26445 underline under the number, then the title, bold, #2A2A2A, on the same line.
- Under it: an anatomical close-up of the body region with only the target muscle filled #F26445 (rest sand / ivory).
- Two thin curved #F26445 arrows lead down from the close-up, one to each exercise figure.
- Bottom: two full-body figures doing the exercises, left and right. A #F26445 circle badge with white `OR` sits between them. Labels under each, regular #2A2A2A.

| Slide | Number | Title | Close-up / highlighted | Left — label | Right — label |
|---|---|---|---|---|---|
| 2 | `#1` | `Quads` | front of the thigh, the quads | plate-loaded hack squat machine, side view, deep knee bend — `Hack Squat` | seated leg extension machine, legs straight at the top, side view — `Leg Extension` |
| 3 | `#2` | `Hamstrings` | back of the thigh, the hamstrings | seated leg curl machine, side view — `Seated Leg Curl` | barbell hip hinge with a flat back, bar at mid-shin, side view — `Romanian Deadlift` |
| 4 | `#3` | `Glutes` | rear hips, the glute max | upper back on a bench, barbell across the hips, hips at the top, side view — `Hip Thrust` | rear foot up on a bench, front knee bent deep, dumbbells in hands, side view — `Bulgarian Split Squat` |
| 5 | `#4` | `Adductors` | inner thigh, front view | seated hip adductor machine, legs squeezing in, front view — `Adductor Machine` | wide-stance squat holding one dumbbell between the legs, toes out, front view — `Sumo Squat` |
| 6 | `#5` | `Outer Glutes` | upper outer hip, the glute medius, side view | seated hip abductor machine, legs pushing out, front view — `Abductor Machine` | side-stepping with a small band around the knees, half-squat, front view — `Banded Side Walk` |
| 7 | `#6` | `Calves` | lower leg from behind, the calves | standing calf raise machine, up on the toes, side view — `Standing Calf Raise` | seated in a 45-degree leg press, pushing the platform with the toes only, side view — `Leg Press Calf Raise` |

### Slide 8 — product ending (twin of LW-CAR-0031 slide 8)
- Headline: `Are Your Legs Getting Enough Work?` (bold, #2A2A2A, two lines if needed) + short #F26445 underline bar.
- Body, two paragraphs, regular #6B6B6B: `Log your workouts in Harda.` / `See how many sets your legs get compared to every other muscle.`
- Phone: the **real Harda Muscle balance screenshot**, the same as on the approved LW-CAR-0031 slide 8 (radar with a Legs axis), true proportions, never squashed. Never generate, redraw or imitate UI.

- **The phone must never touch or cover the body text.** Measure where the body text ends and place the hand and phone below it with a clear gap of at least 40 px; it may run off the bottom edge. Never place the phone at a fixed height.

## Caption
Write `caption.txt` from `copy.json` → `caption.text`, verbatim.

## Order of work
Generate **all slides in one go**, without stopping for the owner between slides; the approved slides above are the visual reference. Then write the manifest (`agent_visual_review: not_performed`, `user_review: pending`), the caption and the ZIP, and commit and push the whole carousel in one commit. If a limit or error interrupts you, push what exists immediately, marked incomplete, with the next slide to generate.
