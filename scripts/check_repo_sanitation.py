#!/usr/bin/env python3
"""Fast repository-integrity checks for Morrow // Needle.

This protects repository hygiene only. Passing it says nothing about legal or
analytical correctness.
"""
from __future__ import annotations

from pathlib import Path
import re
import subprocess
import sys


REQUIRED = {
    ".gitignore",
    "README.md",
    "BACKLOG.md",
    "docs/project-charter.md",
    "docs/assumptions.md",
    "docs/project-health.md",
    "docs/automation/hourly-worker.md",
}

FORBIDDEN_BASENAMES = {
    ".DS_Store",
}

FORBIDDEN_SUFFIXES = {
    ".pem",
    ".pfx",
    ".p12",
    ".key",
    ".pyc",
}

FORBIDDEN_PARTS = {
    "__pycache__",
    ".pytest_cache",
}

FORBIDDEN_TOP_LEVEL = {
    "artifacts",
}

TEXT_SUFFIXES = {
    ".md", ".py", ".json", ".yml", ".yaml", ".toml", ".txt", ".html",
    ".css", ".js", ".ts", ".tsx", ".xml", ".csv",
}

MERGE_MARKERS = (
    "<" * 7 + " ",
    "=" * 7,
    ">" * 7 + " ",
)

SECRET_MARKERS = (
    "-----BEGIN " + "PRIVATE KEY-----",
    "-----BEGIN " + "RSA PRIVATE KEY-----",
    "-----BEGIN " + "OPENSSH PRIVATE KEY-----",
    "github_" + "pat_",
)

LOCAL_PATH_PATTERNS = (
    re.compile(r"(?i)\b[A-Z]:\\Users\\[^\\\r\n]+"),
    re.compile("/" + "Users" + r"/[^/\s]+/"),
    re.compile("/" + "home" + r"/[^/\s]+/"),
)

MAX_TRACKED_BYTES = 1_000_000

# These four files are a frozen historical snapshot of the old scheduled
# operational pilot. Issue #84 stopped their automated growth. The state file
# still contains unique hash-verified Source Observations, so removal requires
# an explicit provenance migration rather than a sanitation shortcut.
LARGE_FILE_ALLOWLIST = {
    "data/operational-pilot-state-v0.1.json",
    "data/operational-pilot-latest-results.json",
    "data/operational-pilot-latest-cards.json",
    "data/operational-pilot-last-report.json",
}


def tracked_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "ls-files", "-z"],
    )
    return [
        Path(raw.decode("utf-8"))
        for raw in output.split(b"\0")
        if raw
    ]


def main() -> int:
    errors: list[str] = []
    paths = tracked_files()
    tracked = {path.as_posix() for path in paths}

    for required in sorted(REQUIRED):
        if required not in tracked:
            errors.append(f"missing required project structure: {required}")

    for path in paths:
        posix = path.as_posix()

        if path.name == ".env" or path.name.startswith(".env."):
            if path.name != ".env.example":
                errors.append(f"forbidden tracked environment file: {path}")
        if path.name in FORBIDDEN_BASENAMES:
            errors.append(f"forbidden tracked file: {path}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden tracked file type: {path}")
        if any(part in FORBIDDEN_PARTS for part in path.parts):
            errors.append(f"generated junk is tracked: {path}")
        if path.parts and path.parts[0] in FORBIDDEN_TOP_LEVEL:
            errors.append(f"generated artifact directory is tracked: {path}")

        size = path.stat().st_size
        if size > MAX_TRACKED_BYTES and posix not in LARGE_FILE_ALLOWLIST:
            errors.append(
                f"tracked file exceeds {MAX_TRACKED_BYTES} bytes without "
                f"explicit evidence allowlist: {path} ({size} bytes)"
            )

        if path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"tracked text is not valid UTF-8: {path}")
            continue

        for marker in MERGE_MARKERS:
            if marker in text:
                errors.append(f"merge marker {marker!r} in {path}")

        for marker in SECRET_MARKERS:
            if marker in text:
                errors.append(f"possible embedded secret marker in {path}")

        for pattern in LOCAL_PATH_PATTERNS:
            if pattern.search(text):
                errors.append(f"possible local user path in tracked text: {path}")

    if errors:
        print("Repository sanitation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Repository sanitation passed: {len(paths)} tracked files; "
        f"{len(REQUIRED)} required structures present."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
