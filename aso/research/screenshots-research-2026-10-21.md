# Screenshot research (2026-10-21)

## Cal AI

Research on Cal AI's App Store page is done. One surprise: what the iTunes lookup returns is not what the US product page shows on current iPhones (details in the method note). I wrote nothing to the repo.

**Method note:** The lookup `screenshotUrls` gives an old 5.5" set of 4 images (1242x2208). The US web product page shows a different set of 6 images at 6.5" (1284x2778). That is the set modern iPhones see. I viewed all 10. Our existing `aso/research/screenshots.md` assumes the lookup order matches the page, and for Cal AI it doesn't. Other apps may have the same mismatch.

## 1. Listing facts (US, fetched 2026-10-21)
- **Name and subtitle:** "Cal AI - Calorie Tracker" / "Food & Macro Counter". The id is 6480417616 and the seller is Viral Development LLC.
- **Ratings:** 371,543 at 4.80 in the lookup; the page shows "372K Ratings".
- **Chart and genres:** the page shows "#5 Health & Fitness". Genres are Health & Fitness and Food & Drink.
- **Release history:** first released 2024-04-08. Current version is 26.42.0 (2026-10-20). Updates ship weekly with the same generic note: "Improvements and tweaks to help you build and be your best".
- **Other:** 15 languages, age rating 9+.
- **In-app purchases:** Unlimited $29.99, Unlimited Plan $19.99, Unlimited $9.99, Unlimited $19.99, Streak Restore $0.99.
- **Promotional text:** none on the web page or in the lookup.
- **App preview video:** none. The phone media shelf is screenshots only and there is no "videos" shelf. This is not checked on a device. There are also 2 Apple Watch screenshots.
- **Description:** 828 characters in total. The first 600:
  > "HOW TO USE CAL AI: 1) Answer lifestyle questions to build your plan 2) Snap a photo of your meal* 3) Get your nutritional breakdown* If you want to get your dream body, Cal AI will help you get there with less time spent than anyone else. We aren't another complicated diet app. We want to empower everyone to be confident in their bodies with minimal time spent, but you have to work hard. We will support you and give you the tools and information you need. If you have any ideas or questions, please email us at team@calai.app. NOTE: We do not offer medical advice. Any and all recommendati…"
  
  It ends with "*FOOD SCANNING ANALYSIS RESULTS REQUIRE A SUBSCRIPTION".

## 2. Current 6.5" set (product page)
Every slide uses the same template:
- White background, a near-black bold headline centred at the top, and one upright iPhone frame with a Dynamic Island.
- No hands, people holding the phone, arrows, stickers, badges, ratings, user counts, press or awards.
- Colour appears only in the data: red for protein, orange for carbs, blue for fat, plus an orange streak flame.

| # | Headline (verbatim) | Words | UI shown | AI demo and visual devices | Social proof |
|---|---|---|---|---|---|
| 1 | (no headline; large "Cal AI" logo) | 0 (logo 2) | Home: flame streak "15", week strip Sun 10–Sat 16 with rings, "1250/2500 Calories eaten", macros "75/150g Protein eaten", "138/275g Carbs eaten", "35/70g Fat eaten", "Recently uploaded" Grilled Salmon 550 Calories; tabs Home/Progress/Groups/Profile and a + button | The calories card is enlarged and breaks out of the phone frame. The food thumbnail hints at photo logging | none |
| 2 | "Just snap a pic" | 4 | Camera: overhead Caesar salad; modes "Scan Food / Barcode / Food Label"; .5x/1x; shutter | **AI input:** white pill labels on leader lines ("Lettuce", "Parmesan", "Cherry Tomatoes", "Croutons") sit on the photo and spill past the frame. The plate also bleeds outside the phone | none |
| 3 | "See the calories" | 3 | Nutrition result for the same photo: "Caesar Salad with Cherry Tomatoes", stepper 1, "Calories 330" (pop-out card), Protein 8g / Carbs 20g / Fats 18g, "Ingredients + Add more", "Lettuce • 20 cal 1.5 cups", buttons "✦ Fix Results" and "Done" | **AI output:** slides 2 and 3 form one photo-to-result story with the same scene. "Fix Results" openly shows that you can correct the AI | none |
| 4 | "Track progress" | 2 | Progress: "Your Weight 132.1 lbs / Goal 140 lbs / Log Weight", "21 Day Streak", weight chart Jun–Nov with tooltip "131.2 lbs Sep 9, 2025", "80% of goal", 90D/6M/1Y/ALL, green line "Great job! Consistency is key, and you're mastering it!", "Daily Average Calories 2861 cal ↑90%" | Gamification: the streak flame and the encouraging message | none |
| 5 | "Grow with friends" | 3 | Groups: "Shred Squad", avatar row of muscular men with streaks 31/24/12/11/2 and a crown on the leader; post by "Cole Belvins": "Grilled Chicken with Avocado, Garlic Spinach, and Toast", 480 cal / 38g / 23g / 24g, reactions 🔥4 👏1, 2 comments | People appear as avatars and an amateur-looking food photo | in-app community only |
| 6 | "Watch the change" | 3 | Compare: before/after body photos "355 lbs Sep 20, 2023" and "182 lbs Jul 7, 2025", "Hide weight" toggle, progress-photo strip, "Share" | The strongest emotional slide. It implies a 173 lb result with no stated cause | transformation (implied proof) |

The story runs brand → snap → result → progress → friends → transformation. The demo numbers on slide 3 don't add up: 8P/20C/18F works out to 274 kcal, but the screen says 330.

## 3. Old 5.5" set (lookup only)
Dark near-black background, white left-aligned headlines over two lines, and a silver device frame.

1. **"Make calorie tracking easy with AI"** (6 words). Home with a pop-out "1250 Calories left"; "45g Protein over / 89g Carbs left / 48g Fats left"; Fattoush Salad 153 calories; Sweet Corn panner… 455 kcal; tabs Home/Analytics/Settings.
2. **"Just snap a picture of your food"** (7 words). Scanner on a pancake stack with a viewfinder, a "Scan food" mode bar and the shutter.
3. **"Then let us do the rest"** (6 words). This caption finishes the sentence from slide 2. The result screen has per-item calorie callouts outside the frame ("Blueberries 8", "Pancakes 595", "Syrup 12"), plus Calories 615, Carbs 93g, Protein 11g, Fats 21g with edit pencils, "Health score 7/10", "Fix Results" and "Done".
4. **"Track your progress as you go"** (6 words). Goal Progress "80% Goal achieved", a kg chart, "Nutritions 90% ↑ This week vs last week", "12780 Total calories / 1952 Daily avg.", and coloured "Protein / Carbs / Fats" pills that break out of the frame.

My inference is that this is the older set: the tab bar is older and the copy is longer. Moving to the 6.5" set, they cut headlines from 6–7 words to 2–4 words. They also added the friends and transformation slides.

## 4. Public commentary on their growth tactics
- **Keywords in name and subtitle.** The founder said "We definitely try to fit in as many keywords as we can" and that keywords came "mainly off the top of our minds", with agencies later. https://getlatka.com/interviews/cal-ai-zach-yadegari-2025
  - Astro shows them #2 for "calorie tracker" and #4 for "calorie counter".
  - The brand search "cal ai" scores 68, above "calorie counter" at 65. https://asoitis.com/case-studies/cal-ai
- **Constant paywall testing (vendor's own figures).** https://superwall.com/case-studies/cal-ai
  - 123 experiments, 160 designs and 424 variants across 46 trigger points; 61 tests on the onboarding paywall alone.
  - Trial-to-paid up 31%. 87% of new users see a paywall and 57% of those start a purchase.
  - Formats tested include a spin-the-wheel discount, video paywalls and web checkout through Stripe.
  - Quote: "ship something, measure it, and improve it tomorrow."
- **Long onboarding that converts better.** Extra questions raised conversion "because the user invests more time". About 25% of users start a trial in the first session. Sign-in was moved to the end.
  - https://founderpath.com/resources/zach-yadegari-cal-ai-onboarding-tests-and-influencer-marketing
  - Latka (above)
- **Onboarding and paywall details** (adapty.io and ASOitis, Oct 2026):
  - 25+ cards, or 29 screens with 16 questions; research statistics between questions; a personalised plan revealed before the paywall.
  - "Join over 10 million people like you", 4.8 stars and "250K+ App Ratings", all shown inside the app, not on the store page.
  - Mock permission prompts before the real ones.
  - Pre-paywall screens: "We want you to try Cal AI for free" / "No Payment Due Now" plus a promise to remind you before the trial ends. The annual plan with a 3-day trial is pre-selected.
  - "Where did you hear about us?" lists TikTok first.
  - ASOitis also points out that their user counts don't match: 10M in the app, 5M on the website.
  - https://adapty.io/blog/how-to-personalize-onboarding-and-paywalls-in-your-mobile-app/
- **Influencers are the main channel.** About 250 creators on flat monthly retainers, mid-six-figure monthly spend, chosen for "very tight communities", paid against reach targets. https://techcrunch.com/?p=3178431 (2026-10-15), founderpath, Latka.
- **Positioning and acquisition.** Speed over precision. MyFitnessPal bought Cal AI and the deal closed Dec 2025. 15M+ downloads and $30M+ yearly revenue, as reported by MyFitnessPal. https://techcrunch.com/?p=3098039
- **AppScreens labels** their March 2026 set (v3.2.6, 6 shots) "Feature Focus" and "Device-in-Hand". That doesn't match today's set, which has no hands. https://appscreens.store/app/cal-ai-calorie-tracker
- **What I couldn't find:**
  - No public source on Cal AI testing screenshots or using custom product pages. web.archive.org kept resetting the connection, so I have no history of their screenshot sets.
  - A separate "Cal AI-Calorie Tracker" listing (id 6753199967) uses the same name. I didn't verify it; it may be a copycat.

## 5. Tactics we can reuse for Lightweight (strength tracker, AI workout editing, dinosaur mascot)
These follow the owner's description of the real features:
- Swipe on an exercise → the exercise catalog opens → the pick replaces it automatically. There is no swap popup.
- A button at the top takes free text, such as an injury or "redo my workout", and rebuilds the workout.

Before any visuals, check the exact UI against the current build.

1. **Show the AI as input then result on two neighbouring slides** with the same workout in both. First slide: the top AI field with a typed request about an injury. Second slide: the rebuilt workout. This is their slide 2 → 3 pattern.
2. **Make the change visible on the screenshot itself** with callout pills and leader lines on the exercises that changed (old → new). Overlays are allowed under Apple rule 2.3.3, but they must match what the app really does.
3. **One pop-out element per slide**, such as the AI field, a replaced exercise row or a PR card, enlarged past the phone frame so it reads at thumbnail size.
4. **Short headlines of 2–4 words built on one verb**, in the same template on every slide.
5. **Show manual control next to the AI.** Their "✦ Fix Results" does this. Our version is the real swipe → catalog → replaced flow: the AI does the work, but you stay in charge.
6. **Clean native UI on plain white with one accent colour.** Colour goes only on data and the dinosaur, which also makes us look different from Cal AI.
7. **Make the description's steps match the slide order.** Their "1) … 2) … 3) …" follows the screenshots. Pro-only features get an asterisk, which matches the Apple rule 2.3.2 note in `apple-rules.md`.
8. **Brand + core keyword in the name, two more keywords in the subtitle** (their pattern: "Cal AI - Calorie Tracker" / "Food & Macro Counter"). Coordinate with `naming.md` and the keyword files.
9. **End on an emotional slide**: a progress or PR chart and a streak. The dinosaur could keep the streak, but only if a streak feature exists. All data must be demo data under Apple rule 2.3.9.
10. **Let users try the AI edit once inside onboarding, before the paywall.** ASOitis flags that Cal AI never lets users scan a meal before paying; we can do better.
11. **Keep the dinosaur as a small sticker** beside the AI moment, never covering the UI. Cal AI has no mascot, so this sets us apart (my inference).
12. **A frequent "What's New" cadence**, like their weekly releases.

## 6. Do NOT copy
1. **A before/after body transformation with weights** ("355 lbs → 182 lbs"). It's an unverifiable claim that the app caused the result, it needs model releases (Apple 2.3.9), and new rule 2.3.14 bans unverifiable claims in creative assets.
2. **Inflated or inconsistent user counts** (10M vs 5M), or any "#1", award or Editor's Choice line in screenshots. Apple's asset guidelines ban these, and we have few ratings.
3. **Anything that suggests the AI gives medical or injury advice.** Our AI button takes injury requests, which makes this the biggest risk. Keep a "not medical advice" disclaimer like Cal AI's.
4. **Pressure tactics on the paywall:** spin-the-wheel discounts, "save 75%" measured against monthly price × 12, a tracking prompt during the loading animation, "free" in screenshots (Apple 2.3.7), or 29 screens before the user sees the product.
5. **A logo-only first slide and sloppy demo numbers.** The logo slide works only with Cal AI's brand search and influencer traffic. Lifters will notice if volume ≠ sets × reps × weight.

## Files
- Data: `/tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/calai/data/`
  - `lookup.json`, `search.json`, `page.html`, `ssd.json`
  - `page_shots/p1.png`–`p6.png` (6.5" set)
  - `shots/ss1.png`–`ss4.png` (5.5" set)
- Scripts: `/tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/calai/scripts/`
  - `parse_page.py`, `dump_ssd.py`

## Competitors A (Hevy, Strong, StrengthLog, Dropset, Boostcamp)

Research is complete for all five apps. I looked at every iPhone screenshot in two sources: the `screenshotUrls` set from the iTunes lookup (9:16, 5.5-inch class) and the set on the US product page (6.5/6.9-inch, which is what current iPhones show). I also read the Apple Watch screenshots and extracted frames from the two app preview videos. Text in quotes is verbatim. Anything marked "Inference" is my judgement, not a fact.

## Corrections to /home/user/lightweight-carousels/aso/research/screenshots.md
1. **Strong and Boostcamp do have app preview videos, in slot 1.** On the product page, the first phone-media item is a video for both apps (`.m3u8` from apptrailers.itunes.apple.com). The existing file says no app showed a video, so the screenshots you see first are actually in slot 2.
2. **The two sets differ in some apps.** Hevy's product-page set has the same headlines but newer UI (for example, slide 6 adds before/after progress photos). Strong slide 3 shows a "Warm-up Sets" modal on the product page and a "Plate Calculator" modal in the lookup set. StrengthLog's two sets are byte-identical; Dropset and Boostcamp match visually. The 6.5/6.9-inch set below is the main reference.
3. **Strong contradicts itself.** The screenshot says "Join over *3 million* Strong users"; its own description says "join over 1.2 million people who have downloaded Strong". Neither number can be verified.

---

## Hevy (1458862350): 10 iPhone screenshots, no video, 5 Watch screenshots
Subtitle: "Weight Lifting Routine Planner". Rating 4.92 from 98,941 reviews.
Style: light grey background with a blue bottom band, bold ALL-CAPS two-line headline (black, or black/blue on slide 1), upright modern iPhone, and one "pop-out" floating card per slide.

| # | Headline (verbatim) | Feature | UI screen | Presentation |
|---|---|---|---|---|
| 1 | "LOG WORKOUTS / GET STRONGER / STAY MOTIVATED" + laurel "★★★★★ Apps We Love" | Positioning + social proof | Tilted phone edge only | Panorama into slide 2 |
| 2 | (none, "HEVY" logo) | Logging | Log Workout: Time 1h 15min, Volume 6 800 kg, Sets 18; Bench Press with note and "Rest Timer: 1min 30s"; Previous column (40kg × 7 …); green completed set rows | Tilted phone, set rows pop out as green cards |
| 3 | "ANALYZE YOUR WORKOUTS" | Progress per exercise | Squat (Barbell), tabs Summary/History/How to/Leaderboard, muscle animation, 80 kg line chart, chips Heaviest Weight/One Rep Max/Best…, "Personal Records" | Upright device (older set had a "PR" medal) |
| 4 | "PLAN YOUR ROUTINES" | Routines/programs | Workout tab: Quick Start "Start Empty Workout", Routines "New Routine"/"Explore", My Routines (6), "Start Routine" | Upright |
| 5 | "JOIN A GROWING COMMUNITY" | Social feed | Feed post "strongdavid – Chest Day 💪", 8 likes, 3 comments, Suggested Athletes, "Invite a friend" | Upright |
| 6 | "TRACK MEASUREMENTS" | Body metrics | Measurements: Progress Pictures (before/after 2022 vs 2024), Body Weight chart, chips Bodyweight/Bodyfat %/Chest | Upright |
| 7 | "COMPARE YOUR STRENGTH" | Social comparison | Comparison "jaumeros VS strongdavid", "STRONGER" badge, One Rep Max ↑16%, Heaviest Weight ↑5%, Best Set (Volume) ↓3% | Upright |
| 8 | "FOLLOW FRIENDS' PROGRESS" | Social profile | Profile: Workouts 56 / Followers 72 / Following 55, "Follow", "3 hours this week" bar chart, Routines | Upright |
| 9 | "LIBRARY WITH HQ VIDEOS" | Exercise library | "Add Exercise": Search Exercise, "All Equipment" and "Chest" filters, Bench Press variants, "Create" | Upright |
| 10 | "SLEEK DARK MODE" | Dark mode | Feed in dark UI | Dark background variant |

- **Watch shelf (5):** Routines with "Sync Routines"; "Live Sync" Push workout 01:06 with heart rate 80 and 3 kcal; Bench Press "Set 3 of 9" kg/reps entry with "Previous: 50.0kg x 7"; Plank duration timer; rest timer "01:00" with "Next set … Set 4/9" and −15s/+15s. Watch never appears in the iPhone set.
- **Feature order:** log, analyze/PRs, routines, then social ×3 (community, compare, friends), measurements, library, dark mode.
- **Social proof:** only the "Apps We Love" laurel on slide 1. The description says "millions of lifters" and "Free, with no ads"; neither is in the images.
- **Replacing exercises:** not shown. The library appears as an "Add Exercise" picker with search and equipment/muscle filters.
- **Programs:** "Explore" button only. "Hevy Trainer" (a Pro feature that "builds a program tailored to your experience, goal, available equipment") is in the description only, never in the screenshots.

## Strong (464254577): video + 6 iPhone screenshots, 1 Watch screenshot
Subtitle: "Strength Training Planner". Rating 4.86 from 108,538 reviews.
Style: dark slate background, white sentence-case headline aligned left, older notched iPhone frame with light UI. Slides 2–4 are one sentence joined by "…".

| # | Headline | Feature | UI | Notes |
|---|---|---|---|---|
| V | Video, about 39 s (poster frame has no text). Cards: "Track your workouts", "Measure your progress", "Get Strong." | Logging, then progress | Deadlift logging with set-type menu "Warm-up / Drop Set / Failure"; rest timer 1:58/2:00; Profile charts; Deadlift About/History/Records (1RM 152 kg, predicted-reps table) | Autoplay not verified |
| 1 | "Join over *3 million* Strong users tracking their workouts." | Social proof + logging | "Monday's session", Bench Press/Squat set table (Previous/kg/Rep/✓), "Finish" | |
| 2 | "Hundreds of built in exercises, with video instructions..." | Library | Bench Press About/History/Charts/Records, illustration, Instructions | |
| 3 | "...warm-up and plate calculators..." | Calculators | "Warm-up Sets" modal (Bar × 5, 50% × 3, 80% × 3, "Insert") | |
| 4 | "...automatic rest timers, and 1RM calculation." | Timer | Rest Timer 0:45/0:30, −30s/+30s/Skip | |
| 5 | "Chart your lifts and favorite metrics." | Progress | Profile "Grace Brooks – I want to lose 8 kg!", Workouts Per Week, Bench Press Chart | |
| 6 | "Track your workout consistency from your Home Screen." | Widget | Home-screen widget "Workouts Per Week, Target: 3" | |

- **Watch (1):** a "Sign In / Help" screen only. This is a weak use of the shelf, even though the description says "Fully-featured Apple Watch app".
- **Feature order:** proof + logging, library, calculators, timers/1RM, charts, widget.
- **Not shown at all:** social, programs and replacing exercises. PRs appear only in the video (Records tab).
- **Social proof:** "3 million" in the slide-1 headline. CNBC and The Verge quotes are in the description only.

## StrengthLog (1434229662): 10 iPhone screenshots (same in both sets), no video, 5 Watch screenshots
Subtitle: "Workout Log & Programs". Rating 4.86 from 3,690 reviews.
Style: blue-grey gradient, centred bold white sentence-case headline, often two short parallel sentences, modern iPhone frame with dark UI. Slide 7 pops a card out; slide 10 has floating cards and no device.

| # | Headline | Feature | UI |
|---|---|---|---|
| 1 | "The gym app built for serious lifters" | Positioning + logging | Active workout "Bodybuilding Ballet: Chest…", Bench Press warm-up rows, sets 75–85 kg, "YR" badges, Volume 2,240 kg / Reps 28 / Average weight 80 kg |
| 2 | "Unlimited workout logging. Zero ads." | Free/no ads | Training log totals (Since start 359 workouts …), program entry "StrengthLog's 3-Day Bodybuilding Split: Week 3, Workout 2" |
| 3 | "See how strong you really are" | Strength benchmark | Strength levels: "Intermediate", "You are stronger than 53% of other users in your weight and age group", pinned Pull-Up/Push-Up |
| 4 | "Train together. Get stronger together." | Social | Friends: Activity/Challenges tabs, friends' workouts with fist-bump counts and muscle maps |
| 5 | "Follow a program. Or build one." | Programs | Library tabs Programs/Workouts/Exercises, "New 5-day split for premium users", PPLUL 5 days/week "Premium" |
| 6 | "See exactly how your training is progressing" | Stats | Statistics "My graphs": All training reps, Body weight |
| 7 | "Know which muscles are being trained" | Muscle map | "Muscles worked – The last 90 days" heat map, Set/week scale |
| 8 | "Plan your training. Never lose track." | Calendar/planning | Month calendar with dots, program workout, "+ Event", "+ Plan workout" |
| 9 | "A huge exercise library. Built to teach." | Library | Bench Press About/Records/Stats/History/Friends tabs, real-gym video, numbered cues |
| 10 | "Everything needed for better training" | Tools/goals | Streaks "3 Workouts/week, Current: 12 weeks"; goal rings (88% 120kg Bench …); 1RM/Plate/RPE calculators, Warm-up for max attempt, IPF/Wilks, Sinclair |

- **Watch shelf (5):** "Feet-Up Bench Press" with "+ Add warmup" and set rows; rest timer 01:03; "Start new workout" and "Program workouts: Beginner Barbell Program: Week 1, Workout A"; exercise video; "All exercises" by muscle (Back (130) …).
- **Feature order:** positioning, free/no ads, benchmark vs others, social, programs, stats, muscle map, planning, library, tools.
- **Social proof:** no ratings, badges or user counts. The percentile comparison ("53%") stands in for it.
- **Replacing exercises:** not shown.

## Dropset (6444746146): 10 iPhone screenshots, no video, no Watch
Subtitle: "Track your gym workouts". Rating 4.42 from 96 reviews; last update 2025-07-30.
Style: pure black, minimal. Headlines are one or two words ending in a period. On slides 3–7 the device is cropped off the right edge with left-hand callout labels. Bento tiles on slides 2 and 8; wordmark end card.

| # | Headline | Feature | UI |
|---|---|---|---|
| 1 | "Serious tracking for serious gym workouts." | Positioning | "Workouts" dashboard: routine cards Chest + tricep (Fridays), Back + bicep + legs (Mondays), Body weight 190 lbs, dot calendar, "Volume lifted 3.200 lbs" |
| 2 | "Athletic by design." | UX qualities | Tiles "Big touch areas", "Works offline", "Fast as lightning", "4:21 Readable at a distance" (no device) |
| 3 | "Not just reps." | Tracking types | Labels "Distance + pace / Sets and reps / Intervals / Check-off / Duration timer"; session 32:08 |
| 4 | "Supersets." | Supersets | "Superset link" chain between exercises |
| 5 | "Dropsets." | Set types | Menu Warmup / Dropset / RPE / Copy + paste / Delete on Pull ups |
| 6 | "Notes." | Notes | Exercise notes with keyboard |
| 7 | "Pace." | Cardio | Park run, minutes picker, "5:42 min/km" |
| 8 | "Flexible planning." | Scheduling | Weekday chips; "How many days of rest do you need between Pull workouts?" |
| 9 | "Community." | Group chat | "Chat" thread ("How do I break through my current plateau…", "Try using a smith machine instead…") |
| 10 | (none) | Brand | "dropset" wordmark |

- **Not shown:** progress charts or PRs (only the volume tile on slide 1), exercise library, replacing exercises, programs, Watch.
- **Social proof:** none.
- **Feature order:** positioning, UX speed/offline, workout types, set techniques, notes, cardio, planning, community.

## Boostcamp (1529354455): video + 6 iPhone screenshots, no Watch shelf
Subtitle: "Gym & Strength Training Plans". Rating 4.85 from 10,640 reviews.
Style: dark charcoal with a brand chevron watermark. Headlines mix weights: the first phrase is bold, the rest is light. Device cropped at the right and bottom; slide 1 has no device.

| # | Headline | Feature | UI |
|---|---|---|---|
| V | Video, about 40 s. Cards: "Follow Programs from Elite Coaches", "Progressive Overload, Built Into Your Training", "Or, Create Your Own Custom Programs", "Analyze Your Progress.", end card "BOOSTCAMP / Stop Guessing Start Progressing" (also the poster) | Programs, auto progression, builder, analytics | Explore "By Coaches 134 / By Users 11,345", program cards (PHUL ★4.2, 26,742 users, "Matches you: Intermediate, Full Gym"); logging with Target/RPE and a **"Swap"** button; Exercises picker (search, muscle groups, equipment, "Add as Superset"); Week 1·Day 1 builder with RPE keypad ("Could do 2 more reps"); Muscle Tracker table, Training Trends |
| 1 | "Science-Based Programs By Renowned Coaches (Not Fitfluencers)" | Authority | Coach grid with credentials and "N Programs" badges (Nuckols, Candito, Lefever, Bromley, Nuñez, Campbell) |
| 2 | "Ditch the spreadsheet with our smart program tracker" | Switching + program logging | Bench Press 5/3/1 BBB note, Previous/Target ("+5 lb", "5-7 RPE", "66% of 1RM"), **"Swap Exercise"** button, RPE keypad |
| 3 | "Weight progressions automatically calculated for you" | Auto progression | Rep Maxes (Training Max ~90%), One Rep Max Calculator |
| 4 | "Custom workout tracker to log your training and create routines" | Custom logging | "Strength Focus": W/1/2/F set types, RPE/RIR, **"Swap"** button |
| 5 | "Track your progress with in-app workout analytics" | Analytics/PRs | Lifetime 234 workouts / 56 h / 7m kg, percentile-style badges (67%, 23%, 9%), "3 Week Streak", "New Personal Records" |
| 6 | "Training tools like exercise demos, timer, plate calculator" | Library/tools | Chest Press demo, History/Charts/Records, volume vs bodyweight chart |

- **Feature order:** authority/programs, switch from spreadsheet, auto progression, custom tracker, analytics/PRs, tools/library.
- **Social proof:** coach credentials only. "1,300,000 lifters", "300M+ workouts", "4.8 stars" and Garage Gym Reviews "Best Workout App Overall in 2026" are in the description only.
- **In the description but not the screenshots:** "AI Coach – Short questionnaire, then a customized multi-week program"; "mid-set exercise swaps that keep your numbers"; Live Activities/Dynamic Island; offline use.

---

## Patterns

**Slide count.** Hevy, StrengthLog and Dropset use all 10 slots. Strong and Boostcamp use 6 images plus a video in slot 1. Typical: 10 images, or 6 plus a video. Three of five have a separate Watch shelf (Hevy 5, StrengthLog 5, Strong 1 weak). No app puts the Watch in its iPhone set.

**Headline length.** Median 6 words; average 4.9 words across the 40 captioned slides.
- Short-headline approach: Dropset averages 2.1 words, often one word plus a period ("Supersets."); Hevy averages 3.4 words in ALL CAPS verb + object ("PLAN YOUR ROUTINES").
- Long-headline approach: StrengthLog averages 6.0 words, often two short sentences ("Follow a program. Or build one."); Strong 6.8 words in full sentences; Boostcamp 7.7 words, bold lead plus light remainder.
- Longest: Boostcamp at about 63 characters.

**Table stakes (shown by 4–5 of the 5):**
1. Live set-logging screen early (slot 1–2, or the first card of the video). All 5. Common details: Previous column, kg/reps, checkmarks, rest timer, and set types (warm-up/drop/failure/RPE).
2. Progress or PR analytics by slot 3–5. 4 of 5; Dropset is the exception. Forms: Heaviest Weight/1RM chart (Hevy), Records tab (Strong), strength level (StrengthLog), "New Personal Records" (Boostcamp).
3. Exercise library with demos. 4 of 5 (Hevy 9, Strong 2, StrengthLog 9, Boostcamp 6).
4. Routines, programs or planning. 4 of 5; Strong shows none.
5. Calculators and timers (plate, 1RM, warm-up, rest). 4 of 5.
6. Dark UI. 4 of 5; Hevy is light but spends a slide on "SLEEK DARK MODE".

**Social features:** Hevy uses 3 of 10 slots, StrengthLog 1, Dropset 1 (chat). Strong and Boostcamp use none. Always placed mid-to-late (slots 4–9), never in slot 1.

**Social proof in the images is thin.** Hevy has a laurel, Strong a user count, Boostcamp coach authority; StrengthLog and Dropset have none. Ratings counts, press quotes and awards sit in descriptions (Strong, Boostcamp), not in screenshots.

**White space (shown by none of the 5):**
1. **Replacing or swapping an exercise as a headline benefit.** Only Boostcamp shows a "Swap Exercise"/"Swap" button, as background UI, never as a headline. Inference: Lightweight's flow (swipe on an exercise, land in the catalogue, the pick replaces it automatically) is an open message, as long as it is shown exactly as it works. Do not call it "AI swap".
2. **AI, or editing a workout in plain words** (for example "I have an injury, rework my workout"). Boostcamp's "AI Coach" and Hevy's "Hevy Trainer" exist only in their descriptions; neither shows AI in images. Nobody shows adapting a workout around an injury. Inference: Lightweight's top button for injury or workout-rework requests would be first in the images in this set, if it is shown as a real UI screen.
3. **Onboarding or personalisation questionnaire screens.** None.
4. **Apple Watch inside the iPhone set.** None.
5. **Importing or switching from another app.** None; Boostcamp's "Ditch the spreadsheet" is the closest.
6. **Price or free-tier transparency.** Only StrengthLog ("Unlimited workout logging. Zero ads.").
7. **Live Activities / Lock Screen / Dynamic Island.** None in images (Boostcamp mentions them in text). Home-screen widget: Strong only.
8. **Outcome or transformation photos.** Only a small before/after inside Hevy's measurements slide.

**Common slide orders.**
- Hevy, Strong, StrengthLog and Dropset: slot 1 is positioning or social proof over a logging screen; slots 2–3 show depth (analytics, library, free/no ads, or UX); progress and benchmark come by slot 3; social and extras at the end.
- Boostcamp: authority, then switching, then auto progression.
- Endings: wordmark end cards (Dropset slide 10; Boostcamp and Strong in their videos).

Not done: Cal AI was not in this assignment (folder comp-a covers only these five apps). Hevy's 2 iMessage screenshots were not viewed.

Files are in /tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/comp-a:
- /tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/comp-a/data/<id>/ — lookup.json, page.html, h01–h10 (lookup set), web01–web10 (product-page set), watch01–05
- /tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/comp-a/video/strong/frames/ and /tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/comp-a/video/boostcamp/frames/ — video frames
- /tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/comp-a/sheets/ — contact sheets: strong_video_a/b.jpg, boostcamp_video_a/b.jpg, hevy_watch.jpg, strengthlog_watch.jpg, dropset_web_a/b.jpg, boost_web_mid.jpg
- /tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/comp-a/scripts/ — fetch.py, hires.py, pages.py, media.py, cmp.py, parse*.py, grid.py, sheet.py

## Competitors B (Fitbod, Alpha, Ladder, Gymverse, Strava, +1)

Research complete: 8 apps, every iPhone screenshot, Apple Watch tabs and app-preview videos. All data is in `/tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/comp-b/`. Nothing was written to the repo.

## 0. Method and data notes (read first)

**Sources (US, fetched 2026-10-21):**
- iTunes lookup `screenshotUrls`.
- Product pages `apps.apple.com/us/app/id<ID>`, parsed from their serialized JSON (phone, watch and pad media shelves, plus video).
- Legacy top-grossing Health & Fitness RSS: `itunes.apple.com/us/rss/topgrossingapplications/limit=200/genre=6013/json`. The marketingtools URL returned 404.

**The lookup API is not what modern iPhones show** for Fitbod, Ladder, Strava and Hevy:
- For those four, lookup returns the old 5.5" set (1242×2208).
- The product page shows a different 6.5"/6.9" set. This document uses the product-page set as primary and notes the 5.5" differences.
- For Alpha, Gymverse, Liftoff and Gravl the two sets are identical.

**Videos:** Gymverse and Strava have an app preview video in position 0. I downloaded both and extracted frames every 2 s.

**"One more" top-grossing app:** the US Health & Fitness top-grossing ranks of the strength/gym apps are:

| App | Top-grossing rank |
|---|---|
| LADDER | #2 |
| Strava | #3 |
| Fitbod | #23 |
| Gymverse | #29 |
| Hevy | #38 |
| Liftoff | #59 |
| Gravl ("AI Personal Trainer") | #78 |
| Alpha Progression | not in top 100 |
| (for reference) Cal AI | #12 |

- I analyzed **Liftoff** (social, streaks, ranks) as the required extra app.
- **Gravl** and **Hevy** are bonus apps. Gravl has the closest analogues to Lightweight's swap and AI-edit features.

**US rating counts (lookup):**

| App | US ratings |
|---|---|
| Strava | 378,127 |
| Fitbod | 287,790 |
| Ladder | 210,500 |
| Gymverse | 165,379 |
| Liftoff | 99,863 |
| Hevy | 99,121 |
| Gravl | 5,948 |
| Alpha | 2,231 |

---

## 1. Per-app screenshot sets (verbatim text; "|" separates headline and subtext)

### Fitbod (1041517543): product-page 6.5" set, 10 screens

Look: black background with a blurred red gym photo, white bold caps headlines, upright devices.

| # | Headline / subtext (verbatim) | Feature shown | Presentation |
|---|---|---|---|
| 1 | Laurel: Apple logo "Editor's Choice", "274,000+ Reviews" \| "SMART WORKOUTS BUILT FOR YOU" | My Plan → "Push Day", "Switch" button, "7 Exercises • 3 Muscles", 45m, gym profile "Planet Fitness", FOCUS EXERCISE Barbell Bench Press 4 Sets • 7 Reps • 100 lb | Award on top, upright device |
| 2 | ★★★★★ "“Took the guesswork out of making progress”" | Recovery body map: "3 DAYS SINCE YOUR LAST WORKOUT", "5 FRESH MUSCLE GROUPS" | Testimonial used as the headline |
| 3 | "CUSTOMIZE YOUR EQUIPMENT" | Equipment picker (Most used/All/Selected): Dumbbells, Squat Rack, Handle Bands, Ab Crunch Machine | The "Dumbbells" row pops out as a floating card |
| 4 | "KNOW HOW MUCH TO LIFT" | Back Squat logging 8 × 185 lb "Bar + Plates", chips 1:30 rest / History / **Replace** | **Apple Watch overlay** showing the same set ("8 REPS 185 POUNDS", "Log Set") |
| 5 | "PROGRESS WITH CONFIDENCE" | Trophy "New Strength Record!", "DUMBBELL ROW Estimated Strength 47.5 lbs in 1 Rep" chart | No device, floating card |
| 6 | "HIT YOUR WEEKLY GOALS" | Weekly Set Targets 43%: Push 15/30, Pull 6/30, Leg 18/30 | The Pull row pops out |
| 7 | "TRACK YOUR PROGRESS" | "Overall Strength 68", mSTRENGTH per muscle group | Device |
| 8 | "LEARN PROPER TECHNIQUE" | Exercise video, Instructions / Target / Equipment | Device |
| 9 | "FIND ALTERNATIVE EXERCISES" | Floating cards "Romanian Deadlift ⇄ Good Morning" with an arrow; phone "Replace Romanian Deadlift → Replace with: ↓Best" list + Search | Swap visual above, device below |
| 10 | "“With Fitbod I can work out how and when I want. It's like having a personal trainer, without the pressure or the price tag.”" \| "3 years training with Fitbod" | Full-bleed photo of a lifter | No UI |

- The 5.5" set (older devices) is one running sentence across red slides, with a tilted-phone panorama on 1–2:
  - 1–2: "Smart workouts built just for you" + "APPLE Editor's Choice", "★★★★★ 250,000 Reviews".
  - 3–10: "Fitbod learns from your previous workouts..." / "To pick your next best exercises, reps & weight." / "Focus on the right parts of your body and..." / "Keep your workouts fresh and varied..." / "So you can shape up, slim down or gain strength..." / "Without any planning or guess work..." / "Get a workout at your gym, home or hotel..." / "Make fitness a habit so you can reach your goals."
  - These include a goals onboarding screen (Build muscle & gain weight / Get lean & defined / Reduce bodyweight / Get stronger…).
- Watch tab (7 images, raw UI, no captions): "Log Set & Next", "1/4 Logged", "RESTING 0:42 Next set: 5 reps 95 lbs", timer, exercise videos, WARM-UP.
- The word "AI" appears in no screenshot. It appears only in the subtitle ("AI Personal Trainer & Workouts") and the description.

### Alpha Progression (1462277793): 8 screens

Look: light-blue gradient on 1–2, navy on 3–8, white bold headlines, dark UI.

| # | Headline / subtext | Feature shown | Presentation |
|---|---|---|---|
| 1 | (none) | Routine editor "PPL-Upper-Lower", Push Day 2, "6 exercises · 19 sets", Save | Large tilted device, cropped |
| 2 | "Build muscle, build strength" \| laurels "APP OF THE DAY", "★★★★★ 4.9 x 39,000" \| "Chris (27) 1 year with AP" | Before/after body photos with an arrow | No UI |
| 3 | "Progression on autopilot" | Squats logging, "3 warm-up sets", LB/REPS/10RM, suggested next set 220 × 8 highlighted, "Yesterday · Legs" | Device |
| 4 | "Custom muscle building programs" | Routine editor again (upright) | Device |
| 5 | "Learn and perfect 795 exercises" | Exercise video + Setup / Execution text | Device |
| 6 | "Stay motivated and achieve your goals" | Workout summary: star 71, "66th workout", "0:55 hours", "**9w streak**", PR medals, muscle % | Device |
| 7 | "Visualize your progress" | Charts for training frequency, Bench Press 10RM, bodyweight | Device |
| 8 | "Periodization, RIR, Deloads" | "4 Weeks" sheet: sets / reps / RIR per week + deload row | Blurred background, sheet in focus |

- No Apple Watch app.
- Heavy jargon (10RM, RIR). The description says "Beginners and advanced lifters get fundamentally different plans", but the screenshots don't show this.

### Ladder (1502936453): product-page 6.5" set, 10 screens

Look: neon yellow/white, heavy extended caps, coach photos inside the UI, tilted-phone panorama on 1–2.

| # | Headline / subtext | Feature shown | Presentation |
|---|---|---|---|
| 1 | "LADDER" \| "GET STRONGER, WITH A PLAN." \| laurel "App Store App of the Year 2025 Finalist" | Home: team "Define", week check-marks, "STRENGTH X PILATES 60 min", "23,340 Completions", "**8,540 sent**" ring + teammate avatars with flames; tabs Workout/Chat/Teams/Nutrition | Tilted panorama |
| 2 | (none) \| laurels "2026 Women's Health Best Overall Workout App", "2026 CNET Best Strength Training App" | In-workout screen "42:30 • 76% • ♥94", "Set 2 of 3 8x Bicep Curl", timer dial 0:28 | Panorama continued |
| 3 | "A PLAN FOR EVERY WORKOUT" | Home "LIMITLESS", "PEACH PALACE 60 min • Lower Body Strength", "35,860 Completions", "6,350 sent" | Upright device on white |
| 4 | "TRACK MACROS" | Camera food scan ("Est. Accuracy", modes Voice / Text / **AI**) + Nutrition screen "520 Calories left", "22 Protein Left (g)", Macro Journal | Two phones |
| 5 | "FIND THE PERFECT PLAN FOR YOU" | Coach Kelly "LIMITLESS" (Skill Level, Workout Style, Suggested Equipment, Designed For) + grid of coach plans (FORGED, TRANSFORM, CREWS CONTROL…) | Two phones |
| 6 | "GET COACHED THROUGH IT ALL" | Coach video intro "PYTHON PUMP", Barbell / Dumbbells / Cable Machine, START WORKOUT | Device |
| 7 | "LEARN CORRECT FORM" | Follow-along video: Goblet Squat, 10 reps, 0:28, 25 lbs, fire emojis | Device |
| 8 | "TRACK YOUR PROGRESS" | Romanian Deadlift "186 lbs Estimated 1RM", "↑12% Since you started", History with Effort % | **Apple Watch Ultra overlay** (2:30, BPM 89, MAX HR 56%, ZONE 1) |
| 9 | "LISTEN TO YOUR OWN MUSIC" \| "Select your music or podcasts to get in the zone." | Spotify / Apple Music / YouTube Music / amazon music / Podcasts | Device |
| 10 | "GET ANSWERS TO YOUR QUESTIONS" | Team Chat "Body & Bell": "Hey everyone! I'm new to the Ladder app and that welcome workout has sealed the deal for me…" → reply "It's so worth it! Welcome to the team!…" + pinned coach video | Device |

- The 5.5" set has 2024 awards and "PREVIEW EVERY MOVEMENT" instead of "TRACK MACROS".
- Watch tab: 1 image ("BANDED DEADLIFTS" 00:28 ring, 121 BPM, 243 CALS).
- No "AI" in the plan pitch. The plans are coach-made.
- My guess about "sent" is unverified: its meaning is not labeled; it may count team high-fives or messages.

### Gymverse (1048454034): video + 9 screens

Look: purple glow background, white italic heavy caps, floating chips and cards.

**Video, 35 s, no caption cards.** Sequence:
1. My Plan.
2. Body-map muscle picker → "Choose the muscles you would like to emphasize (We recommend up to 3)".
3. Plan with swap icons → START.
4. Exercise video with form cues "Pull bar to collarbone" / "Squeeze shoulder blades" / "Return with control".
5. Ranking 74%.
6. T-Rex share card.

| # | Headline / subtext | Feature shown | Presentation |
|---|---|---|---|
| 1 | "TURN YOUR GYM GOALS INTO RESULTS" \| "20M+ DOWNLOADS", "300K+ 5 STAR REVIEWS" | Woman doing a dumbbell row | Lifestyle photo, no UI |
| 2 | "WORKOUTS BUILT AROUND YOU" | My Plan "Week 1/6 - Foundations", Full Body, 7 Exercises 57 Min 252 Cal, swap icons, START WORKOUT | Floating chips "Choose Goal", "Muscle Focus", "Equipment" |
| 3 | "BREAK RECORDS HIT YOUR GOALS" | "Level: 3", "Lift 185 lb to level up", "Ranking: 74% — You are stronger than 74% of trainees with a similar profile to yours.", "Goal achieved for this plan!" | Card pops out of the device |
| 4 | "FULL WORKOUT MANAGEMENT" | **Swap**: floating cards "Standing Dumbbell Curl ⇄ Standing Cable Curl" with a yellow arrow; Day 1 editor with delete / reorder | Floating cards + device |
| 5 | "AI-OPTIMIZED SETS WEIGHTS & REPS" | "Suggested 70 lb (Last 65) / 10 reps", "Hit 70 lb for a new PR!", popup "How many more reps could you do? This will optimize your next workout!" 0 / 1 / 2 / 3+ | Popped card |
| 6 | "TRAIN EFFICIENTLY FEEL THE RESULTS" | "GREAT JOB!" 7 exercises / 18.6K lb / 249 cal; share card "I LIFTED THE WEIGHT OF 1 T-REX DURING MY WORKOUT" + T-Rex image, SHARE | Device |
| 7 | "PHONE-FREE TRAINING" | Two Apple Watch Ultras: Muscles Worked; Barbell Hip Thrust video | Watches only, no phone |
| 8 | "AT HOME, THE GYM OR ON THE ROAD" | Bodyweight Training Full Body list | Device |
| 9 | "JOIN 20M+ USERS WORLDWIDE" \| ★★★★★ "“This app is incredible. It kept me focused on the work, and I'm finally seeing results.”" | Floating round user photos + flame emojis | No UI |

- Watch tab (8 images): Your Plan → Start Day 1; Log "Suggested 185 lb / 10-12 reps / Did It"; Videos; Exercise List; Muscles Worked; Rest timer; "GREAT JOB!"; "Week 10 Completed Plan".

### Strava (426826309): product-page video + 9 screens

Look: black-to-orange gradient, white rounded sans headlines, orange device frames.

**Video, 40 s.** Orange caption cards between UI clips:
1. "Track your workouts" → sport picker / map START.
2. "Share with friends & earn kudos" → feed.
3. "Improve with personalized data" → Progress / Performance Predictions / Goals.
4. "Compete with millions" → segment leaderboards → logo.

| # | Headline | Feature shown | Presentation |
|---|---|---|---|
| 1 | Apple logo "Apple Watch App of the Year" \| "Winner" \| STRAVA | Feed "Squad Run" + Apple Watch Ultra "Coastal Trail Climb", PR badge, "▲2s ahead" with a friend's avatar | Award + watch overlay |
| 2 | "Get motivated by the community" | Comments: "Let's goooooo!!", "W😮W! Absolutely crushed it", "Appreciate you captain!" | Device |
| 3 | "Track your workouts" | Record screen: map + Choose a Sport | Device |
| 4 | "Lift it. Log it. See your gains." | "Night Weight Training": front/back muscle heatmap, Total Volume 4,115 lbs, Total Sets 47, Avg Heart Rate 98 bpm, source label "Runna" | Device |
| 5 | "Hit the trails with hiking tools" | Route map + popped card "Gerbode Valley Loop… 21 recent activities" | Device + popped card |
| 6 | "Share with friends" | Post with "12 gave kudos", comment "Great to see you out!" | Device |
| 7 | "Improve with personalized data" | 384.6 mi ▲12%, "You've logged 12% more distance than in the previous time period." | Device |
| 8 | "Discover new routes" | Route card "Made for you" | Device |
| 9 | "Sync with your devices" | Activity + Garmin Forerunner overlay | Device + watch overlay |

- The 5.5" set has no video and adds slide 10 "Compete against millions" (leaderboards).
- Watch tab: 3 images (run metrics, Record → Outdoor Run Start, Save).

### Liftoff (6448081563): the required extra app, top-grossing #59, 10 screens

Look: light-blue/white background, heavy caps in two tones (blue + black), game-style UI.

| # | Headline / subtext | Feature shown | Presentation |
|---|---|---|---|
| 1 | "LIFTOFF" \| "TURN YOUR WORKOUTS INTO A GAME" \| laurels "4,000,000+ MEMBERS", "4.8 stars 130,000+ reviews" | Lv. 37, 🔥35 (streak), 200 gems, "Ranked Bodygraph" (TITAN / CHAMPION / OLYMPIAN), Global/Regional leaderboard | Tilted panorama |
| 2 | (none) | Panorama continued | |
| 3 | "GET YOUR RANK ON OVER 500 EXERCISES" | "GOLD III · 87 LP", Global #13278 Top 46.7%, Regional #4359 | Device |
| 4 | "EASILY TRACK YOUR WORKOUTS" | Logger with SET / PREV / LBS / REPS, warm-up "W" row | Device |
| 5 | "INSTANTLY IDENTIFY MUSCLES TO IMPROVE" | Bodygraph + Muscle Rankings (Chest GOLD, Upper Chest SILVER III) | Device |
| 6 | "CHALLENGE YOURSELF IN THE LEADERBOARDS" | Friends / Global / Regional tabs, podium, "#2 Christopher Top 33.3%"; tabs Streaks / Ranks / Levels | Device |
| 7 | "SHARE YOUR JOURNEY WITH FRIENDS" | Friends feed: "Hitting legs, feeling faint 💀", Streak 🔥4, Record ⭐2 | Device |
| 8 | "BUILD YOUR STREAK STAY CONSISTENT" | "35 current streak!", Season Rewards chests (35 / 60 / 90 / 115), "+25 For Next Chest", season calendar | Device |
| 9 | "CREATE AND SHARE ROUTINES" | Routines: "Tuesday Arms 💪", "Full body burn 🔥", Create Routine | Device |
| 10 | "TRACK CALORIES WITH A SNAP" | Food photo with floating chips 752 kcal / 23g protein / 43g carbs / 15g fats | Cal AI-style |

- Watch tab (6 images): My Routines → START → set "PREV 360 x 2" 220 × 8 ♥81 → Rest Timer ±15 / Skip → Workout Summary.

### Hevy (1458862350): bonus, top-grossing #38, 10 screens

Look: light grey with a blue band, black/blue caps. Content is the same in both sets.

| # | Headline | Feature shown | Presentation |
|---|---|---|---|
| 1 | "LOG WORKOUTS / GET STRONGER / STAY MOTIVATED" \| "★★★★★ Apps We Love" | Log Workout; note "Feeling strong today! Next session increase the weights for the last two sets." | Completed green set rows pop out across the 1→2 panorama |
| 2 | HEVY logo only | Panorama continued | |
| 3 | "ANALYZE YOUR WORKOUTS" | Squat chart + Personal Records | Device |
| 4 | "PLAN YOUR ROUTINES" | Start Empty Workout / New Routine / Explore | Device |
| 5 | "JOIN A GROWING COMMUNITY" | Feed post with likes and comments, "Suggested Athletes", "+ Invite a friend" | Device |
| 6 | "TRACK MEASUREMENTS" | Progress Pictures (before/after 2022 → 2024), body weight | Device |
| 7 | "COMPARE YOUR STRENGTH" | "jaumeros VS strongdavid", "STRONGER" badge, One Rep Max ↑16% | Device |
| 8 | "FOLLOW FRIENDS' PROGRESS" | Profile with Follow button, "Trying to gain muscle!", "3 hours this week" | Device |
| 9 | "LIBRARY WITH HQ VIDEOS" | Exercise search with equipment / muscle filters | Device |
| 10 | "SLEEK DARK MODE" | Dark feed | Device |

- Watch tab (5 images): Sync Routines; Live Sync; "Previous: 50.0kg x 7"; rest "Next set … Set 4/9" ±15s.
- "Hevy Trainer" (a program builder) is in the description only, not in the screenshots.

### Gravl (6450921637): bonus, "AI Personal Trainer", top-grossing #78, 10 screens

Look: black/navy, white sans headline with a neon-lime second line.

| # | Headline | Feature shown | Presentation |
|---|---|---|---|
| 1 | "GRAVL" \| "Get stronger. Every session." \| "4.9 ★★★★★ 50K+ App ratings" (global claim; US shows 5,948) | Home: gym "Nine Fitness", "0 of 4 completed this week", NEXT WORKOUT, "100 Recovered", "Feeling like something different?" with a tile "**Let our AI help you**" (tiny, partly hidden behind the tab bar) | Tilted panorama |
| 2 | (none) | In-workout photo + pills "8-week streak going strong", "Bench Press +30 lbs in 6 weeks", "Strength score up 19 points" | Floating outcome pills |
| 3 | "Progressive overload, automated." | Back Squat warm-up / effective sets, "↑ Score target" | Device on white |
| 4 | "Perfect your form. Guided exercises." | Full-screen trainer photos | Two phones |
| 5 | "Progress you can actually see." | Strength Score 285 "Elite", "15 to Olympic" | Device |
| 6 | "**Machine taken? Swap it.**" | "Swap exercise": Barbell Row ⇄; "SAME MUSCLE · BACK": Pull Up ✓, Dumbbell Row, Chin Up…; "Swap exercise" button | Device |
| 7 | "Train from your wrist." | Live-activity card "Barbell Row Set 2/3 - 10 reps - 60kg" + two Apple Watch Ultras (rest 2:26 ♥72; "Back Squat … LOG") | Watches + card, no phone |
| 8 | "Recover as hard as you train." | Muscle Recovery 94% | Device |
| 9 | "Real coaches. In your pocket." | Group photo of trainers; chat bubbles "Can I swap bench press for dumbbells today?" → "Done. Swapped it and adjusted your weights 💪" | Photo + chat bubbles, no UI |
| 10 | "Train with your friends." | Compare-progress chart; leaderboard "#1 Matías Last trained about 6 hours ago +14 this week", "#2 You", "Aaron Last trained 12 days ago" | Device |

- The description says "Gravl is an AI personal trainer" and does not mention human coaches. Whether the chat on screen 9 is AI or human is **unclear**.
- Watch tab: 3 images.

---

## 2. Findings by focus area

### A. How AI and personalized plans are presented
- **Almost nobody puts "AI" in a headline.**
  - Fitbod sells the result: "SMART WORKOUTS BUILT FOR YOU", "KNOW HOW MUCH TO LIFT". Its 5.5" set says "Fitbod learns from your previous workouts… To pick your next best exercises, reps & weight."
  - Gravl (AI in its name) says "Progressive overload, automated."
  - Alpha says "Progression on autopilot".
  - The only "AI" headline is Gymverse #5, "AI-OPTIMIZED SETS WEIGHTS & REPS", in 5th position.
- **Ladder (#2 grossing) avoids AI entirely.** It sells human coaches: "A PLAN FOR EVERY WORKOUT", "FIND THE PERFECT PLAN FOR YOU", "GET COACHED THROUGH IT ALL". AI appears only as a mode chip in its food scanner.
- **Typical structure: inputs as chips, output as a ready plan.** Gymverse uses chips "Choose Goal / Muscle Focus / Equipment" over a ready plan with START. Fitbod shows a gym profile ("Planet Fitness") plus duration on the plan.
- **Feedback loop is shown as a small popup.** Gymverse: "How many more reps could you do? This will optimize your next workout!"
- **Conversational AI editing is shown only by Gravl #9**, as two chat bubbles (a request → "Done. Swapped it and adjusted your weights"). This is the closest analogue to Lightweight's top button ("I have an injury / redo my workout").

### B. Injuries, limitations, equipment and swaps
- **Injuries / limitations / pain: none of the 8 apps** mentions them on any screenshot or watch image. A keyword search of their descriptions ("injur", "pain", "limitation") also found nothing.
  - This is a gap in the category (my inference) that Lightweight's limitation-aware "Build a plan" and AI edit could fill.
  - It needs non-medical wording.
- **Equipment:**
  - Fitbod #3 "CUSTOMIZE YOUR EQUIPMENT" (picker with a popped-out card).
  - Gymverse "Equipment" chip and #8 "AT HOME, THE GYM OR ON THE ROAD".
  - Fitbod 5.5": "Get a workout at your gym, home or hotel...".
  - Gym selectors: Fitbod "Planet Fitness", Gravl "Nine Fitness".
- **Exercise swap gets a dedicated slide in 3 apps:**
  - Fitbod #9 "FIND ALTERNATIVE EXERCISES".
  - Gymverse #4 "FULL WORKOUT MANAGEMENT".
  - Gravl #6 "Machine taken? Swap it."
  - The visual standard is **two floating exercise cards with a ⇄ arrow**, readable at a glance.
  - Gravl's headline is a gym situation in question → answer form.
  - Fitbod and Gravl show an automatically suggested list ("Replace with: ↓Best", "SAME MUSCLE · BACK").

### C. Social: friends, streaks, community
- **Strava** makes community the core:
  - #1 friend comparison on the wrist ("▲2s ahead").
  - #2 "Get motivated by the community", shown through real-looking comments.
  - #6 "Share with friends" (kudos).
  - Video: "Share with friends & earn kudos", "Compete with millions".
- **Ladder** shows social as support, not competition:
  - Teams.
  - Social proof on every workout card ("35,860 Completions").
  - A "sent" counter with teammate avatars.
  - #10 team chat where a newcomer is welcomed.
- **Liftoff** turns all 10 slides into a game:
  - Leaderboards with a Friends tab.
  - "BUILD YOUR STREAK STAY CONSISTENT" (streak 35 + season chests + calendar).
  - Friends feed showing streak and record per post.
- **Hevy:**
  - "JOIN A GROWING COMMUNITY", "COMPARE YOUR STRENGTH" (VS + "STRONGER" badge), "FOLLOW FRIENDS' PROGRESS".
  - "Invite a friend" button visible.
- **Gravl:**
  - "Train with your friends." with "Last trained 12 days ago" (an implicit accountability nudge) and "+14 this week".
  - "8-week streak" pill.
- **Alpha:** "9w streak" in the workout summary.
- **No app shows a two-person shared streak or a "kick/nudge" push.** Lightweight's Gym Bro (shared streak + kick) is therefore not shown anywhere in the category (my inference).

### D. Apple Watch
There are two treatments:
1. **Watch overlaid on a phone screen, as proof of sync** (the same set shown on both): Fitbod #4, Ladder #8, Strava #1. Strava #9 does the same with a Garmin.
2. **A dedicated "without the phone" slide:**
   - Gymverse #7 "PHONE-FREE TRAINING".
   - Gravl #7 "Train from your wrist." Gravl's description backs it: "standalone Apple Watch app… finish a whole session from the watch".

- Strava puts the watch on screen 1 together with an award. No strength app shows the watch in its first 3 screens.
- Hevy, Liftoff and Alpha have no watch in their phone screenshots. Hevy and Liftoff show it only in the Watch tab; Alpha has no watch app.
- Watch-tab images are raw UI with no captions: set logging with "Previous", rest timer ±15s, heart rate, summary.

### E. Making a beginner feel the app is for them
- The word "beginner" appears in **no** headline. The signals are indirect:
  - "built for you / around you" (Fitbod, Gymverse); "Find the perfect plan for you" (Ladder).
  - Answering the beginner's main question: "KNOW HOW MUCH TO LIFT" (Fitbod), "Suggested 70 lb… Hit 70 lb for a new PR!" (Gymverse).
  - Technique slides in 5 of 8 apps: "LEARN PROPER TECHNIQUE", "LEARN CORRECT FORM", "Perfect your form. Guided exercises.", "Learn and perfect 795 exercises", "LIBRARY WITH HQ VIDEOS". Gymverse's video adds form cues ("Squeeze shoulder blades").
  - Testimonials that lower intimidation: Fitbod "…like having a personal trainer, without the pressure or the price tag."; "Took the guesswork out of making progress"; Gymverse "…I'm finally seeing results"; Ladder chat "I'm new to the Ladder app…".
  - Location flexibility: home, hotel, on the road.
- Counter-examples aimed at experienced lifters: Alpha ("Periodization, RIR, Deloads", 10RM) and Liftoff (ranks, LP).

---

## 3. Transferable patterns for Lightweight (mapped to confirmed features; items to verify are flagged)

1. **Swap slide.**
   - Use the established visual: two floating exercise cards with ⇄.
   - Use a situational headline like Gravl's ("Machine taken? Swap it.").
   - Show Lightweight's real flow: swipe → exercise catalog → pick → auto-replaced.
   - Do **not** copy Fitbod/Gravl's "suggested same-muscle alternatives" list unless Lightweight actually does that (VERIFY).
2. **AI edit slide in chat-bubble form** (Gravl #9 pattern): the user's request about what's off today → "Done" with the plan changed.
   - No competitor shows adapting to a limitation, so this is the strongest gap to claim.
   - Requirements: non-medical wording, present it as an app function (not as Seryozha or a coach), and avoid "injury" promises.
   - VERIFY the exact behavior and inputs of the top button and of "Build a plan" (goal, days, equipment, limitations?).
3. **Sell the outcome, not "AI".** Use "built for you" + "know how much to lift" phrasing. Show the inputs as chips and the result as a ready plan (Gymverse #2).
4. **Apple Watch:** use the overlay-on-logging treatment (Fitbod #4) now. Make a "phone-free / from your wrist" slide only after verifying standalone operation (the owner has flagged this as unverified).
5. **Gym Bro:**
   - Show human interaction, not mechanics: Strava-style comments/kudos, Ladder-style welcome.
   - Show the kick as a floating notification card (floating pills like Gravl/Gymverse).
   - Don't describe streak rules (owner's rule).
   - Category gap: nobody shows a duo streak or a nudge.
6. **Strava integration proof:** Strava #4 shows exactly how a lifting session appears in Strava (muscle heatmap, volume, sets, average heart rate, source-app label). A "your lifts show up on Strava" slide is concrete. VERIFY which fields Lightweight's upload contains.
7. **Hero slides:** the 1–2 panorama with a tilted device is standard (Ladder, Liftoff, Gravl, Hevy, Fitbod 5.5"). Everyone puts social proof or awards on 1–2.
   - Lightweight has none, so it needs a concrete product promise instead.
   - Use true numbers only (for example the real exercise-catalog count; VERIFY).
8. **Trend relevant to Cal AI:**
   - Two top-grossing gym apps now include Cal AI-style photo calorie tracking: Ladder #4 "TRACK MACROS", Liftoff #10 "TRACK CALORIES WITH A SNAP". Cal AI itself is top-grossing #12.
   - Lightweight has no food tracking, so don't show it.
   - Its analogous "snap" feature is import of a program from a photo/screenshot (my inference about positioning).
9. **Dinosaur collision risk:** Gymverse already uses a T-Rex share card ("I LIFTED THE WEIGHT OF 1 T-REX DURING MY WORKOUT") in screenshot #6 and in its video. Seryozha (the dino mascot) needs to look clearly different.
10. **Format norms:** 2–6-word headlines, one feature per slide, 8–10 slides, dark UI. Only Gymverse and Strava use an app preview video: Gymverse shows UI only, Strava alternates caption cards with UI.

---

## 4. Corrections to existing repo research (not edited, for the owner/parent)
- `aso/research/screenshots.md` says the shelf images match the lookup `screenshotUrls`. That is false for Fitbod, Ladder, Strava and Hevy (lookup = 5.5" set). Its Fitbod and Hevy tables do match the product-page set, so its content is still valid.
- `screenshots.md`: "No app in this set showed a video preview". Gymverse now shows a 35 s app preview first on its product page.
- `screenshots.md` cross-app point 6 ("Apple Watch, friends/streaks not in first 3") still holds for the strength apps. Strava and Liftoff (not in that set) do show them in their first screens.

## Files
Everything is under `/tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/comp-b/`:
- **Product-page screenshots (what current iPhones show):** `data/<app>/page_phone/NN.jpg`
- **Lookup-API screenshots (5.5" set for Fitbod, Ladder, Strava, Hevy):** `data/<app>/NN.jpg`
- **Apple Watch tab images:** `data/<app>/page_watch/NN.jpg`
- **Raw data per app:** `data/<app>/lookup.json`, `page.html`, `media.json`
- **App preview videos:** `data/gymverse/video/video.mp4`, `data/strava/video/video.mp4`
- **Top-grossing feed:** `data/topgrossing_hf.json`
- **Description keyword hits:** `data/desc_kw_1.txt`
- **Side-by-side contact sheets:** `sheets/`
- **Video frame sheets:** `sheets/video/`
- **Zoomed crops:** `sheets/crops/`
- **Scripts:** `scripts/`

## Mascot apps and AI-edit visualization

# Mascots and AI "describe a change" features in App Store screenshots: what top apps do, and rules for Seryozha

I downloaded the full US iPhone screenshot sets of 28 apps on 2026-10-21 and looked at every image. The answer in three points:

- **Mascot:** in the apps that work best, the mascot sits next to a headline that explains the product. It never replaces that headline, and it stays out of the screenshot that sells the AI feature. Duolingo keeps its owl out of screenshots 1–5 entirely.
- **AI edit:** the clearest example (Thelo) fits the whole chain into one screenshot: a short request from the user, a one-line reply, a card saying what changed, then the updated plan.
- **Correction to our draft:** your description of exercise swap does not match draft slot 7. The draft shows a "Swap sheet" with suggested alternatives. In the app, swiping an exercise opens the catalog and your pick replaces it. That slot needs redesigning (rule A9).

Mascot size is my estimate by eye. "Slot" means the position in the lookup's screenshot list. The product-page HTML had no app preview videos, but I did not check on a device. Ratings are US counts from the lookup.

## 1. Mascot-led apps

| App (US ratings) | Mascot in icon | Slots with the mascot | Size | Mascot carries headline? | Speech bubbles | Tone | Product clear in first 3? |
|---|---|---|---|---|---|---|---|
| **Duolingo** (5,516,319) | Yes (Duo) | Duo appears only in slot 6, plus a tiny one inside the lesson screen in slot 8. Other Duolingo characters appear inside lesson screens in slots 3–5 | About 20% of frame height | No. Headlines are lowercase captions on coloured pills at the bottom ("learn 40+ languages for free", "fun, bite-sized lessons", "keep your daily streak") | Real in-app bubbles: "Keep it up! I'm off to brag about your streak."; "Move here to checkmate." | Playful, and the humour lives in the app screens | Yes: course list, lesson, chess puzzle |
| **Finch** (765,831) | Yes | 7 of 8. Slot 1 is illustration only (no UI): two birds hugging | About 50% in slot 1 | No: "Self-care is better together" | In-app: "Nourish what matters to you, cheep!", "You kept going for a whole month! Every day! WOW!" | Warm, never sarcastic | Partly. Slot 1 has no UI; slot 2 shows a habit checklist. The pet is the product here, so this is a weak comparison for us |
| **Habitica** (3,541) | Gryphon logo | User's pixel avatar: small in slot 1, large in slot 4 (reward scene), pets break out of the frame in slot 5 | About 35% in slot 4 | No | None | Game-like | Yes: task lists |
| **BitePal** (56,442), the closest comparison (a tracker plus a mascot with attitude) | Yes (raccoon) | Slot 1 is a hero illustration with no UI: "Food tracker pet" plus an App of the Day badge. **Slots 2–3 have no mascot.** Slot 2 is the AI slot ("Scan your meal", "Powered by AI"). From slot 4 on, the raccoon appears inside the app screens or as a sticker peeking over the phone corner (slots 6 and 8). Slot 10, "Keep your streak", shows a lock-screen card with a grumpy raccoon in sunglasses and the line "21 · 2:29:16 · Your last chance!" | About 40% in slot 1, 15–25% as a sticker | No. Headlines are 2–3 word category labels | Only one line inside the app UI | The attitude comes from his pose and face, not from text | Yes: slot 1 names the category, slots 2–3 are pure product |
| **Gentler Streak** (8,827) | Yes | Slots 1 (small, inside the app screen), 3 (large, decorative under the UI), 4 (large, arms crossed, on the privacy slide; no UI), 9 | 10–45% | No | None | Gentle | Yes |
| **Liftosaur** (426), a dinosaur lifting app | Yes (dinosaur with barbell) | Slot 1 only (bottom-left), plus a tail peeking in slot 6 | About 35% | No: "The most powerful weightlifting planner and tracker app" | None | Neutral | Yes. Slot 1 also says "It's like Google Sheets meets Strong!", which names a competitor (a 2.3.7 risk; do not copy) |
| **Capy Diet** (2,417) | Yes | Slot 1 is a hero illustration with no UI ("Meet Capy, Your new diet coach"). Slot 2 has an in-app bubble "You're doing great! Keep it up!". Slot 7 has a bubble outside the phone, "You can do it!" | About 45% in slot 1 | Partly (slot 1) | Inside and outside the phone | Generic praise | Weak |
| **Bearable** (6,510) | Yes | Slot 1 (under the social proof), tiny inside the app screen in slot 3 | About 25% | No | None | Neutral | Yes |
| **GymStreak** (15,913) | Yes | Only as a tiny round button with eyes, bottom-right. **The mascot is the AI button** | Under 5% | No | None | Neutral | Yes |
| **Tolan** (185,816) | Wordmark | The character is the product. Voice is shown with bubbles outside the phone, a mic button and a "Chat in Voice Mode!" sticker | Large | No | Outside the phone | Warm | Not applicable |
| **GymRoast: Lifting Tracker** (0 ratings) | Flexing arm | No mascot. Slot 1: "Finish a set. Get roasted. The meanest spotter in your phone." with a roast card over the set log: "You lift weights because your face needs backup." Slot 3: "33 days without a PR? It says it to your face — so you fix it." with an in-app line "33 days without a PR — check your plan" | – | – | A card popping out over the log | Insults about looks | Yes |
| **GymRoast - AI Gym Tracker** (0 ratings) | – | No mascot. The roast lives in app text: "Unless you chicken out... again", "Prove you didn't bail", "Analyzing your sweaty existence..." | – | – | – | – | Yes |

Fabulous and ParrotPal show no mascot at all. ParrotPal mentions voice logging only inside a quoted review.

**Age rating:** both GymRoast apps declare "Infrequent/Mild Profanity or Crude Humor" (9+ in the lookup). Habitica, Tolan and MacroFactor declare the same. This supports `aso/research/apple-rules.md` §10.

**Patterns (observations):**
1. No app lets the mascot replace the explaining headline. When a mascot is the hero of slot 1 (BitePal, Liftosaur, Capy), a category label sits next to it ("Food tracker pet", "weightlifting planner and tracker").
2. The biggest mascot brand keeps the mascot out of slots 1–5. It lives in the icon and in one emotional slot (the streak).
3. Speech bubbles are almost always real in-app lines (Duolingo, Finch, BitePal, Capy slot 2), not marketing narration. They run 1–2 short lines.
4. The attitude comes from pose and face plus one line of 5 words or fewer ("Your last chance!").
5. Outside the hero slot, the mascot is a sticker covering 15–25% of the frame, overlapping the phone edge or corner. It never covers the numbers that prove the claim.
6. BitePal's AI slot has no mascot. GymStreak's mascot *is* the AI button, so users will read a mascot shown next to AI as the AI.
7. Roast-led positioning without a mascot (both GymRoast apps) has 0 US ratings. There is no evidence that it drives installs.
8. 9 of the 11 mascot or character apps checked put the character in the icon. Recognition is built there, not in screenshot 1.

## 2. How apps show "describe a change → result"

| App (ratings), slot | How it is shown |
|---|---|
| **Thelo** (2,387), slot 10 "Your personal AI coach". The best single-frame chain | User bubble: "I've been in a chair for 9 hours. Brain is mush. I really can't deal with heavy squats right now." → AI bubble → a "SMART ADJUSTMENT" card ("FATIGUE SIGNAL DETECTED", "LOW", "Swapped heavy lifting for machine work. Keeps it safe while your energy is low.", [View modified workout]) → "Today's plan is ready · 3 movements updated · 48 min" with chips "Leg press", "Seated row", "+1 more" → a "Reply to Coach" field. Slot 1 also shows an "Ask thelo anything.." bar with a voice icon. Weakness: "safe" and "frying your lower back" are implied health claims |
| **Saga** (736), slot 6 "ADJUST YOUR WORKOUTS" | A floating before→after card (Machine Assisted Pull Up → curved orange arrow → Machine Pulldown) above the real "Substitute Exercise" picker |
| **Saga**, slot 7 "REAL-TIME COACHING" | A chat: "I'm having difficulty staying upright during squats" → "Would you like me to make this change…?" → "Yes" → system line "Substituted Dumbbell Front Rack Squat for Dumbbell Goblet Squat". Readable only when zoomed in. Workout screens in slots 3 and 5 show an "Ask anything" bar |
| **Gravl** (5,951), slot 9 | Two bubbles over a team photo: "Can I swap bench press for dumbbells today?" → "Done. Swapped it and adjusted your weights 💪". No UI, and it implies human coaches. Slot 6, "Machine taken? Swap it.", shows the swap list. Slot 1's home screen shows "Feeling like something different?" |
| **GymStreak**, slot 4 "AI WORKOUT EDITOR" | A floating panel listing changes with arrows: "Adjust Sets: 3 → 4", "Change Exercise: Barbell Bench Press → Incline DB Press", "Optimize Rest: 90s → 120s". At full size the text is duplicated and garbled, like generated art. An example of what not to do |
| **Cal AI** (371,543), 4 screenshots | Input and output split across two slots joined by one sentence: slot 2 "Just snap a picture of your food" (camera) → slot 3 "Then let us do the rest" (floating labels "Blueberries 8", "Pancakes 595", "Syrup 12", a nutrition card and a "Fix Results" button). **No "describe your meal" text input appears in the screenshots.** |
| **BitePal**, slot 2 | Input and output merged: food photo with ingredient chips, a macro card, and a "Powered by AI" line above the headline |
| **MacroFactor**, slot 4 | Camera with a "Photo / Photo & Text" switch. Shows the input mode only, no result |
| **Zing** (30,761), slot 1 | "I'm feeling good but planning a light workout day." → "Sounds like a plan!…". No change to the plan is visible. Slot 4, "Adapt To You", has an "Adapt Workout" button |
| **Planfit**, **Coachify** | Chats with multi-paragraph answers. Unreadable at thumbnail size, and no change to the plan is shown |
| **Fitbod, Ladder, Fitness AI, MacroFactor Workouts, Fitify** | No typed or voice editing shown. Fitbod sells AI as automatic ("Fitbod learns from your previous workouts…") |

Fitbod's set has changed since `aso/research/screenshots.md` (2026-10-19). Slot 1 now reads "Smart workouts built just for you", and slot 2 shows "250,000 Reviews".

Our reviews research found that lifters push back on AI when it changes the training on its own. Fitbod has 17 AI mentions, 8 of them at 1–2★, and Strong and StrengthLog are praised for "no AI". AI started by the user's own request is probably less exposed to this. That is an inference I have not tested.

## 3. Rules for Seryozha

- **S1. The first three screenshots must make sense without Seryozha.** Test: cover him with a thumb. If it no longer reads as a workout tracker, the slot fails. The headline and the real UI do the explaining.
- **S2. In slot 1 he only peeks.** He takes up 20% of frame height or less and overlaps the phone edge or corner. He never covers the set rows, the "Previous" column or the rest timer. The draft's "peeking from behind the phone edge" fits this. Do not make slot 1 a mascot hero without UI: we have no award or ratings to make up for it, and Guideline 2.3.3 requires more than half of the screenshots to show the app in use.
- **S3. Seryozha never speaks the headline.** Headlines stay in the brand voice. His line lives in a card, bubble or notification that really exists in the app, word for word. One line, 10 words or fewer.
- **S4. Give him one dedicated character slot, late in the set (6–8).** Duolingo does this at 6 and BitePal at 10. Show the trigger, his reaction and the data together, for example a roast card over a workout with a long rest timer or "same weight for 4 weeks" visible. A roast tied to a data trigger reads as a feature (GymRoast slot 3), not as a gag. Keep "Mute him anytime" in the supporting line.
- **S5. Roast the behaviour, never the body, looks or identity.** "Your face needs backup" is the kind of line to avoid: it is insult humour about looks. No swearing, not even masked. Small risk: the draft line "One set and done? Workout or free sample?" contains "free", and App Review has treated "free" as a price reference. Safer to keep the word out of screenshots.
- **S6. Keep Seryozha out of the AI rework, Build a plan and import slots.** Shown next to AI he will read as the AI coach (the GymStreak pattern), which contradicts the owner's rule that he is not an AI coach. BitePal's AI slot has no mascot either.
- **S7. Use pose and face for attitude** (crossed arms, side-eye, as BitePal does). Use the same art style everywhere and show him at most three times in the set: the slot 1 peek, a small cameo on the Friends slot, and the character slot.
- **S8. Recognition comes from the icon.** If Seryozha is meant to be the brand's face, the icon is where most of these apps put the character.
- **S9. Age rating:** answer the age-rating questions with his roasts counted as insult humour, the same way the GymRoast apps did. Screenshots still have to be suitable for 4+ either way.

## 4. Rules for the AI "describe a change → workout rewritten" screenshot

- **A1. One screenshot, three layers, readable top to bottom in about 3 seconds:**
  1. The request as typed text in the real field at the top of the workout.
  2. The rewritten workout in the real UI, with changed rows marked in the orange accent.
  3. Small chips with arrows saying what changed (for example "Barbell Squat → Leg Press").

  If the app does not show a summary of changes itself, the chips may only be a marketing overlay (2.3.3 allows overlays), and they must match what the app really does.
- **A2. The request is a real-life constraint in the user's words, 10 words or fewer.** For example "Only 30 minutes today", "Gym's packed, no barbells", or "Shoulder's bugging me — rework today". Frame injuries as "avoid". Never say safe, heal, rehab or prevent injury; Thelo's "Keeps it safe" is exactly what to avoid.
- **A3. The headline puts the user in control.** For example "Something changed? Rewrite today's workout." At most a small "AI" label above the headline, never "AI" as the main idea. This follows the lifter pushback on AI noted in section 2.
- **A4. No chat walls** like Planfit and Coachify. If the reply is shown, it is one line that starts with the action, for example "Done. 3 exercises changed." (the Gravl pattern), not advice.
- **A5. Do not show it in a coach persona's voice** (like Thelo's "Hold on, Marcus"), and do not attach Seryozha to it (S6).
- **A6. Show a mic only if rework really accepts voice.** You said "type", and voice is confirmed only for program import. If it does work, Tolan's approach is clean: a bubble outside the phone plus a visible mic button.
- **A7. One slot, not two.** Cal AI's two-slot running sentence is clear, but our set is already full.
- **A8. Placement:** Thelo puts this at slot 10, Saga at 6–7, Gravl at 9. None of the 9 lifting leaders shows it in the first 3. Put it at slot 6 or 7, right after Build a plan, or merge it with the swap slot as a "change anything" message.
- **A9. Redo the swap visual to match the real flow.** Swipe an exercise row (a touch-point or swipe overlay is allowed by 2.3.3), the catalog opens, and the row is replaced. Saga's layout fits: the phone shows the catalog, and above it floats a card like "Bench Press → Dumbbell Bench Press" with a curved arrow.

## 5. Questions for the owner (they decide the copy)

1. What is the exact label of the rework button at the top, and the placeholder text in its field?
2. After a rework, does the app show a summary of changes or ask for confirmation? That decides whether the chips are real UI or an overlay.
3. Does rework accept voice?
4. Which exact Seryozha lines and triggers exist in the app? The screenshot needs a real line.
5. "Seryozha" vs "Seriozha": pick one spelling.

## Files

Everything is in `/tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/mascot-ai/`:
- **Raw lookup data:** `data/lookup/<slug>.json`
- **Individual screenshots:** `data/shots/<slug>/NN.jpg`
- **Side-by-side sheets:** `data/sheets/<slug>_N.jpg`. The most useful are `duolingo_1.jpg`, `bitepal_2.jpg`, `thelo_2.jpg`, `saga_2.jpg`, `gravl_2.jpg`, `gymroast2_1.jpg`.
- **Zoomed crops:** `data/sheets/thelo10_crop.jpg`, `gravl09_crop.jpg`, `gymstreak04_crop.jpg`, `bitepal10_crop.jpg`
- **Icons:** `data/sheets/icons.jpg`
- **Search results and product pages:** `data/search/`, `data/pages/`
- **Scripts:** `scripts/search.py`, `scripts/fetch_shots.py`, `scripts/pages.py`

Nothing was written to the git repo.

## Best practices + review mining

# Screenshot best practices and competitor review mining for Lightweight (Oct 2026)

Apple's own documentation is clear that the first three portrait screenshots carry the search result. From iOS 27, a new search-results image or video can take that slot. Apple does not confirm that text on screenshots counts for search ranking (OCR). In the reviews, people ask for exercise swaps and injury handling at Ladder and Fitbod, not at Hevy or Strong. When AI makes big changes to workouts on its own, Fitbod users react badly.

## Part A: Screenshot conversion evidence

Tags: OFFICIAL = Apple. INDUSTRY = ASO vendors (they sell testing tools, so their numbers come from their own data). UNVERIFIED = no method published, or contested.

**1. The first 3 screenshots and portrait search results**
- OFFICIAL: "Depending on the orientation of your screenshots, the first one to three images will appear in search results when no app preview is available." Apple also says to focus each later screenshot on one main benefit. https://developer.apple.com/app-store/product-page/
- OFFICIAL: "Your app's rating and up to three screenshots or app previews may display in search results." Search page: https://developer.apple.com/app-store/search/
- OFFICIAL: up to 3 app previews can show in search results, and previews always appear before screenshots. https://developer.apple.com/app-store/asset-best-practices/
- OFFICIAL: search results are "where 65% of downloads start" (Apple Ads, 2025-12-17). https://ads.apple.com/news
- OFFICIAL: Apple Ads added more ad slots further down the search results in 2026. Organic results get pushed lower. Same link.
- INDUSTRY: the first 1–3 screenshots usually get the most views. 40% of 70+ audited US pages had hard-to-read captions, and 56% failed to show the value proposition (SplitMetrics, 2023-03-16). https://splitmetrics.com/blog/aso-mistakes-affecting-app-visibility-and-conversion-rate/
- INDUSTRY (older): across 1,800 A/B tests, only 11% of people reached the 5th portrait screenshot, against 15% for landscape (SplitMetrics, 2018-03-02). https://splitmetrics.com/blog/apple-screenshots-scroll-depth/
- UNVERIFIED: the StoreMaven figures "60% don't scroll past the first impression" and "3–6 seconds" are widely repeated, but the method was never published.

**2. Headline length and legibility at thumbnail size**
- OFFICIAL: "If using text, use a short phrase that enhances your visual rather than describes it." Apple also says to keep text legible, keep key elements in the safe area and centred, and check them with the new Preview tool. https://developer.apple.com/app-store/asset-best-practices/
- INDUSTRY: captions should be short, high-contrast and large, with no layered or shadowed text and one theme per screenshot. Sources: Appfigures https://appfigures.com/resources/guides/app-store-algorithm-update-2025 and AppTweak (2025-04-09) https://www.apptweak.com/en/aso-blog/how-to-optimize-your-app-screenshots
- UNVERIFIED: rules like "3–5 words" or "16pt minimum" come from vendor blogs with no data behind them.

**3. Benefit-led vs feature-led captions**
- INDUSTRY: AppTweak recommends benefit phrasing ("Track your workouts effortlessly", not "Workout tracker app"), but its A/B guide treats this as a hypothesis to test. Link as in item 2.
- INDUSTRY: Appfigures recommends active, keyword-bearing captions ("Track Sleep Patterns" rather than "Wake Up Refreshed"). That pushes toward feature + benefit wording. Link as in item 2.
- I found no recent, controlled published test of benefit vs feature captions. The "+15–30%" figure has no source.

**4. Social proof (real only)**
- OFFICIAL: "Avoid claims that can't be verified, such as awards or recognition that your app or game hasn't actually received."
- OFFICIAL: "Please don't include any Apple-designated recognitions — such as Editor's Choice, App of the Day…"
- OFFICIAL: "avoid using the entire asset to highlight general accolades or call-to-action statements." No prices, discounts or URLs. All from https://developer.apple.com/app-store/asset-best-practices/
- OFFICIAL: guideline 2.3.14 (creative assets) bans unverifiable product claims. Already covered in `aso/research/apple-rules.md`.
- INDUSTRY: social proof is one of the strongest influences for Health & Fitness (SplitMetrics, 2021-07-30). https://splitmetrics.com/blog/top-health-fitness-apps-trends/
- Observation: Fitbod and Hevy still show "Editor's Choice" and "Apps We Love" laurels on their screenshots, against Apple's current guidance. Lightweight has no real social proof at launch, so it should leave this out.

**5. Panoramic sets**
- OFFICIAL: "An image of an app in use can be displayed across multiple screenshots." https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots
- UNVERIFIED: the "+30% conversion from panoramas" claim traces to vendor blogs with no study. Scroll-depth data (item 1) suggests each frame must work on its own.

**6. Device frames vs full-bleed UI**
- OFFICIAL: Apple says nothing about frames. Apple does require that more than half of the screenshots show the app in use, and that overlays don't crowd out the app. 2.3.3 link as in item 5.
- UNVERIFIED: I found no controlled test of frames vs full-bleed. All advice either way is opinion.

**7. Light vs dark**
- OFFICIAL: "If your app supports Dark Mode, consider including at least one screenshot that showcases" it. 2.3.3 also says to show configurations "such as Dark Mode". The new preview tool can show the store page in Dark Mode.
- INDUSTRY: SplitMetrics (2021) says dark backgrounds perform better for Health & Fitness but shows no data. In an older SplitMetrics test (OLBG, ~2018), a plain background did 10–13% worse than a themed one. https://splitmetrics.com/customers/olbg-ios-screenshots-optimization/
- 7 of the 9 competitors use dark sets (`screenshots.md`).

**8. People and hands**
- INDUSTRY: for Health & Fitness, people exercising in the first screenshots "prompts users to scroll through the whole screenshot gallery". No sample size is given (SplitMetrics, 2021; link as in item 4).
- OFFICIAL limits: most screenshots must show the app in use (2.3.3). 2.3.9 requires rights to all material and fictional account data; model releases for photos of people are a practical consequence of that. Hands: no data found.

**9. App preview video**
- OFFICIAL: previews autoplay muted, are up to 30 seconds, and the first seconds must work silently.
- OFFICIAL, ambiguous: Apple's Simply Piano case study says "The original product page without an app preview video outperformed the treatment", yet the same page shows "Treatment +3%". https://developer.apple.com/app-store/product-page-optimization/
- INDUSTRY: for Health & Fitness, "adding a video might also drop the conversion rate", and most top-grossing fitness apps use no video (SplitMetrics, 2021).
- UNVERIFIED: AppFollow (2026) gives "+7–14%" for Health & Fitness from anonymised client data, and its own note says to review the figures. https://appfollow.io/blog/aso-video-strategies
- In short: test video with Product Page Optimization before relying on it.

**10. How many screenshots**
- OFFICIAL: up to 10. One per device is enough if it shows the app in use.
- From the scroll-depth data, frames 4–10 reach few people. They still matter for people who open the full product page.

**11. Localization**
- OFFICIAL: localize screenshots and text, and localizations can differ. Product page link as in item 1.
- INDUSTRY (older): Chinese screenshots did 33% better than English for Paper by FiftyThree (SplitMetrics, ~2018, no sample size). https://splitmetrics.com/blog/paper-by-fiftythree-how-to-get-33-more-installs-with-screenshots-ab-testing/

**12. Whether Apple reads screenshot captions for ranking (OCR)**
- OFFICIAL: Apple says ranking text relevance comes from "title, subtitle, keywords, and primary category". Screenshots are only described as displayed. Search page link as in item 1.
- OFFICIAL, indirect: in WWDC25 (session 328), Apple said screenshots "hold very useful information" while describing how its AI-generated tags are built. It does not list screenshots as a source. https://developer.apple.com/videos/play/wwdc2025/328/
- INDUSTRY, claimed: Appfigures says caption text became a ranking signal around June 2025. It calls the mechanism speculation and does not cite Apple.
- INDUSTRY, against: AppTweak (2026-02-04) says "There is no conclusive proof" (https://www.apptweak.com/en/aso-blog/ai-reshaping-app-store-relevance). Phiture (2026-03-19) says "This has since been denied by Apple" but links no Apple statement (https://phiture.com/asostack/aso-trends-in-2026/).
- ConsultMyApp tested 64 caption phrases and found 1 unexplained case (reported second-hand).
- **Status: UNVERIFIED.**

**13. Caption keyword placement**
- UNVERIFIED: Appfigures recommends captions at the top, one keyword theme per screenshot, and not repeating keywords already in the name or subtitle. The author writes "This part is speculation."
- Safe approach: put the search words people use in captions for clarity and conversion, and keep every target keyword in the name, subtitle or keyword field.

**14. iOS 26 changes**
- OFFICIAL: App Store tags (AI-generated, human-reviewed, US only) appear in search results and on the product page. https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags/
- OFFICIAL: custom product pages can be assigned keywords and then replace the default page in search results for those keywords. Up to 70 pages. https://developer.apple.com/app-store/custom-product-pages/
- OFFICIAL: the extra search ads need iOS/iPadOS 26.2 or later. This comes from press coverage of Apple's announcement (searchengineland.com, heise.de); I did not see the version on an Apple page.

**15. iOS 27 changes (announced at WWDC26, live 2026-10-05)**
- OFFICIAL: new creative assets.
  - **Product page header**: 21:9 image or 5–30 s video.
  - **Search-results asset**: 3:2 image or video. In search results, videos are always muted.
  - Sources: https://developer.apple.com/news/?id=ljpl7kyn and https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications/
- OFFICIAL: "If you choose to not use a search result creative asset, your In-App Events, app previews, and screenshots will appear." Apple's guidance for this asset: "State the obvious… Showcase the firsthand experience." Shown on iOS/iPadOS 27 and later. https://developer.apple.com/app-store/asset-best-practices/
- OFFICIAL: the Asset Library allows approval separate from app versions. Creative assets can be used on custom product pages and tested with Product Page Optimization. WWDC26 session 205: https://developer.apple.com/videos/play/wwdc2026/205/
- OFFICIAL: iPhone Duo screenshots are required from April 2027.
- Inference: the header pushes screenshots lower on the product page. So on iOS 27 there are two things to design: the search asset and the first screenshots.

## Part B: Recent US reviews

**Sample:** pages 1–3 of the US "most recent" review feed, fetched 2026-10-21, 150 reviews per app.

| App | Date range | Avg ★ | 1–5★ counts |
|---|---|---|---|
| Hevy | 10-14 → 10-19 | 4.89 | 2/0/2/4/142 |
| Strong | 04-03 → 10-19 | 3.77 | 17/16/19/31/67 |
| Fitbod | 09-14 → 10-19 | 3.67 | 35/7/9/21/78 |
| Ladder (id 1502936453) | 10-09 → 10-19 | 4.88 | 2/2/2/0/144 |

Ladder's latest release notes ask users to "Rate and review us", so its 5★ skew is probably prompted.

**How to read the counts:** cells show the regex hit count, then my count after reading every match (labelled "verified"). The number in brackets is how many hits came from 1–2★ reviews.

**Swapping or replacing an exercise** (regex 0 / 2 (0) / 4 (1) / 5 (0))
- Verified: Hevy 0, Strong 1, Fitbod 3, Ladder 5.
- Strong: "What if there was a way to temporarily add/replace workouts ONLY for that session."
- Ladder: "I love how I can just easily swap workouts or equipment or move things around."

**Injury and limitations** (regex 0 / 3 (2) / 7 (2) / 2 (0))
- Verified: 0 / 0 / 6 / 2.
- Fitbod, 5★, title: "Love the New Injuries & Limitations Feature." That feature is not in Fitbod's current store description, so it needs checking in the app.
- Ladder: "it would be nice if there was a setting to show my injuries and automatically replace moves I can't do with something different."

**AI changing workouts** (regex 6 (0) / 4 (0) / 17 (9) / 1 (0))
- Fitbod: 6 complaints that the AI or algorithm changed workouts badly, and 4 positive or neutral comments about the AI coach.
- Strong: 2 anti-AI ("No AI BS just straight to the point") and 1 asking for AI plus import.
- Hevy: 1 praises the app for "not running just on AI to make the workout for you and you can plan your own". 4 users connect ChatGPT or Claude to Hevy themselves.
- Ladder: 0.
- Fitbod: "Had the 'AI Coach' just suggest I jump an excercise from last week by an extra 40 lbs… and it called it 'a conservative jump'."

**Friends, social and accountability** (regex 27 / 17 / 18 / 51)
- Verified (excluding "user friendly", dev "team" and plain referrals): Hevy 16, Strong 4, Fitbod 2, Ladder 16.
- Ladder also has about 22 mentions of its coach-led "Teams".
- Hevy: "A friend and I use it every time we workout to hold each other accountable."
- Ladder: "the encouragement from other users while you're exercising is such a fun motivator."

**Apple Watch** (regex 7 (2) / 42 (18) / 13 (6) / 3 (1); spot-checked)
- Strong is dominated by sync complaints. About 9 Fitbod reviews say the watch stopped working after an update.
- Hevy: 4 praise, 3 sync issues, one of them "a mess on iOS 27".
- Strong: "Watch App Integration bugs on EVERY Workout."
- Hevy: "pairs perfectly with the Apple Watch and you don't even have to touch your phone."

**Importing and switching** (verified)
- Hevy: 7 came from notes, notebook or pen and paper. 1 moved plans in via ChatGPT. 1 praises CSV export.
- Strong: 1 import request, 3 export mentions, 4 leaving or threatening to leave.
- Fitbod: 0 import requests. 2 stay only because they would lose their history.
- Ladder: 1 export request.
- Strong: "the inability to import workouts and lack of Ai comparability is about to make me jump ship."

**Ease and speed of logging** ("easy"-type word plus log/track/record in the same review)
- Hevy 32, Strong 20, Fitbod 4, Ladder 8.
- Hevy: "save my routine so it only takes 10 seconds to start tracking."

**Beginners and plans** (verified beginner mentions: 8 / 0 / 9 / 7)
- 2 of Fitbod's are negative ("only for beginners").
- Ladder: 60 reviews mention a coach or trainer, and 9 say some form of "don't have to think".
- Ladder: "Ladder keeps me from looking like a clueless idiot at the gym."
- Hevy 3★: "feels more like a workout log than an actual training program."

**Mascot, fun and humor**
- "Mascot": 0 mentions in all 600 reviews.
- "Fun": Hevy 1, Strong 1, Fitbod 0, Ladder 5.
- Ladder 2★: "trainers… have zero-personality." Another Ladder review likes "no cheesy motivational stuff."

**What this means for Lightweight (inference):**
- **Exercise swaps:** asked for at Ladder and Fitbod, mainly when a machine is busy. Never mentioned at Hevy.
- **Injury handling:** a real request, but Fitbod appears to have already shipped an injuries feature, so Lightweight's AI injury button is probably not unique.
- **AI changes:** large unasked changes trigger 1★ reviews. "You ask, AI rewrites, you check" is less exposed. That is untested.
- **Other themes:** friends/accountability and Watch reliability recur. A mascot is not a stated user need.

## Коротко для власника

На iOS 27 (з 5.10.2026) у пошуку можна показувати замість скриншотів окрему картинку або відео. Якщо їх немає, показуються перші 3 скриншоти. Те, що Apple читає текст на скриншотах для ранжування (OCR), не підтверджено. Свап вправ і травми просять у відгуках Ladder і Fitbod. Fitbod, схоже, вже має функцію травм і обмежень. Коли AI сам різко міняє тренування, Fitbod отримує однозірочні відгуки. Маскот у 600 відгуках не згадується жодного разу.

Files are in /tmp/claude-0/-home-user-lightweight-carousels/5c010c7e-107c-5bfa-a33e-e473c9c44f36/scratchpad/aso/screens-research/best-practices/:
- data/reviews/ (raw review feeds)
- data/reviews_flat.csv
- data/theme_matches.json
- data/lookup4.json
- data/search_ladder.json
- scripts/ (fetch.sh, flatten.py, themes.py, ctx.py, show.py)
