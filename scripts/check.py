#!/usr/bin/env python3
"""Offline checks for the Markdown library; no third-party dependencies."""

import ast
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]


def repository_files(root):
    names = subprocess.check_output(
        ["git", "-C", str(root), "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        text=True,
    )
    return sorted({root / name for name in names.split("\0") if name and (root / name).is_file()})


def markdown_links(text):
    """Read inline links and reference definitions, ignoring code examples."""
    text = re.sub(r"(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$", "", text)
    text = re.sub(r"`[^`\n]*`", "", text)
    inline = re.findall(r'\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)', text)
    references = re.findall(r"(?m)^ {0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", text)
    return [link.strip("<>") for link in inline + references]


def check_links(root, files):
    errors = []
    root = root.resolve()
    for path in files:
        for link in markdown_links(path.read_text()):
            url = urlsplit(link)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not target.is_relative_to(root) or not target.exists():
                errors.append(f"{path.relative_to(root)}: missing local link {link}")
    return errors


def check_research(root):
    errors = []
    directory = root / "research"
    index = (directory / "README.md").read_text()
    entries = re.findall(r"\]\(([^)]+\.md)\)\s*\|\s*(\d+)\s*\|", index)
    indexed = [name for name, _ in entries]
    topics = sorted(p.name for p in repository_files(root) if p.parent == directory and p.suffix == ".md" and p.name != "README.md")
    if sorted(indexed) != topics:
        errors.append("research/README.md: index must list every topic exactly once")
    total = 0
    for name, expected in entries:
        path = directory / name
        if not path.is_file():
            continue  # The link check reports this.
        text = path.read_text()
        if "| # | Title | Takeaway | Type | Year | Citations | DOI |" not in text:
            errors.append(f"research/{name}: missing research table header")
        count = len(re.findall(r"(?m)^\|\s*\d+\s*\|", text))
        total += count
        if count != int(expected):
            errors.append(f"research/{name}: {count} entries, index says {expected}")
    if f"Total: {total} paper entries across {len(topics)} topics" not in index:
        errors.append("research/README.md: total does not match the paper entries")
    return errors


def check_migration(root):
    errors = []
    manifest = json.loads((root / "provenance/migration.json").read_text())
    seen = set()
    for source in manifest["sources"]:
        for record in source["files"]:
            if "destination" not in record:
                if not record.get("excluded"):
                    errors.append(f"Missing migration decision: {record['source']}")
                continue
            dest = record["destination"]
            if dest in seen:
                errors.append(f"Duplicate migration destination: {dest}")
            seen.add(dest)
            path = (root / dest).resolve()
            if not path.is_relative_to(root.resolve()) or not path.is_file():
                errors.append(f"Missing migrated file: {dest}")
    # This source's license prohibits raw redistribution, including under a new name.
    restricted = next(
        record["source_sha256"]
        for source in manifest["sources"]
        for record in source["files"]
        if record["source"] == "data/operator-lessons.md"
    )
    import hashlib
    for path in repository_files(root):
        if path.suffix != ".md":
            continue
        if path.name == "operator-lessons.md" or hashlib.sha256(path.read_bytes()).hexdigest() == restricted:
            errors.append(f"Restricted source content must not be imported: {path.relative_to(root)}")
    return errors


def main():
    files = repository_files(ROOT)
    markdown = [path for path in files if path.suffix == ".md"]
    errors = check_links(ROOT, markdown) + check_research(ROOT) + check_migration(ROOT)
    for path in files:
        if path.suffix != ".py":
            continue
        try:
            ast.parse(path.read_text(), filename=str(path))
        except SyntaxError as exc:
            errors.append(str(exc))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(markdown)} Markdown files; local file links, research counts, migration coverage, restricted-file exclusion, and Python syntax")
    return 0


if __name__ == "__main__":
    sys.exit(main())
