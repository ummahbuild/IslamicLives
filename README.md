# Islamic Lives

An original implementation of the When → Where → Life → Story discovery pattern of https://anyhumanever.com, using named people and cited accounts.

## Monorepo workspaces

- `apps/web`: development and build wrapper for the existing static production site.
- `apps/mobile`: Expo SDK 57 mobile application with the same people, references, search, discovery, sharing, chronology, and methodology goals.
- `packages/content`: generated shared data; never edit its JSON by hand.

Run `npm run content:build` before web or mobile release builds so both apps consume the same evidence dataset.

## Current state

Working edition, **not an exhaustive historical database**. The original user scope has expanded to every person mentioned in the Qur’an, hadith, and historical books, plus how Islam spread through 2026. Completion must not be claimed until the corpus is bounded, indexed, reviewed, and its coverage verified.

- 63 people, including the 25 traditionally listed Qur’anic prophets and an initial four-profile Islamic scholars collection.
- Source references at the paragraph level and uncertainty notes.
- Search, category filters, era selection, random discovery, shareable story URLs.
- Crawlable Explore, Prophets, Scholars, People, Sources, and Atlas entry pages with a custom 404 fallback.
- Three.js globe with 16 chapters, play/pause, timeline scrubbing, region selection, and sourced approximate Muslim population snapshots.
- Static site with vendored Three.js r180 browser modules; no package install, API keys, accounts, or database server needed.

## Run and verify

```sh
python3 scripts/build_data.py
python3 scripts/build_pages.py
python3 scripts/validate.py
python3 -m http.server 4387 --bind 127.0.0.1 --directory public
```

For the complete local generation and verification harness, run:

```sh
scripts/audit.sh
```

The hand-reviewed seed is in `scripts/build_data.py`. It generates `public/data/people.json`. Edit the seed, not its output. Coverage and spread chronology have their own JSON files.

`scripts/build_pages.py` generates crawlable profile URLs, JSON-LD metadata, `sitemap.xml`, `robots.txt`, and `llms.txt`. Run it after changing the people seed.

The repository-local `skills/islamic-lives-editorial` skill defines the evidence and review workflow for future biography work. The current product audit and roadmap live in `docs/audits/APP_AUDIT.md` and `docs/plans/DEVELOPMENT_PLAN.md`.

The 25-profile source-alignment review and its limits are recorded in `research/PROPHET-FACT-CHECK.md`.

## Deployment

Cloudflare Pages serves only `public/`. Deployment uses the existing globally installed Wrangler CLI; no dependency installation is required.

```sh
wrangler pages deploy public --project-name islamic-lives --branch main
```

## Editorial boundaries

Qur’an, hadith, historical primary texts, and modern scholarship are distinct evidence classes. An event in a religious report is labelled accordingly. No fictional lives, dialogue, internal thoughts, portraits, precise dates, or unsupported locations are generated. Coordinates are schematic associated-place locators.

Dates marked “not established” must remain null in numeric fields. Inclusion is not endorsement of a person or a judgement about their faith. Sunni and Shia accounts must be attributed, not silently merged. Dhul-Kifl’s prophetic status is flagged as a matter of interpretation. Zewail is included in the modern history of the Muslim world; his scientific work is not a theological claim.

## Next research requirements

See `research/SCOPE.md`. No package installation or dependency upgrade is authorized by this repository.

## Qur’anic reference index

`public/data/quran-mentions.json` adds verse links for 38 people using 649 source-tagged word locations from the Quranic Arabic Corpus. The index preserves query URLs, source counts, retrieval dates and page digests. The source does not cover every narrative reference; known omissions are disclosed in the UI.

Refresh with `python3 scripts/index_quran_mentions.py`. This performs read-only network requests and only writes a new output after every selected source query reconciles. Run `python3 scripts/test_mentions.py` for the external-format regression checks. Attribution and source terms are in `public/data/MENTIONS-NOTICE.txt`.

## World atlas

Open `#spread` (undated scriptural beginning) or `#spread/2026`. `scripts/build_atlas.py` generates the original sourced chapter data in `public/data/atlas.json`. `node --test scripts/test_atlas.mjs` checks source references, missing-value handling, regional arithmetic, and globe coordinates.

Global counts: WCD 2026 provides 1900, 1970, 2000 and 2026 estimates. Pew 2025 provides 2010 and 2020 global and regional snapshots. These methodologies differ and are not interpolated into one growth series. The 2026 regional map remains explicitly dated 2020. No global counts are invented for earlier periods.

Three.js browser modules and Natural Earth land polygons are pinned by upstream commit, with URLs and SHA-256 hashes in `public/vendor/manifest.json`; licenses and attribution are retained. WebGL failure leaves the chapter controls, sources and location list usable.
