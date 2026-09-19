# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/).

## [1.2.0] - 2026-04-30

### Added

- 30 new session transcripts focused on institutional operating layer, change management, AI cognition debates, vibe-coding, and student-support funding
- Round Two analysis in demand-signals.md: five additional panels on the post-ESSER buyer, change-management gap, compliance lever, dependency anxieties, and the buyer-becomes-builder shift
- Theme 7 (AI's effect on cognition) in summit intelligence report, plus new subsections on the anthropomorphism problem, the credential glut, when the tech is ready and the org isn't, the higher-ed value unwind, and mental health and the compliance lever
- Sixth executive-summary signal on the unsettled cognition question
- `tools/match-schedule.py`: fuzzy title matcher that proposes video-metadata.json entries for new transcripts and surfaces low-confidence matches for review

### Changed

- Sentence-case headings throughout the summit report (was mixed title/sentence case)
- Speaker name corrections sourced from transcripts: Josh Allen (Walmart Academy), Sam Chaudhary (ClassDojo), Austen Allred (Gauntlet AI)
- Reed Hastings Rwanda paraphrase replaced with the verbatim transcript quote
- `tools/enrich-transcripts.py` is now idempotent: re-running on already-enriched transcripts is a safe no-op
- `tools/transcribe.py` accepts a `WHISPER_MODEL` env var to override the default model

## [1.1.0] - 2026-04-24

### Added

- Demand signals analysis from five summit panels on education leader adoption decisions
- Jobs-to-be-Done switch analysis of five adoption-signal panels with structured evidence scoring
- Cross-panel pattern analysis identifying three job clusters

### Changed

- Removed PDF frontmatter from deliverables for cleaner GitHub rendering
- Updated README Quick Start section to include demand signals

## [1.0.0] - 2026-04-23

### Added

- 44 enriched session transcripts with YAML frontmatter (speakers, track, tags, YouTube links)
- Summit Intelligence Report: thematic synthesis of key signals
- Full session index covering all 461 ASU+GSV 2026 sessions
- ScaleU-relevant session filter
- Roundtable memo from "What If Universities Stopped Running the Same Pilot Twice?"
- EdTech Pilot Playbook with evaluation and diagnostic frameworks
- Structured video metadata (video-metadata.json)
- Python tooling for transcript generation and enrichment
- CC BY 4.0 licensing
