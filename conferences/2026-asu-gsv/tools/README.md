# Original ASU+GSV processing utilities

[Back to the collection](../README.md)

These three scripts are preserved from the source repository. Reading, editing, and publishing this library does not require them. They have not been exercised against the original audio or private schedule during consolidation.

| Script | Inputs and prerequisites | Behavior |
|---|---|---|
| `transcribe.py` | Run from the event directory; MP3s in `gsv-presentations/`, `ffmpeg`/`ffprobe`, the `openai` package from `requirements.txt`, and `OPENAI_API_KEY` | Sends audio to the hosted OpenAI transcription API and writes `transcripts/`; skips existing output files. API usage incurs charges. |
| `enrich-transcripts.py` | Run from the event directory; `video-metadata.json` and existing transcripts | Rewrites transcript frontmatter and headings from metadata. |
| `match-schedule.py` | The `openpyxl` package (not listed in the original requirements); private schedule and audio files | Uses the original event-specific matching rules and produces proposed metadata. Review the script before reuse. |

`match-schedule.py` resolves its private inputs relative to the event directory's parent. In this layout it expects `conferences/private/source-data/ASU_GSV_2026_Schedule.xlsx` and `conferences/private/source-audio/`. Those source files are not included. Private directories and MP3s are ignored by Git.

The original requirements and scripts remain unchanged for provenance. Review their inputs and outputs before running them. No processing tools or paid API calls run in the repository's validation workflow.
