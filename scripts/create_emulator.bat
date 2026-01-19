@echo off
REM ============================================================
REM Create Android Emulator with Google Play Store
REM For Eptura Engage Automation Project
REM ============================================================

echo ============================================================
echo Creating Android Emulator with Google Play Store
echo ============================================================
echo.

REM Set Android SDK location
set ANDROID_SDK=%LOCALAPPDATA%\Android\Sdk
set EMULATOR_NAME=Pixel_6_API_35_PlayStore

echo [1/4] Checking Android SDK installation...
if not exist "%ANDROID_SDK%\emulator\emulator.exe" (
    echo ERROR: Android SDK not found at %ANDROID_SDK%
    echo Please install Android Studio first.
    pause
    exit /b 1
)
echo     Found Android SDK at: %ANDROID_SDK%
echo.

echo [2/4] Downloading system image (this may take several minutes)...
echo     Package: system-images;android-35;google_apis_playstore;x86_64
call "%ANDROID_SDK%\cmdline-tools\latest\bin\sdkmanager.bat" "system-images;android-35;google_apis_playstore;x86_64"
if errorlevel 1 (
    echo.
    echo WARNING: Could not download using cmdline-tools
    echo Please download manually from Android Studio SDK Manager:
    echo   - Android 15.0 ^(API 35^)
    echo   - System Image: Google APIs Play Store Intel x86_64 Atom System Image
    echo.
)
echo.

echo [3/4] Creating AVD: %EMULATOR_NAME%...
call "%ANDROID_SDK%\cmdline-tools\latest\bin\avdmanager.bat" create avd ^
  --name %EMULATOR_NAME% ^
  --package "system-images;android-35;google_apis_playstore;x86_64" ^
  --device "pixel_6" ^
  --sdcard 512M ^
  --force

if errorlevel 1 (
    echo ERROR: Failed to create AVD
    echo.
    echo Trying alternative method...
    echo Please follow these steps manually:
    echo 1. Open Android Studio
    echo 2. Go to Tools ^> Device Manager
    echo 3. Click 'Create Device'
    echo 4. Select Pixel 6, then Next
    echo 5. Download and select 'VanillaIceCream API 35 - Google APIs Play Store'
    echo 6. Name it: %EMULATOR_NAME%
    pause
    exit /b 1
)
echo.

echo [4/4] Configuring AVD settings...
set AVD_CONFIG=%USERPROFILE%\.android\avd\%EMULATOR_NAME%.avd\config.ini

if exist "%AVD_CONFIG%" (
    echo hw.ramSize=4096 >> "%AVD_CONFIG%"
    echo vm.heapSize=512 >> "%AVD_CONFIG%"
    echo hw.gpu.enabled=yes >> "%AVD_CONFIG%"
    echo hw.gpu.mode=auto >> "%AVD_CONFIG%"
    echo skin.dynamic=yes >> "%AVD_CONFIG%"
    echo     RAM: 4096 MB
    echo     VM Heap: 512 MB
    echo     GPU: Enabled
) else (
    echo WARNING: Could not find config file to customize settings
)
echo.

echo ============================================================
echo SUCCESS! Emulator created: %EMULATOR_NAME%
echo ============================================================
echo.
echo Next steps:
echo 1. Run: start_emulator.bat
echo 2. Wait for emulator to boot completely
echo 3. Configure Google account in the emulator
echo 4. Run: setup_playstore.bat
echo.
pause
