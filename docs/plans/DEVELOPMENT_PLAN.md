# Islamic Lives development plan

The repository is now staged as an npm-workspace monorepo with web and Expo apps plus a generated shared-content package. See `MONOREPO_MIGRATION.md` and `FEATURE_PARITY.md` for migration gates and platform differences.

## Phase 1 — Evidence harness

- Maintain structured Qur’an and Sunnah coverage for every prophet.
- Fail validation when a prophet lacks Qur’an references or a declared Sunnah status.
- Run data generation, static-page generation, validation, JavaScript syntax checks, and existing tests from one command.
- Add a repository-local editorial skill so future work follows the same evidence boundaries.

## Phase 2 — Prophet depth

- Work prophet by prophet, beginning with the longest Qur’anic narratives: Musa, Ibrahim, Nuh, Yusuf, Isa, and Adam.
- Split summaries into narrative units and attach citations to each claim.
- Record verse coverage independently from name-token coverage.
- Review Sahih al-Bukhari and Sahih Muslim first; add other collections only with the displayed grading and edition details.
- Never convert later tafsir, Isra’iliyyat, popular storytelling, or archaeology into unqualified Qur’anic fact.

## Phase 3 — Review workflow

- Add `draft`, `source-reviewed`, and `scholar-reviewed` editorial states.
- Produce a review queue showing changed claims, sources, and unresolved disagreements.
- Obtain review from qualified scholars representing an explicitly stated methodology; record reviewer and date with consent.

## Phase 4 — Product quality

- Create crawlable routes for the atlas and methodology pages.
- Crawlable routes, structured metadata, static error fallback, internal-link checks, and native release-contract checks are now automated.
- Branded loading states, reduced-motion-aware transitions, contextual Qur’an/surah references, and explicit linked Sunnah reports are implemented across the primary reading experience.
- Branded social preview artwork and metadata checks are complete. Add automated browser accessibility checks and explicit page-weight budgets.
- Add CI and preview deployment after the no-package policy and hosting target are confirmed.
- Preserve the atlas interaction contract in browser tests: WebGL fallback, 0.5×/1×/2× playback, a fully visible final chapter, multi-stop camera tours, and manual camera takeover.

## Phase 5 — Native release

- The Expo SDK 57 workspace, shared content package, EAS profiles, and CI export gate are now present.
- Category filtering, four-step discovery, native deep-link routing, persistent saved profiles, and initial app icon/splash assets are implemented.
- Confirm final store artwork with ummah.build, add store screenshots and privacy-policy copy, and complete VoiceOver/TalkBack verification.
- Configure EAS project ownership and store credentials only after the ummah.build owner approves identifiers and listing content.
- Run TestFlight and Play internal testing before public submission.

## Release gate

Do not market the collection as exhaustive until the corpus definitions in `research/SCOPE.md` are closed and every coverage claim is reproducible.

The current generated collection has 81 profiles. The older 77-person target predates the 18 requested additions to the 63-profile main branch and is retained only as historical prompt context, not as a release invariant.
