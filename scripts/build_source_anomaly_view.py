#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

from needle.analytics.source_anomaly import (
    build_source_anomaly_view,
    render_source_anomaly_text,
)


ROOT=Path(".")
COMPOSITION=ROOT / "fixtures/analytics/source-anomaly-first-cohort-v0.1.json"


def main() -> int:
    spec=json.loads(COMPOSITION.read_text(encoding="utf-8"))
    view=build_source_anomaly_view(spec,root=ROOT)

    out=ROOT / "artifacts/source-anomaly"
    out.mkdir(parents=True,exist_ok=True)
    json_path=out / "source-anomaly-first-cohort-v0.1.json"
    text_path=out / "source-anomaly-first-cohort-v0.1.txt"

    json_path.write_text(
        json.dumps(view,indent=2,ensure_ascii=False)+"\n",
        encoding="utf-8",
    )
    text_path.write_text(
        render_source_anomaly_text(view),
        encoding="utf-8",
    )
    print(text_path.read_text(encoding="utf-8"))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
