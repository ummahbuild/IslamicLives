---
name: islamic-lives-editorial
description: Research, write, audit, or expand Islamic Lives profiles while preserving Qur’an, hadith, historical, and uncertainty boundaries.
---

# Islamic Lives editorial workflow

Use this skill for prophet, Companion, scholar, or other biography work in this repository.

## Required outcome

Produce concise original paraphrases with claim-level sources and visible uncertainty. Treat a non-empty field as structurally present, not necessarily researched or complete.

## Evidence rules

- Label Qur’an, hadith, historical primary text, and modern scholarship separately.
- Cite exact surah and verse ranges for Qur’anic claims.
- For hadith, record collection and canonical number. Display the consulted grading when the collection is not Sahih al-Bukhari or Sahih Muslim, and never silently promote a weak or disputed report.
- Do not infer dates, coordinates, family details, dialogue, appearance, or motives from later popular accounts.
- Attribute tafsir interpretations and sectarian or legal-school positions. Do not silently merge them.
- A source mentioning a person does not validate every claim about that person.
- If reliable evidence has not been verified, create an explicit research gap rather than filler.

Read [references/review-checklist.md](references/review-checklist.md) before marking any profile ready.

## Repository workflow

Edit the seed in `scripts/build_data.py`, not generated JSON or profile HTML. Then run `scripts/audit.sh`. Review the generated profile, its source indexes, and the coverage language. Keep `research/SCOPE.md` and `docs/audits/APP_AUDIT.md` limitations intact unless new evidence actually resolves them.
