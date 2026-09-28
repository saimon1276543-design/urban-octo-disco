# Hosted and Offline Workspace Modes

Use this reference whenever a learner wants the learning portfolio to survive across sessions, move between AI tools, or work with Freeplane.

## Plain-language rule

The workspace is the learner's saved learning folder. Freeplane is the visual map. The learning-path-architect skill is the planning and progress method. An LLM may read or update the workspace only when the current host exposes verified read/write access.

Never say that a plan was permanently saved unless the host confirms persistence. Distinguish:

| Mode | Meaning | Safe claim |
|---|---|---|
| Persistent workspace | The host keeps the files available across sessions | “Saved in the workspace.” |
| Session workspace | Files exist only for the current task/session | “Created for this session.” |
| Export-only | Files can be downloaded but persistence is not guaranteed | “Ready to download.” |

## Recommended workspace

```text
learning-workspace/
├── workspace-manifest.json
├── maps/
│   ├── master-learning-map.mm
│   └── map-index.json
├── portfolio/
├── learner/
├── progress/
├── sources/
├── revisions/
└── README-import.md
```

Keep the authoritative planning and progress records in structured workspace files. Use Freeplane maps for visual navigation, notes, hyperlinks, and presentation. Do not make a generated map the only copy of the learner's progress.

## Safe update sequence

Read the current workspace, create a checkpoint when possible, propose material changes, apply only validated changes, verify the files and links, and record the new revision. Never silently overwrite a learner's notes or change goals, prerequisites, evidence, permissions, or safety boundaries.

## Hosted mode

In a hosted LLM environment, probe the host before promising persistence. Check whether files can be written, read back, exported, and reopened later. If recurring jobs are unavailable, run freshness checks when the learner asks for them and say so plainly.

## Offline mode later

On the learner's PC, place the workspace in a backed-up local folder, install Freeplane, open the maps, and verify the cross-map hyperlinks. A local LLM and Freeplane MCP are optional additions for fully offline AI. Keep the workspace portable so it can be moved without rebuilding the learning plan.

## User-facing commands

Support simple requests such as:

- “Save this roadmap.”
- “Show what changed.”
- “Undo the last update.”
- “Export my complete learning workspace.”
- “Check whether my workspace is still available.”
- “Prepare this workspace for my offline computer.”

Technical adapter details belong in the manifest and internal records, not in every user response.

## Privacy boundary

If the LLM is hosted, map contents, notes, progress, and source records may be sent to the model provider when requested. A fully offline guarantee requires both local storage and a local model or another explicitly local AI runtime.

## Required references and templates

Use `templates/workspace-manifest.schema.json`, `templates/hosted-workspace-manifest.example.json`, `templates/map-index.schema.json`, and `templates/README-import.md` when creating or exporting a workspace. Use `references/freeplane-interoperability.md` for map generation and cross-map links.
``` 
