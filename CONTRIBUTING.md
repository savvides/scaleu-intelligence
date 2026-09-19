# Maintaining ScaleU Intelligence

Keep the library useful for edtech founders and practitioners. Prefer a focused correction or a well-sourced observation over another broad overview.

## Where an update belongs

| Material | Location | Index to update |
|---|---|---|
| Recurring advice about demand, products, buyers, or pilots | `guides/` | [Founder guides](guides/README.md) |
| Papers about learning or assessment | `research/` | [Research index](research/README.md) |
| Conference synthesis, transcripts, slides, and source metadata | `conferences/YYYY-event-name/` | [Conference index](conferences/README.md) |
| A publishable meeting observation, research note, or other finding | `notes/YYYY-MM-DD-short-topic.md` | [Field notes](notes/README.md) |

## A routine update

1. Create a branch, or use GitHub's file editor and choose to propose the change in a new branch.
2. Edit the relevant guide or copy the [field-note template](templates/field-note.md). For a conference, create a collection README with the event date, author, summary, evidence limits, source links, and links to its supporting files.
3. State who the finding applies to. Cite a public primary source where possible. Keep observations, reported claims, and your interpretation distinct.
4. Record when the event happened and what you actually reviewed. Change a factual review date only after checking the facts; a formatting edit or migration is not a new fact check.
5. Add the page to its section index and link any related guides. Update the root README only when the entry point for a reader changes.
6. Run `make check` locally, or let the pull request's Validate check run on GitHub. Review the rendered Markdown and the diff, then merge after maintainer review.

Nothing needs to be deployed or restarted. The merged Markdown is the published library on GitHub.

## Research and dated references

For a research collection, keep the existing columns: `#`, Title, Takeaway, Type, Year, Citations, DOI. Add the paper's full citation and DOI, check the takeaway against the paper, keep rows sorted by the recorded citation count, and update the topic and total counts in the research index. Citation counts are a dated snapshot, not a quality score.

For regulations, program terms, funding, or company status, check the current primary source before changing guidance. Preserve older conference statements as historical context; add a clearly dated correction instead of silently rewriting a speaker's claim. The source's transcription tools remain with the ASU+GSV collection; they are optional historical utilities, not part of routine publishing.

## Meeting material

This is a public repository. Publish only content you have permission to share. Do not upload raw private meeting transcripts, student records, unpublished company data, contact lists, or credentials. Review anonymized notes for identifying details too. Keep working material outside the repository; `.gitignore` is a convenience, not a publication review.

## Attribution and licenses

Preserve existing authors, citations, and license notices. Additions to imported collections follow that collection's license. New editorial pages and field notes use CC BY 4.0; repository maintenance code uses MIT. See [LICENSE.md](LICENSE.md) for the scope of each license.

The [migration record](provenance/migration.json) records the initial import. Do not regenerate its source hashes or import hashes to hide later edits. Normal updates appear in Git history; if a migrated file moves, update its destination in the record and repair its links.

## Checks

`make check` needs Git and Python 3.9 or newer and uses only the standard library. It checks tracked files and new files that Git does not ignore, so private scratch files and local environments stay outside validation. It checks local Markdown file links, research table structure and counts, imported file coverage, restricted-file exclusion, and Python syntax. It also runs tests of the checker. It does not verify external websites, factual claims, speaker accuracy, or permissions to publish.

To suggest a correction without editing files, open an issue with the page, the proposed correction, and supporting evidence.
