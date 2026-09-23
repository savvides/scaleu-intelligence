# Maintaining ScaleU Intelligence

Keep the library useful for edtech founders and practitioners. Prefer a focused correction or a well-sourced observation over another broad overview.

Follow the [code of conduct](CODE_OF_CONDUCT.md). The [support guide](SUPPORT.md) explains where to ask questions and report problems.

## Where an update belongs

| Material | Location | Index to update |
|---|---|---|
| Recurring advice about demand, products, buyers, or pilots | `guides/` | [Founder guides](guides/README.md) |
| Papers about learning or assessment | `research/` | [Research index](research/README.md) |
| Conference synthesis, transcripts, slides, and source metadata | `conferences/YYYY-event-name/` | [Conference index](conferences/README.md) |
| A publishable meeting observation, research note, or other finding | `notes/YYYY-MM-DD-short-topic.md` | [Field notes](notes/README.md) |

The library holds documentation only: Markdown pages, PDF or PPTX slides, images, and plain-text license notices. Apart from the existing repository metadata (the citation file, ignore rules, and GitHub issue and pull request templates), do not add code, scripts, notebooks, web pages, build or CI configuration, or structured data files such as JSON, YAML, or CSV.

## A routine update

1. Create a branch, or use GitHub's file editor and choose to propose the change in a new branch.
2. Edit the relevant guide or copy the [field-note template](templates/field-note.md). For a conference, create a collection README with the event date, author, summary, evidence limits, source links, and links to its supporting files.
3. State who the finding applies to. Cite a public primary source where possible. Keep observations, reported claims, and your interpretation distinct.
4. Record when the event happened and what you actually reviewed. Change a factual review date only after checking the facts; a formatting edit or migration is not a new fact check.
5. Add the page to its section index and link any related guides. Update the root README only when the entry point for a reader changes.
6. Work through the [review checklist](#review-checklist). Review the rendered Markdown and the diff, then merge after maintainer review.

Nothing needs to be deployed or restarted. The merged Markdown is the published library on GitHub.

## Research and dated references

For a research collection, keep the existing columns: `#`, Title, Takeaway, Type, Year, Citations, DOI. Add the paper's full citation and DOI, check the takeaway against the paper, keep rows sorted by the recorded citation count, and update the topic and total counts in the research index. Citation counts are a dated snapshot, not a quality score.

Keep research impartial. Use descriptive topic headings and report what each study or review found, including its population, comparisons, and limitations where available. Attribute interpretations and recommendations to the authors. Avoid editorial verdicts such as calling a topic a myth or debunked, or telling readers which approach to adopt. Preserve published paper titles and reported findings, including conflicting or null results; do not alter them to support a position.

For regulations, program terms, funding, or company status, check the current primary source before changing guidance. Preserve older conference statements as historical context; add a clearly dated correction instead of silently rewriting a speaker's claim.

## Meeting material

This is a public repository. Publish only content you have permission to share. Do not upload raw private meeting transcripts, student records, unpublished company data, contact lists, or credentials. Review anonymized notes for identifying details too. Keep working material outside the repository; `.gitignore` is a convenience, not a publication review.

## Attribution and licenses

Preserve existing authors, citations, and license notices. Additions to imported collections follow that collection's license. New editorial pages and field notes use CC BY 4.0. See [LICENSE.md](LICENSE.md) for the scope of each license.

## Review checklist

Reviewers check these by hand before merging; nothing runs automatically.

- Each new or changed relative link opens its target in GitHub's rendered view.
- When a page is moved, renamed, or deleted, every relative link to it elsewhere in the library is updated, including section indexes. Search the repository for the old path to find them.
- A new research topic appears once in the [research index](research/README.md). Topic tables keep the seven columns. Each topic's entry count and the index's "Total: N paper entries across M topics" line match the table rows.
- Schedule links to transcripts read "Transcript: " followed by the linked transcript's title.
- No content from the Founder Stack's restricted `data/operator-lessons.md` is added under any name.
- The change adds only the documentation formats listed under [where an update belongs](#where-an-update-belongs).

This review does not verify external websites, factual claims, speaker accuracy, or permissions to publish.

To suggest a correction without editing files, [open an issue](https://github.com/savvides/scaleu-intelligence/issues/new/choose) with the page, the proposed correction, and supporting evidence.

## Publishing a snapshot

Releases are dated snapshots of this library. They do not certify that every imported claim has been fact-checked. Routine edits can remain on `main` between releases.

1. Summarize the changes and known limitations in [CHANGELOG.md](CHANGELOG.md). Update both citation entries in [CITATION.cff](CITATION.cff), including the version, release date, year, and tagged release URL.
2. Merge the reviewed pull request after completing the review checklist.
3. Create a GitHub release with a new `vMAJOR.MINOR.PATCH` tag targeting that exact commit. Use a major version for a substantial reorganization, minor for new collections or substantial additions, and patch for corrections.
4. Write release notes describing the contents, changes, evidence limits, and collection-specific licenses. GitHub supplies the ZIP and tar.gz source archives; no package build is needed.
5. Verify the tag points to the reviewed commit, the download opens, and the latest-release link in the README resolves. Do not move published release tags; publish a new correction release.
