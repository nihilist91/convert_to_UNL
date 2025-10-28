@echo off
REM Build EXE using Nuitka (supports Python 3.14)
echo ========================================
echo  Building Excel/Word to UNL Converter
echo  Using Nuitka Compiler
echo ========================================
echo.

echo This will take 5-10 minutes (Nuitka compiles to C++)
echo Please be patient...
echo.

.venv\Scripts\python.exe -m nuitka ^
    --standalone ^
    --onefile ^
    --windows-disable-console ^
    --enable-plugin=pyqt6 ^
    --python-for-scons=C:\Python314\python.exe ^
    --msvc=latest ^
    --include-data-files=version.py=version.py ^
    --include-data-dir=samples=samples ^
    --output-dir=dist ^
    --output-filename=Excel_to_UNL_Converter.exe ^
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
