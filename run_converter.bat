@echo off
REM Excel/Word to UNL Converter - Auto Setup & Launch
echo ========================================
echo  Excel/Word to UNL Converter v1.0.0
echo  Auto-Setup and Launcher
echo ========================================
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\python.exe" (
    echo First-time setup detected!
    echo Creating virtual environment...
    python -m venv .venv
    echo.
    echo Installing dependencies...
    .venv\Scripts\pip install --quiet --upgrade pip
    .venv\Scripts\pip install --quiet -r requirements.txt
    echo.
    echo Setup complete!
    echo.
)

echo Starting application...
".venv\Scripts\python.exe" excel_to_unl_converter.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start application!
    echo.
    echo Make sure Python is installed:
    echo https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)
