#!/usr/bin/env python3
"""Search Huang Zheng skill references with compact snippets."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REFS = ROOT / "references"


def iter_reference_files() -> list[Path]:
    files: list[Path] = []
    for pattern in ("*.md", "*.json"):
        files.extend(sorted(REFS.glob(pattern)))
    return files


def snippet(lines: list[str], idx: int, radius: int) -> str:
    start = max(0, idx - radius)
    end = min(len(lines), idx + radius + 1)
    return "\n".join(
        f"{line_no + 1}: {lines[line_no].rstrip()}" for line_no in range(start, end)
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Search huang-zheng-company-thinking references."
    )
    parser.add_argument("terms", nargs="+", help="Search terms. Any term may match.")
    parser.add_argument("--radius", type=int, default=2, help="Context lines around hit.")
    parser.add_argument("--limit", type=int, default=40, help="Maximum hits to print.")
    args = parser.parse_args()

    terms = [term.casefold() for term in args.terms if term.strip()]
    if not terms:
        parser.error("provide at least one non-empty term")

    hit_count = 0
    for path in iter_reference_files():
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        for idx, line in enumerate(lines):
            folded = line.casefold()
            if not any(term in folded for term in terms):
                continue
            rel = path.relative_to(ROOT)
            print(f"\n## {rel}:{idx + 1}")
            print(snippet(lines, idx, args.radius))
            hit_count += 1
            if hit_count >= args.limit:
                return 0

    if hit_count == 0:
        print("No matches.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
