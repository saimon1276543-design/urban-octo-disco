#!/usr/bin/env python3
"""Create a basic Freeplane .mm map from a JSON node list.

Input shape:
{
  "map_title": "Example",
  "nodes": [
    {"id": "root", "title": "Root", "parent_id": null,
     "note": "Optional note", "link": "optional URI"}
  ]
}

This intentionally preserves the core hierarchy, IDs, notes, and links.
Complex Freeplane styling should be checked in Freeplane after export.
"""
from __future__ import annotations
import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def add_richcontent(node: ET.Element, text: str) -> None:
    rich = ET.SubElement(node, "richcontent", {"TYPE": "NOTE"})
    html = ET.SubElement(rich, "html")
    body = ET.SubElement(html, "body")
    p = ET.SubElement(body, "p")
    p.text = text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_json", type=Path)
    parser.add_argument("output_mm", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input_json.read_text(encoding="utf-8"))
    nodes = data.get("nodes", [])
    by_id = {str(n["id"]): n for n in nodes}
    children: dict[str | None, list[dict]] = {}
    for item in nodes:
        children.setdefault(item.get("parent_id"), []).append(item)
    for values in children.values():
        values.sort(key=lambda item: item.get("order", 0))
    roots = children.get(None) or children.get("", [])
    if len(roots) != 1:
        raise ValueError("Input must contain exactly one root node with parent_id null")

    root = ET.Element("map", {"version": "freeplane 1.13.3"})

    def emit(item: dict) -> ET.Element:
        node_id = str(item["id"])
        attrs = {"TEXT": str(item.get("title", "")), "ID": node_id}
        if item.get("link"):
            attrs["LINK"] = str(item["link"])
        out = ET.Element("node", attrs)
        if item.get("note"):
            add_richcontent(out, str(item["note"]))
        for child in children.get(node_id, []):
            out.append(emit(child))
        return out

    root.append(emit(roots[0]))
    ET.indent(root, space="  ")
    args.output_mm.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(args.output_mm, encoding="utf-8", xml_declaration=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"workspace_to_freeplane: {exc}", file=sys.stderr)
        raise SystemExit(2)
