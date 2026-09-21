#!/usr/bin/env python3
"""Model relative learning capacity without promising completion dates.

Required input: capacity_units, parallel_limit, branches[].
Optional capacity fields: reliability, learning_fraction, fixed_overhead_units,
maintenance_units, recovery_reserve_units, observed_throughput_ratio.
Optional branch fields: cognitive_load, minimum_continuity_units, reinforces,
competes_with, observed_effort_units.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def number(data: dict, key: str, default: float) -> float:
    value = data.get(key, default)
    return float(value)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: capacity_model.py <capacity.json>")
        return 1
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        nominal = number(data, "capacity_units", 0)
        parallel_limit = int(data["parallel_limit"])
        branches = data["branches"]
        reliability = number(data, "reliability", 1.0)
        learning_fraction = number(data, "learning_fraction", 1.0)
        fixed_overhead = number(data, "fixed_overhead_units", 0.0)
        maintenance = number(data, "maintenance_units", 0.0)
        recovery = number(data, "recovery_reserve_units", 0.0)
        observed_ratio = data.get("observed_throughput_ratio")
        observed_ratio = None if observed_ratio is None else number(data, "observed_throughput_ratio", 1.0)
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"Capacity modeling failed: {exc}")
        return 1

    if nominal <= 0 or parallel_limit < 1 or not isinstance(branches, list):
        print("Capacity modeling failed: capacity_units > 0, parallel_limit >= 1, and branches[] are required")
        return 1
    if not 0 < reliability <= 1 or not 0 < learning_fraction <= 1:
        print("Capacity modeling failed: reliability and learning_fraction must be between 0 and 1")
        return 1
    if min(fixed_overhead, maintenance, recovery) < 0:
        print("Capacity modeling failed: overhead, maintenance, and recovery values must be nonnegative")
        return 1

    usable = nominal * reliability * learning_fraction - fixed_overhead - maintenance - recovery
    if observed_ratio is not None:
        if observed_ratio <= 0:
            print("Capacity modeling failed: observed_throughput_ratio must be positive")
            return 1
        usable *= min(observed_ratio, 1.0)

    eligible: list[dict] = []
    for branch in branches:
        try:
            branch_id = str(branch["id"])
            effort = number(branch, "effort_units", 0)
            switching = number(branch, "switching_cost_units", 0)
            cognitive = number(branch, "cognitive_load", 1)
            continuity = number(branch, "minimum_continuity_units", 0)
            ready = bool(branch.get("prerequisites_met", False))
        except (KeyError, TypeError, ValueError):
            print("Capacity modeling failed: every branch needs id and numeric effort_units")
            return 1
        if effort <= 0 or switching < 0 or cognitive <= 0 or continuity < 0:
            print("Capacity modeling failed: effort > 0, switching/continuity >= 0, cognitive_load > 0")
            return 1
        if ready:
            eligible.append({
                "id": branch_id,
                "effort": effort,
                "switching": switching,
                "cognitive": cognitive,
                "continuity": continuity,
                "observed_effort": branch.get("observed_effort_units"),
            })

    # Favor lower total load while retaining deterministic ID ordering.
    eligible.sort(key=lambda item: (item["effort"] + item["switching"], item["id"]))
    selected = eligible[:parallel_limit]
    load = sum(item["effort"] + item["switching"] for item in selected)
    cognitive_load = sum(item["cognitive"] for item in selected)
    continuity_gap = sum(max(0.0, item["continuity"] - usable) for item in selected)
    ratio = load / usable if usable > 0 else float("inf")

    if usable <= 0:
        recommendation = "no usable learning capacity remains after reliability, overhead, maintenance, and recovery reserve"
    elif ratio <= 1 and continuity_gap == 0:
        recommendation = "selected branches fit relative usable capacity; verify sustainability with observed progress"
    elif len(selected) > 1:
        recommendation = "reduce concurrency or defer the highest-switching/highest-load branch; capacity or continuity is insufficient"
    else:
        recommendation = "reduce branch scope, increase reliable capacity, or protect recovery reserve; one branch exceeds usable capacity"

    result = {
        "eligible_branches": [item["id"] for item in eligible],
        "selected_branches": [item["id"] for item in selected],
        "nominal_capacity_units": nominal,
        "usable_capacity_units": round(usable, 4),
        "capacity_factors": {
            "reliability": reliability,
            "learning_fraction": learning_fraction,
            "fixed_overhead_units": fixed_overhead,
            "maintenance_units": maintenance,
            "recovery_reserve_units": recovery,
            "observed_throughput_ratio": observed_ratio,
        },
        "relative_load_units": round(load, 4),
        "load_ratio": None if usable <= 0 else round(ratio, 4),
        "cognitive_load": round(cognitive_load, 4),
        "continuity_gap_units": round(continuity_gap, 4),
        "recommendation": recommendation,
        "warning": "This is a relative load and sustainability check, not a duration, mastery, or motivation prediction."
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
