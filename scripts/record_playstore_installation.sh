#!/bin/bash
################################################################################
# Play Store Installation Video Recorder
# 
# This script wraps the Play Store installation process with full video recording
# for debugging purposes. It captures the entire installation flow including:
# - Play Store opening
# - Login process
# - App search
# - Install button click
# - Installation progress
################################################################################

set -e

GOOGLE_EMAIL="$1"
GOOGLE_PASSWORD="$2"
APP_NAME="${3:-Eptura Engage}"
ADB="${ANDROID_HOME:-$ANDROID_SDK_ROOT}/platform-tools/adb"

echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "🎥 PLAY STORE INSTALLATION WITH FULL VIDEO RECORDING"
echo "════════════════════════════════════════════════════════════════════"
echo ""

# Verify prerequisites
if [ -z "$GOOGLE_EMAIL" ] || [ -z "$GOOGLE_PASSWORD" ]; then
    echo "❌ ERROR: Google credentials not provided"
    echo "Usage: $0 <email> <password> [app_name]"
    exit 1
fi

if [ ! -f "src/main/resources/install_from_playstore.py" ]; then
    echo "❌ ERROR: Python installation script not found"
    exit 1
fi

# Create output directories
mkdir -p playstore_screenshots
mkdir -p playstore-recordings

# Setup recording paths
RECORDING_TIMESTAMP=$(date +%Y%m%d_%H%M%S)
RECORDING_DEVICE_PATH="/sdcard/playstore_full_${RECORDING_TIMESTAMP}.mp4"
RECORDING_LOCAL_PATH="playstore-recordings/playstore_full_${RECORDING_TIMESTAMP}.mp4"

echo "📹 Recording Configuration:"
echo "   Device path: $RECORDING_DEVICE_PATH"
echo "   Local path:  $RECORDING_LOCAL_PATH"
echo "   Duration:    10 minutes max"
echo "   Quality:     4 Mbps (High)"
echo "   Format:      MP4 (H.264)"
echo ""

# Check device status
echo "🔍 Checking device status..."
DEVICE_STATUS=$("$ADB" get-state 2>/dev/null || echo "not_found")
if [ "$DEVICE_STATUS" != "device" ]; then
    echo "❌ ERROR: Device not ready (status: $DEVICE_STATUS)"
    exit 1
fi
echo "✅ Device is ready"
echo ""

# Start screen recording
# Use max 180 seconds (3 minutes) due to Android screenrecord limit
echo "🎬 Starting screen recording..."
"$ADB" shell screenrecord --verbose --time-limit 180 --bit-rate 4000000 "$RECORDING_DEVICE_PATH" > recording_output.log 2>&1 &
RECORDING_PID=$!

echo "✅ Screen recording started"
echo "   PID: $RECORDING_PID"
echo "   Output: recording_output.log"
echo "   ℹ️  Note: 'Time limit' warning from screenrecord is normal and can be ignored"

# Give recording time to initialize
sleep 3

# Verify recording process is running
if ! ps -p $RECORDING_PID > /dev/null 2>&1; then
    echo "⚠️  Warning: Recording process may have failed to start"
    echo "🔍 Recording log output:"
    cat recording_output.log 2>/dev/null || true
else
    echo "✅ Recording process confirmed running"
fi

echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "🚀 STARTING PLAY STORE INSTALLATION"
echo "════════════════════════════════════════════════════════════════════"
echo ""

# Determine Python command
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

echo "📱 Installation will proceed with:"
echo "   Email:      ${GOOGLE_EMAIL:0:3}***@***"
echo "   App:        $APP_NAME"
echo "   Python:     $PYTHON_CMD"
echo "   Recording:  ACTIVE ✅"
echo ""
echo "⏳ Starting Python installation script..."
echo "   (Real-time output will appear below)"
echo "────────────────────────────────────────────────────────────────────"
echo ""

# Run the installation with UNBUFFERED output (-u flag) for real-time logs
# This ensures all print statements appear immediately in the pipeline logs
INSTALL_START_TIME=$(date +%s)
$PYTHON_CMD -u src/main/resources/install_from_playstore.py "$GOOGLE_EMAIL" "$GOOGLE_PASSWORD" "$APP_NAME"
INSTALL_RESULT=$?
INSTALL_END_TIME=$(date +%s)
INSTALL_DURATION=$((INSTALL_END_TIME - INSTALL_START_TIME))

echo ""
echo "────────────────────────────────────────────────────────────────────"
echo "✅ Python script execution completed"
echo "   Exit code: $INSTALL_RESULT"
echo "   Duration: ${INSTALL_DURATION}s"
echo ""

echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "🎬 STOPPING AND RETRIEVING VIDEO RECORDING"
echo "════════════════════════════════════════════════════════════════════"
echo ""

# Stop the recording gracefully
echo "⏹️  Sending stop signal to recording..."
"$ADB" shell "pkill -INT screenrecord" 2>/dev/null || true

# Also try to stop by PID if we can
kill -INT $RECORDING_PID 2>/dev/null || true

# Wait for recording to finalize
echo "⏳ Waiting 45 seconds for recording to finalize on device..."
echo "   (This is critical for slow emulators)"
sleep 45

# Check recording process status
if ps -p $RECORDING_PID > /dev/null 2>&1; then
    echo "⚠️  Recording process still running, forcing termination..."
    kill -9 $RECORDING_PID 2>/dev/null || true
    sleep 2
else
    echo "✅ Recording process has stopped"
fi

# Verify recording file exists on device
echo ""
echo "🔍 Verifying recording file on device..."
FILE_INFO=$("$ADB" shell "ls -lh $RECORDING_DEVICE_PATH 2>/dev/null" || echo "FILE_NOT_FOUND")

if [[ "$FILE_INFO" == *"FILE_NOT_FOUND"* ]]; then
    echo "❌ Recording file not found: $RECORDING_DEVICE_PATH"
    echo ""
    echo "🔍 Searching for any recent screen recordings..."
    "$ADB" shell "find /sdcard -name '*.mp4' -type f -mmin -20 2>/dev/null" || echo "   No recordings found"
    echo ""
    echo "⚠️  Video recording failed - check recording_output.log for details:"
    cat recording_output.log 2>/dev/null || echo "   (Log file not found)"
    
    RECORDING_SUCCESS=false
else
    echo "✅ Recording file exists on device:"
    echo "   $FILE_INFO"
    
    # Extract file size from ls output
    FILE_SIZE_HUMAN=$(echo "$FILE_INFO" | awk '{print $5}')
    echo "   Size: $FILE_SIZE_HUMAN"
    
    # Pull the recording with retries
    echo ""
    echo "📥 Pulling recording from device (with retries)..."
    
    PULL_SUCCESS=false
    for attempt in {1..5}; do
        echo "   Attempt $attempt/5..."
        
        if "$ADB" pull "$RECORDING_DEVICE_PATH" "$RECORDING_LOCAL_PATH" 2>&1 | grep -q "pulled"; then
            # Verify the pulled file
            if [ -f "$RECORDING_LOCAL_PATH" ]; then
                LOCAL_SIZE=$(stat -f%z "$RECORDING_LOCAL_PATH" 2>/dev/null || stat -c%s "$RECORDING_LOCAL_PATH" 2>/dev/null || echo "0")
                if [ "$LOCAL_SIZE" -gt 1024 ]; then
                    LOCAL_SIZE_MB=$(echo "scale=2; $LOCAL_SIZE / 1024 / 1024" | bc 2>/dev/null || echo "$LOCAL_SIZE bytes")
                    echo "   ✅ Successfully pulled recording!"
                    echo "   📊 Local file size: ${LOCAL_SIZE_MB} MB"
                    PULL_SUCCESS=true
                    break
                else
                    echo "   ⚠️  File too small ($LOCAL_SIZE bytes), retrying..."
                    rm -f "$RECORDING_LOCAL_PATH"
                fi
            fi
        fi
        
        if [ $attempt -lt 5 ]; then
            echo "   ⏳ Waiting 5 seconds before retry..."
            sleep 5
        fi
    done
    
    if [ "$PULL_SUCCESS" = true ]; then
        RECORDING_SUCCESS=true
        
        # Clean up device file
        echo ""
        echo "🧹 Cleaning up device file..."
        "$ADB" shell "rm -f $RECORDING_DEVICE_PATH" 2>/dev/null || true
    else
        echo ""
        echo "❌ Failed to pull recording after 5 attempts"
        echo "💡 Recording may still be on device at: $RECORDING_DEVICE_PATH"
        echo "   You can manually retrieve it later with:"
        echo "   adb pull $RECORDING_DEVICE_PATH $RECORDING_LOCAL_PATH"
        RECORDING_SUCCESS=false
    fi
fi

# Final summary
echo ""
echo "════════════════════════════════════════════════════════════════════"
echo "📊 INSTALLATION SUMMARY"
echo "════════════════════════════════════════════════════════════════════"
echo ""
echo "Installation Result: $([ $INSTALL_RESULT -eq 0 ] && echo '✅ SUCCESS' || echo '❌ FAILED')"
echo "Duration:            ${INSTALL_DURATION} seconds"
echo "Video Recording:     $([ "$RECORDING_SUCCESS" = true ] && echo '✅ SAVED' || echo '⚠️  FAILED')"
echo ""

if [ "$RECORDING_SUCCESS" = true ]; then
    echo "🎥 VIDEO RECORDING AVAILABLE FOR DEBUGGING"
    echo "   📁 File: $RECORDING_LOCAL_PATH"
    echo "   📋 This video captures the complete installation process"
    echo "   💡 Review this video to debug any installation issues"
    echo ""
    echo "   The recording shows:"
    echo "      • Play Store opening and navigation"
    echo "      • Google account login (if required)"
    echo "      • App search process"
    echo "      • Install button interaction"
    echo "      • Installation progress"
    echo "      • Final verification"
else
    echo "⚠️  VIDEO RECORDING NOT AVAILABLE"
    echo "   Check debug screenshots in: playstore_screenshots/"
    echo "   Check recording log: recording_output.log"
fi

echo ""
echo "📸 Debug screenshots location: playstore_screenshots/"
echo "🎥 Video recordings location:  playstore-recordings/"
echo ""
echo "════════════════════════════════════════════════════════════════════"

# Return the installation result
exit $INSTALL_RESULT