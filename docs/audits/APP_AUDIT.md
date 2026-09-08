# Islamic Lives application audit

Reviewed: 2026-09-08

## Summary

The app has a strong evidence-first premise, 25 prophet records, accessible core controls, a sourced historical atlas, and crawlable profile output. Its largest remaining risk is editorial scale: a valid JSON structure does not prove that a paraphrase is complete, that every relevant verse or hadith has been found, or that a scholar has reviewed interpretation.

## Findings

| Priority | Area | Finding | Required response |
| --- | --- | --- | --- |
| P0 | Religious accuracy | Automated checks validate citations but cannot validate theology or interpretation. | Require qualified human review before marking a profile “reviewed.” |
| P0 | Coverage claims | The Qur’an name index omits pronouns, alternate names, and unnamed references; hadith coverage is not corpus-complete. | Keep “partial” labels and publish corpus/version boundaries. |
| P1 | Prophet depth | Most prophet profiles remain concise two-section summaries. | Expand by narrative unit, record every verse range, and add only verified hadith. |
| P1 | Hadith provenance | The first verified set is mainly Sahih al-Bukhari. | Add collection, number, grade, translator/source, and review status as structured fields. |
| Complete | Routing | Crawlable `/about/`, collection, profile, atlas, and 16 chapter-specific routes are generated with canonical metadata. | Keep the route and metadata checks active. |
| Complete | Testing | The deterministic audit covers generators, links, content, JavaScript, atlas behavior, performance budgets, and hosted CI. | Add device/browser automation without weakening the existing checks. |
| Complete | Social previews | A visually inspected 1200×630 branded Open Graph image is wired to the home and collection pages with alt text and large-card metadata. Individual biography pages intentionally avoid implying that the generic artwork depicts the person. | Keep the release check active and refresh the asset only when branding changes. |
| P2 | Offline/error UX | Generated pages now retain sourced static content when enhancement fails; the home application still uses an error panel. | Consider a service worker only if offline use becomes a product requirement. |
| P2 | Accessibility | Keyboard basics exist, but no automated accessibility scan or screen-reader review is recorded. | Add axe-based checks when a browser-test dependency is approved. |
| P2 | Performance | Initial and atlas-specific transfer budgets are enforced; interaction and animation targets still need device telemetry. | Measure latency and frame rate on representative mobile hardware before turning those targets into CI thresholds. |

## Definition of editorial completeness

A prophet page is not “complete” merely because every field is non-empty. Completion requires a Qur’an narrative audit, explicit alternate-name handling, verified hadith references with grading context, tafsir boundaries, disagreement notes, and named human scholarly review. Until then the UI must say “working profile” or “research gap.”

## 100-point production contract

The release audit now enforces exactly 100 deterministic points: one complete structural contract for each of the 81 profiles and 19 cross-product invariants covering counts, routes, evidence classes, static fallbacks, prominent journey identity, accessibility semantics, responsive styling, web/Expo persistence parity, atlas controls, contributor documentation, GitHub templates, and hosted CI. Passing this contract detects regressions; it does not replace fact-checking, device testing, security review, or qualified scholarly review.
