#!/usr/bin/env python3
"""Summarize learning observations for a capacity/replanning review."""
from __future__ import annotations

import json
import statistics
import sys
from pathlib import Path


def ratio(numerator: float, denominator: float) -> float | None:
    return None if denominator <= 0 else numerator / denominator


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: recalibration_report.py <observation-tracker.json>")
        return 1
    try:
        data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        cycles = data["cycles"]
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"Recalibration failed: {exc}")
        return 1
    if not isinstance(cycles, list) or not cycles:
        print("Recalibration failed: cycles must be a non-empty array")
        return 1

    effort_ratios: list[float] = []
    completion_ratios: list[float] = []
    interruption_rates: list[float] = []
    recovery: list[float] = []
    blocker_flags = 0
    branch_ratios: list[float] = []
    switching: list[float] = []
    evidence_scores: list[float] = []

    for cycle in cycles:
        try:
            planned_effort = float(cycle["planned_effort_units"])
            actual_effort = float(cycle["actual_effort_units"])
            planned_units = float(cycle["planned_units"])
            completed_units = float(cycle["completed_units"])
            sessions_planned = int(cycle["sessions_planned"])
            interruptions = int(cycle["interruptions"])
            branches_planned = int(cycle["branches_planned"])
            branches_sustained = int(cycle["branches_sustained"])
        except (KeyError, TypeError, ValueError) as exc:
            print(f"Recalibration failed: invalid cycle: {exc}")
            return 1
        if min(planned_effort, actual_effort, planned_units, completed_units, sessions_planned, interruptions, branches_planned, branches_sustained) < 0:
            print("Recalibration failed: cycle values must be nonnegative")
            return 1
        if planned_effort > 0:
            effort_ratios.append(actual_effort / planned_effort)
        if planned_units > 0:
            completion_ratios.append(completed_units / planned_units)
        if sessions_planned > 0:
            interruption_rates.append(interruptions / sessions_planned)
        recovery.append(float(cycle.get("recovery_units", 0)))
        blocker_flags += int(bool(cycle.get("repeated_blocker", False)))
        if branches_planned > 0:
            branch_ratios.append(branches_sustained / branches_planned)
        switching.append(float(cycle.get("switching_cost_units", 0)))
        for field in ("retention_score", "transfer_score"):
            value = cycle.get(field)
            if value is not None:
                evidence_scores.append(float(value))

    median_effort = statistics.median(effort_ratios) if effort_ratios else None
    median_completion = statistics.median(completion_ratios) if completion_ratios else None
    median_interruptions = statistics.median(interruption_rates) if interruption_rates else None
    median_branches = statistics.median(branch_ratios) if branch_ratios else None
    median_evidence = statistics.median(evidence_scores) if evidence_scores else None

    flags: list[str] = []
    if median_effort is not None and median_effort > 1.25:
        flags.append("actual effort is consistently above plan: revisit decomposition or capacity")
    if median_completion is not None and median_completion < 0.75:
        flags.append("completion ratio is low: narrow scope, reduce concurrency, or remediate a blocker")
    if blocker_flags >= max(2, len(cycles) // 2):
        flags.append("repeated blocker detected: identify and remediate the smallest prerequisite")
    if median_interruptions is not None and median_interruptions > 0.25:
        flags.append("interruptions are frequent: protect reserve and use a more reliable availability band")
    if median_branches is not None and median_branches < 0.75:
        flags.append("planned concurrency is not being sustained: reduce active branches")
    if median_evidence is not None and median_evidence < 0.6:
        flags.append("retention/transfer evidence is weak: do not expand capacity based on speed")
    if not flags:
        flags.append("no dominant capacity failure detected; change only one dimension at the next expansion")

    if flags and any("blocker" in flag or "scope" in flag or "concurrency" in flag for flag in flags):
        recommendation = "remediate or narrow before expanding"
    elif median_effort is not None and median_effort < 0.85 and (median_evidence is None or median_evidence >= 0.75):
        recommendation = "capacity may be underestimated; expand one dimension only after another confirming cycle"
    else:
        recommendation = "continue with calibrated assumptions and review at the next trigger"

    result = {
        "cycles_observed": len(cycles),
        "median_actual_to_planned_effort": None if median_effort is None else round(median_effort, 4),
        "median_completion_ratio": None if median_completion is None else round(median_completion, 4),
        "median_interruptions_per_session": None if median_interruptions is None else round(median_interruptions, 4),
        "median_recovery_units": round(statistics.median(recovery), 4),
        "repeated_blocker_cycles": blocker_flags,
        "median_branches_sustained_ratio": None if median_branches is None else round(median_branches, 4),
        "median_switching_cost_units": round(statistics.median(switching), 4),
        "median_retention_transfer_score": None if median_evidence is None else round(median_evidence, 4),
        "flags": flags,
        "recommendation": recommendation,
        "review_sequence": ["collect", "check evidence", "calibrate", "recompute frontier", "decide", "explain", "commit checkpoint", "expose next action"]
    }
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
