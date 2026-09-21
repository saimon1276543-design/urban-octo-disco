from pathlib import Path

from freeplane_sync.engine import Workspace
from freeplane_sync.model import parse_map, save_json


def write_sample(path: Path) -> None:
    path.write_text('''<?xml version="1.0" encoding="UTF-8"?>\n<map version="freeplane 1.12.0"><node TEXT="Root" ID="ID_ROOT"><richcontent TYPE="NOTE"><html><body><p>Overview</p></body></html></richcontent><node TEXT="Child" ID="ID_CHILD"/></node></map>\n''', encoding="utf-8")


def test_parse_and_import(tmp_path: Path) -> None:
    maps = tmp_path / "maps"
    maps.mkdir()
    write_sample(maps / "master.mm")
    ws = Workspace(tmp_path)
    ws.init()
    result = ws.import_maps()
    assert result.status == "synced"
    data = ws.load_workspace()
    assert data["maps"][0]["root_id"] == "ID_ROOT"
    assert data["maps"][0]["nodes"]["ID_CHILD"]["parent_id"] == "ID_ROOT"
    assert data["maps"][0]["nodes"]["ID_ROOT"]["note"] == "Overview"


def test_workspace_export_and_round_trip(tmp_path: Path) -> None:
    maps = tmp_path / "maps"
    maps.mkdir()
    write_sample(maps / "master.mm")
    ws = Workspace(tmp_path)
    ws.init()
    ws.import_maps()
    data = ws.load_workspace()
    data["maps"][0]["nodes"]["ID_CHILD"]["text"] = "Renamed"
    save_json(ws.workspace_file, data)
    result = ws.export_maps()
    assert result.status == "synced"
    assert parse_map(maps / "master.mm").nodes["ID_CHILD"].text == "Renamed"


def test_conflict_is_not_silent(tmp_path: Path) -> None:
    maps = tmp_path / "maps"
    maps.mkdir()
    write_sample(maps / "master.mm")
    ws = Workspace(tmp_path)
    ws.init()
    ws.import_maps()
    data = ws.load_workspace()
    data["maps"][0]["nodes"]["ID_CHILD"]["text"] = "Workspace edit"
    save_json(ws.workspace_file, data)
    maps.joinpath("master.mm").write_text(maps.joinpath("master.mm").read_text(encoding="utf-8").replace("Child", "Map edit"), encoding="utf-8")
    result = ws.import_maps()
    assert result.status == "conflict"
    assert ws.conflicts_file.exists()
