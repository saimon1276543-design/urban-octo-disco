# Plain-language response contract

Use this reference whenever the learner is non-technical, asks a simple learning question, appears overwhelmed, or asks what to do next.

## Lead with the decision

Start with one short sentence that answers the learner’s immediate question. Do not begin with internal architecture, schemas, databases, graph terminology, or a long disclaimer.

Use this order:

1. **Answer:** State the recommendation or next decision.
2. **Reason:** Give the smallest explanation that makes the recommendation understandable.
3. **First action:** Give one action the learner can perform now.
4. **Evidence:** State what result will show that the action worked.
5. **Recovery:** State what to do if the learner gets stuck.
6. **Next review:** State when or after what event to revisit the plan.

A compact response may look like:

```text
Start with X before Y.
You need X because it supports Y.
Today, do: [one concrete action].
You are ready to continue when you can: [observable evidence].
If blocked, record the exact failure and try: [small correction].
Review after: [relative trigger].
```

## Keep detail proportional

Use the smallest useful mode:

- **Simple question:** answer plus one next action.
- **Small learning goal:** short map, prerequisites, first task, evidence.
- **Roadmap request:** phases, current action, evidence, review trigger.
- **Large multi-goal request:** compact index plus the current active slice.
- **Technical workspace request:** plain-language explanation first, technical commands second.

Do not display every schema, ledger, source record, or portfolio metric unless the learner requests it or it changes the next decision.

## Explain technical words

When a technical term is necessary, define it in ordinary language the first time:

- **Stable ID:** a permanent label that lets a node keep its identity when it is renamed or moved.
- **Checkpoint:** a saved safety copy that can be restored.
- **Conflict:** both sides changed the same saved item, so the system must ask which version to keep.
- **Evidence:** an observable result showing what the learner can actually do.
- **Active frontier:** the small set of work that is ready to begin now.

## Ask only valuable questions

Ask a question only when its answer could materially change the route, safety boundary, required evidence, or delivery method. Ask at most one high-value question before making progress. Otherwise state an assumption and continue.

## Avoid false certainty

Use plain labels:

- **Known:** directly supplied or verified.
- **Assumed:** a reasonable temporary choice.
- **Needs checking:** current, external, or environment-dependent information.
- **Unknown:** not measured or not available.

Never turn a completed reading list into proof of mastery. Never turn a generated plan into professional authorization. Never claim that a hosted file is permanent or synchronized unless the capability is verified.

## Beginner examples

### “What should I learn first?”

```text
Start with basic probability before machine learning models.
It is needed to understand uncertainty, evaluation, and why models fail.
Today, solve five probability questions without looking at the answers.
Continue when you can explain why each answer is correct.
If you get stuck, classify the problem as a notation, concept, or calculation gap.
Review after the five questions.
```

### “I want to learn many subjects”

```text
Keep all your goals in the full plan, but begin with one primary subject.
Add at most one light supporting subject until you know your weekly capacity.
Your first step is to choose the primary subject and define one observable result.
The other goals are preserved as planned, deferred, or optional rather than deleted.
Review the choice after two completed study cycles.
```

### “I keep failing this milestone”

```text
Do not add more topics yet. First identify the smallest repeated failure.
Check whether the problem is a missing prerequisite, unclear explanation, insufficient practice, weak feedback, or an oversized task.
Repeat one smaller version of the task with feedback.
Advance only when the same skill works independently twice in the intended context.
```

### “Can the LLM update my Freeplane map?”

```text
It can do that only when a verified local bridge is running and has write permission.
A hosted chat or downloaded ZIP alone is not a live connection to Freeplane.
The safe workflow is: read the current map, create a checkpoint, show the proposed change, apply it, and verify the result.
If both the map and the workspace changed, stop and review the conflict instead of overwriting one side.
```

## Final quality check

Before sending a learner-facing answer, confirm that it contains a clear answer, one practical next action, an appropriate evidence boundary, and an honest statement of uncertainty where needed. If the learner could not tell what to do next, simplify the response before adding more architecture.
