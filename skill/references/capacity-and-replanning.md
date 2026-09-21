# Capacity and Periodic Replanning

Use this reference for any roadmap where time, energy, competing commitments, concurrency, sustainability, or repeated review matters. Model capacity as a changing operating constraint, not as a single hours-per-week number.

For a practical implementation, copy `templates/learning-observation-tracker.md` or create a record conforming to `templates/observation-tracker.schema.json`. After each bounded cycle, record the planned and actual values; at the stated review trigger, run `scripts/recalibration_report.py` or perform the same calculations manually. The tracker is the bridge between the roadmap’s assumptions and the next revision.

## 1. Separate capacity layers

Record the following separately:

| Layer | Meaning | How to use it |
|---|---|---|
| Nominal availability | Time the learner says may be available | Upper bound, not guaranteed study time |
| Reliable availability | Portion usually protected from obligations | Use for the base route |
| Learning capacity | Reliable availability after setup, recovery, and switching overhead | Use for branch selection |
| Cognitive capacity | Amount of difficult novelty the learner can sustain | Limit simultaneous high-load branches |
| Maintenance load | Effort needed to retain completed capabilities | Reserve before adding branches |
| Recovery reserve | Buffer for illness, interruptions, life events, and underestimation | Keep unallocated unless the learner asks for aggressive pacing |

Never convert nominal time directly into mastery claims. If the learner supplies only hours, ask or infer a conservative reliability range and mark confidence.

## 2. Model usable capacity

A useful relative model is:

`usable capacity = nominal availability × reliability × learning fraction − fixed overhead − switching load − maintenance load − recovery reserve`

Use ranges when inputs are uncertain. Fixed overhead includes setup, commuting, environment repair, resource discovery, and administrative work. Switching load grows with the number of active branches and their context distance. Maintenance load belongs to completed capabilities that the learner must keep usable.

Represent each factor as a relative value or band, not false precision. If the learner supplies actual observations, prefer them over generic assumptions. Keep the model transparent: show which values are stated, observed, inferred, or unknown.

## 3. Model cognitive load and branch fit

For each active branch, record:

- novelty or cognitive-load band;
- setup friction;
- switching cost;
- minimum viable practice continuity;
- maintenance need;
- dependency readiness;
- whether it reinforces or competes with another branch.

A branch can be calendar-parallel but not cognitively parallel. Do not activate several high-novelty branches merely because their prerequisites are independent. Prefer one high-load primary branch plus a low-load maintenance, retrieval, writing, or transfer branch unless the learner has demonstrated sustainable concurrency.

## 4. Calibrate from observed progress

After at least a small amount of real work, compare planned versus observed effort and evidence:

- completion ratio;
- blocked-node frequency;
- interruption frequency;
- average recovery time after a missed cycle;
- retention or transfer results;
- number of active branches actually sustained;
- evidence quality and independence;
- repeated setup or context-switch cost.

Use a robust trend, such as a median or conservative lower band, rather than a single unusually good or bad cycle. If observed throughput is consistently below the assumed capacity, reduce scope or concurrency before extending the learner’s burden. If it is consistently above assumptions and evidence quality remains strong, expand only one dimension at a time.

Do not use completion speed alone to infer learning. A fast completion with weak transfer should reduce confidence in capacity for that branch.

### Minimum practical log

At minimum, each cycle needs: planned effort, actual effort, planned units, completed units, sessions planned/completed, interruptions, recovery units, blocker count, whether a blocker repeated, branches planned/sustained, switching cost, retention/transfer evidence, evidence quality, and the reason for material variance. Missing values should be marked unknown rather than silently treated as zero.

## 5. Choose concurrency deliberately

Treat the learner’s requested parallel limit as a preference subject to feasibility. Evaluate each candidate set by:

1. hard prerequisites met;
2. total usable effort load;
3. cognitive-load sum;
4. switching and setup cost;
5. maintenance obligations;
6. reinforcement or competition between branches;
7. evidence deadlines or urgency;
8. sustainability confidence.

If the set fails, keep the priority order and explain the smallest reduction: reduce branch count, defer a volatile tool, narrow scope, lower target depth, or extend the horizon. Do not silently remove a named goal.

## 6. Define review cadence without fabricating a calendar

Use two kinds of reviews:

- **Event review:** immediately after a milestone passes or fails, a capacity shock, a goal/context change, a blocker, a safety/freshness change, or a conflict.
- **Periodic review:** after a bounded amount of evidence or a user-supplied interval. If no interval is supplied, define the trigger relatively, such as “after two completed cycles,” “after the next phase exit,” or “when three attempts expose the same blocker.”

A review is due when the route assumptions are no longer trustworthy, not merely because a date arrived.

## 7. Use a fixed review sequence

At every review:

1. **Collect:** current node states, evidence provenance, observed effort, interruptions, blockers, capacity changes, and external changes.
2. **Check evidence:** decide whether the exit criterion was met in the required performance context; mark evidence as verified, self-reported, stale, or conflicting.
3. **Calibrate:** update capacity, cognitive-load, switching-cost, and concurrency assumptions from observations.
4. **Recompute:** refresh dependencies, unlocked nodes, active frontier, maintenance obligations, and volatile-tool revalidation.
5. **Decide:** for each family choose continue, advance, remediate, maintain, narrow, defer, replace, retire, or split.
6. **Explain:** record what changed, why, what remains stable, and what becomes available or blocked.
7. **Commit:** write a checkpointed revision only after verification; preserve the last known-good plan if the update fails.
8. **Expose:** show the learner the current primary action, optional parallel action, next evidence, and next review trigger.

The review record should preserve the observed summary, smallest failing assumption, decision, route impact, next primary action, and next review trigger. Do not overwrite the historical cycle log when recalibrating; append a new review and update only the current assumptions.

## 8. Replanning decision rules

- **Advance:** exit evidence is met and the next node is feasible under current capacity.
- **Remediate:** evidence fails or a repeated blocker identifies the smallest missing prerequisite.
- **Narrow:** the outcome remains valid but the current scope exceeds usable capacity.
- **Maintain:** capability is complete but later goals depend on retained fluency.
- **Defer:** the branch is valuable but not currently justified by priority, readiness, capacity, or route leverage.
- **Replace:** a tool, route, or project no longer serves the north star; preserve the capability target.
- **Retire:** the learner explicitly abandons the outcome or it is no longer relevant; preserve history and rationale.
- **Split:** one branch contains incompatible effort, proficiency, or context requirements.
- **Pause:** capacity or life context temporarily prevents reliable progress; protect evidence and define a resume trigger.

Never respond to uncertainty by adding more topics. Reduce the smallest failing assumption first.

## 9. Plan for shocks and recovery

When capacity drops temporarily, protect the north star and completed evidence. Move to maintenance or a minimum viable action, defer optional branches, and reserve recovery time. When capacity returns, do not immediately restore all deferred branches; re-estimate using observed recovery and current constraints.

When capacity is volatile, use a base route plus optional expansion nodes. When the learner repeatedly overestimates capacity, lower the planning band and increase reserve rather than treating the learner as undisciplined.

## 10. Report uncertainty honestly

Every capacity-sensitive roadmap should distinguish stated, observed, inferred, and unknown values. Avoid exact completion dates unless the learner requests calendar planning and supplies adequate data. The purpose of the model is to choose a sustainable next action and detect when the route must change—not to manufacture certainty.
