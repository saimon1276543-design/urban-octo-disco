#!/usr/bin/env python3
"""Validate Learning Path Architect package hygiene and resource references."""
from __future__ import annotations

import re
import sys
from pathlib import Path


REFERENCE_PATTERN = re.compile(r"`((?:references|templates|scripts)/[^`]+)`")
LINK_PATTERN = re.compile(r"\]\((?:(?:\.\/)?)(references|templates|scripts)/([^)#]+)")


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1])
    skill = root / "SKILL.md"
    errors: list[str] = []

    if not skill.exists():
        errors.append("Missing SKILL.md")
    else:
        lines = skill.read_text(encoding="utf-8").splitlines()
        if len(lines) >= 500:
            errors.append(f"SKILL.md has {len(lines)} lines; keep it below 500")
        frontmatter = "\n".join(lines[: min(len(lines), 12)])
        if not re.search(r"^name:\s*\S+", frontmatter, re.MULTILINE):
            errors.append("SKILL.md frontmatter is missing name")
        if not re.search(r"^description:\s*.+", frontmatter, re.MULTILINE):
            errors.append("SKILL.md frontmatter is missing description")

    if not (root / "README.md").is_file():
        errors.append("Missing retained README.md")

    markdown_files = sorted(root.rglob("*.md"))
    for markdown in markdown_files:
        text = markdown.read_text(encoding="utf-8")
        for reference in REFERENCE_PATTERN.findall(text):
            if not (root / reference).exists():
                errors.append(
                    f"Missing referenced resource in {markdown.relative_to(root)}: {reference}"
                )
        for directory, filename in LINK_PATTERN.findall(text):
            reference = f"{directory}/{filename}"
            if not (root / reference).exists():
                errors.append(
                    f"Missing linked resource in {markdown.relative_to(root)}: {reference}"
                )

    for forbidden in ("CHANGELOG.md",):
        if (root / forbidden).exists():
            errors.append(f"Forbidden auxiliary file at package root: {forbidden}")

    for path in root.rglob("*"):
        if path.is_dir() and path.name == "__pycache__":
            errors.append(f"Generated cache directory present: {path.relative_to(root)}")
        if path.is_file() and path.name.startswith("latest-"):
            errors.append(f"Generated evaluation artifact present: {path.relative_to(root)}")

    if errors:
        print("Package lint failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1

    print(f"Package lint passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
