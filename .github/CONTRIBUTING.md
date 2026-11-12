# Maintaining ScaleU Intelligence

Keep the library useful for edtech founders and practitioners. Prefer a focused correction or a well-sourced observation over another broad overview.

The library is Markdown only: no code, scripts, data files, or binaries. Founders point their AI assistants at it, so every file must read as text. Link to anything else at its original location.

Follow the [code of conduct](CODE_OF_CONDUCT.md). The [support guide](SUPPORT.md) explains where to ask questions and report problems.

## Where an update belongs

| Material | Location | Index to update |
|---|---|---|
| Advice that answers a founder question | `guides/<question>/`: `demand/`, `selling/`, `evidence/`, `product/`, `business/`, or `market/` | [Founder guides](../guides/README.md) |
| A document a founder copies and fills in | `guides/templates/` | [Templates](../guides/templates/README.md) |
| An outside resource worth recommending | A line in [`guides/resources.md`](../guides/resources.md) | None |
| A term founders meet | An entry in [`guides/glossary.md`](../guides/glossary.md) | None |
| Papers about learning or assessment | `sources/research/` | [Research index](../sources/research/README.md) |
| Conference synthesis, transcripts, and session indexes | `sources/events/YYYY-event-name/` | [Events index](../sources/events/README.md) |
| A publishable meeting observation, research note, or other finding | `sources/notes/YYYY-MM-DD-short-topic.md` | [Field notes](../sources/notes/README.md) |
| A new kind of source material | `sources/<kind>/` with its own README | [Sources index](../sources/README.md) |

Guides synthesize; sources preserve. A guide states the advice and links to the sources behind it. A source keeps its original context, dates, and attribution.

## A routine update

1. Create a branch, or use GitHub's file editor and choose to propose the change in a new branch.
2. Edit the relevant guide or copy the [field-note template](../about/templates/field-note.md). For a conference, create a collection README with the event date, author, summary, evidence limits, source links, and links to its supporting files.
3. State who the finding applies to. Cite a public primary source where possible. Keep observations, reported claims, and your interpretation distinct.
4. Record when the event happened and what you reviewed. Change a factual review date only after checking the facts; a formatting edit or migration is not a new fact check.
5. Add the page to its section index and link any related guides. Update the root README only when the entry point for a reader changes.
6. Work through the [review checklist](#review-checklist). Review the rendered Markdown and the diff, then merge after maintainer review.

You deploy and restart nothing. The merged Markdown is the published library on GitHub.

## How a guide is written

- Open with the answer or the decision the page supports, then an **Applies to** line naming the segment and geography.
- Label evidence by type: research finding (paper and DOI), law or official statistic (primary source), speaker claim (transcript), or practitioner estimate. Label judgment as ScaleU's view.
- Link every fact to the source you checked. Leave out what you cannot verify.
- Write plainly, after Strunk's *The Elements of Style*: active voice, positive statements, concrete words, no needless ones. Use sentence-case headings, "edtech", and "K-12". Avoid slogans, scare quotes, and decorative emphasis.
- End with related guides and one footer line that gives the date the facts were checked and what the check covered.

## Research and dated references

For a research collection, keep the existing columns: `#`, Title, Takeaway, Type, Year, Citations, DOI. Add the paper's full citation and DOI, check the takeaway against the paper, keep rows sorted by the recorded citation count, and update the topic and total counts in the research index. Citation counts are a dated snapshot, not a quality score.

Keep research impartial. Use descriptive topic headings and report what each study or review found, including its population, comparisons, and limitations where available. Attribute interpretations and recommendations to the authors. Avoid editorial verdicts such as calling a topic a myth or debunked, or telling readers which approach to adopt. Preserve published paper titles and reported findings, including conflicting or null results; do not alter them to support a position.

For regulations, program terms, funding, or company status, check the current primary source before changing guidance. Preserve older conference statements as historical context; add a dated correction instead of rewriting a speaker's claim.

## Meeting material

The repository is public. Publish only content you have permission to share. Do not upload raw private meeting transcripts, student records, unpublished company data, contact lists, or credentials. Review anonymized notes for identifying details too. Keep working material outside the repository; `.gitignore` is a convenience, not a publication review.

## Attribution and licenses

Preserve existing authors, citations, and license notices. Additions to imported collections follow that collection's license. New editorial pages and field notes use CC BY 4.0. See [LICENSE.md](../LICENSE.md) for the scope of each license.

## Review checklist

Reviewers check these by hand before merging; nothing runs automatically.

- Each new or changed relative link opens its target in GitHub's rendered view.
- When a page moves, changes its name, or disappears, every relative link to it elsewhere in the library, including section indexes, points to the right place. Search the repository for the old path to find them.
- A new research topic appears once in the [research index](../sources/research/README.md). Topic tables keep the seven columns. Each topic's entry count and the index's "Total: N paper entries across M topics" line match the table rows.
- Schedule links to transcripts read "Transcript: " followed by the linked transcript's title.
- The change adds no content from the Founder Stack's restricted `data/operator-lessons.md` under any name.
- The change adds only Markdown files.

This review does not verify external websites, factual claims, speaker accuracy, or permissions to publish.

## Corrections

To suggest a correction without editing files, [open an issue](https://github.com/savvides/scaleu-intelligence/issues/new/choose) with the page, the proposed correction, and supporting evidence.

## Publishing a snapshot

Releases are dated snapshots of this library. They do not certify that anyone has fact-checked every imported claim. Routine edits can remain on `main` between releases.

1. Summarize the changes and known limitations in [CHANGELOG.md](../CHANGELOG.md). Update the version in the citation in the [README](../README.md#cite-and-reuse).
2. Merge the reviewed pull request after completing the review checklist.
3. Create a GitHub release with a new `vMAJOR.MINOR.PATCH` tag targeting that exact commit. Use a major version for a substantial reorganization, minor for new collections or substantial additions, and patch for corrections.
4. Write release notes describing the contents, changes, evidence limits, and collection-specific licenses. GitHub supplies the ZIP and tar.gz source archives; you build no package.
5. Verify the tag points to the reviewed commit, the download opens, and the latest-release link in the README resolves. Do not move published release tags; publish a new correction release.
