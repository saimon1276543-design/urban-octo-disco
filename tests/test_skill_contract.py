from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "SKILL.md"


def main() -> None:
    text = SKILL.read_text(encoding="utf-8")
    assert text.count("\n") < 500, "SKILL.md must stay below the progressive-disclosure limit"
    assert "plain-language-response-contract.md" in text
    assert "plan-quality-check.md" in text
    assert "one primary next action" in text
    assert "Do not report that the host recognized" in text
    assert (ROOT / "skill" / "references" / "plain-language-response-contract.md").exists()
    assert (ROOT / "skill" / "references" / "plan-quality-check.md").exists()
    print("skill contract smoke test passed")


if __name__ == "__main__":
    main()
