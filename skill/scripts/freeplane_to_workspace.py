#!/usr/bin/env python3
"""Import the core hierarchy, IDs, notes, and links from a Freeplane .mm map."""
from __future__ import annotations
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def note_text(node: ET.Element) -> str | None:
    rich = node.find("richcontent[@TYPE='NOTE']")
    if rich is None:
        return None
    return " ".join("".join(rich.itertext()).split()) or None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_mm", type=Path)
    parser.add_argument("output_json", type=Path)
    args = parser.parse_args()
    tree = ET.parse(args.input_mm)
    root = tree.getroot().find("node")
    if root is None:
        raise ValueError("Map has no root node")
    used: set[str] = set()
    nodes: list[dict] = []

    def stable_id(element: ET.Element, path: str) -> str:
        value = element.get("ID") or f"imported-{path}"
        value = re.sub(r"[^A-Za-z0-9_.:-]", "-", value)
        candidate = value
        counter = 2
        while candidate in used:
            candidate = f"{value}-{counter}"
            counter += 1
        used.add(candidate)
        return candidate

    def visit(element: ET.Element, parent_id: str | None, path: str) -> None:
        node_id = stable_id(element, path)
        item = {"id": node_id, "title": element.get("TEXT", ""), "parent_id": parent_id, "order": len([n for n in nodes if n.get("parent_id") == parent_id])}
        if element.get("LINK"):
            item["link"] = element.get("LINK")
        text = note_text(element)
        if text:
            item["note"] = text
        nodes.append(item)
        for index, child in enumerate(element.findall("node"), start=1):
            visit(child, node_id, f"{path}.{index}")

    visit(root, None, "1")
    result = {"map_title": root.get("TEXT", ""), "nodes": nodes}
    args.output_json.parent.mkdir(parents=True, exist_ok=True)
    args.output_json.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, ET.ParseError) as exc:
        print(f"freeplane_to_workspace: {exc}", file=sys.stderr)
        raise SystemExit(2)
