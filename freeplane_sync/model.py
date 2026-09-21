from __future__ import annotations

import html
import json
import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


def _text(value: str | None) -> str:
    return value or ""


def _note_from_element(node: ET.Element) -> str:
    for child in node.findall("richcontent"):
        if child.get("TYPE", "").upper() == "NOTE":
            return " ".join(t.strip() for t in child.itertext() if t.strip())
    return ""


@dataclass
class NodeRecord:
    id: str
    text: str
    note: str = ""
    attributes: dict[str, str] = field(default_factory=dict)
    parent_id: str | None = None
    children: list[str] = field(default_factory=list)
    links: list[str] = field(default_factory=list)
    map_id: str = ""

    def as_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "text": self.text,
            "note": self.note,
            "attributes": dict(self.attributes),
            "parent_id": self.parent_id,
            "children": list(self.children),
            "links": list(self.links),
            "map_id": self.map_id,
        }


@dataclass
class MapRecord:
    map_id: str
    file: str
    root_id: str
    nodes: dict[str, NodeRecord]

    def as_dict(self) -> dict[str, Any]:
        return {
            "map_id": self.map_id,
            "file": self.file,
            "root_id": self.root_id,
            "nodes": {key: value.as_dict() for key, value in sorted(self.nodes.items())},
        }


def _safe_id(value: str, fallback: str) -> str:
    return value or fallback


def parse_map(path: Path, map_id: str | None = None) -> MapRecord:
    tree = ET.parse(path)
    root = tree.getroot().find("node")
    if root is None:
        raise ValueError(f"Freeplane map has no root node: {path}")
    mid = map_id or path.stem
    nodes: dict[str, NodeRecord] = {}

    def visit(element: ET.Element, parent: str | None) -> str:
        node_id = _safe_id(element.get("ID"), f"generated-{len(nodes)+1}")
        record = NodeRecord(
            id=node_id,
            text=_text(element.get("TEXT")),
            note=_note_from_element(element),
            parent_id=parent,
            map_id=mid,
        )
        for child in element.findall("node"):
            child_id = visit(child, node_id)
            record.children.append(child_id)
        nodes[node_id] = record
        return node_id

    root_id = visit(root, None)
    return MapRecord(mid, path.name, root_id, nodes)


def workspace_to_map(data: dict[str, Any], path: Path) -> None:
    map_data = data["maps"][0] if "maps" in data else data
    root_id = map_data["root_id"]
    nodes = map_data["nodes"]
    root = ET.Element("node", {"TEXT": nodes[root_id].get("text", ""), "ID": root_id})

    def add_children(parent: ET.Element, node_id: str) -> None:
        record = nodes[node_id]
        note = record.get("note", "")
        if note:
            rich = ET.SubElement(parent, "richcontent", {"TYPE": "NOTE"})
            html_el = ET.SubElement(rich, "html")
            body = ET.SubElement(html_el, "body")
            p = ET.SubElement(body, "p")
            p.text = note
        for child_id in record.get("children", []):
            child_record = nodes[child_id]
            child = ET.SubElement(parent, "node", {
                "TEXT": child_record.get("text", ""),
                "ID": child_id,
            })
            add_children(child, child_id)

    add_children(root, root_id)
    map_el = ET.Element("map", {"version": "freeplane_sync 1.0"})
    map_el.append(root)
    tree = ET.ElementTree(map_el)
    ET.indent(tree, space="  ")
    path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def map_as_workspace(record: MapRecord) -> dict[str, Any]:
    return {"schema_version": "1.0", "maps": [record.as_dict()]}


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temp.replace(path)


def flatten_workspace(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for map_data in data.get("maps", []):
        for node_id, node in map_data.get("nodes", {}).items():
            item = dict(node)
            item["map_id"] = map_data.get("map_id", item.get("map_id", ""))
            result[f"{item['map_id']}:{node_id}"] = item
    return result


def merge_map_records(records: list[MapRecord]) -> dict[str, Any]:
    return {"schema_version": "1.0", "maps": [record.as_dict() for record in records]}
