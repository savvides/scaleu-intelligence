# Instructions for AI assistants

This repository is ScaleU Intelligence: a Markdown library of advice and evidence for edtech founders. Nothing needs to be installed or run.

## Answering a founder's question

1. Read `guides/README.md`, pick the folder that matches the question (`demand/`, `selling/`, `evidence/`, `product/`, `market/`), and answer from those guides first.
2. Follow a guide's links into `sources/` only when you need detail. Don't read `sources/events/*/transcripts/` in bulk; transcripts are long and record what speakers said, not verified results.
3. Skip `about/` and `.github/` unless asked about licensing, the field-note template, or contributing.

## Reporting what you found

- Cite the library file and the original source it cites (paper DOI, statute, official dataset, transcript).
- Keep evidence types apart: research findings, laws and official statistics, speaker claims, and figures the guides label as ScaleU or practitioner estimates.
- Give dates. Most guides end with an updated or checked date; recheck anything time-sensitive (regulations, funding, company status) at its primary source.
- If the library doesn't cover the question, say so instead of filling the gap.

## Editing the library

Follow `.github/CONTRIBUTING.md`. The rules most often missed:

- Add only Markdown files. Link to anything else at its original location.
- Add each new page to its section index (the table in CONTRIBUTING.md says which one).
- When moving, renaming, or deleting a page, search the repository for its old path and fix every link, including indexes.
- Change a guide's review date only after rechecking its facts; a formatting edit is not a fact check.
- Nothing runs automatically: there is no build, test, or link checker. Check links and the diff by hand.
