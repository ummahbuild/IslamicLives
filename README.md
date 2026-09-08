# Islamic Lives

Islamic Lives is an evidence-first web and Expo experience for exploring named people in the Qur’an, Sunnah, and Islamic history through **When → Where → Life → Story**.

The current working edition contains 81 profiles, including the 25 prophets in the commonly taught list, other Qur’anic people, Companions, scholars, scientists, travellers, rulers, and builders. It is a growing research collection—not an exhaustive religious or historical database.

## What is included

- Source-linked profiles with visible uncertainty notes.
- Qur’anic passages and separately labelled transmitted hadith reports.
- Search, category filters, random discovery, Saved Lives, and shareable URLs.
- A Three.js atlas with sourced chapters, illustrative extents, camera tours, and 0.5×/1×/2× playback.
- Crawlable pages with structured metadata, sitemap, `robots.txt`, and `llms.txt`.
- An Expo SDK 57 app using the same generated content package as the web app.
- A repository-local editorial skill and validation harness.

## Repository structure

```text
IslamicLives/
├── apps/
│   ├── web/                 Static web development/build wrapper
│   └── mobile/              Expo application and native assets
├── packages/content/        Generated data shared by web and Expo
├── public/                  Deployable static website and generated routes
│   ├── data/                People, coverage, mentions, and atlas JSON
│   ├── people/              Generated non-prophet profile routes
│   ├── prophets/            Generated prophet profile routes
│   └── vendor/              Pinned Three.js and map dependencies
├── scripts/                 Generators, audits, tests, and release checks
├── skills/                  Repository-local editorial workflow
├── research/                Scope, verification, and fact-check records
├── docs/                    Audits, plans, and project documentation
└── .github/                 CI and contributor templates
```

Generated JSON and profile HTML must not be edited by hand. Make profile changes in `scripts/build_data.py`, atlas changes in `scripts/build_atlas.py`, then rebuild.

## Local development

Requirements: Node.js 24 (see `.nvmrc`), npm, and Python 3.

```sh
npm install
npm run ci
npm run web
```

Run Expo separately with:

```sh
npm run mobile
```

## Validation commands

| Command | Purpose |
| --- | --- |
| `npm run content:build` | Regenerate profile pages and synchronize shared content |
| `npm run audit` | Validate data, citations, links, JavaScript, mentions, and atlas models |
| `npm run production:check` | Verify metadata, social artwork, native assets, and release contracts |
| `npm run mobile:check` | Export the Expo web target as a compilation check |
| `npm run ci` | Run the complete local release gate |

Passing validation proves structural and product invariants. It does not prove theological correctness, exhaustive coverage, or independent historical truth.

## Editorial standards

- Do not invent dates, locations, dialogue, motives, appearance, relationships, or narrative detail.
- Separate Qur’anic text, hadith, historical primary material, and modern scholarship.
- Link every material claim to a supporting source.
- Preserve variant dates, disputed identities, and interpretive uncertainty.
- Treat coordinates as schematic associated-place locators, never precise birthplace claims.
- Never label a profile “scholar reviewed” without an identified qualified reviewer and recorded scope.

Read [CONTRIBUTING.md](CONTRIBUTING.md), the [editorial workflow](skills/islamic-lives-editorial/SKILL.md), and [profile review checklist](skills/islamic-lives-editorial/references/review-checklist.md) before changing content.

## Documentation

- [Documentation index](docs/README.md)
- [Development plan](docs/plans/DEVELOPMENT_PLAN.md)
- [Web/mobile parity](docs/plans/FEATURE_PARITY.md)
- [Repository TODO](TODO.md)
- [Application audit](docs/audits/APP_AUDIT.md)
- [Research scope](research/SCOPE.md)
- [Prophet fact-check](research/PROPHET-FACT-CHECK.md)
- [Requested additions fact-check](research/ADDITIONS-FACT-CHECK.md)
- [Verification record](research/VERIFICATION.md)
- [Security policy](docs/SECURITY.md)

## Current limits

- The Qur’anic name index does not cover every pronoun, title, alternate name, or unnamed figure.
- Hadith coverage is not corpus-complete.
- Most profiles lack documented review by a qualified Islamic scholar.
- Native iPhone Safari, VoiceOver, TalkBack, TestFlight, and Play internal testing remain.
- Atlas extents and routes are illustrative—not borders, ownership, conversion percentages, or exact paths.

## Deployment

The static web deployment serves `public/`. Production publication remains owner-controlled.

```sh
wrangler pages deploy public --project-name islamic-lives --branch main
```

Do not deploy contributor branches without maintainer approval.

## Contributing and licence

Contributions are welcome, especially source corrections, uncertainty improvements, accessibility fixes, tests, and bounded biographies. See [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

No open-source licence has been declared yet. Until the maintainers add one, normal copyright restrictions apply even though contributions are accepted.

Built by [ummah.build](https://ummah.build) · [X](https://x.com/ummahbuild) · [LinkedIn](https://www.linkedin.com/company/ummah-build) · [TikTok](https://www.tiktok.com/@ummah.build) · [GitHub](https://github.com/ummahbuild) · [YouTube](https://www.youtube.com/@ummah_build)
