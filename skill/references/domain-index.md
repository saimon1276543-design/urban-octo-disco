# Domain Module Index

Use this index to select one or more concrete domain modules without loading the entire domain library. If a request spans domains, load only the modules that affect the requested outcomes.

| Signals in the request | Module | Use for |
|---|---|---|
| Applications, APIs, architecture, testing, software delivery, debugging, services, production code | `domains/software-engineering.md` | Software construction, system design, testing, and operational readiness |
| Datasets, prediction, modeling, statistics, features, neural networks, evaluation, data pipelines | `domains/machine-learning-data.md` | Data analysis, modeling, evaluation, and ML operations |
| Cloud, infrastructure, containers, deployment, Terraform-like workflows, CI/CD, reliability, platform operations | `domains/cloud-devops.md` | Infrastructure automation, delivery systems, and platform operations |

If no bundled module matches the request, use **Generic path — no bundled module**: apply the core workflow, select the appropriate freshness mode, and record the domain as a candidate for a future reference rather than silently implying coverage. Do not treat a signal as proof that every module section is required. Map the user’s actual outcome first, then use the module only to improve prerequisites, traps, evidence, and boundaries.
