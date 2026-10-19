# Lightweight: App Store markets and localization priorities after US English

Data collected on 2026-10-19 from the public iTunes Search/Lookup API, Apple's legacy RSS charts and apps.apple.com product pages. Raw files are in `markets/raw/` and the scripts are in `aso/scripts/`.
Labels used below: **[data]** means fetched directly. **[proxy]** means an indirect signal. **[inference]** means my judgement. **[secondary]** means a third-party figure that I did not check against the primary report.

**Candidate pool:** these are the confirmed Lightweight UI languages at release. They are English, Ukrainian, Russian, Polish, German, Dutch, French, Spanish, Portuguese (Portugal), Portuguese (Brazil), Italian, Turkish and Czech. A localized App Store product page should be created only for a language the app UI supports. Every candidate below is a UI language.

---

## 0. Recommendation (ranked)

| # | App Store localization(s) | Storefronts reached (default / additional per Apple) | Why |
|---|---|---|---|
| — | **English (U.K.)** (plus English (Australia) and English (Canada)): a near-free step and not a translation | GB, AU and CA as default. Default in PL, CZ, TR, UA, BE and KZ. **Additional** in DE, AT, CH, FR, ES, PT, IT, NL, SE, BR, MX | The UI is already English. This adds a second 100-character keyword field in almost every European storefront. It also covers the #2 to #4 English markets (GB 138.7k, CA 105.1k, AU 74.1k summed ratings [proxy]). |
| 1 | **German** | DE, AT, CH (default) | Largest non-English proxy: DE 49.6k + AT 7.0k + CH 7.7k [proxy]. Euro pricing is at the top of the range (Adapty price index about 1.2 vs US). Strength trackers chart in Top Grossing H&F in DE: Hevy #29, Alpha Progression #39, Lyfta #60, Fitbod #69, Strong #78 [data]. Competitors win German keywords with German titles (“Hevy - Gym & Trainingstagebuch”, “Alpha Progression Muskelaufbau”) [data]. |
| 2 | **Spanish (Mexico) + Spanish (Spain)**: one translation adapted into two locales | MX (default), ES (default). Spanish (Mexico) is also an **additional language in the US storefront** | ES 28.6k + MX 27.9k [proxy]. Hevy is #1 for “registro gimnasio” in both stores and #7 Top Grossing H&F in ES [data]. es-MX adds keyword space in the US, the main revenue market [inference, see §4]. |
| 3 | **French** (later French (Canada)) | FR (default). Additional in BE, CH and the **US**. French (Canada) is additional in CA | FR 26.5k + BE 6.4k + part of CH and CA [proxy]. Hevy holds #1 for “suivi musculation” and “carnet d'entraînement” with a French title [data]. |
| 4 | **Portuguese (Brazil)** | BR (default). Also additional in the **US** | BR 32.5k, the second-largest non-English proxy, almost all of it Hevy (25.2k) [proxy]. Hevy is #19 Top Grossing H&F in BR [data]. Prices are lower: Hevy charges R$99.90/yr against $23.99 in the US [data]. This market is about volume and the extra US keyword field, not ARPU [inference]. |
| 5 (optional / strategic) | **Ukrainian** | UA (additional; English (U.K.) is the default) | Smallest revenue signal (UA 2.9k [proxy]). No major tracker ships a Ukrainian product page: Hevy and Strong have no UK binary, and Lyfta's UA page shows English even with `lang=uk` [data]. Cost is near zero for a Ukrainian team, and it supports home-market credibility, PR and early reviews [inference]. Do it for brand reasons, not for revenue. |

**Next wave (worth doing after the first 4–5 are measured):** Dutch (NL 19.2k, an English-heavy market) and Italian (IT 14.3k). Polish comes after those (PL 9.7k). Polish is only an *additional* language in PL, and English (U.K.) is the default. The Ukrainian diaspora may be relevant there, but that is an inference.
**Skip for now:** Turkish (TR 6.4k; very low prices: Hevy ₺159.99/yr vs €26.49 in DE [data]; Adapty: DE is 4.4× TR for H&F annual plans [secondary]), Czech (CZ 4.2k, the smallest European proxy, with Czech additional only), Portuguese (Portugal) (PT 7.3k; it can reuse pt-BR work later with light adaptation) and Russian (see §5).

---

## 1. Competitor localizations (binary `languageCodesISO2A`, US lookup)

`languageCodesISO2A` lists the **app binary** languages, not necessarily localized product pages. For example, Hevy lists PL but keeps an English title in PL even with `lang=pl`. Hevy has a Turkish title in TR with `lang=tr` [data].

|App|#langs|EN|DE|ES|FR|PT|IT|NL|PL|CS|TR|UK|RU|Other|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Hevy|16|Y|Y|Y|Y|Y|Y|·|Y|·|Y|·|Y|AR CA HI JA KO ZH ZH|
|Strong|11|Y|Y|Y|Y|Y|Y|·|·|·|·|·|Y|JA KO ZH ZH|
|Fitbod|3|Y|·|Y|·|Y|·|·|·|·|·|·|·||
|StrengthLog|1|Y|·|·|·|·|·|·|·|·|·|·|·||
|AlphaProg|13|Y|Y|Y|Y|Y|Y|Y|Y|·|Y|·|·|DA JA NB SV|
|JEFIT|6|Y|Y|Y|Y|·|Y|·|·|·|·|·|·|ZH|
|Dropset|1|Y|·|·|·|·|·|·|·|·|·|·|·||
|HeavySet|1|Y|·|·|·|·|·|·|·|·|·|·|·||
|Boostcamp|1|Y|·|·|·|·|·|·|·|·|·|·|·||
|Lyfta|28|Y|Y|Y|Y|Y|Y|Y|Y|Y|Y|Y|Y|AR DA FI EL ID JA KO LT MS NB FA ZH SV TH ZH VI|
|Stronglifts|20|Y|Y|Y|Y|Y|Y|Y|Y|·|Y|Y|Y|HR DA FI JA KO NB ZH SV ZH|
|Gymverse|1|Y|·|·|·|·|·|·|·|·|·|·|·||
|Liftoff|1|Y|·|·|·|·|·|·|·|·|·|·|·||
|Setgraph|7|Y|Y|Y|Y|·|·|·|·|·|·|·|·|JA KO ZH|
|RepCount|12|Y|Y|Y|Y|Y|Y|Y|·|·|·|·|·|DA FI KO NB SV|

Source: `https://itunes.apple.com/lookup?id=<id>&country=us`. App IDs: Hevy 1458862350, Strong 464254577, Fitbod 1041517543, StrengthLog 1434229662, Alpha Progression 1462277793, JEFIT 449810000, Dropset 6444746146, HeavySet 1171500310, Boostcamp 1529354455, Lyfta 6443740936, Stronglifts 488580022, Gymverse 1048454034, Liftoff 6448081563, Setgraph 1209781676, RepCount 594982044.

**Localized product page titles per storefront** [data, lookup default language]:
| Store | Hevy | Lyfta | Alpha Progression |
|---|---|---|---|
| de | Hevy - Gym & Trainingstagebuch | Lyfta: Gym & Trainingstagebuch | Alpha Progression Muskelaufbau |
| fr | Hevy Carnet de Musculation Gym | Lyfta : Carnet de Musculation | Alpha Progression Musculation |
| es / mx | Hevy: Gym tracker y rutinas | Lyfta: Rutinas & Gym Tracker | Musculación / Rutinas Gym |
| it | Hevy: Scheda Palestra Esercizi | Lyfta: Scheda Palestra | Alpha Progression Palestra |
| br | Hevy Gym - Treino de Academia | Lyfta: Treinos de Academia Gym | Alpha Progression Treino Gym |
| nl | Hevy - Workout Tracker Gym Log (EN) | Lyfta: Trainingslogboek | Alpha Progression Spieropbouw |
| pl (`lang=pl`) | EN title | Lyfta: Dziennik Treningowy | — |
| tr (`lang=tr`) | Hevy - Spor, Vücut Geliştirme | Lyfta: Spor & Vücut Geliştirme | — |
| ua (`lang=uk`) | EN title | EN title | — |

PL, CZ, TR and UA lookups without `lang` return English, which matches Apple's table: English (U.K.) is the default there.

## 2. Rating counts per storefront: **[proxy] for where the category has users**

`userRatingCount` from `lookup?id=…&country=<cc>` is per storefront. These counts are cumulative ratings, not active users or revenue. They skew towards older apps and apps that prompt for ratings.

|App|us|gb|ca|au|de|at|ch|fr|be|es|pt|it|nl|se|pl|cz|br|mx|tr|ua|ru|kz|jp|kr|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Hevy|98819|30118|21458|18077|12733|1735|2541|11339|2304|19424|3619|7757|7512|3094|4237|1682|25248|12424|2076|1194|–|326|2102|597|
|Strong|108536|23933|13027|13418|10134|1955|1605|2592|755|1700|710|1570|3121|1983|1466|465|916|1501|618|340|450|48|1658|3629|
|Fitbod|287740|16320|25002|9734|1734|366|812|970|671|1097|414|763|1395|1887|645|207|848|1465|394|194|171|41|212|108|
|StrengthLog|3687|783|490|379|179|19|36|53|30|48|28|35|76|14477|25|22|36|40|17|9|–|1|24|3|
|AlphaProg|2226|845|458|398|12076|1303|707|86|38|68|25|60|126|88|72|22|53|51|31|18|16|7|8|5|
|JEFIT|46917|6137|6960|4298|1308|208|307|470|274|983|359|342|1109|861|673|146|508|828|297|210|364|64|239|481|
|Dropset|96|51|22|23|11|0|5|6|0|2|1|9|1|35|3|1|4|8|2|9|12|1|1|0|
|HeavySet|1274|304|176|163|81|9|30|26|11|22|4|19|55|48|22|7|11|17|3|7|22|0|14|4|
|Boostcamp|10611|1242|1495|728|314|47|50|130|65|82|66|86|209|190|111|44|84|104|88|24|26|8|67|1371|
|Lyfta|7014|1319|1539|915|1144|179|184|1183|294|755|506|756|427|620|362|147|544|756|339|267|293|179|68|44|
|Stronglifts|76850|14496|8065|6739|1200|183|287|467|341|357|139|192|1544|2887|397|117|284|207|491|66|285|23|320|1644|
|Gymverse|165350|21115|10998|10846|1033|235|243|541|308|932|565|568|575|2678|280|179|959|4210|1162|234|139|40|269|104|
|Liftoff|99755|15268|12016|5450|5025|508|629|8063|1061|2693|674|1470|1438|1293|1230|1056|2744|5996|694|244|124|182|1708|149|
|Setgraph|6174|1550|1301|1091|398|26|75|169|61|149|90|135|293|156|94|55|134|158|154|51|28|13|11|1|
|RepCount|13406|5200|2092|1882|2239|268|217|426|222|251|86|498|1311|3430|111|37|99|170|31|10|9|6|30|518|
|**Sum**|928455|138681|105099|74141|49609|7041|7728|26521|6435|28563|7286|14260|19192|33727|9728|4187|32472|27935|6397|2877|1939|939|6731|8658|

“–” means the app is not returned in that storefront. Hevy and StrengthLog are not available in the Russia storefront [data].
Observations [inference]:
- Outside English markets, the largest pools are DE (49.6k), SE (33.7k, mostly StrengthLog, which is Swedish), BR (32.5k), ES (28.6k), MX (27.9k), FR (26.5k), NL (19.2k) and IT (14.3k).
- Alpha Progression is German and has 12.1k ratings in DE, more than in the US. A focused German product page can carry an app in that market.
- NL and SE punch above their population, but both are high-English markets and Swedish is not a Lightweight UI language.

## 3. Search results for localized “workout tracker / gym log” terms

`https://itunes.apple.com/search?entity=software&country=<cc>&limit=25&term=<term>`. The API ranking only approximates in-app App Store search [proxy].

|Store|Term|Tracked apps (rank in top 25)|Top 5 results (store ratings)|
|---|---|---|---|
|us|workout tracker|Strong #1, Hevy #2, Fitbod #5, JEFIT #12|Strong Workout Tracker Gym L (108536); Hevy - Workout Tracker Gym L (98819); Habit Tracker (148052); RepCount - Gym Workout Track (13406); Fitbod: Gym & Fitness Planne (287740)|
|us|gym tracker|Strong #1, Hevy #2, Fitbod #5, JEFIT #9, Dropset #18|Strong Workout Tracker Gym L (108536); Hevy - Workout Tracker Gym L (98819); Iron - Workout Tracker (379); SHRED: Gym & Home Workouts (40385); Fitbod: Gym & Fitness Planne (287740)|
|us|gym log|Strong #1, Hevy #3, Fitbod #8, JEFIT #12|Strong Workout Tracker Gym L (108536); Gym Workout Planner Log: Gri (49); Hevy - Workout Tracker Gym L (98819); Gym log - Strive (877); Gym Log+ — Workout Tracker (694)|
|gb|workout tracker|Hevy #1, Strong #2, Fitbod #7, JEFIT #15|Hevy - Gym Tracker Workout L (30118); Strong Workout Tracker Gym L (23933); RepCount - Gym Workout Track (5200); Habit Tracker (23095); Stronger - Gym Workout Plann (6138)|
|gb|gym tracker|Hevy #1, Strong #2, Fitbod #7, JEFIT #15, Dropset #19|Hevy - Gym Tracker Workout L (30118); Strong Workout Tracker Gym L (23933); Iron - Workout Tracker (35); Stronger - Gym Workout Plann (6138); RepCount - Gym Workout Track (5200)|
|ca|workout tracker|Hevy #1, Strong #2, Fitbod #5, JEFIT #10|Hevy - Gym Tracker Workout L (21458); Strong Workout Tracker Gym L (13027); Habit Tracker (19455); RepCount - Gym Workout Track (2092); Fitbod Workout & Gym Planner (25002)|
|au|gym tracker|Hevy #1, Strong #2, Fitbod #7, JEFIT #14, Dropset #15, Boostcamp #19, AlphaProg #21|Hevy - Workout Tracker Gym L (18077); Strong Workout Tracker Gym L (13418); Iron - Workout Tracker (56); Stronger - Gym Workout Plann (1746); Reps: Workout Tracker Gym Lo (4)|
|de|gym tracker|Strong #1, Hevy #2, AlphaProg #3, Fitbod #17, JEFIT #22|Strong Workout Tracker Gym L (10134); Hevy - Gym & Trainingstagebu (12733); Alpha Progression Muskelaufb (12076); Fitness App—Gym Workout, Spo (18164); RepCount - Trainingstagebuch (2239)|
|de|trainingstagebuch|Hevy #1, Strong #4, AlphaProg #10|Hevy - Gym & Trainingstagebu (12733); RepCount - Trainingstagebuch (2239); GymBook ・ Krafttraining (5187); Strong Workout Tracker Gym L (10134); GAINSFIRE Trainingstagebuch (5923)|
|de|krafttraining|Hevy #1, AlphaProg #5, Strong #9|Hevy - Gym & Trainingstagebu (12733); Workouts Zuhause - Fitness A (17419); GymBook ・ Krafttraining (5187); Fitness App—Gym Workout, Spo (18164); Alpha Progression Muskelaufb (12076)|
|at|trainingsplan fitnessstudio|Hevy #10|MyFitCoach - Trainingsplan (963); Fitness App—Gym Workout, Spo (1306); Trainingsplaner: Fitnessplän (75); GymBook ・ Krafttraining (403); Muskelaufbau Trainingsplan A (248)|
|fr|suivi musculation|Hevy #1, Strong #7, JEFIT #19|Hevy Carnet de Musculation G (11339); Carnet de Musculation (1983); Fitness & Exercice Musculati (19318); Carnet de musculation: Lifty (80); RepFlow - Suivi Musculation (3)|
|fr|carnet d'entraînement|Hevy #1|Hevy Carnet de Musculation G (11339); GymBook ・ Musculation (1639); Carnet de musculation: Lifty (80); Journal d'entraînement (0); Train-Note : Votre carnet de (1)|
|fr|musculation|Hevy #3, Strong #16|Entraînement à la Maison (28872); Fitness & Exercice Musculati (19318); Hevy Carnet de Musculation G (11339); FizzUp - Fitness & Musculati (24589); Gym: Exercice Musculation (267)|
|be|musculation|Hevy #3, Strong #22, JEFIT #24|Home Workout - No Equipments (3028); Gym Workout App & Fitness Pl (1270); Hevy - Gym Tracker Workout L (2304); Lyfta: Gym Tracker Workout L (294); Decathlon Coach: Sport/Runni (1341)|
|es|registro gimnasio|Hevy #1|Hevy: Gym tracker y rutinas (19424); FitTracker - Diario de Gym (56); Progression: Entrenamiento (14); Rutinas: Registro de gimnasi (2); Registro de Entrenos: Gimnas (0)|
|es|rutina gimnasio|Hevy #1, Fitbod #11|Hevy: Gym tracker y rutinas (19424); Symmetry: Gym Tracker con IA (11799); Ejercicios, entrenamiento ca (15277); Gym WP - Rutina Entrenamient (4416); Gym Life - Rutina Gimnasio (730)|
|pt|treino ginásio|Hevy #14|App de Fitness: Treino em ca (3074); Treino Academia e Musculação (89); Gym WP - Treino Academia (712); Lyfta: Treinos de Ginásio (506); Fitness - Treino e Exercicio (289)|
|pt|registo de treino|AlphaProg #4|Progression: Diário de Trein (13); FitPad (1); GymStreak: Plano de Treino I (574); Alpha Progression Musculação (25); Metric – Treino de Força (2)|
|it|diario allenamento|Hevy #1, Strong #6|Hevy: Scheda Palestra Eserci (7757); RepCount Diario di allenamen (498); GymPad - Diario palestra (1); GymBook ・ Allenamento Forza (1015); Allenamento a Casa (9869)|
|it|scheda palestra|Hevy #1|Hevy: Scheda Palestra Eserci (7757); Gym Life - Scheda palestra (2384); Lyfta: Scheda Palestra (756); Allenamento a casa e palestr (13837); GymBook ・ Allenamento Forza (1015)|
|nl|gym tracker|Hevy #1, Strong #2, Fitbod #8, JEFIT #14|Hevy - Workout Tracker Gym L (7512); Strong Workout Tracker Gym L (3121); Liftoff - Ranked Gym Workout (1438); Stronger - Gym Workout Plann (569); RepCount - Gym Workout Track (1311)|
|nl|trainingsschema|AlphaProg #7|Sportschool Krachttraining (38); Fitness App—GYM Workout, Spo (3740); Workouts voor Thuis (2795); Fitness Trainingsschema: Ada (88); Sporten: afvallen in 30 dage (15)|
|se|träningsdagbok|StrengthLog #3|RepCount Träningsdagbok Gym (3430); Träningsdagbok - WorkoutWise (1); StrengthLog – Workout Tracke (14477); Fiore: Gym Träningsdagbok (5); Lyfta: Träningsapp för Gym (620)|
|se|gym tracker|Hevy #2, StrengthLog #3, Strong #7, Fitbod #15, JEFIT #21|RepCount Träningsdagbok Gym (3430); Hevy - Workout Tracker Gym L (3094); StrengthLog – Workout Tracke (14477); Stronger - Gym Workout Plann (1139); Lyfta: Träningsapp för Gym (620)|
|pl|dziennik treningowy|—|Gym log - Strive (1931); Gym Routine Tracker - Reps (39); Gymlify - workout tracker (554); Gravitus - Gym Workout Track (2647); GymPad - Workout Tracker (35)|
|pl|plan treningowy siłownia|AlphaProg #11|Gym Workout App & Fitness Pl (5538); Gymlify - workout tracker (554); Gym Workout Planner & Gym Lo (140); Fitness Planner Gym・Workout  (450); Weight Training Plan for Wom (0)|
|cz|deník tréninku|—|Workout Tracker: Strength Lo (0); Workout Tracker - RPG Fitnes (0); Liftset: Push Pull Legs Log (0); Push Up Log: Press Up Tracke (0); Kettlebook: Gym Workout Log (0)|
|cz|posilovna|—|Fitness Planner Gym・Workout  (182); Gym Workout Planner Tracker (0); Fitwill: Workout Log & Plann (4); Gym Workout - Muscle Buildin (19); Liftoff - Ranked Gym Workout (1056)|
|br|registro de treino|Hevy #1, AlphaProg #25|Hevy Gym - Treino de Academi (25248); GymPad - Diário de treino (8); Steady: Treinos de Academia (120); Check Calendar - Hábitos (932); FitFit Diário de Treino (3)|
|br|treino academia|Hevy #7, Fitbod #18|Treino App: Exercícios em Ca (100484); Treino (132339); Treino Academia e Musculação (939); Gym WP - Treino Academia (24480); Fitness: Treinos para mulher (1012)|
|mx|registro gimnasio|Hevy #1|Hevy: Gym tracker y rutinas (12424); kach: Registro de Gimnasio (0); Rutinas: Registro de gimnasi (0); Gimnasio Diario y Calendario (2); FitTracker - Diario de Gym (26)|
|mx|rutina gimnasio|Hevy #2, Fitbod #16|Symmetry: Gym Tracker con IA (17653); Hevy: Gym tracker y rutinas (12424); Gym WP - Rutina Entrenamient (6212); Gravl: Entrenador Personal I (5006); Ejercicio en casa, fitness g (13231)|
|tr|antrenman takip|AlphaProg #22|Gym Workout Tracker: GymCycl (9); Fit Records - Workout Tracke (24); Gym Workout App & Fitness Pl (8130); MuscleWiki: Workout & Fitnes (594); ANTRENMAN TAKİP (2)|
|tr|spor salonu|Hevy #8|Gym Workout Planner & Gym Lo (143); ProFit: Workout Planner (2288); GymTekno (83); GoGYM - GYM Workouts|Exercis (4); MAC+: Gym & Home Workouts (45397)|
|ua|щоденник тренувань|Strong #11|Forma: Workout Tracker Gym L (259); Steel Weight Lifting Workout (51); Fiore: Workout Tracker Gym L (4); GymUp: Gym Workout Tracker L (106); Workout Tracker Gym Log - Sw (0)|
|ua|gym tracker|Hevy #1, Strong #5, Dropset #13, Fitbod #16, AlphaProg #17, JEFIT #23|Hevy - Gym Tracker Workout L (1194); Forma: Workout Tracker Gym L (259); Lyfta: Gym Tracker Workout L (267); Gym Workout App & Fitness Pl (9315); Strong Workout Tracker Gym L (340)|
|ua|тренування в залі|—|Gym Workout App & Fitness Pl (9315); Gym Workout Planner - Fitoni (766); GT Gym Workout Plans (188); Фитнес Тренировка в Зале Дом (177); Pro Fitness: Gym Workout Pla (32)|
|ru|дневник тренировок|—|Fitsession: дневник трениров (1912); Forma - дневник тренировок (2123); Фитнес тренировки дома, в за (59400); Дневник тренировок - Wise (163); Дневник тренировок Тренировк (241)|
|kz|дневник тренировок|Hevy #2|Gymsee: дневник тренировок (4); Hevy - Gym Tracker Workout L (326); Forma: Workout Tracker Gym L (46); Gym Workout App & Fitness Pl (3253); Grif: Workout Tracker (0)|
|jp|筋トレ 記録|—|最強の筋トレ管理アプリ-筋トレMEMO (51699); 継続する技術｜ダイエットも筋トレも記録・習慣化で目標達成 (53402); 筋トレ記録・管理で継続＆習慣化 - バーンフィット (2779); 「筋トレ日記」- サクサク入力できる (1286); トレメモ　筋トレ記録・トレーニング管理アプリ (32)|
|kr|헬스 기록|Hevy #6|플릭 - 운동일지, 운동기록, 운동일기, 운동루틴 (13694); 플랜핏 - 운동 루틴 추천과 헬스 홈트 다이어트 기 (29187); 셀핏 - 운동기록, 운동일지 (1020); 번핏 - 헬스 운동일지 운동기록 운동루틴 다이어트 (7089); 짐워크 - 헬스 홈트 운동일지 운동기록 루틴 다이어 (3439)|

Takeaways [inference]:
- Hevy is #1 for the main localized term in DE, FR, ES, MX, IT and BR, and each of those storefronts has a localized title.
- In PL, CZ, TR and UA the local-language terms are fragmented: weak apps, low rating counts and no major tracker localized. Competition is easier there, but so is the demand signal.
- JP and KR are dominated by local apps and are not UI languages, so they are excluded.

## 4. Top charts: Health & Fitness (genre 6013)

`https://itunes.apple.com/<cc>/rss/topfreeapplications/limit=200/genre=6013/json` and `…/topgrossingapplications/…`. The feed returns 100 entries. This is a single snapshot from 2026-10-19 [data].

|Store|Top Free H&F: tracked apps (rank/100)|Top Grossing H&F: tracked apps (rank/100)|Other gym/strength-like apps in Top Grossing|
|---|---|---|---|
|us|Ladder #3, Fitbod #26, Hevy #34, Lyfta #49, Liftoff #86|Ladder #2, Fitbod #20, Gymverse #39, Hevy #43, Liftoff #54, Strong #66, Lyfta #91|Muscle Booster Workout Tra #58; FORM: Strength, Pilates, G #68|
|gb|Hevy #8, Ladder #47, Lyfta #52, Liftoff #65, Fitbod #87|Ladder #9, Hevy #17, Fitbod #20, Strong #31, Liftoff #49, Gymverse #71, Lyfta #72|TrainingPeaks: Plan Train  #28; EvolveYou: Strength For Wo #36; Gymproluxe #59|
|ca|Hevy #9, Lyfta #12, Ladder #17, Fitbod #43, Liftoff #46|Ladder #3, Fitbod #12, Hevy #26, Liftoff #45, Lyfta #48, Strong #72, Gymverse #84|Muscle Booster Workout Pla #58; Muscle Monster Workout Pla #62; EvolveYou: Strength For Wo #67|
|au|Hevy #4, Lyfta #16, Ladder #32, Fitbod #62, Liftoff #69, Strong #88, Boostcamp #96|Ladder #5, Hevy #16, Fitbod #20, Lyfta #24, Strong #40, Gymverse #42, Liftoff #46|TrainingPeaks: Plan Train  #35; EvolveYou: Strength For Wo #82; Muscle Monster Workout Pla #97|
|de|Hevy #17, Lyfta #35, Liftoff #70|Hevy #29, AlphaProg #39, Ladder #46, Lyfta #60, Fitbod #69, Liftoff #76, Strong #78|Gymondo Fitness, Pilates,  #48; Fitness App—Gym Workout, S #58; GYMKY - Fitness & KI Ernäh #99|
|at|Lyfta #11, Hevy #15, Liftoff #47, Strong #62|Lyfta #18, Hevy #22, AlphaProg #45, Strong #48, Liftoff #77, Ladder #94|GYMKY - Fitness & KI Ernäh #28; MWH: Pilates Sculpt Streng #36; Centr: Strength & Fitness  #58; Gymondo Fitness, Pilates,  #89; Fitness App—Gym Workout, S #91|
|ch|Lyfta #13, Hevy #18|Hevy #34, AlphaProg #53, Liftoff #57, Strong #60, Lyfta #62, Fitbod #71, Ladder #98|EvolveYou: Strength For Wo #48; Gymax Muskelaufbau Planer #91|
|fr|Hevy #22, Lyfta #35, Liftoff #51|Liftoff #32, Hevy #42, Lyfta #49, Fitbod #63, Ladder #87|Muscle Booster - Musculati #52; Fitness & Exercice Muscula #58; FizzUp - Fitness & Muscula #68|
|be|Lyfta #17, Hevy #23, Liftoff #55|Ladder #37, Hevy #40, Lyfta #48, Liftoff #86|TrainingPeaks: Plan Train  #25; MyFitCoach - Workout Plann #56; ChillFit: Home Workout Pla #66; EvolveYou: Strength For Wo #82|
|es|Hevy #6, Lyfta #35, Fitbod #75, Liftoff #91|Hevy #7, Lyfta #30, Fitbod #44, Ladder #51, Gymverse #75, Strong #89|Symmetry: Gym Tracker con  #9; Gymtone - Rutinas de gimna #56; SmartGym: Gym & Home Worko #92|
|pt|Hevy #12, Lyfta #13|Hevy #14, Lyfta #25, Fitbod #29, Ladder #69|Befit: Plano e Treino Acad #13; EvolveYou: Strength For Wo #62|
|it|Hevy #17, Lyfta #21|Hevy #20, Lyfta #24, Fitbod #86|Allenamento a casa e pales #22; MWH: Pilates Sculpt Streng #78; Befit: Scheda Palestra Fit #93|
|nl|Hevy #6, Lyfta #23, Liftoff #93, Strong #98|Hevy #22, Fitbod #28, Lyfta #29, Ladder #45, Strong #65, Liftoff #72|TrainingPeaks: Plan Train  #27; EvolveYou: Strength For Wo #46; Gymax: Muscle Workout Plan #88|
|se|Lyfta #13, Hevy #23, StrengthLog #28, RepCount #51, Liftoff #68, Fitbod #85|StrengthLog #5, Lyfta #24, Fitbod #32, Hevy #37, Liftoff #63, Ladder #66, RepCount #75, Strong #83|TrainingPeaks: Plan Train  #54; MyFitCoach - Workout Plann #96|
|pl|Hevy #9, Lyfta #13, Liftoff #69|Lyfta #26, Hevy #27, Fitbod #59, Liftoff #61, Ladder #75|Gym Workout App & Fitness  #23; TrainingPeaks: Plan Train  #48; MyFitCoach - Workout Plann #50; Workout Tracker - SmartWor #51; Fitness Planner Gym・Workou #65|
|cz|Lyfta #8, Hevy #14, Liftoff #74|Lyfta #14, Liftoff #19, Hevy #23, Gymverse #86, Ladder #96|GymRat Fitness Workout Tra #20; TrainingPeaks: Plan Train  #27; SHRED: Gym & Home Workouts #34; Caliber: Strength Training #49; EvolveYou: Strength For Wo #89|
|br|Hevy #36, Fitbod #98|Hevy #19, Fitbod #54|Befit: Plano e Treino Acad #6; GymRats · Desafio fitness #14; Gym WP - Treino Academia #20; SmartGym: AI, Treino, Acad #44; Muscle Booster Treino acad #70|
|mx|Hevy #29, Fitbod #50, Liftoff #51|Hevy #19, Fitbod #24, Ladder #57, Gymverse #90|Symmetry: Gym Tracker con  #12; Befit: Rutinas Gym y Ejerc #51; Gymax: Entrenamiento Muscu #76; Gymtone - Rutinas de gimna #81; Ejercicio en casa, fitness #86|
|tr|Hevy #48|Liftoff #24, Hevy #56, Ladder #60, Fitbod #83|Muscle Monster Workout Pla #35; Gym Workout App & Fitness  #43; Befit: Gym Workout Tracker #49; Gymwork: Workout Tracker L #70; TrainingPeaks: Plan Train  #79|
|ua|Hevy #37, Lyfta #84|Hevy #30, Fitbod #55, JEFIT #60, Liftoff #96|Gym Workout App & Fitness  #16; Fitness Planner Gym・Workou #57; Workout Planner MuscleFit #66; Gymtone - Gym Workout Plan #70; TrainingPeaks: Plan Train  #76|
|kz|Hevy #55|Hevy #32, Lyfta #39|Gymtone - Gym Workout Plan #9; Gym Workout App & Fitness  #14; Gymaholic: Workout Tracker #53; TrainingPeaks: Plan Train  #77; Muscle Monster Workout Pla #89|
|jp|—|Liftoff #45|Gymwork(ジムワーク) - 筋トレ記録＆分析 #6; 自宅ワークアウト: 筋トレ, フィットネスアプリ #17; 筋トレ記録・管理で継続＆習慣化 - バーンフィット #29; 最強の筋トレ管理アプリ-筋トレMEMO #32; ダイエットアプリOWN.筋トレとカロリー&PFC管理 #40|
|kr|Hevy #97|Stronglifts #40, Hevy #44, Gymverse #86, Fitbod #91|플랜핏 - 운동 루틴 추천과 헬스 홈트 다이어트 #1; 짐워크 - 헬스 홈트 운동일지 운동기록 루틴 다 #2; 플릭 - 운동일지, 운동기록, 운동일기, 운동루 #14; 핑크다이어리-생리 배란 임신 헬스케어 앱 #18; 라이즈 - 운동기록 운동일지 헬스장 루틴 피트니 #23|

Takeaways [inference]:
- Strength trackers reach **Top Grossing** in DE, AT, CH, ES, PT, IT, NL, SE, PL, CZ and BR, which shows people in those markets pay for trackers.
- Hevy's grossing rank is strongest in ES (#7), PT (#14), GB (#17), AU (#16), BR and MX (#19) and IT (#20).
- Lyfta (28 languages) ranks high in AT, CZ, PL and CH, which points to localization paying off in smaller markets.
- TR and UA Top Grossing is led by generic “Gym Workout App” planners rather than trackers.

## 5. Storefront ↔ localization mapping (affects keyword space)

Official source: Apple, *App Store localizations* (App Store Connect Help), <https://developer.apple.com/help/app-store-connect/reference/app-store-localizations/>, fetched 2026-10-19.

| Storefront | Default language | Additional languages |
|---|---|---|
| United States | English (US) | Arabic, Chinese (Simplified), Chinese (Traditional), French, Korean, Portuguese (Brazil), Russian, Spanish (Mexico), Vietnamese |
| United Kingdom | English (U.K.) | — |
| Canada | English (Canada) | French (Canada) |
| Australia | English (Australia) | English (U.K.) |
| Germany / Austria | German | English (U.K.) |
| Switzerland | German | English (U.K.), French, Italian |
| France | French | English (U.K.) |
| Belgium | English (U.K.) | Dutch, French |
| Spain | Spanish (Spain) | Catalan, English (U.K.) |
| Portugal | Portuguese (Portugal) | English (U.K.) |
| Italy | Italian | English (U.K.) |
| Netherlands | Dutch | English (U.K.) |
| Sweden | Swedish | English (U.K.) |
| Poland | English (U.K.) | Polish |
| Czechia | English (U.K.) | Czech |
| Türkiye | English (U.K.) | Turkish |
| Ukraine | English (U.K.) | Russian, Ukrainian |
| Brazil | Portuguese (Brazil) | English (U.K.) |
| Mexico | Spanish (Mexico) | English (U.K.) |
| Kazakhstan | English (U.K.) | — |

**Industry view on keyword indexing (conflicting):**
- Sonar describes the practical US setup as English (US) + Spanish (Mexico), giving about 200 keyword characters. It also warns against replacing English keywords in es-MX: <https://trysonar.app/blog/app-localization-keep-home-rankings-intact>.
- Mobile Action and AppFollow say all of the US additional locales count, up to about 10× the keyword space: <https://www.mobileaction.co/blog/app-store-cross-localization/>, <https://appfollow.io/blog/app-store-optimization-localization>.
- Asodesk keeps a cross-localization table: <https://help.asodesk.com/app-store-localizations>.
- **Treat anything beyond es-MX in the US as unverified and test it** [inference].

Implications [inference]:
- **es-MX, pt-BR and French** (all in the UI pool) each serve their home market *and* add US keyword space.
- **English (U.K.)** adds a second keyword field in nearly every European and LatAm storefront at no translation cost.
- **Russian** is also a US additional locale. That is a technical option, but see the brand note below.
- Polish, Czech, Turkish and Ukrainian product pages are only *additional* in their own storefronts. Users with English device settings still see the English (U.K.) page there.

## 6. Price sensitivity: Hevy Pro prices per storefront [data]

Source: `https://apps.apple.com/<cc>/app/id1458862350`, “In-App Purchases” section, fetched 2026-10-19. Hevy appears to use two monthly price points (legacy and current). Both are shown.

| Store | Monthly | Yearly | Lifetime |
|---|---|---|---|
| us | $2.99 / $3.99 | $23.99 | $74.99 |
| gb | £2.99 / £3.99 | £23.49 | £74.99 |
| de, fr, es, it, nl, pt | €3.49 / €4.49 | €26.49 | €89.99 |
| pl | 14,99 / 22,99 zł | 117,99 zł | 429,99 zł |
| cz | 89 / 119 Kč | 679 Kč | 1 990 Kč |
| br | R$12,90 / R$20,90 | R$99,90 | R$429,90 |
| mx | MX$59 / MX$79 | MX$479 | MX$1,899 |
| tr | ₺19,99 / ₺29,99 | ₺159,99 | ₺3.999,99 |
| ua | 2,99 / 4,99 USD | 23,99 USD | 89,99 USD |

Lightweight's planned $4.99/mo and $29.99/yr sit above Hevy in the US. Eurozone storefronts carry Euro prices at or above US nominal levels. BR, MX and especially TR are cut sharply [inference].

## 7. Public market-size data (cited; not independently verified)

| Fact | Source / date |
|---|---|
| The US captured **more than half** of global H&F consumer spending in 2024. The UK was second with **8%**. 2024 H&F downloads were **3.6B** (+6% YoY). 2025 global H&F IAP was forecast to pass **$4B**. The report covers “23 markets”, but no other country shares are on the public page. | Sensor Tower, *State of Mobile Health & Fitness 2025*, Feb 2025: <https://sensortower.com/blog/state-of-mobile-health-and-fitness-in-2025> |
| 2025 H&F IAP of about **$4.5B** (+13%) and downloads of about **3.96B** (+0.8%), attributed to Sensor Tower [secondary] | Voxbooster summary, 2026: <https://voxbooster.com/blog/fitness-app-statistics-2026> |
| North America “still drives over half of subscription revenue”, and Europe’s share held steady. Median one-year H&F install LTV is about $1.20, the highest category. Europe is now the most expensive region for subscriptions. Price index (US=1, apparently): UK/FR/DE/IT/ES 1.2, TR 0.7. **DE is 4.4× TR for H&F annual plans.** Country LTVs listed include UK $23.6, US $19.9 and MX $17.6. | Adapty, *State of In-App Subscriptions 2026* (2025 data): <https://adapty.io/state-of-in-app-subscriptions-report/> |
| Adapty 2025 edition: US **48.9%** and Europe **24.8%** of in-app subscription revenue [secondary, via search snippet] | <https://uploads.adapty.io/state_of_in_app_subscriptions_2025.pdf> |
| H&F has the highest median revenue per install: **$0.63** at 60 days in the 2025 report and **$0.48** at 14 days in the 2026 report. The two windows are not comparable. Only 5% of H&F apps reach $10k in two years [secondary] | RevenueCat *State of Subscription Apps*, via <https://athletechnews.com/fitness-apps-monetizable-winner-take-all-or-most/> |
| German fitness-app market about €121M, per a Statista Digital Market Outlook infographic. The year was not visible, so treat it as outdated [secondary] | <https://de.statista.com/infografik/amp/24676/umfrage-zur-nutzung-von-fitness-apps> |

No free public source gave per-country H&F revenue for DE, FR, ES, BR, PL, TR or UA. Sensor Tower, data.ai (now Sensor Tower) and Statista country pages are paywalled. The country ranking above therefore relies on the proxies in §2–§4 plus regional pricing.

## 8. Team advantages and risks [inference]

- **Ukrainian:** native copy costs almost nothing and supports authentic PR and community seeding. Revenue potential is low: small proxy, USD pricing in a stressed economy, and English (U.K.) is the default page.
- **Russian:** it is a UI language and a US additional locale (extra keywords), and it is additional in UA. However, the Russia storefront has payment constraints (Apple suspended some payment methods in 2022; verify the current status), and Hevy is not offered there. A Ukrainian team marketing in Russian is a positioning decision for the owner. I do not recommend a Russian product page as a priority.
- **8-language exercise content:** EN, UK, ES, IT, TR, RU, PL and FR are already translated, which lowers the cost of ES, FR and IT pages. **German and pt-BR are not in the exercise-content set**, so check whether the exercise library displays in those languages before marketing them (open question).
- The Apple Watch angle and native iOS fit high-ARPU markets (DE, GB, CH, NL, Nordics) better than price-sensitive ones [inference].

## 9. Open questions

1. Does the exercise library ship in German, Dutch, Portuguese and Czech at release? The UI is localized, but the exercise content list covers 8 languages without DE, NL, PT or CS.
2. Is regional pricing planned (Apple's auto-equalized tiers vs custom), especially for BR, MX and TR?
3. Can the owner accept a Russian-language product page, for US keyword space only? This is a brand decision.
4. Test plan: after launch, verify that es-MX, pt-BR and FR keywords rank in the US storefront, since the industry sources disagree.
