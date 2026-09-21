#!/usr/bin/env python3
"""Check local file targets in LINK attributes of Freeplane maps."""
from __future__ import annotations
import argparse
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("map_file", type=Path)
    args = parser.parse_args()
    tree = ET.parse(args.map_file)
    missing: list[str] = []
    checked = 0
    for node in tree.getroot().iter("node"):
        link = node.get("LINK")
        if not link or "://" in link or link.startswith(("freeplane:", "#")):
            continue
        path_part = urllib.parse.unquote(link.split("#", 1)[0])
        if path_part.startswith("file:"):
            path_part = path_part[5:]
        target = (args.map_file.parent / path_part).resolve()
        checked += 1
        if not target.exists():
            missing.append(f"{node.get('TEXT', '')}: {target}")
    if missing:
        print("Missing local Freeplane link targets:", file=sys.stderr)
        print("\n".join(missing), file=sys.stderr)
        return 1
    print(f"Validated {checked} local link target(s): OK")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ET.ParseError) as exc:
        print(f"validate_freeplane_links: {exc}", file=sys.stderr)
        raise SystemExit(2)
