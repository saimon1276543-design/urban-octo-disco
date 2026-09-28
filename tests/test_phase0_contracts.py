import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "skill [learning-path-architect]" / "templates"

SCHEMA_NAMES = [
    "capstone.schema.json",
    "submission-manifest.schema.json",
    "evaluation-result.schema.json",
    "mistake-memory.schema.json",
    "review-event.schema.json",
    "permission-policy.schema.json",
]


def read_schema(name: str) -> dict:
    path = TEMPLATES / name
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["$schema"].endswith("2020-12/schema")
    assert data["type"] == "object"
    assert data["additionalProperties"] is False
    return data


def main() -> None:
    schemas = {name: read_schema(name) for name in SCHEMA_NAMES}

    capstone = schemas["capstone.schema.json"]
    assert {"capstone_id", "rubric", "evidence_requirements", "review_policy"} <= set(capstone["required"])

    submission = schemas["submission-manifest.schema.json"]
    assert {"authorized_root", "files", "learner_statement"} <= set(submission["required"])
    assert "relative_path" in submission["$defs"]["file"]["properties"]

    evaluation = schemas["evaluation-result.schema.json"]
    statuses = evaluation["$defs"]["evidence"]["properties"]["status"]["enum"]
    assert "unknown" in statuses and "tool_checked" in statuses and "retention_checked" in statuses
    assert "uncertainties" in evaluation["required"]

    mistake = schemas["mistake-memory.schema.json"]
    assert {"observation_count", "status", "review_policy"} <= set(mistake["required"])

    review = schemas["review-event.schema.json"]
    assert {"estimated_task_minutes", "status", "roadmap_insertion"} <= set(review["required"])
    assert "time_tracker" in review["properties"]["time_source"]["enum"]

    permission = schemas["permission-policy.schema.json"]
    assert {"authorized_roots", "read", "write", "execution", "confirmation"} <= set(permission["required"])
    assert "official_records" in permission["properties"]["write"]["properties"]
    assert "update_freeplane" in permission["properties"]["confirmation"]["properties"]

    print("phase 0 contract tests passed")


if __name__ == "__main__":
    main()
