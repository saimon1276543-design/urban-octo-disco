param(
  [string]$Workspace = "$HOME\LearningWorkspace"
)
$ErrorActionPreference = "Stop"
$python = if (Test-Path .\.venv\Scripts\python.exe) { .\.venv\Scripts\python.exe } else { "python" }
& $python -m freeplane_sync.watch --workspace $Workspace
