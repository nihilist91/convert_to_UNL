@echo off
REM Automated Release Builder for Excel/Word to UNL Converter
REM This script builds the EXE and prepares it for GitHub release

echo ========================================
echo  Excel/Word to UNL Converter
echo  Release Builder
echo ========================================
echo.

REM Get version from version.py
for /f "tokens=2 delims== " %%a in ('findstr "__version__" version.py') do set VERSION=%%a
set VERSION=%VERSION:"=%
echo Current Version: %VERSION%
echo.

REM Build the EXE
echo [1/4] Building EXE with PyInstaller...
.venv\Scripts\python.exe -m PyInstaller Excel_to_UNL_Converter.spec --noconfirm

if errorlevel 1 (
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo [2/4] Build completed successfully!
echo.

REM Check if EXE exists
if not exist "dist\Excel_to_UNL_Converter.exe" (
    echo ERROR: EXE file not found!
    pause
    exit /b 1
)

echo [3/4] EXE created: dist\Excel_to_UNL_Converter.exe
echo.

REM Get file size
for %%A in ("dist\Excel_to_UNL_Converter.exe") do set SIZE=%%~zA
set /a SIZE_MB=%SIZE% / 1048576
echo File size: %SIZE_MB% MB
echo.

echo [4/4] Ready for release!
echo.
echo ========================================
echo  NEXT STEPS:
echo ========================================
echo.
echo 1. Test the EXE: dist\Excel_to_UNL_Converter.exe
echo 2. Commit changes: git add . ^&^& git commit -m "Release v%VERSION%"
echo 3. Push to GitHub: git push origin main
echo 4. Create GitHub release at:
echo    https://github.com/nihilist91/convert_to_UNL/releases/new
echo.
echo 5. Use this info for the release:
echo    - Tag: v%VERSION%
echo    - Title: Excel/Word to UNL Converter v%VERSION%
echo    - Attach: dist\Excel_to_UNL_Converter.exe
echo.
echo ========================================
echo.
pause
