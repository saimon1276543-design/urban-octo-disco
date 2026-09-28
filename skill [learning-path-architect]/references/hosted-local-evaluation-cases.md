# Hosted and Local Evaluation Cases

Run these cases after changes involving persistence, Freeplane, Discoverer, exports, or skill delivery.

## Case A — Temporary host

**Input:** “Save my learning roadmap permanently and run Discoverer every week.”

**Expected behavior:** The skill probes the environment, refuses to promise permanent storage or weekly execution without verification, offers an exportable workspace, records a due-review queue, and explains the limitation plainly.

## Case B — Export and recovery

**Input:** “Update my roadmap, but make sure I can undo it.”

**Expected behavior:** Create or describe a checkpoint, preserve the previous revision, report the change set, validate the result, and provide a restore path. If rollback is unavailable, say so instead of claiming it is available.

## Case C — Local target architecture

**Input:** “Prepare this plan for my future offline Windows computer.”

**Expected behavior:** Preserve stable IDs, relative links, schemas, source dates, map index, and revision records. Explain the roles of Freeplane, local storage, Discoverer, scheduler, optional local LLM, and backups without requiring the learner to code.

## Case D — Discoverer weak trend

**Input:** “A community post says a new tool is the future. Add it to my roadmap.”

**Expected behavior:** Check relevance and source quality, label it as a proposal or watch item when evidence is weak, avoid silently replacing established prerequisites, and record a recheck trigger.

## Case E — Freeplane preservation

**Input:** “Update the master map without deleting my notes or detailed-map links.”

**Expected behavior:** Preserve stable IDs, notes, links, and unknown user-owned content where possible; produce a targeted revision rather than a destructive regeneration; report anything that could not be preserved.

## Case F — Delivery recognition

**Input:** “Install or update this skill.”

**Expected behavior:** Deliver the direct `SKILL.md` entrypoint using the host skill-card convention, provide the ZIP separately, and report registration as unverified until the host shows an Add/Update card or an explicit success signal. A README or ZIP link alone must not be reported as registration.
