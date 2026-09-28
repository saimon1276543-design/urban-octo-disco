# Freeplane Learning Workspace

This project helps keep a Freeplane mind map and the learning records used by the `learning-path-architect` skill together.

You do **not** need to understand the source code. You use Freeplane normally. The helper files quietly make backups and keep a saved copy of the learning information.

## The simple picture

```text
You edit your map in Freeplane
              ↓
The helper saves a matching learning record
              ↓
An LLM can read or update the saved record
              ↓
The helper can update the Freeplane map
```

Freeplane is still the mind-map application. This project is only the connecting helper.

## Current status: working foundation

This repository is a **working foundation**, not the completed offline learning platform. The current foundation provides the basic connection between Freeplane maps, saved learning records, backups, revisions, conflicts, and the local connection point. It is useful for testing and extending the workflow, but several larger capabilities are still future work.

The complete future system is intended to add a local evidence database, project-submission intake, deterministic project checks, bounded LLM evaluation, mistake memory, spaced review, parallel evaluation agents, automatic roadmap proposals, a Freeplane add-on, a dockable side panel, and optional time tracking. These capabilities should not be considered available merely because they are described in the repository or in `OFFLINE_IMPLEMENTATION_TODO.md`.

Use this README as the guide for what the current repository can do. Use [`OFFLINE_IMPLEMENTATION_TODO.md`](OFFLINE_IMPLEMENTATION_TODO.md) as the detailed engineering checklist for what must be built and verified later.

## What is already included

- Freeplane map reading and writing.
- Parent, child, and branch movement support.
- Node names and notes.
- Basic workspace-to-map and map-to-workspace updates.
- Backups before important changes.
- Conflict detection when both sides changed the same saved work.
- Saved versions with undo and redo.
- The latest ten saved versions are retained for saved-state recovery.
- A local, password-protected LLM connection point.
- Windows double-click setup files.
- The updated learning-path-architect skill package.

## Quick setup on Windows

Install **Freeplane** and **Python 3.10 or newer** first.

Then download this repository and double-click:

```text
setup.bat
```

The setup creates your workspace here:

```text
C:\Users\YOUR-NAME\LearningWorkspace
```

Put your Freeplane `.mm` files inside:

```text
C:\Users\YOUR-NAME\LearningWorkspace\maps
```

Then double-click:

```text
start-sync.bat
```

Leave that window open while you work. It watches for saved changes.

## What you normally do

1. Open your map in Freeplane.
2. Edit it as usual.
3. Save it in Freeplane.
4. Leave the synchronization window running.
5. The helper creates or updates the matching saved learning record.

You do not need to edit `workspace.json` yourself.

## If an LLM needs access

Start the local connection point with:

```powershell
python -m freeplane_sync.mcp_server --workspace C:\Users\YOUR-NAME\LearningWorkspace --token CHANGE-ME
```

It listens only on your own computer:

```text
http://127.0.0.1:6299/mcp
```

The token is like a password. Keep it private. Do not put it in GitHub or send it to other people.

The LLM connection can be given reading access first. Only enable writing after you are comfortable with the backup and conflict behavior.

## Simple commands

If you prefer commands instead of double-clicking files, open PowerShell in this project folder.

Create the workspace:

```powershell
python -m freeplane_sync.cli init --workspace C:\Users\YOUR-NAME\LearningWorkspace
```

Import saved Freeplane maps into the learning workspace:

```powershell
python -m freeplane_sync.cli import --workspace C:\Users\YOUR-NAME\LearningWorkspace
```

Send workspace changes back into Freeplane maps:

```powershell
python -m freeplane_sync.cli export --workspace C:\Users\YOUR-NAME\LearningWorkspace
```

Create a manual backup:

```powershell
python -m freeplane_sync.cli backup --workspace C:\Users\YOUR-NAME\LearningWorkspace
```

See saved versions:

```powershell
python -m freeplane_sync.cli revisions --workspace C:\Users\YOUR-NAME\LearningWorkspace
```

Restore the previous saved version:

```powershell
python -m freeplane_sync.cli undo --workspace C:\Users\YOUR-NAME\LearningWorkspace
```

Redo the last restoration:

```powershell
python -m freeplane_sync.cli redo --workspace C:\Users\YOUR-NAME\LearningWorkspace
```

See conflicts:

```powershell
python -m freeplane_sync.cli conflicts --workspace C:\Users\YOUR-NAME\LearningWorkspace
```

## What happens if both sides changed

The helper will not silently choose a version. It records a conflict and stops the automatic update.

For example:

```text
The same node was changed in Freeplane and by the LLM.
Please choose which version to keep.
```

Keep a backup before resolving the conflict. The current first version reports conflicts in a file; a later version will provide a more visual conflict-review screen.

## Undo and redo

There are two kinds of undo:

### Normal editing in Freeplane

Freeplane controls its own normal Undo and Redo buttons. The helper does not replace those controls.

### Saved-workspace recovery

The helper keeps saved snapshots separately. It can restore the previous saved state and redo that restoration. It keeps at least the latest ten saved workflow versions.

This means the helper does not promise to recreate Freeplane’s native unsaved undo history after Freeplane has been closed. Freeplane’s own undo system and the helper’s saved backups are two separate safety nets.

## Hosted LLM use

A hosted LLM can create or revise a downloadable workspace and Freeplane maps. That hosted environment should be treated as a temporary workshop unless it explicitly confirms that it has permanent storage.

When you move to your own computer, download the complete workspace ZIP and keep it as a backup. Live synchronization with Freeplane happens only when the local helper is running on your computer.

## Skill package

The `skill/` folder contains the learning-path-architect skill. Its main file is:

```text
skill/SKILL.md
```

The host’s Add/Update card is generated only when the active skill is delivered from its recognized skill path. A GitHub repository or ZIP file is a backup and transport method; it is not automatic installation.

## What is not finished yet

This is a working foundation, not a polished commercial product. Future improvements include:

- Better preservation of advanced Freeplane styling and connector appearance.
- A full standard MCP implementation tested with a real LLM client.
- A visual conflict-resolution screen.
- A polished one-click installer.
- More tests using real complex Freeplane maps.
- A guided import/export wizard.

Until those improvements are complete, keep regular backups of the whole `LearningWorkspace` folder.

## Future offline implementation checklist

The detailed future work is documented separately in [`OFFLINE_IMPLEMENTATION_TODO.md`](OFFLINE_IMPLEMENTATION_TODO.md). It covers the local database, evidence intake, deterministic checks, bounded LLM evaluation, mistake memory, review scheduling, parallel evaluation, roadmap proposals, Freeplane add-on, side panel, time tracking, security, recovery, and acceptance tests.

The workflow diagram is available as the editable Mermaid source [`OFFLINE_IMPLEMENTATION_WORKFLOW.mmd`](OFFLINE_IMPLEMENTATION_WORKFLOW.mmd) and as [`OFFLINE_IMPLEMENTATION_WORKFLOW.png`](OFFLINE_IMPLEMENTATION_WORKFLOW.png).


## Latest learning-path-architect improvements

The skill now deliberately starts with the learner’s immediate decision instead of showing its internal technical structure first. For ordinary questions it should provide a plain-language answer, one practical next action, the reason that action comes first, observable evidence of progress, a small recovery step if the learner gets stuck, and a review trigger.

It also now has a final quality check for coverage, prerequisites, evidence, adaptation, safety, uncertainty, and unnecessary complexity. The full portfolio architecture remains available for large requests, but it should not overwhelm a simple question.

The new guidance is stored in:

```text
skill/references/plain-language-response-contract.md
skill/references/plan-quality-check.md
```

The skill’s main file explicitly routes beginner and Freeplane questions to these references. The repository includes a regression test so the main skill remains below the host’s 500-line progressive-disclosure limit and continues to point to the required references.


## Phase 0 capstone foundation

The repository now contains the first contracts for the future capstone workflow. These are definitions and safety rules; they do not yet run an autonomous swarm or change Freeplane automatically.

The planned flow is:

```text
learning-path-architect creates the assignment
        ↓
you place the project in an authorized folder
        ↓
the bridge records files and hashes
        ↓
later evaluators inspect bounded evidence units
        ↓
results, mistakes, and future reviews are saved
        ↓
Freeplane shows a concise, reversible progress update
```

Phase 0 defines six records:

```text
skill/templates/capstone.schema.json
skill/templates/submission-manifest.schema.json
skill/templates/evaluation-result.schema.json
skill/templates/mistake-memory.schema.json
skill/templates/review-event.schema.json
skill/templates/permission-policy.schema.json
```

The permission policy is intentionally conservative. “Full project access” means access to the project folder that you explicitly authorize, not unrestricted access to the entire computer. Official records and Freeplane updates are designed to require confirmation in the first versions.

A recurring mistake can later create a small linked review item in the roadmap. The original capability node and history remain intact. Available time will initially be entered manually; a future time-tracker adapter can provide observed capacity without replacing the learning database.


## Hosted-only improvements

The skill now has a clear hosted-session boundary. It can design assignments, inspect material supplied in the current session, create portable records, and propose roadmap updates. It does not pretend to watch offline work, access arbitrary local folders, send background reminders, control a running Freeplane application, or maintain a permanent database without a verified integration.

Time estimates now separate focused effort, practical session length, full learning cycle, calendar range, and deadline feasibility. Non-trivial estimates use low/typical/high ranges, explicit capacity assumptions, uncertainty, recovery reserve, and a calibration task. A time estimate is a planning range, not a promise of mastery.

New portable templates are available under `skill/templates/` for hosted capstones, time plans, and progress views.


## Diagnostic-first improvement

The skill now diagnoses before expanding a learning route. When a learner is stuck, late, or submits weak evidence, it should use a small representative pilot to distinguish a prerequisite gap, practice gap, feedback problem, scope problem, time-estimation error, transfer problem, or retention problem. It then chooses the smallest intervention and preserves the reason for any route change in a portable decision record.


## Network API interception encyclopedia

The skill now includes a dedicated reference for authorized network-API interception in scraping and browser debugging. It consolidates request discovery, XHR/fetch, GraphQL, WebSocket, SSE, service workers, CDP Fetch, Playwright routing, Puppeteer interception, Selenium/CDP limits, HAR/fixture replay, provenance, redaction, rate limits, and authorization boundaries.
