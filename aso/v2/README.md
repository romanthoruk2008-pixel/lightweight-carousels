# ASO v2 — Sonar-measured listings

Second round, 2026-10-20 to 2026-10-22. Supersedes the keyword picks in `aso/drafts/app-store-v1.md`.

| File | What |
|---|---|
| [2026-10-20-app-store-connect-audit.md](2026-10-20-app-store-connect-audit.md) | What is filled in App Store Connect and what is still blank |
| [2026-10-20-aso-rules-research.md](2026-10-20-aso-rules-research.md) | How App Store search works now: limits, indexed fields, cross-localization |
| [2026-10-20-competitors.md](2026-10-20-competitors.md) | 62 US competitors, top 10 per search, autocomplete |
| [final/metadata.md](final/metadata.md) | Name, subtitle, keywords: en-US, es-MX, en-GB, de, fr |
| [final/more-locales.md](final/more-locales.md) | The same for es-ES, it, pt-BR, pl, tr, cs, uk, ru, nl |
| [research/keywords.csv](research/keywords.csv) | Every measured term: popularity, difficulty, field, locale |
| [research/seeds/](research/seeds/) | Seed lists sent to Sonar per store |

`metadata.md` mentions scripts under `Tools/ASO/`; they live in the app repo, not here.

## Changes to make before pasting

1. **Drop `fitness` from the en-US and en-GB keyword fields.** The app's categories are Health &
   Fitness and Sports, and Apple indexes category words already. Use the freed 8 characters for
   `dumbbell` (US, 31/36) and `superset` (UK, 26/5).
2. **Consider swapping `531`.** 5/3/1 is Jim Wendler's program name and may be his trademark
   (unverified). In the US, `hypertrophy` scores the same (30/25); it is in es-MX now, so es-MX
   would take a bench word instead.
3. **Sentence case** for every non-English name and subtitle except German (done in
   `more-locales.md`; the French lines in `metadata.md` still use Title Case).
4. **One line per keyword field**, no spaces or line breaks; check App Store Connect's counter,
   several fields are at exactly 100 bytes.
5. **Native-speaker check** for every non-English line.

## Done in App Store Connect (2026-10-22)

- Name `Harda: Gym Workout Tracker`, subtitle `Strength Training Log & Plans`.
- Categories Health & Fitness + Sports; content rights: no third-party content (confirm the
  exercise library's images are your own); Apple's standard EULA.
- Age rating: 13+ (12+ Vietnam and Korea, A14 Brazil).

Still open: regulated medical device declaration (No), privacy policy and support URLs, App
Privacy labels, price and countries, description with Terms of Use link, screenshots (iPhone and
Watch), review screenshots for both subscriptions, demo account, build, Mac/Vision Pro
availability, `ITSAppUsesNonExemptEncryption = NO` in Info.plist.
