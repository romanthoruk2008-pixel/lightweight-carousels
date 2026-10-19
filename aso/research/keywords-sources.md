# Sources and method: keyword long-list

Collected on 2026-10-19 from a Linux container through the agent HTTPS proxy. Storefront: US. Every request was a one-time snapshot. **No source gives search volume, popularity or difficulty, and none is reported.**

Directory layout under `scratchpad/aso/`:
- `kw_scripts/`: scripts and hand-curated inputs. Contains `terms.tsv` (term, intent, relevance, reason), `brands.tsv`, `top60.txt` and `tokens.txt`.
- `kw_data/`: downloaded raw data, treated as untrusted. All parsing ran with `python3 -I`.
- `keywords/`: outputs. Contains `longlist.csv`, `longlist.md` and this file.

## 1. App Store search autocomplete: WORKS
- **Endpoint that works:** `https://search.itunes.apple.com/WebObjects/MZSearchHints.woa/wa/hints?clientApplication=Software&media=software&term=<prefix>`
  - Header: `X-Apple-Store-Front: 143441-1,29` (US).
  - Returns an XML plist with up to 10 `hints[].term` strings, in order, with no scores. `&media=software` made no difference.
- **Endpoint that fails:** `https://itunes.apple.com/WebObjects/MZStoreServices.woa/wa/hints?...` returned **HTTP 404**. The amp-api endpoints were not needed and were not tried.
- **Prefixes covered:** 551 in total, in four batches. Raw files are `kw_data/hints/hints1.json` … `hints4.json`, mapping prefix to an ordered list.
  - Seed prefixes from the brief, plus feature words.
  - Letter expansion `a–z` for: `workout`, `gym`, `lifting`, `weight lifting`, `strength training`, `workout log`, `gym tracker`, `workout tracker`.
  - Social, import, watch, beginner, style and brand probes.
- **Result:** 2,242 distinct suggestions.
- **How suggestions were interpreted:**
  - A suggestion is either a query or an **app title** (e.g. "hevy – workout tracker & planner"). Titles often include a colon or dash.
  - Unknown strings return an empty list (e.g. `lifting buddy`, `drop set`, `gym spreadsheet`, `import workout`). So when Apple echoes a typed prefix back, Apple knows that term.
  - Suggestion order is used only as a relative signal. The highest-weight evidence is a term appearing in the top 3 for a **shorter** prefix.
- **Cross-check:** the other agent's `../keyword-matrix.md` used the same endpoint for 40-odd prefixes. Its observations match these where they overlap: "workout with friends" #2 for `workout w`, "gym buddy" #1 for `gym b`, and the two "lightweight" apps in brand autocomplete.

## 2. Competitor metadata
- **Data:** `https://itunes.apple.com/lookup?country=us&entity=software&id=<30 ids>` → `kw_data/lookup/lookup.json`. This has the full descriptions.
- **App list:** the 30 IDs and the **subtitles** come from the other agent's `../raw/competitors.json`. The lookup API does not return subtitles.
- **Apps:** Fitbod, LADDER, Gymverse, Strong, Liftoff, Hevy, Stronglifts, Fitness AI, JEFIT, Fitness App, SmartGym, Stronger, RepCount, Boostcamp, Lyfta, Setgraph, StrengthLog, Gymaholic, Gravitus, GymBook, Alpha Progression, Stacked, HeavySet, Liftin', Gym Log+, Liftosaur, Dropset, and three "Lightweight"-named apps.
- **Exclusion:** the three "Lightweight"-named apps are left out of the competitor counts, so counts are out of 27.
- **N-gram analysis:** 1–3-gram counts are in `kw_data/lookup/ngrams.json`.
  - Name + subtitle n-grams used by the most apps: workout (24), gym (23), tracker (20), planner (14), log (14), "workout tracker" (14), "gym workout" (11), lifting (11), "weight lifting" (9), strength (8), "strength training" (6), "gym workout tracker" (6), "workout planner" (5), "routine planner" (4), "gym log" (4).
  - Feature phrases common in descriptions: "rest timer" (9), "apple health" (15), "apple watch" (13), "progressive overload" (8), "body measurements" (7), "drop sets" (7), "exercise library" (7), "supersets" (11), "personal records" (11), "friends" (12), "notes" (12).

## 3. Google autocomplete (language signal, not App Store volume)
- **Endpoint:** `https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=<query>`. It worked.
- **Coverage:** 97 queries → `kw_data/google/google.json`. Topics: best/app-to-track phrasing, friends, Apple Watch, import/switch, notes/spreadsheet, beginners, progressive overload, streak/accountability, how-to.
- **Reddit pattern:** many suggestions end in "reddit" (e.g. "best app to track lifts reddit", "gym tracker app reddit"). People ask Reddit for tracker recommendations.

## 4. Reddit and forums: NOT REACHABLE
- `https://www.reddit.com/r/fitness/search.json` returned HTTP 403.
- The WebSearch tool refuses `reddit.com` ("domain not accessible to our user agent").
- Open-web searches only returned SEO and competitor blog posts (setgraph.app, alternativeto.net). These were not used as term sources.
- **What replaced it:** user wording came from the Google "...reddit" suggestions and from App Store reviews (section 5).

## 5. App Store reviews (light phrase mining)
- **Feed:** `https://itunes.apple.com/us/rss/customerreviews/page=<1..3>/id=<id>/sortby=mostrecent/json`
- **Apps:** Hevy (1458862350), Strong (464254577), Liftin' (1445041669), Setgraph (1209781676), Dropset (6444746146; 28 reviews), Boostcamp (1529354455).
- **Result:** 778 reviews → `kw_data/reviews/reviews.json`. Only pattern counts were used. No personal data was kept in the outputs.
- **Phrases observed:**
  - "i was using notes app before", "old pen and paper", "pen and paper guy", "google sheets i used before", "using a spreadsheet to track my workouts"
  - "made the switch over to hevy for progressive overload tracking", "you can import both hevy and strong data easily"
  - "a friend and i use it every time we workout to hold each other accountable", "community accountability"
  - "pairs perfectly with the apple watch", "watch app doesn't sync"
  - "supersets, drop sets, rest timer", "warm up sets", "gym notebook extinct", "track my progress"

## Per-term evidence fields (`longlist.csv`)
| Column | Meaning |
|---|---|
| `term`, `words`, `intent` | The term, its word count, and its intent. Intent codes are 1–9 as in `longlist.md`; `B` = brand; `1+6` = primary + secondary. |
| `relevance` | H / M / L / X, plus a one-line reason. These are my judgements against the confirmed feature list. X = irrelevant or a feature that is not available (AI coach, recovery). |
| `brand_flag` | "DO NOT USE: …" for trademarks. |
| `sources` | One or more of AS-AC, COMP-META, G-AC, REVIEWS, or INFERRED. |
| `evidence_tier` | A–D, as defined in `longlist.md`. |
| `as_exact_best_rank` | Best position at which the exact term was suggested, for any prefix. |
| `as_best_rank_shorter_prefix` | Same, but only for prefixes shorter than the term. |
| `as_exact_count` | Number of prefixes where the term was suggested exactly. |
| `as_contained` | Distinct App Store suggestions containing the term as a phrase. These are mostly app titles, so this measures crowding, not demand. |
| `comp_name_subtitle` | Out of 27 competitors: how many have the term in their name or subtitle. |
| `comp_desc` | Out of 27 competitors: how many have the term in their description. |
| `g_exact_count`, `g_contained` | Google autocomplete: exact matches, and suggestions containing the term. |
| `review_mentions` | Reviews containing the term, out of 778. |
| `evidence` | Human-readable summary, including the first prefixes and positions. |

Matching is case-insensitive on whole words, after normalising punctuation. Before using any term, re-run the scripts or check the raw files: autocomplete changes over time.

## Limitations
- Autocomplete order is not volume. AppTweak or Apple Search Ads popularity is needed to compare terms.
- Relevance ratings rely on the feature list in the brief. These items are marked M or L until confirmed:
  - **Unconfirmed features:** 1RM estimates, plate calculator, export, offline use, templates for named programs (5/3/1, nSuns, PHUL, GZCLP), scheduling, challenges.
- 'Apple Watch', 'Apple Health' and 'Strava' are placed under brand terms as a precaution. Check Apple's App Review Guidelines 2.3.7 and Apple's trademark guidelines before using any of them in the name, subtitle or keywords.
