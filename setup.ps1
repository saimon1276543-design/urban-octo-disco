param(
  [string]$Workspace = "$HOME\LearningWorkspace"
)
$ErrorActionPreference = "Stop"
python -m venv .venv
& .\.venv\Scripts\python.exe -m freeplane_sync.cli init --workspace $Workspace
Write-Host "Workspace ready at $Workspace"
Write-Host "Put Freeplane .mm files in $Workspace\maps, then run .\start-sync.ps1 -Workspace $Workspace"
