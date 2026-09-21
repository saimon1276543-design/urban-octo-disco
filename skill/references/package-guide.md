# Learning Path Architect

This package converts unstructured learning goals into hierarchical, dependency-aware learning maps and practical roadmaps. The core behavior is defined in `SKILL.md`.

## Resource selection

Start with `README.md` when a learner needs an orientation to the skill, its situations, capabilities, tracker workflow, or limitations. Use `SKILL.md` for the execution instructions used by the AI harness.

| User need | Resource | Use it when |
|---|---|---|
| Response-mode, scope, freshness, and risk selection | `references/decision-gate.md` | Read first when deciding whether the request needs a map, roadmap, portfolio, assessment, revision workflow, current research, or special safeguards. |
| Any supplied duration or ongoing program | `references/long-horizon-planning.md` | Use for day/month/year/open-ended horizon layers, north star, capacity, concurrency, stability classes, maintenance, and periodic replanning. |
| Deep capacity and periodic replanning | `references/capacity-and-replanning.md` and `scripts/capacity_model.py` | Use when time, interruptions, cognitive load, maintenance, recovery, observed throughput, concurrency, sustainability, or review decisions affect the route. |
| Time decomposition and estimation | `references/time-estimation-and-scheduling.md`, `templates/time-budget.schema.json`, and `scripts/time_estimator.py` | Use when the learner asks how long learning will take, requests a schedule/deadline plan, or needs effort converted into sessions, cycles, and calendar time. |
| Practical capacity observation tracker | `templates/learning-observation-tracker.md` and `templates/observation-tracker.schema.json` | Use when the learner needs to log planned/actual effort, completion, sessions, interruptions, recovery, blockers, concurrency, switching cost, and evidence for later recalibration. |
| Recalibration review summary | `scripts/recalibration_report.py` | Use on structured tracker data to summarize robust ratios, flags, the smallest failing assumption, and the next review decision. It supports judgment; it does not automatically change the roadmap. |
| Learner intake and clarification | `references/learner-intake.md` | Use when outcome, context, current level, evidence standard, capacity, or delivery preference is materially unclear; ask only questions that change the route. |
| Assumption and fragility ledger | `references/assumption-ledger.md` | Use for complex or adaptive plans to record sources, confidence, impact if wrong, validation, and review status of consequential assumptions. |
| Evidence design | `references/evidence-design.md` | Use when proficiency, transfer, retention, milestone completion, or unlocking decisions need evidence matched to context. |
| Learner-state diagnostics | `references/learner-state-and-diagnostics.md` and `templates/learner-state-record.md` | Use proportional diagnostics to decide whether to skip, sample, remediate, or start guided; preserve the evidence-backed state. |
| Error-to-intervention | `references/error-to-intervention.md` | Use after failure or stalling to classify the smallest likely gap and select one bounded corrective intervention. |
| Adaptive learning loop | `references/adaptive-learning-loop.md` | Use when the learner needs a retrieve → practice → feedback → transfer → decision cycle. |
| Resource selection | `references/resource-selection.md` and `templates/resource-register.md` | Use only when resources are requested or a diagnosed gap needs a resource tied to evidence. |
| Capability maintenance and decay | `references/maintenance-and-decay.md` | Use for long-horizon, paused, or retention-sensitive plans to protect demonstrated capabilities without creating a second syllabus. |
| Learner-state progress fields | `templates/progress.schema.json` | Optional machine-readable state, intervention, and learner-history fields for durable adaptive replanning. |
| Adaptive-record validation | `scripts/validate_adaptive_records.py` | Validate representative learner-state and intervention records before using them for route decisions. |
| Low-friction tracker modes | `references/tracker-modes.md` | Choose Lite, Standard, or Structured tracking based on the decision need and tracking burden. |
| Current execution action | `templates/current-action-card.md` | Use to expose the primary action, feasible parallel action, evidence boundary, blocker response, and review trigger. |
| Plan revision diff | `templates/plan-revision-diff.md` | Use when a review changes capacity, estimates, nodes, dependencies, route state, or the active frontier. |
| Plan-control validation | `scripts/validate_plan_controls.py` | Validate representative current-action and assumption-ledger JSON records before relying on them in automation. |
| Single syllabus, linked parts, workspace, local/cloud delivery, or progress tracking | `references/delivery-and-linking.md` | Use to choose single-document versus linked-part delivery, detect verified workspace/link capabilities, and integrate persistent progress safely. |
| Hands-off persistence, synchronization, MCP/API/database integration | `references/workspace-adapters.md` | Use the automation-first adapter hierarchy and capability contract; avoid recurring manual upload/download and never claim an unavailable connector. |
| Portable workspace interface | `references/workspace-contract.md` and `references/interoperability.md` | Use when moving a roadmap between AI harnesses or mapping the same plan to MCP, filesystem, Git, database, project API, or artifact storage. |
| Adapter capability discovery | `references/capability-probing.md` | Use before trusting a persistent adapter; record reachability, authentication, permissions, persistence, links, versioning, transactions, conflicts, and missing operations. |
| Safe persistent updates | `references/safe-mutation.md` | Use before changing an existing workspace; apply checkpoints/versioning, idempotent updates, post-write verification, rollback/recovery, and conflict rules. |
| Standard syllabus or skill map | `templates/learning-map.md` | The user wants decomposition, coverage, prerequisites, or a structured map without a schedule. |
| Sequenced study plan | `templates/roadmap.md` | The user asks what to learn first, how to progress, or how milestones should be ordered for one main route. |
| Integrated multi-topic portfolio | `templates/portfolio-roadmap.md` and `references/long-input-integration.md` | A very long wall of text contains multiple learning goals that must be clustered, connected, prioritized, and delivered together without false linearity. |
| Massive multi-domain portfolio | `references/massive-multi-domain-portfolio.md` and `templates/multi-domain-portfolio.md` | The learner wants several vast domains together; build a scalable index, preserve irreducible cores, control concurrency, and stage integration. |
| Domain registry and ontology | `references/domain-registry-and-ontology.md` | Domain labels contain multiple subdisciplines or could be confused with credentials, technologies, or capabilities. |
| Cross-domain bridges and interference | `references/cross-domain-interference-and-bridges.md` | Parallel families, bridge competencies, integration studios, or cross-domain switching affect the route. |
| Multi-domain machine-readable manifest | `templates/multi-domain-portfolio.schema.json` | A downstream workspace or tracker needs a stable domain registry, bridge list, and active frontier. |
| Multi-domain manifest validation | `scripts/validate_multi_domain_portfolio.py` | Validate domain IDs, route states, bridge coverage, and active-frontier fields before using a portfolio manifest. |
| Readiness or proficiency validation | `templates/proficiency-assessment.md` | The user asks how to judge progress, demonstrate competence, or validate a target level. |
| Five-level calibration | `references/proficiency-levels.md` | A target level is stated or must be inferred: Novice, Advanced Beginner, Competent, Proficient, or Expert. |
| Recurring domain customization | `references/domain-reference-template.md` | A domain needs specialized prerequisites, misconceptions, tools, or level-specific evidence. |
| Safe revision of an existing map | `templates/revision-diff.md` | A prior map or roadmap must be updated without silent route or dependency changes. |
| Regression testing | `references/evaluation-cases.md` | The skill has been revised and outputs should be checked against representative requests. |
| Consistent quality scoring | `references/evaluation-scorecard.md` | Outputs need to be compared across revisions using explicit quality dimensions and thresholds. |
| Recording test runs | `templates/evaluation-report.md` | Scores, failures, regression checks, and revision decisions need to be retained across real examples. |
| Structured learner context | `templates/learner-profile.md` | Current levels, constraints, tools, preferences, and diagnostics need to be made explicit without over-questioning. |
| Prerequisite audit | `templates/prerequisite-register.md` | Inferred dependencies materially affect scope or need explicit confidence, rationale, and activation conditions. |
| High-consequence boundaries | `references/risk-and-boundary-guide.md` | A path involves regulated, safety-critical, hazardous, privacy-sensitive, or dual-use work. |
| Domain-module selection | `references/domain-index.md` | The request may match one or more supported domains and the smallest relevant module must be selected. |
| Current domain verification | `references/freshness-protocol.md` | The freshness gate determines whether strict research, lighter verification, or the explicitly abstract timeless exception applies. |
| Freshness control plane | `references/freshness-control-plane.md` | Large or current portfolios need a source ledger, change taxonomy, update mode, research cutoff, and honest automation boundary. |
| Incremental update impact | `references/incremental-update-protocol.md` | A source, tool, regulation, evidence standard, bridge, or learner context changes and only the affected subgraph should be revalidated. |
| Drift scans and triggers | `references/drift-scans-and-triggers.md` | An ongoing portfolio needs expiry, version, source, integration, learner-change, or scheduled revalidation triggers. |
| Source health and conflicts | `references/source-health-and-conflicts.md` | Sources age, become inaccessible, disagree, or differ by region, version, or context. |
| Portable update operation | `references/portable-update-operation.md` | The portfolio must work across AI harnesses, online/offline hosts, local files, cached archives, MCP, databases, hosted workspaces, or artifacts. |
| Source and claim ledger | `templates/source-claim-ledger.schema.json` | Current claims require source authority, access date, version/context, health, node mapping, confidence, and recheck triggers. |
| Revalidation queue | `templates/revalidation-queue.schema.json` | Drift or uncertainty needs prioritized queued work without silently changing the route. |
| Update run and report | `templates/update-run.schema.json` and `templates/update-report.md` | Record update scope, cutoff, accepted/rejected/conflicting changes, unchanged scopes, verification, rollback, and next trigger. |
| Update-record validation | `scripts/validate_update_records.py` | Validate source ledgers, revalidation queues, and update runs before using them for route changes. |
| Portfolio graph contract | `references/portfolio-graph-contract.md` and `templates/portfolio-graph.schema.json` | Represent stable nodes, typed edges, evidence, sources, safety states, and graph invariants. |
| Scenario and what-if planning | `references/scenario-planning.md`, `templates/scenario-manifest.schema.json`, and `templates/scenario-comparison.md` | Compare routes before changing capacity, priorities, domains, deadlines, access, or target depth. |
| Portfolio health | `references/portfolio-health.md` | Diagnose coverage, bottlenecks, bridge leverage, volatility, evidence, update debt, sustainability, and learner-facing complexity. |
| Complexity budgets | `references/complexity-budgets.md` | Keep enormous portfolios usable through staging, indexing, and progressive disclosure. |
| Goal closure and safety propagation | `references/goal-closure-and-safety-propagation.md` | Check every required goal has a credible evidence route and propagate risk only through actual dependencies. |
| Decision provenance and queries | `references/decision-provenance-and-queries.md` and `templates/decision-provenance.schema.json` | Explain route choices and answer targeted portfolio questions from the smallest relevant slice. |
| Decision-record validation | `scripts/validate_decision_records.py` | Validate graph, scenario, provenance, and complexity records before relying on them. |
| Research boundary | `templates/research-brief.md` | Current web research is required and its scope, stable exclusions, source plan, and recheck boundary should be explicit. |
| Freshness tracking | `templates/freshness-ledger.md` | Research materially changes the syllabus and source/date/version/expiry information should be retained. |
| Research synthesis | `templates/research-synthesis.md` | Current sources influence sequencing, prerequisites, tool choices, evidence requirements, or risk boundaries and facts must be separated from instructional judgment. |
| Supported domain grounding | `references/domains/` | The request clearly belongs to software engineering, machine learning/data, or cloud/DevOps. |
| Golden output calibration | `references/exemplars/` | The required output shape is difficult to calibrate or a narrow-versus-comprehensive contrast is useful. |
| Ambiguity triage | `references/clarification-triage.md` | The request is too unconstrained to define a useful destination. |
| Learning science | `references/learning-science.md` | A roadmap needs retrieval, spacing, interleaving, transfer, or calibrated-support guidance. |
| Shortest-route audit | `references/route-audit.md` | A broad, constrained, multi-branch, or revised path needs an auditable minimality and trade-off check. |
| Long-input integration | `references/long-input-integration.md` | The request is a very long wall of text or a portfolio of learning intentions requiring segmentation, family clustering, shared foundations, conflict handling, and staged delivery. |
| Effort and source guidance | `references/effort-and-sources.md` | The user asks how large the work is or where to study from. |
| Visual dependency graph | `templates/learning-map.mermaid.md` | A Mermaid DAG is requested or cross-branch dependencies need visual explanation. |
| Machine-readable export | `templates/learning-map.schema.json` | A downstream tracker, LMS, application, or structured workflow needs JSON, including optional freshness, uncertainty, source references, confidence, and performance-support fields. |
| Durable roadmap progress | `templates/progress.schema.json` and `scripts/validate_progress.py` | The user requests progress-aware replanning or a machine-readable record; validate the record before relying on it. |
| Workspace and adapter metadata | `templates/workspace-manifest.schema.json` | Persistent or portable workspaces need an adapter identity, capability record, lifecycle state, schema version, and current revision. |
| Concurrent edit record | `templates/conflict-record.schema.json` | A stale or concurrently modified workspace cannot be safely merged automatically. |
| Workspace schema checks | `scripts/validate_workspace.py` | Validate representative workspace manifests and conflict records before relying on them. |
| JSON package integrity | `scripts/check_json_syntax.py` | Ensure all bundled schemas and machine-readable templates parse before delivery. |
| Revision/checkpoint history | `templates/revision-record.schema.json` | Record imports, updates, splits, lifecycle changes, stable-ID policy, checkpoints, verification, rollback, and conflict status. |
| Staged very-large input | `templates/ingestion-manifest.schema.json` | Preserve source segments and stable item IDs before designing a route when the request arrives in multiple parts. |
| Relative capacity and concurrency check | `scripts/capacity_model.py` | The user supplies relative effort units and wants a deterministic check of whether selected parallel branches fit capacity; never interpret its output as a completion-time or mastery prediction. |
| Workspace index for linked parts | `templates/workspace-index.md` | A very large or ongoing plan is delivered as an index plus linked phase/family files. |
| Automated package check | `scripts/eval_runner.py` | Package integrity and an evaluation-report scaffold should be generated before manual case scoring. It does not judge model outputs. |
| Package hygiene lint | `scripts/package_lint.py` | Structural revisions need checks for frontmatter, missing references throughout Markdown resources, stale artifacts, cache directories, forbidden root files, and SKILL.md size. |

## Operating principle

Use the smallest resource set that fits the request. Do not expose internal dependency analysis or add schedules, assessments, resources, or domain detail unless the user’s request calls for them. Treat proficiency labels as planning bands, not as formal credentials, and keep claims proportional to observable evidence. For long-horizon work, keep the portfolio architecture stable but make the current frontier, capacity assumptions, volatile-tool revalidation, and review decisions explicit.
