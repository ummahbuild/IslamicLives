# Start here — your first contribution to IslamicLives

Welcome! IslamicLives is a public educational repository for source-aware biographies and illustrative historical exploration. **The repository currently has no declared open-source license.** Code visibility and invitations to contribute do not grant automatic permission to reuse or redistribute the repository. Maintainers are working on a licensing decision ([issue #1](https://github.com/ummahbuild/IslamicLives/issues/1)). If license terms affect your contribution, ask in an issue first.

## Choose your path

**No-code / researcher (15–60 minutes)**: read a public profile, inspect a source, and open a [content-correction report](.github/ISSUE_TEMPLATE/content-correction.yml) giving exact text, source location and proposed change. Do not submit a guess, generated citation, or unsourced religious summary.

**First code PR (1–2 hours)**: choose a [beginner-sized task](https://github.com/ummahbuild/IslamicLives/issues?q=is%3Aissue+is%3Aopen+%22Good+first+issue%22), comment briefly with your intended approach, and wait for the maintainer to confirm scope if the issue is being actively claimed.

**Reviewer / educator**: start with the [editorial workflow](skills/islamic-lives-editorial/SKILL.md) and [review checklist](skills/islamic-lives-editorial/references/review-checklist.md). Review of sources is not the same as qualified Islamic scholarly endorsement.

## Five-minute local setup (after dependencies install)

Prerequisites: **Node 24** (see `.nvmrc`), npm, Python 3, Git. No accounts, tokens, or deployment credentials are needed for the local public build.

```bash
git clone https://github.com/ummahbuild/IslamicLives.git
cd IslamicLives
npm ci
npm run ci
npm run web
```

For mobile (optional): `npm run mobile`. Native testing requires the appropriate Expo development environment and device/emulator. Do not deploy to production.

If you do not have write access, [fork the repository](https://github.com/ummahbuild/IslamicLives/fork), clone **your fork** instead, create a descriptive branch, commit, push, and open a pull request against `ummahbuild/IslamicLives:main`. The clone command above checks out the upstream read-only copy; use your fork URL for the PR route.

## Where files belong

| Goal | Source of truth | Do not edit directly |
| --- | --- | --- |
| Biography / evidence data | `scripts/build_data.py` and review records | `public/data/people.json`, `packages/content/data/people.json`, generated profile HTML |
| Atlas model | `scripts/build_atlas.py` and evidence | Generated atlas JSON |
| Generated pages | `scripts/build_pages.py` | Generated profile page HTML |
| Web UI | `public/app.js`, `public/style.css`, atlas modules | Don't add unsourced claims |
| Mobile UI | `apps/mobile/App.js` | Don't break web/mobile parity |
| Tests | `scripts/` and related docs | Don't weaken release gates to get a green build |

Content workflow: edit generator source → attach sources and uncertainty → `npm run content:build` → `npm run ci` → inspect changed output and note any generated diffs. **Never edit generated JSON or profile HTML directly.**

## Your first PR checklist
1. Search issues and PRs for duplicates, then choose a small task.
2. Reproduce or explain the current behavior. A test-only PR is valuable if no bug exists.
3. Make the smallest change that addresses the task.
4. Run `npm run ci` when feasible; report exact exceptions and environment.
5. If UI changes, check desktop, 390px, keyboard focus, reduced motion, and accessible text; include screenshots where useful.
6. If content changes, cite direct Qur'anic surah/ayah or hadith collection/report and edition, or credible historical scholarship. Record ambiguity.
7. Open a PR using the template and link its issue (e.g. `Closes #47` only when fully satisfied).
8. Respond respectfully to reviewer feedback; review timing depends on volunteer capacity.

## Choose a starter ticket
- [#45 Documentation link clarification](https://github.com/ummahbuild/IslamicLives/issues/45) — documentation
- [#46 No-results search regression test](https://github.com/ummahbuild/IslamicLives/issues/46) — test
- [#47 390px biography review](https://github.com/ummahbuild/IslamicLives/issues/47) — UI/accessibility
- [#48 Source-link regression](https://github.com/ummahbuild/IslamicLives/issues/48) — test
- [#49 Navigation control accessibility](https://github.com/ummahbuild/IslamicLives/issues/49) — accessibility
- [#50 Generator instructions](https://github.com/ummahbuild/IslamicLives/issues/50) — docs
- [#51 Verified alias search test](https://github.com/ummahbuild/IslamicLives/issues/51) — test
- [#52 Reduced-motion atlas test](https://github.com/ummahbuild/IslamicLives/issues/52) — QA

## Reporting problems
For reproducible bugs, include platform, build/ref, steps, expected vs actual, browser/device and redacted logs. For source disputes, identify the exact claim and reliable supporting evidence. **Security vulnerabilities and exposed secrets must not be reported in public issues**; use the channel in [security policy](docs/SECURITY.md). For interpersonal issues see [code of conduct](CODE_OF_CONDUCT.md).

Be patient and precise. A small verified improvement is better than a large unsupported rewrite.
