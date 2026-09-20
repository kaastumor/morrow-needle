#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from needle.analytics.half_life import (
    build_half_life_view,
    render_half_life_text,
)


ROOT=Path(".")
COMPOSITION=ROOT / "fixtures/analytics/eprivacy-half-life-v0.1.json"


def main() -> int:
    spec=json.loads(COMPOSITION.read_text(encoding="utf-8"))
    view=build_half_life_view(spec,root=ROOT)

    out=ROOT / "artifacts/half-life"
    out.mkdir(parents=True,exist_ok=True)
    json_path=out / "eprivacy-half-life-v0.1.json"
    text_path=out / "eprivacy-half-life-v0.1.txt"

    json_path.write_text(
        json.dumps(view,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    text_path.write_text(render_half_life_text(view),encoding="utf-8")
    print(text_path.read_text(encoding="utf-8"))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
