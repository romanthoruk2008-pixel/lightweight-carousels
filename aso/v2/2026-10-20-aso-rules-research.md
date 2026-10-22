# How App Store search works, as of 2026-10-20

Web research for the Harda launch (US and UK first, twelve languages). **[A]** is Apple's own
documentation. **[I]** is an ASO-industry claim. Apple's pages carry no revision date, so "fetched
2026-10-20" is all that can be given for them.

## 1. Limits and what is searched

- **Limits [A]:** Name 2–30 characters
  ([App Information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information)),
  Subtitle 30, Promotional text 170, Description 4,000, What's New 4,000
  ([Platform version info](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information)).
- **Keywords:** the reference says "100 **bytes**"; the
  [product-page guide](https://developer.apple.com/app-store/product-page/) says "100 characters".
  Cyrillic is 2 bytes a letter in UTF-8, so uk/ru may get half. Unverified: paste a real string
  into App Store Connect to check.
- **Searched [A]** ([search guide](https://developer.apple.com/app-store/search/)): name, subtitle,
  keywords, primary category, secondary category. The company (seller) name is searchable too.
- **Not searched [A]:** promotional text. The description feeds only web search engines, not App
  Store search. No 2025–26 change found (Appfigures, Jun 2025, and SplitMetrics, Sep 2025, agree [I]).
- **Unverified:** What's New; in-app purchase display names (Apple says promoted purchases "appear
  in search results"; vendors disagree on whether their names are searched); in-app event text.

## 2. Keyword field rules

- **[A]:** commas, no spaces (spaces only inside a phrase). Don't repeat words already in the name,
  subtitle or category; a plural counts as a repeat. Skip "app", "game", filler words and special
  characters. No trademarks or competitors' app names
  ([Guideline 2.3.7](https://developer.apple.com/app-store/review/guidelines/)); Apple "may modify
  inappropriate keywords at any time".
- **How words combine** (not documented by Apple):
  - AppTweak (Aug 2024): Apple combines single words by itself, repeating adds no weight, singular is
    enough in English but "not always" in other languages [I]
    ([link](https://www.apptweak.com/en/aso-blog/how-to-optimize-your-ios-keyword-field)).
  - aso.dev (Jul 2026): phrases form from words across name, subtitle and keywords, **but only
    within one language** [I] ([link](https://aso.dev/metadata/cross-localization/)).
  - Phiture's test (2016, updated 2019): no phrases across languages [I]
    ([link](https://phiture.com/?p=83231)).

## 3. Extra languages searched in each country

Apple: "Users can search for your app using localized keywords in all countries or regions where
the App Store supports [that language]"
([Localize app information](https://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-information)).
The table is Apple's
([App Store localizations](https://developer.apple.com/help/app-store-connect/reference/app-information/app-store-localizations)).

| Country | Main language | Also supported |
|---|---|---|
| US | English (U.S.) | Arabic, Chinese (Simplified), Chinese (Traditional), French, Korean, Portuguese (Brazil), Russian, **Spanish (Mexico)**, Vietnamese |
| UK | English (U.K.) | none |
| Canada | English (Canada) | French (Canada) |
| Australia | English (Australia) | English (U.K.) |
| Germany, France, Italy, Netherlands, Brazil | de, fr, it, nl, pt-BR | English (U.K.) |
| Spain | Spanish (Spain) | Catalan, English (U.K.) |
| Poland, Czechia, Türkiye | English (U.K.) | pl, cs, tr |
| Ukraine | English (U.K.) | Russian, Ukrainian |
| Russia | Russian | English (U.K.), Ukrainian |

- **Our Spanish is Spain's**, so it does not reach the US. The US needs a Spanish (Mexico) listing.
- **English (U.K.) reaches about ten countries** besides the UK: Australia, Germany, France, Italy,
  the Netherlands, Brazil, Spain, Poland, Czechia, Türkiye, Ukraine, Russia.
- **Is every supported language searched?** Apple's wording implies yes. No controlled 2025–26 test
  found; Phiture's covered only US + es-MX and UK + en-GB [I]. MobileAction (Apr 2026) lists the
  same nine US extras and calls it "industry observation" [I]
  ([link](https://www.mobileaction.co/blog/app-store-cross-localization/)).
- App Store Connect supports 50 listing languages since 2026-03-30
  ([release notes](https://developer.apple.com/help/app-store-connect/release-notes/)).

## 4. New in 2025–2026

- **App Store tags:** Apple's models write them from the metadata and people review them
  ([WWDC25 #328](https://developer.apple.com/videos/play/wwdc2025/328/)). You can only deselect
  them (App Information → App Store Tags → Edit), not add. Built from en-US metadata, shown only in
  the US for now ([help](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags)).
  Apple does not say they affect ranking.
- **Custom product pages in search [A]:** assign keywords (from the approved keyword field, per
  language) to a custom page; it replaces the default page in results for those keywords. A
  keyword-only change needs no review. One page per keyword combination. **Up to 70 pages** (was 35,
  raised 2025-10-28) ([news](https://developer.apple.com/news/?id=gf6mgrs6)). Keywords per page:
  not documented. App Store Connect gives no keyword-level numbers; filter analytics by source "App
  Store Search" ([WWDC26 lab](https://developer.apple.com/videos/play/wwdc2026/8010/)).
- **iOS 27:** a product-page header and custom search-result visuals
  ([WWDC26 #205](https://developer.apple.com/videos/play/wwdc2026/205/)). Asset Library in App Store
  Connect since 2026-10-05.
- **Text inside screenshots (OCR):** never documented by Apple; **unproven**. For: Appfigures (Jun
  2025, no sample sizes; says caption-only keywords are weak)
  ([link](https://appfigures.com/resources/guides/app-store-algorithm-update-2025)). Against:
  ConsultMyApp's 64-phrase test (36 did not rank, 27 explained by metadata, 1 unexplained); AppDrift
  withdrew its claim on 2026-09-29 ([link](https://appdrift.co/blog/app-store-screenshot-text-indexing)).
- **More search ads:** extra ad slots in search results since 2026-03-03, UK first, everywhere by end
  of March, on iOS 26.2+
  ([Macworld](https://www.macworld.com/article/3041228/get-ready-for-more-ads-in-the-app-store.html)).

## 5. What ranks an app besides its words

- **Apple confirms only** text relevance plus user behaviour: downloads, ratings and reviews. No
  weights given.
- **[I]:** App Radar (Apr 2026) puts download speed first, then conversion, ratings, retention.
  SplitMetrics (Sep 2025) says conversion is not a direct signal. No evidence found that paid
  installs lift organic rank.
- **Apple on new apps:** "Popular, functional terms … are highly competitive – especially if you are
  a newer or smaller app." Less common terms are less contested.
- **The researcher's reading (no source):** go for 2–4 word long-tail phrases first, tie them to
  custom pages, rank first in the quieter pl, cs, tr and uk stores, ask for a rating after a finished
  workout.

## 6. Where keyword popularity comes from

- **Apple Ads Platform API** (the renamed Search Ads API):
  [Search Term Popularity](https://developer.apple.com/documentation/apple-ads-platform-api/query-app-search-term-popularity-data)
  gives the top terms per genre (Health & Fitness exists) and country, weekly or monthly, with
  `searchPopularity1to100` — but cannot look up any keyword you choose.
  [Keyword Suggestions](https://developer.apple.com/documentation/apple-ads-platform-api/query-keyword-suggestions)
  returns a relative `popularity`; needs the app's id.
- The "5–100, minimum 5" scale and "only 35+ reported since October 2025" come from Sonar's own data
  [I] ([link](https://trysonar.app/blog/apple-search-popularity.md)).

| Tool | Found |
|---|---|
| Sonar | trysonar.app — publishes popularity data built on Apple's (see above); its API was not checked |
| AppTweak | Public API, volume and difficulty at 10 credits each; packs $20–40 per 25k credits; 7-day trial ([help](https://help.apptweak.com/en/articles/6051203-app-store-api-pricing-credits-plans)) |
| Astro | Popularity from Apple plus difficulty; $9/month; Mac only; no API found ([site](https://tryastro.app)) |
| Appfigures | API only on the top tier (contact sales) ([pricing](https://appfigures.com/pricing)) |
| Sensor Tower, MobileAction, AppFollow, Asodesk | keyword API unverified |

## 7. Turning a visit into a download

- **Screenshots [A]**
  ([spec](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications)):
  1–10 per size, JPEG or PNG, no transparency. 6.9" is 1260×2736, 1290×2796 or 1320×2868. The 6.5"
  set is needed only without a 6.9" one. The page also lists the medium Dynamic Island size
  (1179×2556 or 1206×2622) as required; whether a 6.9" set covers it is unverified — check on upload.
  Text overlays are allowed (Guideline 2.3.3).
- **App previews [A]**
  ([spec](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications)):
  up to 3 per size and language, 15–30 s, 886×1920 portrait.
- **Product page tests:** up to 3 variants, 90 days at most (from search snippets, page not fetched).
- **In-app events [A]**
  ([help](https://developer.apple.com/help/app-store-connect/offer-in-app-events/offer-in-app-events/)):
  up to 10 published and 15 approved; name 30, short description 50, long description 120.
- **Promoted purchases:** show in search results; up to 20 on the product page.
- **Rating prompt [A]** ([StoreKit](https://developer.apple.com/documentation/storekit/requestreviewaction)):
  at most 3 times in 365 days for someone who hasn't rated; never from a button tap; does nothing in
  TestFlight.
- **Compliance:** since 2026-03-26, Health & Fitness apps in the US, UK and EU declare their
  regulated-medical-device status in the age-rating questionnaire.

## 8. Apple Watch

- The Watch app has **no listing or keywords of its own**: it lives on the iPhone app's page. Apple
  says to describe the Watch features in the description
  ([help](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-watchos-app-information/)).
- **Watch screenshots are required.** One size for all languages, e.g. 416×496 (Series 10–12) or
  422×514 (Ultra 3/4); they should show the real app.
- Ranking inside the Watch's own App Store: no current source found.
