#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from needle.thread.render import render_article3_preview, render_preview_text


THREAD = Path("fixtures/thread/reg794-article3-thread-v0.1.json")
OUT = Path("artifacts/thread-preview")


def main() -> int:
    thread = json.loads(THREAD.read_text(encoding="utf-8"))
    preview = render_article3_preview(thread)

    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "reg794-article3-thread-v0.1.json"
    text_path = OUT / "reg794-article3-thread-v0.1.txt"

    json_path.write_text(
        json.dumps(preview, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    text_path.write_text(render_preview_text(preview), encoding="utf-8")

    print(json.dumps({
        "thread_id":preview["thread_id"],
        "source_mode":preview["source_mode"],
        "json":str(json_path),
        "text":str(text_path),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
