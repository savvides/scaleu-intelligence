# Change history

Release dates describe library snapshots, not new factual review dates for the source material. See [releases](https://github.com/savvides/scaleu-intelligence/releases) for downloads and [commit history](https://github.com/savvides/scaleu-intelligence/commits/main/) for edits between releases.

## 3.0.0 · 2026-11-11

This release rebuilds the guides around the decisions a founder makes and closes the gaps.

- Added 16 guides: [start here](guides/start-here.md) (a roadmap by company stage), [glossary](guides/glossary.md), [resources](guides/resources.md), [go-to-market](guides/selling/go-to-market.md), [vendor review readiness](guides/selling/vendor-review-readiness.md), [evidence roadmap](guides/evidence/evidence-roadmap.md), [learning science](guides/product/learning-science.md), [interoperability](guides/product/interoperability.md), [business models and pricing](guides/business/business-models-and-pricing.md), [unit economics](guides/business/unit-economics.md), [fundraising](guides/business/fundraising.md), [exits and acquirers](guides/business/exits-and-acquirers.md), [K-12 landscape](guides/market/k12-landscape.md), [consumer learning](guides/market/consumer-learning.md), [international markets](guides/market/international-markets.md), and [market data sources](guides/market/market-data-sources.md).
- Added a `guides/business/` folder and eight [templates](guides/templates/README.md) to copy and fill in: discovery interview, pilot agreement outline, logic model, evidence brief, budget request memo, sole-source justification, trust packet checklist, and investor update.
- Rewrote the 18 existing guides and the operating principles for clarity, after *The Elements of Style*. Each now opens with its answer and an "Applies to" line and ends with one footer stating what was checked and when. Headings that other pages link to stayed; some others changed, so old anchors may fail.
- Added to existing guides: buyer roles for K-12, higher ed, and workforce in the personas; sourced federal and state purchase thresholds, the RFP process, contract terms, and a higher-ed budget calendar in procurement; published trials of AI tutoring, model choices and costs, and the law on chatbots and minors in the AI guides; institutional finances and 2025 federal policy changes in the higher-ed landscape; a rebuilt workforce and corporate learning guide. The funding landscape is now a directory; stage advice moved to the fundraising guide.
- Corrected six speaker claims in [buyer demand signals](guides/demand/buyer-demand-signals.md) that a check against the transcripts found misattributed or unsaid. The original [ASU+GSV demand signals report](sources/events/2026-asu-gsv/deliverables/demand-signals.md) is preserved and carries a dated correction.
- Removed the remaining links to the Founder Stack's restricted operator-lessons file.
- Rewrote the README and guide index, and added the house style to the contribution guide.

Known limits: new facts were checked against the linked sources on 2026-11-11 by the drafter and spot-checked the same day by a second reviewer; this is not a line-by-line audit. Each guide's footer lists what could not be verified. Some sources block automated access and were read in a browser or through a named secondary source. Facts carried over from earlier versions keep their earlier check dates unless a footer says otherwise. Figures labeled as practitioner estimates are judgment. Federal education funding, AI regulation, and company ownership were changing when this version was written; confirm them at the primary source.

## 2.2.0 · 2026-10-30

- Added a field note from ScaleU's Q1 FY27 update (July–September 2026): the stages of the student journey where ScaleU's 88 sourced higher-ed and workforce companies build, higher-ed venture funding, the Keypath and Watermark deals, the federal earnings accountability rule, news from ScaleU portfolio companies, and four reports for further reading.
- The higher-ed jobs atlas now gives the pipeline counts beside its Course Experience estimate and no longer calls Graduate & Beyond "wide open". The competitive landscape adds the Keypath and Watermark deals, the funding landscape a higher-ed funding figure, and the higher-ed landscape the earnings rule, checked at the Federal Register.

Known limits: the pipeline reflects where ScaleU looked in one quarter, not the market. The higher-ed funding figures come from ScaleU's analysis of Harmonic, a paid database, and were not independently checked. The Watermark sale had not been confirmed closed.

## 2.1.0 · 2026-10-30

- Added the first field note, on SETDA's 2026 State EdTech Trends Report, and its K-12 state findings to the procurement, K-12 regulation, and evidence tiers guides. State AI requirements in Ohio, North Carolina, and Tennessee were checked at the statute.

## 2.0.0 · 2026-10-30

- Added `AGENTS.md` (imported by `CLAUDE.md`) telling AI assistants to start in `guides/`, cite sources, keep evidence types apart, and avoid bulk-reading transcripts.
- Reorganized the library for founders and their AI assistants: `guides/` grouped by founder question (demand, selling, evidence, product, market), `sources/` for research, events, and field notes, and `about/` for provenance and licenses. Contributor files moved to `.github/`.
- Made the library Markdown only. Converted the ASU+GSV JTBD analyses to Markdown with their content preserved. Removed the validation script, tests, workflow, citation file, ASU+GSV processing scripts and metadata file, and the SXSW slide deck and preview image; the originals remain at their pinned source commits.
- Moved the EdTech pilot playbook from the ASU+GSV deliverables to `guides/selling/`, so the pilot entry point stays within the guides.
- Removed the standalone SXSW diagnostic page, which duplicated the demand validation guide.
- Made the EdTech pilot playbook the canonical source for pilot readiness filters and the decision gate. Pilot benchmarks now link to it, reconcile its cohort and timeline figures, label the pilot-to-contract rates as unsourced practitioner estimates, and cover advising, retention, and persistence pilots. Clarified the playbook's evidence window, cohort size, and HECVAT spelling. Evidence tiers and the procurement guide now state their K-12 scope and add sourced pointers for higher ed.
- Checked unsourced figures in pilot benchmarks and evidence tiers against primary sources. Evidence tiers now state what the statute and 34 CFR 77.1 require at each tier (no peer-review or publication rule; 350 or more individuals across more than one site for a single strong or moderate study under the grant regulations) in place of "200+ students and a peer-reviewed publication", note that only the top three tiers count for ESEA section 1003 school improvement, and label costs, timelines, buyers, and the investor table as ScaleU estimates. Pilot benchmarks no longer say a full academic year is required for Tier 1-2 evidence, label the active-usage and outcome-improvement figures as unsourced estimates with published effect-size benchmarks for context, replace the IRB time ranges with AAHRPP's 2025 medians, and note the Common Rule exemptions for educational research.
- Replaced automated checks with a review checklist in the contribution guide.
- Reframed research topic pages with descriptive headings and attributed interpretations and recommendations to the cited authors. Renamed `research/learning-styles-myth.md` to `research/learning-styles.md`; links to the old path no longer resolve on `main`.

Known limits: local links, research counts, and exclusion of restricted content are checked by reviewers, not automatically. Imported claims have not received a new comprehensive fact check; paper entries are not a count of unique papers. The ASU+GSV schedule retains 36 unverified title/transcript associations.

## 1.0.0 · 2026-09-19

- Consolidated EdTech Founder Stack, ASU+GSV 2026 Summit Intelligence, and Cracking Higher Ed at SXSW EDU into one library with navigation organized around founder decisions.
- Included 18 founder guides, 376 paper entries across 19 research topics, 74 conference transcripts, conference synthesis, and the SXSW EDU framework and slide deck.
- Imported 143 of 175 source files and excluded 32. Preserved source attribution and collection-specific licenses; excluded the restricted operator-lessons file.
- Added citation metadata, contribution and reporting guidance, and issue and pull request templates.

Known limits: imported claims have not received a new comprehensive fact check; paper entries are not a count of unique papers. The ASU+GSV schedule retains 36 unverified title/transcript associations, with linked transcript titles exposed for readers to check. Field notes are an empty section for future contributions.
