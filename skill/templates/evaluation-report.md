# Learning Path Architect Evaluation Report

Use this template after running one or more cases from `references/evaluation-cases.md` and scoring them with `references/evaluation-scorecard.md`.

## Run metadata

| Field | Value |
|---|---|
| Skill version or revision | {{Identifier}} |
| Date | {{Date}} |
| Cases run | {{Case numbers}} |
| Evaluator | {{Name or system}} |

## Case results

| Case | Total score / 84 | Blocking zero? | Lowest dimension | Result |
|---|---:|---|---|---|
| {{Case}} | {{Score}} | {{Yes/No}} | {{Dimension}} | {{Pass / revise}} |

## Observed failures

| Case | Failure | Root cause | Smallest proposed rule change |
|---|---|---|---|
| {{Case}} | {{What failed}} | {{Why it failed}} | {{Minimal change}} |

## Regression checks

| Contrasting case | What could regress | Result |
|---|---|---|
| {{Case}} | {{Narrowness, breadth, ambiguity, or other risk}} | {{Pass / revise}} |

## Decision

{{Accept the revision, revise again, or revert. Explain the evidence briefly.}}

Do not claim general improvement from a small test set. Report the tested cases, scores, limitations, and unresolved risks.
