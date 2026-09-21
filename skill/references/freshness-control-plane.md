# Freshness Control Plane

Use this reference for large or current multi-domain portfolios. It keeps stable learning architecture separate from changing claims, tools, regulations, research, evidence expectations, and learner context.

## Control-plane records

Maintain a portfolio revision, research cutoff, update-run ID, source registry, source-to-node mappings, volatility class, expiry/recheck triggers, pending revalidation queue, accepted/rejected/conflicting changes, impact summary, and last verified state. A control plane may be a file, database, MCP resource, project workspace, or generated artifact only when that capability is verified.

## Change taxonomy

| Change | Default handling |
|---|---|
| Cosmetic wording | Metadata-only update |
| Equivalent tool replacement | Update resource/tool node and revalidate evidence |
| Deprecation | Mark affected node stale, identify replacement, recompute affected subgraph |
| New capability or paper | Candidate optional/bridge node until relevance and evidence are established |
| Prerequisite shift | Recompute affected dependencies and active frontier |
| Evidence shift | Update milestone evidence; do not rewrite unrelated foundations |
| Safety/regulatory shift | Research authoritative sources and gate affected practice |
| Source correction or conflict | Preserve conflict, contextualize it, and revise only affected claims |
| Learner goal/context change | Re-run prioritization and route impact analysis |

A change is also labeled informational, structural, route-changing, safety-critical, or unresolved. New does not mean required, and different does not automatically mean better for this learner.

## Update modes

Use no-current-claims mode only for explicitly timeless abstract requests. Use targeted refresh for named claims/tools, domain refresh for one family and its bridges, portfolio drift scan for source/expiry flags across domains, and full portfolio review only for a north-star, horizon, role, regulatory, safety, or major context change. State research scope and cutoff.

## Honest automation

Automatic monitoring exists only when the environment exposes and verifies a schedule, subscription, connector, MCP capability, or persistent process. Otherwise provide a next drift-scan trigger or invocation instruction. Never claim that a portfolio is being monitored in the background when it is not.
