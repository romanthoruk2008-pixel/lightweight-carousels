# App Store name, subtitle and keywords — the picks

Measured 2026-10-22 with Sonar (`/keywords/metrics`, iOS) in four stores: US 273 terms, UK 253,
Germany 118, France 101. Every number below is reproduced by `python3 -I Tools/ASO/listings.py`;
the rows are in [`../research/keywords.csv`](../research/keywords.csv).

**How to read the numbers.** `53/74` is popularity/difficulty. Popularity is Apple's own reading
only from 38 up: below 38 Apple reports "5", and Sonar's estimate (at most 37) stands in. That
covers most terms: only 28 of the 273 US terms have a real Apple reading. Difficulty is Sonar's
0–100 score. "Target" means popularity ≥ 20 and difficulty ≤ 40.

**How an option is scored.** A search term counts as covered when all its words are in the same
locale's name, subtitle and keyword field (Apple joins words across those three, within one
locale only). Each covered term is worth popularity × (1 − difficulty/100), halved or cut to 0.3
for terms that only partly describe Harda (see `Tools/ASO/keyword_picker.py`). "Name + subtitle"
counts the terms formed from those two fields alone, which carry the most weight. The keyword
fields were filled greedily; a swap pass found at most 3% more, so they are close to the best
this model can do.

## Paste this

| Locale | Searched in | Name (30) | Subtitle (30) | Keywords (100) |
|---|---|---|---|---|
| English (U.S.) | US | `Harda: Gym Workout Tracker` | `Strength Training Log & Plans` | `ai,1rm,5x5,fitness,531,lifting,planner,weight,coach,program,gains,streak,gymbro,lift,social,routine` |
| Spanish (Mexico) | US, Mexico | `Harda: Weightlifting Journal` | `Powerlifting & Bodybuilding` | `workout,gym,superset,barbell,lifter,split,muscle,friends,hypertrophy,timer,stats,diary,buddy,build` |
| English (U.K.) | UK, Australia, and 11 European stores including Germany and France | `Harda: Gym Workout Planner` | `Training Log, Tracker & Split` | `ai,plan,fitness,531,5x5,lifting,weight,strength,coach,gains,gymbro,routine,barbell,streak,program,pr` |
| German | Germany | `Harda: Trainingsplan & Tracker` | `Krafttraining & Muskelaufbau` | `1rm,ki,gym,powerlifting,pausentimer,plan,körpermaße,trainingspartner,fitnessstudio,anfänger,coach` |
| French | France | `Harda: Musculation & Programme` | `Carnet, Séries & Progression` | `ia,sport,1rm,coach,barre,entrainement,suivi,mensurations,salle,bodybuilding,haltères,poids,plan` |

No word repeats within a locale. No plurals of a word already used, no "app", no "iphone", no
competitor, no "harda" in keywords.

## Where the brief and the data disagree

- **English (U.K.) is not searched in the US.** Apple's localization table gives the US store
  English (U.S.) plus Spanish (Mexico), Arabic, Chinese (both), French, Korean, Portuguese (Brazil),
  Russian and Vietnamese ([table](../2026-10-20-aso-rules-research.md#3-extra-languages-searched-in-each-country)).
  The extra US slot is therefore Spanish (Mexico): +160 characters at most (30 + 30 + 100), not
  +200. English (U.K.) is the UK's own listing, and the UK reads nothing else, so once it exists
  the UK stops seeing the U.S. listing. It is also the main listing in Poland, Czechia, Türkiye and
  Ukraine until those get their own.
- **A third English slot for the US** (Korean, Vietnamese, Arabic or Chinese, none of which Harda
  ships) would add about 20 terms, popularity 272 and one target. That isn't worth a listing that
  shows English to those stores before launch. Apple says those languages are searched in the US,
  but no test has confirmed it.
- **Spanish (Mexico) repeats "gym" and "workout".** Words join into phrases only inside one locale, so
  the Mexico listing needs its own glue words to form "workout journal" or "gym timer". Everything
  else in it is new.

## US: English (U.S.) + Spanish (Mexico)

| Option | Subtitle | Terms | Popularity | Targets | Name + subtitle |
|---|---|---|---|---|---|
| **A, the pick** | Strength Training Log & Plans | 99 | 2,294 | 8 | 30 terms, 814 |
| B | Weightlifting Log & Planner | 93 | 2,201 | 7 | 21 terms, 677 |
| C | Lifting Log, AI Plans, Streaks | 99 | 2,294 | 8 | 32 terms, 796 |

All three keep the name already in App Store Connect, and the data backs it. "Gym Workout Tracker"
forms the three strongest relevant head terms Apple measures: workout tracker 53/74, gym workout
48/77 and gym tracker 44/72. All are hard, as head terms are. Keyword fields per option are in
`listings.py`.

- **Why A:** it ties C on total coverage and wins on what the two heaviest fields form: strength
  33/44, training log 21/61, strength training 20/74, workout plan 19/76. "Planner" in keywords
  still forms workout planner 49/75.
- **C sells the wedge** (AI, streaks) and reads as different from Hevy's "Weight Lifting Routine
  Planner". It is the pick if conversion matters more than rank. It forms the same 99 terms, but it
  moves small ones into the subtitle (gym streak 18/69, ai workout plan 11/37) and sends strength
  33/44 and training log 21/61 down to the keyword field.
- **B** gets weightlifting 34/53 into the subtitle but forms 9 fewer title terms. Weightlifting goes
  into the Spanish (Mexico) name instead.
- **Target terms in A:** 1rm 29/13, 531 30/25, gains 28/18, program 28/20, gymbro 27/17, strength
  coach 25/29, fitness streak 25/37, social workout 20/32. Below the bar but in: 5x5 35/41,
  workout log 25/55.

| Spanish (Mexico) option | Name / subtitle | New terms | Popularity | Targets | Name + subtitle |
|---|---|---|---|---|---|
| **A, the pick** | Weightlifting Journal / Powerlifting & Bodybuilding | 28 | 581 | 5 | 4 terms, 157 |
| B | Gym Journal & Split / Powerlifting & Bodybuilding | 29 | 587 | 6 | 6 terms, 184 |
| C | Workout Journal & Timer / Weightlifting & Powerlifting | 28 | 581 | 5 | 5 terms, 166 |

Only terms English (U.S.) misses are counted. A puts weightlifting 34/53, the biggest US term the
U.S. listing had no room for, in a name. Its subtitle forms powerlifting 31/32 and bodybuilding
32/49, and its keywords add hypertrophy 30/25, superset 27/7, lifter 25/39, barbell 22/19, workout
journal 24/55 and gym timer 20/64. B forms one more target (dumbbell 31/36) but drops
weightlifting. Anyone
shown the Spanish (Mexico) listing, including Mexico's store, sees it in English.

## UK: English (U.K.)

| Option | Name / subtitle | Terms | Popularity | Targets | Name + subtitle |
|---|---|---|---|---|---|
| **A, the pick** | Gym Workout Planner / Training Log, Tracker & Split | 99 | 1,663 | 11 | 24 terms, 661 |
| B | Gym Workout Tracker / Training Log, Routine & Split | 99 | 1,663 | 11 | 23 terms, 551 |
| C | the U.S. listing as is | 101 | 1,667 | 9 | 30 terms, 631 |

- The same head terms are about 20 points easier in the UK: gym tracker 49/52, workout tracker
  48/54, and gym workout planner 49/56, which Apple measures there. A puts that last phrase in the
  name whole and still forms both trackers from name + subtitle.
- Training 38/39 and routine 39/40 are Apple-measured and meet the target bar, and split 37/24
  meets it on Sonar's estimate. Weightlifting, the US's best mid-size term, is weak here (16/66).
- **Left out for room** (all on the UK bench below): superset 26/5, hypertrophy 29/16,
  bodybuilding 30/33, rep counter 22/31. British "programme" phrases (gym programme, training
  programme) are 6–7 each and not worth the space.

## Germany: German + English (U.K.)

English (U.K.) is searched in Germany too, and the pick above already covers 31 terms there: gym
tracker 49/44, workout tracker 39/49, 5x5 30/30, 531 29/23. The German listing only counts what
English misses.

| Option | Name / subtitle | New terms | Popularity | Targets | Name + subtitle |
|---|---|---|---|---|---|
| **A, the pick** | Trainingsplan & Tracker / Krafttraining & Muskelaufbau | 24 | 378 | 4 | 7 terms, 161 |
| B | Krafttraining Tagebuch / Trainingsplan & Muskelaufbau | 23 | 382 | 4 | 6 terms, 155 |
| C | Gym Trainingstagebuch / Trainingsplan & Krafttraining | 20 | 395 | 4 | 6 terms, 153 |

- A puts the biggest German term in the name: trainingsplan 52/60. Its subtitle forms
  krafttraining 37/56 and muskelaufbau 37/57, and its keywords hold the targets powerlifting 32/28,
  1rm 26/5, trainingspartner 25/14 and pausentimer 23/11. Körpermaße 15/12 is the Measures screen.
- Apple doesn't split German compounds, so "Tagebuch" never forms trainingstagebuch 36/49. Only C
  holds the whole word, at the cost of four terms.
- The keyword field is 97 characters and **100 bytes**: ä, ö and ß take two bytes each.

## France: French + English (U.K.)

English (U.K.) covers 19 French-store terms, including split 42/45 and 5x5 30/37.

| Option | Name / subtitle | New terms | Popularity | Targets | Name + subtitle |
|---|---|---|---|---|---|
| **A, the pick** | Musculation & Programme / Carnet, Séries & Progression | 32 | 535 | 4 | 6 terms, 157 |
| B | Carnet de Musculation / Programme, Suivi & Progression | 32 | 535 | 4 | 6 terms, 134 |
| C | Suivi Musculation & Gym / Carnet, Séries & Progression | 31 | 525 | 4 | 6 terms, 148 |

- Musculation 53/57 is France's term. A and B form the same terms; A puts programme musculation
  17/60 in the name. Its subtitle holds séries 31/52 and progression 28/17, and its keywords hold
  barre 30/28, haltères 29/26, mensurations 22/12 (Measures), bodybuilding 35/48 and entrainement
  37/56.
- "entrainement" goes in without its accent: people type it that way (37 against 17 for
  "entraînement"). Whether Apple folds accents is not documented.

## Why the UK, Germany and France

They are the largest App Store markets among Harda's languages by consumer spending, going by
industry reports rather than anything measured here: the UK and Germany first, then France. Brazil
is bigger in downloads and smaller in spending. English (U.K.) also reaches Australia. Sonar's
popularity is relative within each store, so it cannot rank countries against each other.

## Left out on purpose

- **Competitors**, research only (Guideline 2.3.7): hevy 61/67, ladder 57/53, fitbod 55/79, liftoff
  53/58, lyfta 52/72, boostcamp 51/68, jefit 45/78, alpha progression 41/68. "hevy alternative" is
  5/14 and "strong alternative" 27/48.
- **Seryozha's words:** "dinosaur" 50/74 is searched for kids' games, and trex is 33/61. The search
  that matches his "Gym Bro" card is gymbro 27/17, and it is in.
- **Apple Watch:** "apple" is Apple's mark, and "watch" alone forms too little (watch workout 10/64).
  The Watch app belongs in the description and screenshots.
- **Terms that don't describe Harda:** one-audience phrases (for women, for men), calisthenics
  47/65, cardio, kettlebell 32/22, "free".
- **531** is Jim Wendler's program name, 5/3/1. Other listings use it. If App Review objects, swap
  it for hypertrophy in the UK and superset in the US.

## Before submitting

1. **Get a native speaker to check the German and French lines.** The founders' rule covers every
   language before the App Store, and these lines were written by an agent.
2. **Paste each keyword field into App Store Connect and read its counter.** Apple's reference says
   100 bytes and its guide says 100 characters; German is exactly 100 bytes.
3. **Create the four new localizations** (only English (U.S.) exists today). Each needs its own
   description; screenshots fall back to English when none are added.

## After launch: every 2–4 weeks

- **Check ranks:** `python3 -I Tools/ASO/rank_check.py --country us` (then gb, de, fr). It needs
  no key.
  - It writes `docs/aso/research/rankings/<date>-<country>.csv` and prints each keyword-field
    word's best rank.
  - It uses Apple's public search API, which ranks close to the App Store but not exactly, so
    compare runs with each other.
  - Sonar's own rank tracking (`/apps/{id}/rankings`) needs a paid Indie or Agency plan; this key
    is on the 150-calls-a-day tier.
- **Re-measure popularity** with `Tools/ASO/sonar_metrics.py` and re-score with `listings.py`. The
  skill `tracking-aso-keywords` has the steps.
- **Rule:** a keyword-field word that forms no term in the top 50 after four weeks is replaced by
  the next word on its store's bench. Name, subtitle and keywords all change only with a new app
  version, so batch the swaps into releases, and give the name and subtitle at least two cycles.
- **Bench, in order:**
  - US: dumbbell, rep counter, one rep max, leg day, push pull, exercise library.
  - UK: superset, lifter, hypertrophy, 1rm, bodybuilding, rep counter.
  - Germany: trainingstagebuch, langhantel, satzpause, hantel, bodybuilding, fortschritt.
  - France: weightlifting, force, prise de masse, hypertrophie, full body.
