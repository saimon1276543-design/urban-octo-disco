# Cloud and DevOps Domain Module

Use this module when the request includes cloud infrastructure, infrastructure-as-code, deployment automation, reliability, or platform operations.

## Common prerequisite branches

| Outcome | High-confidence foundations | Context-dependent additions |
|---|---|---|
| Automate infrastructure | Networking, identity, configuration, version control, state, testing | Provider-specific services, policy-as-code, multi-account design |
| Build a delivery pipeline | Build artifacts, tests, environments, secrets, rollback, observability | Container orchestration, progressive delivery, compliance gates |
| Operate a reliable platform | Linux or runtime basics, networking, monitoring, incident response, backups | SRE practices, multi-region design, regulated controls, cost optimization |

## Infrastructure-as-code safeguards

Teach desired state, state storage and locking, plan or preview workflows, drift detection, import and migration, secrets handling, review, and rollback. Distinguish reusable modules from provider-specific implementation details.

## Operational environment ladder

Separate local or sandbox work, isolated test environments, staging or pre-production, and production. Require authorization and reversible changes before any real environment action. Make access, blast radius, backup, and rollback visible in the evidence.

## Common traps

Check for unmanaged state, credential leakage, overly broad permissions, insecure defaults, untested recovery, hidden provider coupling, missing observability, and confusing a successful deployment with reliable operation.

## Evidence by level

| Level | Suitable evidence context |
|---|---|
| Novice | Guided deployment in a sandbox with a documented rollback |
| Advanced Beginner | Independent familiar environment change with validation and cleanup |
| Competent | Bounded unfamiliar infrastructure change with state, security, tests, and recovery evidence |
| Proficient | Ambiguous platform design with reliability, cost, security, and operational trade-offs |
| Expert | Novel platform judgment, failure modeling, governance, and defensible architecture review |
