from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .engine import Workspace
from .model import load_json, save_json


def main() -> int:
    parser = argparse.ArgumentParser(prog="freeplane-sync")
    parser.add_argument("command", choices=["init", "import", "export", "sync", "undo", "redo", "backup", "revisions", "conflicts", "status"])
    parser.add_argument("--workspace", default=".")
    args = parser.parse_args()
    ws = Workspace(Path(args.workspace).resolve())
    ws.init()
    if args.command == "init":
        print(json.dumps({"status": "initialized", "workspace": str(ws.root)}, indent=2))
        return 0
    if args.command == "backup":
        print(json.dumps({"status": "checkpoint-created", "path": str(ws.checkpoint("manual"))}, indent=2))
        return 0
    if args.command == "revisions":
        print(json.dumps({"revisions": load_json(ws.history_file, [])}, indent=2))
        return 0
    if args.command == "conflicts":
        print(json.dumps({"conflicts": load_json(ws.conflicts_file, [])}, indent=2))
        return 0
    if args.command == "import":
        result = ws.import_maps()
    elif args.command == "export":
        result = ws.export_maps()
    elif args.command == "sync":
        result = ws.import_maps()
        if result.status == "unchanged":
            result = ws.export_maps()
    elif args.command == "undo":
        result = ws.undo_saved()
    elif args.command == "redo":
        result = ws.redo_saved()
    else:
        result = {"workspace": str(ws.root), "maps": [str(p) for p in ws.map_paths()], "workspace_file": str(ws.workspace_file)}
        print(json.dumps(result, indent=2))
        return 0
    print(json.dumps(result.__dict__, indent=2))
    return 2 if result.status == "conflict" else 0


if __name__ == "__main__":
    sys.exit(main())
