from __future__ import annotations

import re
from typing import Any

from needle.ast.historical_html import extract_blocks


TOKEN_RE = re.compile(r"[\w]+", re.UNICODE)


def tokens(text: str) -> list[str]:
    return TOKEN_RE.findall(text.casefold())


def shingles(token_list: list[str], size: int = 7) -> set[tuple[str, ...]]:
    if size <= 0:
        raise ValueError("shingle size must be positive")
    if len(token_list) < size:
        return set()
    return {
        tuple(token_list[i : i + size])
        for i in range(len(token_list) - size + 1)
    }


def _coverage(source: set[tuple[str, ...]], target: set[tuple[str, ...]]) -> float | None:
    if not source:
        return None
    return len(source & target) / len(source)


def audit_text_witness(
    primary_ast: dict[str, Any],
    witness_html: bytes,
    *,
    shingle_size: int = 7,
    excess_block_threshold: float = 0.20,
    min_block_tokens: int = 20,
) -> dict[str, Any]:
    """Compare a primary structured AST to an official HTML/XHTML text witness.

    This is a completeness diagnostic, not a legal-text merge operation.
    """
    primary_text = " ".join(
        segment["text_compare"]
        for segment in primary_ast.get("segments", [])
        if segment.get("text_compare")
    )
    witness_blocks = extract_blocks(witness_html)
    witness_text = " ".join(text for _, text in witness_blocks)

    primary_tokens = tokens(primary_text)
    witness_tokens = tokens(witness_text)
    primary_shingles = shingles(primary_tokens, shingle_size)
    witness_shingles = shingles(witness_tokens, shingle_size)

    excess_blocks = []
    for tag, text in witness_blocks:
        block_tokens = tokens(text)
        if len(block_tokens) < min_block_tokens:
            continue
        block_shingles = shingles(block_tokens, shingle_size)
        block_coverage = _coverage(block_shingles, primary_shingles)
        if block_coverage is not None and block_coverage < excess_block_threshold:
            excess_blocks.append(
                {
                    "tag": tag,
                    "token_count": len(block_tokens),
                    "primary_shingle_coverage": round(block_coverage, 6),
                    "text_prefix": text[:240],
                }
            )

    excess_blocks.sort(
        key=lambda item: (item["primary_shingle_coverage"], -item["token_count"])
    )

    return {
        "audit_version": "0.1",
        "method": f"{shingle_size}-token-shingle-set",
        "primary": {
            "token_count": len(primary_tokens),
            "shingle_count": len(primary_shingles),
        },
        "witness": {
            "block_count": len(witness_blocks),
            "token_count": len(witness_tokens),
            "shingle_count": len(witness_shingles),
        },
        "coverage": {
            "primary_shingles_found_in_witness": (
                None
                if _coverage(primary_shingles, witness_shingles) is None
                else round(_coverage(primary_shingles, witness_shingles), 6)
            ),
            "witness_shingles_found_in_primary": (
                None
                if _coverage(witness_shingles, primary_shingles) is None
                else round(_coverage(witness_shingles, primary_shingles), 6)
            ),
        },
        "witness_excess_block_count": len(excess_blocks),
        "witness_excess_blocks_sample": excess_blocks[:30],
        "interpretation_guardrail": (
            "Coverage differences indicate representation/text-extraction divergence. "
            "They do not by themselves prove missing legal content or authorize cross-source merging."
        ),
    }
