@echo off
REM ============================================================
REM Check Emulator Status and Configuration
REM ============================================================

echo ============================================================
echo Checking Emulator Status
echo ============================================================
echo.

REM Set Android SDK location
set ANDROID_SDK=%LOCALAPPDATA%\Android\Sdk

echo [1] Checking connected devices...
call "%ANDROID_SDK%\platform-tools\adb.exe" devices
echo.

echo [2] Checking emulator boot status...
call "%ANDROID_SDK%\platform-tools\adb.exe" shell getprop sys.boot_completed
if errorlevel 1 (
    echo WARNING: Emulator not fully booted or not connected
) else (
    echo SUCCESS: Emulator is booted
)
echo.

echo [3] Checking Android version...
for /f "tokens=*" %%a in ('call "%ANDROID_SDK%\platform-tools\adb.exe" shell getprop ro.build.version.release') do (
    echo Android Version: %%a
)
for /f "tokens=*" %%a in ('call "%ANDROID_SDK%\platform-tools\adb.exe" shell getprop ro.build.version.sdk') do (
    echo API Level: %%a
)
echo.

echo [4] Checking device model...
for /f "tokens=*" %%a in ('call "%ANDROID_SDK%\platform-tools\adb.exe" shell getprop ro.product.model') do (
    echo Device Model: %%a
)
echo.

echo [5] Checking Google Play Store...
call "%ANDROID_SDK%\platform-tools\adb.exe" shell pm list packages | findstr "com.android.vending"
if errorlevel 1 (
    echo WARNING: Google Play Store NOT found!
    echo You may need to recreate the emulator with Google Play system image.
) else (
    echo SUCCESS: Google Play Store is installed
)
echo.

echo [6] Checking Eptura Engage app...
call "%ANDROID_SDK%\platform-tools\adb.exe" shell pm list packages | findstr "com.condecosoftware.condeco"
if errorlevel 1 (
    echo INFO: Eptura Engage app NOT installed yet
) else (
    echo SUCCESS: Eptura Engage app is installed
)
echo.

echo [7] Checking Appium helper apps...
call "%ANDROID_SDK%\platform-tools\adb.exe" shell pm list packages | findstr "io.appium"
echo.

echo ============================================================
echo Check complete!
echo ============================================================
pause
