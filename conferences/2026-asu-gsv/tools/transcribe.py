#!/usr/bin/env python3
"""Transcribe MP3 files to markdown using OpenAI Whisper API."""

import os
import sys
import subprocess
import tempfile
import re
from pathlib import Path
from openai import OpenAI

# Config
INPUT_DIR = Path("gsv-presentations")
OUTPUT_DIR = Path("transcripts")
MAX_SIZE_MB = 24  # Stay under 25MB API limit
MODEL = os.environ.get("WHISPER_MODEL", "whisper-1")
API_KEY = os.environ["OPENAI_API_KEY"]

client = OpenAI(api_key=API_KEY)
OUTPUT_DIR.mkdir(exist_ok=True)


def get_duration_seconds(filepath: str) -> float:
    result = subprocess.run(
        ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", filepath],
        capture_output=True, text=True
    )
    import json
    info = json.loads(result.stdout)
    return float(info["format"]["duration"])


def split_audio(filepath: str, chunk_duration_s: int = 600) -> list[str]:
    """Split audio into chunks of chunk_duration_s seconds. Returns list of temp file paths."""
    total_duration = get_duration_seconds(filepath)
    if os.path.getsize(filepath) <= MAX_SIZE_MB * 1024 * 1024:
        return [filepath]

    chunks = []
    tmpdir = tempfile.mkdtemp()
    start = 0
    i = 0
    while start < total_duration:
        chunk_path = os.path.join(tmpdir, f"chunk_{i:03d}.mp3")
        subprocess.run([
            "ffmpeg", "-y", "-i", filepath,
            "-ss", str(start), "-t", str(chunk_duration_s),
            "-acodec", "libmp3lame", "-ab", "64k",  # compress to stay under limit
            "-q:a", "5",
            chunk_path
        ], capture_output=True)
        if os.path.exists(chunk_path) and os.path.getsize(chunk_path) > 0:
            chunks.append(chunk_path)
        start += chunk_duration_s
        i += 1
    return chunks


def transcribe_file(filepath: str) -> str:
    """Transcribe a single MP3 file, handling chunking if needed."""
    chunks = split_audio(filepath)
    full_transcript = []

    for i, chunk in enumerate(chunks):
        if len(chunks) > 1:
            print(f"    Chunk {i+1}/{len(chunks)}...", flush=True)
        with open(chunk, "rb") as f:
            response = client.audio.transcriptions.create(
                model=MODEL,
                file=f,
                response_format="text"
            )
        full_transcript.append(response.strip())

    # Clean up temp chunks (but not the original)
    if len(chunks) > 1:
        for chunk in chunks:
            if chunk != filepath:
                os.unlink(chunk)

    return "\n\n".join(full_transcript)


def extract_title(filename: str) -> str:
    """Extract a clean title from the filename."""
    name = Path(filename).stem
    # Remove leading number prefix like "01 - "
    name = re.sub(r'^\d+\s*-\s*', '', name)
    # Remove " | ASU+GSV Summit 2026" suffix
    name = re.sub(r'\s*[｜|]\s*ASU\+GSV Summit \d{4}$', '', name)
    return name.strip()


def main():
    mp3_files = sorted(INPUT_DIR.glob("*.mp3"))
    print(f"Found {len(mp3_files)} MP3 files to transcribe.\n")

    for i, mp3 in enumerate(mp3_files):
        title = extract_title(mp3.name)
        # Create safe filename
        num_match = re.match(r'^(\d+)', mp3.name)
        num = num_match.group(1) if num_match else f"{i+1:02d}"
        safe_name = re.sub(r'[^\w\s-]', '', title)[:80].strip()
        safe_name = re.sub(r'\s+', '-', safe_name).lower()
        out_path = OUTPUT_DIR / f"{num}-{safe_name}.md"

        if out_path.exists():
            print(f"[{i+1}/{len(mp3_files)}] SKIP (exists): {mp3.name}")
            continue

        size_mb = mp3.stat().st_size / (1024 * 1024)
        print(f"[{i+1}/{len(mp3_files)}] Transcribing ({size_mb:.0f}MB): {mp3.name}", flush=True)

        try:
            transcript = transcribe_file(str(mp3))
            # Write markdown
            md_content = f"# {title}\n\n"
            md_content += f"**Source**: {mp3.name}\n\n"
            md_content += "---\n\n"
            md_content += transcript + "\n"

            out_path.write_text(md_content, encoding="utf-8")
            print(f"    -> Saved: {out_path}")
        except Exception as e:
            print(f"    ERROR: {e}", file=sys.stderr)

    print("\nDone!")


if __name__ == "__main__":
    main()
