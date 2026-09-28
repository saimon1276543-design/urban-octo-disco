from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill [learning-path-architect]" / "SKILL.md"


def main() -> None:
    text = SKILL.read_text(encoding="utf-8")
    assert text.count("\n") < 500, "SKILL.md must stay below the progressive-disclosure limit"
    assert "plain-language-response-contract.md" in text
    assert "plan-quality-check.md" in text
    assert "hosted-only-operating-contract.md" in text
    assert "hosted-time-plan.md" in text
    assert "diagnostic-first-learning-loop.md" in text
    assert "decision-record.md" in text
    assert "network-api-interception-for-scraping.md" in text
    assert "effort, session, cycle, calendar, and deadline-feasibility" in text
    assert "one primary next action" in text
    assert "Do not report that the host recognized" in text
    root = ROOT / "skill [learning-path-architect]"
    assert (root / "references" / "plain-language-response-contract.md").exists()
    assert (root / "references" / "plan-quality-check.md").exists()
    assert (root / "references" / "hosted-only-operating-contract.md").exists()
    assert (root / "templates" / "hosted-capstone.md").exists()
    assert (root / "templates" / "hosted-time-plan.md").exists()
    assert (root / "templates" / "hosted-progress-view.md").exists()
    assert (root / "references" / "diagnostic-first-learning-loop.md").exists()
    assert (root / "references" / "network-api-interception-for-scraping.md").exists()
    assert (root / "templates" / "decision-record.md").exists()
    print("skill contract smoke test passed")


if __name__ == "__main__":
    main()
