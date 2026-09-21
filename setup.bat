@echo off
setlocal
set WORKSPACE=%USERPROFILE%\LearningWorkspace
if not exist .venv\Scripts\python.exe py -3 -m venv .venv
.venv\Scripts\python.exe -m freeplane_sync.cli init --workspace "%WORKSPACE%"
echo Workspace ready at %WORKSPACE%
echo Put Freeplane .mm files in %WORKSPACE%\maps and run start-sync.bat
pause
