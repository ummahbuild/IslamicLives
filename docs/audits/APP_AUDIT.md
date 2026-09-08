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
| P1 | Routing | The home atlas/about views still use fragments. | Generate crawlable collection/methodology routes in a later routing pass. |
| P1 | Testing | There is no single project command for all generators and tests. | Add a deterministic audit runner and CI job. |
| P2 | Social previews | Metadata exists but no branded Open Graph image is present. | Produce and visually inspect one branded preview asset. |
| P2 | Offline/error UX | Data loading has one generic failure state. | Identify the failed resource and retain static page content when enhancement fails. |
| P2 | Accessibility | Keyboard basics exist, but no automated accessibility scan or screen-reader review is recorded. | Add axe-based checks when a browser-test dependency is approved. |
| P2 | Performance | Three.js is vendored and loaded only by the atlas, but budgets are not measured. | Record page-weight and interaction budgets in CI.

## Definition of editorial completeness

A prophet page is not “complete” merely because every field is non-empty. Completion requires a Qur’an narrative audit, explicit alternate-name handling, verified hadith references with grading context, tafsir boundaries, disagreement notes, and named human scholarly review. Until then the UI must say “working profile” or “research gap.”
