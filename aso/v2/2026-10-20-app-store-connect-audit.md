# App Store Connect: what is filled in, and what is not

Read 2026-10-20 through the App Store Connect API (key "Harda Claude", `2D29T2L88K`, read-only calls).
App `6820992220`, bundle `com.xata.lightweight`, version **1.0**, state `PREPARE_FOR_SUBMISSION`.
Nothing was written. The API cannot read the App Privacy labels; those need a look in the web dashboard.

## Summary

**Filled:** the App Name, the subscription group and its two plans (prices, trials, names in twelve
languages), and 5 processed builds (latest: 15, uploaded 2026-10-19).

**Blank:** everything else a submission needs — subtitle, keywords, description, support URL,
copyright, screenshots (iPhone and Apple Watch), category, age rating, privacy policy URL, price,
countries, App Review contact and demo account, and the build on the version.

**Only one listing language exists: English (U.S.).**

## App Information (applies to every version)

| Field | Value now | Required? | Searched? |
|---|---|---|---|
| Name | **Harda: Gym Workout Tracker** (26 of 30) | yes | yes, strongest |
| Subtitle | blank | no | yes |
| Primary category | blank | yes | yes |
| Secondary category | blank | no | yes |
| Privacy Policy URL | blank | yes | — |
| Privacy Choices URL | blank | no | — |
| Age rating questionnaire | every answer blank (incl. the new health, social media, user-generated content and messaging questions) | yes | — |
| Content rights declaration | blank (does the app show third-party content?) | yes | — |
| Made for kids | no | — | — |
| License agreement | Apple's standard (no custom EULA) | — | — |
| Accessibility URL | blank | no | — |
| App Store tags | none yet (Apple generates them; you can only remove) | — | US only |

## Version 1.0 page (English U.S.)

| Field | Value now | Limit | Required? | Searched? |
|---|---|---|---|---|
| Keywords | blank | 100 | no | yes |
| Description | blank | 4,000 | yes | no (web search only) |
| Promotional text | blank | 170 | no | no |
| What's New | blank | 4,000 | not on 1.0 | no |
| Support URL | blank | — | yes | — |
| Marketing URL | blank | — | no | — |
| Copyright | blank | — | yes | — |
| iPhone screenshots | **none** | 1–10 | yes (6.9" set) | — |
| Apple Watch screenshots | **none** | 1–10 | **yes, because the app ships a Watch app** | — |
| App previews (video) | none | up to 3 | no | — |
| Build | **none attached** (build 15 is the latest) | — | yes | — |
| Release | after approval | — | — | — |
| Uses IDFA | not answered | — | yes | — |

## App Review information

| Field | Value now |
|---|---|
| Contact name, phone, email | blank |
| Demo account | blank — **needed**: the app has sign-in |
| Notes | blank |

## Price and countries

| Field | Value now |
|---|---|
| App price | **not set** (base territory USD exists, no price) |
| Countries | **not set** |

## Subscriptions

Group **Harda Premium** (`22490652`).

| Plan | Product id | State | Missing |
|---|---|---|---|
| Harda Premium Monthly | `com.xata.lightweight.premium.monthly` | MISSING_METADATA | App Review screenshot |
| Harda Premium Yearly | `com.xata.lightweight.premium.yearly` | MISSING_METADATA | App Review screenshot |

No promotional images, so neither can be promoted on the product page or in search. Both must go
to review with the first app version.

## Discovery features, all unused

| Feature | Count now | What it does |
|---|---|---|
| Custom product pages | 0 (of 70) | A second product page; can be tied to keywords in search |
| Search keywords for those pages | 0 | Empty because the keyword field is empty |
| In-app events | 0 | Event cards that show in search and on the product page |
| Product page tests | 0 | A/B tests of icon and screenshots |
| Promoted in-app purchases | 0 | Subscriptions shown on the product page and in search |
| Accessibility labels | 0 | The new accessibility "nutrition label" |

## Other settings read

- Builds report a computed minimum macOS 15.0 and visionOS 2.0: unless switched off, the iPhone app
  may be offered on Apple silicon Macs and Vision Pro. Check "iPhone and iPad Apps on Apple Silicon
  Macs" in Pricing and Availability (the founders' rule is iPhone only).
- No App Clip, no Game Center, no webhooks.
- Since 2026-03-26, Health & Fitness apps in the US, UK and EU must declare whether they are a
  regulated medical device in the age-rating questionnaire (App Store Connect release notes).
