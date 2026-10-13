# IslamicLives audit-to-issue backlog — October 2026

## Method and limitations
Read repository tree, README, TODO, app audit, feature parity, security policy, CI configuration, Expo App.js excerpt and issue templates on 2026-10-13. Inspected existing issues before opening tasks. **No full local `npm run ci`, live end-to-end browser suite, physical-device tests or independent religious-source verification was conducted in this audit.** Therefore tickets are labelled as documented gaps, proposals or verification tasks rather than confirmed runtime bugs.

## Priority definitions
- **P0:** licensing, religious-claim integrity, corpus definition and governance needed before unqualified public positioning.
- **P1:** actionable quality, release, security and contributor infrastructure.
- **P2:** useful enhancements requiring design and testing.

## Issue groups
- Governance and scholarly evidence: [#1–#5](https://github.com/ummahbuild/IslamicLives/issues?q=is%3Aissue+is%3Aopen)
- Content provenance and narrative depth: [#6–#12](https://github.com/ummahbuild/IslamicLives/issues?q=is%3Aissue+is%3Aopen)
- Further source, reliability and roadmap tasks: issues #13–#20.
- Browser, assistive tech, mobile, perf, security and release: #14–#20 and #28–#33. Tickets #21–#27 were closed as duplicates of #14–#20.
- Discovery, localization and history exploration: #34–#40.
- Newcomer and contribution infrastructure: #41–#44.
- Eight first-timer tasks: #45–#52.

## Observed repo facts
- README documents 81 source-linked profiles, 25 traditionally listed prophets, a Three.js atlas, search, saved and share, shared web/Expo content.
- TODO acknowledges no explicit license, qualified scholarly review gaps, corpus/index incompleteness, native device tests, accessibility and deterministic browser testing.
- App audit says 100 structural production checks exist, but passing them does not establish theological truth.
- `.github/workflows/ci.yml` runs Node 24, `npm ci`, `npm run ci` on push and PR, with an artifact upload.
- `.github/ISSUE_TEMPLATE/` currently includes content correction and feature request; onboarding bug/accessibility templates are additional improvements.
- `docs/SECURITY.md` dated September 2026 reports 10 moderate Expo transitive advisories; this is a **historical audit result**, not a fresh vulnerability scan.
- `public/_headers` uses a CSP with `'unsafe-inline'` for scripts: a hardening target, not itself proof of exploitability.

## Triage rules
Every issue needs observed motivation, measurable acceptance criteria and a starting file. If a ticket describes possible behavior, reproduce it before calling it a bug. Avoid duplicate work; comment on the issue and link PRs. Only assign **good first issue** to tasks with genuinely bounded independent scope. Scholarly source disputes get qualified reviewer oversight. Security disclosures remain private.

## Proposed release gates
1. Explicit license and third-party rights review.
2. Claims and scope/coverage language verified against source methodology.
3. Review claims tracked per item and qualified scholarly review not invented.
4. Automated and representative real-device UX/accessibility testing.
5. Owner-approved privacy/support/deployment and production rollback.
6. Versioned changelog, test reports and reproducible release checks.

## Triage result
52 issues were initially created, and duplicate tickets #21–#27 were closed, leaving 45 open at the point of this audit. Eight starter issues (#45–#52) received the `good first issue` label. Scope remains provisional until a contributor reproduces or validates each claim. The repo's START_HERE guide, README and CONTRIBUTING link the backlog and first-contributor tasks.
