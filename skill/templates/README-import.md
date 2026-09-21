# Learning Workspace Import Guide

This folder contains a portable learning workspace.

## Open the visual maps

Open `maps/master-learning-map.mm` in Freeplane. Follow the links from the master map to detailed maps in the same `maps/` folder. If a link does not work after moving the folder, use the map index and recreate it with relative paths.

## What is authoritative

The structured workspace records are the durable planning and progress record. Freeplane is the visual map and navigation layer. Do not delete structured records merely because the map looks correct.

## Restore safely

1. Copy the entire workspace folder to a new location.
2. Check `workspace-manifest.json`.
3. Open the master map.
4. Test one detailed-map link.
5. Keep the original folder as a backup until the copy is verified.

## Update history

Use the files under `revisions/` to understand what changed. Restore the previous revision rather than manually guessing which files to replace.

## Privacy

If this workspace was created by a hosted LLM, its contents may have been sent to that provider. For fully local use, store it locally and use a local AI runtime.
