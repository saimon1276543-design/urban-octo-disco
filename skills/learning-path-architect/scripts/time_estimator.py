#!/usr/bin/env python3
"""Estimate learning effort and calendar ranges without promising mastery dates."""
from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: time_estimator.py <time-budget.json>")
        return 1
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        units = data["units"]
        availability = data.get("availability") or {}
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"Time estimation failed: {exc}")
        return 1
    if not isinstance(units, list) or not units:
        print("Time estimation failed: units must be a non-empty array")
        return 1

    records: dict[str, dict] = {}
    for unit in units:
        try:
            unit_id = str(unit["unit_id"])
            low = float(unit["low_effort"])
            typical = float(unit["typical_effort"])
            high = float(unit["high_effort"])
            setup = float(unit.get("setup_effort", 0))
            feedback = float(unit.get("feedback_wait", 0))
            spacing = float(unit.get("spacing_calendar_units", 0))
            prerequisites = [str(value) for value in unit.get("prerequisites", [])]
        except (KeyError, TypeError, ValueError) as exc:
            print(f"Time estimation failed: invalid unit: {exc}")
            return 1
        if not (0 <= low <= typical <= high) or min(setup, feedback, spacing) < 0:
            print("Time estimation failed: require 0 <= low <= typical <= high and nonnegative overheads")
            return 1
        if unit_id in records:
            print(f"Time estimation failed: duplicate unit_id {unit_id}")
            return 1
        records[unit_id] = {
            "low": low + setup,
            "typical": typical + setup,
            "high": high + setup,
            "feedback": feedback,
            "spacing": spacing,
            "prerequisites": prerequisites,
            "critical": bool(unit.get("critical_path", False)),
            "actual": unit.get("actual_effort"),
        }

    missing = sorted({dep for item in records.values() for dep in item["prerequisites"] if dep not in records})
    if missing:
        print(f"Time estimation failed: unknown prerequisites: {', '.join(missing)}")
        return 1

    order: list[str] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visited:
            return
        if node in visiting:
            raise ValueError("dependency cycle detected")
        visiting.add(node)
        for dep in records[node]["prerequisites"]:
            visit(dep)
        visiting.remove(node)
        visited.add(node)
        order.append(node)

    try:
        for node in records:
            visit(node)
    except ValueError as exc:
        print(f"Time estimation failed: {exc}")
        return 1

    total_low = sum(records[node]["low"] for node in order)
    total_typical = sum(records[node]["typical"] for node in order)
    total_high = sum(records[node]["high"] for node in order)
    expected = (total_low + 4 * total_typical + total_high) / 6

    # Dependency-aware effort lower bound: longest typical path including feedback waits.
    path_end: dict[str, float] = {}
    for node in order:
        start = max((path_end[dep] for dep in records[node]["prerequisites"]), default=0.0)
        path_end[node] = start + records[node]["typical"] + records[node]["feedback"]
    critical_path_typical = max(path_end.values(), default=0.0)

    window = float(availability.get("window_units_per_cycle", 0) or 0)
    reliability = float(availability.get("reliability", 1) or 1)
    reserve = float(availability.get("recovery_reserve_units", 0) or 0)
    usable_window = max(0.0, window * reliability - reserve)
    session_min = float(availability.get("session_min_units", 0) or 0)
    session_max = float(availability.get("session_max_units", 0) or 0)
    sessions_typical = None if session_max <= 0 else round(expected / session_max, 2)
    cycles_typical = None if usable_window <= 0 else round(expected / usable_window, 2)
    calendar_lower_bound = None if usable_window <= 0 else round(critical_path_typical / usable_window, 2)

    actuals = [float(item["actual"]) for item in records.values() if item["actual"] is not None]
    observed_ratio = None if not actuals or total_typical <= 0 else round(sum(actuals) / total_typical, 4)
    result = {
        "unit_count": len(order),
        "estimate_basis": data.get("estimate_basis", "mixed"),
        "effort_range": {"low": round(total_low, 2), "typical": round(total_typical, 2), "high": round(total_high, 2), "weighted_expected": round(expected, 2)},
        "critical_path_typical": round(critical_path_typical, 2),
        "availability": {"window_units_per_cycle": window, "reliability": reliability, "recovery_reserve_units": reserve, "usable_window_units": round(usable_window, 2), "session_min_units": session_min, "session_max_units": session_max},
        "typical_sessions": sessions_typical,
        "typical_cycles": cycles_typical,
        "calendar_lower_bound_cycles": calendar_lower_bound,
        "observed_effort_to_plan_ratio": observed_ratio,
        "dominant_uncertainty": data.get("dominant_uncertainty"),
        "warning": "Ranges describe planned effort and dependency/availability constraints, not guaranteed mastery or a fixed completion date."
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
