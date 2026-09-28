#!/usr/bin/env python3
"""Build a deterministic release manifest for a Learning Path Architect package."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

EXCLUDED_PARTS = {"__pycache__"}
EXCLUDED_SUFFIXES = {".pyc"}
MARKER_FILES = {
    "SKILL.md",
    "README.md",
    "references/release-and-sync.md",
    "references/portfolio-runtime.md",
    "references/domain-safety-profiles.md",
    "scripts/analyze_portfolio_runtime.py",
    "scripts/migrate_portfolio.py",
    "scripts/benchmark_outputs.py",
    "templates/portfolio-runtime.schema.json",
    "templates/release-manifest.schema.json",
    "scripts/build_release_manifest.py",
}


def files_for(root: Path) -> list[Path]:
    paths: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        if path.suffix in EXCLUDED_SUFFIXES:
            continue
        paths.append(path)
    return sorted(paths, key=lambda item: item.relative_to(root).as_posix())


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalized_digest(root: Path, paths: list[Path]) -> str:
    digest = hashlib.sha256()
    for path in paths:
        relative = path.relative_to(root).as_posix()
        data = path.read_bytes()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(data)
        digest.update(b"\0")
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill_dir", type=Path)
    parser.add_argument("--release-id", default=None)
    parser.add_argument("--package-sha256", default=None)
    parser.add_argument("--zip-path", default=None)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    root = args.skill_dir.resolve()
    paths = files_for(root)
    relative_paths = {path.relative_to(root).as_posix(): path for path in paths}
    skill_path = root / "SKILL.md"
    manifest_path = root / "templates/release-manifest.schema.json"
    if not skill_path.is_file() or not manifest_path.is_file():
        raise SystemExit("skill_dir must contain SKILL.md and templates/release-manifest.schema.json")

    release_id = args.release_id or datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    markers = [item for item in sorted(MARKER_FILES) if item in relative_paths]
    manifest = {
        "schema_version": "1.0",
        "skill_name": "learning-path-architect",
        "release_id": release_id,
        "artifact": {
            "file_count": len(paths),
            "total_bytes": sum(path.stat().st_size for path in paths),
            "package_sha256": args.package_sha256 or normalized_digest(root, paths),
            "zip_path": args.zip_path,
        },
        "workspace": {
            "skill_sha256": sha256_bytes(skill_path.read_bytes()),
            "manifest_sha256": sha256_bytes(manifest_path.read_bytes()),
            "capability_markers": markers,
        },
        "validation": {
            "status": "unverified",
            "checked_at": None,
            "checks": [],
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Release manifest written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
