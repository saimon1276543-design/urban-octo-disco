# Tracker Modes

Choose the lightest tracker that can support the learner’s decision. Do not impose a detailed log on a learner who only needs a next-step review.

## Lite tracker

Use after a short cycle or when tracking burden is a risk. Record only planned effort, actual effort, completed units, the main blocker, evidence result, and next action. Review after two or three cycles. Treat all unrecorded dimensions as unknown.

| Cycle | Planned effort | Actual effort | Completed/planned units | Main blocker | Evidence result | Next action |
|---|---:|---:|---:|---|---|---|
| {{}} | {{}} | {{}} | {{}} / {{}} | {{}} | {{}} | {{}} |

## Standard tracker

Use `templates/learning-observation-tracker.md` when capacity, interruptions, recovery, concurrency, switching cost, or periodic replanning materially affect the route.

## Structured tracker

Use `templates/observation-tracker.schema.json` when records must be validated, aggregated, stored in a database, or processed by `scripts/recalibration_report.py`.

## Missing and unusual data

Mark missing observations as unknown; do not treat them as zero. Separate a one-off shock from a repeated pattern. Use medians or conservative bands across comparable cycles rather than one unusually good or bad cycle. Do not change multiple assumptions at once unless the evidence shows they are coupled. When evidence quality is weak, narrow the claim rather than increasing confidence.

## Mode escalation

Escalate from Lite to Standard when two cycles reveal unexplained variance, repeated blockers, unsustainable concurrency, or a capacity shock. Escalate to Structured when automation, persistent history, cross-session comparison, or machine validation is needed. Return to Lite when tracking burden itself becomes a blocker and the route can be safely managed with fewer fields.
