# Як шукати теми для каруселей — v0.1

Основа: розбір REF-001…REF-007 ([references/PATTERN.md](../references/PATTERN.md)). Це пропозиція для власника, а не запуск генерації.

## 1. Звідки брати теми

1. **Сітка профілю Arrow.** Власник робить 2–4 скриншоти сітки профілю @arrowfitnessapp у TikTok. На кожній обкладинці видно hook і **кількість переглядів**, а саме переглядів нам зараз бракує. Агент виписує всі теми й сортує їх за переглядами. Найкращі власник докладає в CAROUSELS.md повністю, як REF-008, REF-009 тощо. З хмарного середовища TikTok напряму не відкривається, тому скриншоти — єдиний робочий канал. Перший такий розбір (~50 постів із переглядами): [references/ARROW-PROFILE.md](../references/ARROW-PROFILE.md).
2. **Інші акаунти-каруселі.** У пошуку TikTok шукати push day, pull day, leg day, gym split, best exercises, weak back, вкладка «Фото». Брати пости з великою кількістю збережень і так само додавати скриншоти.
3. **Коментарі під сильними постами.** Найлайкнутіші питання й суперечки — це готові теми наступних каруселей (див. розділ 3).
4. **Матриця «формат × тема».** Формат береться з перевіреного референсу, тема — з наступного блоку. Так виходить серія без вигадування нової механіки.
5. **Власна статистика.** Після публікації записувати перегляди, лайки, збереження й коментарі. Повторювати формати з найкращим співвідношенням saves/likes.

## 2. Перевірені формати (з референсів)

| Код | Формат | Референс | Saves/likes |
|---|---|---|---|
| F1 | STRUCTURE THE PERFECT ___ DAY: чекліст → #1–#6 зон → «оберіть 1 з 2» | 001, 005 | 67–74% |
| F2 | THE ULTIMATE ___ DAY: 6 вправ із сетами й підказкою з техніки | 002 | 64% |
| F3 | BEST EXERCISES FOR EVERY MUSCLE GROUP (___ Edition): зона → A OR B | 004 | 55% |
| F4 | WEAK ___?: мапа м'язів → 5 зон A OR B | 007 | 60% |
| F5 | RANKING ___: відлік #8 → #1, зірочки, продукт перед топ-3 | 003 | 36% (зате найбільше коментарів) |
| F6 | CONSISTENCY: трансформація → харчування → спліт на 5 днів | 006 | 66% |

## 3. Беклог тем (кандидати, не затверджені)

**Прогалини в серії** (у референсах цих тем немає; перед стартом звірити із сіткою Arrow):
- STRUCTURE THE PERFECT LEG DAY (F1)
- BEST EXERCISES FOR EVERY MUSCLE GROUP (Pull Day Edition / Leg Day Edition) (F3). «Edition» в оригіналі сам обіцяє продовження.
- THE ULTIMATE UPPER DAY / LOWER DAY (F2)
- WEAK CHEST? / WEAK LEGS? / WEAK SHOULDERS? / WEAK ARMS? (F4)

**З коментарів під референсами:**
- «what about rear delts?» (REF-001) → карусель про задні дельти (F4 або F3)
- «ONE BICEP» (REF-005, 117 лайків) → ARM DAY (F1/F2)
- «what can i do instead of JM Press and machine dips?» (REF-004) → заміни без тренажерів (F3)
- «what about ppl, rest, pp?» (REF-003, 284 лайки) → продовження рейтингу сплітів (F5)
- Рейтинги вправ (RANKING EVERY BICEPS / TRICEPS EXERCISE). Arrow робить такі у відео, у форматі каруселі (F5) їх серед референсів немає.

## 4. Продуктовий фінал за темою

Усі теми про конкретний тренувальний день → фінал «запиши тренування» з реальним екраном запису чи підсумку (як 001, 002, 004). Теми про спліт і план (F5, F6) → лише якщо в Lightweight є реальна функція програм чи папок. Інакше обрати іншу реальну функцію й назвати це відхиленням від оригіналу. Конкретні екрани визначаються після того, як власник додасть їх в APP-SCREENS.md.

## 5. Заплановані повтори (рішення власника)

- **«THE MUSCLES YOU'RE FORGETTING» — нова версія** (на основі LW-CAR-0006). Та сама ідея й формат, але новий текст (без «lifters»), інші ілюстрації та інша подача, щоб це була окрема карусель, а не копія. Зробити пізніше як новий LW-CAR-ID.

## 6. Беклог тем v2 (2026-10-19)

Вже в роботі: WEAK BACK? (0001), PUSH / PULL / LEGS (0002, 0004, 0009), THE ULTIMATE PULL DAY (0003), BEST EXERCISES PUSH (0005), THE MUSCLES YOU'RE FORGETTING (0006), HOW MANY SETS (0007), WEAK CHEST? (0008), YOUR FIRST WEEK IN THE GYM (0010).

Правила для всіх: без «lifters»; у вправах, де можна, варіант з власною вагою; фінал — реальна функція з реального екрана (журнал тренувань, кількість тренувань / підходів, Muscle balance, Distribution).

### Пріоритет 1 — найбільший очікуваний ефект
| # | Хук | Формат | Ідея слайдів | Фінал |
|---|---|---|---|---|
| 1 | WHAT 1 YEAR OF TRAINING ACTUALLY LOOKS LIKE | трансформація (CONSISTENCY 1.2M, DISCIPLINE 517K у Arrow) | 1 / 3 / 6 / 12 місяців — реалістично, що змінюється (сила, форма, звички); чесна відповідь на коментарі «це нереально» | «Log every workout. Watch your year add up.» + кількість тренувань |
| 2 | STRUCTURE THE PERFECT FULL BODY DAY | Structure (FULL BODY WORKOUT 740K у Arrow) | чекліст → 6 слотів (squat, hinge, push, pull, shoulders, core) | Track Your Workouts + екран |
| 3 | PROGRESSIVE OVERLOAD, EXPLAINED | пояснення + шпаргалка | 4 способи прогресувати: вага, повтори, підходи, техніка; приклад тижнів 1→4 | найсильніший зв'язок з продуктом: «You can't beat numbers you don't track.» |
| 4 | SKINNY ARMS? | WEAK ___? (SKINNY ARMS 98K у Arrow) | мапа: біцепс, довга голова трицепса, брахіаліс, передпліччя → 4 слоти | Muscle balance (вісь Arms) |
| 5 | WEAK SHOULDERS? | WEAK ___? | передня, середня, задня дельта + верх трапецій | Muscle balance (вісь Shoulders) |
| 6 | PULL-UP PROGRESSION | рівні 1→5 (калістеніка) | dead hang → scapular pull → negatives → band → full pull-up | «Log every set. See the day you hit your first pull-up.» |
| 7 | 5 MISTAKES KILLING YOUR GAINS | помилки (суперечки = коментарі) | его-ваги, без прогресії, випадкові тренування, пропуск ніг, недосип | журнал тренувань |
| 8 | STRUCTURE THE PERFECT UPPER DAY | Structure | серія з 0002/0004/0009 | Track Your Workouts |
| 9 | STRUCTURE THE PERFECT LOWER DAY | Structure | серія | Track Your Workouts |
| 10 | NO GYM? NO PROBLEM | Structure / калістеніка | full body без обладнання: squat, push-up, pike push-up, row під столом/на брусі, lunge, plank | журнал тренувань |

### Пріоритет 2
| # | Хук | Формат | Ідея |
|---|---|---|---|
| 11 | PUSH-UP PROGRESSION | рівні | від стіни до push-up на одній руці; збережуть калістеніка й новачки |
| 12 | HOW MANY REPS SHOULD YOU DO? | цифри (як 0007) | і малі, і великі повторення будують м'язи, якщо підходи важкі; потребує перевірки джерел |
| 13 | HOW LONG SHOULD YOU REST BETWEEN SETS? | цифри | довший відпочинок на базових вправах; потребує перевірки джерел |
| 14 | HOW OFTEN SHOULD YOU TRAIN EACH MUSCLE? | цифри | ~2 рази на тиждень як практична порада; без «так більше росте» |
| 15 | WEAK CORE? | WEAK ___? | прес, косі, поперек; майже все з власною вагою |
| 16 | NARROW SHOULDERS? | WEAK ___? | V-силует: середні дельти + широчайші |
| 17 | STRUCTURE THE PERFECT ARM DAY | Structure | біцепс / трицепс / передпліччя, 6 слотів |
| 18 | STRUCTURE THE PERFECT HOME WORKOUT | Structure | лише гантелі |
| 19 | CHEST EXERCISE TIER LIST | рейтинг S→D (тир-лист спини 164K у Arrow) | рейтинги провокують коментарі |
| 20 | BICEPS EXERCISE TIER LIST | рейтинг | те саме для біцепса |

### Пріоритет 3 — новачки та звички
| # | Хук | Ідея |
|---|---|---|
| 21 | THINGS NOBODY TELLS YOU BEFORE YOUR FIRST GYM DAY | етикет, що брати, як не соромитися; для новачків, часто пересилають |
| 22 | HOW TO PICK YOUR STARTING WEIGHT | метод «12 повторів з запасом 2–3» |
| 23 | YOUR FIRST MONTH IN THE GYM | продовження 0010: тижні 1→4 |
| 24 | DISCIPLINE BEATS MOTIVATION | звички замість мотивації; фінал — кількість тренувань |
| 25 | GYM MYTHS THAT NEED TO DIE | «спалити жир у точці», «muscle confusion», «треба до відмови» (Refalo 2023) |
| 26 | WHY YOU'RE NOT GROWING | чекліст причин (як «The reason your legs aren't growing» у Arrow, 51K) |
| 27 | RANKING EVERY GYM SPLIT | наш власний рейтинг сплітів, власний текст |
| 28 | THE MUSCLES YOU'RE FORGETTING — нова версія | див. розділ 5 |

## 7. Нові формати в стилі S2 (не тір-листи), 2026-10-20
Усі в дизайні 0020–0023: біла фігура, жирний текст з малої літери, кораловий маркер, фон #F0F1EB, логотип Harda, фінал з рукою й телефоном. Без цифр і досліджень, тільки думки й практичні поради.

| # | Формат | Хук обкладинки | Структура | Головна метрика | Фінал |
|---|---|---|---|---|---|
| F1 | **Одна вправа на м'яз** | `1 exercise per muscle` / `(if you could only pick one)` | 8–10 слайдів: м'яз → одна вправа + 1 рядок «чому» | коментарі («ти забув X») + збереження | Harda показує, які м'язи ти пропускаєш (Muscle balance) |
| F2 | **This or that?** | `this or that?` / `(gym edition)` | 6 дуелей: дві фігури поруч, `vs`, вердикт маркером на наступному слайді | коментарі (люди обирають сторону) | лог тренувань: «test both, track both» |
| F3 | **Заміни це на це** | `stop doing this.` / `do this instead` | 6 пар: закреслена вправа → краща заміна + чому | збереження | лог сетів: «see which one actually grows» |
| F4 | **Gym red flags 🚩** | `gym red flags` | 7 поведінкових «червоних прапорців» новачка з легким гумором (его-ліфтинг, без розминки, сидіти в телефоні на тренажері…) | репости й коментарі | «green flag: you track your workouts» |
| F5 | **Недооцінені вправи** | `underrated exercises` / `(nobody does these)` | 7 вправ: назва + що дає + фігура | збереження | «add them to your next workout in Harda» |
| F6 | **Найважчі м'язи для росту** | `hardest muscles to grow` / `(ranked)` | 7 місць зі шкалою складності 1–5 (без тірів) | коментарі | Muscle balance: «see which ones are falling behind» |

Порядок запуску (рекомендація Claude): F1 → F2 → F3, потім F4–F6, чергуючи з тір-листами (плечі, трицепс).
