@echo off
REM ============================================================
REM Start Android Emulator for Eptura Engage Testing
REM ============================================================

echo ============================================================
echo Starting Android Emulator
echo ============================================================
echo.

REM Set Android SDK location
set ANDROID_SDK=%LOCALAPPDATA%\Android\Sdk
set EMULATOR_NAME=Pixel_6_API_35_PlayStore

echo Checking for emulator: %EMULATOR_NAME%...
echo.

REM Check if emulator exists
call "%ANDROID_SDK%\emulator\emulator.exe" -list-avds | findstr /C:"%EMULATOR_NAME%" >nul
if errorlevel 1 (
    echo ERROR: Emulator '%EMULATOR_NAME%' not found!
    echo.
    echo Available emulators:
    call "%ANDROID_SDK%\emulator\emulator.exe" -list-avds
    echo.
    echo Please run create_emulator.bat first to create the emulator.
    pause
    exit /b 1
)

echo Starting emulator: %EMULATOR_NAME%...
echo This may take 2-5 minutes for first boot.
echo.
echo IMPORTANT: Do NOT close this window!
echo The emulator will stop if you close this window.
echo.

REM Start emulator with optimized settings
call "%ANDROID_SDK%\emulator\emulator.exe" -avd %EMULATOR_NAME% ^
  -netdelay none ^
  -netspeed full ^
  -no-snapshot-load ^
  -gpu auto ^
  -memory 4096

echo.
echo Emulator closed.
pause
