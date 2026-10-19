# "Lightweight" app name: risk and ASO check

Date checked: 2026-10-19. Prepared for Xata Labs / Xata Agency. Product: "Lightweight", a native iPhone + Apple Watch strength-training tracker. US App Store launch first. Placeholder name in App Store Connect: "Lightweight Gym Tracker".

> **Not legal advice.** This is desk research from public registries and the App Store. It is not a trademark clearance opinion. Before you commit to a name, a US trademark attorney should run a full clearance search, including phonetic, design and common-law checks.

## Короткий підсумок для власника (UA)

- **Ризик: ВИСОКИЙ.** У USPTO є **чинна реєстрація LIGHTWEIGHT!**: Reg. No. 8430632, serial 99490250, зареєстрована 2026-09-15. Власник: Lightweight LLC (Delaware). Класи 9 і 41 охоплюють саме мобільний застосунок для тренувань і фітнес-трекінгу. Цей самий власник має застосунок "Lightweight! Workout Analysis", який з 2021 року стоїть на **#1** за запитом "lightweight" у всіх 8 перевірених країнах.
- Додаткове слово в назві ("Lightweight Lifts", "Lightweight by Xata" тощо) зменшує плутанину в App Store. Юридичний конфлікт воно **не прибирає**: головне слово й ті самі товари залишаються.
- Apple дозволяє власнику торговельної марки подати claim на назву застосунку. Після запуску це може призвести до примусового перейменування і втрати накопиченого ASO.
- Шанс стати #1 за запитом "lightweight" у найближчій перспективі низький.
- Рекомендація: спершу отримати висновок юриста. Якщо він негативний, перейти на fallback-бренд (Featherlift / Platelight / Lightrep), а "light weight, baby" залишити як tagline або в контенті, а не як назву.

---

## 1. App Store: apps with "lightweight" / "light weight" in the name

Method: iTunes Search API, `https://itunes.apple.com/search?entity=software&limit=50&country=<cc>&term=<query>`. Storefronts: us, gb, ca, au, de, pl, ua, es. Queries: "lightweight", "lightweight app", "lightweight workout", "lightweight gym", "lightweight tracker", "light weight". That makes 48 requests. Some got rate-limited with 403 and were retried until all 48 returned 200. Rating counts and metadata come from the US lookup API (`https://itunes.apple.com/lookup?country=us&id=...`) unless noted otherwise.

**Caveat:** the iTunes Search API only approximates real App Store search. It ignores personalization, Search Ads and Apple's behavioral signals. Treat its ranks as indicative, not as the true on-device ranking.

### 1a. Fitness or gym apps (direct competitors)

| App (US name) | Seller | Genre | US ratings (avg) | Ratings elsewhere | Released | Last update | Website | App ID / URL |
|---|---|---|---|---|---|---|---|---|
| **Lightweight! Workout Analysis** | LIGHTWEIGHT LLC | Health & Fitness | **183 (4.79)** | DE 255, GB 59, CA 40, PL 22, AU 11, UA 4, ES 3 | 2021-09-15 | 2026-10-07 (v5.0.0) | lightweightapp.com | [1580231861](https://apps.apple.com/us/app/id1580231861) |
| Lightweight: Workout Tracker (ES title: "Lightweight: Diario de Entreno") | Cem Kagan Kayili | Health & Fitness | 1 (5.0) | 0 | 2026-04-24 | 2026-04-25 (v1.0.1) | lightweight-app.com | [6762335584](https://apps.apple.com/us/app/id6762335584) |
| LW: Gym Workout Tracker & Log (DE title: "LW: Trainingsplan & Fitness") | Lightweight Fitness Ltd | Health & Fitness | 0 in US; 1 in GB | 0 | 2026-09-14 | 2026-10-16 (v1.2.0) | getlightweight.com | [6786713713](https://apps.apple.com/us/app/id6786713713) |
| GoLightWeight: Workout Tracker | Taejun Oh | Health & Fitness | 1 (5.0) | 0 | 2026-07-19 | 2026-10-19 (v1.8.2) | golightweight.app | [6781628893](https://apps.apple.com/us/app/id6781628893) |
| lightweight. | Aron Takacs | Sports | 0 | 0 | 2026-09-15 | 2026-09-22 | lightweight.hu (VBT sensor and app, Hungary) | [6760489698](https://apps.apple.com/us/app/id6760489698) |
| 라잇웨잇 ("LightWeight", Korean) | LightWeight Incorporated (artist name "Light Weight") | Health & Fitness | 0 | 0 | 2025-08-07 | 2026-10-04 | n/a (digital weight machine companion app) | [6477874268](https://apps.apple.com/us/app/id6477874268) |
| 耶巴蒂Lightweight-健身紀錄、組間休息與計畫app | Xiangan Xie | Health & Fitness | 0 | 0 | 2026-03-30 (US) | 2026-09-30 | none | [6760705027](https://apps.apple.com/us/app/id6760705027) |

The brief gives the LW app's start as 2026-09. The API returns a release date of 2026-09-14. GoLightWeight advertises an Apple Watch companion app on its website, which makes it the closest feature overlap with our iPhone + Watch product.

### 1b. Non-fitness apps that use "lightweight" as an adjective

These still compete for the query "lightweight".

| App | Seller | Genre | US ratings | Released | App ID |
|---|---|---|---|---|---|
| Lightweight Text Editor | Erik Wegener | Productivity | 59 | 2022-06-06 | 1626906348 |
| Airshow: Lightweight Podcasts | Feedbin, Inc. | Entertainment | 33 | 2022-07-18 | 1584582270 |
| Quran - Lightweight Quran App | Abdurahman Sherif | Book | 6 | 2025-09-19 | 6752298970 |
| Lightweight Clock | Floyd Ross | Utilities | 3 | 2024-12-02 | 6733222071 |
| Lightweight WiFi Scanner | Owen Gerke | Utilities | 1 | 2026-03-04 | 6759912660 |
| Npp - Lightweight Text Editor | Ilia Bogdanovski | Developer Tools | 0 | 2026-03-10 | 6760112915 |
| Lightweight Boxer Stickers | Paul Scott | Sports | 0 (not seen in US) | 2025-08-22 | 6751363439 |
| Doa VPN - Lightweight VPN | LUSIA (KR) | Utilities | 0 | 2026-06-05 | 6770985904 |
| FraudShield - Lightweight LLMs | CodeScale | Utilities | 0 | 2025-05-01 | 6745196395 |
| babla – lightweight polls | Ting Chi Huang | Social Networking | 0 | 2026-09-10 | 6763086541 |
| Photo1M: Lightweight Camera | 深锐 郑 | Photo & Video | 0 | 2026-09-14 | 6804128282 |

No app with the two-word spelling "Light Weight" in its title appeared in any of the 48 result sets.

### 1c. Rank by query and storefront

"-" means the app was not in the returned results. The API returned 36–50 results per query.

**Lightweight! Workout Analysis (LIGHTWEIGHT LLC, 1580231861)**

| cc | lightweight | lightweight app | lightweight workout | lightweight gym | lightweight tracker | light weight |
|---|---|---|---|---|---|---|
| us | **1** | **1** | **1** | 7 | 31 | **1** |
| gb | 1 | 1 | 1 | 7 | 16 | 1 |
| ca | 1 | 1 | 1 | 2 | 18 | 1 |
| au | 1 | 1 | 1 | 6 | 12 | 1 |
| de | 1 | 1 | 1 | 1 | 1 | 1 |
| pl | 1 | 1 | 1 | 1 | 2 | 1 |
| ua | 1 | 1 | 1 | 1 | 3 | 2 |
| es | 1 | 1 | 1 | 1 | 3 | 1 |

**Lightweight: Workout Tracker (Cem Kagan Kayili, 6762335584)**

| cc | lightweight | lightweight app | lightweight workout | lightweight gym | lightweight tracker | light weight |
|---|---|---|---|---|---|---|
| us | 3 | 5 | 2 | - | 15 | 3 |
| gb | 3 | 4 | 3 | - | 20 | 4 |
| ca | 4 | 14 | 5 | - | - | 5 |
| au | 4 | 14 | 5 | - | - | 6 |
| de | 32 | 29 | 3 | 3 | 7 | 20 |
| pl | 3 | 15 | 4 | 3 | 7 | 23 |
| ua | 6 | 10 | 2 | 4 | 8 | 4 |
| es | 3 | 7 | 2 | 3 | 6 | 3 |

**LW: Gym Workout Tracker & Log (Lightweight Fitness Ltd, 6786713713).** "Lightweight" is not in its US title.

| cc | lightweight | lightweight app | lightweight workout | lightweight gym | lightweight tracker | light weight |
|---|---|---|---|---|---|---|
| us | 6 | - | 26 | 2 | 26 | 19 |
| gb | 2 | 5 | 2 | 1 | 1 | 3 |
| ca | - | - | - | 36 | - | 19 |
| au | - | - | - | - | - | 14 |
| de | - | - | 5 | 2 | 6 | - |
| pl | - | 32 | 5 | 2 | 6 | 13 |
| ua | - | 34 | 6 | 3 | 7 | 16 |
| es | 35 | - | 5 | 2 | 5 | - |

**Other "lightweight"-named apps: US rank for "lightweight" / "light weight"**

- Lightweight Text Editor: 2 / 2. It is #2–#6 for "lightweight" in every storefront.
- 라잇웨잇 (Korean): 5 / 5. Also #2 for "lightweight" in CA and UA.
- GoLightWeight: not in the top 50 for "lightweight". #28 in the US for "light weight".
- lightweight. (HU): not in the US results. #4 for "lightweight gym" in DE, PL and ES.

**US top 5 for "lightweight":**

1. Lightweight! Workout Analysis (183 ratings)
2. Lightweight Text Editor (59)
3. Lightweight: Workout Tracker (1)
4. Npp - Lightweight Text Editor (0)
5. 라잇웨잇 (0)

**US top 5 for "lightweight gym":**

1. Gym Workout: Trainer & Tracker (4,508)
2. LW: Gym Workout Tracker & Log (0)
3. The Gym Group (833)
4. Gym Workout Planner (678)
5. Gold's Gym (64)

**US top 5 for "lightweight tracker":** all generic tracker apps, such as CUBE Tracker and Weigh In. The query behaves like the generic word "tracker".

Raw data: `raw/search/*.json` and `analysis.json` in this folder.

## 2. Competitor websites

| Site | Brand usage | ® / ™ | Company / location (as published on the site) |
|---|---|---|---|
| https://www.lightweightapp.com/ | "Lightweight!" with an exclamation mark. Page title: "Lightweight! Fitness Exercise App — Smarter Workouts" | No ® or ™ on the homepage, terms or privacy pages. The Terms say: "Our trademarks and trade dress may not be used in connection with any product…" | © 2025 LIGHTWEIGHT LLC, 108 W. 13th Street, Suite 100, Wilmington, DE 19801. Governing law: Delaware, United States (https://www.lightweightapp.com/company/terms, /company/privacy). Contact: team@lightweightapp.com. This owner holds **USPTO Reg. 8430632** (see §3). |
| https://lightweight-app.com/ | "LIGHTWEIGHT." wordmark. Page title: "Lightweight — Track Every PR." Says "iOS & Android". | None | "© 2026 Lightweight". Terms are governed by the laws of the Republic of Türkiye, courts of Istanbul (https://lightweight-app.com/terms). The contact is a personal Gmail address. |
| https://getlightweight.com/ | Page title: "Lightweight: Workout Logger, Gym Finder & Gym Passport". The hero wordmark reads **"Lightweight, baby!"**, which is the same meme as our concept. The App Store title is "LW: …". The site has "Hevy alternative" and "Strong alternative" pages. | None | Lightweight Fitness Ltd, registered in England and Wales, Company no. 17401675, registered office Flat 14, 9b Eastcheap, London EC3M 1BN (https://getlightweight.com/legal). Terms are dated 18 Sep 2026, "trading as Lightweight". |
| https://golightweight.app/ (extra) | "GoLightWeight". Advertises an Apple Watch companion app and EN/KR languages. | None | "© GoLightWeight" |
| https://lightweight.hu/ (extra) | "lightweight." VBT sensor and app | None | Hungarian domain |

**Inference, not verified:** Lightweight Fitness Ltd may use "LW:" as its App Store title because of the US LIGHTWEIGHT! registration. Nothing on its site states this.

## 3. Trademark registries

### Reachability

| Registry | Reachable? | Method |
|---|---|---|
| USPTO Trademark Search (tmsearch.uspto.gov) | **Yes** | The site's public JSON search backend (`POST https://tmsearch.uspto.gov/prod-stage-v1-0-0/tmsearch`). Wordmark query: `lightweight OR lightweights OR "light weight" OR liteweight OR "lite weight" OR litewate OR lightwate…` returned 242 records, 73 of them live. Owner-name searches were also run. |
| EUIPO TMview (tmdn.org/tmview) | **Yes** | Public JSON search backend. "lightweight" filtered to Nice classes 9/41/42 returned 134 records. "light weight" in 9/41/42 returned 174 records; only the first 100 were reviewed. |
| WIPO Global Brand Database (branddb.wipo.int) | **No** | Blocked by a proof-of-work captcha (ALTCHA). TMview includes WIPO international registrations (WO) only partly. |
| UKIPO / EUIPO eSearch direct | Not queried directly | GB and EM records seen through TMview. |

### 3a. USPTO: live marks in classes 9 / 41 / 42 that contain LIGHTWEIGHT

| Mark | Serial / Reg. No. | Status | Classes | Owner | Goods / services (abridged) | Relevance |
|---|---|---|---|---|---|---|
| **LIGHTWEIGHT!** (standard characters; pseudo-mark "LIGHT WEIGHT!") | SN **99490250** / Reg. **8430632** | **REGISTERED** 2026-09-15 (filed 2025-11-11) | **9, 41** | **Lightweight LLC** (Delaware LLC), 108 W. 13th St, Suite 100, Wilmington DE 19801 | IC 009: "Downloadable software in the nature of a mobile application for creating and tracking personalized workout programs, nutrition plans, and fitness progress; … mobile application for fitness training, exercise tracking, and health monitoring." IC 041: online fitness coaching, fitness instructional courses, and virtual personal coaching | **Direct conflict.** Same word and the same goods as our app. Owner also runs App Store #1 for "lightweight". |
| LIGHTWEIGHT CHARTS | SN 97298772 / Reg. 7340628 (2024-03-26) | Registered | 9, 42 | TradingView, Inc. (DE) | Financial charting software | Unrelated goods. Low relevance. |
| LIGHTWEIGHTM2M | SN 87319274 / Reg. 5271075 | Registered | 42 | Open Mobile Alliance | M2M data protocols | Low |
| DUNN LIGHTWEIGHT | SN 90449051 / Reg. 6840378 | Registered | 42 | Andres Villaseñor Cortina (MX) | Architectural services | Low |
| COMBINE LIGHTWEIGHT DESIGN HEAVYWEIGHT PERFORMANCE | SN 86873022 / Reg. 5088311 | Registered | 42 | Concurrent Technologies Corp. | Software development frameworks | Low |
| LIFT LIGHTWEIGHT INNOVATIONS FOR TOMORROW | SN 88776818 / Reg. 6113661 | Registered | 41, 42 | American Lightweight Materials Mfg. Innovation Institute | Workforce training and materials R&D | Low |
| ALMEX LIGHTWEIGHT | SN 99407803 | Pending (suspension letter mailed) | 7, 9, 37, 42 | Almex Canada, Ltd. | Conveyor belt monitoring | Low |
| LIGHTWEIGHT STRUCTURES | SN 99902320 | Pending (assigned to examiner) | 40, 42 | Seaman Integrated Solutions | Tent and fabric structures | Low |

Related live marks outside 9/41/42 that matter for the meme:

| Mark | Reg. No. | Classes | Owner | Note |
|---|---|---|---|---|
| RONNIE COLEMAN'S "LIGHT WEIGHT BABY" | 5991413 (SN 87000611), §8&15 accepted | 5 (dietary supplements) | CA IP Holdings, LLC (FL) | The meme phrase is registered with Ronnie Coleman's name, for supplements. Apple's keyword rules also forbid celebrity names. |
| YEAH BUDDY | 6648127 (SN 90321637) | **9** (mobile apps on fitness and nutrition topics) | CA IP Holdings (FL) | The same owner has class-9 app coverage for another Ronnie Coleman catchphrase. Avoid both catchphrases in the name. |
| LIGHTWEIGHT | 6591170 (SN 88835020) | 3 (cosmetics) | Grooming Trade LLC / Nesis Labs LLC | Different goods |
| LIGHTWEIGHT | SN 99886716 (pending) | 33 (alcohol) | Team Demi Inc | Different goods |

Dead marks that show earlier interest in fitness and apps:

| Mark | Serial | Status | Classes | Owner |
|---|---|---|---|---|
| LIGHTWEIGHT | 97520296 | Abandoned | 28 (exercise weights) | LightWeight Inc. (Korea), the same company as the 라잇웨잇 app |
| LIGHT WEIGHT 85 GET YOUR WEIGHT UP! | 90733894 | Abandoned | 25, 41 (physical fitness instruction) | Angel Irizarry |
| LIGHTWEIGHT | 75902923 | Abandoned | 9 (unified messaging software) | Tornado Development, Inc. |

USPTO links:
- Record: https://tsdr.uspto.gov/#caseNumber=99490250&caseType=SERIAL_NO&searchType=statusSearch (TSDR returned HTTP 500 to this environment, so this record was not opened. The data above comes from the tmsearch backend.)
- Search UI: https://tmsearch.uspto.gov/search/search-information

No USPTO filings were found under the owner names "Lightweight Fitness" (the LW app), "Kayili", "GoLightWeight" or "Taejun Oh".

### 3b. TMview: live marks with LIGHTWEIGHT or LIGHT WEIGHT in Nice 9 / 41 / 42, outside the US

| Office | Mark | Appl. / Reg. No. | Status | Classes | Owner | Relevance |
|---|---|---|---|---|---|---|
| GB | LIGHTWEIGHTS (word) | UK00004214011 (filed 2025-06-04) | Registered | 41 | George Duke | **Medium for a future UK launch.** Near-identical word in class 41. Exact services not retrieved; check them. |
| KR | LIGHT WEIGHT | 4020230193860 / 4023804600000 (filed 2023-10-26) | Registered | 9 | 주식회사 라잇웨잇 (LightWeight Inc.) | High for Korea, if Korea is ever a target |
| CN | LIGHTWEIGHT | 43668241 (filed 2020-01-08) | Registered | 41 | 北京励德展览有限公司 (Beijing Reed Exhibitions) | Relevant only for China |
| IN | M UNISEX FITNESS STUDIO Light Weight Baby (combined) | 5055651 | Registered | 41 | C. Manikandan | India only |
| AU | GYM PT … THE LIGHTWEIGHT MOVEMENT … (figurative) | 2578053 | Registered | 9, 16, 35, 41 | Jason Dean Warburton | Low to medium for AU. Long composite mark. |
| EM (EUIPO) | German Lightweight (figurative) | 015697873 | Registered | 10, 17, 19, 20, 27, 28, 35, 40, 41 | Gaugler & Lutz GmbH & Co. KG | Low (materials industry) |
| EM | ELA European Lightweight Association (figurative) | 018412376 | Registered | 9, 16, 35, 41 | Bayern Innovativ GmbH et al. | Low |
| GB | LIGHTWEIGHT LEISURE (TRAILER) AWARDS (figurative) | UK00004136909, UK00004101842 | Registered | 16, 18, 35, 41 | The Caravan Club Ltd | Low |

No live EUIPO (EM) word mark "LIGHTWEIGHT" covering fitness or workout software was found in the TMview results reviewed.

TMview search UI: https://www.tmdn.org/tmview/#/tmview (search "lightweight", filter Nice 9/41/42).

### 3c. What the owner or counsel should still search manually

1. **USPTO TSDR record and file history for SN 99490250** (link above). Check the specimen, whether the registration is on the Principal Register, and any disclaimers. Also check any **later filings by Lightweight LLC**, such as class 42 or a design mark.
2. **USPTO full clearance**, done by an attorney or a search vendor such as CompuMark or Corsearch. Cover phonetic equivalents (LITEWAIT, LYTEWEIGHT), the house-mark combinations you plan to use, and **common-law use**: the App Store, Google Play, websites, social handles and state registrations.
3. **WIPO Global Brand Database** (https://branddb.wipo.int): "LIGHTWEIGHT" in classes 9/41/42 with US designation. It was not reachable from this environment because of a captcha.
4. **UKIPO**: check the services of UK00004214011 LIGHTWEIGHTS (https://trademarks.ipo.gov.uk/ipo-tmcase/page/Results/1/UK00004214011; this URL returned 403 from this environment, so if it fails search the number at https://www.gov.uk/search-for-trademark) before any UK launch.
5. **EUIPO eSearch** (https://euipo.europa.eu/eSearch/) for EU expansion.
6. **Xata as a house mark:** USPTO shows **XATA, Reg. 7094736, class 42** (SaaS for managing databases), owned by Xatabase, Inc. (DE). There are also XATA marks in classes 29 and 33. Counsel should check this before putting "Xata" into the app name.

## 4. ASO implications for the query "lightweight"

**How crowded is it?**
- The query is a common English adjective. 36–50 results come back per storefront, and many are non-fitness ("lightweight text editor", "lightweight VPN").
- **Seven** fitness or gym apps carry the brand. Four of them launched in 2026 alone: Cem Kayili in April, GoLightWeight in July, LW in September, and lightweight. (HU) in September.
- Lightweight! is **#1 for "lightweight", "lightweight app", "lightweight workout" and "light weight" in all 8 storefronts.** It has five years of history and 183 US ratings (255 in DE).

**Could a new app realistically rank #1?**
- Not in the short term. Apple's own search page lists ranking factors as "text relevance (matches for your app's title, subtitle, keywords, and primary category), as well as user behavior (downloads, ratings and reviews, and more)" (https://developer.apple.com/app-store/search/).
- A newcomer can match the incumbent on title text. It cannot match the incumbent's behavioral signals. Cem Kayili's app has a near-exact title ("Lightweight: Workout Tracker") and still ranks only #3 in the US, behind a text editor with 59 ratings.
- People searching "lightweight" will be split between the brand-intent user (looking for the incumbent) and generic intent. So the brand query is a weak acquisition channel for us even if we win it.

**How does Apple handle exact-name matches?**
- App Store Connect blocks an identical name only within the same localization: "You can use an app name for one app per localization." The trademark claim route is spelled out in the same doc: "If another developer is using the app name and you have trademark rights to it, you can submit a claim" (https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app, linking to https://www.apple.com/legal/internet-services/itunes/appnamenotices/).
- Apple's docs do not say whether the uniqueness check ignores punctuation or case. "Lightweight!" and "lightweight." already coexist with "Lightweight: Workout Tracker".
- Search ranking itself gives no special bonus for an identical title beyond text relevance.

**Practical risk.** Lightweight LLC now holds a registered class-9 mark that covers workout-tracking apps. It can file an app-name claim or an IP dispute with Apple (https://www.apple.com/legal/intellectual-property/dispute-forms/index.html). Guidelines 5.2.1 and 4.1 apply. A forced rename after launch would throw away the title-keyword equity, the screenshots and the brand recall built in the meantime.

**Name structures that help**
- `Brand: keyword keyword` puts high-volume generic terms such as "gym", "workout", "lift", "tracker" and "log" into the title, which is the heaviest-weighted field. The subtitle (30 characters) and the keyword field (100 characters) carry the rest. Do not repeat words across the three fields (Apple search guidance).
- A **distinctive compound brand** such as "Lightweight Lifts" gives searchers a unique string to type and reduces mis-installs. It does **not** fix the trademark issue, because LIGHTWEIGHT stays the dominant element and the goods are identical.
- Apple says to avoid "names that use generic terms or are too similar to existing app names" (https://developer.apple.com/app-store/product-page/).
- Do **not** use "Hevy", "Strong", "Ronnie Coleman" or "Apple" in the name or keywords. Apple's rules forbid trademarked terms, competing app names and celebrity names. "Watch" alone is a generic word.

## 5. Name options

All counts are characters, including spaces and punctuation; the limit is 30. "iTunes check" means an exact-string query on US iTunes Search (limit 25). "No identical name" means no result had the same normalized title.

**Every "Lightweight …" option below carries the same trademark exposure to US Reg. 8430632.** The modifier only reduces App Store confusion.

| # | Name | Chars | iTunes check (US) | Pros | Cons |
|---|---|---|---|---|---|
| 1 | **Lightweight Lifts: Gym Tracker** | 30 | No identical name. Top results are generic gym trackers (Stacked, Gymatic). | Unique compound brand that is easy to say. "lifts", "gym" and "tracker" are in the title. | Exactly 30, no spare room. LIGHTWEIGHT still dominant. |
| 2 | **Lightweight: Lift & Watch Log** | 29 | No identical name | Highlights the Apple Watch differentiator; few competitors say "Watch". | "Watch log" is lower-volume than "workout tracker". "&" uses a character. |
| 3 | **Lightweight Strength Tracker** | 28 | No identical name | Matches the product exactly. "strength" is a strong keyword. | Reads generic. Weak brand distinctiveness against the incumbent. |
| 4 | Lightweight Lift Log | 20 | No identical name. "Lift Log: #1 Weightlifting Log" (FitnessAI, 978 ratings) and "Lift Log: Lifting Tracker" exist. | Short. 10 spare characters. | Overlaps an existing "Lift Log" app name. |
| 5 | Lightweight Sets: Gym Log | 25 | No identical name | "sets" signals set logging | "Sets" is a weak brand element |
| 6 | Lightweight Wrist: Gym Log | 26 | No identical name | Watch angle | "Wrist" is unclear without context |
| 7 | Lightweight Club: Lift Tracker | 30 | No identical name | Community feel | Implies social features. Only claim them if the app really has them. |
| 8 | Lightweight by Xata: Gym Log | 28 | No identical name | House mark adds distinctiveness, like "Almex Lightweight" or "Dunn Lightweight" at the USPTO | Live USPTO **XATA, Reg. 7094736, class 42** (Xatabase, Inc.). Spends characters on the agency name. |
| 9 | Lightweight Gym Tracker (current placeholder) | 23 | No identical name | Simple, keyword-rich | The most generic option and the closest to the incumbent |
| 10 | Lightweight Baby: Gym Tracker | 29 | No identical name | Captures the meme | **Not recommended.** RONNIE COLEMAN'S "LIGHT WEIGHT BABY" is Reg. 5991413. getlightweight.com already uses "Lightweight, baby!". Celebrity association. |

### Fallback distinctive brands (use only if counsel rates the LIGHTWEIGHT risk unacceptable; not the recommendation)

| Name | Chars | iTunes check (US) | USPTO quick check (exact word only) | Notes |
|---|---|---|---|---|
| **Featherlift**: Gym Workout Log | 28 | No app named Featherlift | Only live record is FEATHERLIFT SN 99527376, class 3 hair care (Soulstice, notice of allowance). Others are dead. | Keeps the "light" idea (a feather-light lift). Easy to spell. |
| **Platelight**: Lift Tracker | 24 | No app named Platelight | No PLATELIGHT records. PLATELITE (class 9, outlet covers) is abandoned. | Plate plus light. Nods to the meme without using it. |
| **Lightrep**: Gym Workout Log | 25 | No app named Lightrep | LIGHTREP class 9 (office software), cancelled | Short. "Rep" fits fitness. Still contains "Light", so check similarity to LIGHTWEIGHT! with counsel. |

Rejected during the check:
- HeavySet: "HeavySet - Gym Workout Log", Runloop Ltd, 1,274 ratings.
- Ironfeather: live IRONFEATHER and IRON FEATHER marks in class 28 (fishing), 25, 13 and 33.

The "light weight, baby!" line can live on as a tagline, a screenshot caption or a social hook, subject to the same counsel review because of CA IP Holdings' mark.

## 6. Apple's official rules on app names

- **App Review Guideline 2.3.7:** "Choose a unique app name, assign keywords that accurately describe your app, and don't try to pack any of your metadata with trademarked terms, popular app names, pricing information, or other irrelevant phrases just to game the system. App names must be limited to 30 characters." (https://developer.apple.com/app-store/review/guidelines/#2.3.7)
- **Guideline 4.1(a) Copycats:** "Don't simply copy the latest popular app on the App Store, or make some minor changes to another app's name or UI and pass it off as your own. In addition to risking an intellectual property infringement claim, it makes the App Store harder to navigate…"
- **Guideline 5.2.1:** "Don't use protected third-party material such as trademarks … and don't include misleading, false, or copycat representations, names, or metadata in your app bundle or developer name."
- **App Store Connect Help, "Add a new app" (FAQ):** "You can use an app name for one app per localization. If an app in your account already uses the app name, you have two options: submit an update to the existing app to change its name, or remove the app from App Store Connect… If another developer is using the app name and you have trademark rights to it, you can submit a claim." (https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app)
- **App Store Connect Help, "App information":** "The name must be at least two characters and no more than 30 characters." (https://developer.apple.com/help/app-store-connect/reference/app-information/app-information)
- **Product page guidance:** "Be distinctive. Avoid names that use generic terms or are too similar to existing app names. An app name can be up to 30 characters long." (https://developer.apple.com/app-store/product-page/)

## Files in this folder

- `raw/search/`: 48 iTunes Search responses
- `raw/lookup/`: lookup responses for us, gb and de
- `raw/names/`: candidate-name searches
- `raw/web/`: competitor web pages
- `raw/tm/`: USPTO and TMview JSON
- `raw/apple/`: Apple documentation pages
- `analysis.json`
- `scripts/`: the scripts that produced these results. Python was run with `-I`.
