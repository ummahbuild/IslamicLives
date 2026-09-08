# Contributing to Islamic Lives

Thank you for helping improve Islamic Lives. Content contributions carry unusual responsibility: a valid build does not make a religious or historical claim accurate.

## Before opening a contribution

1. Search existing issues and profiles for the same person or correction.
2. Read the repository [editorial workflow](skills/islamic-lives-editorial/SKILL.md).
3. For biography work, complete the [profile review checklist](skills/islamic-lives-editorial/references/review-checklist.md).
4. Keep the change focused. Separate broad interface work from contested editorial changes where practical.

## Evidence requirements

- **Qur’anic account:** cite exact surah and verse ranges.
- **Hadith:** cite collection and report number, preserving displayed grading and edition context.
- **Historical primary text:** name the work, compiler, edition or stable archive, and relevant location where practical.
- **Historical scholarship:** prefer peer-reviewed research, academic references, critical editions, university publications, or recognized institutions.

Do not use search snippets, unsourced biography sites, generated prose, social posts, or another repository summary as final authority. If sources disagree, record the alternatives. Never silently combine Sunni, Shia, tafsir, later devotional, and modern historical accounts.

## Content workflow

1. Edit `scripts/build_data.py`.
2. Add source links, evidence type, access date, and a precise uncertainty note.
3. Run `npm run content:build`.
4. Run `npm run ci`.
5. Inspect generated JSON and desktop and 390px profile rendering.
6. Update the relevant `research/` review record.

Never edit generated people JSON or generated profile HTML directly.

The CI documentation check also verifies every repository-relative Markdown link. Prefer relative links for files inside this repository so documentation works in forks and local clones.

## Engineering workflow

- Preserve the npm-workspace architecture.
- Keep web profiles readable without JavaScript and atlas content usable without WebGL.
- Maintain keyboard access, visible focus, semantic labels, reduced-motion behavior, and mobile layouts.
- Avoid dependencies when platform APIs already cover the requirement.
- Do not commit credentials, `.env` values, caches, or personal browser state.

## Pull-request checklist

- [ ] The change has a clear, bounded purpose.
- [ ] New claims have direct sources and an evidence type.
- [ ] Uncertainty and disagreement remain visible.
- [ ] Generated files were rebuilt from source scripts.
- [ ] `npm run ci` passes.
- [ ] Desktop and 390px layouts were checked for UI changes.
- [ ] Web and Expo parity implications are documented.
- [ ] No exhaustive or scholar-review claim is unsupported.
- [ ] No secrets, personal data, or unrelated generated files are included.

## Review labels

- **Structure checked:** automated schemas, links, and required fields pass.
- **Source-alignment checked:** a reviewer confirmed that cited sources support the bounded wording.
- **Scholar reviewed:** a qualified reviewer, date, methodology, and scope are recorded with consent.

Only maintainers may assign the latter two labels.

Report vulnerabilities or exposed credentials through [docs/SECURITY.md](docs/SECURITY.md), not a public issue.
