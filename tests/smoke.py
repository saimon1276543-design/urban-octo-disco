from pathlib import Path
from tempfile import TemporaryDirectory

from freeplane_sync.engine import Workspace
from freeplane_sync.model import parse_map, save_json


def sample(path: Path) -> None:
    path.write_text('<?xml version="1.0"?><map version="freeplane"><node TEXT="Root" ID="ID_ROOT"><richcontent TYPE="NOTE"><html><body><p>Overview</p></body></html></richcontent><node TEXT="Child" ID="ID_CHILD"/></node></map>', encoding="utf-8")


def main() -> None:
    with TemporaryDirectory() as temp:
        root = Path(temp)
        (root / "maps").mkdir()
        sample(root / "maps" / "master.mm")
        ws = Workspace(root)
        ws.init()
        assert ws.import_maps().status == "synced"
        data = ws.load_workspace()
        assert data["maps"][0]["nodes"]["ID_ROOT"]["note"] == "Overview"
        data["maps"][0]["nodes"]["ID_CHILD"]["text"] = "Renamed"
        save_json(ws.workspace_file, data)
        assert ws.export_maps().status == "synced"
        assert parse_map(root / "maps" / "master.mm").nodes["ID_CHILD"].text == "Renamed"
        assert ws.undo_saved().status == "restored"
        assert parse_map(root / "maps" / "master.mm").nodes["ID_CHILD"].text == "Child"
        assert ws.redo_saved().status == "restored"
        assert parse_map(root / "maps" / "master.mm").nodes["ID_CHILD"].text == "Renamed"
        data = ws.load_workspace()
        data["maps"][0]["nodes"]["ID_CHILD"]["text"] = "Workspace edit"
        save_json(ws.workspace_file, data)
        map_path = root / "maps" / "master.mm"
        map_path.write_text(map_path.read_text(encoding="utf-8").replace("Renamed", "Map edit"), encoding="utf-8")
        assert ws.import_maps().status == "conflict"
    print("smoke tests passed")


if __name__ == "__main__":
    main()
