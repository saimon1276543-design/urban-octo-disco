from __future__ import annotations

import argparse
import time
from pathlib import Path

from .engine import Workspace


def _signature(ws: Workspace) -> tuple:
    maps = tuple((p.name, p.stat().st_mtime_ns, p.stat().st_size) for p in ws.map_paths())
    workspace = ws.workspace_file.stat().st_mtime_ns if ws.workspace_file.exists() else 0
    return maps, workspace


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default=".")
    parser.add_argument("--interval", type=float, default=1.5)
    args = parser.parse_args()
    ws = Workspace(Path(args.workspace).resolve())
    ws.init()
    print(f"Watching {ws.root}; press Ctrl+C to stop")
    last = None
    try:
        while True:
            current = _signature(ws)
            if current != last:
                if last is None or current[0] != last[0]:
                    result = ws.import_maps()
                else:
                    result = ws.export_maps()
                if result.status in {"synced", "conflict"}:
                    print(result)
                last = current
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("Stopped")
