@echo off
REM Excel to UNL Converter Launcher
echo Starting Excel to UNL Converter...
echo.

REM Check if virtual environment exists
if exist ".venv\Scripts\python.exe" (
    echo Using virtual environment...
    ".venv\Scripts\python.exe" excel_to_unl_converter.py
) else (
    echo Using system Python...
    python excel_to_unl_converter.py
)

pause
