@echo off
REM Get the directory of the batch file
set "SCRIPT_DIR=%~dp0"

REM Navigate to the script directory
cd /d "%SCRIPT_DIR%"

REM Run the Python script
python ExportsGenerator.py

REM Pause the console after execution
pause
