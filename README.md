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


## Latest learning-path-architect improvements

The skill now deliberately starts with the learner’s immediate decision instead of showing its internal technical structure first. For ordinary questions it should provide a plain-language answer, one practical next action, the reason that action comes first, observable evidence of progress, a small recovery step if the learner gets stuck, and a review trigger.

It also now has a final quality check for coverage, prerequisites, evidence, adaptation, safety, uncertainty, and unnecessary complexity. The full portfolio architecture remains available for large requests, but it should not overwhelm a simple question.

The new guidance is stored in:

```text
skill/references/plain-language-response-contract.md
skill/references/plan-quality-check.md
```

The skill’s main file explicitly routes beginner and Freeplane questions to these references. The repository includes a regression test so the main skill remains below the host’s 500-line progressive-disclosure limit and continues to point to the required references.
