#!/bin/bash
# Script to verify artifact directories and their contents
# This helps diagnose if screenshots/recordings are being saved correctly

echo "=========================================="
echo "🔍 ARTIFACT DIRECTORY DIAGNOSTIC"
echo "=========================================="

WORKSPACE_DIR="$(pwd)"
echo "📁 Current working directory: $WORKSPACE_DIR"
echo ""

# Check screenshots directory
SCREENSHOTS_DIR="$WORKSPACE_DIR/playstore_screenshots"
echo "📸 Checking screenshots directory..."
if [ -d "$SCREENSHOTS_DIR" ]; then
    echo "   ✅ Directory exists: $SCREENSHOTS_DIR"
    FILE_COUNT=$(find "$SCREENSHOTS_DIR" -type f -name "*.png" 2>/dev/null | wc -l)
    echo "   📊 PNG files found: $FILE_COUNT"
    
    if [ $FILE_COUNT -gt 0 ]; then
        echo "   📋 Files:"
        ls -lh "$SCREENSHOTS_DIR"/*.png 2>/dev/null | while read line; do
            echo "      $line"
        done
    else
        echo "   ⚠️  No PNG files found"
        echo "   📋 Directory contents:"
        ls -la "$SCREENSHOTS_DIR" 2>/dev/null || echo "      (Empty)"
    fi
else
    echo "   ❌ Directory does not exist: $SCREENSHOTS_DIR"
fi

echo ""

# Check recordings directory
RECORDINGS_DIR="$WORKSPACE_DIR/playstore-recordings"
echo "🎥 Checking recordings directory..."
if [ -d "$RECORDINGS_DIR" ]; then
    echo "   ✅ Directory exists: $RECORDINGS_DIR"
    FILE_COUNT=$(find "$RECORDINGS_DIR" -type f -name "*.mp4" 2>/dev/null | wc -l)
    echo "   📊 MP4 files found: $FILE_COUNT"
    
    if [ $FILE_COUNT -gt 0 ]; then
        echo "   📋 Files:"
        ls -lh "$RECORDINGS_DIR"/*.mp4 2>/dev/null | while read line; do
            echo "      $line"
        done
    else
        echo "   ⚠️  No MP4 files found"
        echo "   📋 Directory contents:"
        ls -la "$RECORDINGS_DIR" 2>/dev/null || echo "      (Empty)"
    fi
else
    echo "   ❌ Directory does not exist: $RECORDINGS_DIR"
fi

echo ""

# Check XML debug files
echo "📄 Checking for XML debug files..."
if [ -f "$SCREENSHOTS_DIR/page_source_debug.xml" ]; then
    SIZE=$(stat -f%z "$SCREENSHOTS_DIR/page_source_debug.xml" 2>/dev/null || stat -c%s "$SCREENSHOTS_DIR/page_source_debug.xml" 2>/dev/null)
    echo "   ✅ Found: page_source_debug.xml (${SIZE} bytes)"
else
    echo "   ℹ️  No page_source_debug.xml found"
fi

echo ""
echo "=========================================="
echo "📦 ARTIFACTS READY FOR PUBLISHING"
echo "=========================================="
echo ""
echo "These directories will be published as build artifacts:"
echo "   1. 'playstore-debug-screenshots' -> $SCREENSHOTS_DIR"
echo "   2. 'playstore-video-recordings' -> $RECORDINGS_DIR"
echo ""
echo "After pipeline completes, access them in Azure DevOps:"
echo "   Pipeline Run > Summary > Published artifacts"
echo "=========================================="
