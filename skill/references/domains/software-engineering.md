# Software Engineering Domain Module

Use this module when the request includes software development, system design, testing, delivery, or production operations. Load only the sections relevant to the requested outcome.

## Common prerequisite branches

| Outcome | High-confidence foundations | Context-dependent additions |
|---|---|---|
| Build a maintainable application | Programming fluency, version control, debugging, data modeling, testing | Framework conventions, team workflow, deployment platform |
| Design a service or system | Requirements, interfaces, data flow, failure modes, observability | Distributed systems, cost modeling, compliance, scale |
| Operate software reliably | Linux or platform basics, networking, logs, backups, incident response | Cloud provider, container orchestration, SLOs, regulated controls |

## Leaf-objective patterns

Prefer objectives such as “Write a focused unit test and diagnose a failing assertion,” “Design an interface and document error behavior,” “Trace a request across service boundaries using logs,” and “Deploy a reversible change with a rollback procedure.” Avoid treating framework syntax as a substitute for shared concepts.

## Testing ladder

When testing is part of the outcome, distinguish focused unit tests, component or integration tests, contract tests, end-to-end tests, performance tests, and failure or recovery tests. Do not require every tier unless the target context justifies it.

## Operational environment ladder

Separate local development, isolated test or staging environments, and production-like operation. A production deployment objective should include configuration, secrets, observability, rollback, backup, and access boundaries only when they are relevant to the requested system.

## Common traps

Check for hidden coupling, weak error handling, untested failure paths, unclear ownership, missing observability, insecure secret handling, and confusing “works locally” with operational readiness. Use a focused corrective unit rather than a generic list.

## Evidence by level

| Level | Suitable evidence context |
|---|---|
| Novice | Guided implementation with tests and explanation of the local workflow |
| Advanced Beginner | Independent feature or bugfix in a familiar codebase |
| Competent | Reliable change in a bounded unfamiliar codebase with tests and debugging evidence |
| Proficient | Ambiguous design or integration with trade-offs, failure analysis, and operational evidence |
| Expert | Novel system judgment, explicit evaluation criteria, and defensible architectural communication |
