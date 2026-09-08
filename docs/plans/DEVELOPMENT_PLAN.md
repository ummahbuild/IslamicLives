# Islamic Lives development plan

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
- Add social preview art, a robust static error fallback, automated accessibility checks, link checking, and page-weight budgets.
- Add CI and preview deployment after the no-package policy and hosting target are confirmed.

## Release gate

Do not market the collection as exhaustive until the corpus definitions in `research/SCOPE.md` are closed and every coverage claim is reproducible.
