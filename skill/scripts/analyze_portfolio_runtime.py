#!/usr/bin/env python3
"""Derive conservative portfolio metrics, uncertainty signals, and repair proposals."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def as_list(value):
    return value if isinstance(value, list) else []


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("runtime", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.runtime.read_text(encoding="utf-8"))
    entities = data.get("entities", {}) if isinstance(data, dict) else {}
    relationships = as_list(data.get("relationships")) if isinstance(data, dict) else []
    evidence = as_list(data.get("evidence")) if isinstance(data, dict) else []
    goals = as_list(entities.get("goals"))
    capabilities = as_list(entities.get("capabilities"))
    active = [item for item in capabilities if isinstance(item, dict) and item.get("status") in {"active", "required", "blocked"}]
    evidenced_ids = {ref for item in evidence if isinstance(item, dict) for ref in as_list(item.get("node_ids"))}
    active_ids = {item.get("id") or item.get("node_id") for item in active}
    active_ids.discard(None)
    evidence_coverage = None if not active_ids else round(len(active_ids & evidenced_ids) / len(active_ids), 3)
    hard_edges = [edge for edge in relationships if isinstance(edge, dict) and edge.get("type") in {"hard_prerequisite", "required"}]
    incoming = {edge.get("to") for edge in hard_edges if edge.get("to")}
    bottlenecks = sorted({edge.get("from") for edge in hard_edges if edge.get("from")}, key=lambda item: item)
    uncertainty = []
    for item in list(entities.get("assumptions", [])) + list(entities.get("uncertainties", [])):
        if isinstance(item, dict) and item.get("status") not in {"confirmed", "verified"}:
            uncertainty.append({"id": item.get("id", "unknown"), "affected_ids": as_list(item.get("affected_ids")), "reason": item.get("reason") or item.get("assumption", "unresolved"), "mitigation": item.get("validation_method") or "targeted observation"})
    repairs = []
    known = {item.get("id") or item.get("node_id") for group in entities.values() if isinstance(group, list) for item in group if isinstance(item, dict)}
    for index, edge in enumerate(relationships):
        if not isinstance(edge, dict):
            continue
        missing = [key for key in ("from", "to") if edge.get(key) not in known]
        if missing:
            repairs.append({"issue_id": f"repair.dangling-edge-{index}", "affected_ids": [edge.get("from"), edge.get("to")], "proposed_change": "resolve or quarantine dangling relationship", "reversibility": "high", "approval_required": True})
    for goal in goals:
        if isinstance(goal, dict) and goal.get("id") and goal.get("id") not in {item.get("goal_id") for item in capabilities if isinstance(item, dict)}:
            repairs.append({"issue_id": f"repair.goal-closure-{goal['id']}", "affected_ids": [goal["id"]], "proposed_change": "attach capability and evidence closure route", "reversibility": "high", "approval_required": True})
    output = {
        "schema_version": "1.0",
        "portfolio_id": data.get("portfolio_id"),
        "revision": data.get("revision"),
        "metrics": {
            "capacity_utilization": data.get("derived_metrics", {}).get("capacity_utilization", "unknown"),
            "maintenance_load": data.get("derived_metrics", {}).get("maintenance_load", "unknown"),
            "dependency_bottleneck_count": len(set(bottlenecks)),
            "evidence_coverage": evidence_coverage if evidence_coverage is not None else "unknown",
            "active_frontier_readiness": data.get("derived_metrics", {}).get("active_frontier_readiness", "unknown"),
            "uncertainty_concentration": "high" if len(uncertainty) >= 5 else "medium" if uncertainty else "low"
        },
        "uncertainty": uncertainty,
        "repair_proposals": repairs,
        "generated_at": "runtime-derived"
    }
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(f"Runtime analysis written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
