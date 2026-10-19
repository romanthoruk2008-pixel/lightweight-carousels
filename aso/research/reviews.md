# Recent US reviews — Hevy, Strong, Dropset, Fitbod, StrengthLog, Alpha Progression

Source: `https://itunes.apple.com/us/rss/customerreviews/page={1,2,3}/id=<ID>/sortby=mostrecent/json`, fetched 2026-10-19. The RSS feed returns at most 50 reviews per page and 3 pages here, so up to 150 per app. Raw files are in `raw/reviews/`. The flattened file is `raw/reviews_flat.csv` and per-theme matches are in `raw/review_themes.json`.

| App | Reviews collected | Date range of those reviews | Avg ★ of sample | ★ distribution (1/2/3/4/5) |
|---|---|---|---|---|
| Hevy | 150 | 2026-10-13 → 2026-10-17 | 4.91 | 1/0/2/6/141 |
| Strong | 150 | 2026-04-01 → 2026-10-07 | 3.73 | 17/17/20/31/65 |
| Fitbod | 150 | 2026-09-12 → 2026-10-17 | 3.73 | 33/6/10/21/80 |
| StrengthLog | 150 | 2024-02-20 → 2026-10-15 | 4.50 | 9/5/8/8/120 |
| Alpha Progression | 150 | 2024-08-12 → 2026-10-16 | 4.61 | 7/1/8/11/123 |
| Dropset | 28 (all the feed has; pages 2–3 empty) | 2024-01-03 → 2026-05-05 | 4.14 | 1/1/5/7/14 |

**Observation on review velocity (inference):** Hevy's latest 150 written reviews all fall within 5 days. Strong's 150 cover about 6 months, and StrengthLog's and Alpha's about 2 years. This suggests Hevy currently gets written US reviews at a far higher rate than the others. Recent-review samples are not representative of all-time ratings: Strong's recent sample averages 3.73★ against 4.86★ all-time.

## Method and caveats
Theme counts come from case-insensitive keyword regexes over title + body (patterns are in `scripts/themes.py`, kept outside `aso/`). A review can hit several themes. Counts are **mentions**, not sentiment: "no ads" counts under *ads*, and "free version is great" counts under *paywall/price*. The number in parentheses is how many of those mentions came from 1–2★ reviews. I read the matching reviews for the themes below, and the verdicts summarise that reading. Quotes are verbatim excerpts.

## Theme matrix (mentions, (of which 1–2★))
| Theme | Hevy | Strong | Fitbod | StrengthLog | Alpha | Dropset |
|---|---|---|---|---|---|---|
| Ease of logging / simple / intuitive / fast | 54 (0) | 37 (4) | 23 (1) | 49 (1) | 54 (0) | 11 (1) |
| Paywall / price / subscription / free | 24 (0) | 43 (11) | 38 (23) | 73 (5) | 43 (6) | 6 (1) |
| Apple Watch | 12 (1) | **45 (20)** | 15 (6) | 9 (4) | 10 (0) | 4 (0) |
| Bugs / sync / data loss | 4 (1) | **34 (18)** | 20 (10) | 10 (3) | 7 (2) | 2 (0) |
| Progress / PRs / charts / stats | 33 (0) | 20 (3) | 9 (2) | 28 (1) | 24 (2) | 3 (0) |
| Routines / programs / templates | 14 (1) | 22 (8) | 5 (2) | 31 (5) | 29 (0) | 4 (0) |
| Progressive overload / recommendations | 25 (0) | 20 (3) | 19 (4) | 21 (1) | **54 (1)** | 4 (0) |
| Social / friends / community / share | **20 (0)** | 9 (2) | 7 (3) | 6 (1) | 11 (0) | 1 (0) |
| Beginners / new to lifting | 6 (0) | 2 (2) | 12 (3) | 10 (0) | 17 (0) | 0 |
| Switching / importing / exporting | 5 (0) | 11 (3) | 4 (1) | 7 (1) | 11 (0) | 2 (0) |
| CSV / spreadsheet / notes app / paper / notebook | 6 (0) | 8 (3) | 2 (0) | 18 (1) | 10 (0) | 3 (0) |
| AI | 4 (0) | 4 (0) | **17 (8)** | 4 (0) | 6 (0) | 0 |
| Ads | 1 (0) | 4 (0) | 1 (0) | 8 (0) | 0 | 0 |
| Rest timer | 5 (1) | 10 (2) | 0 | 5 (0) | 11 (0) | 2 (0) |
| Exercise library / videos / custom exercises | 6 (0) | 11 (3) | 4 (0) | 18 (0) | 15 (0) | 3 (1) |
| Apple Health / Strava | 2 (0) | 5 (0) | 4 (2) | 2 (0) | 2 (0) | 0 |

## Per-app summary

### Hevy (very positive; 141/150 are 5★)
- **Praise:** easy logging, free tier is generous, progress/PR tracking, and the social/accountability side.
  - "my friend got me to start using it because i was using notes app before, and i'm so glad i switched"
  - "A friend and I use it every time we workout to hold each other accountable"
  - "community accountability aspect of the app sets it apart."
- **Complaints (few):** Apple Watch sync. "Apple Watch live sync constantly fails." / "Doesn't stay connected on Apple Watch."
- Beginners: 6 mentions, all positive ("I am a beginner to all things lifting and this app has been so very helpful.").

### Strong (mixed; long-time users unhappy)
- **Dominant complaint is Apple Watch sync** (45 mentions, 20 of them 1–2★), often with lost sets or data.
  - "Watch App Integration bugs on EVERY Workout."
  - "If you use the 'live sync' feature … the app will regularly lose sets you have already saved."
- **Paywall:** the 3-template free limit is a recurring complaint. "not allowing users to create more than 3 diy workout templates unless they pay a subscription should be borderline illegal."
- **Churn to competitors:** "uninstalled and went with Hevy" (missing Live Activity). "Hevy app gives more options, insights and charts than this app."
- **Import request:** "the inability to import workouts and lack of Ai comparability is about to make me jump ship".
- **Social request:** "Please make it so I can add my friends on this app and we can share our workouts and see our PRs!!"
- **Praise:** simple and fast, no ads, longevity ("I've logged 963 workouts"), and anti-AI sentiment ("No AI BS just straight to the point").

### Fitbod (polarised; 33 of 150 are 1★)
- **Billing/trial anger dominates the negatives:** charged after cancelling, forced trial after an onboarding quiz, $15–16/month.
  - "Unpassable paywall after annoying time consuming quiz"
  - "I cancelled my trial period three days before it was up and STILL got charged!!"
- **AI coach backlash** (17 AI mentions, 8 of them 1–2★): "AI ruining another app…", "Not great AI".
- **Praise:** beginners and "tell me what to do" users. "I was a total beginner at strength training and this app is so intuitive". "When I started working out, I had no direction and I feel like Fitbod really put me on the right path."
- **Family plan disappointment:** users expected shared stats ("we can see each other workouts").

### StrengthLog (positive, but price and paywall friction)
- **Praise:** free logging with no ads, many free programs, exercise library, and switching away from notebooks or spreadsheets.
  - "I can FINALLY say goodbye to planning workouts in my notes app."
  - "I started tracking my workouts on a spreadsheet. Old School. Found this app and it's a GameChanger!"
- **Complaints:** the price ($16/month, about $100/yr) and stats locked behind premium.
  - "Paying $100 a year for a tracking app seemed kind of steep."
  - "free is only good for logging workouts … All stats and graphs are entirely locked behind pr[emium]".
- **Watch:** 4 negative ("the apple watch app doesn't function at all").

### Alpha Progression (positive; auto-progression is the hook)
- **Praise:** progression suggestions (54 mentions), the plan generator, and being beginner-friendly.
  - "it gives actual advice on how to improve weight, technique, and reps."
  - "Best App for Beginners".
- **Most common request: an Apple Watch app** (10 mentions, all asking for one). "Great app but lacking Apple Watch interface".
- **Complaints:** features moved behind the paywall and auto-charge after the trial. "even things that a spreadsheet would do just as well such as recording RIR are now behind a paywall".

### Dropset (small sample, 28)
- **Praise:** clean UI, personalisation, and replacing the Notes app.
- **The #1 request is an Apple Watch app** (4 of 28). "Will switch from Hevy once Apple Watch is supported."

## Cross-app takeaways (focus items requested)
- **Switching/importing:** people describe switching *from notes app, paper, spreadsheets or a trainer* more often than from another app. App-to-app switching shows up mainly as Strong → Hevy. Explicit **import** requests appear once (Strong). The regex's other "import" hits are false positives ("important"). No review mentions CSV import. CSV *export* is praised (Hevy, StrengthLog).
- **CSV:** 2 mentions, both about *export*: Hevy (praise: "I can very easily export everything to csv for Claude analysis and tips") and Strong (complaint: workout data "buried way over under settings with an option to do a CSV"). No review mentions CSV *import*.
- **Strava / Apple Health:** Strava integration is requested in 4 Strong reviews ("I really wish it had Strava integration. I want my workout to upload to Strava.") and 1 Alpha review. It is praised in 1 Hevy review ("Strava connectivity").
- **Apple Watch:** the biggest pain point at Strong (sync, lost sets). It is the top request at Alpha and Dropset, which have no watch app. A reliable watch experience is a differentiator against those three.
- **Social/friends:** valued at Hevy (accountability). Requested at Strong. Fitbod family-plan users expected shared progress. No reviews here mention streaks or nudges specifically.
- **Paywall/price:** the strongest negative driver across Fitbod, Strong (3-template limit), StrengthLog ($16/mo), and Alpha (features moved behind the paywall, trial auto-charge). "Free, no ads" is a top praise point for Hevy, StrengthLog and Strong.
- **Ads:** every ads mention is praise for having none.
- **AI:** split opinion. Negative when AI changes the training (Fitbod). Some lifters explicitly praise "no AI" (Strong, StrengthLog). One Strong reviewer asks for AI *and* import. Inference: AI framed as a utility (for example "import your program from a photo") is less exposed to this backlash than AI as a coach. That is untested.
- **Ease of logging:** the most common praise theme for every app.
- **Beginners:** Fitbod and Alpha attract them through generated plans. Hevy and StrengthLog through exercise demos and free programs.
