#!/usr/bin/env python3
"""Verify the sealed external artifacts for Issue #87.

The plaintext packets intentionally remain outside Git until independent relay
execution completes. This script verifies that later-supplied files are exactly
the bytes committed by hash before execution.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys


MANIFEST = Path(
    "fixtures/value-gates/issue87-sealed-manifest-v0.1.json"
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "directory",
        type=Path,
        help="Directory containing the three sealed Issue #87 JSON files.",
    )
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    errors: list[str] = []

    for item in manifest["sealed_artifacts"]:
        path = args.directory / item["filename"]
        if not path.is_file():
            errors.append(f"missing: {path}")
            continue

        actual = sha256(path)
        expected = item["sha256"]
        if actual != expected:
            errors.append(
                f"hash mismatch for {item['filename']}: "
                f"expected {expected}, got {actual}"
            )
        else:
            print(f"OK {item['filename']} {actual}")

    if errors:
        print("Issue #87 sealed-artifact verification failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Issue #87 sealed artifacts match their pre-execution commitments.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
