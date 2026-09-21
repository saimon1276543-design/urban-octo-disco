# Release and synchronization protocol

Use this reference when a learner reports that an installed skill is stale, the downloaded size differs from the workspace package, an update card did not appear, or a portable package must be transferred between harnesses.

## Release layers

Keep four layers distinct:

1. **Authoritative workspace** — the files currently edited and validated at the active skill path.
2. **Portable artifact** — a ZIP or equivalent package generated from that workspace.
3. **Registered skill** — the version accepted by the host’s skill registry or “My Skills” store.
4. **Client download/cache** — the copy a desktop or mobile client currently offers or has cached.

A successful workspace edit does not prove that the registered skill or client cache changed. A successful ZIP download does not prove that the ZIP was registered. Never claim that a registry update occurred unless the host exposes an explicit success signal.

## Release identity

Give each material package a release identity containing:

- skill name;
- release label or UTC timestamp;
- normalized file count and total bytes;
- SHA-256 fingerprint of the package;
- SHA-256 fingerprints of `SKILL.md` and the release manifest;
- capability markers naming the changed resources;
- validation status and validation timestamp.

Use normalized relative paths, exclude generated caches and compiled files, and preserve stable paths across harnesses. File size is a useful diagnostic but not an identity: compression settings, ZIP metadata, line endings, and excluded files can change size without changing capability.

## Stale-copy diagnosis

Compare in this order:

1. active workspace manifest and file hashes;
2. portable artifact manifest and ZIP hash;
3. registered-release identifier, if the host exposes one;
4. downloaded/client artifact hash or size, if the user can provide it.

Classify the result as **workspace-only**, **package-built**, **registration-unverified**, **client-stale**, or **matched**. State exactly which layer was verified and which was not. Do not infer a registry failure from size alone.

## Delivery rule

When the host supports skill-card generation, deliver the active `SKILL.md` path using the skill-creator convention. This allows the host to detect the skill directory and generate an Add/Update card. Provide the ZIP as a secondary portable artifact, not as a substitute for registration. If the card is absent, report that the filesystem/package work succeeded but host registration remains unverified.

## Portable update rule

On another AI harness, use the release manifest to compare capability identity before importing. Preserve `SKILL.md`, references, templates, scripts, stable IDs, and schemas. Remap only host-specific paths or URIs. Reject or quarantine incomplete packages rather than silently merging a stale copy over a newer authoritative release.

## Plain-language explanation

Tell non-technical users: “The skill can be updated in its working folder, packaged into a ZIP, and registered in the app as three separate steps. The app’s download size reflects the registered/client copy, not necessarily the folder we just changed. We can prove the folder and package, but only the app’s update card or registry status proves registration.”

## Limits

This protocol does not invent access to Manus’s private skill registry, mobile cache, background synchronization, or account state. It records evidence available in the current harness and gives the strongest honest diagnosis.
