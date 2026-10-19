# Competitor set — US App Store (English), collected 2026-10-19

**Sources**
- iTunes Lookup API (`itunes.apple.com/lookup?country=us&id=…`): name, seller, genre, rating, counts, dates, price, description.
- App Store product pages (`apps.apple.com/us/app/id<ID>`): **subtitle**, Apple Watch compatibility (the "Compatibility → Apple Watch / Requires watchOS" entry), and the "In-App Purchases" list.
- iTunes Search API: discovery of the extra competitors.

Raw data is in `raw/lookup/`, `raw/pages/`, `raw/pages_parsed.json`, `raw/competitors.csv|json` and `raw/discovery_recurrence.json`.

**Notes on the data**
- Ratings are **US-storefront** averages and counts from the lookup API. Every app is in primary genre Health & Fitness.
- "Apple Watch app = Yes" means the product page lists Apple Watch under Compatibility or a watchOS requirement. Alpha Progression, Boostcamp, HeavySet, Dropset, Stronger, RepCount and Stacked show none.
- All apps are free to download, and all except Stacked list IAPs.
- Some descriptions contain user/download claims (for example "+10 million users"). These are the developers' own claims, not verified.

## How the extra competitors were chosen
I ran 16 discovery terms through the iTunes Search API (limit 25): workout tracker, gym log, workout log, lifting tracker, weight lifting, strength training, gym tracker, workout planner, routine builder, training log, progressive overload, workout app, gym app, lift tracker, gym workout planner, workout routine. Then I counted how often each app appeared (`raw/discovery_recurrence.json`).

| App | Appearances in top 25 (of 16 terms) | of which in top 10 |
|---|---|---|
| Strong | 15 | 14 |
| Hevy | 15 | 12 |
| Fitbod | 14 | 14 |
| Gymverse | 13 | 6 |
| JEFIT | 12 | 4 |
| Stronger | 10 | 3 |
| RepCount | 8 | 7 |
| Setgraph | 8 | 4 |
| SmartGym | 8 | 3 |
| Fitness AI | 8 | 2 |
| Liftoff | 7 | 7 |
| GymBook | 7 | 2 |
| Lyfta | 7 | 1 |
| LADDER | 6 | 4 |
| Stronglifts 5x5 | 5 | 3 |
| Fitness App: Gym Workout Plan | 5 | 3 |
| Gym Log+ | 4 | 1 |
| StrengthLog | 2 | 0 |

- **Excluded** although they recur, because they are not gym/strength trackers: Home Workout – No Equipments (7), SHRED: Gym & Home Workouts (6), Workout for Women (6), Muscle Booster (5), Habit Tracker (4), Nike Training Club (3).
- **Added for product relevance despite low recurrence:** Gravitus and Liftosaur.
- Of the named set, StrengthLog (2), HeavySet, Alpha Progression, Boostcamp, Dropset, Liftin', Stacked and Gymaholic rarely or never reach the top 25 for these generic terms. They rank mostly on their own brand names.

## Title / subtitle patterns (observations)
1. **"Workout Tracker" + "Gym Log" is the leader formula.** Hevy and Strong use the *same* trailing name, "Workout Tracker Gym Log" (Hevy: "Hevy - Workout Tracker Gym Log"; Strong: "Strong Workout Tracker Gym Log"). Lyfta uses "Gym Workout Tracker Log". RepCount, Setgraph, Gravitus and Liftin' all use "Gym Workout Tracker".
2. **Subtitles almost all repeat lifting nouns.** Exact subtitles reused by several apps:
   - "Weight Lifting Routine Planner": Hevy, Liftoff, Lyfta (Liftin' uses "Weightlifting Routine Planner").
   - "Weight Lifting Strength Log": Setgraph, Gravitus.
   - "Weight Lifting & Exercise Log": Stronger, RepCount.
   - "Strength Training Planner/Tracker": Strong, HeavySet.
3. **Words are split between fields.** "weight / lifting", "log", "routine", "planner" and "program" live mainly in the **subtitle**. "workout", "tracker" and "gym" live in the **name** (see the table below).
4. **Planner apps (AI/coach)** use "Planner / Plan / Trainer / Coach / AI": Fitbod, Gymverse, Fitness AI, LADDER, Stronglifts, JEFIT.
5. **Words used by almost nobody in name or subtitle:** "logbook" (0), "program" (2 subtitles: Stronglifts, StrengthLog), "bodybuilding" (1), "Apple Watch" (1: Gymaholic's subtitle "Gym Log, Planner & Apple Watch"), "AI" (2: Fitness AI's name, Fitbod's subtitle), "beginner" (0), "friends/social" (0), "import" (0), "progress/progressive overload" (0 — only as part of the brand "Alpha Progression"), "PR/records" (0), "measurements/photos" (0), "routine" in the name (0).
6. **Brand-first vs keyword-first.** Every leader puts its brand first, then 20–25 characters of keywords. Several 30-character names look cut at the limit, for example "Stacked - Workout Tracker for" (sic).

## Word usage: App Name vs Subtitle (27 competitors, excluding the three "Lightweight" apps)
Case-insensitive whole-word match. "weight" counts "Weight Lifting". "weightlifting" is counted separately.

| Word | in Name (n=27) | in Subtitle | in either | apps (name / subtitle) |
|---|---|---|---|---|
| workout | 22 | 8 | 27 | Gymverse, Strong, Liftoff, Hevy, Stronglifts, FitnessAI, JEFIT, FitnessApp, SmartGym, Stronger, RepCount, Boostcamp, Lyfta, Setgraph, StrengthLog, Gymaholic, Gravitus, Stacked, HeavySet, Liftin', GymLog+, Liftosaur / Fitbod, LADDER, Gymverse, StrengthLog, GymBook, Alpha, Liftosaur, Dropset |
| tracker / track | 15 | 4 | 18 | Strong, Hevy, JEFIT, RepCount, Boostcamp, Lyfta, Setgraph, StrengthLog, Gymaholic, Gravitus, Alpha, Stacked, Liftin', GymLog+, Dropset / FitnessApp, GymBook, HeavySet, Dropset |
| gym | 19 | 5 | 22 | Fitbod, Gymverse, Strong, Liftoff, Hevy, FitnessAI, JEFIT, FitnessApp, SmartGym, Stronger, RepCount, Lyfta, Setgraph, Gravitus, Alpha, HeavySet, Liftin', GymLog+, Dropset / Stronglifts, SmartGym, Boostcamp, Gymaholic, Dropset |
| log (incl. logger) | 5 | 9 | 14 | Strong, Hevy, Lyfta, HeavySet, GymLog+ / JEFIT, Stronger, RepCount, Setgraph, StrengthLog, Gymaholic, Gravitus, GymBook, Alpha |
| logbook | 0 | 0 | 0 | – / – |
| lifting / lift | 0 | 11 | 11 | – / Liftoff, Hevy, SmartGym, Stronger, RepCount, Lyfta, Setgraph, Gravitus, Alpha, Stacked, GymLog+ |
| weight (incl. weight lifting) | 0 | 9 | 9 | – / Liftoff, Hevy, SmartGym, Stronger, RepCount, Lyfta, Setgraph, Gravitus, Stacked |
| weightlifting (one word) | 0 | 1 | 1 | – / Liftin' |
| strength | 2 | 6 | 8 | LADDER, GymBook / Strong, Stronglifts, Boostcamp, Setgraph, Gravitus, HeavySet |
| training | 2 | 5 | 7 | LADDER, GymBook / Strong, Stronglifts, JEFIT, Boostcamp, HeavySet |
| planner | 4 | 9 | 13 | Fitbod, Gymverse, FitnessAI, Stronger / Strong, Liftoff, Hevy, JEFIT, Lyfta, Gymaholic, GymBook, Alpha, Liftin' |
| plan / plans | 4 | 1 | 5 | LADDER, Stronglifts, JEFIT, FitnessApp / Boostcamp |
| routine | 0 | 5 | 5 | – / Liftoff, Hevy, FitnessApp, Lyfta, Liftin' |
| program(s) | 0 | 2 | 2 | – / Stronglifts, StrengthLog |
| fitness | 3 | 3 | 6 | Fitbod, FitnessAI, FitnessApp / LADDER, Gymverse, JEFIT |
| exercise | 0 | 3 | 3 | – / FitnessApp, Stronger, RepCount |
| trainer / coach | 0 | 4 | 4 | – / Fitbod, LADDER, Gymverse, FitnessAI |
| AI | 1 | 1 | 2 | FitnessAI / Fitbod |
| bodybuilding | 0 | 1 | 1 | – / Stacked |
| apple watch | 0 | 1 | 1 | – / Gymaholic |
| home | 1 | 2 | 2 | SmartGym / FitnessApp, SmartGym |

## Competitor tables

### A. Named competitor set (from the brief)
| trackId | App Name (exact) | Subtitle | Seller | Genre | ★ US | # US ratings | First release | Last update | Price | Apple Watch app |
|---|---|---|---|---|---|---|---|---|---|---|
| 1041517543 | Fitbod: Gym & Fitness Planner | AI Personal Trainer & Workouts | Fitbod Inc. | Health & Fitness | 4.81 | 287,740 | 2015-09-26 | 2026-10-14 | Free + IAP | Yes |
| 464254577 | Strong Workout Tracker Gym Log | Strength Training Planner | Strong Fitness PTE Limited | Health & Fitness | 4.86 | 108,536 | 2011-09-15 | 2026-10-08 | Free + IAP | Yes |
| 1458862350 | Hevy - Workout Tracker Gym Log | Weight Lifting Routine Planner | Hevy Studios S.L. | Health & Fitness | 4.92 | 98,819 | 2019-07-01 | 2026-10-13 | Free + IAP | Yes |
| 449810000 | JEFIT Workout Plan Gym Tracker | Training Log Fitness Planner | Jefit Inc. | Health & Fitness | 4.76 | 46,917 | 2011-07-25 | 2026-10-12 | Free + IAP | Yes |
| 1529354455 | Boostcamp: Workout Tracker | Gym & Strength Training Plans | BPM Health Co. | Health & Fitness | 4.85 | 10,611 | 2020-10-04 | 2026-10-02 | Free + IAP | No |
| 1209781676 | Setgraph: Gym Workout Tracker | Weight Lifting Strength Log | Setgraph LLC | Health & Fitness | 4.72 | 6,174 | 2017-06-20 | 2026-09-18 | Free + IAP | Yes |
| 1434229662 | StrengthLog – Workout Tracker | Workout Log & Programs | Styrkelabbet AB | Health & Fitness | 4.86 | 3,687 | 2018-11-07 | 2026-10-19 | Free + IAP | Yes |
| 648518560 | Gymaholic: Workout Tracker | Gym Log, Planner & Apple Watch | Devenyi Gabor | Health & Fitness | 4.58 | 3,466 | 2013-07-03 | 2026-10-15 | Free + IAP | Yes |
| 1462277793 | Alpha Progression Gym Tracker | Workout Planner & Lifting Log | Alpha Progression GmbH | Health & Fitness | 4.92 | 2,226 | 2019-09-23 | 2026-10-06 | Free + IAP | No |
| 1116989938 | Stacked - Workout Tracker for | Weight Lifting & Bodybuilding | M4L, Inc. | Health & Fitness | 4.56 | 1,726 | 2017-01-19 | 2022-06-07 | Free | No |
| 1171500310 | HeavySet - Gym Workout Log | Strength Training Tracker | Runloop Ltd | Health & Fitness | 4.56 | 1,274 | 2017-01-21 | 2025-08-20 | Free + IAP | No |
| 1445041669 | Liftin' - Gym Workout Tracker | Weightlifting Routine Planner | Valter Hemmi | Health & Fitness | 4.74 | 774 | 2019-05-02 | 2026-10-13 | Free + IAP | Yes |
| 6444746146 | Dropset: Gym tracker | Track your gym workouts | Fortyfour AB | Health & Fitness | 4.42 | 96 | 2023-03-31 | 2025-07-30 | Free + IAP | No |

### B. Discovered via iTunes Search API (recurring strength/gym trackers; Gravitus and Liftosaur added for relevance)
| trackId | App Name (exact) | Subtitle | Seller | Genre | ★ US | # US ratings | First release | Last update | Price | Apple Watch app |
|---|---|---|---|---|---|---|---|---|---|---|
| 1502936453 | LADDER Strength Training Plans | Fitness, Workouts, Coaching | Ladder Technologies, Inc. | Health & Fitness | 4.95 | 209,927 | 2020-06-23 | 2026-10-06 | Free + IAP | Yes |
| 1048454034 | Gymverse: Gym Workout Planner | Workout & Fitness Trainer | FITNESS22 LTD | Health & Fitness | 4.85 | 165,350 | 2015-12-18 | 2026-10-18 | Free + IAP | Yes |
| 6448081563 | Liftoff - Ranked Gym Workouts | Weight Lifting Routine Planner | Liftoff Labs Inc. | Health & Fitness | 4.83 | 99,755 | 2023-04-20 | 2026-10-18 | Free + IAP | Yes |
| 488580022 | Stronglifts 5x5 Workout Plan | Gym Strength Training Program | Stronglifts Limited | Health & Fitness | 4.86 | 76,850 | 2011-12-22 | 2026-10-16 | Free + IAP | Yes |
| 1446224156 | Fitness AI Gym Workout Planner | Personal Trainer: Muscle Coach | FitnessAI Inc. | Health & Fitness | 4.70 | 55,969 | 2018-12-20 | 2026-10-16 | Free + IAP | Yes |
| 1114387800 | Fitness App: Gym Workout Plan | Exercise tracker, home routine | FITNESS ONLINE MChJ | Health & Fitness | 4.74 | 36,641 | 2016-09-15 | 2026-10-16 | Free + IAP | Yes |
| 922744883 | SmartGym: Gym & Home Workouts | HIIT, Home, Gym Weight Lifting | SmartGym Services LLC | Health & Fitness | 4.70 | 34,497 | 2014-11-04 | 2026-10-16 | Free + IAP | Yes |
| 1621719397 | Stronger - Gym Workout Planner | Weight Lifting & Exercise Log | Atlas Smart Technologies LTD | Health & Fitness | 4.77 | 17,578 | 2022-05-30 | 2026-09-11 | Free + IAP | No |
| 594982044 | RepCount - Gym Workout Tracker | Weight Lifting & Exercise Log | Siper Apps AB | Health & Fitness | 4.85 | 13,406 | 2013-05-04 | 2026-10-15 | Free + IAP | No |
| 6443740936 | Lyfta: Gym Workout Tracker Log | Weight Lifting Routine Planner | Lindberg Development AS | Health & Fitness | 4.81 | 7,014 | 2022-10-10 | 2026-10-11 | Free + IAP | Yes |
| 965383840 | Gravitus - Gym Workout Tracker | Weight Lifting Strength Log | Gravitus, Inc. | Health & Fitness | 4.83 | 3,340 | 2015-11-14 | 2026-10-02 | Free + IAP | Yes |
| 650113307 | GymBook ・ Strength Training | Workout Planner・Logger・Tracker | Appwise GmbH | Health & Fitness | 4.79 | 2,435 | 2013-05-22 | 2026-10-11 | Free + IAP | Yes |
| 871239624 | Gym Log+ — Workout Tracker | Every Lift Logged in Seconds | Minds Aspire LLC | Health & Fitness | 4.50 | 694 | 2014-05-05 | 2026-10-18 | Free + IAP | Yes |
| 1661880849 | Liftosaur: Scriptable Workouts | Automate Your Workouts | Liftosaur, LLC | Health & Fitness | 4.85 | 423 | 2023-01-12 | 2026-10-13 | Free + IAP | Yes |

### C. Existing apps using the name "Lightweight"
| trackId | App Name (exact) | Subtitle | Seller | Genre | ★ US | # US ratings | First release | Last update | Price | Apple Watch app |
|---|---|---|---|---|---|---|---|---|---|---|
| 1580231861 | Lightweight! Workout Analysis | Science-based training | LIGHTWEIGHT LLC | Health & Fitness | 4.79 | 183 | 2021-09-15 | 2026-10-07 | Free + IAP | No |
| 6762335584 | Lightweight: Workout Tracker | Progressive overload, tracked. | Cem Kagan Kayili | Health & Fitness | 5.00 | 1 | 2026-04-24 | 2026-04-25 | Free + IAP | No |
| 6786713713 | LW: Gym Workout Tracker & Log | Lightweight Lifting Planner | Lightweight Fitness Ltd | Health & Fitness | 0.00 | 0 | 2026-09-14 | 2026-10-16 | Free + IAP | No |

### IAP price points shown on the US App Store page ("Top In-App Purchases", first 4 unique)
| App | IAP items |
|---|---|
| Fitbod: Gym & Fitness Planner | Monthly Plan $12.99; (Legacy Pricing) fitbod ELITE $9.99; Monthly Plan $15.99; (Legacy Pricing) fitbod ELITE $59.99 |
| LADDER Strength Training Plans | PRO $29.99; PRO Annual $179.99; PRO+ $34.99; ELITE $44.99 |
| Gymverse: Gym Workout Planner | Workout Premium $59.99; Workout Premium $69.99; Premium Upgrade $19.99; Premium Upgrade $59.99 |
| Strong Workout Tracker Gym Log | Strong PRO (1 Month) $4.99; Strong PRO (1 Year) $29.99; Strong PRO Forever $99.99; Strong PRO (6 Months) $19.99 |
| Liftoff - Ranked Gym Workouts | Liftoff Pro $79.99; Liftoff Pro $12.99; Liftoff Pro $39.99; Liftoff Pro $3.99 |
| Hevy - Workout Tracker Gym Log | Hevy Pro - Monthly $2.99; Hevy Pro - Yearly $23.99; Hevy Pro - Lifetime $74.99; Hevy Pro - Monthly $3.99 |
| Stronglifts 5x5 Workout Plan | Pro Yearly $59.99; Pro Monthly $11.99; Pro Quarterly $29.99; Pro Weekly $4.99 |
| Fitness AI Gym Workout Planner | FitnessAI - Annual Member $89.99; Weekly Membership $3.99; Annual Membership 3 $89.99; Monthly product $19.99 |
| JEFIT Workout Plan Gym Tracker | (Legacy Pricing) Elite $6.99; Elite Monthly Subscription $12.99; (Legacy Pricing) Elite $39.99; Elite Yearly (50% off) $69.99 |
| Fitness App: Gym Workout Plan | Full unlimited access /monthly $6.99; Full unlimited access /annual $59.99 |
| SmartGym: Gym & Home Workouts | SmartGym Premium+ Yearly $59.99; SmartGym Premium+ Monthly $9.99; SG Premium $39.99; User Account Monthly $6.99 |
| Stronger - Gym Workout Planner | Stronger PRO Annual $39.99; Stronger PRO $12.99; Stronger PRO Monthly $9.99; STRONGER PRO ANNUAL $69.99 |
| RepCount - Gym Workout Tracker | RepCount Premium $4.99; RepCount Premium $29.99; RepCount Premium $6.99; RepCount Premium $39.99 |
| Boostcamp: Workout Tracker | Boostcamp Pro $59.99; Boostcamp Pro $14.99; Boostcamp Pro $11.99; Boostcamp Pro $79.99 |
| Lyfta: Gym Workout Tracker Log | Lyfta Premium $59.99; Lyfta Premium $49.99; Lyfta Premium $29.99; Lyfta Premium $79.99 |
| Setgraph: Gym Workout Tracker | Pro Membership $29.99; Pro Membership (Monthly) $4.99; Lifetime Pro Membership $199.99 |
| StrengthLog – Workout Tracker | StrengthLog Premium - 1 month $16.90; StrengthLog Premium - 3 months $37.90; StrengthLog Premium - 1 year $109.00 |
| Gymaholic: Workout Tracker | Monthly $3.99; Yearly $31.99; Pro version $4.99; Pro Gold version $14.99 |
| Gravitus - Gym Workout Tracker | Gravitus Pro $7.99; Gravitus Pro $12.99; Gravitus Pro $11.49; Gravitus Pro $59.99 |
| GymBook ・ Strength Training | Platinum ・ Package $17.99; +Exercises ・ Feature $5.99; GymBook Pro · Lifetime $22.99; GymBook Pro · Monthly $1.99 |
| Alpha Progression Gym Tracker | Yearly plan for best results $79.99; Monthly plan for best results $12.99; Monthly plan [Legacy] $24.99 |
| Stacked - Workout Tracker for | – |
| HeavySet - Gym Workout Log | Lifetime Intermediate $19.99 |
| Liftin' - Gym Workout Tracker | Liftin' Unlimited Monthly $2.99; Liftin' Unlimited Yearly $24.99; Liftin' Unlimited Lifetime $99.99 |
| Gym Log+ — Workout Tracker | Upgrade $79.99; Pro Yearly $29.99; Pro Monthly $4.99; Pro Lifetime $79.99 |
| Liftosaur: Scriptable Workouts | Monthly Subscription $4.99; Yearly Subscription $39.99; Lifetime Subscription $99.99 |
| Lightweight! Workout Analysis | Lightweight Pro - Annual $14.99; Lightweight Pro - Monthly $2.99; Lightweight Pro - Annual Discounted $5.99 |
| Dropset: Gym tracker | Monthly plan $4.99; Yearly plan $39.99; Lifetime $99.00 |
| Lightweight: Workout Tracker | Premium Monthly $5.99; Premium Yearly $53.99 |
| LW: Gym Workout Tracker & Log | Lightweight Pro $17.99; Lightweight Pro $1.99 |

### Description — first ~300 characters (verbatim, from iTunes lookup)

- **Fitbod: Gym & Fitness Planner** (1041517543): "*Apple Editor’s Choice Award Winner*   Build muscle, gain strength and lose weight with a customized workout plan just for you. Fitbod is the ultimate fitness platform made to help enhance your strength training and endurance through personalized AI workouts. You won’t just get stronger—you’ll do it…"
- **LADDER Strength Training Plans** (1502936453): "Try Ladder COMPLETELY FREE for 7 days. NO PAYMENT collected during trial.  LADDER IS THE #1 APP FOR STRENGTH TRAINING Apple's 2025 App of the Year Finalist Apple's Editors Choice Award Women's Health 2026 Best Overall CNET 2026 Best Strength Training App  Ladder gives you a structured, coach-built w…"
- **Gymverse: Gym Workout Planner** (1048454034): "Gymverse acts as your personal trainer, building a fully managed, multi-week training plan tailored to your goals, schedule, and equipment. Set your goals, track every milestone, and celebrate every personal record along the way, Gymverse highlights your personal bests, total weight lifted, and stre…"
- **Strong Workout Tracker Gym Log** (464254577): "The most intuitive workout and exercise tracker for any fitness routine.  Strong is the simplest and most intuitive workout tracker, designed to help you get better results from your workouts. Whether you want to gain strength or just stay healthy, join over 1.2 million people who have downloaded St…"
- **Liftoff - Ranked Gym Workouts** (6448081563): "Liftoff is the best workout tracker app that ranks your gym performance. Get feedback on 600+ exercises, track progress, and compete with friends. Download the #1 gym rank app & join over 4 million lifters today!  Gamified Workout Tracker | Ranks | Streaks | Accountability | Logger  Boost Your Fitne…"
- **Hevy - Workout Tracker Gym Log** (1458862350): "** Featured by Apple ** Join +10 million users! Hevy is the most intuitive workout tracker & planner in the world. No ads and free. Plan your weight lifting routines, log your workouts and track your exercise progress. Join a growing community and get started today - for free!  WHAT USERS ARE SAYING…"
- **Stronglifts 5x5 Workout Plan** (488580022): "Get stronger with the world’s simplest, most proven barbell program: the 5×5 workout. No guesswork. Just follow along and see real results, in just 3 workouts a week.  StrongLifts is made for lifters starting or returning to barbell strength training. The app removes all confusion and complexity by…"
- **Fitness AI Gym Workout Planner** (1446224156): "Workout at home or at the gym with FitnessAI’s advanced training algorithm to guide you through the perfect set, rep and weight combination to reach your fitness goals.   ● Get results with whatever equipment you have available to you. Whether your fitness goals are to build muscle, get toned or los…"
- **JEFIT Workout Plan Gym Tracker** (449810000): "Get Fit and Strong with JEFIT: Your Reliable Gym Planner and Workout Tracker  JEFIT is the ultimate workout tracker to plan your strength training, log workouts, and track exercise progress. Whether you want a simple gym log to track your weights and reps, or a smart, AI-guided routine that tells yo…"
- **Fitness App: Gym Workout Plan** (1114387800): "Whether you are trying to lose weight, gain muscle mass, rounder buttocks or want to get 6-pack abs – our fitness app offers full body workout plans with many 3D workout exercises for free. Here you will find ready workouts with champions’ diets. You can choose from a variety of exercise plans for m…"
- **SmartGym: Gym & Home Workouts** (922744883): "Achieve your goals faster than ever.  • Apple's Apple Watch App of the Year • Apple Design Awards Finalist • #1 Health & Fitness app in over 30 countries  FORBES: "Best Apple Watch Apps for Health and Fitness"  Looking for an app to help you work out? SmartGym offers a beautiful, elegant and easy wa…"
- **Stronger - Gym Workout Planner** (1621719397): "Built for lifters who take their training seriously.  Trusted by over 1 million athletes worldwide, Stronger is the simple and intuitive workout planner to help you crush your fitness goals. Track your workouts, receive AI coaching, and compete with your friends. Whether you want to build strength,…"
- **RepCount - Gym Workout Tracker** (594982044): "To maximize your results in the gym you need to track your workouts. There is a saying that "what you don't measure, you can't improve". Don't worry, RepCount got you covered. It is a quick and simple workout log for strength training. RepCount won't lift the weights for you, but it makes tracking a…"
- **Boostcamp: Workout Tracker** (1529354455): "Trusted by over 1,300,000 lifters. 300M+ workouts logged. 4.8 stars.  Boostcamp is a free workout tracker and gym logger with 11,000+ programs and an AI coach that builds a custom plan from your goal, schedule, and equipment. Log every set. Run nSuns, GZCLP, 5/3/1, Reddit PPL, PHUL, PHAT, or 130+ co…"
- **Lyfta: Gym Workout Tracker Log** (6443740936): "Join over 7 million gym and fitness enthusiasts and lift more with Lyfta – the free workout tracker, gym log, and strength training planner.  Log your workouts, build routines, and track progress so you can focus on what matters most: getting stronger.  What Our Users Are Saying:  • "I've tried prob…"
- **Setgraph: Gym Workout Tracker** (1209781676): "Setgraph is the fast, no-fuss way to track your lifts and actually achieve progressive overload. Log a set in seconds, then watch your strength climb on clear, real-time graphs. Built for lifters of all levels, it stays simple and quick, so logging never gets in the way of training.  Features  Fast…"
- **StrengthLog – Workout Tracker** (1434229662): "** The world’s most generous workout tracker – built by lifters, for lifters **  Tired of downloading gym apps and creating an account, just to be locked out in a matter of days if you don’t pay or watch endless commercials?  We offer 100% gains and 0% ads – with unlimited workout logging and free s…"
- **Gymaholic: Workout Tracker** (648518560): "Log every set from your Apple Watch. No phone, no fumbling.  Build muscle, gain strength, and track every workout. Log every rep, every plate, and every personal record across 850+ exercises with interactive 3D animations. Used by serious lifters for over a decade.  APPLE WATCH — YOUR WRIST IS ENOUG…"
- **Gravitus - Gym Workout Tracker** (965383840): "Gravitus is the ultimate workout tracker & planner for the gym. Lift without ads for free. Elevate your weight lifting with advanced routines, a thriving community and the largest exercise database in the world! Track, log, and train like a pro with Gravitus.   WHAT USERS ARE SAYING • “Probably the…"
- **GymBook ・ Strength Training** (650113307): "Here is GymBook, your fitness app to efficiently create, log and analyze your workouts at the gym - all in a beautiful and minimalist user interface.  MANAGE YOUR WORKOUTS • Create your workout with your own exercises or choose from the 50+ simple exercises with animated images and visualizations of…"
- **Alpha Progression Gym Tracker** (1462277793): "Stop guessing. Pro builds your plan and recommends weight and reps for every set, adapting to how strong you are today. Free logging, no account. 14-day free trial.  Alpha Progression tells you exactly what to lift. Every set, every workout. Build your plan in a minute, then follow weight and rep re…"
- **Stacked - Workout Tracker for** (1116989938): "FINALLY! A 100% FREE WEIGHTLIFTING APP ACTUALLY WORTH USING!  Whether you’re a beginner or an experienced weightlifter, Stacked will help you gain muscle and strength faster.  With it, you can easily and effectively plan and track your weightlifting workouts and fitness goals.  And unlike most other…"
- **HeavySet - Gym Workout Log** (1171500310): "HeavySet is a gym log / workout tracker for weightlifting, bodybuilding and strength training. It has a simple interface which makes tracking workouts easy and efficient.   HEAVYSET AT A GLANCE:  ROUTINES:  - Supersets / Giant sets - Preset rest timers per exercise - Rep ranges - Set ranges - AMRAP…"
- **Liftin' - Gym Workout Tracker** (1445041669): "Liftin' is the gym tracker for people who lift. Log a set with one tap, let your weights progress automatically, and build the program you want with AI, on iPhone, iPad, Mac and Apple Watch.  TRACK WITH ONE TAP • A clean workout screen that puts your next set front and center. Log it, let the rest t…"
- **Gym Log+ — Workout Tracker** (871239624): "Gym Log+ is the fast, private workout tracker — logging lifting sets in seconds since 2013, now rebuilt from the ground up for modern iPhone and Apple Watch.  I built Gym Log+ in 2013 because I wanted a faster way to log my workouts. I rebuilt it in 2026 for the same reason.  ALREADY A GYM LOG+ USER…"
- **Liftosaur: Scriptable Workouts** (1661880849): "Liftosaur is the most customizable weightlifting app and strength training tracker and planner.  # Automate Your Strength Training  Build your own progressive overload programs or start with proven routines like GZCLP, 5/3/1, or Basic Beginner Routine. Track every workout, visualize your progress, a…"
- **Lightweight! Workout Analysis** (1580231861): "DON’T JUST TRACK YOUR TRAINING. SEE WHICH MUSCLES ARE ACTUALLY DOING THE WORK!  Lightweight! is a science-based workout tracking and analysis app built for fitness, bodybuilding, strength training, powerlifting, and anyone who wants to understand their training at a deeper level. • Discover effectiv…"
- **Dropset: Gym tracker** (6444746146): "Dropset is a clean and minimal tool for tracking your gym workouts, designed to be as non distracting as possible. You won’t find annoying upsells, or unnecessary options. There's simply what you need to set up your workout routine and your exercises and then track them at the gym. Also, it's super…"
- **Lightweight: Workout Tracker** (6762335584): "Lightweight is a workout tracker for lifters who actually train. No social feed, no cookie-cutter programs, no bloat. Just fast logging, clean data, and the insights that matter for progressive overload.  BUILT FOR THE SESSION • Log sets in seconds with a keypad designed for the gym floor • Previous…"
- **LW: Gym Workout Tracker & Log** (6786713713): "Find serious gyms anywhere, log your lifts and build a passport of everywhere you’ve trained.  Lightweight combines a fast workout logger with a gym directory built for lifters. Track routines, previous values, rest times and PRs; discover gyms by prices, equipment, access and day-pass availability;…"

## Per-app notes (positioning as observed; claims are the developers')
- **Hevy:** "Workout Tracker Gym Log" + "Weight Lifting Routine Planner". The description leads with "No ads and free", "Join +10 million users" and community. Pro is the cheapest of the leaders ($2.99–3.99/mo, $23.99/yr, $74.99 lifetime). Has a Watch app. 16 languages.
- **Strong:** the oldest (2011). Same "Workout Tracker Gym Log" name pattern; subtitle "Strength Training Planner". Pro $4.99/mo, $29.99/yr, $99.99 forever: the same price points as the planned Lightweight pricing. Has a Watch app.
- **Fitbod:** "Gym & Fitness Planner" + "AI Personal Trainer & Workouts". The description leads with the Apple Editor's Choice award and "personalized AI workouts". The most expensive of the trackers ($12.99–15.99/mo).
- **JEFIT:** "Workout Plan Gym Tracker" + "Training Log Fitness Planner". The description mixes "simple gym log" with "AI-guided routine".
- **Boostcamp:** "Workout Tracker" + "Gym & Strength Training Plans". Program-library positioning ("11,000+ programs", named Reddit programs). No Watch app.
- **Setgraph:** "Gym Workout Tracker" + "Weight Lifting Strength Log". Speed and progressive overload ("Log a set in seconds").
- **StrengthLog:** "Workout Tracker" + "Workout Log & Programs". "world's most generous workout tracker", "0% ads". Premium is expensive ($16.90/mo, $109/yr).
- **Gymaholic:** the only app that puts **Apple Watch** in its subtitle ("Gym Log, Planner & Apple Watch"), and its description opens "Log every set from your Apple Watch." The page lists "Requires iOS 27.0", as observed.
- **Alpha Progression:** brand + "Gym Tracker" + "Workout Planner & Lifting Log". Auto-progression ("Stop guessing… recommends weight and reps"). No Watch app (reviews ask for one).
- **Stacked:** last updated 2022-06-07 (stale). The name is cut at 30 characters.
- **HeavySet:** last updated 2025-08-20. Only a $19.99 lifetime IAP. No Watch app listed.
- **Liftin':** "Gym Workout Tracker" + "Weightlifting Routine Planner". The description mentions "build the program you want with AI" and Apple Watch.
- **Dropset:** "Gym tracker" + "Track your gym workouts". Minimal, "no annoying upsells". No Watch app. Last updated 2025-07-30. Only 96 US ratings.
- **Discovered high-rating-count apps:**
  - LADDER (209,927; coach-led plans, expensive)
  - Gymverse (165,350; "personal trainer", multi-week plans)
  - Liftoff (99,755; "Ranked Gym Workouts". The description: "compete with friends", "Ranks | Streaks | Accountability". The closest social/gamified competitor in the top results)
  - Stronglifts 5x5 (76,850; one program)
  - Fitness AI (55,969)
  - Stronger (17,578; "AI coaching, and compete with your friends")
  - RepCount (13,406; "quick and simple workout log")
- **Smaller, Watch-centric or speed-centric:** Gym Log+ ("Every Lift Logged in Seconds"), GymBook, Gravitus (ad-free + community), Liftosaur (scriptable programs).

## The three existing "Lightweight" apps
| | Lightweight! Workout Analysis | Lightweight: Workout Tracker | LW: Gym Workout Tracker & Log |
|---|---|---|---|
| trackId | 1580231861 | 6762335584 | 6786713713 |
| Seller | LIGHTWEIGHT LLC | Cem Kagan Kayili | Lightweight Fitness Ltd |
| Subtitle | Science-based training | Progressive overload, tracked. | Lightweight Lifting Planner |
| Released / updated | 2021-09-15 / 2026-10-07 | 2026-04-24 / 2026-04-25 | 2026-09-14 / 2026-10-16 |
| US ratings | 183 (4.79★) | 1 (5★) | 0 |
| IAP | Pro $2.99/mo, $14.99/yr | Premium $5.99/mo, $53.99/yr | Lightweight Pro $1.99 / $17.99 |
| Watch | No | No | No |
| Positioning | Muscle heatmaps / training analysis, "500K+ athletes" (claim on screenshot) | Plain lifting tracker for "lifters who actually train. **No social feed**…" | Workout logger + **gym directory** ("Find serious gyms anywhere… passport") |

- On App Store web search for **"lightweight"** they rank #1 (Workout Analysis), #2 (Workout Tracker) and #5 (LW). For "lightweight workout" the first two rank #1–2, and for "lightweight gym" Workout Analysis and LW rank #1–2 (see keyword-matrix.md).
- The autocomplete for "lightweight" already suggests "lightweight! workout analysis" and "lightweight: workout tracker" (see keyword-matrix.md).
- **Inference / risk:**
  - 6762335584 has almost the same name ("Lightweight: Workout Tracker") and the same category of product (a lifting tracker) as the planned app, and its seller is an individual.
  - 6786713713's seller is literally "Lightweight Fitness Ltd" and uses "Lightweight" in its subtitle.
  - An exact App Name "Lightweight: Workout Tracker" is already taken. App Store names must be unique, so the planned app will need a different full name string, such as a different suffix.
  - Brand-search traffic for "lightweight" will be shared with three apps plus unrelated "lightweight browser/text editor" results.
  - Trademark questions are outside this research.
