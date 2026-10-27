# Поточний handoff — максимально близька адаптація референсів

## Поточна вказівка власника — 2026-10-18

**Референси є зразком для максимально близького відтворення.** Завдання — адаптувати конкретну надану карусель до Lightweight.

Зберігати максимально близько до джерела:
- тему, hook, фактичне формулювання тексту, голос, довжину й структуру пояснень;
- кількість, послідовність і призначення слайдів;
- композицію, розташування, масштаб, відступи й ієрархію елементів;
- тип, добір, пози й подачу ілюстрацій, анатомії, вправ та обладнання;
- графічні прийоми й побудову продуктового фіналу.

Погоджені зміни: акцентні кольори Lightweight і фактичний шрифт Lightweight. У продуктовій частині використовувати назву, реальні екрани й підтверджені функції Lightweight згідно з попередньою вимогою власника. Інші творчі зміни не додавати самостійно.

Не переписувати голос на власний «gym bro», не додавати жарти/roasts, нові вправи, іншу тему, новий hook або іншу композицію. Якщо текст не вміщується через шрифт — повідомити про конкретну проблему, не переписувати його мовчки.

Власник повідомив, що має дозвіл власника референсів на таке відтворення. Референси з references/CAROUSELS.md — надане ним джерело.

Напрям адаптації підтверджений; конкретний відтворений результат ще не створений/не прийнятий як master. Шрифт Lightweight — Rubik (рішення власника 2026-10-18).

Поточне доручення — записати ці правила. Генерація наступної каруселі буде окремим наступним кроком. Автоматичний QA/рецензент залишаються вимкненими; на комп'ютер власника нічого не завантажувати.

## Поточні матеріали
Сім каруселей у references/CAROUSELS.md: 61 унікальний скриншот, 62 входження через один повтор. Під час останньої перевірки всі входження зображень відкрилися у браузері; файли на комп'ютер власника не зберігалися. Оригінальні екрани апки за останнім читанням ще не додані.

## Зараз
Правила записані. Наступну карусель не генерувати до наступного завдання. Потім вибрати конкретний REF-ID, використати його тему/тексти/графіку як джерело, застосувати кольори й фактичний шрифт Lightweight та релевантний продуктовий фінал.

Claude, хмарна генерація, канал точного вставлення UI й автоматичний випуск поки не налаштовані.

## Оновлення 2026-10-18 — після розбору референсів
Розбір і патерн: references/PATTERN.md, references/analysis/. Шрифт — Rubik. Твердження джерела зберігаються дослівно. Пошук тем: docs/TOPICS.md.
Наступний крок: власник додає екрани застосунку → пілот REF-001: спершу copy.json, потім візуали. Генерацію без окремого завдання не запускати.

## Пілот LW-CAR-0001 «WEAK BACK?» (REF-007)
Пакет: carousels/LW-CAR-0001/ (brief.md, copy.json v1.0, prompts/codex-task.md). Текст 1:1; заміни — акцент #F26445, Rubik, логотип з файла власника. Codex: слайди 1 і 3 → фідбек власника → 2, 4–7. Слайд 8 заблокований до реального скриншота Lightweight і підтвердження останнього рядка.

## LW-CAR-0002 «STRUCTURE THE PERFECT PUSH DAY» (REF-001)
Пакет: carousels/LW-CAR-0002/ (brief.md, copy.json v1.0, prompts/codex-task.md). 9 слайдів у відновленому порядку. Codex робить 1–8; слайд 9 чекає реального екрана тренування Lightweight або варіанта фіналу.

## Пакети LW-CAR-0003…0005 і спільні правила
- Спільні правила для Codex: carousels/CODEX-SERIES-RULES.md (палітра, Rubik, логотип, фінал зі справжнім екраном у правильних пропорціях, збереження одним комітом).
- LW-CAR-0003 «THE ULTIMATE PULL DAY» (REF-002), 8 слайдів — готовий до генерації.
- LW-CAR-0004 «STRUCTURE THE PERFECT PULL DAY» (REF-005), 9 слайдів — 1–8 готові; слайд 9 чекає підтвердження «Personalised Plans» і трансформації Day 1 → Day 100.
- LW-CAR-0005 «BEST EXERCISES… (Push Day Edition)» (REF-004), 8 слайдів — готовий до генерації.
- LW-CAR-0002 слайд 9 розблоковано: за замовчуванням справжній екран Muscle balance.

## LW-CAR-0006 «THE MUSCLES YOU'RE FORGETTING» — власна тема
Пакет: carousels/LW-CAR-0006/. 8 слайдів, усі готові до генерації. Візуальний зразок — LW-CAR-0001 (обкладинка, мапа, список, прийнятий фінал зі справжнім екраном Muscle balance).

## LW-CAR-0007 «HOW MANY SETS DO YOU ACTUALLY NEED?» — власна тема
Пакет: carousels/LW-CAR-0007/. 8 слайдів, усі готові до генерації. Інфографічні слайди (велике число, ✓/✗, таблиця тижня, стовпчики) у стилі серії; фінал — прийнятий LW-CAR-0001 slide 8 з новим текстом. Джерела й рівень тверджень — у copy.json → claims_to_verify.

## LW-CAR-0008 «WEAK CHEST?» — власна тема
Пакет: carousels/LW-CAR-0008/. 8 слайдів, усі готові до генерації. Двійник LW-CAR-0001 (вид спереду), шаблон списку — LW-CAR-0006; у 3 з 4 слайдів варіант з власною вагою; Bonus Tip; фінал зі справжнім екраном Muscle balance.

## LW-CAR-0009 «STRUCTURE THE PERFECT LEG DAY» — власна тема
Пакет: carousels/LW-CAR-0009/. 8 слайдів, усі готові до генерації. Двійник прийнятої LW-CAR-0002 (push day); серія push / pull / legs. Фінал зі справжнім екраном Muscle balance (вісь Legs).

## LW-CAR-0010 «YOUR FIRST WEEK IN THE GYM» — власна тема для новачків
Пакет: carousels/LW-CAR-0010/. 10 слайдів, усі готові до генерації. Full body 3×/тиждень, 5 рухів, правила для новачка, фінал «Week One Done? / Now Beat It.». Усі макети — з наших прийнятих слайдів (0001, 0002, 0007).

## LW-CAR-0011 «WHAT 1 YEAR OF TRAINING ACTUALLY LOOKS LIKE» — власна тема
Пакет: carousels/LW-CAR-0011/. 9 слайдів, усі готові до генерації. Чесна версія формату CONSISTENCY: одна фігура в 4 реалістичних стадіях, сітка 156 тренувань, фінал «Your Year Starts With Workout #1.».

## LW-CAR-0012 «5 MISTAKES KILLING YOUR GAINS» — власна тема
Пакет: carousels/LW-CAR-0012/. 8 слайдів, усі готові до генерації. Відлік #5 → #1 з ✗ помилкою / ✓ виправленням і ілюстраціями; «Which one did we miss?»; фінал «Fix #1 And #2 Starting Today.».

## LW-CAR-0013 «PROGRESSIVE OVERLOAD, EXPLAINED» — власна тема
Пакет: carousels/LW-CAR-0013/. 9 слайдів, усі готові до генерації. 4 способи прогресу (BEFORE → AFTER), таблиця на 4 тижні, «застряг?», фінал «You Can't Beat Numbers You Don't Track.». Найкраще пасує екран запису тренування.

## Фон без арки + пакети LW-CAR-0014…0017
- Правило фонів: carousels/CODEX-SERIES-RULES.md (GRID / DOTS / CLEAN / PLATES, без арки, без смужки прогресу). LW-CAR-0011 → PLATES.
- LW-CAR-0014 «NO GYM? NO PROBLEM» (DOTS, 9), LW-CAR-0015 «SKINNY ARMS?» (GRID, 8), LW-CAR-0016 «CAN'T DO A PULL-UP?» (CLEAN, 9), LW-CAR-0017 «HOW TO LOOK WIDER» (PLATES, 8). Усі готові до генерації; у 0014 власник має підтвердити запис вправ з власною вагою в апці.

## LW-CAR-0018 «GYM MYTHS THAT NEED TO DIE» — власна тема
Пакет: carousels/LW-CAR-0018/. 8 слайдів, фон DOTS, повний логотип з файлу. Усі готові до генерації. 6 міфів у форматі «MYTH #N (закреслений) → TRUTH», без вигаданих цифр; джерела в copy.json → claims_to_verify. Фінал «Stop Guessing. / Track What Works.».

## LW-CAR-0019 «WEAK BACK?» — тест мінімалістичного тіла
Пакет: carousels/LW-CAR-0019/. Тексти й макети LW-CAR-0001, фон GRID, повний логотип. Спершу Codex малює слайди 1 і 3 у трьох стилях фігури (A пласкі форми, B лайн-арт, C м'який матовий), власник обирає, потім уся карусель у вибраному стилі.

## LW-CAR-0020 / 0021 — тір-листи в стилі S2
- 0020 «chest tier list» v1.1: вигляд REF-008, наші вправи, рейтинг і тексти. Стане еталоном S2 після прийняття.
- 0021 «back tier list»: та сама серія для спини. Генерувати краще після прийняття 0020, щоб збігались.
- 0020 і 0021 прийняті власником повністю.
- 0022 «legs tier list» і 0023 «biceps tier list»: та сама серія S2, наш рейтинг і тексти. Еталон — прийняті 0020 / 0021.
- 0024 «1 exercise per muscle» (12 слайдів) і 0025 «this or that? (gym edition)» (14 слайдів): нові формати S2, еталон вигляду — прийнята 0022 з логотипом Harda.
- 0026 «hardest muscles to grow (ranked)» (9 слайдів): відлік #7 → #1 зі шкалою складності й порадою «fix:», стиль S2.
- Пачка 2026-10-22: BATCH-A (0027 glutes tier list, 0028 stop doing this, 0029 why you're not growing) і BATCH-B (0030 underrated exercises, 0031 WEAK CORE? у стилі S1, 0032 ranking every gym split). Генератори роблять усе одразу, без зупинок на перевірку.
- Пачка 2026-10-23: BATCH-C (0033 signs you're making progress, 0034 not a beginner anymore, 0035 home workout tier list, 0036 secretly killing your gains, 0037 beginner vs advanced), один агент робить усе одразу.
- Пачка 2026-10-23: BATCH-D = спершу FIX-ENDINGS (7 фіналів), потім 0038 gym red flags, 0039 unwritten gym rules, 0040 why you keep quitting the gym, 0041 types of people at the gym, 0042 look bigger in a t-shirt.
- Пачка 2026-10-24: BATCH-E (0043 favorite exercise says about you, 0044 things only gym people understand, 0045 gym bro translator, 0046 gym green flags, 0047 look better shirtless). 0038–0042 готові, 7 старих фіналів виправлені.
- Пачка 2026-10-24: BATCH-F (0048 5 stages of leg day, 0049 gym excuses tier list, 0050 gym pet peeves, 0051 gym outfit says about you, 0052 muscles people notice first, 0053 types of gyms tier list). 0043–0047 готові.
- Пачка 2026-10-26: BATCH-G (0054 if muscles were people, 0055 gym playlist says about you, 0056 most skipped muscles tier list, 0057 gym zodiac signs, 0058 favorite day says about you, 0059 cardio tier list, 0060 post-workout meals tier list, 0061 gym time says about you). BATCH-F ще чекає на перевірку після генерації.
- 2026-10-27: BATCH-F (0048–0053) готова. BATCH-G: 0054–0055 готові, зупинка через HTTP 408 при push. Дозавершення: carousels/BATCH-G-RESUME.md (0056–0061).
- Пачка 2026-10-27: BATCH-H (0062 gym things that feel illegal і 0069 gym tips that feel illegal to know у S2; 0063 WEAK LEGS?, 0064 WEAK SHOULDERS?, 0065 WEAK GLUTES?, 0066–0068 STRUCTURE THE PERFECT UPPER / ARM / FULL BODY DAY у S1). Запускати після BATCH-G-RESUME.
