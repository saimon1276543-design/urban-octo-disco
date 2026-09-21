@echo off
setlocal
set WORKSPACE=%USERPROFILE%\LearningWorkspace
if exist .venv\Scripts\python.exe (set PYTHON=.venv\Scripts\python.exe) else (set PYTHON=py -3)
%PYTHON% -m freeplane_sync.watch --workspace "%WORKSPACE%"
pause
