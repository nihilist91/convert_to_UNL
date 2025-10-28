@echo off
REM Build EXE using PyInstaller
echo ========================================
echo  Building Excel/Word to UNL Converter
echo ========================================
echo.

echo Cleaning previous builds...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist

echo.
echo Building standalone EXE...
echo This may take 2-3 minutes...
echo.

.venv\Scripts\python.exe -m PyInstaller --name="Excel_to_UNL_Converter" ^
    --onefile ^
    --windowed ^
    --add-data "version.py;." ^
    --add-data "samples\4.unl;samples" ^
    --add-data "samples\bvov10105000002510160001.unl;samples" ^
    --add-data "samples\bvov23104700002505210001 (1).unl;samples" ^
    --add-data "samples\bvov23104700002505210001.unl;samples" ^
    --add-data "samples\bvov2510210001.unl;samples" ^
    --add-data "samples\CNTR_PRIMAIR.xlsx;samples" ^
    --add-data "samples\cntr.docx;samples" ^
    excel_to_unl_converter.py

if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    pause
    exit /b 1
)

echo.
echo ========================================
echo  Build Complete!
echo ========================================
echo.
echo EXE Location: dist\Excel_to_UNL_Converter.exe
echo.

for %%A in ("dist\Excel_to_UNL_Converter.exe") do set SIZE=%%~zA
set /a SIZE_MB=%SIZE% / 1048576
echo File Size: %SIZE_MB% MB
echo.
echo You can now test the app by running:
echo   dist\Excel_to_UNL_Converter.exe
echo.
pause
