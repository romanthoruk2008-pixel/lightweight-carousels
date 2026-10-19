# Lightweight: candidate keyword long-list (US English)


Collected 2026-10-19. Read-only research. **No search volume, popularity or difficulty numbers are reported anywhere in this file.** All evidence is observed: App Store autocomplete position, how many competitor names/subtitles/descriptions use a phrase, Google autocomplete, and phrases from reviews. Full per-term data is in `longlist.csv`. Sources and method are in `sources.md`.

- Terms: 410 total. 366 candidate terms plus 44 brand terms (do not use).
- Relevance among candidates: H=188, L=50, M=117, X=11 (H high, M medium, L low, X irrelevant / feature not available).
- Evidence tier among candidates: A=111, B=154, C=87, D=14.

**Evidence tiers.** These tiers measure how strong the evidence is. They do not measure search volume.
- **A:** the exact term was suggested by App Store autocomplete in the top 3 positions for a strictly shorter prefix. It beat other completions.
- **B:** one of the following:
  - the term was suggested at any position, including as an echo of its own prefix (Apple returned nothing for unknown strings such as `lifting buddy`, so an echo still means Apple knows the term);
  - it appears inside 3 or more App Store suggestions;
  - it is used in 2 or more competitor names/subtitles.
- **C:** only weaker signals: Google autocomplete, reviews, competitor descriptions, or fewer than 3 App Store suggestions.
- **D:** inferred only.
- **Note:** single words such as 'lifting' were never typed as a longer word's prefix, so they cannot reach tier A by construction.

Most App Store suggestions that contain a phrase are **app titles** (e.g. 'gymroast: lifting tracker'), not user queries. A count of suggestions containing a phrase therefore shows how crowded the phrase is in app names, not how many people search for it.

## Key findings (observed only)

1. **Core logging vocabulary.** These are the strongest App Store autocomplete signals, and the core-term ranking is almost a straight match for Lightweight's launch features:
   - `workout` → "workout tracker" #2 (after "workout app free"). Then "workout planner" #3 and "workout calendar" #10.
   - `gym` → "gym tracker" #8, behind brand and studio names. `gym t` → "gym tracker" #1.
   - `workout l` → "workout log free" #1, "workout log" #2.
   - `lifting` → "lifting tracker" #1.
   - `weight lifting` → "weight lifting tracker" #1.
   - `strength` → "strength log" #1.
   - `strength training l` → "strength training log" #1.
   - The matrix in `../keyword-matrix.md` shows Strong and Hevy hold #1–3 on nearly all of these.
2. **Notebook, journal and notes wording is everywhere.** Apple suggests "workout journal", "workout log book", "workout notebook", "workout notes", "gym notes", "gym notebook", "gym diary", "gym journal" and "lifting journal". Reviews say "I was using notes app before", "pen and paper", "google sheets" and "spreadsheet". This vocabulary is the natural keyword bridge to the photo-of-notebook / text / screenshot import feature.
3. **Import has no App Store demand signal.** Nothing fitness-related came back for these prefixes: `import workout`, `workout from screenshot`, `scan workout`, `workout ai import`. `workout import` returns one app ("fitoor: ai workout import"). Google shows switching intent only with competitor brands: "import workouts from strong to hevy", "strong app alternative", "apps like hevy", "hevy vs strong". Keep import for screenshots and description copy. Do not put it in keywords.
4. **Social is a real query space that the major trackers leave alone.**
   - `workout w` → "workout with friends" #2.
   - `gym b` → "gym buddy" #1, and "gym bros" appears in the same list.
   - `workout tracker w` → "workout tracker with friends" #2.
   - "workout buddy", "gym accountability", "workout streak" and "gym streak" all exist as suggestions.
   - 9 small apps are named "X: workout with friends".
   - Google adds "gym tracker with friends", "workout accountability app with friends" and "app to track gym progress with friends".
   - The matrix shows no major tracker targeting these terms.
5. **Apple Watch.**
   - "workout tracker apple watch" is an exact suggestion (#1 for `workout tracker apple`), and "apple watch workout app" is another.
   - Google adds "apple watch strength training app", "apple watch lifting app", "best apple watch gym app" and "gym log apple watch".
   - 'Apple Watch' is an Apple trademark. It is listed under brand terms. 'watch' on its own is fine as a token.
6. **Progress.**
   - Apple suggests "progressive overload tracker", "gym progress tracker", "workout progress tracker", "gym pr tracker", "body measurements tracker" and "progress photos".
   - Google has 32 suggestions containing "progressive overload", e.g. "best app to track workouts and progressive overload".
   - Per the matrix, measurements and photos are owned by small single-purpose apps.
7. **Beginners.** `beginner workout` → "beginner workout plans for gym" #1. Google: "gym app for beginners", "strength training app for beginners". Home-workout content apps dominate this space, and Lightweight only has *basic* ready-made programs, so the fit is medium to high.
8. **The brand is contested.**
   - `lightweight` → "lightweight! workout analysis" and "lightweight: workout tracker". Two existing lifting apps hold brand autocomplete (IDs 1580231861 and 6762335584).
   - "LW: Gym Workout Tracker & Log" (seller 'Lightweight Fitness Ltd', 6786713713) also exists.
   - `lightweight gym`, `lightweight baby` and `light weight baby` return nothing.
   - This needs an owner decision. It is not a keyword task.
9. **Surprising gaps and noise.**
   - **No App Store suggestions at all:** "drop set", "warm up sets", "workout history", "exercise swap", "muscle balance", "lifting buddy", "gym app with friends", "gym roast" and "gym spreadsheet".
   - **Prefixes taken by other categories:**
     - "ppl" → PPL Electric (utility).
     - "routine planner" / "routine builder" → habit apps.
     - "rep" / "set" / "sets" → unrelated apps.
     - "muscle tracker" → GLP-1 apps.
     - "superset" → software companies.
   - **'free' and 'for women' variants are very frequent.** For example, "gym workout tracker free" was an exact suggestion under 5 prefixes. 'free' is pricing language. Check Apple's metadata rules before use, given the freemium model.
   - **Gamified mascot angles exist as queries:** "workout pet", "fitness pet", "workout duolingo" (brand) and "gym ranked". This is weak but relevant to the optional dinosaur mascot.

## Top 60 recommended for numeric validation (AppTweak)

These were chosen by hand. Each is relevance H, has no brand flag, and has the strongest observed evidence within its intent. All 9 intents are covered. Brand-sensitive Apple terms are kept to 'watch' phrasing.

| # | Term | Intent | Tier | Evidence |
|---|---|---|---|---|
| 1 | workout tracker | 1 | A | AS AC #1 from shorter prefix; in 156 AS sugg.; 12/27 comp names/subtitles; 12/27 comp descr.; Google AC exact 0, in 36; 26 reviews |
| 2 | workout log | 1 | A | AS AC #2 from shorter prefix; in 98 AS sugg.; 2/27 comp names/subtitles; 3/27 comp descr.; Google AC exact 1, in 10; 2 reviews |
| 3 | gym tracker | 1 | A | AS AC #1 from shorter prefix; in 53 AS sugg.; 3/27 comp names/subtitles; 2/27 comp descr.; Google AC exact 1, in 22 |
| 4 | gym log | 1 | A | AS AC #2 from shorter prefix; in 25 AS sugg.; 4/27 comp names/subtitles; 6/27 comp descr.; Google AC exact 1, in 9 |
| 5 | gym workout tracker | 1 | A | AS AC #1 from shorter prefix; in 22 AS sugg.; 5/27 comp names/subtitles |
| 6 | lifting tracker | 1 | A | AS AC #1 from shorter prefix; in 15 AS sugg.; Google AC exact 1, in 9; 1 reviews |
| 7 | lifting log | 1 | A | AS AC #3 from shorter prefix; in 11 AS sugg.; 1/27 comp names/subtitles; Google AC exact 0, in 3 |
| 8 | lift tracker | 1 | B | AS AC #2 (own prefix); in 10 AS sugg.; Google AC exact 0, in 1 |
| 9 | weight lifting tracker | 1 | A | AS AC #1 from shorter prefix; in 8 AS sugg.; Google AC exact 0, in 1 |
| 10 | weightlifting tracker | 1 | A | AS AC #1 from shorter prefix; in 8 AS sugg.; Google AC exact 1, in 8; 1 reviews |
| 11 | weight lifting log | 1 | A | AS AC #1 from shorter prefix; in 6 AS sugg. |
| 12 | strength training log | 1 | A | AS AC #1 from shorter prefix; in 7 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 2 |
| 13 | strength training tracker | 1 | A | AS AC #1 from shorter prefix; 1/27 comp names/subtitles; 1/27 comp descr.; Google AC exact 0, in 2 |
| 14 | strength log | 1 | A | AS AC #1 from shorter prefix; in 11 AS sugg.; 2/27 comp names/subtitles |
| 15 | strength tracker | 1 | B | AS AC #1 (own prefix); in 9 AS sugg. |
| 16 | workout journal | 1 | A | AS AC #1 from shorter prefix; in 10 AS sugg.; Google AC exact 0, in 7 |
| 17 | workout log book | 1+6 | A | AS AC #1 from shorter prefix; in 1 AS sugg.; Google AC exact 1, in 0 |
| 18 | workout notebook | 1 | A | AS AC #2 from shorter prefix; in 1 AS sugg. |
| 19 | gym notes | 1 | A | AS AC #2 from shorter prefix; in 3 AS sugg.; Google AC exact 0, in 5 |
| 20 | lifting app | 1 | A | AS AC #2 from shorter prefix; in 5 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 9; 10 reviews |
| 21 | strength training app | 1 | A | AS AC #1 from shorter prefix; in 5 AS sugg.; 3/27 comp descr.; Google AC exact 0, in 16; 2 reviews |
| 22 | workout tracker app | 1 | A | AS AC #3 from shorter prefix; in 3 AS sugg.; 1/27 comp descr.; Google AC exact 1, in 24; 2 reviews |
| 23 | gym tracker app | 1 | A | AS AC #1 from shorter prefix; Google AC exact 2, in 13 |
| 24 | simple workout tracker | 1 | B | AS AC #1 (own prefix); in 9 AS sugg.; 1 reviews |
| 25 | gym rest timer | 1 | A | AS AC #1 from shorter prefix; in 9 AS sugg. |
| 26 | workout calendar | 1 | A | AS AC #1 from shorter prefix; in 9 AS sugg. |
| 27 | workout planner | 2 | A | AS AC #1 from shorter prefix; in 25 AS sugg.; 5/27 comp names/subtitles; 4/27 comp descr.; 2 reviews |
| 28 | workout planner and tracker | 2 | B | AS AC #6 from shorter prefix; in 1 AS sugg.; 1 reviews |
| 29 | workout routine | 2 | A | AS AC #1 from shorter prefix; in 10 AS sugg.; 3/27 comp descr.; Google AC exact 0, in 2; 6 reviews |
| 30 | workout routine planner | 2 | A | AS AC #1 from shorter prefix; in 1 AS sugg. |
| 31 | gym workout planner | 2 | A | AS AC #1 from shorter prefix; in 3 AS sugg.; 3/27 comp names/subtitles |
| 32 | gym routine planner | 2 | A | AS AC #1 from shorter prefix; in 1 AS sugg. |
| 33 | workout program | 2 | A | AS AC #3 from shorter prefix; in 4 AS sugg.; 3 reviews |
| 34 | lifting program | 2 | A | AS AC #1 from shorter prefix; 1/27 comp descr.; Google AC exact 0, in 1 |
| 35 | workout split tracker | 2 | A | AS AC #1 from shorter prefix |
| 36 | push pull legs | 2 | A | AS AC #1 from shorter prefix; in 3 AS sugg.; 2/27 comp descr.; Google AC exact 0, in 10; 1 reviews |
| 37 | 5x5 workout | 2 | A | AS AC #2 from shorter prefix; in 7 AS sugg.; 1/27 comp names/subtitles |
| 38 | full body workout | 2 | A | AS AC #2 from shorter prefix; in 3 AS sugg.; 2/27 comp descr. |
| 39 | progressive overload | 3 | B | AS AC #2 (own prefix); in 8 AS sugg.; 7/27 comp descr.; Google AC exact 0, in 32; 15 reviews |
| 40 | progressive overload tracker | 3 | A | AS AC #1 from shorter prefix |
| 41 | gym progress tracker | 3 | A | AS AC #1 from shorter prefix; in 1 AS sugg.; Google AC exact 0, in 6 |
| 42 | workout progress tracker | 3 | A | AS AC #1 from shorter prefix; Google AC exact 0, in 2 |
| 43 | pr tracker | 3 | B | AS AC #2 (own prefix); in 10 AS sugg. |
| 44 | body measurements tracker | 3 | A | AS AC #1 from shorter prefix; in 1 AS sugg.; 1/27 comp descr. |
| 45 | progress photos | 3 | B | AS AC #1 (own prefix); in 9 AS sugg.; 4/27 comp descr.; Google AC exact 0, in 2; 1 reviews |
| 46 | workout stats | 3 | B | AS AC #2 (own prefix); in 2 AS sugg. |
| 47 | beginner workout plans for gym | 4 | A | AS AC #1 from shorter prefix |
| 48 | beginner gym | 4 | B | AS AC #1 (own prefix); in 4 AS sugg.; Google AC exact 0, in 3 |
| 49 | exercise library | 4 | B | AS AC #1 (own prefix); in 2 AS sugg.; 6/27 comp descr.; 7 reviews |
| 50 | workout with friends | 5 | A | AS AC #2 from shorter prefix; in 8 AS sugg. |
| 51 | workout buddy | 5 | A | AS AC #1 from shorter prefix; in 9 AS sugg. |
| 52 | gym buddy | 5 | A | AS AC #1 from shorter prefix; in 9 AS sugg.; Google AC exact 0, in 10 |
| 53 | workout tracker with friends | 5 | A | AS AC #2 from shorter prefix |
| 54 | gym streak | 5 | B | AS AC #6 from shorter prefix; in 2 AS sugg.; Google AC exact 0, in 7 |
| 55 | workout streak | 5 | B | AS AC #6 from shorter prefix; in 4 AS sugg.; Google AC exact 0, in 4 |
| 56 | gym accountability | 5 | A | AS AC #3 from shorter prefix; in 6 AS sugg.; Google AC exact 0, in 7 |
| 57 | gym bros | 5 | A | AS AC #1 from shorter prefix; in 1 AS sugg. |
| 58 | workout notes | 6 | A | AS AC #3 from shorter prefix; in 5 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 4 |
| 59 | workout tracker apple watch | 7 | A | AS AC #1 from shorter prefix; Google AC exact 1, in 0 |
| 60 | watch workout log | 7 | A | AS AC #2 from shorter prefix; in 1 AS sugg. |

The top 60 has no branded 'lightweight' term on purpose. Validate `lightweight workout tracker` separately, because it is a name conflict question. See intent 9.

## Building-block tokens for the 100-character keyword field

These are single words that can be combined across name, subtitle and keyword field. Common ASO practice, which this research did not verify: do not repeat words that are already in the name or subtitle, use commas without spaces, and do not add plurals of words already present.
- Column 1 counts how many of the H/M long-list terms contain the token.
- Column 2 counts how many distinct App Store autocomplete suggestions (out of 2,242 collected) contain it. This shows breadth of use. It is **not** volume.

| Token | # H/M long-list terms | # AS suggestions containing | Note |
|---|---|---|---|
| workout | 115 | 740 | core noun |
| gym | 71 | 587 | core noun |
| tracker | 52 | 410 | core |
| log | 28 | 240 | core |
| lifting | 24 | 105 | core activity |
| lift | 3 | 50 | stem of lifting/lifts |
| weightlifting | 4 | 23 | one-word spelling (separate token from 'weight'+'lifting') |
| weight | 16 | 62 | pairs with lifting/training |
| strength | 16 | 101 | pairs with training/log/tracker |
| training | 23 | 118 | pairs with strength/weight |
| planner | 10 | 91 | plan intent |
| routine | 8 | 44 | plan intent |
| program | 7 | 17 | plan intent |
| split | 5 | 15 | plan intent (PPL etc.) |
| plan | 6 | 27 | plan intent |
| journal | 6 | 45 | log synonym |
| notebook | 2 | 4 | log synonym / notebook import angle |
| notes | 4 | 13 | notes-app switchers |
| logbook | 1 | 14 | log synonym (also 'log book') |
| diary | 4 | 21 | log synonym |
| progress | 10 | 30 | progress intent |
| overload | 4 | 10 | progressive overload |
| progressive | 4 | 10 | progressive overload |
| pr | 2 | 15 | personal records |
| records | 1 | 3 | personal records |
| rest | 4 | 21 | rest timer |
| timer | 5 | 58 | rest timer |
| sets | 3 | 12 | logging detail |
| reps | 2 | 13 | logging detail |
| superset | 2 | 10 | launch feature |
| calendar | 3 | 16 | launch feature |
| stats | 2 | 4 | statistics |
| volume | 3 | 14 | statistics |
| measurements | 3 | 12 | body measurements |
| photos | 3 | 10 | progress photos |
| body | 7 | 41 | body measurements/photos |
| exercise | 6 | 41 | exercise library / exercise log |
| friends | 11 | 23 | social |
| buddy | 2 | 22 | social |
| bro | 1 | 9 | Gym Bro feature |
| streak | 3 | 25 | shared streak |
| accountability | 4 | 34 | social |
| share | 2 | 7 | share workouts |
| watch | 13 | 12 | Apple Watch app (word 'watch' alone is generic) |
| ppl | 1 | 5 | push pull legs (collides with utility brand alone) |
| push | 3 | 12 | push pull legs |
| pull | 3 | 11 | push pull legs |
| legs | 2 | 4 | push pull legs |
| 5x5 | 3 | 14 | ready-made 5x5 |
| beginner | 3 | 16 | beginner programs |
| simple | 3 | 25 | positioning |
| import | 3 | 1 | import feature (no AS demand seen) |
| bodybuilding | 3 | 14 | style |
| powerlifting | 3 | 12 | style |
| hypertrophy | 3 | 10 | style |

Avoid these tokens:
- **Brands:** hevy, strong (as a brand), fitbod, strava, jefit, stronglifts, apple, health, google, sheets, excel, crossfit, duolingo.
- **Features that are not available:** ai, coach, trainer, recovery, generator.
- **Noisy tokens:** 'set' (LEGO/Pokemon set trackers), 'rep' (Replika/Replit), 'program' alone (programming apps), 'routine' alone (habit planners), 'ppl' alone (PPL Electric).

## Long-list grouped by intent

Rows within each intent are sorted by tier, then relevance. The evidence column is abbreviated; `longlist.csv` has exact prefixes and positions.

### 1. Log a workout / tracker (100 terms)

| Term | Rel. | Tier | Evidence | Reason |
|---|---|---|---|---|
| workout tracker | H | A | AS AC #1 from shorter prefix; in 156 AS sugg.; 12/27 comp names/subtitles; 12/27 comp descr.; Google AC exact 0, in 36; 26 reviews | Core category phrase; exact match to launch feature (fast logging) |
| workout log book | H | A | AS AC #1 from shorter prefix; in 1 AS sugg.; Google AC exact 1, in 0 | Notebook-replacement wording |
| workout journal | H | A | AS AC #1 from shorter prefix; in 10 AS sugg.; Google AC exact 0, in 7 | Journal framing of logging |
| workout log app | H | A | AS AC #1 from shorter prefix; in 5 AS sugg.; 1/27 comp descr.; Google AC exact 2, in 1 | Core + 'app' |
| gym tracker | H | A | AS AC #1 from shorter prefix; in 53 AS sugg.; 3/27 comp names/subtitles; 2/27 comp descr.; Google AC exact 1, in 22 | Core category phrase |
| gym journal | H | A | AS AC #1 from shorter prefix; in 6 AS sugg.; Google AC exact 0, in 1; 1 reviews | Journal wording |
| gym tracker app | H | A | AS AC #1 from shorter prefix; Google AC exact 2, in 13 | Core + 'app' |
| gym workout tracker | H | A | AS AC #1 from shorter prefix; in 22 AS sugg.; 5/27 comp names/subtitles | Core; used by 6 competitors in name/subtitle |
| lifting tracker | H | A | AS AC #1 from shorter prefix; in 15 AS sugg.; Google AC exact 1, in 9; 1 reviews | Lifter wording |
| lifting journal | H | A | AS AC #1 from shorter prefix; Google AC exact 0, in 1 | Lifter + journal |
| weight lifting tracker | H | A | AS AC #1 from shorter prefix; in 8 AS sugg.; Google AC exact 0, in 1 | Exact AS AC; core |
| weight lifting log | H | A | AS AC #1 from shorter prefix; in 6 AS sugg. | Exact AS AC; core |
| weight lifting app | H | A | AS AC #1 from shorter prefix; in 1 AS sugg.; 1/27 comp descr. | Exact AS AC |
| weightlifting tracker | H | A | AS AC #1 from shorter prefix; in 8 AS sugg.; Google AC exact 1, in 8; 1 reviews | One-word spelling variant |
| strength training log | H | A | AS AC #1 from shorter prefix; in 7 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 2 | Strength wording; used by Strong/HeavySet |
| strength training tracker | H | A | AS AC #1 from shorter prefix; 1/27 comp names/subtitles; 1/27 comp descr.; Google AC exact 0, in 2 | Strength wording |
| strength log | H | A | AS AC #1 from shorter prefix; in 11 AS sugg.; 2/27 comp names/subtitles | Strength wording |
| strength training app | H | A | AS AC #1 from shorter prefix; in 5 AS sugg.; 3/27 comp descr.; Google AC exact 0, in 16; 2 reviews | Category query |
| gym set tracker | H | A | AS AC #1 from shorter prefix | Set-level logging |
| gym rest timer | H | A | AS AC #1 from shorter prefix; in 9 AS sugg. | Launch feature |
| workout calendar | H | A | AS AC #1 from shorter prefix; in 9 AS sugg. | Launch feature (calendar) |
| workout tracker calendar | H | A | AS AC #1 from shorter prefix | Exact AS AC; calendar |
| workout log | H | A | AS AC #2 from shorter prefix; in 98 AS sugg.; 2/27 comp names/subtitles; 3/27 comp descr.; Google AC exact 1, in 10; 2 reviews | Core; logging sets/reps/weight |
| workout notebook | H | A | AS AC #2 from shorter prefix; in 1 AS sugg. | Paper-notebook wording; fits fast logging + import from notebook photo |
| gym log | H | A | AS AC #2 from shorter prefix; in 25 AS sugg.; 4/27 comp names/subtitles; 6/27 comp descr.; Google AC exact 1, in 9 | Core category phrase |
| gym log book | H | A | AS AC #2 from shorter prefix; in 1 AS sugg.; Google AC exact 1, in 0 | Notebook wording |
| gym notes | H | A | AS AC #2 from shorter prefix; in 3 AS sugg.; Google AC exact 0, in 5 | Notes-app replacement wording |
| gym exercise tracker | H | A | AS AC #2 from shorter prefix | Logging per exercise |
| lifting app | H | A | AS AC #2 from shorter prefix; in 5 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 9; 10 reviews | Generic lifter app query |
| weight training tracker | H | A | AS AC #2 from shorter prefix; in 2 AS sugg.; Google AC exact 0, in 2 | Synonym |
| workout tracker app | H | A | AS AC #3 from shorter prefix; in 3 AS sugg.; 1/27 comp descr.; Google AC exact 1, in 24; 2 reviews | Core + 'app' |
| lifting log | H | A | AS AC #3 from shorter prefix; in 11 AS sugg.; 1/27 comp names/subtitles; Google AC exact 0, in 3 | Lifter wording |
| weight training log | H | A | AS AC #3 from shorter prefix; in 1 AS sugg. | Synonym (weight training) |
| workout tracker free | M | A | AS AC #1 from shorter prefix; in 2 AS sugg. | Freemium: 'free' true for core logging only if free tier allows; check |
| workout log free | M | A | AS AC #1 from shorter prefix; Google AC exact 0, in 1 | Same 'free' caveat |
| gym workout tracker free | M | A | AS AC #1 from shorter prefix | 'free' caveat |
| lifting notepad | M | A | AS AC #1 from shorter prefix | Seen in AS AC (low breadth) |
| fitness logbook | M | A | AS AC #1 from shorter prefix; in 2 AS sugg. | Generic fitness |
| exercise tracker | M | A | AS AC #2 from shorter prefix; in 9 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr.; 2 reviews | Ambiguous with step/calorie/activity trackers |
| gym timer | M | A | AS AC #2 from shorter prefix; in 6 AS sugg. | Mostly interval/HIIT timer apps |
| weight lifting tracking app | M | A | AS AC #3 from shorter prefix | Long-tail |
| workout timer | L | A | AS AC #2 from shorter prefix; in 7 AS sugg.; 1 reviews | Mostly HIIT/interval timers |
| workout logger | H | B | AS AC #4 from shorter prefix; in 6 AS sugg.; Google AC exact 1, in 9 | Logging synonym |
| workout diary | H | B | AS AC #4 from shorter prefix; in 9 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 1 | Synonym for log |
| gym logger | H | B | AS AC #4 from shorter prefix; 1/27 comp descr. | Logging synonym |
| gym calendar | H | B | AS AC #4 from shorter prefix | Launch feature (calendar) |
| workout set tracker | H | B | AS AC #5 from shorter prefix | Set-level logging |
| rest timer for gym | H | B | AS AC #5 from shorter prefix | Launch feature |
| workout rep tracker | H | B | AS AC #6 from shorter prefix | Rep-level logging |
| gym rep tracker | H | B | AS AC #6 from shorter prefix | Rep-level logging |
| workout rest timer | H | B | AS AC #6 from shorter prefix; 1/27 comp descr. | Launch feature |
| gym notebook | H | B | AS AC #7 from shorter prefix; in 1 AS sugg.; 1 reviews | Notebook wording |
| weightlifting log | H | B | AS AC #7 from shorter prefix; in 3 AS sugg.; Google AC exact 0, in 2 | One-word spelling variant |
| gym diary | H | B | AS AC #8 from shorter prefix; in 5 AS sugg. | Diary wording |
| workout tracking | H | B | AS AC #9 from shorter prefix; 2/27 comp descr.; Google AC exact 0, in 3; 12 reviews | Gerund variant of core term |
| exercise log | H | B | AS AC #9 from shorter prefix; in 4 AS sugg.; 2/27 comp names/subtitles | Generic logging |
| gym workout log | H | B | AS AC #1 (own prefix); in 12 AS sugg.; 1/27 comp names/subtitles | Core |
| lift log | H | B | AS AC #1 (own prefix); in 10 AS sugg.; Google AC exact 1, in 1 | Lifter wording |
| lift tracker | H | B | AS AC #2 (own prefix); in 10 AS sugg.; Google AC exact 0, in 1 | Lifter wording |
| weightlifting app | H | B | AS AC #2 (own prefix); in 2 AS sugg.; 2/27 comp descr.; Google AC exact 0, in 9; 9 reviews | One-word spelling variant |
| strength tracker | H | B | AS AC #1 (own prefix); in 9 AS sugg. | Strength wording |
| training log | H | B | AS AC #2 (own prefix); in 17 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr.; Google AC exact 0, in 3 | Athlete wording |
| reps and sets | H | B | AS AC #1 (own prefix); in 1 AS sugg.; 3 reviews | Word-order variant |
| simple workout tracker | H | B | AS AC #1 (own prefix); in 9 AS sugg.; 1 reviews | Positioning wording; fast logging |
| simple gym tracker | H | B | AS AC #1 (own prefix); in 2 AS sugg. | Positioning wording |
| simple workout log | H | B | in 8 AS sugg.; 1/27 comp descr. | Positioning wording |
| rest timer | H | B | AS AC #2 (own prefix); in 18 AS sugg.; 8/27 comp descr.; Google AC exact 0, in 1; 17 reviews | Launch feature |
| gym log free | M | B | AS AC #5 from shorter prefix; in 1 AS sugg. | 'free' caveat |
| workout recorder | M | B | AS AC #10 from shorter prefix | Rare synonym |
| free workout tracker | M | B | in 5 AS sugg.; 3/27 comp descr.; Google AC exact 0, in 8 | Same 'free' caveat |
| strength app | M | B | AS AC #1 (own prefix); in 4 AS sugg.; 1/27 comp descr. | Short, ambiguous |
| fitness log | M | B | AS AC #2 (own prefix); in 7 AS sugg. | Generic fitness |
| fitness journal | M | B | AS AC #1 (own prefix); in 9 AS sugg. | Generic fitness |
| training journal | M | B | in 11 AS sugg.; Google AC exact 0, in 1 | AS AC dominated by BJJ/dance journals |
| training diary | M | B | in 4 AS sugg. | Low breadth |
| set tracker | M | B | AS AC #3 (own prefix); in 8 AS sugg.; 1 reviews | Ambiguous (LEGO/Pokemon sets in AC) |
| workout app | M | B | in 10 AS sugg.; 4/27 comp descr.; Google AC exact 0, in 50; 42 reviews | Very broad; dominated by guided workout apps |
| gym app | M | B | AS AC #2 (own prefix); in 10 AS sugg.; Google AC exact 0, in 25; 2 reviews | Very broad; includes gym membership apps |
| superset | M | B | AS AC #1 (own prefix); in 9 AS sugg.; 2/27 comp descr.; Google AC exact 0, in 10; 2 reviews | Launch feature; AC dominated by non-fitness 'Superset' companies |
| fitness tracker | L | B | AS AC #4 from shorter prefix; in 12 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 14; 3 reviews | Mostly wearable/activity tracker intent |
| workout counter | L | B | AS AC #7 from shorter prefix | Ambiguous |
| workout checklist | L | B | AS AC #8 from shorter prefix | Ambiguous |
| rep counter | L | B | AS AC #1 (own prefix); in 10 AS sugg. | Usually camera/motion auto-counting; Lightweight logs manually |
| fitness app | L | B | AS AC #1 (own prefix); in 11 AS sugg.; 1/27 comp names/subtitles; 5/27 comp descr.; Google AC exact 0, in 15; 16 reviews | Very broad, branded gym apps |
| gym log app | H | C | 1/27 comp descr.; Google AC exact 2, in 5 | Core + 'app' |
| sets and reps | H | C | in 1 AS sugg.; 2/27 comp descr.; 5 reviews | Plain-language logging need |
| track workouts | H | C | Google AC exact 0, in 24; 8 reviews | Plain-language need (Google AC) |
| track lifts | H | C | Google AC exact 0, in 17 | Plain-language need (Google AC) |
| track my lifts | H | C | Google AC exact 1, in 3 | Plain-language need (Google AC) |
| log lifts | H | C | Google AC exact 0, in 3 | Plain-language need (Google AC) |
| workout tracking app | H | C | 1/27 comp descr.; Google AC exact 0, in 1; 10 reviews | Long-tail (Google AC) |
| gym tracker free | M | C | Google AC exact 1, in 0 | 'free' caveat |
| lifting diary | M | C | in 1 AS sugg.; Google AC exact 0, in 1 | Seen only in Google AC |
| minimal workout log | M | C | in 2 AS sugg. | Positioning wording |
| offline workout tracker | M | C | in 2 AS sugg. | Only if app works offline - unconfirmed |
| superset workout | M | C | in 1 AS sugg. | Launch feature |
| drop set | M | C | 1 reviews | Launch feature; no AS AC |
| warm up sets | M | C | 3/27 comp descr.; 1 reviews | Launch feature; no AS AC |
| workout history | M | C | 8 reviews | Feature; no AS AC |
| workout tracker no subscription | L | C | Google AC exact 1, in 0 | Lightweight is a subscription app (Google AC only) |

### 2. Plan or organize a program / routine / split (65 terms)

| Term | Rel. | Tier | Evidence | Reason |
|---|---|---|---|---|
| workout planner | H | A | AS AC #1 from shorter prefix; in 25 AS sugg.; 5/27 comp names/subtitles; 4/27 comp descr.; 2 reviews | Routines/programs/folders |
| workout routine | H | A | AS AC #1 from shorter prefix; in 10 AS sugg.; 3/27 comp descr.; Google AC exact 0, in 2; 6 reviews | Routines |
| workout routine planner | H | A | AS AC #1 from shorter prefix; in 1 AS sugg. | Routine editor |
| workout split tracker | H | A | AS AC #1 from shorter prefix | Exact AS AC |
| gym routine planner | H | A | AS AC #1 from shorter prefix; in 1 AS sugg. | Routine editor |
| gym workout planner | H | A | AS AC #1 from shorter prefix; in 3 AS sugg.; 3/27 comp names/subtitles | Planning |
| lifting program | H | A | AS AC #1 from shorter prefix; 1/27 comp descr.; Google AC exact 0, in 1 | Programs |
| push pull legs | H | A | AS AC #1 from shorter prefix; in 3 AS sugg.; 2/27 comp descr.; Google AC exact 0, in 10; 1 reviews | Ready-made PPL program at launch |
| workout builder | H | A | AS AC #2 from shorter prefix; in 9 AS sugg. | Routine editor |
| workout organizer | H | A | AS AC #2 from shorter prefix; in 1 AS sugg. | Folders + pinning |
| gym planner | H | A | AS AC #2 from shorter prefix; in 9 AS sugg.; 1/27 comp descr. | Planning |
| weight lifting workout planner | H | A | AS AC #2 from shorter prefix; in 1 AS sugg. | Exact AS AC |
| full body workout | H | A | AS AC #2 from shorter prefix; in 3 AS sugg.; 2/27 comp descr. | Ready-made full body program |
| 5x5 workout | H | A | AS AC #2 from shorter prefix; in 7 AS sugg.; 1/27 comp names/subtitles | Ready-made 5x5 program |
| workout program | H | A | AS AC #3 from shorter prefix; in 4 AS sugg.; 3 reviews | Programs |
| gym organizer | H | A | AS AC #3 from shorter prefix | Folders + pinning |
| full body workout routines | H | A | AS AC #3 from shorter prefix | Ready-made program |
| weight lifting workout | M | A | AS AC #1 from shorter prefix; in 3 AS sugg. | Content-ish query |
| training planner | M | A | AS AC #1 from shorter prefix; in 1 AS sugg.; 1/27 comp names/subtitles; 2/27 comp descr. | Mostly endurance |
| 5/3/1 workout | M | A | AS AC #1 from shorter prefix; in 4 AS sugg. | Same caveat |
| workout schedule | M | A | AS AC #2 from shorter prefix; Google AC exact 0, in 1; 1 reviews | No scheduling feature confirmed |
| workout maker | M | A | AS AC #3 from shorter prefix | Routine editor; ambiguous with video makers |
| gym schedule | M | A | AS AC #3 from shorter prefix | No scheduling feature confirmed |
| routine planner | L | A | AS AC #1 from shorter prefix; in 11 AS sugg.; 4/27 comp names/subtitles | Mostly daily-habit planners |
| workout generator | L | A | AS AC #3 from shorter prefix; 1/27 comp descr. | Implies auto-generated plans (AI coach not available) |
| workout plan | H | B | AS AC #4 from shorter prefix; in 10 AS sugg.; 3/27 comp names/subtitles; 5/27 comp descr.; Google AC exact 0, in 12; 4 reviews | Routines/programs |
| workout routine tracker | H | B | AS AC #4 from shorter prefix; 1 reviews | Routines + logging |
| gym routine tracker | H | B | AS AC #4 from shorter prefix | Routines + logging |
| gym routine | H | B | AS AC #5 from shorter prefix; in 7 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 1; 2 reviews | Routines |
| workout planner and tracker | H | B | AS AC #6 from shorter prefix; in 1 AS sugg.; 1 reviews | Exact AS AC; combines plan+log |
| 5x5 workout logger | H | B | AS AC #6 from shorter prefix; in 1 AS sugg. | Exact AS AC |
| gym program | H | B | AS AC #7 from shorter prefix; in 1 AS sugg. | Programs |
| workout programs | H | B | AS AC #8 from shorter prefix; in 3 AS sugg.; 2/27 comp descr.; 3 reviews | Ready-made programs |
| workout split | H | B | AS AC #9 from shorter prefix; in 5 AS sugg. | Splits via routines/programs |
| gym plan | H | B | AS AC #9 from shorter prefix; in 4 AS sugg. | Planning |
| gym workout plan | H | B | AS AC #9 from shorter prefix; in 2 AS sugg.; 1/27 comp names/subtitles; Google AC exact 0, in 4 | Planning |
| gym split tracker | H | B | AS AC #9 from shorter prefix | Splits + logging |
| gym split | H | B | AS AC #10 from shorter prefix; in 1 AS sugg.; 1/27 comp descr. | Splits |
| workout plans | H | B | AS AC #1 (own prefix); in 15 AS sugg.; 4/27 comp descr.; 5 reviews | Ready-made programs |
| gym workout plans | H | B | in 7 AS sugg. | Ready-made programs |
| lifting routine | H | B | 3/27 comp names/subtitles; 1/27 comp descr. | Routines; Hevy/Lyfta/Liftoff subtitles |
| weight lifting routine planner | H | B | 3/27 comp names/subtitles | Competitor subtitle phrase (Hevy/Liftoff/Lyfta) |
| push pull | H | B | AS AC #2 (own prefix); in 8 AS sugg.; 3/27 comp descr.; Google AC exact 0, in 10; 1 reviews | PPL short form |
| 5x5 | H | B | AS AC #4 (own prefix); in 13 AS sugg.; 1/27 comp names/subtitles; 4/27 comp descr.; Google AC exact 0, in 10; 1 reviews | Ready-made 5x5 program |
| muscle building workout split | M | B | AS AC #4 from shorter prefix; in 1 AS sugg. | Split content query |
| strength training plans | M | B | in 4 AS sugg.; 2/27 comp names/subtitles | Coached-plan competitors |
| training plan | M | B | AS AC #2 (own prefix); in 4 AS sugg.; 3/27 comp descr.; Google AC exact 0, in 4 | Mostly running/marathon plans |
| training program | M | B | AS AC #5 (own prefix); in 5 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr.; 1 reviews | Broad |
| fitness planner | M | B | AS AC #2 (own prefix); in 10 AS sugg.; 2/27 comp names/subtitles | Fitbod/JEFIT wording; broad |
| nsuns | L | B | AS AC #1 (own prefix); in 2 AS sugg.; 3/27 comp descr.; 1 reviews | Named program; not confirmed |
| gzclp | L | B | AS AC #1 (own prefix); 3/27 comp descr. | Named program; not confirmed |
| workout program tracker | H | C | in 1 AS sugg. | Programs + logging |
| strength program | H | C | 4/27 comp descr. | Programs |
| push pull legs log | H | C | in 2 AS sugg. | Exact app-title suggestion |
| workout templates | M | C | 2 reviews | Competitor term for routines; no AS AC |
| gym plans | M | C | in 1 AS sugg. | Planning |
| strength training plan | M | C | in 1 AS sugg. | AC dominated by coached plan apps (LADDER/Volt) |
| upper lower | M | C | in 1 AS sugg.; 1/27 comp descr. | Split type; no evidence of a ready-made plan |
| custom workout | M | C | 2/27 comp descr.; 5 reviews | Routine editor |
| create workouts | M | C | 1 reviews | Routine editor |
| phul | L | C | in 2 AS sugg.; 2/27 comp descr. | Named program; not confirmed |
| phat workout | L | C | in 2 AS sugg. | Named program; not confirmed |
| madcow 5x5 | L | C | in 1 AS sugg. | Named program; not confirmed |
| ppl workout | M | D | no observation (inferred) | 'ppl' alone collides with PPL Electric utility |
| workout routine generator | L | D | no observation (inferred) | Implies generation; not available |

### 3. Track progress / PRs / stats / measurements / photos (43 terms)

| Term | Rel. | Tier | Evidence | Reason |
|---|---|---|---|---|
| progressive overload tracker | H | A | AS AC #1 from shorter prefix | Exact AS AC |
| workout progress tracker | H | A | AS AC #1 from shorter prefix; Google AC exact 0, in 2 | Exact AS AC |
| gym progress tracker | H | A | AS AC #1 from shorter prefix; in 1 AS sugg.; Google AC exact 0, in 6 | Exact AS AC |
| strength progress tracker | H | A | AS AC #1 from shorter prefix | Exact AS AC |
| gym pr tracker | H | A | AS AC #1 from shorter prefix | Personal records |
| body measurements tracker | H | A | AS AC #1 from shorter prefix; in 1 AS sugg.; 1/27 comp descr. | Launch feature |
| body progress photos | H | A | AS AC #2 from shorter prefix; in 1 AS sugg. | Launch feature |
| 1rm calculator | L | A | AS AC #1 from shorter prefix; in 9 AS sugg.; 1/27 comp descr. | Calculator apps dominate; feature unconfirmed |
| one rep max calculator | L | A | AS AC #1 from shorter prefix; in 2 AS sugg.; 1/27 comp descr. | Calculator apps dominate |
| track gym progress | H | B | AS AC #5 from shorter prefix; in 2 AS sugg.; Google AC exact 0, in 7 | Exact AS AC |
| track body measurements | H | B | AS AC #6 from shorter prefix | Exact AS AC |
| progressive overload | H | B | AS AC #2 (own prefix); in 8 AS sugg.; 7/27 comp descr.; Google AC exact 0, in 32; 15 reviews | Core lifter goal; previous results inline + PRs |
| workout progress | H | B | in 4 AS sugg.; Google AC exact 0, in 6; 1 reviews | Progress |
| gym progress | H | B | AS AC #4 (own prefix); in 8 AS sugg.; Google AC exact 0, in 18 | Progress |
| pr tracker | H | B | AS AC #2 (own prefix); in 10 AS sugg. | Personal records |
| workout stats | H | B | AS AC #2 (own prefix); in 2 AS sugg. | Statistics feature |
| workout analytics | H | B | AS AC #1 (own prefix); in 3 AS sugg. | Statistics feature |
| gym stats | H | B | AS AC #1 (own prefix) | Statistics feature |
| progress photos | H | B | AS AC #1 (own prefix); in 9 AS sugg.; 4/27 comp descr.; Google AC exact 0, in 2; 1 reviews | Launch feature |
| body measurements | H | B | AS AC #2 (own prefix); in 9 AS sugg.; 6/27 comp descr.; Google AC exact 0, in 7 | Launch feature |
| progressive overload workout | M | B | AS AC #6 from shorter prefix | Content-ish |
| gym progression | M | B | AS AC #8 from shorter prefix; in 1 AS sugg. | Progress |
| one rep max | M | B | AS AC #2 (own prefix); in 8 AS sugg.; 7/27 comp descr. | 1RM estimates not confirmed as feature |
| 1rm | M | B | AS AC #2 (own prefix); in 18 AS sugg.; 8/27 comp descr.; 2 reviews | 1RM estimates not confirmed |
| volume tracker | M | B | AS AC #1 (own prefix); in 3 AS sugg.; 1 reviews | Ambiguous (manga volume tracker) |
| muscle map | M | B | AS AC #1 (own prefix); in 4 AS sugg.; 1/27 comp descr. | Muscle images + muscle balance radar (not a heat map; check) |
| body tracker | M | B | AS AC #1 (own prefix); in 10 AS sugg. | Progress photos/measurements; broad |
| plate calculator | L | B | AS AC #1 (own prefix); in 9 AS sugg.; 9/27 comp descr.; 2 reviews | Feature not confirmed |
| muscle tracker | L | B | AS AC #1 (own prefix); in 6 AS sugg. | AC dominated by GLP-1 muscle trackers |
| progressive overload app | H | C | in 1 AS sugg.; Google AC exact 1, in 7 | Google AC |
| personal records | H | C | in 2 AS sugg.; 9/27 comp descr.; 2 reviews | Personal records feature |
| personal record tracker | H | C | in 1 AS sugg. | Personal records |
| workout volume tracker | H | C | in 2 AS sugg. | Volume stats |
| gym progress photos | H | C | in 2 AS sugg.; Google AC exact 0, in 1 | Launch feature |
| progress pics | H | C | in 1 AS sugg.; 1 reviews | Launch feature |
| workout analysis | M | C | in 2 AS sugg. | Used in name of 'Lightweight! Workout Analysis' |
| training volume | M | C | in 1 AS sugg.; 1/27 comp descr.; 1 reviews | Volume stats |
| muscle groups | M | C | 8/27 comp descr.; 2 reviews | Muscle stats |
| strength gains | M | C | 3/27 comp descr.; 1 reviews | Outcome wording |
| muscle heat map | L | C | in 1 AS sugg. | Different visualization than radar |
| workout statistics | H | D | no observation (inferred) | Statistics feature |
| muscle balance | M | D | no observation (inferred) | Muscle balance radar; no AS AC |
| workout charts | M | D | no observation (inferred) | Stats wording |

### 4. Beginners / start strength training / ready-made plans (25 terms)

| Term | Rel. | Tier | Evidence | Reason |
|---|---|---|---|---|
| beginner workout plans for gym | H | A | AS AC #1 from shorter prefix | Exact AS AC; basic ready-made programs |
| workout exercises | M | A | AS AC #1 from shorter prefix; in 3 AS sugg.; 1/27 comp descr.; 1 reviews | Exercise library |
| gym workout | M | A | AS AC #2 from shorter prefix; in 69 AS sugg.; 10/27 comp names/subtitles; 2/27 comp descr.; Google AC exact 0, in 9; 1 reviews | Broad |
| workout for men | L | A | AS AC #3 from shorter prefix; in 9 AS sugg.; 1/27 comp descr. | Home-workout content apps |
| beginner gym | H | B | AS AC #1 (own prefix); in 4 AS sugg.; Google AC exact 0, in 3 | Exact AS AC |
| exercise library | H | B | AS AC #1 (own prefix); in 2 AS sugg.; 6/27 comp descr.; 7 reviews | Launch feature |
| workout plan app free | M | B | AS AC #4 from shorter prefix | 'free' caveat |
| workout beginners | M | B | AS AC #5 from shorter prefix | AS AC |
| gym guide | M | B | AS AC #7 from shorter prefix; in 1 AS sugg. | Exercise instructions |
| beginner workout | M | B | AS AC #2 (own prefix); in 5 AS sugg.; Google AC exact 0, in 4 | Ready-made basic programs; AC mixes home/no-equipment |
| exercise guide | M | B | in 3 AS sugg. | Instructions feature |
| gym exercises | M | B | in 3 AS sugg.; 1 reviews | Exercise library |
| gym workout for men | L | B | AS AC #4 from shorter prefix | Content apps; gendered |
| muscle anatomy | L | B | AS AC #5 from shorter prefix; in 4 AS sugg. | AC: anatomy study/game apps |
| gym app for beginners | H | C | Google AC exact 3, in 6 | Google AC |
| lifting app for beginners | H | C | Google AC exact 1, in 0 | Google AC |
| strength training app for beginners | H | C | Google AC exact 2, in 3 | Google AC |
| weight training app for beginners | H | C | Google AC exact 2, in 3 | Google AC |
| workout app for beginners | M | C | Google AC exact 2, in 5 | Google AC; broad |
| strength training for beginners | M | C | Google AC exact 0, in 1 | Content query |
| free workout plans | M | C | in 1 AS sugg. | 'free' caveat; ready-made programs |
| how to start lifting | L | C | Google AC exact 1, in 9 | Informational (Google only) |
| how to start strength training | L | C | Google AC exact 1, in 9 | Informational (Google only) |
| gym for beginners | H | D | no observation (inferred) | Google AC |
| gym exercise library | H | D | no observation (inferred) | Launch feature |

### 5. Train with friends / accountability / streak / social (43 terms)

| Term | Rel. | Tier | Evidence | Reason |
|---|---|---|---|---|
| workout buddy | H | A | AS AC #1 from shorter prefix; in 9 AS sugg. | Social; exact AS AC |
| gym buddy | H | A | AS AC #1 from shorter prefix; in 9 AS sugg.; Google AC exact 0, in 10 | Social; exact AS AC |
| gym bros | H | A | AS AC #1 from shorter prefix; in 1 AS sugg. | Feature name |
| workout with friends | H | A | AS AC #2 from shorter prefix; in 8 AS sugg. | Gym Bro social; 9+ apps use exact phrase |
| workout tracker with friends | H | A | AS AC #2 from shorter prefix | Exact AS AC; core + social |
| gym friends | H | A | AS AC #3 from shorter prefix; in 1 AS sugg. | Social |
| gym accountability | H | A | AS AC #3 from shorter prefix; in 6 AS sugg.; Google AC exact 0, in 7 | Social accountability |
| workout motivation | M | A | AS AC #1 from shorter prefix; in 4 AS sugg. | AC mostly music/quotes |
| workout reminder | M | A | AS AC #2 from shorter prefix | Nudge/push from a friend; not scheduled reminders |
| streak tracker | L | A | AS AC #1 from shorter prefix; in 8 AS sugg.; Google AC exact 0, in 1 | Mostly habit trackers |
| accountability partner | L | A | AS AC #1 from shorter prefix; in 7 AS sugg.; Google AC exact 0, in 2 | AC dominated by habit/faith apps |
| gym ranked | L | A | AS AC #1 from shorter prefix; in 2 AS sugg. | Ranks/leagues not a feature |
| workout streak | H | B | AS AC #6 from shorter prefix; in 4 AS sugg.; Google AC exact 0, in 4 | Shared streak |
| gym streak | H | B | AS AC #6 from shorter prefix; in 2 AS sugg.; Google AC exact 0, in 7 | Shared streak; exact AS AC |
| gym bro | H | B | in 7 AS sugg.; Google AC exact 0, in 8 | Feature name 'Gym Bro'; AS AC 'gym bros' |
| workout accountability | H | B | AS AC #1 (own prefix); in 1 AS sugg.; Google AC exact 0, in 8 | Social accountability |
| lift with friends | H | B | in 3 AS sugg. | AS AC (app titles) |
| share workouts | H | B | in 6 AS sugg.; 4/27 comp descr.; Google AC exact 0, in 2 | Share finished workouts |
| social workout tracker | H | B | in 4 AS sugg. | AS AC (app titles) |
| gym partner | M | B | AS AC #4 from shorter prefix; in 6 AS sugg.; Google AC exact 0, in 1 | AC: partner-finder apps (matching strangers) - Lightweight is friends you know |
| gym motivation | M | B | AS AC #4 from shorter prefix; in 4 AS sugg. | Motivation (streak/nudge/mascot) |
| workout pet | M | B | AS AC #10 from shorter prefix | Optional dinosaur mascot |
| fitness streak | M | B | in 3 AS sugg.; Google AC exact 0, in 1 | Streak |
| fitness accountability | M | B | AS AC #1 (own prefix); in 5 AS sugg.; Google AC exact 0, in 3 | Social accountability |
| social fitness | M | B | in 11 AS sugg. | Social; broad |
| fitness social | M | B | AS AC #1 (own prefix); in 7 AS sugg. | Social; broad |
| gym community | M | B | in 4 AS sugg. | No public community feed confirmed (friends only) |
| fitness challenge with friends | M | B | AS AC #1 (own prefix) | No challenges feature confirmed |
| couples workout | M | B | AS AC #1 (own prefix); in 2 AS sugg. | Friends feature could serve couples |
| fitness pet | M | B | AS AC #1 (own prefix); in 1 AS sugg. | Optional dinosaur mascot |
| workout challenge | L | B | AS AC #4 from shorter prefix; in 2 AS sugg.; Google AC exact 0, in 1 | Challenges not confirmed |
| nudge | L | B | AS AC #1 (own prefix); in 6 AS sugg. | Generic word; AC brand apps |
| gym check in | L | B | AS AC #1 (own prefix); in 1 AS sugg.; Google AC exact 0, in 1 | Check-in apps (gym access) |
| roast me | L | B | AS AC #1 (own prefix); in 6 AS sugg. | AC = AI comedy apps; mascot roasts are minor |
| workout game | L | B | in 5 AS sugg.; 1 reviews | Gamification not core |
| gym tracker with friends | H | C | Google AC exact 1, in 0 | Google AC |
| workout app with friends | H | C | Google AC exact 2, in 0 | Google AC |
| gym app with friends | H | C | Google AC exact 1, in 1 | Google AC |
| lifting app with friends | H | C | Google AC exact 1, in 0 | Google AC |
| workout accountability app with friends | H | C | Google AC exact 1, in 2 | Google AC long-tail |
| share workout | H | C | Google AC exact 0, in 1; 1 reviews | Share finished workouts |
| fitness app with friends | M | C | Google AC exact 2, in 0 | Google AC; broad |
| partner workout | M | C | in 1 AS sugg. | Friends feature |

### 6. Import / switch / notes / spreadsheet (17 terms)

| Term | Rel. | Tier | Evidence | Reason |
|---|---|---|---|---|
| workout notes | H | A | AS AC #3 from shorter prefix; in 5 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 4 | Users moving from notes app |
| workout export | M | A | AS AC #2 from shorter prefix | Export not confirmed |
| workout notepad | H | B | AS AC #8 from shorter prefix | AS AC |
| workout import | H | C | in 1 AS sugg. | Import from screenshot/photo/text/voice/CSV |
| ai workout import | H | C | in 1 AS sugg. | AI turns notes into routines |
| workout scanner | H | C | in 2 AS sugg. | Import from screenshot/photo |
| workout notes app | H | C | Google AC exact 1, in 3 | Google AC |
| gym notes app | H | C | Google AC exact 1, in 4 | Google AC |
| workout journal app | H | C | Google AC exact 1, in 5 | Google AC |
| import workouts | H | C | Google AC exact 0, in 5; 1 reviews | CSV/history import (Google AC with competitor names) |
| workout spreadsheet | M | C | Google AC exact 1, in 5 | Google AC; spreadsheet users are switch candidates (CSV import) |
| gym spreadsheet | M | C | Google AC exact 1, in 8 | Google AC; noisy (resale 'spreadsheets') |
| lifting spreadsheet | M | C | Google AC exact 1, in 4 | Google AC |
| workout tracker spreadsheet | M | C | Google AC exact 1, in 3 | Google AC |
| workout log spreadsheet | M | C | Google AC exact 1, in 1 | Google AC |
| paper workout log | M | C | in 1 AS sugg. | Photo-of-notebook import angle (inferred; not observed as AC) |
| switch workout app | M | D | no observation (inferred) | Inferred from reviews ('switched'); no AC |

### 7. Apple Watch / Health / Strava (16 terms)

| Term | Rel. | Tier | Evidence | Reason |
|---|---|---|---|---|
| apple watch workout app | H | A | AS AC #1 from shorter prefix; Google AC exact 2, in 9; 1 reviews | Watch app |
| workout tracker apple watch | H | A | AS AC #1 from shorter prefix; Google AC exact 1, in 0 | Exact AS AC |
| watch workout log | H | A | AS AC #2 from shorter prefix; in 1 AS sugg. | Exact AS AC |
| workout apple watch | H | A | AS AC #3 from shorter prefix; Google AC exact 0, in 1 | Watch app; exact AS AC |
| apple watch gym | H | B | AS AC #1 (own prefix); Google AC exact 0, in 8 | Exact AS AC |
| fitness app apple watch | M | B | AS AC #5 from shorter prefix; Google AC exact 1, in 1 | Broad |
| watch workout | M | B | in 5 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 12; 2 reviews | Watch app |
| apple watch gym app | H | C | Google AC exact 2, in 3 | Google AC |
| apple watch gym tracker | H | C | Google AC exact 1, in 1 | Google AC |
| apple watch lifting app | H | C | Google AC exact 1, in 0 | Google AC |
| apple watch strength training app | H | C | Google AC exact 2, in 1 | Google AC |
| apple watch weight training app | H | C | Google AC exact 1, in 1 | Google AC |
| gym log apple watch | H | C | Google AC exact 1, in 0 | Google AC |
| workout app that syncs with apple health | H | C | Google AC exact 1, in 0 | Google AC |
| heart rate | M | C | in 1 AS sugg.; 9/27 comp descr.; 11 reviews | Watch heart rate; AC dominated by HR monitors |
| health sync | M | C | 2/27 comp descr. | Apple Health integration (no AC observed) |

### 8. Specific styles and activities (48 terms)

| Term | Rel. | Tier | Evidence | Reason |
|---|---|---|---|---|
| strength training | H | A | AS AC #2 from shorter prefix; in 37 AS sugg.; 6/27 comp names/subtitles; 15/27 comp descr.; Google AC exact 0, in 40; 13 reviews | Core activity |
| lifting weights | H | A | AS AC #2 from shorter prefix; in 1 AS sugg.; 2/27 comp descr.; Google AC exact 0, in 7; 1 reviews | Core activity |
| powerlifting program | M | A | AS AC #1 from shorter prefix | Programs; no powerlifting template confirmed |
| strength training for women | M | A | AS AC #1 from shorter prefix; Google AC exact 0, in 1 | Same |
| weight lifting for women | M | A | AS AC #1 from shorter prefix; in 1 AS sugg. | Same |
| muscle building app | M | A | AS AC #2 from shorter prefix; in 1 AS sugg. | Goal |
| workout for women | L | A | AS AC #1 from shorter prefix; in 7 AS sugg.; 1/27 comp descr. | Home-workout content apps |
| calisthenics workout | L | A | AS AC #1 from shorter prefix; in 2 AS sugg.; Google AC exact 0, in 2 | Same |
| dumbbell home workout | L | A | AS AC #1 from shorter prefix; in 1 AS sugg. | Content apps |
| dumbbell workout | L | A | AS AC #2 from shorter prefix; in 1 AS sugg. | Content apps |
| ai workout planner | X | A | AS AC #1 from shorter prefix; in 3 AS sugg. | AI coach NOT available |
| ai gym coach | X | A | AS AC #1 from shorter prefix; in 3 AS sugg. | AI coach NOT available |
| weight training | H | B | AS AC #5 (own prefix); in 11 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 10; 5 reviews | Core activity |
| weight lifting | H | B | AS AC #5 (own prefix); in 31 AS sugg.; 9/27 comp names/subtitles; 4/27 comp descr.; Google AC exact 0, in 7; 4 reviews | Core activity |
| weightlifting | H | B | AS AC #3 (own prefix); in 22 AS sugg.; 1/27 comp names/subtitles; 6/27 comp descr.; Google AC exact 0, in 26; 18 reviews | Core activity (also olympic weightlifting) |
| lifting | H | B | AS AC #7 (own prefix); in 104 AS sugg.; 10/27 comp names/subtitles; 11/27 comp descr.; Google AC exact 0, in 61; 33 reviews | Core activity |
| barbell workout | M | B | AS AC #6 from shorter prefix | Barbell lifting fits |
| bodybuilding | M | B | AS AC #3 (own prefix); in 13 AS sugg.; 1/27 comp names/subtitles; 8/27 comp descr.; 4 reviews | Logger fits bodybuilders; AC brand-heavy (bodybuilding.com) |
| bodybuilding app | M | B | in 4 AS sugg. | Logger fits bodybuilders |
| powerlifting | M | B | AS AC #3 (own prefix); in 11 AS sugg.; 3/27 comp descr.; 1 reviews | Logger fits; no meet/RPE tools confirmed |
| hypertrophy | M | B | AS AC #2 (own prefix); in 9 AS sugg.; 4/27 comp descr.; 3 reviews | Logger fits; AC brand-heavy (RP) |
| muscle building | M | B | in 10 AS sugg.; 1/27 comp descr.; 1 reviews | Goal; logger fits |
| lifting for women | M | B | in 3 AS sugg. | Same |
| home workout planner | L | B | AS AC #7 from shorter prefix; in 1 AS sugg. | Same |
| fitness and bodybuilding | L | B | AS AC #8 from shorter prefix | Content apps |
| muscle gain | L | B | AS AC #2 (own prefix); in 7 AS sugg.; 2/27 comp descr. | AC dominated by nutrition/protein trackers |
| calisthenics | L | B | AS AC #5 (own prefix); in 9 AS sugg.; Google AC exact 0, in 2 | Bodyweight skill apps; logger can log but not positioned |
| home workout | L | B | AS AC #3 (own prefix); in 25 AS sugg. | Guided home workout apps |
| bench press | L | B | AS AC #2 (own prefix); in 7 AS sugg.; 2/27 comp descr.; 2 reviews | Single-lift apps |
| squat | L | B | in 5 AS sugg.; 1/27 comp descr.; 3 reviews | Mostly counters/challenges |
| deadlift | L | B | in 4 AS sugg.; 2/27 comp descr.; 1 reviews | Form-check apps |
| weight loss | X | B | AS AC #4 from shorter prefix; in 4 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 1 | Irrelevant (no nutrition) |
| ai personal trainer | X | B | AS AC #6 from shorter prefix; in 1 AS sugg.; 1/27 comp names/subtitles | AI coach NOT available |
| hiit | X | B | AS AC #6 (own prefix); in 13 AS sugg.; 1/27 comp names/subtitles; 3/27 comp descr. | Interval timers; irrelevant |
| cardio | X | B | AS AC #3 (own prefix); in 6 AS sugg.; 10/27 comp descr.; 7 reviews | Irrelevant |
| running | X | B | in 6 AS sugg.; 2/27 comp descr.; 6 reviews | Irrelevant |
| yoga | X | B | in 6 AS sugg.; 2/27 comp descr. | Irrelevant |
| muscle recovery | X | B | in 6 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 1 | Recovery tracking NOT available (future) |
| personal trainer | X | B | AS AC #1 (own prefix); in 9 AS sugg.; 2/27 comp names/subtitles; 5/27 comp descr.; 3 reviews | No coaching |
| bodybuilding workout | M | C | in 1 AS sugg. | Content apps |
| powerlifting tracker | M | C | in 1 AS sugg. | Logger fits |
| hypertrophy log | M | C | in 1 AS sugg. | Logger fits |
| build muscle | M | C | 5/27 comp descr. | Goal wording in descriptions |
| olympic weightlifting | L | C | in 1 AS sugg. | Technique-specific |
| kettlebell | L | C | in 2 AS sugg.; 1/27 comp descr.; 2 reviews | Equipment-specific content |
| workout coach | X | C | in 2 AS sugg. | No coaching |
| hypertrophy workout | M | D | no observation (inferred) | Content |
| weight training for women | M | D | no observation (inferred) | Logger fits; AC dominated by women-specific plan apps |

### 9. Branded 'lightweight' terms (9 terms)

| Term | Rel. | Tier | Evidence | Reason |
|---|---|---|---|---|
| lightweight workout tracker | H | A | AS AC #2 from shorter prefix | Brand+category; collides with 'Lightweight: Workout Tracker' (id 6762335584) |
| lightweight | H | B | AS AC #2 (own prefix); in 11 AS sugg. | Brand; but 3 existing apps already use name (conflict) |
| lw | L | B | in 4 AS sugg. | Abbreviation; AC unrelated; 'LW: Gym Workout Tracker & Log' exists |
| lightweight workout | H | C | in 2 AS sugg. | Brand; AC already returns two other 'Lightweight' apps |
| yeah buddy | L | C | in 1 AS sugg. | Meme phrase; AS AC 'yeah buddy app' exists |
| lightweight gym | M | D | no observation (inferred) | Brand+category; no AC |
| lightweight app | M | D | no observation (inferred) | Brand; AC 'lightweight browser' etc. |
| light weight | M | D | no observation (inferred) | Spacing variant; AS AC maps to 'lightweight' |
| lightweight baby | L | D | no observation (inferred) | Meme phrase (Ronnie Coleman); no AS AC observed |

## Brand terms: do not use in keywords

These are competitor or third-party trademarks. Leave them out of the name, subtitle and keyword field. Integrations such as Apple Health and Strava can be described in the description text, in line with Apple's guidelines; check before use.

| Term | Why | Evidence |
|---|---|---|
| dropset | Competitor app name (also a generic lifting term 'drop set' - use the two-word form) | AS AC #1 (own prefix); in 2 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr.; 5 reviews |
| 5/3/1 | Program name associated with Jim Wendler - verify trademark status before use | AS AC #2 (own prefix); in 9 AS sugg.; 3/27 comp descr. |
| crossfit | CrossFit trademark | AS AC #1 (own prefix); in 10 AS sugg.; 1 reviews |
| hevy | Competitor app (Hevy) | AS AC #1 (own prefix); in 10 AS sugg.; 1/27 comp names/subtitles; 4/27 comp descr.; Google AC exact 0, in 26; 39 reviews |
| hevy alternative | Competitor brand + switch intent | Google AC exact 0, in 2 |
| apps like hevy | Competitor brand + switch intent | Google AC exact 1, in 4 |
| strong app | Competitor app (Strong) - 'strong' as generic adjective is fine only outside brand context | Google AC exact 0, in 13; 3 reviews |
| strong app alternative | Competitor brand + switch intent | Google AC exact 1, in 4 |
| apps like strong | Competitor brand + switch intent | 1/27 comp descr.; Google AC exact 2, in 2 |
| hevy vs strong | Competitor comparison query | Google AC exact 1, in 7 |
| fitbod | Competitor app | in 1 AS sugg.; 1/27 comp names/subtitles; 2/27 comp descr.; Google AC exact 0, in 11 |
| fitbod alternative | Competitor brand + switch intent | Google AC exact 0, in 4 |
| jefit | Competitor app | in 1 AS sugg.; 1/27 comp names/subtitles; 2/27 comp descr.; Google AC exact 0, in 1; 3 reviews |
| stronglifts | Competitor app/program brand | AS AC #3 (own prefix); in 4 AS sugg.; 1/27 comp names/subtitles; 4/27 comp descr.; Google AC exact 0, in 4; 5 reviews |
| stronglifts 5x5 | Competitor app/program brand | in 2 AS sugg.; 1/27 comp names/subtitles; 3/27 comp descr.; Google AC exact 0, in 2; 1 reviews |
| boostcamp | Competitor app | in 1 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr.; Google AC exact 0, in 1; 10 reviews |
| setgraph | Competitor app | in 1 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr.; 9 reviews |
| alpha progression | Competitor app | 1/27 comp names/subtitles; 1/27 comp descr. |
| heavyset | Competitor app | in 1 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr. |
| strengthlog | Competitor app | 1/27 comp names/subtitles; 1/27 comp descr. |
| liftin | Competitor app | 1/27 comp names/subtitles; 1/27 comp descr.; 26 reviews |
| liftosaur | Competitor app | AS AC #10 from shorter prefix; 1/27 comp names/subtitles; 1/27 comp descr. |
| lyfta | Competitor app | in 2 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr. |
| gymbook | Competitor app | AS AC #1 (own prefix); in 5 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr.; 1 reviews |
| gymverse | Competitor app | AS AC #4 from shorter prefix; in 1 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr. |
| liftoff | Competitor app | AS AC #3 from shorter prefix; in 1 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr. |
| gymrats | Third-party app name | AS AC #1 from shorter prefix; in 1 AS sugg. |
| ladder | Competitor app (LADDER) | in 1 AS sugg.; 1/27 comp names/subtitles; 1/27 comp descr.; 1 reviews |
| trainheroic | Competitor app | in 1 AS sugg. |
| strava | Integration partner trademark (Strava) - describe in description only | 4/27 comp descr.; Google AC exact 0, in 7; 7 reviews |
| apple health | Apple trademark - describe compatibility in description; check Apple guidelines before keyword use | 15/27 comp descr.; Google AC exact 0, in 5; 2 reviews |
| apple watch | Apple trademark - common in competitor descriptions; check Apple guidelines before keyword use | in 5 AS sugg.; 1/27 comp names/subtitles; 13/27 comp descr.; Google AC exact 0, in 76; 82 reviews |
| google sheets | Google trademark | Google AC exact 0, in 7; 2 reviews |
| excel | Microsoft trademark | in 1 AS sugg.; 1/27 comp descr.; Google AC exact 0, in 4; 3 reviews |
| duolingo | Third-party brand (appeared as 'workout duolingo' in AS AC) | in 1 AS sugg. |
| starting strength | Program/brand trademark | AS AC #1 (own prefix); in 3 AS sugg.; 1/27 comp descr.; 1 reviews |
| rp hypertrophy | Competitor brand (RP Strength) | AS AC #1 from shorter prefix; 1/27 comp descr. |
| musclewiki | Third-party brand | AS AC #2 from shorter prefix |
| myfitnesspal | Third-party brand | AS AC #5 (own prefix); Google AC exact 0, in 1; 1 reviews |
| gymshark | Third-party brand | AS AC #1 from shorter prefix |
| garmin | Third-party brand | Google AC exact 0, in 6; 3 reviews |
| whoop | Third-party brand | Google AC exact 0, in 2 |
| macrofactor | Third-party brand | Google AC exact 0, in 2 |
| bodybuilding.com | Third-party brand | AS AC #1 from shorter prefix |