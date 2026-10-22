# Name, subtitle and keywords — nine more locales

Measured with Sonar (iOS), one country at a time, 2026-10-22. Same rules as
[`metadata.md`](metadata.md): no repeated words within a locale, no competitors, no "harda", no
category words (fitness, health, sports). `1rm`, `5x5` and `531` are out everywhere (owner's call,
2026-10-22): the measured coverage below still counts 1rm, so the real totals are slightly lower. `55A/45` means popularity/difficulty; `A` marks
Apple's own popularity reading, the rest are Sonar estimates.

**Every line needs a native-speaker check before App Store Connect.**

## Paste this

Names and subtitles are in sentence case. Only English capitalizes Every Word; German
capitalizes nouns anyway. Search is not case-sensitive, so this changes nothing in ranking.
The Ukrainian and Russian lines have been read; the rest still need a native speaker.

Each keyword field goes in as one line: no spaces, no line breaks.

| Locale | Name (30) | Subtitle (30) | Keywords (100) | Chars / bytes |
|---|---|---|---|---|
| Spanish (Spain) | `Harda: Rutinas gym y fuerza` | `Plan de entrenamiento y pesas` | `gimnasio,barra,ejercicios,entreno,diario,registro,bodybuilding,racha,masa,muscular,hypertrophy` | 94 / 94 |
| Italian | `Harda: Esercizi in palestra` | `Scheda allenamento e progressi` | `pesi,ripetizioni,manubri,squat,hypertrophy,bodybuilding,weightlifting,diario,forza,programma,gym` | 96 / 96 |
| Portuguese (Brazil) | `Harda: Treino de academia` | `Musculação e hipertrofia` | `ficha,perna,maromba,timer,montar,repetições,barra,ia,weightlifting,agachamento,full,body,abc` | 92 / 94 |
| Polish | `Harda: Siłownia i trening` | `Plan treningowy i dziennik` | `fbw,hypertrophy,bodybuilding,powerlifting,weightlifting,dumbbell,ai,przysiad,ćwiczenia,silownia` | 95 / 96 |
| Turkish | `Harda: Egzersiz ve antrenman` | `Vücut geliştirme programı` | `squat,gym,kas,deadlift,hypertrophy,powerlifting,bodybuilding,dumbbell,weightlifting,takibi,bro` | 94 / 94 |
| Czech | `Harda: Posilovna a trénink` | `Tréninkový plán a deník` | `fitko,hypertrophy,powerlifting,weightlifting,dumbbell,progres,dřep,cviky,bodybuilding,cvičení` | 93 / 96 |
| Ukrainian | `Harda: План тренувань` | `Спортзал, качалка і прогрес` | `hypertrophy,powerlifting,weightlifting,dumbbell,зал,bodybuilding,щоденник,спліт` | 79 / 95 |
| Russian | `Harda: Тренировки в зале` | `Спортзал, гантели и штанга` | `качок,weightlifting,качалка,приседания,bodybuilding,powerlifting,body,full` | 74 / 96 |
| Dutch | `Harda: Krachttraining schema` | `Trainingslogboek & spiermassa` | `hypertrophy,rusttimer,squat,trainingsschema,sportschool,weightlifting,trainingsdagboek,trainen` | 94 / 94 |

Cyrillic and letters such as ł, ř, ç, ğ take two bytes. Several fields are at exactly 100
bytes: read App Store Connect's counter after pasting and drop the last word if it refuses.

## Per locale

### Spanish (Spain)

- Coverage: 29 terms beyond en-GB (popularity 512, 4 targets). Name + subtitle form 10 terms (192).
- Top terms: rutinas gym 45A/50, entreno 50A/47, barra 32/37, masa muscular 24/31,
  bodybuilding 24/43, 1rm 16/20, ejercicios con pesas 13/37, entrenamiento de fuerza 13/40,
  hypertrophy 12/9, diario de entrenamiento 10/23.
- Alternatives:
  - Subtitle `Masa muscular y entrenamiento`: 2% more in total, but the title forms only 7 terms (173).
  - Name `Harda: Rutinas gym y entreno`: ties on total and puts entreno (50A) in the name; the title forms 8 terms (185).
- Why the pick: within 2% of the best total, and the most terms in name + subtitle.

### Italian

- Coverage: 27 terms (popularity 547, 6 targets). Title 9 terms (232).
- Top terms: esercizi palestra 46A/46, ripetizioni 38A/25, bodybuilding 34/40, manubri 29/21,
  weightlifting 27/32, hypertrophy 25/14, progressi palestra 25/40, allenamento palestra 25/59,
  scheda palestra 18/44, squat 17/24.
- Alternative: `Harda: Scheda palestra e pesi` / `Allenamento, serie e progressi`, with keywords
  `ripetizioni,esercizi,1rm,manubri,squat,hypertrophy,bodybuilding,weightlifting,diario,forza,programma`:
  2% more in total, 11 title terms (211).
- Why the pick: the name holds esercizi palestra, the only Italian phrase Apple measures, and
  it gives the highest title popularity. "Scheda palestra" is the classic phrase but measures 18.

### Portuguese (Brazil)

- Coverage: 25 terms (popularity 651, 9 targets). Title 9 terms (300).
- Top terms: treino academia 57A/60, montar treino 42A/63, hipertrofia 34/47,
  weightlifting 28/28, treino full body 25/37, 1rm 22/12, repetições 21/7, treino de perna 21/17,
  agachamento 21/20, maromba 20/7.
- Alternatives:
  - `Harda: Academia e musculação` / `Treino ABC e hipertrofia`: 2% more, 10 title terms (320), but it splits "treino academia" across name and subtitle.
  - `Harda: Treino academia e força`: 1% more, but reads as search terms rather than Portuguese.
- Why the pick: the strongest term (57A) sits whole in the name, in natural Portuguese.

### Polish

- Coverage: 19 terms (popularity 349, 7 targets). Title 6 terms (73). en-GB already covers
  gym 55A, gym tracker 41A and workout tracker 37.
- Top terms: silownia 44A/42, ćwiczenia 37/39, bodybuilding 29/26, weightlifting 27/30,
  hypertrophy 26/16, dumbbell 26/9, powerlifting 24/15, 1rm 23/5, fbw 13/36, przysiad 9/8.
- **Flag:** "silownia" in keywords is the name's "siłownia" without ł, on purpose: people type it
  that way (44A against 13). Apple may or may not fold ł into l. If a search for "silownia"
  finds Harda without it, swap in "siłka" (16/4).
- Alternative: `Harda: Plan treningowy i siłka` / `Trening siłowy, FBW i split`: 0.5% more,
  but siłownia leaves the name.
- Why the pick: same total, and the name carries the only Polish word Apple measures.

### Turkish

- Coverage: 20 terms (popularity 373, 7 targets). Title 6 terms (130).
- Top terms: weightlifting 29/40, squat 28/24, dumbbell 27/11, hypertrophy 25/7,
  bodybuilding 25/30, powerlifting 24/13, 1rm 22/3, deadlift 19/6, vücut geliştirme 16/50,
  kas geliştirme 14/42.
- Alternatives:
  - `Harda: Antrenman programı` / `Vücut geliştirme, set, tekrar`: 2% less, title 5 terms (74).
  - `Harda: Spor salonu programı` breaks the category rule ("spor") and adds only 1%.
- Why the pick: egzersiz (46A) is the only Turkish word Apple measures, and it's in the name.
  Turks mostly search in English ("gym" 50A), which en-GB covers.

### Czech

- Coverage: 21 terms (popularity 263, 6 targets). Title 8 terms (61). Czech-language search is
  tiny: nothing above 21. gym 49A and workout 46A come from en-GB.
- Top terms: weightlifting 25/21, dumbbell 25/6, hypertrophy 23/9, powerlifting 23/10,
  1rm 22/3, fitko 21/8, bodybuilding 15/28, trenink 13/27, progres 11/16, dřep 7/4.
- Alternative: `Harda: Fitko a posilovna` / `Tréninkový deník a progres`: same total, 5 title terms (52).
- Why the pick: same total, more title terms. Fitko is already in keywords.

### Ukrainian

- Coverage: 13 terms (popularity 291, 11 targets). Title 4 terms (92). The Russian listing adds
  4 more terms in Ukraine.
- Top terms: план тренувань 28/20, качалка 28/26, щоденник тренувань 27/15, dumbbell 26/8,
  hypertrophy 23/4, weightlifting 23/17, bodybuilding 23/36, 1rm 21/3, powerlifting 21/6, спліт 8/5.
- Alternative: `Harda: Щоденник тренувань`, same subtitle: ties, but its keyword field ends in two filler words.
- Why the pick: ties, план тренувань is the most-searched Ukrainian phrase, no filler. The top
  Ukrainian searches are off-topic: тренування вдома 54A (home) and воркаут 45A (street workout).

### Russian

- Coverage: 13 terms (popularity 399, 8 targets). Title 5 terms (188).
- Top terms: тренировки в зале 55A/45, качалка 41A/57, качок 35/30, гантели 31/23,
  приседания 30/26, full body 27/36, weightlifting 24/12, 1rm 21/3, bodybuilding 20/34,
  powerlifting 13/10.
- Alternative: subtitle `Бодибилдинг и набор массы`: ties on total, title 4 terms (138).
- Why the pick: same total, more title terms.
- **Business decision, not ASO:** the Russian listing is also read by Russian-language devices in
  Ukraine, Kazakhstan and elsewhere, and is searched in the US. Whether to sell in Russia's own
  store is separate (Pricing and Availability); App Store payments there are heavily
  restricted since 2022, so subscriptions would barely work.

### Dutch

- Coverage: 15 terms (popularity 302, 7 targets). Title 4 terms (72). en-GB covers gym 51A,
  workout 49A, gym tracker 44A, workout tracker 40A.
- Top terms: krachttraining 34/38, trainingsschema 33/32, rusttimer 30/43, weightlifting 28/35,
  hypertrophy 25/10, 1rm 24/6, trainingslogboek 24/10, trainingsdagboek 22/4, trainen 14/43, squat 12/18.
- Alternative: `Harda: Trainingsschema & gym`, same subtitle: ties, title 3 terms (66), needs a filler word ("bro").
- Why the pick: same total, one more title term, no filler. A native speaker should say whether
  "Krachttraining schema" should be written as one compound.
