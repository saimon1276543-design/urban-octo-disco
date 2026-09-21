# Capability Ontology and Proficiency

Use this reference when the learner asks what to learn first, how deep to go, whether they are ready, or how to prove capability.

## Capability record

Represent a capability with a stable ID, canonical name, observable outcome, domain/subdomain, target context, conceptual and performance prerequisites, required environment, proficiency target, evidence requirements, maintenance behavior, safety/authorization boundary, volatile overlays, bridge relationships, and route state.

An outcome should describe what the learner can reliably do, not a topic they have seen. Example: “Diagnose a reproducible browser-network failure using DevTools and record a minimal repair” is a capability; “Chrome DevTools” is a subject label.

## Common progression

| Level | Meaning | Minimum evidence pattern |
|---|---|---|
| Awareness | Recognizes vocabulary and purpose | Accurate classification and examples |
| Conceptual | Explains principles, constraints, and trade-offs | Worked reasoning or teach-back |
| Guided practice | Performs a bounded task with support | Guided artifact plus corrections |
| Independent | Performs a bounded task without step-by-step help | Reproducible artifact and validation |
| Debugging/optimization | Diagnoses failure and improves behavior | Failure analysis, tests, measurements |
| Systems integration | Connects components under constraints | Integration artifact and interface evidence |
| Production/research | Operates or investigates reliably in a defined context | Runbook/experiment, governance, monitoring, recovery |
| Review/leadership | Evaluates work and teaches decisions | Design review, critique, and risk judgment |

Levels are contextual. Independent Python scripting does not unlock independent distributed systems, clinical neurology, or secure production operations. A learner can hold different levels across contexts and can have stale or contradicted evidence.

## Evidence states

Use exposure, guided, practiced, independent, transferable, retained, maintained, stale, contradicted, and unknown. Record evidence date, context, support allowed, confidence, limitations, and next recheck. Time spent, topic count, tutorial completion, or one polished artifact is insufficient by itself.

## Progression decision

Unlock only the capability and context actually tested. If evidence is weak, identify the smallest gap and assign a proportional diagnostic or practice task. Keep higher-level branches deferred when a hard prerequisite, safety gate, or operational dependency is not met.
