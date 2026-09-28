#!/usr/bin/env python3
"""Check that all JSON files in a skill package parse successfully."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors: list[str] = []
    files = sorted(root.rglob("*.json"))
    for path in files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(root)}: {exc}")
    if errors:
        print("JSON syntax check failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"JSON syntax check passed: {len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
