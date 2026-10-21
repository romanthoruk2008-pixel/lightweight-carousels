# Harda — App Store screenshots v3 (2026-10-21)

Produced by a multi-agent run: 5 research agents (Cal AI, competitor full sets A/B, mascot + AI-feature apps, best practices + reviews), 3 independent strategies, 3 judges, synthesis, 3 adversarial checks (feature truth, Apple rules, copy), final fix.

Owner corrections included: no swap sheet (swipe on exercise → catalog → pick → replaced); AI button at the top of the workout/editor (type or say a change → workout reworked).

## Strategy
**How the plans were weighed.** Totals across the three judges:

| Plan | ASO | User | Brand | Total |
|---|---|---|---|---|
| A | 7.6 | 7.5 | 8.0 | 23.1 |
| C | 7.3 | 6.5 | 8.4 | 22.2 |
| B | 6.4 | 6.0 | 7.4 | 19.8 |

Plan A stays the base. Two of three judges picked it, and it puts three things in the search results that none of the 9 leaders in `aso/research/screenshots.md` shows in its first 3 screenshots.
- **Plan C supplies the craft:** short verb headlines with one orange word, one hero pop-out, input → output with pill labels, and AI framed around equipment.
- **Plan B supplies the discipline:** numbers that add up, nothing that reads as a weight recommendation, and an honest list of gaps.

**What v4 changes after review**
- **Only shipping UI.** Every string drawn as app UI comes from the submitted build: roast lines, kick card, push text, button labels, AI output, parser output and plan output. If a line is wanted, it goes into the app first and then gets captured.
- **No sync claim.** Nothing says or shows that a set logged on the Watch appears live on the iPhone until that is verified.
- **Search-trio headlines rewritten** for thumbnail size and non-native readers:
  - "Log every set. Beat last time."
  - "Have a program? Bring it in."
  - "Say what changed. The workout adapts."
- **Data fixed** so real captures can't contradict the slides. Today's 145 × 8 bench is the PR, and the history climbs to it. Week buckets are no longer hand-made. One counting rule covers warm-ups.
- **Unverified promises removed:**
  - "You stay in charge"
  - "See how it's done" and "step-by-step"
  - "kick whoever's skipping"
  - "Skip leg day. Seryozha will notice."
  - the swap checkmark
  - Plank's timed sets
  - the injury test
- **Premium disclosure.** The description puts an asterisk on every AI feature the screenshots show. Captures come from a Premium-entitled account with no upsell UI.
- **Sourced stats.** Every statistic is either sourced to a repo file or marked "unverified (plan research, not in repo)".

**The search trio** (the only screens most searchers see)
1. **What it is.** "Log every set. Beat last time." A workout tracker for iPhone and Apple Watch; the PREVIOUS column shows the benefit.
2. **Why it's better.** "Have a program? Bring it in." A notebook page goes in and editable routines come out. CSV history is on subhead line 2.
3. **Why now.** "Say what changed. The workout adapts." You type or say "Hotel gym. Dumbbells only." and the routine is reworked, and you can edit anything afterwards.

Three things keep the category obvious: the app name "Harda: Gym Workout Tracker", the live logging screen, and "Workout tracker" in the slot 1 subhead. "workout tracker" has Apple popularity 53, the only checked term with real volume (`keyword-metrics.md`).

**After the trio**
- 4: Gym Bro (friends)
- 5: Progress and PRs
- 6: Build a plan (beginners)
- 7: Swipe to replace
- 8: Seryozha (on hold until his trigger and line are confirmed)
- 9: Exercise instructions
- 10: Programs, folders, parity chips and integration badges

**Conflicts resolved**
1. **Slots 2 and 3:** import in 2, AI rework in 3. Import is a one-time action with lower AI-skeptic and paywall risk. The reverse order is A/B Test 2 T1.
2. **AI example:** an equipment request ("Hotel gym. Dumbbells only.") on the Push Day routine in the editor, not on today's live barbell workout, so it doesn't contradict slot 1.
   - No injury or pain wording anywhere, including tests. The preference variant "Skip overhead pressing today." is a test that runs only after owner sign-off.
   - Voice is confirmed in the product facts, so the mic stays, drawn exactly as the real UI draws it.
3. **Slot 1 Watch:** the Watch shows its own real screen at the same moment (rest before set 4). It does not show the same set ticked on both devices, and there is no sync cue. Gate: if the phone and the Watch don't share the live workout, the Watch leaves slot 1.
4. **Seryozha:**
   - Peeks from behind the phone in slot 1, at 15% of frame height or less, tested against a clean version.
   - One hero slot (8).
   - Never next to AI, import, plan or Gym Bro.
5. **Friends headline:** "Different gyms. Same streak.", pending the owner's sign-off that it survives the planned rule change. Fallback: "Train with friends. Keep a streak."
6. **Replace headline:** "Squat rack taken? Swipe to replace." The word "swap" is used only if the app itself uses it.
7. **Import visual:** the notebook hero plus three parser pills. The CSV card is cut: CSV history is a separate import and must not point into "Review detected routines". CSV moves to subhead line 2 and the description.
8. **Watch slots:** the Watch appears in slot 1 and in its own Watch set. If fewer than 4 real Watch screens exist, ship fewer Watch screenshots.
9. **No parity slide:** warm-ups appear in slot 1. Supersets, drop sets and lb/kg go in a footer chip strip in slot 10 and in the description.
10. **Beginners:** the plan slot (with a "Beginner" chip) and the instructions slot both stay.
11. **App preview:** launch without one.

**Hard gates before any frame is designed** (details in open questions)
- Every in-UI string exists in the submitted build.
- How a live workout behaves across the Watch and the iPhone is verified (slot 1, Watch set, preview).
- A final Free vs Premium list exists for every featured item. It decides the description asterisks (guideline 2.3.2).
- Seryozha's real trigger is confirmed and a clean line ships in the build (slot 8).
- The Strava integration is approved for public use and the official badge file is in hand (slot 10).
- Captures come from a Premium-entitled demo account with no upsell banners, allowance counters, or lock or crown icons.
- Before upload, every frame is text-searched, including small UI text, for "free", "trial", "$", "Premium", "Pro", "unlock" and lock glyphs.

**Template for all 10 frames**
- **Canvas:** 1320×2868, also exported at 1206×2622. Dark background (#141513).
- **Headline:** at the top in white Rubik Bold, at most 7 words and 2 lines, with exactly one orange word (#F26445). In the search trio each line is about 19 characters or fewer, so all three set at the same size.
- **Subhead:** Rubik Medium at about 60% white, at most 2 lines and 50 characters.
- **Devices:**
  - Latest-generation iPhone and Apple Watch bezels from Apple Design Resources, unaltered.
  - Pop-outs may overlap the screen or sit in front of a device, but nothing alters, grips or bends a bezel.
  - A device may bleed off the canvas.
- **Pop-outs:** one hero pop-out cluster per frame, meaning one element plus its own thin-line annotation pills. Two explicit exceptions:
  - the slot 10 footer;
  - the slot 1 Seryozha peek, which sits behind the phone and is A/B tested.
- **Inside the phone:** annotations stay outside the phone. Inside it, only real captured UI appears; touch indicators are allowed (2.3.3).
- **Status bar and locale:** status bar 9:41 with full signal, Wi-Fi and battery. US English, lb/in.
- **Names, units and glyphs:** exercise names, units and glyphs (×, -15, sec, heart-rate format) are copied exactly from the real UI. Overlay copy writes sets × reps as "4 × 8"; "5x5" appears only as a program name.
- **Banned in every frame:**
  - "free", a price, a trial or "Premium"
  - ratings or user counts
  - profanity
  - Strava, except through the official badge

**Master demo dataset (US, lb).** Every frame uses it, and every number shown is a real capture from a seeded account.

*People and dates*
- Today is Wed Oct 21, 2026. If captures happen on another day, shift every date so the pattern holds.
- The user is Alex, avatar "A".
- The friend is Sam, a second real demo account. Shared streak: the real counter value after the two accounts share workouts. The target is 24, and the number is never faked.
- The folder "My PPL" is imported from the notebook page, whose headings read "Push day / Pull day / Leg day" so the parser's names match. History comes in through a CSV seed file built from this dataset, Aug 31 – Oct 19.
- Rotation, Mon/Wed/Fri: Oct 2 Pull, Oct 5 Legs, Oct 7 Push, Oct 9 Pull, Oct 12 Legs, Oct 14 Push, Oct 16 Pull, Oct 19 Legs, Oct 21 Push (today). October has 9 workouts including today.

*Canonical exercise names.* These are placeholders: replace each with the library's exact string and use that string in every UI, pill, card and caption.
- Push: Bench Press (Barbell), Incline Dumbbell Press, Overhead Press, Lateral Raise, Cable Fly, Triceps Pushdown
- Pull: Deadlift (Barbell), Lat Pulldown, Cable Row, Face Pull, Dumbbell Curl
- Legs: Squat (Barbell), Romanian Deadlift, Leg Press, Leg Curl, Standing Calf Raise

*Push Day: 6 exercises, 19 sets (1 warm-up + 18 working)*
- **Bench Press (Barbell):** W + 4 sets. No set above 135 lb anywhere in the history.
  - Oct 7: 95×10, 135×8, 135×8, 135×7, 135×6.
  - Oct 14 (shown as PREVIOUS): 95×10, 135×8, 135×8, 135×8, 135×7.
- **Incline Dumbbell Press:** 3 sets. Oct 7: 45×10, 10, 10. Oct 14: 50×10, 10, 9.
- **Overhead Press:** 3×8 @ 95.
- **Lateral Raise:** 3×12 @ 20.
- **Cable Fly:** 3×12 @ 30.
- **Triceps Pushdown:** 2×12 @ 50.

*Today: slot 1 and the Watch set, during the rest before bench set 4*
- Logged: W 95×10 ✓, set 1 135×8 ✓, set 2 145×8 ✓, set 3 145×8 ✓. Set 2 is a new PR on every metric. Set 4 is next.
- Rest 2:29 of 2:30. Heart rate 128.
- About 14 min elapsed, shown in the app's real duration format.
- The finished Push Day keeps its real duration (about 58 min).

*One counting rule.* VERIFY whether warm-ups count, then use one column everywhere.

| Where | Warm-ups counted | Warm-ups not counted |
|---|---|---|
| Slot 1 header | 4 of 19 sets · 4,350 lb | 3 of 18 sets · 3,400 lb |
| Finish summary, W2, W4-alt, preview | 19 sets | 18 sets |
| Watch set label | same label as the phone row it refers to | same |

If the app's format allows it, prefer "4 of 19" to "4/19", which reads as a date to US eyes.

*Pull Day: 5 exercises, 15 sets*
- Deadlift (Barbell) 3×5: Oct 2 255, Oct 9 265, Oct 16 275 (PR).
- Lat Pulldown 3×10 @ 120.
- Cable Row 3×10 @ 110.
- Face Pull 3×15 @ 40.
- Dumbbell Curl 3×12 @ 25.

*Leg Day: 5 exercises, 17 sets*
- Squat (Barbell) 4×5: Oct 5 205, Oct 12 215, Oct 19 225 (PR).
- Romanian Deadlift 3×8 @ 185.
- Leg Press 3×10 @ 270.
- Leg Curl 3×12 @ 90.
- Standing Calf Raise 4×12 @ 135.

*Expected personal records.* VERIFY which PR types the app tracks (heaviest weight, e1RM, set volume) and re-check after seeding.
- Bench Press (Barbell) 145 lb × 8 · Oct 21
- Squat (Barbell) 225 lb × 5 · Oct 19
- Deadlift (Barbell) 275 lb × 5 · Oct 16

*No longer hand-specified:* total and weekly volume, chart bars and the radar shape all come from the capture.

*Other personas:* the plan-builder slot uses a separate unnamed beginner account. No demo account has progress photos.

*Capture order*
1. Seed the CSV history.
2. Slot 9: exercise detail, captured before today's workout.
3. Slot 2: notebook import.
4. Start Push Day and log through set 3, then capture slot 1 and the Watch set.
5. Finish the workout, then capture slots 5 and 10.
6. Start Leg Day and capture slot 7 (swipe on Squat → catalog → Hack Squat). Discard, restart, log 5 sets, capture the slot 8 sheet, then discard.
7. Slot 6 on the beginner account.
8. Slot 4 from the Alex/Sam pair.
9. Slot 3 last: run the AI rework on Push Day, capture it, then revert.

**Description**

*Opening* (mirrors the slides, a Cal AI tactic):

"Harda is a workout tracker for iPhone and Apple Watch.
1) Log every set with last session's numbers beside it.
2) Bring the program you already have from paper, a screenshot, text or voice[*], plus your workout history via CSV from any app that exports it.
3) Say what changed and Harda reworks the workout.*"

*Then add:*
- "On Apple Watch: start a workout, log sets and see your heart rate." This makes no standalone claim, and Apple requires the description to say what the app does on Apple Watch.
- A parity list: warm-up sets, supersets, drop sets, rest timer, kg/lb and cm/in, 13 languages, works with Apple Health, and Strava only if approved.
- One neutral footnote: "*AI features are part of Harda Premium, an auto-renewable subscription. A small number of AI requests each month is included for everyone."
- "Harda doesn't give medical advice."
- Terms of Use (EULA) and Privacy Policy links at the end of every localization (3.1.2).

*Asterisks* go on every Premium item the screenshots show:
- the AI rework (certain);
- import from screenshot, photo, text or voice, and Build a plan, if they use the AI allowance;
- the Watch, if it is gated.

*Launch carousel lines* ("Bring that plan into Harda", "You'll open your workout tracker every time you train…") belong in the description and social posts, not in the screenshots.

**Чесно для власника**

**Заміна вправи.** Окремого шиту заміни немає, і на скринах його теж немає.
- Слот 7 показує реальний флоу: свайп по вправі → каталог → обираєш вправу → вона автоматично замінюється.
- Заголовок тепер «Swipe to replace». Слово «swap» беремо, лише якщо так написано в самому застосунку.
- AI-кнопка зверху має окремий слот 3: запит «Hotel gym. Dumbbells only.» у редакторі Push Day, і тренування переробляється.
- Травми й болю не показуємо ніде, навіть у тестах. У тесті максимум «Skip overhead pressing today.», і лише з твого дозволу.

**Що змінилося після рев'ю**
- **Лише те, що є в білді.** Репліки Серьожі, текст kick-картки й push-сповіщення, підписи кнопок, а також результат AI, парсера й генератора плану беремо зі справжніх знімків. Якщо рядка в застосунку немає, спершу додаємо його туди, потім знімаємо.
- **Годинник.** Не показуємо, що підхід «синхронізувався», поки не перевіримо, що підхід із годинника одразу з'являється на iPhone. Якщо телефон і годинник не ведуть одне живе тренування, годинник іде зі слота 1 у власний набір скринів.
- **Контроль над AI.** Фразу «You stay in charge» прибрали: не перевірено, чи можна скасувати результат AI. Замість неї «Edit anything after.»: routines редагуються, це підтверджено.
- **Слот 8 на паузі.** Чекаємо, доки ти підтвердиш, на що саме реагує Серьожа, і доки в білді з'явиться чиста репліка.
- **Рекорд жиму тепер сьогоднішній (145 × 8).** Інакше справжній знімок показав би інший PR, ніж слот 5. Заодно це виконує обіцянку «Beat last time».
- **Premium.** Слова «Premium» на скринах немає, тому в описі зірочка стоїть на кожній AI-функції, яку показують скрини. Знімаємо з Premium-акаунта без банерів, лічильників і замків.
- **Strava.** Значок ставимо, лише якщо інтеграцію відкрито для всіх. Нові застосунки в Strava API мають ліміт атлетів до перевірки, тож без схвалення значок обіцяв би підключення, яке більшість не зможе зробити.
- **Заголовки трійки** переписано під мініатюру в пошуку й під людей, для яких англійська не рідна.

**Що реально продає** (джерела: файли в `aso/research/`)
1. **Перенесення своєї програми.**
   - У відгуках люди частіше переходять з нотаток, паперу й таблиць, ніж з іншого застосунку. Тема «notes / paper / spreadsheet / CSV»: Hevy 6, Strong 8, StrengthLog 18, Alpha 10 згадок (`reviews.md`).
   - Прямий запит на імпорт трапляється один раз (Strong).
   - Жоден з 9 лідерів не показує імпорт у перших 3 скринах (`screenshots.md`).
   - Чесно: про CSV-імпорт у відгуках не пише ніхто, хвалять лише CSV-експорт. Тому CSV у нас заспокійливий рядок, а не головний аргумент.
2. **Apple Watch.**
   - Strong: 45 згадок, з них 20 у відгуках на 1–2★, переважно збої синхронізації й утрачені підходи.
   - Alpha (10 згадок) і Dropset (4 з 28 відгуків): найчастіший запит.
   - Жоден з 9 лідерів не показує годинник у перших трьох скринах.
3. **AI-переробка за запитом.**
   - Fitbod: 17 згадок AI, з них 8 у відгуках на 1–2★. Люди злі, коли AI сам змінює тренування. Strong хвалять за «No AI BS».
   - Тому продаємо контроль, а не «AI-тренера».
   - Важливо: Fitbod на 3-му скрині показує вибір обладнання (пікер). Тож казати «ніхто не підлаштовує тренування під обладнання» не можна. Наша різниця в тому, що зміну кажеш своїми словами.
4. **Gym Bro.**
   - Hevy: 20 згадок про друзів і спільноту, жодної у відгуках на 1–2★. У Strong просять додати друзів.
   - Про стріки й «kick» у відгуках не пише ніхто, тож спільний стрік — наша гіпотеза. Test 2 її перевірить.
5. **База, яка мусить бути бездоганною, хоч сама й не продає.**
   - Легкість запису — найчастіша похвала в усіх 6 застосунках.
   - Прогрес і PR: Hevy 33, StrengthLog 28 згадок. Програми: StrengthLog 31, Alpha 29.
   - Сюди ж таймер, план для новачка й інструкції до вправ.
6. **Серьожа.**
   - Робить бренд упізнаваним, але даних «за» чи «проти» немає: у вибірці 778 відгуків про 6 застосунків без маскотів, тож ця тема там не виникає.
   - Цифру «0 згадок у 600 відгуках» з попередньої версії в репозиторії не знайдено, тому її прибрали.
   - Отже, він лише визирає в слоті 1 і має один свій слот.

**Що не перевірено**
- Цифри й приклади про Ladder, Gravl, Thelo, Saga, GymRoast, Duolingo, BitePal і Cal AI прийшли з попередніх планів.
- Так само позиції скринів після 3-го (Fitbod #9, Gymverse #4, Gravl #6).
- У репозиторії їх немає: у `reviews.md` 6 застосунків (без Ladder), у `screenshots.md` 9 застосунків і лише перші 3 скрини.
- Позначені «не перевірено», і рішень на них не будуємо.

**Чого бракує, щоб продавати сильніше.** У конкурентів це є; ми цього не заявляємо; кандидати в роадмап:
- **Підказка ваги чи прогресії.** В Alpha прогресію згадують 54 рази. Наша чесна заміна поки що — «Beat last time».
- **Таймер на заблокованому екрані (Live Activity) і віджет.** Через Live Activity люди йшли зі Strong до Hevy.
- **Калькулятори дисків, 1RM і розминки:** Strong (3-й скрин), Boostcamp (3-й скрин).
- **Відео або анімації вправ:** Strong (2-й скрин, «video instructions»).
- **Видимий експорт CSV.** Його хвалять у відгуках, і це сигнал, що ми не тримаємо користувача в пастці.
- **Перевірена робота годинника без iPhone.** Тоді з'явиться заголовок «Leave your phone in the locker.»
- **Рейтинг.** Його не намалюєш. Просимо оцінку системним запитом Apple у хороший момент: новий PR або завершене тренування.

**Cal AI** (спостереження з попередніх планів, у репозиторії не задокументовано)
- **Взяли:** однаковий шаблон, короткі дієслівні заголовки з одним помаранчевим словом, один «герой» поза рамкою, «вхід → результат» із пілюлями-підписами, перші рядки опису в порядку скринів.
- **Не взяли:** лічильники користувачів, лаври, рейтинги, before/after тіла, «free», лого замість продукту на першому скрині, демо-цифри, що не сходяться.

## Screens
### 1. Log every set. Beat last time.
*Workout tracker for iPhone and Apple Watch.*

**Goal:**
What it is. Within a one-second search glance: a gym workout tracker for iPhone and Apple Watch that puts last session's numbers next to every set so you can beat them.

**Visual:**
**Text:** headline at the top in two lines, "Log every set." / "Beat last time.", with "Beat" in orange. The headline must carry the frame on its own: in search results app UI text renders at about 3–4 pt and can't be read.

**iPhone:**
- Latest-generation bezel from Apple Design Resources, unaltered.
- Left of centre, about 75% of canvas width.
- Zoomed so the Bench Press card fills most of the visible screen. The bottom may bleed off the canvas.

**Apple Watch (the one pop-out):**
- Latest-generation bezel, unaltered, at roughly real proportion (about 50% of the phone's width).
- In front of the phone at the lower right. It overlaps only the phone's right margin and the next-exercise card, and may bleed off the canvas's right edge.
- Never covers the set rows, the PREVIOUS column, the header stats or the rest bar.
- No arrow, glow or label links it to a phone row.

**Seryozha (an exception: he sits behind the phone):**
- Head and one eye rise from behind the phone's top-right edge, with no fingers on the bezel.
- At most 15% of frame height, eye looking down at the PREVIOUS column, no speech bubble.
- Removed in Test 1 T1.

**Nothing else:** no badges, no arrows, no "synced" styling.

**Gate:** VERIFY that the phone and the Watch show the same live workout. If they don't, drop the Watch from this frame (use the Test 1 T3 layout) and keep it to the Watch set.

**UI text and data:**
**Status bar:** 9:41.

**Header:** "Push Day" · about 14 min elapsed, in the app's real labelled duration format (e.g. "Duration 14:06" or "14 min"; never a bare clock next to 9:41) · [Finish].

**Stats:**
- "4 of 19 sets · 4,350 lb" if warm-ups count; "3 of 18 sets · 3,400 lb" if they don't.
- The same rule applies everywhere (see the dataset). Use the app's real format.

**Exercise card:** "Bench Press (Barbell)" · "Rest 2:30".

**Columns:** SET | PREVIOUS | LB | REPS | ✓ (use the real labels).

| Set | Previous | lb | Reps | ✓ |
|---|---|---|---|---|
| W | 95 × 10 | 95 | 10 | ✓ |
| 1 | 135 × 8 | 135 | 8 | ✓ |
| 2 | 135 × 8 | 145 | 8 | ✓ |
| 3 | 135 × 8 | 145 | 8 | ✓ |
| 4 (next) | 135 × 7 | empty | empty | |

- **Set 2 is a new PR on every metric.** If the app marks PRs during the workout, keep its real PR marker on that row; it pays off the headline. If it doesn't, add none.
- **Row 4** shows only the app's real placeholders.
- **No row** is marked as synced or as coming from the Watch.
- Below the rows: "+ Add Set".

**Next card:** "Incline Dumbbell Press · 3 sets · Previous 50 × 10".

**Rest bar:** "Rest 2:29 · Next: Bench Press (Barbell), Set 4" · "-15" "+15" "Skip", exactly as rendered.

**Watch:** its real screen at the same moment, during the rest before set 4.
- **Screen:** the rest timer if the Watch has one; otherwise the set-4 entry screen.
- **Heart rate:** 128, in the app's real format.
- **Set label:** matches the phone's row label.
- **Pre-filled values:** if set 4 is pre-filled with values that differ from both PREVIOUS (135 × 7) and the last logged set (145 × 8), show it empty instead, so nothing reads as a recommendation.
- **Check mark:** no tapped ✓.

**Typos to fix:** "Dumbbell", not "Dumbell".

**Seryozha:**
Peek only, from the 2204 art. He rises from behind the phone's top-right edge: at most 15% of frame height, curious face, no fingers on the bezel, no speech bubble, covering no data. The clean variant is Test 1 T1.

**Features claimed:**
Workout logging: sets, reps, weight, warm-up sets; Previous session's numbers shown inline next to each set; Rest timer (-15/+15/Skip, shows next set); Apple Watch app during a workout: log sets, heart rate (no live sync and no standalone use claimed); Personal records (only if the app marks them during the workout)

**Reuses frame:**
2204, modified:
- New headline and subhead.
- kg → lb, with all data from the dataset. Header numbers match the visible rows under one counting rule.
- Elapsed time in the app's labelled duration format.
- The Watch moves off the rest timer and "+ Add Set" to the lower right at real proportion. It shows its own screen for the same moment, replacing the contradicting "Set 2 of 4, 60 kg, 10:09".
- Seryozha's peek moves behind the phone: 15% of frame height or less, no fingers on the bezel, covering no data.
- "Dumbell" typo fixed.

2210's duplicate of this screen is retired.

**Why:**
**Clarity:**
- Screen 1 almost always shows the core logging or plan UI: Hevy, Strong, StrengthLog, Fitbod, Dropset and HeavySet (`screenshots.md`, pattern 1).
- "workout tracker" has Apple popularity 53, the only checked term with real volume (`keyword-metrics.md`).

**Headline:**
- "Log every set." names the unit that "Log it." left unnamed and matches description line 1. Its lines are balanced at 14 and 15 characters.
- "Beat last time." turns the PREVIOUS column into a promise. That is our honest stand-in for the next-weight suggestions we don't have.
- Today's PR on set 2 makes the promise true in the data.

**The Watch:**
- Strong has 45 Apple Watch mentions in 150 recent reviews, 20 of them 1–2★, mostly sync problems and lost sets (`reviews.md`).
- An Apple Watch app is the most common request at Alpha (10 mentions) and Dropset (4 of 28 reviews).
- None of the 9 leaders shows a Watch in its first 3 screenshots (`screenshots.md`, pattern 6).
- Apple allows showing the app on another Apple platform when that is part of the experience (`apple-rules.md` 5.4).

**No sync or standalone claim:** the Watch shows its own state at the same moment. Nothing says a set travelled between devices or that the Watch works without the iPhone. Given Strong's sync complaints, an unverified sync promise is the most damaging thing we could overclaim.

**Subhead:** "The" is dropped. It implied "the one", an unverifiable claim, and could read as the official Apple Watch tracker. "for iPhone and Apple Watch" is Apple's referential form.

**Seryozha's peek:**
- It is the only brand distinctiveness in the search trio, and the owner likes it.
- It sits behind the phone, not on the bezel.
- It is tested first (Test 1).

### 2. Have a program? Bring it in.
*Paper, screenshot, text, voice. Plus CSV history.*

**Goal:**
Why it's better, part 1. Remove the switching cost for the searcher whose program lives in notes, on paper or in another app, and show that their history can come too.

**Visual:**
**Text:**
- Headline at the top in two lines, "Have a program?" / "Bring it in." (15 and 12 characters), set at the same size as slots 1 and 3.
- Only "Bring" is orange.
- Subhead line 2, "Plus CSV history.", sits on its own line.

**Notebook page (the hero pop-out):**
- A real photographed spiral-notebook page with a handwritten program, light paper tilted about −6°.
- Upper-left, bleeding past the canvas's left edge and tucked behind the phone.
- It is the only light element in a row of dark search thumbnails.

**Pills (part of the hero cluster):** three white pills on thin orange leader lines run from three handwritten lines toward the phone, outside it. Their text is the parser's real output.

**Phone:** latest-generation bezel, unaltered, right of centre, about 65% of canvas width. It shows the real "Review detected routines" capture.

**Cut:**
- The CSV card and its arrow. CSV history is a separate import and must not point into the routines review.
- The coach-chat screenshot.
- The voice-note card.

**Rules:** no competitor UI, no real names, no Seryozha.

**UI text and data:**
**Handwritten page:** headings are written so the parser names the routines the way the rest of the set does.
- "Push day: Bench 4x8 / Incline DB 3x10 / OHP 3x8 / Lat raise 3x12 / Cable fly 3x12 / Pushdown 2x12"
- "Pull day: Deadlift 3x5 / Lat pulldown 3x10 / Cable row 3x10 / Face pull 3x15 / DB curl 3x12"
- "Leg day: Squat 4x5 / RDL 3x8 / Leg press 3x10 / Leg curl 3x12 / Calf raise 4x12"
- No weekdays and no weights on the page.

**Pills (placeholders until the parser runs):**
- "Bench Press (Barbell) · 4 × 8"
- "Incline Dumbbell Press · 3 × 10"
- "Overhead Press · 3 × 8"

**Phone:** "Review detected routines" with the parser's real cards. Expected:
- "Push Day · 6 exercises"
- "Pull Day · 5 exercises"
- "Leg Day · 5 exercises"

The screen shows:
- only the counters and status lines the app really displays;
- the real edit affordance on each card;
- the real primary button (VERIFY, e.g. "Save routines").

No set counts appear on the cards.

**Before design:**
- Run this exact page through the build, by camera or photo picker, whichever the app really uses.
- Copy the routine names, exercise names and pill text from the real output.
- If the parser names the routines differently, use its names in every frame.

**Seryozha:**
None (import must not read as the mascot's or an AI coach's work).

**Features claimed:**
Bring existing program: import from a photo of paper, a screenshot, text or voice into editable routines ready to start; 'Review detected routines' screen; CSV import of full workout history from any app that exports CSV (subhead only)

**Reuses frame:**
2207, modified:
- Headline shortened, with only "Bring" orange. New subhead.
- The collage is cut to the notebook photo (hero) with three parser pills.
- Removed: the orphan "CSV history import" label, the coach screenshot and the voice-note card.
- The phone gets the real "Review detected routines" capture for the PPL page.
- All sources are fictional and checked for typos.

**Why:**
**Nobody in our sample shows it:** none of the 9 leaders shows import or switching in its first 3 screenshots. Boostcamp's "Ditch the spreadsheet" (#2) is the closest (`screenshots.md`).

**Where people come from (`reviews.md`):**
- Reviewers describe switching from notes, paper and spreadsheets more often than from another app.
- The "CSV / spreadsheet / notes / paper" theme has 6 mentions at Hevy, 8 at Strong, 18 at StrengthLog and 10 at Alpha.
- Quotes: "i was using notes app before" (Hevy) and "say goodbye to planning workouts in my notes app" (StrengthLog).
- There is one explicit import request: "the inability to import workouts … is about to make me jump ship" (Strong).

**Honest limit:** no review mentions CSV import; CSV export is what gets praised. So CSV is a reassurance line, not the hero.

**Headline:**
- "Already have a program?" (23 characters) would wrap to 3 lines or need type about 35% smaller than its neighbours.
- "Have a program? Bring it in." sets at the same size and has one orange word. "Bring it in" can't be misread as "bring it on".
- The owner's original stays as Test 4 T1.

**Visual:** notebook → routines gives Cal AI's "snap → result" in one frame. Cutting to one input fixes the density all three judges raised.

**Premium status:** if photo, screenshot, text or voice import uses the AI allowance, item 2 of the description gets the asterisk (2.3.2).

### 3. Say what changed. The workout adapts.
*Type or say it. Edit anything after.*

**Goal:**
Why now. The plan meets real life in one sentence. Show user-started, user-controlled AI editing, without an AI-coach persona or medical framing.

**Visual:**
**Text:** headline at the top in two lines, "Say what changed." / "The workout adapts." (17 and 19 characters), with "Say" in orange.

**Phone:**
- Latest-generation bezel, unaltered, upright and centred.
- Shows the Push Day routine in the routine editor after the rework (real capture), not today's live workout.

**Pop-out (the hero):**
- A real capture of the input state that appears after tapping the top AI button (sheet, field or dictation UI, whichever is real), with the request typed.
- Enlarged past the phone's edges.
- Mic icon only as the real UI draws it.
- The pop-out shows the input state; the phone shows the result state.

**Pills (part of the cluster):** left of the phone and outside it: two pills and a "+2 more" pill on thin orange leader lines to the changed rows.

**Inside the phone:** only real UI. Orange change bars or highlights appear only if the app draws them.

**Do not show:**
- "AI" in the headline.
- A sparkle, unless it is on the real button.
- Chat bubbles or a coach persona.
- Seryozha.
- "Premium", unless the 2.3.2 fallback is triggered.

**UI text and data:**
**Request:** "Hotel gym. Dumbbells only." plus the real send control (and the mic, if shown). VERIFY the button label and placeholder.

**Header:** "Push Day · 6 exercises".

**Expected list** (sets × reps, no weights on changed rows; replace with the real output):
1. "Dumbbell Bench Press · 4 × 8" (changed)
2. "Incline Dumbbell Press · 3 × 10"
3. "Seated Dumbbell Shoulder Press · 3 × 8" (changed)
4. "Lateral Raise · 3 × 12"
5. "Dumbbell Fly · 3 × 12" (changed)
6. "Overhead Dumbbell Triceps Extension · 2 × 12" (changed)

**Pills** (exact names from the output):
- "Bench Press (Barbell) → Dumbbell Bench Press"
- "Cable Fly → Dumbbell Fly"
- "+2 more"

**Optional status line** (e.g. "4 exercises changed"): only if the app shows one.

**Before design:** run this exact request on the current build against the seeded Push Day. Capture it last, then revert the routine so slot 1 is unaffected.

**Seryozha:**
None (next to AI he would read as an AI coach; owner rule).

**Features claimed:**
AI edit: button at the top of the workout/editor where you type or say a change and the workout is reworked (Premium with a monthly allowance; asterisk in the description only); Editable routines / routine editor

**Reuses frame:**
New frame. Needs real captures of the AI input UI and its output on the seeded Push Day.

**Why:**
**The gap, stated precisely:**
- None of the 9 leaders shows typed or spoken workout changes in its first 3 screenshots (`screenshots.md`).
- Fitbod does show equipment customisation at #3 (an equipment picker), so never claim we are the only app that adapts to equipment. The difference is that you say it in your own words.
- Unverified (plan research, not in repo): later-slot and non-leader examples (Gravl, Thelo, Saga) and Fitbod's reported injuries feature. Never claim "first" or "only".

**Control, not a coach:**
- Fitbod has 17 AI mentions in 150 recent reviews, 8 of them 1–2★ ("AI ruining another app…"). Strong fans praise "No AI BS" (`reviews.md`).
- Here the user starts the change, and the subhead says they can edit anything afterwards, because routines are confirmed editable.
- "You stay in charge" comes back only if a confirm or undo step is verified.

**Headline:** "Just say what changed." gave a thumbnail reader no noun. "The workout adapts" names what changes in plain words; "reworks" is uncommon for non-native readers.

**Equipment, not injury:**
- The request is universal (travel, home, a busy gym) and has no medical implication.
- It is shown on the routine, not on today's barbell session, so it doesn't contradict slot 1.

### 4. Different gyms. Same streak.
*Train with friends. Share workouts, send a kick.*

**Goal:**
Social accountability that works for beginners and women too: a friend, a shared streak, a nudge. No feed, no competition.

**Visual:**
**Text:** headline at the top, with "streak" in orange.

**Phone:** latest-generation bezel, unaltered, upright, showing Alex's real friends screen. Two avatars joined by a flame and the streak counter sit at top centre, with the kick card below.

**Pop-out:**
- A real captured iOS notification banner, received on Alex's device after Sam's demo account sends a kick.
- It floats above the phone's top-right, slightly larger than the phone UI.
- It arrives to the viewer, so the nudge reads as friends nudging each other.

**Removed:**
- Seryozha's kick from 2206.
- Shared-workout rows, unless the app has a real per-friend view that can't be mistaken for a feed.

**Do not show:** a leaderboard, comparisons, chat or a feed.

**UI text and data:**
**Tab title:** the label in the build being submitted ("Community" now, "Gym Bro" later). Small, never in the headline.

**Avatars:** "You" (orange monogram "A") and "Sam".

**Streak:**
- A flame plus the real counter from the two demo accounts (target 24), with the app's real label (e.g. "Shared streak").
- No rules or units unless the app shows them.

**Kick card:**
- "Give Sam a kick", the body text and [Kick], each exactly as the shipping string. VERIFY each one, including the body.
- Drop "That streak isn't going to survive on excuses." unless it ships.

**Notification:** the app display name exactly as iOS renders it · "now" · "Sam gave you a kick." VERIFY the real push text.

**Optional rows** (only if this is a real per-friend view):
- "You · Push Day · Today"
- "Sam · Leg Day · Tue"

**Seryozha:**
None.

**Features claimed:**
Gym Bro: friends; Share finished workouts (subhead); Shared streak (rules not described); 'Give a kick' nudge via push notification

**Reuses frame:**
2206, modified:
- New headline (the original stays as fallback) and new subhead.
- Sasha → Sam. Streak 59 → the real counter (target 24).
- "X" avatar → "A".
- Seryozha's kick removed.
- A real notification banner "Sam gave you a kick." added.
- Tab label taken from the shipping build.

**Why:**
**Gap in our sample:** none of the 9 leaders shows friends, streaks or nudges in its first 3 screenshots. HeavySet only mentions sharing routines in a caption (`screenshots.md`).

**Reviews (`reviews.md`):**
- Hevy's social/friends theme has 20 mentions, none of them 1–2★: "A friend and I use it every time we workout to hold each other accountable".
- Strong users ask to add friends.
- No review mentions streaks or nudges. The two-person streak is our hypothesis, not proven demand; Test 2 T2 measures it.

**Why slot 4:** it is the first frame after the trio, so a friend-trainer sees it without deep scrolling.

**Headline:**
- Short, ironic and true under today's rule.
- Needs the owner's sign-off that it survives the planned rule change. Fallback: "Train with friends. Keep a streak."

**Subhead:** avoids "whoever's skipping", which implied the app detects skipping, and that is a rule.

**Seryozha removed:** the dino must never be read as the "gym bro".

**Banner direction fixed:** over Alex's phone, the banner must be one Alex receives.

### 5. Your progress has receipts.
*Personal records, volume and every lift logged.*

**Goal:**
Table stake: progress is measured, and the headline's promise of PRs is visibly kept with today's record.

**Visual:**
**Text:** headline at the top, with "receipts" in orange. This is the owner's voice. The slot is outside the search trio, so the slang is acceptable, and the subhead spells out "Personal records".

**Phone:** latest-generation bezel, unaltered, upright. It shows the real Statistics capture from the seeded account: the chart, the muscle balance radar, and the Explore Progress grid partly visible.

**Pop-out:** today's real Personal record card, breaking past the phone's left edge.

**Chart:**
- Whatever the real chart shows.
- Prefer a period or metric whose last bar is complete (VERIFY the options).
- If the current calendar week is partial and therefore lower, keep the app's own styling. Never recolour it orange or hand-draw bars.

**Do not show:**
- Body photos, before/after, or a compare slider.
- Anything but an icon or empty state on the Progress photos tile.

**UI text and data:**
**Header:** "Statistics" · the real period label (e.g. "This Month") · tabs "Volume / Duration / Reps".

**Totals:** as captured. Expect "9 workouts" in October. Volume is whatever the app computes, with thousands separators.

**Personal records** (expected; VERIFY the PR types):
- "Bench Press (Barbell) · 145 lb × 8 · Oct 21"
- "Squat (Barbell) · 225 lb × 5 · Oct 19"
- "Deadlift (Barbell) · 275 lb × 5 · Oct 16"

**Pop-out card:** "Personal record · Bench Press (Barbell) · 145 lb × 8 · Oct 21", in the app's real PR styling.

**Muscle balance radar:** the app's real axes and shape, with no hand-tuning.

**Tiles:** Calendar, Records, Measurements, Progress photos. Use the real names, and seed no photos.

**Formatting:** thousands separators. No August dates under a "This Month" label.

**Seryozha:**
None.

**Features claimed:**
Statistics (volume/duration/reps chart); Personal records; Muscle balance radar; Calendar, body measurements, progress photos (as grid tiles)

**Reuses frame:**
2208, modified:
- Real Statistics capture from the seeded account.
- PR list with today's bench PR, plus a popped PR card.
- Explore Progress grid trimmed; the Progress photos tile is empty.
- Headline kept; subhead spells out "Personal records".
- "Last Month" and August labels removed.

**Why:**
**Table stake:**
- Progress/PR analytics appear by screen 3 for nearly every leader: Hevy, StrengthLog, Gymverse, HeavySet, Alpha and Boostcamp (`screenshots.md`).
- Progress and PRs is a top praise theme: Hevy 33, StrengthLog 28, Alpha 24 mentions (`reviews.md`).
- Without it the page looks thin.

**What this fixes:**
- 2208's headline promised PRs the screen didn't show, and its period labels contradicted each other.
- In v3, today's 145 × 8 would have beaten the Oct 7 bench PR (155 × 5) on e1RM and set volume, so a real capture would have contradicted the slide.
- Today's PR also pays off slot 1's "Beat last time".

**Weekly buckets:** v3's Oct 1–7/8–14/15–21 were Thursday–Wednesday spans. A real calendar-week chart on Wed Oct 21 has a partial current week, so the chart now comes from the capture.

**Copy:** "receipts" is the owner's ironic voice, so it stays. The alternative "Proof you're getting stronger." goes to the owner.

**What it avoids:** body transformation imagery (2.3.14) and invented numbers.

### 6. No plan? Get one that fits.
*Built around your goal, schedule and gear.*

**Goal:**
Win beginners (including women new to the gym) and anyone without a program: a plan built from their own answers, including moves to skip.

**Visual:**
**Text:** headline at the top, with "fits" in orange.

**Answer chips (the pop-out cluster):** left of the phone, six chips styled like the real onboarding answers, stacked, with one orange line into the phone.

**Phone:** latest-generation bezel, unaltered, showing the real generated plan with Day 1 expanded and the real Start button.

**Do not show:**
- Seryozha.
- "AI" wording.
- Weights in the plan, so nothing implies a recommendation.

**UI text and data:**
**Chips** (use the real onboarding wording): "Get stronger" · "Beginner" · "3 days a week" · "45 min" · "Gym" · "Skip: overhead pressing". Use the app's real Avoid/Skip label.

**Phone** (expected; replace with the real output): "Your plan · Full Body · 3 days a week".
- "Full Body A" expanded:
  - Goblet Squat 3 × 10
  - Dumbbell Bench Press 3 × 10
  - Lat Pulldown 3 × 10
  - Dumbbell Romanian Deadlift 3 × 10
  - Cable Crunch 3 × 12 (a rep-based core move; Plank is removed because timed sets aren't confirmed)
- "Full Body B" and "Full Body C" collapsed.
- [Start] (real label).
- No overhead pressing anywhere, matching the chip.

**Persona:** a separate unnamed beginner account, same units.

**Before design:** generate the plan on the build with these exact answers, and use its real title, day names, exercises and labels.

**Seryozha:**
None (plan generation must not read as Seryozha's work; owner rule).

**Features claimed:**
Build a plan: personalized plan from onboarding answers (goal, experience, days/week, duration, place, equipment, priorities, exercises/movements to avoid)

**Reuses frame:**
New frame.

**Why:**
**Beginner signal:** Fitbod and Gymverse both lead with "built for you" plus answer chips that lead to a ready plan (`screenshots.md`):
- Fitbod #1: "SMART WORKOUTS BUILT FOR YOU".
- Gymverse #2: "WORKOUTS BUILT AROUND YOU", with "Choose Goal / Muscle Focus / Equipment" chips.

**Reviews (`reviews.md`):**
- Beginners praise generated plans at Fitbod ("I had no direction and I feel like Fitbod really put me on the right path").
- At Alpha they praise the plan generator and call it the "Best App for Beginners".
- Unverified (plan research, not in repo): the Ladder figures and the Hevy "workout log, not a training program" quote.

**The "Beginner" chip** speaks to the persona every judge found under-served.

**"Skip: overhead pressing":** shows limitation-aware planning as a preference, not medical handling (owner rule: no medical promises).

**Subhead:** shortened to fit 2 lines. The chip carries the skip idea.

**Premium:** if plan generation uses the AI allowance, the description puts an asterisk on it.

### 7. Squat rack taken? Swipe to replace.
*Pick another exercise and keep going.*

**Goal:**
Manual control alongside AI. The busy-gym moment, solved with the real flow: swipe on the exercise → the exercise catalog opens → pick one → it's replaced.

**Visual:**
**Text:** headline at the top, with "Swipe" in orange. Use "swap" only if the app's own wording is "swap" (owner to confirm).

**Pop-out (the hero):**
- The real "Squat (Barbell)" row, captured from the Leg Day workout and lifted above the phone.
- Shown mid-swipe in the real direction (VERIFY), with a touch-indicator dot and a short arrow (an overlay allowed under 2.3.3).
- Joined to the phone by a curved orange line.

**Phone:** latest-generation bezel, unaltered. It shows the real exercise catalog as it opens from that swipe, with a tap indicator on "Hack Squat".

**Cut:** the "Hack Squat ✓" after-card. Elsewhere in the set, ✓ means a logged set.

**Do not show:**
- A swap sheet.
- A "suggested alternatives" list or a same-muscle filter, unless the catalog really has them.
- "AI" or Seryozha.

**UI text and data:**
**Lifted row:** "Squat (Barbell)" with the real row content. Show "4 sets · Previous 225 × 5" only if the row displays them.

**Catalog:** the real title (VERIFY), with "squat" typed in the search field. Alternatively, a real "Legs" filter with the field empty.

**Rows:** every row must match "squat" and exist in the library. VERIFY names, tags and thumbnails.
- "Hack Squat" (tapped)
- "Goblet Squat"
- "Smith Machine Squat"
- "Bulgarian Split Squat"
- Muscle and equipment tags and muscle-image thumbnails appear only as the real list shows them.

**After the tap:** nothing is drawn; the subhead tells the rest. Whether sets, weights and reps carry over is an open question, not a claim.

**Seryozha:**
None.

**Features claimed:**
Replace an exercise: swipe on it in the workout, the exercise catalog opens, pick a new one, it replaces automatically; Exercise library (catalog with search)

**Reuses frame:**
2210, repurposed:
- Drop its duplicate workout screen.
- Its headline "Finish a set. Log it. Go again." is kept as a backup line.
- Reuse the frame shell and phone position.
- New real captures of the Leg Day row and the catalog.

**Why:**
**Correction:** the owner confirmed there is no swap sheet. v2's swap sheet is gone, and the real flow is shown with the owner's own verb ("заміниться" = replace).

**Precedent:** the swapping slides at Fitbod #9, Gymverse #4 and Gravl #6 are unverified (plan research, not in repo). `screenshots.md` covers only the first 3 screenshots.

**Headline:** names the situation and the real action in one line. "All the benches are taken. Of course." stays as the owner-voice backup.

**Data:**
- Leg Day keeps slot 1's bench data untouched and reuses the 225 × 5 squat PR from slot 5.
- Every result contains "squat", so the list matches its query. Leg Press is out: it doesn't match "squat" and is already in Leg Day.

**Bonus:** the catalog covers the exercise-library table stake.

### 8. Seryozha has opinions about short workouts.
*Clean roasts, never about looks. Mute him anytime.*

**Goal:**
Brand character: a dino who reacts to what you do, never how you look. 4+-safe and mutable. The memorable difference after trust is earned. On hold until his real trigger and a shipped clean line are confirmed.

**Visual:**
**Status: on hold.** Design only after all three of these are true:
1. The owner confirms that finishing early really triggers a roast.
2. A clean line of 10 words or fewer ships in the build.
3. The "Finish Leg Day?" sheet and its labels are captured.

If the confirmed trigger is something else (long rests, missed days), the headline and the phone change to show that trigger.

**Template:** headline at the top, with "opinions" in orange.

**Phone:** latest-generation bezel, unaltered, smaller (about 60% of frame height), right of centre. It shows the real "Finish Leg Day?" sheet.

**Seryozha (the hero pop-out):**
- Large: 35–40% of frame height, bottom-left.
- In front of the phone's lower-left corner, without touching the bezel.
- 2211 pose with dumbbells or arms crossed, side-eyeing the sheet.
- Never covers "5 of 17".

**Speech bubble:** one, with the shipped line exactly.

**Mute chip:** only with the real setting label.

**Must look nothing like Gymverse's T-Rex.**

**UI text and data:**
**Sheet:** "Finish Leg Day?" · "5 of 17 sets done" · [Keep going] [Finish]. VERIFY all labels and the count format (the counting rule applies).

**Bubble:** the shipped line only.
- Preferred candidate for the owner to add: "Leaving already? The squat rack misses you." Its irony is unmistakable.
- Don't use "Leaving after 5 sets? Bold." Many non-native readers take "Bold." as praise, and the count would have to be dynamic.

**Optional chip:** e.g. "Seryozha's roasts · On" (real label only).

**Bans:**
- No profanity, not even masked.
- No body, looks or identity jokes.
- No word "free".
- Never called "gym bro".

**Seryozha:**
Hero of this slot, and his second and last screenshot appearance (slot 1 peek, slot 8, plus the icon). Pose and side-eye carry the attitude, with one shipped line about behaviour only. Spelling (Seryozha / Seriozha) is locked before final art.

**Features claimed:**
Mascot Seryozha who occasionally roasts the user; Roasts are filtered (no profanity) and can be muted; Finish workout flow

**Reuses frame:**
2211, modified:
- Headline moved to the top and rewritten; subhead rewritten.
- "Finish Push day? 6 of 19" → "Finish Leg Day? 5 of 17 sets done" (real capture).
- The profane bubble is replaced with a shipped clean line.
- Seryozha resized to 35–40% of frame height and kept off the bezel and the numbers.
- Spelling locked before final art.

**Why:**
**Headline:**
- "Skip leg day. Seryozha will notice." had four problems:
  - it claimed an unverified trigger (skipped days);
  - it turned "occasionally" into "always";
  - it read as advice to skip;
  - it didn't match the sheet, which shows leaving early, not skipping.
- "Has opinions about short workouts" is declarative (only slots 2, 6 and 7 stay questions) and matches the sheet. "Opinions" honestly allows for "occasionally".
- Alternatives for the owner: "Cut leg day short? Seryozha has notes." and 2211's "Comes with a dinosaur who notices."

**Subhead:**
- "Clean" is confirmed by the profanity filter.
- "never about looks" needs the owner's confirmation that every line avoids body, looks and identity. Fallback: "Clean roasts only. Mute him anytime."
- Muting is confirmed; the setting's label isn't.

**Placement:**
- A late, dedicated character slot tied to a visible trigger reads as a feature.
- The Duolingo, BitePal and GymRoast placements are unverified (plan research, not in repo).
- Our review sample (778 reviews of 6 apps without mascots, `reviews.md`) says nothing for or against mascots. The earlier "0 mentions in 600 reviews" figure couldn't be traced and was dropped.

**What this fixes in 2211:**
- The profanity, which breaks 2.3.8: screenshots must be 4+ even if the app is rated higher.
- A "Leg day" headline over a Push day sheet.

### 9. Know the move before you lift.
*Instructions, target muscles and your history.*

**Goal:**
Reassure beginners that they'll know how to do each movement, and give lifters per-exercise history.

**Visual:**
**Text:** headline at the top, with "move" in orange. It is declarative, which breaks the run of question headlines.

**Phone:** latest-generation bezel, unaltered, upright, showing the real exercise detail page.

**Pop-out:** the real muscle-image card, enlarged past the phone's right edge, in its real colours (not recoloured orange).

**History:** visible below the instructions.

**Do not show:** a video player, play icon or any animation cue (none exists).

**UI text and data:**
**Title:** "Incline Dumbbell Press".

**Muscles:** as the real taxonomy shows them. Expected: primary "Upper chest"; secondary "Front delts", "Triceps".

**Instructions:** the real app copy, in its real format. Say "step-by-step" nowhere unless they are numbered steps.

**History** (captured before today's workout):
- "Oct 14 · 50 lb × 10, 10, 9"
- "Oct 7 · 45 lb × 10, 10, 10"
- These match slot 1's "Previous 50 × 10".

**Seryozha:**
None.

**Features claimed:**
Exercise library with instructions; Muscle images; Per-exercise history

**Reuses frame:**
New frame.

**Why:**
**Technique slides:**
- Strong's #2 is "Hundreds of built in exercises, with video instructions…", and Hevy's #3 shows a "How to" tab (`screenshots.md`).
- Beginners reach Hevy and StrengthLog through exercise demos and free programs. The exercise-library theme has 18 mentions at StrengthLog and 15 at Alpha (`reviews.md`).
- Unverified (plan research, not in repo): the "5 of 8 competitors" count and the Ladder "clueless idiot" quote.

**Honesty:**
- "See how it's done" implied a demonstration we don't have; videos and animations are on the gap list.
- "Know the move" promises understanding, which text plus muscle images deliver.
- The subhead names exactly what's there.

**For lifters:** per-exercise history (Hevy and Strong show History tabs).

### 10. Classic programs. Or your own.
*Full Body, PPL, 5x5. Organize yours in folders.*

**Goal:**
Close with completeness and honest trust: ready-made programs, your own routines in folders, parity with the set types switchers use, and real integration badges in place of social proof.

**Visual:**
**Text:** headline at the top, with "own" in orange.

**Phone:** latest-generation bezel, unaltered, upright. It shows the real Routines tab with the pinned folder, a second folder and the ready-made programs section.

**Footer below the phone (not a pop-out):**
1. A slim row of small text chips: "Warm-up sets · Supersets · Drop sets · lb / kg". Drop it if it hurts legibility; the description covers these.
2. A small Harda wordmark, then the badge row:
   - **Apple Health:** the official "Works with Apple Health" badge, unaltered: white with outline, at least 30 px, clear space of ¼ its height. If text is used instead, set it as a plain caption, never as a pill or badge shape. Never use the Apple Health heart icon or Health app imagery.
   - **Strava:** the official "Compatible with Strava" badge, unaltered, in its white or neutral variant (not orange next to our orange). Minimum size with the required clear space, smaller than the Harda wordmark and the headline. Only if the integration is approved for public use; otherwise drop it and keep Strava out of the listing.

**Do not add:** a download call to action or Seryozha.

**UI text and data:**
**Pinned folder "My PPL"** (names as imported):
- "Push Day · 6 exercises"
- "Pull Day · 5 exercises"
- "Leg Day · 5 exercises"

**Folder "Home · Dumbbells":** "2 routines" (create it in the demo account).

**Ready-made programs section:** "Full Body" · "Push Pull Legs" · "5x5". Show only programs that really ship, and VERIFY the section label.

**Badges:** "Works with Apple Health" and "Compatible with Strava" (conditional). "Strava" appears nowhere else.

**Seryozha:**
None.

**Features claimed:**
Routines, folders, pinned folders, routine editor; Ready-made programs (Full Body, Push Pull Legs, 5x5); Warm-up sets, supersets, drop sets; kg/lb switch; Apple Health integration; Compatible with Strava (only if approved for public use)

**Reuses frame:**
New frame.

**Why:**
**Table stake:**
- Routines and programs appear early for many leaders (`screenshots.md`):
  - Alpha #1: routine editor.
  - Dropset #1: routine cards.
  - HeavySet #2: routines.
  - Boostcamp: programs.
- Routines and programs is a large review theme: StrengthLog 31, Alpha 29, Strong 22 (8 of them 1–2★, mostly about the 3-template limit) (`reviews.md`).

**In place of social proof:**
- Six of the 9 leaders show awards, ratings or user counts in their first two screens. Harda has none and must not invent them (2.3.14).
- Real integration badges are honest trust markers for deep scrollers.

**Parity:** the footer chip strip reassures careful switchers without spending a whole slot.

**Strava:**
- "Compatible with Strava" is the only allowed wording.
- Strava's name must not be more prominent than ours, hence the wordmark and the neutral badge variant.
- New Strava API apps start with limited athlete capacity, so an unapproved badge would promise a connection most users can't make.

**Subhead:** "Folders for the rest" could read as folders for rest timers. "Organize yours in folders" can't.

## Apple Watch set
- Rules for every Watch screenshot:
- **Capture:** raw Watch UI only, from real captures. No bezel, no captions, and no Seryozha unless he appears in the Watch UI itself.
- **Size:** one size across all localizations, the largest App Store Connect accepts for the build (e.g. 422×514).
- **Data:** the same Push Day workout as iPhone slot 1, with the same counting rule and the same exercise names.
- **Heart rate:** one format on every frame, the app's real one (e.g. "♥ 128 BPM").
- **Claims:** nothing claims or suggests use without the iPhone, or live sync with it.
- **Never show:** Activity rings, concentric rings, Activity colours (red, green, blue) or Health app screens.
- **No A/B testing:** Product Page Optimization isn't available for Apple Watch product pages, so get these right the first time.
- **Real screens only:** build each one only from a screen that exists. If fewer than 4 exist, ship fewer rather than mock-ups.
- **Description:** the description must state what the app does on Apple Watch.
- W1. Log a set (hero, shown first).
- The explicit logged state of Bench Press (Barbell) set 3: "145 lb" / "8 reps" / heart rate / the real confirmation state (✓ or "Logged").
- The set label equals the phone's row label ("Set 3" if the phone row is "3"). Add "of N" only as the counting rule allows.
- Add "Previous 135 × 8" only if the Watch app really shows it.
- VERIFY the labels and the stepper or Digital Crown affordance.
- W2. Live workout with heart rate, only if the Watch has this screen.
- "Push Day"
- Elapsed time in the app's real format
- Heart rate 128
- A set counter only if the Watch shows one: "4 of 19" or "3 of 18", by the same rule as slot 1.
- W3. Rest timer, only if the Watch app has one (VERIFY).
- "Rest 2:29" / "Next: Bench Press (Barbell) · Set 4" / "-15" "+15" "Skip", as rendered.
- Only the app's real single-ring timer, in Harda orange. If the real UI looks like Activity rings, use W3-alt.

W3-alt, only if it exists: the in-workout exercise list. Bench Press (Barbell) with its progress, then Incline Dumbbell Press, Overhead Press, Lateral Raise, Cable Fly and Triceps Pushdown.
- W4. Start a workout.
- **If routines sync to the Watch (VERIFY):** the routine list with "Push Day · 6 exercises" highlighted and the real start button, then "Pull Day · 5 exercises" and "Leg Day · 5 exercises".
- **Otherwise:** the Watch's real start-workout screen.
- **Or, only if it exists, a finish summary:** "Push Day" / real duration / "19 sets" or "18 sets" by the counting rule / average heart rate only if shown. No volume figure.
- **Never** a sign-in screen.

## A/B tests
- Test 1, slot 1 (run first). Product Page Optimization, conversion rate, one test at a time. A new app gets little traffic, so expect long runs.
- **Control:** "Log every set. Beat last time." with the Watch and the Seryozha peek.
- **T1:** the same frame without Seryozha. Does the dino help a new brand stand out among identical dark trackers, or add clutter?
- **T2:** the headline "The workout tracker that remembers last time." with the same visual.
- **T3:** the same frame without the Watch, leaving the Seryozha peek as the only extra element. Tests whether the Watch earns its density. If the live-session gate fails, this layout becomes the control and T3 is dropped.
- **Later**, only if the owner confirms the Watch works without the iPhone: "Leave your phone in the locker." or "Log every set. Phone or wrist."
- Test 2, which reason to switch earns search slots 2–3.
- **Control:** Import (2), AI rework (3).
- **T1:** AI rework (2), Import (3). This was Plan A's original order.
- **T2:** Gym Bro friends in slot 3 (AI → 4). Tests friend accountability: Hevy's social theme has 20 mentions, none of them 1–2★ (`reviews.md`). The two-person streak itself is unproven.
- **T3:** Build a plan in slot 3 (AI → 4). Tests the beginner gap that no plan's trio covers.
- **After the test:** use the winner to build Custom Product Pages for Apple Ads keyword groups. For example, a switcher page led by import for "workout log" / "gym log", and a beginner page led by the plan for "workout plan".
- Test 3, the framing of slot 3 (only if AI stays in the first three).
PPO treatments go through review, and visitors see them before the description, so no treatment may depend on the description to be safe.
- **Control:** "Say what changed. The workout adapts." with "Hotel gym. Dumbbells only."
- **T1:** "Dumbbells only? Just say so." with the same visual. Sharper, but narrower.
- **T2:** the same headline with the request "Skip overhead pressing today." Preference wording only, with no pain or injury words. Runs only after owner sign-off.
- **Dropped:** the injury framing ("Shoulder acting up?").
- Test 4, the slot 2 headline (after Test 3).
- **Control:** "Have a program? Bring it in."
- **T1:** "Already have a program? Bring it." This is the owner's original 2207 headline; the control is preferred for width.
- **T2:** "Switching apps? Bring your CSV history." with a CSV-led visual: a "workouts.csv" card → the real CSV import result with its real count. Never "Your history comes too": CSV works only from apps that export it.

**Later candidates once traffic allows:**
- The app preview video.
- The iOS 27 search-results asset: notebook → "Review detected routines", captioned "Bring the program you already have." First confirm in App Store Connect that it can be tested.

## App preview
**Recommendation: launch without an app preview.** All three plans agree.
- A preview always takes the first search-result position and would push screenshot 3 out of the search trio.
- Evidence on video in Health & Fitness is mixed (industry reports; not verified in the repo).

Add it later only as a Product Page Optimization treatment.

**If produced:**
- 15–30 s (target 24 s), portrait 886×1920, 30 fps or less.
- Screen recordings of the current build only (2.3.4); text overlays allowed. No hands or people; touch indicators only.
- Must work muted. One caption per beat in the screenshot style (white Rubik Bold, one orange word).
- No prices, "free", "Premium", profanity or chat bubbles.
- No Watch inset unless live Watch ↔ iPhone sync is verified. Even then, drop the inset if App Review objects.
- Set the poster frame explicitly to beat 1, which must read as a workout tracker on its own. The default is 5 s, and it can't be edited after approval.
- End on a real in-app frame with a text overlay, not a separate icon or art card.

**Beats:**

**0:00–0:05**
- Push Day, Bench Press (Barbell). PREVIOUS shows 135 × 8.
- Set 3 is logged on the phone (145 × 8).
- The header ticks to "4 of 19 sets" (or "3 of 18" if warm-ups aren't counted).
- The rest bar starts at 2:30 with "Next: Bench Press (Barbell), Set 4".
- Caption: "Log every set. Beat last time."

**0:05–0:09**
- The notebook photo is picked or captured, then the real processing state.
- "Review detected routines" appears; tap the real button.
- Caption: "Have a program? Bring it in."

**0:09–0:13**
- Push Day routine editor: tap the top AI button, then type or dictate "Hotel gym. Dumbbells only."
- The list updates (real output).
- Caption: "Say what changed. The workout adapts."

**0:13–0:16**
- Leg Day: swipe Squat (Barbell). The catalog opens; tap Hack Squat and the row is replaced.
- Caption: "Squat rack taken? Swipe to replace."

**0:16–0:19**
- Friends screen with the real streak value; tap "Kick" on Sam.
- Caption: "Different gyms. Same streak."

**0:19–0:22**
- The finish summary (Push Day, real duration, 19 or 18 sets by the counting rule).
- Then Statistics with today's PR card, "Bench Press (Barbell) · 145 lb × 8".
- Caption: "Your progress has receipts."

**0:22–0:24**
- Hold on a real in-app frame, e.g. the Routines tab, with the overlay "Harda: Gym Workout Tracker · Workout tracker for iPhone and Apple Watch".
- Seryozha appears only if he is part of that real frame; no new line.

**Later reuse:** a 5–15 s cut of beats 1–2 can become the iOS 27 search-results asset once it is confirmed in App Store Connect.

## Changes vs current Figma frames
- Global (all frames):
- **Headline:** at the top, at most 7 words and 2 lines, exactly one orange word.
- **Subhead:** at most 2 lines and 50 characters.
- **Pop-outs:** one hero pop-out cluster per frame. Annotations sit outside the phone. Only shipping UI strings appear inside it.
- **Devices:** latest-generation Apple bezels, unaltered.
- **Status bar:** 9:41.
- **Data:** US lb with comma thousands separators. One dataset and one counting rule. Canonical exercise names from the library.
- **Banned:** "free", prices, "Premium", profanity.
- **Typos:** "Dumbell" → "Dumbbell", "Bench Pres" → "Bench Press", "lasy" removed.
- **Capture:** from a Premium-entitled account with no upsell UI, and text-searched before upload.
- 2204 → Slot 1:
- **Headline** → "Log every set. Beat last time." ("Beat" orange). **Subhead** → "Workout tracker for iPhone and Apple Watch."
- **Units:** kg → lb.
- **Header:** "Sets 6/18 · 1,908 kg" → "4 of 19 sets · 4,350 lb", or "3 of 18 sets · 3,400 lb" if warm-ups aren't counted. Elapsed time in the app's labelled duration format.
- **Rows:** W 95×10, 135×8, 145×8, 145×8 checked, row 4 empty, with PREVIOUS shown. A PR marker on set 2 only if the app draws one.
- **Watch:** moves off the rest timer and "+ Add Set" to the lower right at real proportion. It shows its own real screen for the same moment (rest before set 4), not the same set ticked, with no sync cue. Its old data ("Set 2 of 4, 60 kg, 10:09") goes.
- **Seryozha:** the peek moves behind the phone, at 15% of frame height or less, with no fingers on the bezel.
- 2210 → retired as a duplicate of 2204.
- Its frame shell and phone position are reused for slot 7 (swipe → catalog replace, new captures).
- Its headline "Finish a set. Log it. Go again." is kept as a backup line.
- 2207 → Slot 2:
- **Headline** → "Have a program? Bring it in." (only "Bring" orange). The original goes to Test 4 T1.
- **Subhead** → "Paper, screenshot, text, voice. Plus CSV history."
- **Collage:** cut to the handwritten notebook page as a light hero bleeding off the left edge, with 3 parser pills.
- **Removed:** the CSV card or label, the coach-chat card and the voice-note card.
- **Phone:** the real "Review detected routines" capture with the parser's names and the real button.
- 2206 → Slot 4:
- **Headline** → "Different gyms. Same streak." (the old headline stays as fallback; owner sign-off needed). **Subhead** → "Train with friends. Share workouts, send a kick."
- **Data:** Sasha → Sam; streak 59 → the real counter from two demo accounts (target 24); "X" avatar → orange "A".
- **Removed:** Seryozha's kick, and the shared-workout rows unless they are a real per-friend view.
- **Added:** a real captured iOS banner, "Sam gave you a kick." (verify the push text).
- **Kick card:** shipping strings only.
- **Tab label:** from the shipping build (Community / Gym Bro).
- 2208 → Slot 5:
- **Statistics:** a real capture from the seeded account. No hand-made weekly bars and no hand-made totals.
- **Labels:** "Last Month" and August dates removed.
- **PRs:** Bench Press (Barbell) 145×8 Oct 21, Squat (Barbell) 225×5 Oct 19, Deadlift (Barbell) 275×5 Oct 16, plus a popped PR card for today's bench PR.
- **Grid:** Explore Progress trimmed; the Progress photos tile is empty.
- **Copy:** headline kept; subhead → "Personal records, volume and every lift logged."
- 2211 → Slot 8 (on hold until the trigger and line are confirmed):
- **Headline:** moved to the top and rewritten as "Seryozha has opinions about short workouts." **Subhead** → "Clean roasts, never about looks. Mute him anytime."
- **Sheet:** "Finish Push day? 6 of 19" → the real "Finish Leg Day? 5 of 17 sets done".
- **Bubble:** the profane line is replaced with one shipped line of 10 words or fewer.
- **Seryozha:** resized to 35–40%, off the bezel and the numbers.
- New frames to design:
- **Slot 3:** AI edit. Needs real captures of the input UI and its output on the Push Day routine.
- **Slot 6:** Build a plan, from real output; Plank is replaced.
- **Slot 9:** exercise detail, with the declarative headline.
- **Slot 10:** Routines, programs, parity chips, the Harda wordmark, the Apple Health badge and the conditional Strava badge.
- **Apple Watch set:** up to 4 screens, real screens only.
- Description:
- **Opening:** mirrors the slides, with the CSV history wording separated from program import.
- **Watch line:** "On Apple Watch: start a workout, log sets and see your heart rate."
- **Premium:** asterisks on every Premium item shown, with one neutral footnote.
- **Other lines:** "Harda doesn't give medical advice." and the parity list.
- **Links:** Terms of Use (EULA) and Privacy Policy at the end of every localization.
- Instagram launch carousel:
- Its lines ("Bring that plan into Harda", "Then there's Seryozha", "You'll open your workout tracker every time you train…") go into the App Store description and social posts, not the screenshots.
- "Your gym bro can be part of it too" must refer only to the friends feature, never to Seryozha.
- No Works with Apple Health badge or Apple product images in social posts.
- Production:
- **Accounts:** seed Alex's history through Harda's own CSV import, built from the dataset. Create Sam as a second real account and a separate beginner account.
- **Capture order:** slot 9 → slot 2 → slot 1 + Watch → finish → slots 5 and 10 → Leg Day for slots 7 and 8 (discard) → slot 6 → slot 4 → slot 3 last (revert).
- **Before upload:** text-search every frame for "free", "trial", "$", "Premium", "Pro", "unlock" and lock glyphs.
- **EU set (later):** native kg numbers (e.g. 60 / 65 kg bench), not converted decimals.

## Open questions for the owner
- Жорстке правило. На скринах показуємо лише тексти, які вже є в білді, що йде на перевірку: репліки Серьожі, kick-картку, push, кнопки, результат AI, парсера й генератора плану.

Якщо потрібного рядка немає, спершу додаємо його в застосунок, потім знімаємо. Погоджуєшся?
- Free і Premium. Дай остаточний список для всього, що показують скрини:
- Чи витрачає AI-ліміт імпорт зі скрина, фото, тексту чи голосу?
- Чи є Build a plan AI-функцією або Premium?
- AI-переробка: так, це Premium.
- Чи безкоштовний Apple Watch?

Від цього залежать зірочки в описі (правило Apple 2.3.2).

Запасний план: якщо Apple відхилить за 2.3.2, додаємо маленьку мітку «Premium» біля AI-поля в слоті 3, без ціни й без «free». Ок?
- Warm-up у підрахунку. Чи рахує застосунок warm-up-підходи в лічильнику підходів і в об'ємі?

Від цього залежать слот 1, екран підсумку, годинник і відео: «4 of 19 · 4,350 lb» і «19 sets» або «3 of 18 · 3,400 lb» і «18 sets».

Який формат лічильника: «4/19» чи можна «4 of 19»? Як підписана тривалість тренування?
- Apple Watch:
- Чи з'являється підхід, записаний на годиннику, на iPhone одразу, у тому самому тренуванні?
- Чи ведуть телефон і годинник одне живе тренування?

Якщо ні, годинник прибираємо зі слота 1.

Також:
- Чи є на годиннику таймер відпочинку, екран тренування з пульсом, Previous і підсумок?
- Чи синхронізуються routines на годинник?
- Точні підписи кнопок.
- Чи заповнює годинник наступний підхід наперед, і якими числами?

Окремо: чи працює годинник без iPhone поруч?
- AI-кнопка зверху:
- Що з'являється після натискання: шит, поле чи диктування?
- Точна назва кнопки й placeholder.
- Як виглядає мікрофон саме там?
- Чи підсвічує застосунок змінені вправи?
- Чи можна скасувати або відредагувати результат? Якщо є підтвердження чи undo, повертаємо «You stay in charge».

Що реально видає AI на «Hotel gym. Dumbbells only.» для нашого Push Day?
- Імпорт:
- Камера в застосунку чи вибір фото з галереї?
- Точні підписи екрана «Review detected routines» і головної кнопки.
- Як парсер назве routines? Сторінку пишемо з заголовками «Push day / Pull day / Leg day».
- CSV-імпорт історії — окремий флоу?
- Чи показує CSV-імпорт кількість імпортованих тренувань?
- Заміна вправи:
- У який бік свайп?
- Як називається каталог? Чи є пошук і фільтри? Чи є в списку мініатюри з м'язами?
- Чи є в бібліотеці Hack Squat, Goblet Squat, Smith Machine Squat і Bulgarian Split Squat?
- Чи переносяться підходи, вага й повтори після заміни? Поки не перевірено, не заявляємо.
- Яке слово в самому застосунку: «Replace» чи «Swap»? Від цього залежить заголовок: «Swipe to replace» або «Swipe to swap».
- Gym Bro:
- Як називатиметься вкладка в білді, який подаємо?
- Точний текст push для kick.
- Точний текст kick-картки, включно з основним текстом. Чи є там «That streak isn't going to survive on excuses.»?
- Чи є окремий перегляд спільних тренувань друга?
- Чи переживе «Different gyms. Same streak.» майбутню зміну правил стріку? Запасний варіант: «Train with friends. Keep a streak.»
- Погоджуєшся замінити Sasha на Sam?
- Чи можемо зробити два демо-акаунти зі справжнім стріком (бажано 24)?
- Серьожа:
- Які реальні тригери підколок: ранній фініш, довгий відпочинок, пропущені дні?
- Які репліки до 10 слів без лайки вже є в білді? Кандидат: «Leaving already? The squat rack misses you.»
- Чи жодна репліка не стосується тіла, зовнішності чи ідентичності? Це потрібно для «never about looks».
- Як підписаний перемикач підколок?
- Остаточне написання: Seryozha чи Seriozha?

Заголовок слота 8 на вибір:
- «Seryozha has opinions about short workouts.»
- «Cut leg day short? Seryozha has notes.»
- «Comes with a dinosaur who notices.»
- Заголовки:
- Слот 2: замінюємо схвалений «Already have a program? Bring it.» на «Have a program? Bring it in.»? Він ширше читається в мініатюрі, а старий іде в Test 4.
- Слот 5: лишаємо «Your progress has receipts.» чи беремо зрозуміліше «Proof you're getting stronger.»?
- Build a plan:
- Точні підписи онбордингу: «Avoid» чи «Skip», назви цілей.
- Як виглядає екран готового плану і як там названі дні?
- Чи підтримуються підходи на час (Plank)? Поки замінили його на Cable Crunch 3 × 12.
- Статистика:
- Які періоди є?
- Як групуються тижні: пн–нд чи нд–сб?
- Чи є вигляд, де останній стовпчик — повний тиждень?
- Які типи PR рахує застосунок: найбільша вага, e1RM, об'єм підходу?
- Чи позначає PR прямо під час тренування?
- Точні назви плиток. Чи показує плитка фото прогресу лише іконку, коли фото немає?
- Вправи:
- Інструкції — це нумеровані кроки чи абзац тексту?
- Точні назви в бібліотеці, щоб використати їх скрізь: «Bench Press (Barbell)», «Squat (Barbell)», «Deadlift (Barbell)» чи інакше?
- Програми:
- Які готові програми точно є в релізі: Full Body, Push Pull Legs, 5x5?
- Як називається цей розділ?
- Інтеграції:
- Strava: чи схвалила Strava інтеграцію для публічного використання (піднято ліміт атлетів)? Чи є офіційний файл значка «Compatible with Strava» у білому чи нейтральному варіанті? Якщо ні, прибираємо Strava зі сторінки.
- Apple Health: ставимо офіційний значок «Works with Apple Health», його дозволено на сторінці App Store. Ок?
- Демо-акаунти:
- Чи можна засіяти історію Alex через наш CSV-імпорт?
- Чи можна знімати з Premium-акаунта без банерів, лічильників AI-ліміту й замків?
- Окремий акаунт новачка для слота 6.
- Якщо знімаємо не 21 жовтня, зсуваємо всі дати.
- Роадмап (чесно, щоб продавати сильніше): що з цього реально зробити до або одразу після релізу?
- підказка ваги на наступний підхід;
- таймер на заблокованому екрані (Live Activity) і віджет;
- калькулятори дисків, 1RM і розминки;
- відео чи анімації вправ;
- видимий експорт CSV;
- системний запит оцінки після нового PR або завершеного тренування.
- Відео (App Preview): погоджуєшся запускатися без нього й тестувати пізніше? Відео завжди стоїть першим і витісняє один зі скринів із результатів пошуку.
## Update 2026-10-21: owner wants three more screens (muscle distribution, ChatGPT app, Apple Watch)
Proposed 10-slot order:
1. Log every set. Beat last time. (no Watch overlay now)
2. Have a program? Bring it in.
3. Say what changed. The workout adapts.
4. Different gyms. Same streak.
5. Log sets from your wrist. — Apple Watch hero (own slot)
6. Your progress has receipts.
7. See what you're skipping. — muscle distribution radar + Seryozha bubble (merges the Seryozha slot)
8. Ask ChatGPT about your training. — Harda in ChatGPT (only if the ChatGPT app is live and public; follow OpenAI brand guidelines; keep Harda UI dominant for 2.3.3)
9. No plan? Get one that fits.
10. Squat rack taken? Swipe to replace.
Cut: standalone Seryozha slot (merged into 7), "Know the move before you lift", "Classic programs. Or your own." (covered in description).
