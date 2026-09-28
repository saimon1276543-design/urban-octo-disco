#!/usr/bin/env python3
"""Create a non-destructive portfolio migration preview."""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path


def collect_ids(data: object) -> set[str]:
    ids: set[str] = set()
    if isinstance(data, dict):
        for key, value in data.items():
            if key in {"id", "node_id", "goal_id", "portfolio_id"} and isinstance(value, str):
                ids.add(value)
            ids.update(collect_ids(value))
    elif isinstance(data, list):
        for value in data:
            ids.update(collect_ids(value))
    return ids


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("target", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = json.loads(args.source.read_text(encoding="utf-8"))
    target = json.loads(args.target.read_text(encoding="utf-8"))
    source_ids, target_ids = collect_ids(source), collect_ids(target)
    conflicts = []
    if source.get("portfolio_id") and target.get("portfolio_id") and source["portfolio_id"] != target["portfolio_id"]:
        conflicts.append("portfolio_id mismatch")
    if source.get("north_star") and target.get("north_star") and source["north_star"] != target["north_star"]:
        conflicts.append("north_star mismatch")
    preserved = sorted(source_ids & target_ids)
    affected = sorted(source_ids ^ target_ids)
    preview = {
        "schema_version": "1.0",
        "migration_id": f"preview:{source.get('revision', 'unknown')}->{target.get('revision', 'unknown')}",
        "source_version": str(source.get("schema_version", "unknown")),
        "target_version": str(target.get("schema_version", "unknown")),
        "status": "preview",
        "preserved_ids": preserved,
        "affected_paths": affected,
        "transformed_fields": [],
        "unresolved_links": [],
        "conflicts": conflicts,
        "validation": "preview only; no source or target mutation",
        "rollback_reference": str(args.source)
    }
    args.output.write_text(json.dumps(preview, indent=2) + "\n", encoding="utf-8")
    print(f"Migration preview written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
