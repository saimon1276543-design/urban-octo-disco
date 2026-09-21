from __future__ import annotations

import hashlib
import json
import shutil
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .model import load_json, parse_map, save_json, workspace_to_map


@dataclass
class SyncResult:
    status: str
    direction: str
    changed: list[str]
    conflicts: list[str]
    revision_id: str | None = None


class Workspace:
    def __init__(self, root: Path):
        self.root = root
        self.maps_dir = root / "maps"
        self.meta_dir = root / ".sync"
        self.checkpoints_dir = self.root / "checkpoints"
        self.revisions_dir = root / "revisions"
        self.workspace_file = root / "workspace.json"
        self.snapshot_file = self.meta_dir / "last-synced-workspace.json"
        self.map_snapshot_file = self.meta_dir / "last-synced-map.json"
        self.history_file = self.meta_dir / "saved-history.json"
        self.redo_file = self.meta_dir / "redo.json"
        self.conflicts_file = root / "conflicts.json"

    def load_workspace(self) -> dict[str, Any]:
        return load_json(self.workspace_file, {"schema_version": "1.0", "maps": []})

    def map_paths(self) -> list[Path]:
        return sorted(self.maps_dir.glob("*.mm"))

    def read_maps(self) -> dict[str, Any]:
        records = [parse_map(path) for path in self.map_paths()]
        return {"schema_version": "1.0", "maps": [record.as_dict() for record in records]}

    @staticmethod
    def digest(value: Any) -> str:
        raw = json.dumps(value, sort_keys=True, ensure_ascii=False).encode()
        return hashlib.sha256(raw).hexdigest()

    def init(self) -> None:
        for directory in [self.maps_dir, self.meta_dir, self.checkpoints_dir, self.revisions_dir]:
            directory.mkdir(parents=True, exist_ok=True)
        if not self.workspace_file.exists():
            save_json(self.workspace_file, {"schema_version": "1.0", "maps": []})
        if not self.conflicts_file.exists():
            save_json(self.conflicts_file, [])
        if not self.history_file.exists():
            save_json(self.history_file, [])
        if not self.redo_file.exists():
            save_json(self.redo_file, [])

    def checkpoint(self, label: str = "checkpoint") -> Path:
        stamp = time.strftime("%Y%m%d-%H%M%S")
        target = self.checkpoints_dir / f"{stamp}-{label}-{time.time_ns()}"
        target.mkdir(parents=True, exist_ok=False)
        self._copy_state(target)
        return target

    def _copy_state(self, target: Path) -> None:
        for source in [self.workspace_file, self.conflicts_file]:
            if source.exists():
                shutil.copy2(source, target / source.name)
        if self.maps_dir.exists():
            shutil.copytree(self.maps_dir, target / "maps")

    def _record_saved_revision(self, label: str) -> str:
        stamp = time.strftime("%Y%m%d-%H%M%S")
        revision_id = f"{stamp}-{label}-{time.time_ns()}"
        target = self.revisions_dir / revision_id
        target.mkdir(parents=True, exist_ok=False)
        self._copy_state(target)
        history = load_json(self.history_file, [])
        history.append({"revision_id": revision_id, "path": str(target), "created_at": time.time()})
        save_json(self.history_file, history[-10:])
        save_json(self.redo_file, [])
        return revision_id

    def import_maps(self) -> SyncResult:
        current = self.read_maps()
        previous = load_json(self.snapshot_file, None)
        workspace = self.load_workspace()
        workspace_changed = previous is not None and self.digest(workspace) != self.digest(previous)
        map_changed = previous is None or self.digest(current) != self.digest(load_json(self.map_snapshot_file, {}))
        if workspace_changed and map_changed:
            return self._record_conflict("Freeplane and workspace changed since the last sync")
        if not map_changed:
            return SyncResult("unchanged", "none", [])
        self.checkpoint("before-import")
        save_json(self.workspace_file, current)
        save_json(self.snapshot_file, current)
        save_json(self.map_snapshot_file, current)
        revision = self._record_saved_revision("import")
        return SyncResult("synced", "map-to-workspace", [str(self.workspace_file)], [], revision)

    def export_maps(self) -> SyncResult:
        workspace = self.load_workspace()
        previous = load_json(self.snapshot_file, None)
        current_maps = self.read_maps()
        workspace_changed = previous is None or self.digest(workspace) != self.digest(previous)
        map_changed = previous is not None and self.digest(current_maps) != self.digest(load_json(self.map_snapshot_file, {}))
        if workspace_changed and map_changed:
            return self._record_conflict("Freeplane and workspace changed since the last sync")
        if not workspace_changed:
            return SyncResult("unchanged", "none", [])
        self.checkpoint("before-export")
        for map_data in workspace.get("maps", []):
            filename = map_data.get("file", f"{map_data.get('map_id', 'map')}.mm")
            workspace_to_map({"maps": [map_data]}, self.maps_dir / filename)
        save_json(self.snapshot_file, workspace)
        saved_maps = self.read_maps()
        save_json(self.map_snapshot_file, saved_maps)
        revision = self._record_saved_revision("export")
        return SyncResult("synced", "workspace-to-map", [str(p) for p in self.map_paths()], [], revision)

    def undo_saved(self) -> SyncResult:
        history = load_json(self.history_file, [])
        if len(history) < 2:
            return SyncResult("unavailable", "none", [], [])
        current = history.pop()
        target = history[-1]
        redo = load_json(self.redo_file, [])
        redo.append(current)
        save_json(self.history_file, history)
        save_json(self.redo_file, redo[-10:])
        self.checkpoint("before-undo")
        self._restore(Path(target["path"]))
        return SyncResult("restored", "undo", [target["path"]], [], target["revision_id"])

    def redo_saved(self) -> SyncResult:
        redo = load_json(self.redo_file, [])
        if not redo:
            return SyncResult("unavailable", "none", [], [])
        target = redo.pop()
        history = load_json(self.history_file, [])
        history.append(target)
        save_json(self.history_file, history[-10:])
        save_json(self.redo_file, redo)
        self.checkpoint("before-redo")
        self._restore(Path(target["path"]))
        return SyncResult("restored", "redo", [target["path"]], [], target["revision_id"])

    def _restore(self, revision: Path) -> None:
        for name in ["workspace.json", "conflicts.json"]:
            source = revision / name
            if source.exists():
                shutil.copy2(source, self.root / name)
        source_maps = revision / "maps"
        if source_maps.exists():
            if self.maps_dir.exists():
                shutil.rmtree(self.maps_dir)
            shutil.copytree(source_maps, self.maps_dir)
        save_json(self.snapshot_file, self.load_workspace())
        save_json(self.map_snapshot_file, self.read_maps())

    def _record_conflict(self, message: str) -> SyncResult:
        conflict_id = f"conflict-{int(time.time())}"
        conflicts = load_json(self.conflicts_file, [])
        conflicts.append({"id": conflict_id, "type": "concurrent-change", "message": message, "created_at": time.time()})
        save_json(self.conflicts_file, conflicts)
        return SyncResult("conflict", "none", [], [conflict_id])
