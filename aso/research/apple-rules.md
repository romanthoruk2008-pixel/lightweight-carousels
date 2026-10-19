# App Store product page metadata: rules sheet for "Lightweight"

Prepared 2026-10-19 for: Lightweight, a strength-training tracker for iPhone and Apple Watch. It is freemium with an auto-renewable subscription and a 30-day free trial, and it launches first on the US storefront in English (U.S.).

**How to read this sheet**
- **[OFFICIAL]** means Apple's own documentation, fetched on 2026-10-19. Quotes are verbatim.
- **[INDUSTRY]** means widely cited ASO practice that Apple does not document. The source is cited, and it may be wrong or out of date.
- **[UNVERIFIED]** means I could not confirm the point.
- The App Review Guidelines page shows "Last Updated: October 16, 2026". That update added guideline 2.3.14 (creative assets) and 2.5.19 (hidden features).

---

## 0. Quick reference table

| Field | Limit | Indexed for App Store search? | Editable without new version? | Source |
|---|---|---|---|---|
| App Name | 2–30 characters | **Yes** [OFFICIAL] | No (only with a new version) | [App information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information); [View and edit app info FAQ](https://developer.apple.com/help/app-store-connect/create-an-app-record/view-and-edit-app-information) |
| Subtitle | 30 characters | **Yes** [OFFICIAL] | No (only with a new version) | same; [Creating your product page](https://developer.apple.com/app-store/product-page/) |
| Keywords | "100 bytes" (ASC reference) / "100 characters" (Apple marketing pages); each keyword more than 2 characters; comma-separated with no spaces | **Yes** [OFFICIAL]; not displayed publicly | No (only with a new version) | [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information); [Search](https://developer.apple.com/app-store/search/) |
| Developer (company) name | Set once at the first app record; can't be changed later | **Yes** [OFFICIAL] | Never | [Set your developer name](https://developer.apple.com/help/app-store-connect/create-an-app-record/set-your-developer-name); [View and edit FAQ](https://developer.apple.com/help/app-store-connect/create-an-app-record/view-and-edit-app-information) |
| Primary and secondary category | 2 categories (Games can add subcategories) | **Yes** [OFFICIAL]: "Your primary category and optional secondary category are indexed by our search algorithm." | Changed with a version submission | [Search](https://developer.apple.com/app-store/search/) |
| Promotional Text | 170 characters | **No** [OFFICIAL]: "doesn't affect your app's search ranking" | **Yes, any time** | [Product page](https://developer.apple.com/app-store/product-page/) |
| Description | 4000 characters, plain text, no HTML | **Not for App Store search** (Apple doesn't list it; [INDUSTRY] consensus is "not indexed"). Apple says it is used for **web search engine** results. It is also an input to LLM-generated **App Tags** (US) | No (only with a new version) | [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information); [Manage app tags](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags) |
| What's New | 4000 characters; not available on the first version | No ([INDUSTRY]) | Only with a version | [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information) |
| IAP / subscription Display Name | **2–30 characters** (ASC Help); the product page doc says 35 | Promoted IAPs appear in search results [OFFICIAL]. That their names are indexed is [INDUSTRY] | Each change needs review, but not a new app version | [In-App Purchase information](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-information) vs [Product page](https://developer.apple.com/app-store/product-page/) |
| IAP / subscription Description | **max 45 characters** (ASC Help); the product page doc says 55 | Same as above | Needs review | same |
| IAP promotional image | 1024×1024 px, JPG/PNG, 72 dpi, RGB, flattened, no rounded corners | n/a | needs review | [In-App Purchase information](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-information) |
| In-App Event name | 30 characters, title case | Events "appear in search results"; "Users can also search for In-App Events directly" [OFFICIAL] | Event submitted independently | [In-App Events](https://developer.apple.com/app-store/in-app-events/); [Offer In-App Events](https://developer.apple.com/help/app-store-connect/offer-in-app-events/offer-in-app-events) |
| In-App Event short description | 50 characters, sentence case | as above | as above | same |
| In-App Event long description | 120 characters, sentence case | as above | as above | same |
| Custom Product Page promotional text | Not stated on the CPP pages. It is presumably the same 170-character field [UNVERIFIED] | No (promo text isn't ranked) | CPP is submitted independently of a version | [CPP](https://developer.apple.com/app-store/custom-product-pages/) |
| Custom Product Page keywords | Chosen **from the keywords of the latest approved version**; each keyword combination should be unique to one page | The CPP replaces the default page in results for those keywords | Assignable any time; searchable after approval and visibility | [Configure multiple product page versions](https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions) |
| Screenshots | 1–10 per device size and localization; JPG/PNG; no alpha | Not officially indexed. Text-in-screenshot indexing is **unconfirmed** (see section 2.3) | Only with a version, CPP, or PPO | [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications) |
| App previews | Up to 3 per device size and language; 15–30 s; ≤500 MB; ≤30 fps | Not indexed | Only with a version, CPP, or PPO | [App preview specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications) |
| Creative assets (new in iOS 27): product page header and search-results asset | Header 21:9 (3840×1646) or 16:9 (5244×2950 PNG); search result 3:2 (1920×1280 to 3840×2560); video 5–30 s | Not indexed | Asset Library, submitted independently | [Creative assets specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications) |
| Support URL | Required; must lead to real contact information | n/a | — | [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information) |
| Privacy Policy URL | Required for iOS | n/a | Editable | [App information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information) |
| Review Notes | 4000 bytes | n/a | — | [Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information) |
| Reference names (IAP, CPP, PPO, IAE) | 64 characters, internal only | No | — | various |

**Official list of searchable fields.** The ASC Help FAQ says: "Your app is searchable on the App Store by app name, app subtitle, keywords, and your company name." The Search page adds: "Search results are based on a number of factors, including text relevance (matches for your app's title, subtitle, keywords, and primary category), as well as user behavior (downloads, ratings and reviews, and more)." ([FAQ](https://developer.apple.com/help/app-store-connect/create-an-app-record/view-and-edit-app-information), [Search](https://developer.apple.com/app-store/search/))

---

## 1. Field-by-field limits and rules

### 1.1 App Name: 30 characters [OFFICIAL]
- "The name must be at least two characters and no more than 30 characters. You can edit it until you submit the app to App Review. Later, you can change the name when you create a new version…" ([App information](https://developer.apple.com/help/app-store-connect/reference/app-information/app-information))
- Guideline 2.3.7: "Choose a unique app name … App names must be limited to 30 characters. Metadata such as app names, subtitles, screenshots, and previews should not include prices, terms, or descriptions that are not specific to the metadata type."
- Product page guidance: "Be distinctive. Avoid names that use generic terms or are too similar to existing app names." ([Product page](https://developer.apple.com/app-store/product-page/)) Note that "Lightweight" is a generic English word (see section 9).
- Guideline 2.3.8: "ensure your metadata, including app name and icons (small, large, Apple Watch app, alternate icons, etc.), are similar to avoid creating confusion." This means the Watch app's icon and name should match the iPhone app.

### 1.2 Subtitle: 30 characters [OFFICIAL]
- "A summary of your app that appears under your app's name … This can't be longer than 30 characters."
- 2.3.7: subtitles "must follow our standard metadata rules and should not include inappropriate content, reference other apps, or make unverifiable product claims."
- Product page guidance: "Avoid generic descriptions such as 'world's best app.' … You can update your subtitle when submitting a new version."

### 1.3 Keywords: 100 (bytes or characters) [OFFICIAL, with a conflict]
- ASC reference: "One or more keywords (each greater than two characters) describing your app. You can provide up to 100 bytes of content. Your app is searchable by app name and company name, so you shouldn't duplicate these values in the keyword list. Names of other apps or companies aren't allowed." ([Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information))
- Search and Product page guidance: "Keywords are limited to 100 characters total, with terms separated by commas and no spaces. You can use spaces to separate words within keyword phrases. For example: Property,House,Real Estate." ([Search](https://developer.apple.com/app-store/search/))
- **Bytes vs characters.** For English (U.S.) ASCII it makes no difference, because 1 character equals 1 byte and commas count. For non-ASCII scripts, Apple's two pages conflict. [INDUSTRY] AppDrift scanned 5,304 live keyword fields (published 2026-10-07): 1,339 were longer than 100 bytes and none was longer than 100 characters. Its conclusion is that the enforced limit is 100 characters per localization. ([AppDrift](https://appdrift.co/blog/aso-localization)) UTF-8 sizes for reference: Cyrillic, Arabic, Hebrew and Greek take 2 bytes per character; CJK, Thai and Hindi take 3.
- Keywords must be "greater than two characters", so a 2-character token such as "AI" is not allowed as a standalone keyword. [OFFICIAL, per ASC wording]
- The keyword field is not shown publicly.

### 1.4 Promotional Text: 170 characters, editable any time [OFFICIAL]
- "Promotional text lets you inform your App Store visitors of any current app features without requiring an updated submission. This text will appear above your description … can't be longer than 170 characters." ([Platform version information](https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information))
- "You can update promotional text at any time without having to submit a new version of your app." "promotional text doesn't affect your app's search ranking so it should not be used to display keywords." ([Product page](https://developer.apple.com/app-store/product-page/))

### 1.5 Description: 4000 characters [OFFICIAL]
- "Limited to 4000 characters. The description should be in plain text, with line breaks as needed. HTML format isn't supported." It "will be used for web engine search results once you release your app."
- Product page guidance: "The first sentence of your description is the most important — this is what users can read without having to tap to read more." "Don't add unnecessary keywords to your description in an attempt to improve search results. Also avoid including specific prices in your app description."
- Watch companion: "Ensure your description includes the app's functionality on Apple Watch." ([Add watchOS app information](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-watchos-app-information))
- Subscription apps: this is where the Terms of Use (EULA) link goes (see section 6).

### 1.6 What's New: 4000 characters [OFFICIAL]
- "Limited to 4000 characters … This property isn't available for the first version of the app but required for all subsequent versions."
- Guideline 2.3.12: "Apps must clearly describe new features and product changes in their 'What's New' text. Simple bug fixes, security updates, and performance improvements may rely on a generic description, but more significant changes must be listed in the notes."

### 1.7 In-App Purchase and subscription display metadata [OFFICIAL, with a conflict]
- ASC Help: "The display name must be at least two characters and no more than 30 characters." "The description must be no more than 45 characters." "Changes to the localized information require review." ([IAP information](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/in-app-purchase-information))
- The marketing page says something different: "In-app purchase names are limited to 35 characters and descriptions are limited to 55 characters." ([Product page](https://developer.apple.com/app-store/product-page/)) **Use the stricter 30/45**, which is what App Store Connect enforces according to its own Help.
- Subscription and group display names "must not contain control characters … or markup language (for example, HTML tags, or Unicode characters, such as emoticons, diacritics, or special characters)." This means no emoji. ([Auto-renewable subscription information](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/auto-renewable-subscription-information))
- Subscriptions page: "Use distinct names for the app, the subscription group, and each subscription to avoid confusion." ([Subscriptions](https://developer.apple.com/app-store/subscriptions/))
- Promotion: up to 20 promoted IAPs. Promotion requires the 1024×1024 image and PurchaseIntent API support. "Promoted In-App Purchases appear on your product page, can display in search results, and may be featured on the Today, Games, and Apps tabs." ([Promote In-App Purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases))
- Guideline 2.3.2: if you promote IAPs, "ensure that the in-app purchase Display Name, Screenshot and Description are appropriate for a public audience…"

### 1.8 In-App Events [OFFICIAL]
- Name up to 30 characters, short description up to 50, long description up to 120. ([Offer In-App Events](https://developer.apple.com/help/app-store-connect/offer-in-app-events/offer-in-app-events))
- Style ([In-App Events](https://developer.apple.com/app-store/in-app-events/)):
  - Name: "distinctive, unique name … written in title case … the actual name of the event … rather than a call to action."
  - Short and long descriptions: sentence case.
  - "Don't include specific prices in your metadata … Including specific pricing will lead to rejection by App Review."
- Limits: 10 published at a time, 15 approved in ASC, up to 10 with overlapping dates. Each event lasts at least 15 minutes and at most 31 days. It can be published up to 14 days before it starts.
- Media: event card 16:9 (1920×1080 to 3840×2160); details page 9:16 (1080×1920 to 2160×3840); video 15–30 s; up to 500 MB. ([IAE media specs](https://developer.apple.com/help/app-store-connect/reference/in-app-events/in-app-event-media-and-audio-specifications))
- Guideline 2.3.13: "All event metadata must be accurate and pertain to the event itself, rather than the app more generally."
- Search: "When users search for an app, the event card appears along with your app for users who have downloaded your app, while screenshots show for those who haven't … Users can also search for In-App Events directly." ([In-App Events](https://developer.apple.com/app-store/in-app-events/)) Whether event names act as ranking keywords for the *app* is [INDUSTRY]. Apple does not say.

### 1.9 Custom Product Pages: promotional text
- CPP pages can vary "screenshots, previews, promotional text, and keywords". I found no separate character limit for CPP promotional text, so it is presumably the standard 170 characters. [UNVERIFIED]

### 1.10 Other required fields [OFFICIAL]
- **Support URL**: "must lead to actual contact information."
- **Privacy Policy URL**: "Required for iOS and macOS apps."
- **Copyright**: "2026 Example, Inc." format; the © symbol is added automatically.
- **License Agreement (EULA)**: "If you don't provide a custom EULA, the standard EULA is applied to your app and the license agreement link isn't shown on your App Store product page." ([Custom license agreement](https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement)) This matters for subscriptions; see section 6.
- **Propagation**: "it may take up to 24 hours for the changes to appear on the App Store."

---

## 2. What is indexed and what isn't

### 2.1 Indexed [OFFICIAL]
| Element | Evidence |
|---|---|
| App name | ASC FAQ; Search page ("title") |
| Subtitle | ASC FAQ; Search page |
| Keyword field | ASC FAQ; Search page |
| Company/developer name | ASC FAQ ("and your company name"); ASC keyword note ("searchable by app name and company name") |
| Primary category (and secondary) | Search page ("primary category" in text relevance; "Your primary category and optional secondary category are indexed") |
| Promoted IAPs | They "appear in App Store search results" (Search page). Treating the IAP *name* as a ranking keyword is [INDUSTRY] ([AppFollow](https://appfollow.io/blog/advanced-app-store-optimization-how-to-use-in-app-purchases-to-gain-more-app-visibility), [Adapty](https://adapty.io/blog/improve-app-visibility-in-app-store)). AppFollow and Adapty say only *promoted* IAPs count. |
| In-App Events | "Users can also search for In-App Events directly" |
| Custom product pages with assigned keywords | They "can appear in search results for those selected keywords instead of your default product page" |

### 2.2 Not indexed
| Element | Status |
|---|---|
| Promotional text | [OFFICIAL] does not affect ranking |
| Description | Not listed by Apple as searchable, and Apple says "Don't add unnecessary keywords to your description". [INDUSTRY] consensus is that it isn't indexed for App Store search. [OFFICIAL] It is used for *web* search engines and is an input to App Tags. |
| What's New | [INDUSTRY] not indexed |
| Screenshot or preview text | See section 2.3. Unconfirmed |

### 2.3 Screenshot caption "OCR indexing" (claimed in 2025): **unconfirmed**
- Apple documentation (Search page, ASC FAQ) lists no screenshot indexing. Screenshots are described only as *displayed* in search results.
- **For indexing**:
  - Around 5–9 June 2025, Appfigures reported ranking anomalies and concluded that caption text had become a ranking signal ("Screenshots are no longer just for conversion. They now influence discovery."). I could not retrieve Appfigures' original report (HTTP 403); this is as summarized by [Lomio, 2026-04-06](https://lomio.io/blog/do-app-stores-read-screenshot-text).
  - SplitMetrics called captions "active ranking factors" (also via Lomio).
- **Against**:
  - ConsultMyApp tested 64 caption phrases across 8 apps. 36 didn't rank, 27 were fully explained by name, subtitle or keywords, and 1 (Audible) was anomalous. Their verdict: "not consistent, it's not confirmed" (via Lomio).
  - Phiture reportedly said Apple denied using OCR. **I could not verify this.**
- **Related, confirmed:** App Review appears to read screenshot text when it checks for prices. See section 5.6.
- **Decision:** write captions for conversion. Don't rely on them for ranking, and keep every target keyword in name, subtitle or keywords.

### 2.4 App Tags (2025–2026, US only) [OFFICIAL]
- "Search results may also include app tags … These are generated using large language models (LLMs) based on the metadata you've provided in App Store Connect." ([Search](https://developer.apple.com/app-store/search/))
- "Tags are based on the App Store metadata you provide in App Store Connect, artificial intelligence, and human curation … Currently, tags are only supported and displayed to users across the App Store in the United States." "Tags are applied to your app by default, based on the metadata you provide in App Store Connect (en_US only). You can deselect the tags you don't want … Deselecting all tags may affect your discoverability." ([Manage app tags](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags))
- **Implication:** the en-US description and other metadata now feed a US discovery surface. Write the description so the right concepts appear clearly, for example strength training, workout log, Apple Watch, progressive overload and rest timer, but only if those features are real. Then review the tags in ASC after the first approval.

---

## 3. Keyword best practices

| Rule | Status | Source / quote |
|---|---|---|
| Separate with commas, no spaces after commas; spaces are allowed *within* a phrase | OFFICIAL | Search: "terms separated by commas and no spaces. You can use spaces to separate words within keyword phrases." |
| Don't repeat words already in name, subtitle or category | OFFICIAL | Search: "Don't repeat any words … included in your app name, subtitle, or category." ASC: don't duplicate app name or company name. |
| Don't add plurals of words you already have | OFFICIAL | Search: "Plurals of words you've already included, such as 'climbs' and 'climb,' as these are considered duplicates." [INDUSTRY nuance] AppTweak found singular and plural can rank differently and advises researching both ([AppTweak](https://www.apptweak.com/en/aso-blog/do-singular-or-plural-keywords-rank-differently-in-aso)). Follow Apple for English. |
| Avoid "app", "game", category names | OFFICIAL | Product page: avoid "Names of categories or the word 'app'". Search: "Generic terms that are too broad … such as 'app' or 'game.'" |
| Avoid filler words ("the", "to") | OFFICIAL | Search page |
| Avoid special characters (#, @) | OFFICIAL | "Special characters don't carry extra weight" |
| Don't use "free" | OFFICIAL (indirect) + INDUSTRY | 2.3.7 bans "pricing information" in metadata. App Review has stated that "references to free or discounted services are considered a price reference and are not appropriate for app metadata" (App Review message quoted in [forum thread 765443](https://developer.apple.com/forums/thread/765443), Oct 2024, about screenshots). AppTweak says "free" and "app" are matched automatically anyway ([AppTweak](https://www.apptweak.com/en/aso-blog/how-to-optimize-your-ios-keyword-field)). |
| No competitor or other app names, trademarks or celebrity names | OFFICIAL | Search: "Don't include: Unauthorized use of trademarked terms, celebrity names, or other protected words and phrases. Terms that are not relevant to the app. Competing app names. Inappropriate, offensive, or objectionable terms." ASC: "Names of other apps or companies aren't allowed." |
| Each keyword must be longer than 2 characters | OFFICIAL | ASC reference |
| Words combine across name, subtitle and keyword field (single words are recombined into phrases) | INDUSTRY | AppTweak: "The Apple algorithm will automatically make combinations with the different keywords in your keyword field" ([AppTweak](https://www.apptweak.com/en/aso-blog/how-to-optimize-your-ios-keyword-field)). Prefer single words over long phrases. |
| Keywords do NOT combine across *different localizations* | INDUSTRY | AppTweak: "Keywords are not combined across localizations" ([AppTweak cross-localization](https://www.apptweak.com/en/aso-blog/how-to-benefit-from-cross-localization-on-the-app-store)) |
| Repetition gives no extra weight | INDUSTRY | AppTweak: Apple "does not take into account keyword density" |
| Apple may edit keywords | OFFICIAL | 2.3.7: "Apple may modify inappropriate keywords at any time or take other appropriate steps to prevent abuse." |

**Guideline 2.3.7, verbatim** ([App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/#accurate-metadata)):
> Choose a unique app name, assign keywords that accurately describe your app, and don't try to pack any of your metadata with trademarked terms, popular app names, pricing information, or other irrelevant phrases just to game the system. App names must be limited to 30 characters. Metadata such as app names, subtitles, screenshots, and previews should not include prices, terms, or descriptions that are not specific to the metadata type. App subtitles are a great way to provide additional context for your app; they must follow our standard metadata rules and should not include inappropriate content, reference other apps, or make unverifiable product claims. Apple may modify inappropriate keywords at any time or take other appropriate steps to prevent abuse.

**Specific to Lightweight**
- Don't put competitor names in the keyword field, for example "strava", "hevy", "strong", "fitbod" or "jefit". Generic dictionary words that happen to be app names are a grey area; AppTweak notes that generic words like "dragon" or "city" aren't trademarked on their own. Use generic words only for their generic meaning and be conservative. "Strong" is a competitor brand.
- Don't put "Apple Watch", "Apple Health" or "HealthKit" in the keyword field. They are Apple trademarks; see section 5.7. "watch" alone is a generic word. [Judgment, not an official rule]
- **Search popularity data.** The official Apple Ads UI shows "Search popularity is displayed as numbers from 1 to 5, with 5 being the most popular." ([Apple Ads glossary](https://ads.apple.com/app-store/help-glossary), [Review recommendations](https://ads.apple.com/app-store/help/recommendations/0055-review-recommendations)). [INDUSTRY] Third-party tools show a 5–100 popularity score derived from Apple Ads data; MobileAction estimates about 90% of keywords sit at the floor of 5 ([MobileAction](https://www.mobileaction.co/blog/apple-search-popularity-decoded/)).

---

## 4. Localizations and extra keyword space

### 4.1 Apple's official table [OFFICIAL]
Source: [App Store localizations](https://developer.apple.com/help/app-store-connect/reference/app-store-localizations)

There are now **50 metadata languages**. Eleven were added on 2026-03-31: Bangla, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Slovenian, Tamil, Telugu and Urdu. ([News](https://developer.apple.com/news/))

Apple publishes "Default language" and "Additional supported language(s)" per storefront. **Apple describes these as display languages, not as search indexing.** ASC Help says: "Users can search for your app using localized keywords in all countries or regions where the App Store supports French." ([Localize app information](https://developer.apple.com/help/app-store-connect/manage-app-information/localize-app-information)) That is the closest official statement that a storefront's supported languages are searchable there.

| Storefront | Default language (Apple) | Additional supported (Apple) |
|---|---|---|
| **United States** | English (US) | **Arabic, Chinese (Simplified), Chinese (Traditional), French, Korean, Portuguese (Brazil), Russian, Spanish (Mexico), Vietnamese** |
| United Kingdom | English (U.K.) | none |
| Canada | English (Canada) | French (Canada) |
| Australia | English (Australia) | English (U.K.) |
| Germany | German | English (U.K.) |
| France | French | English (U.K.) |
| Spain | Spanish (Spain) | Catalan, English (U.K.) |
| Italy | Italian | English (U.K.) |
| Poland | English (U.K.) | Polish |
| Brazil | Portuguese (Brazil) | English (U.K.) |
| Mexico | Spanish (Mexico) | English (U.K.) |
| Ukraine | English (U.K.) | Russian, Ukrainian |
| Türkiye | English (U.K.) | Turkish |
| Japan (for reference) | Japanese | English (US) |

### 4.2 Industry observation of search indexing [INDUSTRY]
- **US storefront: 10 indexed localizations.** English (U.S.) plus Spanish (Mexico), Russian, Chinese (Simplified), Arabic, French, Portuguese (Brazil), Chinese (Traditional), Vietnamese and Korean. This matches Apple's table. Sources: [AppTweak](https://www.apptweak.com/en/aso-blog/how-to-benefit-from-cross-localization-on-the-app-store) (updated 2025-11-21; data from 2022 fake-keyword tests) and [ASO Agency](https://asoagency.io/blogs/which-languages-to-localize-app-first) (2026-09-24). ASO Agency adds: "Apple doesn't document which ones are search-indexed; that part is industry observation."
- That gives about 10 × 100 = **roughly 1,000 characters of keyword field** for US search. Each extra localization also has its own name (30) and subtitle (30), which are likely indexed as well ([AppTweak](https://www.apptweak.com/en/aso-blog/how-to-benefit-from-cross-localization-on-the-app-store)).
- **AppTweak's table differs from Apple's** for some markets:
  - UK: AppTweak shows English (Australia) as indexed; Apple lists nothing.
  - Ukraine: AppTweak gives Ukrainian as primary with Russian and English (UK).
  - Türkiye: AppTweak gives Turkish as primary with English (UK) and French.

  These may reflect older (2022) tests. Treat Apple's 2026 table as the more current baseline and verify with a rank tracker.
- **Risks** [INDUSTRY]:
  - Each "extra" localization is still the *visible* listing for users whose device language matches. A US user with Spanish, Russian, Vietnamese or another matching device language, or a user in a storefront where that language is the default (Mexico uses Spanish (Mexico)), sees that localization's name, subtitle and screenshots.
  - AppTweak: "this practice is frowned upon by Apple, so far, no rejections from Apple have been publicized." It advises localizing name and subtitle properly and using the keyword field for the extra English terms.
  - Words don't combine across localizations, so a two-word phrase must live in one locale.
  - App Review reviews all localizations. Irrelevant or keyword-stuffed text is a 2.3.7 risk.
- **ASC behavior** [OFFICIAL]: "When you add a language … screenshots and the properties for the new language default to those of the primary language, except for the description and keywords."

---

## 5. Screenshots, previews and visual metadata

### 5.1 iPhone screenshot sizes [OFFICIAL] (changed in 2026)
Source: [Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications)
- "You must include at least one screenshot and can upload up to 10 screenshots per device size in .jpeg, .jpg, or .png formats … Images can't include alpha channels or transparencies."
- **Required**: "iPhone: At least one screenshot for iPhone with Dynamic Island (medium display)." That category is iPhone 14 Pro through 18 Pro and 15/16/17. Accepted sizes: **1206×2622** or 1179×2556 (portrait).
- Dynamic Island (large display) covers iPhone Air, the Pro Max models and the Plus models. Accepted sizes: **1320×2868**, 1290×2796 or 1260×2736. The page's own fallback notes say:
  - Face ID (large): 1284×2778 / 1242×2688, "Required if app runs on iPhone and screenshots for iPhone with Dynamic Island (large display) aren't provided".
  - Medium falls back to Face ID (large) scaled.

  The page is internally inconsistent here. **Safest: upload a 1320×2868 set and a 1206×2622 set.**
- "If your app's user interface is consistent across multiple device sizes and localizations, you only need to provide screenshots for the highest required resolution."
- **iPhone Duo** (foldable, on sale 2026-10-23): 1398×2034 outer and 2007×2853 inner. "Starting in April 2027, screenshots will be required for any app using the iOS 27.1 SDK or later." Supplying them adds an "optimized for iPhone Duo" badge.
- Screenshots per product page: up to 10. "Depending on the orientation of your screenshots, the first one to three images will appear in search results when no app preview is available." ([Product page](https://developer.apple.com/app-store/product-page/)) With portrait screenshots, the first 3 show.
- **New in iOS 27:** a "search results" creative asset, if provided, takes that slot. "If you choose to not use a search result creative asset, your In-App Events, app previews, and screenshots will appear." ([Asset best practices](https://developer.apple.com/app-store/asset-best-practices/))

### 5.2 Apple Watch screenshots [OFFICIAL]
- "Required for Apple Watch apps." Provide one of these sizes:
  - 422×514 (Ultra 4, Ultra 3)
  - 410×502 (Ultra 2, Ultra)
  - 416×496 (Series 12/11/10)
  - 396×484 (Series 9/8/7)
  - 368×448 (Series 6/5/4, SE)
  - 312×390 (Series 3/2/1)

  "You must use the same screenshot size for Apple Watch consistently across all localizations for the app." ([Screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications))
- "Ensure your description includes the app's functionality on Apple Watch. Provide screenshots of Apple Watch and an app icon … iOS screenshots are also required for apps with an iOS component." ([Add watchOS app information](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-watchos-app-information))
- **Device frame:** Apple's spec says nothing about frames. [INDUSTRY] consensus is to submit the raw watch UI without a bezel, because the canvas is tiny ([Gummicube](https://blog.gummicube.com/blog/apple-watch-launch): "do not frame the screenshot in an Apple Watch"). There is also an anecdotal rejection for framed watch mockups.
- App previews: the preview spec lists only iOS, macOS, tvOS and visionOS. **There are no Watch app previews.**
- Product page optimization is "not available for … product pages on the App Store for Apple Watch".

### 5.3 App previews [OFFICIAL]
- Up to 3 per device size and language, 15–30 s, ≤500 MB, ≤30 fps, H.264 or ProRes 422 HQ. The iPhone 6.9"/6.7"/6.5"/6.1" classes all accept **886×1920** (portrait) / 1920×886. ([App preview specifications](https://developer.apple.com/help/app-store-connect/reference/app-information/app-preview-specifications))
- "App previews autoplay with muted audio when users view your product page … App preview poster frames appear whenever videos do not autoplay." ([Product page](https://developer.apple.com/app-store/product-page/))
- "App previews always appear before screenshots."
- The default poster frame is at 5 s, and poster frames "can't be edited after assets have been approved."
- Guideline 2.3.4: "previews may only use video screen captures of the app itself … You can add narration and video or textual overlays."

### 5.4 Guideline 2.3.3, verbatim, plus how App Review applies it [OFFICIAL]
> 2.3.3 Screenshots should show the app in use, and not merely the title art, login page, or splash screen. They may also include text and image overlays (for example, to demonstrate input mechanisms, such as an animated touch point or Apple Pencil) and show extended functionality on device, such as Touch Bar.

App Review's reference page adds ([2.3.3 guideline reference](https://developer.apple.com/help/app-review/guideline-reference/2-3-3-screenshots)):
- "App Review … will approve only those submissions where more than half of screenshots show the app in use … if an app has four screenshots for each device, three must show the app in use."
- Do: "Include splash screens or marketing text, as long as the majority of screenshots still show the app in use."
- Do: "Show your app running on another Apple platform when that's part of the experience." For Lightweight, an iPhone screenshot that also shows the Watch is acceptable.
- Don't: "Don't let overlays or marketing visuals crowd out your app." "Don't show only the hardware or an overlay with no app interface behind it."

### 5.5 Guideline 2.3.8, verbatim [OFFICIAL]
> 2.3.8 Metadata should be appropriate for all audiences, so make sure your app and in-app purchase icons, screenshots, and previews adhere to a 4+ age rating even if your app is rated higher. For example, if your app is a game that includes violence, select images that don't depict a gruesome death or a gun pointed at a specific character. Use of terms like "For Kids" and "For Children" in app metadata is reserved in the App Store for the Kids Category. Remember to ensure your metadata, including app name and icons (small, large, Apple Watch app, alternate icons, etc.), are similar to avoid creating confusion.

Asset best practices: "Assets displayed on the App Store must meet a 4+ age rating … Refrain from showing objectionable content, including … profanity…" ([Asset best practices](https://developer.apple.com/app-store/asset-best-practices/)) **This means no profane mascot "roasts" in screenshots, previews, icons or creative assets, even if the app is rated 13+.** Masked profanity such as "f***" is also risky. [Judgment]

### 5.6 Prices, "free", people, real data, other platforms [OFFICIAL]
- 2.3.7: no prices or "terms" in name, subtitle, screenshots or previews.
- An App Review message quoted on a forum (Oct 2024): "references to free or discounted services are considered a price reference and are not appropriate for app metadata." ([thread 765443](https://developer.apple.com/forums/thread/765443)) **So "30-day free trial" must not appear in screenshots, subtitle or name.**
- Asset best practices: "Don't include specific pricing, discounts, website URLs, copyright symbols." "Avoid claims that can't be verified, such as awards or recognition." "Don't include … Apple-designated recognitions — such as Editor's Choice, App of the Day…"
- 2.3.14 (new, 2026-10-16): creative assets "should not include inappropriate content, references to other apps with an intent to mislead, unverifiable product claims, or specific or discounted pricing information."
- 2.3.9: "You are responsible for securing the rights to use all materials in your app icons, screenshots, and previews, and you should display fictional account information instead of data from a real person." Photos of people need model releases, and workout data shown should be demo data.
- 2.3.10: "don't include names, icons, or imagery of other mobile platforms or alternative app marketplaces." That rules out Android and Wear OS.
- 2.3.2: "make sure your app description, screenshots, and previews clearly indicate whether any featured items, levels, subscriptions, etc. require additional purchases." **This applies directly to Lightweight:** if a screenshot shows a Pro-only feature, indicate that somewhere (description at minimum).
- Device frames, from the marketing guidelines ([Marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/)):
  - "Use Apple-provided product bezels in all your marketing materials … Always use the latest-generation devices."
  - "Always display the product 'as is' — don't add cases or covers. Don't show an Apple product along with a competing product from another manufacturer."
  - Status bar: "full network icon …, a full Wi-Fi icon, and a full battery icon."
  - "If your marketing contains illustrations of generic devices, ensure that these devices do not include details that are unique to Apple products."

  These are written for marketing materials. For App Store screenshots, frames are optional [INDUSTRY].

### 5.7 Apple Health, Apple Watch and Strava naming and logos
**Apple Health / HealthKit** [OFFICIAL] ([HIG: HealthKit](https://developer.apple.com/design/human-interface-guidelines/healthkit); [Works with Apple Health](https://developer.apple.com/health-fitness/works-with-apple-health/))
- "Refer to the Health app as Apple Health or the Apple Health app." "**Don't use the term HealthKit.** HealthKit is a developer-facing term … you might say that your app 'works with the Apple Health app'."
- App Store: "**App Store Preview**: Refer to Apple Health app compatibility in text or use the Works with Apple Health badge." The badge is white with an outline, min 30 px on screen, with clear space equal to ¼ of its height. Use one per promotion, unaltered, and add no ™ to the badge.
- Apple Health *icon*: "Use only the Apple-provided icon … Display the name Apple Health close to the Apple Health icon … Don't use the Apple Health icon within text or as a replacement for the terms Health, Apple Health, or HealthKit." "**Don't display Health app images or screenshots.**"
- "Do not refer to Apple Health data. Health data belongs to the user, not Apple."
- Social media: "Do not use the Works with Apple Health badge or Apple product images in social media promotions … Do not create a hashtag that includes the name Apple, Apple Health, or any Apple trademark." **This is relevant to the carousels project.**
- **Activity rings**: "Never use Activity rings in your app's icon or marketing materials." See also 5.2.5.

**Apple Watch naming** [OFFICIAL] ([Marketing guidelines](https://developer.apple.com/app-store/marketing/guidelines/))
- "Always typeset Apple Watch as two words … Don't use the article the before Apple Watch … It is acceptable to say Name of app for Apple Watch."
- "Don't use the word watch or time as a pun or verb in your marketing materials."
- "Use Apple product names … in a referential phrase … say app name for iPhone … or use a phrase such as works with or compatible with. Don't say iPhone app name."
- Apple's trademark guidelines: you may not use an Apple trademark "in whole or in part" as part of your product name. Referential use is allowed only if "The Apple word mark is not part of the product name" and it "is less prominent than the product name." ([Apple trademark guidelines](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)) **Don't put "Apple Watch" in the App Name.** "Workout log for Apple Watch" in the description is fine. In the subtitle it is a grey area [judgment].

**Strava** (third-party; [Strava API Brand Guidelines](https://developers.strava.com/guidelines/), last revised 2025-09-29)
- "If you choose to refer to interoperability with Strava you must use one of the following: 'Powered by Strava' or 'Compatible with Strava'." Use the official logos.
- "You must not use the Strava name in your application name." "Never use any part of a Strava logo as the icon for your application." "Never use Strava logos in any manner that implies your application was developed or sponsored by Strava." The Strava name "should not appear more prominently than the name of your application."
- Apple 4.1(c): "You cannot use another developer's icon, brand, or product name in your app's icon or name, without approval from the developer."
- Apple 5.2.2: you must be "specifically permitted" under the third-party service's terms.
- **Only claim Strava compatibility if it actually ships.** Never put "strava" in the keyword field ("Competing app names" / "Names of other apps or companies aren't allowed").

---

## 6. Subscription metadata (auto-renewable, 30-day free trial)

**Guideline 3.1.2, verbatim** (excerpts relevant here) ([Guidelines](https://developer.apple.com/app-store/review/guidelines/#subscriptions)):
> 3.1.2(a) … If you offer an auto-renewable subscription, you must provide ongoing value to the customer, and the subscription period must last at least seven days and be available across all of the user's devices. … Auto-renewable subscription apps may offer a free trial period to customers by providing the relevant information set forth in App Store Connect. … Apps that attempt to scam users will be removed from the App Store. This includes apps that attempt to trick users into purchasing a subscription under false pretenses or engage in bait-and-switch and scam practices…
>
> 3.1.2(c) Subscription Information: Before asking a customer to subscribe, you should clearly describe what the user will get for the price. … Ensure you clearly communicate the requirements described in Schedule 2 of the Apple Developer Program License Agreement.

**Metadata requirements**
- [OFFICIAL] "Please note that your app and App Store metadata must include links to your Terms of Use and Privacy Policy." ([Subscriptions](https://developer.apple.com/app-store/subscriptions/))
- [OFFICIAL] Privacy Policy URL field: required for iOS apps.
- [OFFICIAL, via App Review messages] Standard 3.1.2 rejection text (June 2025): "The app's metadata is missing the following required information: A functional link to the Terms of Use (EULA). If you are using the standard Apple Terms of Use (EULA), include a link to the Terms of Use in the App Description." ([forum 786790](https://developer.apple.com/forums/thread/786790)) The alternative is a custom EULA in the ASC License Agreement field. Note that with the standard EULA, ASC shows no license link on the product page ([EULA help](https://developer.apple.com/help/app-store-connect/manage-app-information/provide-a-custom-license-agreement)), which is why the link must be in the description.
- **Action:** put a "Terms of Use (EULA): https://www.apple.com/legal/internet-services/itunes/dev/stdeula/" line (or your own ToS URL) and a "Privacy Policy:" link at the end of the **description in every localization**. A developer was rejected because the link was in the French description but missing from the English one ([forum 786790](https://developer.apple.com/forums/thread/786790)).
- In-app requirements (not metadata, but they get checked in review) [OFFICIAL, Subscriptions page]:
  - The sign-up screen must show the "Subscription name and duration, and the content or services provided"; the "Full renewal price, shown clearly and prominently"; and "A way for current subscribers to sign in or restore purchases."
  - "In the purchase flow for a free trial, clearly indicate how long the free trial lasts and the price billed once the free trial is over."
  - "the amount that will be billed must be the most prominent pricing element in the layout."
  - Functional Terms and Privacy links on the paywall [INDUSTRY consensus from rejections].

**How to mention the 30-day free trial**
- Configure it as an **introductory offer** in ASC ("providing the relevant information set forth in App Store Connect"). The App Store then shows it in the purchase sheet. [OFFICIAL]
- **Name, subtitle, screenshots, previews, creative assets, IAE metadata: no "free" and no prices** (2.3.7, 2.3.14, the App Review "free = price reference" message, IAE pricing rule).
- **Description:** Apple says to "avoid including specific prices" because they may be inaccurate across regions. Mentioning that a trial exists, with accurate terms, is common practice [INDUSTRY]. A conservative wording: "Lightweight Pro is an auto-renewable subscription. New subscribers may be eligible for a free trial; terms are shown before purchase. Payment is charged to your Apple Account at confirmation…" with no currency amounts.
- **Promotional text:** editable any time, so it's a lower-risk place to announce a trial offer. It is still metadata and still reviewed when versions are reviewed. Avoid currency amounts. [Judgment]
- Subscription display names: use distinct names (for example "Lightweight Pro Monthly" / "Annual"), 2–30 characters, no emoji, description ≤45 characters.

---

## 7. Product Page Optimization, Custom Product Pages, In-App Events

### 7.1 Product Page Optimization (A/B tests) [OFFICIAL]
Sources: [PPO](https://developer.apple.com/app-store/product-page-optimization/), [Create a test](https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/create-a-test), [Configure treatments](https://developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/configure-test-treatments)
- **Up to 3 treatments** against the original, **one test at a time**, running **up to 90 days**. "you cannot change a test once it's started." Traffic proportion is chosen by you.
- What can be tested:
  - **app icon** (alternate icons must be in the live binary; 1024×1024)
  - **screenshots**
  - **app previews**
  - (2026) **"Header and Search Results"** creative assets

  **Not testable:** name, subtitle, description, keywords or promotional text.
- Treatment metadata needs App Review approval. Tests without new icons can be submitted without a new app version.
- The app must be live (Ready for Distribution). Tests run on iOS/iPadOS 15+.
- Not available for custom product pages or for Apple Watch / iMessage product pages.
- Apple recommends waiting for "at least 90% confidence" before applying a treatment.

### 7.2 Custom Product Pages [OFFICIAL]
Sources: [CPP](https://developer.apple.com/app-store/custom-product-pages/), [Configure CPP](https://developer.apple.com/help/app-store-connect/create-custom-product-pages/configure-multiple-product-page-versions)
- **Up to 70 CPPs.** The limit was doubled from 35 on 2025-10-29. Each CPP can vary **screenshots, app previews, promotional text and keywords**, plus a deep link (iOS 18+). Creative assets from Asset Library are also usable. Each has a unique URL.
- **Keyword assignment (added October 2025, confirmed):**
  - "You can assign keywords from your latest approved app version to a custom product page. This directs customers to your custom product page when they search those keywords, rather than your default product page."
  - "the custom product page is searchable only after it's approved and set to visible."
  - "ensure the keywords you select match the intent of your custom product page and that each keyword combination is unique to a single product page."

  **CPPs do not add new keywords.** They only re-route existing ones (name, subtitle or keywords of the approved version).
- CPPs are submitted for review independently of an app update and need the app to be Ready for Distribution. Metrics appear after five first-time downloads.
- Also usable in Apple Ads, including search results ad variations.

### 7.3 In-App Events [OFFICIAL]
See section 1.8 for limits. Events are discoverable in search, on the Today/Games/Apps tabs and on the product page. They can be submitted independently of a version.

Possible fits for Lightweight include a monthly challenge or a "Major Update" badge for a feature launch. Badge options: Challenge, Competition, Live Event, Major Update, New Season, Premiere, Special Event. The event must happen in the app at the listed dates (2.3.13).

---

## 8. Category: Health & Fitness vs Sports [OFFICIAL]
Source: [Categories](https://developer.apple.com/app-store/categories/)
- **Health & Fitness**: "Apps related to healthy living, including stress management, fitness, and recreational activities. For example: yoga, muscle diagrams, **workout tracking**, running, cycling, … weight loss, pilates…"
- **Sports**: "Apps related to professional, amateur, collegiate, or recreational sporting activities. For example: fantasy sports companions, college teams/conference, professional teams/leagues, athletes, score trackers, instruction, sports news."
- **Recommendation: Primary = Health & Fitness**, because Apple names "workout tracking" as an example. Secondary is optional. Sports is defensible only weakly; Lifestyle or Utilities are other options. Apple warns: "Choosing categories that aren't relevant is grounds for rejection" (Search page). 2.3.5: "If you're way off base, we may change the category for you."
- Two categories are allowed. "The primary category … will be the category in which the app appears when people browse the App Store or filter search results." Both primary and secondary are indexed for search. **Don't repeat category words in the keyword field** (Apple). Whether that means "fitness" and "health" should stay out of the keyword field, and how strong the category-only match is, are debated [INDUSTRY]. AppTweak calls the category a "free keyword" but doesn't recommend relying on it ([AppTweak](https://www.apptweak.com/en/aso-blog/how-to-optimize-your-ios-keyword-field)).
- Choosing Entertainment or Games would place the app in the new Time Allowance categories (iOS 27). That's another reason to avoid Entertainment as secondary.

---

## 9. App name uniqueness, reservation and trademarks
- [OFFICIAL] "You can use an app name for one app per localization." If another developer uses it "and you have trademark rights to it, you can submit a claim." ([Add a new app](https://developer.apple.com/help/app-store-connect/create-an-app-record/add-a-new-app))
- [OFFICIAL] "If you remove an app, you'll lose ownership of the app name." ([Remove an app](https://developer.apple.com/help/app-store-connect/create-an-app-record/remove-an-app))
- **180-day rule:** I found **no current Apple documentation** of a 120- or 180-day expiry for unused names. It existed historically: 120 days in 2010 per [AppleInsider](https://appleinsider.com/articles/10/09/11/apple_removing_app_store_name_squatters), with later forum mentions of 180. A forum user reports it was dropped ([forum 21429](https://developer.apple.com/forums/thread/21429)). Current practice: creating the app record reserves the name per localization ([forum 809402](https://developer.apple.com/forums/thread/809402), community answer, December 2025). Names of deleted records can remain blocked (DUPLICATE.DIFFERENT_ACCOUNT error; [forum 844943](https://developer.apple.com/forums/thread/844943), September 2026, unanswered). Status: **[UNVERIFIED] / likely no longer enforced.**
- [OFFICIAL] 4.1(c), added 2025-11-13: "You cannot use another developer's icon, brand, or product name in your app's icon or name, without approval from the developer."
- [OFFICIAL] 5.2.1: "Don't use protected third-party material such as trademarks … and don't include misleading, false, or copycat representations, names, or metadata in your app bundle or developer name."
- Developer name: the legal name, or for organizations a registered trade name/DBA. It is "set … only when adding an app to your account for the first time. You can't edit or update this name later." It is searchable.
- **IMPORTANT FINDING for Lightweight:** an existing US App Store app is **"Lightweight! Workout Analysis"** by seller **LIGHTWEIGHT LLC** ([id1580231861](https://apps.apple.com/us/app/-/id1580231861)).
  - Subtitle "Science-based training"; category Health & Fitness.
  - Free with "Lightweight Pro" IAP subscriptions; iPhone only.
  - Version 5.0.0, updated "Oct 7"; 183 ratings, 4.8.
  - It targets strength training, bodybuilding and powerlifting.

  This is the same space and the same brand word. Risks:
  - (a) A 4.1(c) / 5.2.1 rejection or a trademark claim.
  - (b) User confusion in search.
  - (c) The exact string "Lightweight" may still be free per localization, but similarity is the issue, not exact match.

  **Recommendation:** a trademark search (USPTO TESS/EUIPO) and legal clearance before committing. Also check name availability in ASC early by creating the app record. I did not check trademark registers.

---

## 10. Age rating (2025 system) and an optional profane mascot
Sources: [Age ratings values and definitions](https://developer.apple.com/help/app-store-connect/reference/app-information/age-ratings-values-and-definitions), [Set an app age rating](https://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating), [News](https://developer.apple.com/news/)

- [OFFICIAL] 2025-07-24: "The updated age rating system adds 13+, 16+, and 18+ to the existing 4+ and 9+ ratings."
  - New required questions cover in-app controls, capabilities, medical or wellness topics and violent themes. Answers were due by 2026-01-31.
  - You can "Override to Higher Age Rating"; this is required if your EULA's minimum age is higher.
  - 2026-07-09: social media capability questions were added and have been **required since September 2026**.
  - Ratings may vary by region (Australia, Brazil, Korea, Vietnam).
- Relevant descriptors (global values):

| Content | Rating impact |
|---|---|
| **Health or Wellness Topics** ("calorie tracking, dieting advice, or exercise recommendations") | **9+** |
| **Infrequent profanity and crude humor** | **9+** |
| **Frequent profanity and crude humor** | **13+** |
| Infrequent medical or treatment information | 13+ |
| Infrequent contests ("sport or fitness contests") | 4+ |
| Frequent contests | 13+ |
| Social media capability | 13+ |
| Parental controls, age assurance (in-app controls) | listed under 4+ |

- Definition: "Profanity or Crude Humor: Offensive or vulgar language that may be considered rude, obscene, or inappropriate. May include: swearing, derogatory slurs, **insult-based humor**…" **Mascot "roasts" count as insult-based humor even without swear words.**
- **Implication for Lightweight:**
  - Exercise recommendations alone push the app to at least **9+**.
  - Roasts with profanity: rated 9+ if infrequent, **13+ if frequent**.
  - Apple's questionnaire asks about *frequency* of content in the app. **I found no official provision that an opt-in or off-by-default toggle lowers the rating** [UNVERIFIED that it would]. Answer honestly (2.3.6) based on what a user can encounter.
  - Profanity must never appear in App Store assets (2.3.8 and asset best practices).
  - Slurs or demeaning content about targeted groups would breach 1.1.1, not just affect the rating.
  - Korea: Apple announced on 2026-08-12 that "starting in October 2026" the Korean storefront moves "Infrequent profanity and crude humor" from All to 12+. The Korea table on the age-rating reference page still showed it under "All" when I fetched it.
- 2.3.6: "Answer the age rating questions in App Store Connect honestly … If your app is mis-rated … it could trigger an inquiry from government regulators."

---

## 11. Recent changes worth knowing (2025–2026)
| Date | Change | Source |
|---|---|---|
| 2025-06 | Claims that screenshot text is indexed via OCR. **Unconfirmed**; tests point both ways | §2.3 |
| 2025 (iOS 26) | LLM-generated **App Tags** in search results; US-only, en_US metadata, manageable in ASC | [Manage app tags](https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-tags) |
| 2025-07-24 | New age ratings: 13+, 16+, 18+, and new questions | [News](https://developer.apple.com/news/) |
| 2025-10-29 | CPPs go from 35 to **70**, plus **keywords on CPPs** (organic search); IAEs submittable separately | [News](https://developer.apple.com/news/) |
| 2025-11-13 | **4.1(c)**: no other developer's brand or product name in your app name or icon | [News](https://developer.apple.com/news/) |
| 2026-03-31 | 11 new metadata languages (50 total) | [News](https://developer.apple.com/news/) |
| 2026-07-09 | Social media age-rating questions (required from September 2026) | [News](https://developer.apple.com/news/) |
| 2026-10-05 | **Creative assets** (product page header and search-results asset; iOS 27), **Asset Library**, product page preview tool; iPhone Duo screenshot sizes (required April 2027) | [News](https://developer.apple.com/news/), [Asset best practices](https://developer.apple.com/app-store/asset-best-practices/) |
| 2026-10-16 | Guidelines updated: **2.3.14** (creative assets) and 2.5.19 (hidden features) | [Guidelines](https://developer.apple.com/app-store/review/guidelines/) |
| 2026 (spec page) | Required iPhone screenshot class is now **"Dynamic Island (medium display)"** (1206×2622 / 1179×2556) | [Screenshot specs](https://developer.apple.com/help/app-store-connect/reference/app-information/screenshot-specifications) |

## 12. Open questions / not verified
1. Whether CPP promotional text is limited to 170 characters. It is presumed, not stated.
2. Bytes vs characters for non-ASCII keyword fields. Apple's docs conflict; the empirical answer is characters.
3. Whether event names, IAP names and secondary-localization name/subtitle are weighted for ranking. All [INDUSTRY].
4. Screenshot OCR indexing: unconfirmed.
5. Whether an opt-in profanity toggle affects the age rating: no Apple guidance found.
6. Trademark status of "LIGHTWEIGHT" in the US/EU: not checked. Needs legal review.
7. The 180-day name expiry: no current documentation found.
