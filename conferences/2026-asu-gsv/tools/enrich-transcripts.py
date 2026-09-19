#!/usr/bin/env python3
"""Enrich transcript files with YAML frontmatter from video-metadata.json."""

import json
import os
import re
from pathlib import Path

TRANSCRIPTS_DIR = Path("transcripts")
METADATA_FILE = Path("video-metadata.json")

with open(METADATA_FILE) as f:
    videos = json.load(f)

# Build lookup by num
meta_by_num = {v["num"]: v for v in videos}

def add_paragraph_breaks(text, sentences_per_para=4):
    """Add paragraph breaks to a wall of text."""
    # Split on sentence boundaries (period + space + capital letter)
    # This is a rough heuristic but works for speech transcripts
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)

    paragraphs = []
    current = []
    for i, s in enumerate(sentences):
        current.append(s)
        if len(current) >= sentences_per_para:
            paragraphs.append(' '.join(current))
            current = []
    if current:
        paragraphs.append(' '.join(current))

    return '\n\n'.join(paragraphs)


def enrich_transcript(filepath, meta):
    """Add YAML frontmatter and structure to a transcript file.
    Skips files that already start with YAML frontmatter — re-enriching a
    hand-edited transcript would treat its prior headers as transcript body
    and produce duplicated, garbled headers.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if content.startswith('---\n'):
        return None  # already enriched, leave alone

    # Extract original title (first H1)
    title_match = re.match(r'^#\s+(.+)', content)
    original_title = title_match.group(1) if title_match else meta.get('yt_title', 'Unknown')

    # Extract the transcript body (everything after the --- separator)
    parts = content.split('---', 2)
    if len(parts) >= 3:
        transcript_body = parts[2].strip()
    elif len(parts) >= 2:
        transcript_body = parts[1].strip()
    else:
        # No separator, take everything after the title
        lines = content.split('\n', 3)
        transcript_body = lines[-1].strip() if len(lines) > 1 else content

    # Clean up: remove **Source**: line if present
    transcript_body = re.sub(r'\*\*Source\*\*:.*?\n', '', transcript_body).strip()

    # Add paragraph breaks if the transcript is one big block
    if transcript_body.count('\n\n') < 5 and len(transcript_body) > 1000:
        transcript_body = add_paragraph_breaks(transcript_body)

    # Build frontmatter
    speakers = meta.get('speakers', '')
    track = meta.get('track', 'Unknown')
    tags = meta.get('tags', '')
    day = meta.get('day', '')
    time = meta.get('time', '')
    yt_url = meta.get('yt_url', '')
    schedule_url = meta.get('schedule_url', '')

    frontmatter = f"""---
title: "{original_title}"
speakers: "{speakers}"
track: "{track}"
tags: "{tags}"
day: "{day}"
time: "{time}"
youtube_url: "{yt_url}"
schedule_url: "{schedule_url}"
---"""

    # Build enriched content
    enriched = f"""{frontmatter}

# {original_title}

**Speakers:** {speakers if speakers else 'Not identified'}

**Track:** {track} | **Tags:** {tags if tags else 'N/A'}

**Date:** {day}{', ' + time if time else ''}

**YouTube:** [{meta.get('yt_title', original_title)}]({yt_url})

---

## Full Transcript

{transcript_body}
"""

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(enriched)

    return original_title


# Process all transcripts
processed = 0
for fn in sorted(os.listdir(TRANSCRIPTS_DIR)):
    if not fn.endswith('.md'):
        continue

    # Extract number from filename
    num_match = re.match(r'^(\d+)', fn)
    if not num_match:
        continue

    num = num_match.group(1)
    meta = meta_by_num.get(num)

    if not meta:
        print(f"  SKIP (no metadata): {fn}")
        continue

    filepath = TRANSCRIPTS_DIR / fn
    title = enrich_transcript(filepath, meta)
    if title is None:
        print(f"  SKIP (already enriched): {fn}")
        continue
    processed += 1
    print(f"  [{processed}] Enriched: {fn}")

print(f"\nDone! Enriched {processed} transcripts.")
