# Instructions for AI assistants

This repository is ScaleU Intelligence: a Markdown library of advice and evidence for edtech founders. It needs no installation and runs no code.

## Answering a founder's question

1. Read `guides/README.md`, pick the folder that matches the question (`demand/`, `selling/`, `evidence/`, `product/`, `business/`, `market/`), and answer from those guides first. `guides/start-here.md` orders the guides by company stage; `guides/glossary.md` defines terms; `guides/templates/` holds documents to fill in; `guides/resources.md` lists outside resources.
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
- Before renaming or removing a heading, search the repository for its anchor (`page.md#heading-slug`); other pages link to headings.
- Keep notes about how a fact was checked (a blocked site, a search that found nothing) in the page's footer, not in its body.
- Some sources refuse automated fetches (sec.gov, ed.gov, doi.org, and openai.com, for example). Open them in a browser before settling for a secondary source, and label any secondary source as secondary where you cite it.
- Conference transcripts in `sources/events/*/transcripts/` carry no speaker labels. Before attributing a claim to a speaker, search the transcript for the passage and confirm who said it and what was said.
- The same fact often appears in several guides. Before changing a number, date, or status, search the other guides for it so that one fact carries one value everywhere.
- Change a guide's review date only after rechecking its facts; a formatting edit is not a fact check.
- Nothing runs automatically; the repository has no build, test, or link checker. Check links and the diff by hand.
- A version bump is unfinished until the release is published: the README's citation links to the release tag. Follow "Publishing a snapshot" in CONTRIBUTING.md.
