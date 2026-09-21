# Freeplane Interoperability

Use this reference when producing or updating Freeplane maps from a learning workspace.

## Roles

The structured workspace is the authoritative learning record. Freeplane is the visual interface: the master map, detailed maps, node notes, connectors, formulas, and cross-map hyperlinks.

## Map structure

```text
maps/
├── master-learning-map.mm
├── mathematics.mm
├── programming.mm
└── map-index.json
```

The master map should link to the root or relevant node of each detailed map. Each detailed map should include a “Back to master map” link where practical. Use relative file links so the folder can be moved to another computer.

## Stable identity

Preserve a node's stable ID when changing its title or position. If a map node has no stable ID, create one during import and record the mapping. Never use a title as the permanent identity because titles can change and can repeat.

## Notes and formulas

Keep visible node titles short. Put explanations, examples, evidence, and learner notes in the node note. Preserve rich text where the format allows it. Do not discard formulas, links, or notes merely to simplify a map export; if a conversion cannot preserve something, report it.

## Hosted export

The hosted environment can generate or update `.mm` files and provide them as downloadable artifacts. It cannot claim to control a running Freeplane desktop application unless a verified local or remote MCP connection exists.

Use `scripts/workspace_to_freeplane.py` for a deterministic basic export from a JSON node list. Use `scripts/freeplane_to_workspace.py` for a basic import back into a structured node list. These scripts preserve the core hierarchy, node IDs, notes, and ordinary hyperlinks; complex Freeplane styling should be treated as user-owned content and checked after an update.

## Validation

Before delivery, open the generated map in Freeplane and check the master map, at least one detail map, notes, formulas, and cross-map links. Use `scripts/validate_freeplane_links.py` for basic file-target checks when links use local paths.
