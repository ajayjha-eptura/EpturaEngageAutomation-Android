@echo off
REM Quick setup script for Azure Blob Storage APK management (Windows)

echo ==============================================
echo Azure Blob Storage Setup for APK Management
echo ==============================================
echo.

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed. Please install Python 3.x
    pause
    exit /b 1
)
echo [OK] Python found

REM Install required packages
echo.
echo Installing required Python packages...
pip install -r scripts\requirements.txt

if errorlevel 1 (
    echo X Failed to install requirements
    pause
    exit /b 1
)

echo.
echo [OK] Setup complete!
echo.
echo ==============================================
echo Next Steps:
echo ==============================================
echo.
echo 1. Create Azure Storage Account:
echo    - Go to https://portal.azure.com
echo    - Create a Storage Account
echo    - Create a container (e.g., 'apk-files')
echo.
echo 2. Set environment variables (Windows):
echo    set AZURE_STORAGE_ACCOUNT=your-storage-account
echo    set AZURE_STORAGE_KEY=your-storage-key
echo    set AZURE_STORAGE_CONTAINER=apk-files
echo.
echo 3. Upload your APK:
echo    python scripts\upload_apk_to_blob.py --apk-path C:\path\to\app.apk --blob-name EpturaEngage.apk
echo.
echo 4. Configure Azure DevOps Pipeline:
echo    - Add the azure-pipelines.yml to your repo
echo    - Set pipeline variables (see AZURE_BLOB_SETUP.md)
echo.
echo For detailed instructions, see: AZURE_BLOB_SETUP.md
echo ==============================================
echo.
pause
