# Verification — 2026-09-08

## Confirmed

- `python3 scripts/validate.py`: 59 unique people; expected 25 traditionally named prophet identities; paragraph source references resolve; no numeric years or coordinates on undated scriptural records.
- `node --check public/app.js`: passes.
- Local browser on port 4387: Adam When → reveal time → Where → reveal location → Life → reveal identity → Story. Date and location remain unestablished; story contains the cited Qur’anic references.
- Deployed Cloudflare Pages homepage rendered and loaded data.
- Live search for Khadijah: 1 matching person. Search for a nonexistent string: 0 results and explanatory message.
- GitHub API confirms asghar07/islamic-lives is PRIVATE.
- Cloudflare production hostname returns HTTP 200 with text/html and security headers.

## Not established

- Exhaustive person indexing across all Qur’anic verses, hadith, or historical works.
- Full regional/period coverage of Islam's spread through 2026.
- Independent scholarly review of every prose claim.
- Comprehensive browser accessibility, mobile, failure-mode and source-link checks.

No structural test is evidence of historical truth or corpus completeness. This is an intermediate working release.

## Quranic name-reference index

- Source concept queries retrieved for 38 existing people: 649 word locations, with all retrieved pages reconciled to the source's reported match counts.
- Pagination verified by Musa's 136 source-tagged locations across three pages; Adam has 25.
- Multiword names may have more token locations than source matches. Parser tests cover these spans and reject truncated or unexpected source documents.
- Known source omission: Dhul-Kifl query includes 38:48 but omits 21:85. The product explicitly links the missing primary passage and does not call this an exhaustive narrative index.
- Local browser verified reference section, direct verse links, attribution and source-gap note on Dhul-Kifl's story.
- These checks establish successful import of selected source queries, not full Qur'anic person/alias/pronoun coverage.

## 2026-09-08 — Three.js atlas

- PASS: five atlas tests (unknown counts, 2026 vs 2020 distinction, citation/connection integrity, rounded regional arithmetic, sphere coordinates); JavaScript syntax; existing dataset and mention tests.
- Browser visual testing currently unavailable: Mac locked. Do not call this browser-verified. WebGL fallback is implemented but not yet exercised in a browser.
- Primary 2026 WCD table read (row 14) through its publisher: 1900=200,301,000; 1970=576,995,000; 2000=1,311,342,000; 2020=1,917,487,000; 2026=2,105,142,000. Display rounded counts.
- Pew Appendix B first page supplies rounded regional input totals and Muslim percentages for 2010/2020. Derived counts labelled approximate; not used as 2026 regional predictions.

## Date and place evidence correction

- Re-read SEP Ibn Sina (2025 revision), Quran 10:87, 12:99 and 28:22. Added distinct date/place evidence with citation indexes for Ibn Sina, Musa, Harun and Yusuf.
- Ibn Sina displays conventional 980 alongside the SEP ca. 970 proposal; no exact numeric birth year asserted. Egypt/Madyan are named regions, while exact coordinates remain unasserted.
- PASS: regenerated dataset, evidence-citation validation, JavaScript syntax. Visual verification remains pending.

## When-page population context

- Added five WCD 2026-edition Muslim population snapshots to the When stage, with log/linear time controls, accessible tabular values and source disclosure. No extrapolation before 1900; no claim that population represents the curated person sampling probabilities.
- PASS: three chart tests (endpoints and unsupported dates; single-source 2020 value; rendered controls, table and fallback), five atlas tests and JS syntax. Browser visual review remains pending.
