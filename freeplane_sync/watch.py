from __future__ import annotations

import argparse
import time
from pathlib import Path

from .engine import Workspace


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
            signature = tuple((p.name, p.stat().st_mtime_ns, p.stat().st_size) for p in ws.map_paths())
            if signature != last:
                result = ws.import_maps()
                if result.status in {"synced", "conflict"}:
                    print(result)
                last = signature
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("Stopped")
