# Provenance and migration record

[ScaleU Intelligence](../README.md) / Provenance

This library was consolidated on September 19, 2026, from the three repositories below. That is the import date, not a new factual verification date. The initial import retained the sources' research summaries, historical claims, speaker attributions, and update dates. Subsequent editorial revisions appear in Git history.

## Sources

| Original repository and pinned commit | Destination | Files imported |
|---|---|---|
| [EdTech Founder Stack, `800fcaf`](https://github.com/savvides/edtechfounderstack/tree/800fcaf5fcc187b3ee3c35f4224cbcdc560548a6) | [Guides](../guides/README.md), [research](../research/README.md), and original license | 39 |
| [ASU+GSV 2026, `f3de496`](https://github.com/savvides/asu-gsv-2026-summit-intelligence/tree/f3de496b426a53e0e8a5b1ccdeeeedfdd808ffd2) | [ASU+GSV collection](../conferences/2026-asu-gsv/README.md) | 96 |
| [Cracking Higher Ed, `8a320b4`](https://github.com/savvides/cracking-higher-ed-sxswedu/tree/8a320b4f70386a88ba05d0e4c906578ed5b52e46) | [SXSW EDU collection](../conferences/2026-sxsw-edu/README.md) | 8 |

The [machine-readable manifest](migration.json) accounts for every tracked file at those commits: its original path and SHA-256 hash, and either its destination or an exclusion reason. Imported files also have an initial import hash and a description of any migration edits. These hashes record the initial transfer; later maintenance belongs in Git history.

The 143 imported files include the founder reference material, 19 research topics, 74 summit transcripts, reports, schedules, structured session and demand-analysis data, the original processing scripts, and both SXSW slide formats. The original repositories and their histories remain available at the links above. Their Git histories were not merged into this repository, which would also import material excluded below.

## Exclusions

- `edtechfounderstack/data/operator-lessons.md`: the source [license](../licenses/founder-stack.txt) explicitly prohibits redistribution as raw content. The file is not included. Existing references link to its pinned original location.
- Source-specific agent instructions, workflows, contribution templates, repository documentation, ignore files, and Founder Stack promotional HTML: replaced by the unified navigation, contribution guide, ignore rules, and validation workflow. Each excluded path is listed individually in the manifest, and remains available in its source history.

Conference changelogs and SXSW presentation assets are retained as historical material. The sources' licenses are preserved; see [license scopes](../LICENSE.md).

## Changes made during migration

- Moved Founder Stack's reference files to `guides/`, its research collection to `research/`, and its ethos to `guides/ethos.md`.
- Grouped each conference's material under its own dated directory. Added a conference index, a transcript index, and links back to the library.
- Repaired the summit schedule's relative transcript links, which originally pointed into a nonexistent `schedule/transcripts/` directory.
- Labeled those links with the actual transcript titles and flagged 36 differing-title associations as unverified. The original schedule associations and transcript metadata remain source-supplied; the separate transcript index provides direct browsing by title.
- Pointed the buyer-demand guide to the local summit collection. Changed references to the excluded operator-lessons file to links to the original source.
- Added source-context notes to the research and event entry pages. Clarified that the research total counts paper entries, with possible overlap between topics.
- Replaced the SXSW page's outdated installable-skills claim with links to the actual guides. Updated its contribution-guide path.
- Documented the original processing utilities' working directories and prerequisites. The scripts and their original requirements are unchanged; their private inputs are not part of the public sources and were not imported.
- Removed trailing spaces and extra final blank lines flagged by `git diff --check` in the imported files. These whitespace edits are recorded in the manifest.

At consolidation, transcripts retained their text, with whitespace-only cleanup where flagged. Research topic tables, slide files, and license notices were byte-identical to their sources. No new meeting observations or research claims were invented for the consolidation. Later research edits use neutral topic framing and attribute interpretations to the cited authors; the original source and import hashes remain unchanged.

## Validation and publication

`make check` validates local Markdown file targets, research table structure and counts, imported destination coverage, restricted-file exclusion, and Python syntax, and runs regression tests of the checker. It does not check URL availability, heading fragments, factual accuracy, or the optional processing scripts against private inputs.

The source repositories have not been changed, redirected, or archived. This consolidation is reviewed through a pull request in `scaleu-intelligence`; merging publishes the library on GitHub. Retiring the source repositories is a separate maintainer action after the destination is accepted.
