#!/usr/bin/env python3
"""Fast repository-integrity checks for Morrow // Needle.

This protects repository hygiene only. Passing it says nothing about legal or
analytical correctness.
"""
from __future__ import annotations

from pathlib import Path
import subprocess
import sys


REQUIRED = {
    "README.md",
    "BACKLOG.md",
    "docs/project-charter.md",
    "docs/assumptions.md",
    "docs/project-health.md",
    "docs/automation/hourly-worker.md",
}

FORBIDDEN_BASENAMES = {
    ".env",
    ".env.local",
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

TEXT_SUFFIXES = {
    ".md", ".py", ".json", ".yml", ".yaml", ".toml", ".txt", ".html",
    ".css", ".js", ".ts", ".tsx", ".xml", ".csv",
}

MERGE_MARKERS = ("<<<<<<< ", "=======", ">>>>>>> ")


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
        if path.name in FORBIDDEN_BASENAMES:
            errors.append(f"forbidden tracked file: {path}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden tracked file type: {path}")
        if any(part in FORBIDDEN_PARTS for part in path.parts):
            errors.append(f"generated junk is tracked: {path}")

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
