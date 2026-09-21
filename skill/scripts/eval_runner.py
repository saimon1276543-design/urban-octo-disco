#!/usr/bin/env python3
"""Package-level evaluation harness for Learning Path Architect.

This script does not generate or judge model outputs. It verifies that the
bundled evaluation resources exist, counts evaluation cases, and writes a
report scaffold so a human or model can record actual case scores honestly.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re

REQUIRED = [
    "SKILL.md",
    "references/evaluation-cases.md",
    "references/evaluation-scorecard.md",
    "templates/evaluation-report.md",
    "templates/learning-map.md",
    "templates/roadmap.md",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", type=Path)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    root = args.skill_dir.resolve()
    missing = [item for item in REQUIRED if not (root / item).is_file()]
    cases_path = root / "references/evaluation-cases.md"
    case_count = 0
    if cases_path.is_file():
        case_count = len(re.findall(r"^## Case \d+:", cases_path.read_text(encoding="utf-8"), re.MULTILINE))

    lines = [
        "# Learning Path Architect Evaluation Report",
        "",
        "## Package integrity",
        "",
        f"- Skill directory: `{root}`",
        f"- Required resources present: {'yes' if not missing else 'no'}",
        f"- Missing resources: {', '.join(missing) if missing else 'none'}",
        f"- Evaluation cases discovered: {case_count}",
        "",
        "## Case results",
        "",
        "| Case | Total score / 84 | Blocking zero? | Lowest dimension | Result |",
        "|---|---:|---|---|---|",
    ]
    for index in range(1, case_count + 1):
        lines.append(f"| {index} | {{score}} | {{yes/no}} | {{dimension}} | {{pass/revise}} |")
    lines += [
        "",
        "> This harness checks package integrity and creates a reporting scaffold; it does not claim to have evaluated model outputs.",
        "",
    ]
    report = "\n".join(lines)
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report)
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
