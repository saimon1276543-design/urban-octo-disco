# Machine Learning and Data Domain Module

Use this module when the request includes data analysis, machine learning, model development, or production data workflows.

## Common prerequisite branches

| Outcome | High-confidence foundations | Context-dependent additions |
|---|---|---|
| Analyze data reliably | Programming, data structures, tabular manipulation, visualization, uncertainty | Statistics depth, domain knowledge, SQL, distributed processing |
| Build predictive models | Data preparation, probability and statistics, validation, feature reasoning, baseline modeling | Linear algebra, optimization, deep learning, specialized modalities |
| Operate models responsibly | Reproducible pipelines, monitoring, evaluation design, data governance | MLOps platform, privacy, fairness review, regulated controls |

## Evaluation safeguards

Require a baseline, a clearly defined target, an appropriate split strategy, leakage checks, metric justification, error analysis, and a statement of where the model should not be trusted. Distinguish offline validation from real-world performance. Do not treat a high metric on a flawed split as evidence of competence.

## Data-pipeline patterns

Separate data acquisition, quality checks, transformation, feature or representation construction, training, validation, packaging, monitoring, and rollback. Add distributed systems or streaming only when the requested scale or latency requires them.

## Common traps

Check for target leakage, selection bias, unrepresentative samples, metric gaming, class imbalance, spurious correlations, overfitting, data drift, and confusing correlation with causal evidence. Place only the relevant trap checks in the map.

## Evidence by level

| Level | Suitable evidence context |
|---|---|
| Novice | Guided analysis with a documented dataset, baseline, and interpretation |
| Advanced Beginner | Independent familiar dataset workflow with validation and error review |
| Competent | Bounded unfamiliar dataset with defensible evaluation and reproducible pipeline |
| Proficient | Ambiguous modeling problem with trade-offs, robustness analysis, and deployment constraints |
| Expert | Novel modeling or evaluation judgment, explicit limitations, and authoritative technical communication |
