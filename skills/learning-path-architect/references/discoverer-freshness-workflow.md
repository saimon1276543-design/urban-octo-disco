# Discoverer Freshness Workflow

Use this reference for a companion skill that keeps a learning roadmap current without silently rewriting it.

## Freshness classes

| Class | Typical content | Review target |
|---|---|---:|
| Stable foundations | durable concepts and long-established principles | yearly |
| Changing intermediate knowledge | tools, methods, standards, and common practices | every six months |
| Fast-moving/community knowledge | releases, emerging methods, market capability, active community discussion | weekly |

These are review targets, not promises that a hosted environment will run in the background. Record the actual check date and the next due date.

## Discoverer procedure

1. Read the freshness ledger and select only areas that are due.
2. Search primary sources and credible technical/community sources appropriate to the topic.
3. Record source URLs, publication or release dates, access dates, and confidence.
4. Separate confirmed change, credible emerging signal, speculation, and irrelevant noise.
5. Identify which roadmap nodes, prerequisites, tools, evidence, or maintenance tasks are affected.
6. Produce an update proposal rather than silently changing the canonical route.
7. Accept, reject, or watch the proposal according to the learner's decision.
8. Record the decision, revision, and next review trigger.

## Decision labels

Use `add`, `replace`, `revise`, `watch`, `defer`, or `ignore`. A weekly discovery should not displace a stable prerequisite merely because it is new. Add it only when it improves the target capability, changes the market expectation, closes a real gap, or materially affects the chosen route.

## Hosted scheduling rule

Before claiming that Discoverer checked the roadmap automatically, verify that the current host provides recurring execution and persistent result storage. If it does not, expose a manual action: “Run Discoverer now.” Keep the review queue so the next run can continue from the last verified date.

## User-facing report

```text
Discoverer review
Checked: 2026-09-20
Scope: fast-moving community topics

Finding: [short description]
Affected area: [roadmap branch]
Importance: essential / useful / optional / irrelevant
Evidence: [sources and dates]
Recommendation: add / replace / revise / watch / ignore
Status: pending learner decision
```

## Safety and scope

Do not use novelty as proof of quality. Do not add every trend. Preserve the previous route until a proposal is accepted or a clearly documented low-risk maintenance rule applies. For volatile or safety-sensitive fields, require stronger source verification and shorter revalidation intervals.

Use `templates/discoverer-review.schema.json`, `templates/revalidation-queue.schema.json`, `templates/source-claim-ledger.schema.json`, and `templates/update-run.schema.json` for durable records.
