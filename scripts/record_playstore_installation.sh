#!/bin/bash
################################################################################
# Play Store Installation Script (No Video Recording)
# This script logs each step of the Play Store installation process for debugging.
################################################################################

set -e

GOOGLE_EMAIL="$1"
GOOGLE_PASSWORD="$2"
APP_NAME="${3:-Eptura Engage}"
APP_PACKAGE="com.condecosoftware.condeco"
ADB="${ANDROID_HOME:-$ANDROID_SDK_ROOT}/platform-tools/adb"

# Verify prerequisites
if [ -z "$GOOGLE_EMAIL" ] || [ -z "$GOOGLE_PASSWORD" ]; then
    echo "ERROR: Google credentials not provided"
    echo "Usage: $0 <email> <password> [app_name]"
    exit 1
fi

if [ ! -f "src/main/resources/install_from_playstore.py" ]; then
    echo "ERROR: Python installation script not found"
    exit 1
fi

echo "Step 1: Checking device status..."
DEVICE_STATUS=$("$ADB" get-state 2>/dev/null || echo "not_found")
if [ "$DEVICE_STATUS" != "device" ]; then
    echo "ERROR: Device not ready (status: $DEVICE_STATUS)"
    exit 1
fi
echo "Device is ready."

echo "Step 2: Starting Play Store installation process..."
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

echo "Step 3: Invoking Python installation script..."
INSTALL_START_TIME=$(date +%s)
$PYTHON_CMD -u src/main/resources/install_from_playstore.py "$GOOGLE_EMAIL" "$GOOGLE_PASSWORD" "$APP_PACKAGE"
INSTALL_RESULT=$?
INSTALL_END_TIME=$(date +%s)
INSTALL_DURATION=$((INSTALL_END_TIME - INSTALL_START_TIME))

echo ""
echo "============================================================"
echo "INSTALLATION SUMMARY"
echo "============================================================"
echo "Installation Result: $([ $INSTALL_RESULT -eq 0 ] && echo 'SUCCESS' || echo 'FAILED')"
echo "Duration: ${INSTALL_DURATION} seconds"
echo "============================================================"

exit $INSTALL_RESULT