# Scope and unfinished acceptance work

User requests (2026-09-08):
1. Recreate Any Human Ever's storyboard for actual people in Islamic history since Adam.
2. Research multiple reliable facts and create a database; JSON is acceptable when small.
3. Create a private repository under asghar07 and deploy, preferring Cloudflare for a small static dataset.
4. Expanded scope: every Islamically mentioned prophet, Sahabah, every person mentioned in Qur’an/hadith/historical books after Muhammad, and how Islam spread through 2026.

## Exhaustive coverage requires a corpus

An asynchronous question is pending: Qur’an + six major Sunni collections + documented historical selection, or Sunni and Shia collections + historical selection, or a user-supplied bibliography. Do not silently convert a curated seed to an exhaustive completion claim.

Required work:
- Audit all 114 Qur’anic chapters for named and unnamed human individuals, keeping collective groups and nonhuman beings separate. Distinguish personal names, titles, aliases, debated identifications, and unnamed people.
- All 25 traditionally named prophets have seed entries. They need a full occurrence index; most currently have two relevant references, not full biographies. Hadith-only prophets and debated identities need review.
- Define editions and numbering systems for hadith; separate isnad narrators from people in the report itself. Store original mentions and canonical person links, avoid merging namesakes.
- Define historical works, editions, access/rights, and chronological cutoffs. Mention in a book does not make all claims true. Store claim provenance and conflicts.
- Expand Sahabah and women’s coverage, successors, scholars, patrons, travellers, political figures, ordinary named people, and non-Muslims mentioned in the corpus.
- Expand spread timeline to Umayyad/Abbasid periods, Iberia, Central/South/Southeast Asia, East/West Africa, Ottoman/Safavid/Mughal worlds, colonial and postcolonial periods, migration, and recent evidence to 2026.
- Distinguish conquest from conversion, proselytism from demographic growth; do not present future 2026 events as observed.
- Source audit: use primary texts and reliable scholarship, preserve disagreements. No article copies or unlicensed source corpora in public assets.

## Research observations

- Qur’an.com individual verse pages usually work; several range pages and Britannica pages were inaccessible. Do not claim inaccessible pages as reviewed.
- St Andrews MacTutor and Stanford SEP were read successfully. SEP disputes Ibn Sina's conventional birth year; record no numeric birth year.
- Tirmidhi 3883 is graded Hasan by Darussalam on Sunnah.com. Bukhari 3 supports Khadijah and Aisha accounts; Bukhari 4987 supports Uthman copying Qur’anic manuscripts.
- Pew's 2025 Muslim population report describes 2010–2020, not a 2026 population count.
- Initial browser port 4173 had a pre-existing service worker from another project. Use isolated port 4387 for local verification.

## Continuation checkpoint

- Repo: /Users/asgharali/Development/islamic-lives; remote https://github.com/asghar07/islamic-lives (PRIVATE confirmed).
- Production: https://islamic-lives.pages.dev ; Wrangler project islamic-lives.
- 59 current entries. Main seed scripts/build_data.py imports scripts/quran_people.py. Coverage JSON explicitly partial.
- Current source leads: Quranic Arabic Corpus topic index at https://corpus.quran.com/topics.jsp links named-entity concepts and occurrence lists. Ontology derives some identifications from tafsir: names such as Abel, Cain, and Umm Jamil must not be labelled Qur’an-explicit. Public facts can be referenced; do not copy an entire licensed ontology without reviewing terms.
- Remaining immediate gaps: Dhul-Qarnayn, Tubba (title/people ambiguity), more unnamed Qur’anic individuals; full verse occurrence index; hadith-only prophets and expanded Sahabah; source bibliography boundary question still pending.
- New entries require primary passage review and clear confidence/identity labels; no count padding with fabricated biography.
- Frontend is static dependency-free. Installed Wrangler handles deployment. No package installation has been performed or authorized.

## Name-index continuation

- scripts/index_quran_mentions.py retrieves concept-tagged word references from the Quranic Arabic Corpus; public/data/quran-mentions.json has 38 people and 649 token locations.
- Source pagination and reported match counts reconcile; multiword entities are grouped for source-match counts, distinct from token counts.
- The Corpus omits 21:85 from its Dhul-Kifl concept search. A visible note supplements the source result. Do not infer exhaustiveness from source count reconciliation.
- Next: independent Quran-text occurrence comparison, alias/title maps (Ahmad/Muhammad, Israel/Yaqub, Messiah/Isa), remaining named/titled/unnamed people. Name indexing does not yet resolve pronouns or group mentions.
