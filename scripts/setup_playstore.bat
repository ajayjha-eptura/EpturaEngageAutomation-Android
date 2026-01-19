@echo off
REM ============================================================
REM Setup Google Play Store and Install Eptura Engage
REM ============================================================

echo ============================================================
echo Google Play Store Setup and App Installation
echo ============================================================
echo.

REM Set Android SDK location
set ANDROID_SDK=%LOCALAPPDATA%\Android\Sdk

echo [Step 1] Checking if emulator is running...
call "%ANDROID_SDK%\platform-tools\adb.exe" devices | findstr "emulator"
if errorlevel 1 (
    echo ERROR: No emulator detected!
    echo Please start the emulator first using start_emulator.bat
    pause
    exit /b 1
)
echo SUCCESS: Emulator is running
echo.

echo [Step 2] Waiting for emulator to be fully ready...
timeout /t 10 /nobreak >nul
call "%ANDROID_SDK%\platform-tools\adb.exe" wait-for-device
echo SUCCESS: Emulator is ready
echo.

echo [Step 3] Checking Play Store installation...
call "%ANDROID_SDK%\platform-tools\adb.exe" shell pm list packages | findstr "com.android.vending"
if errorlevel 1 (
    echo ERROR: Google Play Store not found!
    echo Please recreate emulator with "Google Play" system image.
    pause
    exit /b 1
)
echo SUCCESS: Play Store is installed
echo.

echo ============================================================
echo MANUAL CONFIGURATION REQUIRED
echo ============================================================
echo.
echo Please complete these steps manually in the emulator:
echo.
echo 1. Open the Play Store app from the app drawer
echo 2. Sign in with your Google account
echo    - Email: [your-test-account@gmail.com]
echo    - Password: [your-password]
echo 3. Accept terms and conditions
echo 4. Complete any additional setup prompts
echo.
echo After completing the above, you have two options:
echo.
echo OPTION A - Manual Installation:
echo   5. Search for "Eptura Engage" or "Condeco"
echo   6. Click Install
echo   7. Wait for installation to complete
echo.
echo OPTION B - Automated Installation:
echo   5. Press any key to continue...
pause
echo.

echo ============================================================
echo Running Automated Installation Script
echo ============================================================
echo.

echo [Step 4] Checking if Python is installed...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)
echo SUCCESS: Python is installed
echo.

echo [Step 5] Installing Python dependencies...
if exist "..\target\classes\requirements.txt" (
    pip install -r ..\target\classes\requirements.txt
) else if exist "..\src\main\resources\requirements.txt" (
    pip install -r ..\src\main\resources\requirements.txt
) else (
    echo WARNING: requirements.txt not found
    echo Installing common dependencies...
    pip install appium-python-client selenium requests
)
echo.

echo [Step 6] Checking if Appium server is running...
curl -s http://127.0.0.1:4723/status >nul 2>&1
if errorlevel 1 (
    echo WARNING: Appium server not detected at http://127.0.0.1:4723
    echo.
    echo Please start Appium server in a separate terminal:
    echo   appium
    echo.
    echo Press any key after starting Appium server...
    pause
)
echo SUCCESS: Appium server is running
echo.

echo [Step 7] Running Play Store installation script...
echo.
echo You will be prompted for Google account credentials.
echo.

if exist "..\target\classes\install_from_playstore.py" (
    cd ..\target\classes
    python install_from_playstore.py
    cd ..\..\scripts
) else if exist "..\src\main\resources\install_from_playstore.py" (
    cd ..\src\main\resources
    python install_from_playstore.py
    cd ..\..\..\scripts
) else (
    echo ERROR: install_from_playstore.py not found!
    echo Expected location: target\classes\install_from_playstore.py
    pause
    exit /b 1
)

echo.
echo ============================================================
echo Setup Complete!
echo ============================================================
echo.
echo Verify installation:
call "%ANDROID_SDK%\platform-tools\adb.exe" shell pm list packages | findstr "com.condecosoftware.condeco"
if errorlevel 1 (
    echo WARNING: App installation may have failed
) else (
    echo SUCCESS: Eptura Engage is installed!
)
echo.
pause
