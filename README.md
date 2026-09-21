# Freeplane Learning Workspace Bridge

This repository adds a small, local, no-code-oriented bridge for a Freeplane learning workspace. Freeplane remains the visual editor. The bridge mirrors Freeplane `.mm` maps into structured JSON, creates checkpoints, detects concurrent edits, and exposes a localhost MCP-style HTTP endpoint for an LLM client.

## Current status

This is the first verified foundation. It supports:

- Freeplane XML map parsing and generation
- Stable node IDs and hierarchy round trips
- Notes and basic node metadata
- Map-to-workspace and workspace-to-map synchronization
- Atomic JSON writes
- Checkpoints before synchronization and restore
- Conflict records when both sides changed since the last sync
- Saved-state undo/redo using revision folders
- A localhost-only MCP-style endpoint with read/status, sync, and checkpoint tools
- The updated `learning-path-architect` package under `skill/`

Native Freeplane in-session undo/redo remains owned by Freeplane. The bridge deliberately does not rewrite the open map during ordinary editing. Saved-state history is separate and retains recoverable revisions; the bridge keeps the latest ten redo entries and all created checkpoint folders until cleanup.

## Quick start on Windows

Install Python 3.11+ and Freeplane first. In PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m freeplane_sync.cli init --workspace C:\LearningWorkspace
```

Copy or create Freeplane maps under `C:\LearningWorkspace\maps`, then import them:

```powershell
python -m freeplane_sync.cli import --workspace C:\LearningWorkspace
```

After an LLM-side workspace change, export it back to Freeplane:

```powershell
python -m freeplane_sync.cli export --workspace C:\LearningWorkspace
```

Watch for map changes:

```powershell
python -m freeplane_sync.watch --workspace C:\LearningWorkspace
```

Create a local MCP endpoint:

```powershell
python -m freeplane_sync.mcp_server --workspace C:\LearningWorkspace --token CHANGE-ME
```

The endpoint is deliberately bound to `127.0.0.1`, not the public network:

```text
http://127.0.0.1:6299/mcp
Authorization: Bearer CHANGE-ME
```

## Revision controls

```powershell
python -m freeplane_sync.cli undo --workspace C:\LearningWorkspace
python -m freeplane_sync.cli redo --workspace C:\LearningWorkspace
```

Restores are checkpointed first, so the current state is not discarded silently.

## Hosted mode

The hosted LLM environment can generate and revise `workspace.json` and `.mm` files, then export the entire folder as a ZIP. It cannot live-sync with Freeplane until the local bridge is running on the user’s computer. This limitation is intentional and is recorded in the workspace design.

## Limitations of this first release

- It is not yet a full native MCP SDK implementation; it provides a small authenticated JSON-RPC HTTP bridge for the initial local workflow.
- Freeplane visual-only details such as complex styles, floating positions, and connector styling require a later preservation layer.
- Changes should be synchronized after saving a map; the watcher is near-real-time, not a collaborative editor.
- Conflicts are recorded and stop automatic synchronization rather than being silently merged.
- The repository does not store model/API keys.
