#!/bin/bash
# Emulator Warm-Up Script
# Pre-installs Appium UiAutomator2 APKs and optimizes package manager performance
# This prevents timeout errors during Appium driver initialization

echo "🔥 EMULATOR WARM-UP: Pre-installing Appium APKs & Performance Tuning"
echo "============================================================================"
export ANDROID_HOME=$ANDROID_SDK_ROOT
ADB="$ANDROID_HOME/platform-tools/adb"

# Step 1: Verify device is responsive
echo "🔍 Step 1: Verifying device responsiveness..."
for i in {1..5}; do
  if "$ADB" shell getprop sys.boot_completed 2>/dev/null | grep -q "1"; then
    echo "✅ Device responsive on attempt $i"
    break
  fi
  echo "  Waiting for device... ($i/5)"
  sleep 3
done

# Step 2: Warm up package manager with multiple operations
echo ""
echo "🔥 Step 2: Warming up package manager (critical for APK installations)..."
echo "   This reduces subsequent APK installation times significantly"

# List packages multiple times to warm up the service
for i in {1..3}; do
  echo "   Warm-up round $i/3..."
  "$ADB" shell pm list packages -s > /dev/null 2>&1 || true
  "$ADB" shell pm path android > /dev/null 2>&1 || true
  sleep 2
done

echo "✅ Package manager warmed up"

# Step 3: Increase emulator storage performance
echo ""
echo "🚀 Step 3: Optimizing emulator I/O performance..."
"$ADB" shell settings put global package_verifier_enable 0 2>/dev/null || true
"$ADB" shell settings put global verifier_verify_adb_installs 0 2>/dev/null || true
echo "✅ Package verification disabled for faster installs"

# Step 4: Pre-install Appium UiAutomator2 APKs to avoid timeout during Python script
echo ""
echo "📦 Step 4: Pre-installing Appium UiAutomator2 server APKs..."
echo "   This prevents the 60-second timeout error during Appium driver initialization"
echo "   Location: ~/.appium/node_modules/appium-uiautomator2-driver/"

APPIUM_DRIVER_PATH="$HOME/.appium/node_modules/appium-uiautomator2-driver"

if [ -d "$APPIUM_DRIVER_PATH" ]; then
  # Find the APKs
  SERVER_APK=$(find "$APPIUM_DRIVER_PATH" -name "appium-uiautomator2-server-*.apk" -not -name "*-androidTest.apk" 2>/dev/null | head -1)
  TEST_APK=$(find "$APPIUM_DRIVER_PATH" -name "appium-uiautomator2-server-*-androidTest.apk" 2>/dev/null | head -1)
  
  if [ -n "$SERVER_APK" ]; then
    echo "📲 Installing UiAutomator2 server APK..."
    echo "   File: $(basename $SERVER_APK)"
    
    # Install with increased timeout and retry (180 seconds per attempt)
    for attempt in {1..3}; do
      echo "   Attempt $attempt/3..."
      if timeout 180 "$ADB" install -r -g "$SERVER_APK" 2>&1 | tee /tmp/install_server_output.txt; then
        if grep -q "Success" /tmp/install_server_output.txt; then
          echo "✅ Server APK installed successfully"
          break
        fi
      fi
      
      if [ $attempt -lt 3 ]; then
        echo "⚠️  Installation slow/failed, retrying in 10s..."
        sleep 10
      else
        echo "⚠️  Server APK installation had issues, but continuing..."
      fi
    done
  else
    echo "⚠️  Server APK not found"
  fi
  
  if [ -n "$TEST_APK" ]; then
    echo ""
    echo "📲 Installing UiAutomator2 test APK..."
    echo "   File: $(basename $TEST_APK)"
    
    for attempt in {1..3}; do
      echo "   Attempt $attempt/3..."
      if timeout 180 "$ADB" install -r -g "$TEST_APK" 2>&1 | tee /tmp/install_test_output.txt; then
        if grep -q "Success" /tmp/install_test_output.txt; then
          echo "✅ Test APK installed successfully"
          break
        fi
      fi
      
      if [ $attempt -lt 3 ]; then
        echo "⚠️  Installation slow/failed, retrying in 10s..."
        sleep 10
      else
        echo "⚠️  Test APK installation had issues, but continuing..."
      fi
    done
  else
    echo "⚠️  Test APK not found"
  fi
  
  # Also pre-install Appium Settings APK (required for Appium to function)
  echo ""
  SETTINGS_APK=$(find "$HOME/.appium/node_modules" -path "*/io.appium.settings/apks/settings_apk-*.apk" 2>/dev/null | head -1)
  if [ -n "$SETTINGS_APK" ]; then
    echo "📲 Installing Appium Settings APK..."
    echo "   File: $(basename $SETTINGS_APK)"
    
    for attempt in {1..3}; do
      echo "   Attempt $attempt/3..."
      if timeout 120 "$ADB" install -r -g "$SETTINGS_APK" 2>&1 | tee /tmp/install_settings_output.txt; then
        if grep -q "Success" /tmp/install_settings_output.txt; then
          echo "✅ Settings APK installed successfully"
          break
        fi
      fi
      
      if [ $attempt -lt 3 ]; then
        echo "⚠️  Installation slow/failed, retrying in 10s..."
        sleep 10
      else
        echo "⚠️  Settings APK installation had issues, but continuing..."
      fi
    done
  else
    echo "⚠️  Settings APK not found at expected location"
    # Try alternate location
    SETTINGS_APK_ALT=$(find "$HOME/.appium" -name "settings_apk*.apk" 2>/dev/null | head -1)
    if [ -n "$SETTINGS_APK_ALT" ]; then
      echo "   Found at alternate location: $(basename $SETTINGS_APK_ALT)"
      timeout 120 "$ADB" install -r -g "$SETTINGS_APK_ALT" 2>&1 || true
    fi
  fi
  
  echo ""
  echo "✅ Pre-installation complete!"
  echo ""
  echo "📋 Installed Appium packages:"
  "$ADB" shell pm list packages | grep -E "(uiautomator2|appium|io.appium)" || echo "   (packages may take a moment to register)"
  
else
  echo "⚠️  Appium driver path not found: $APPIUM_DRIVER_PATH"
  echo "   Checking alternate locations..."
  
  # Try to find Appium installation in common locations
  ALTERNATE_PATHS=(
    "/usr/local/lib/node_modules/appium/node_modules/appium-uiautomator2-driver"
    "$HOME/.nvm/versions/node/*/lib/node_modules/appium/node_modules/appium-uiautomator2-driver"
  )
  
  FOUND=false
  for path in "${ALTERNATE_PATHS[@]}"; do
    if [ -d "$path" ]; then
      echo "✅ Found at: $path"
      APPIUM_DRIVER_PATH="$path"
      FOUND=true
      break
    fi
  done
  
  if [ "$FOUND" = false ]; then
    echo "⚠️  Could not find Appium UiAutomator2 driver"
    echo "   APKs will be installed during Python script execution (may timeout)"
  fi
fi

# Step 5: Final verification
echo ""
echo "🎯 Step 5: Final system check..."
echo "   Testing package manager responsiveness..."

# Quick test to verify package manager is responsive
if "$ADB" shell pm list packages | head -5 > /dev/null 2>&1; then
  echo "✅ Package manager is responsive"
else
  echo "⚠️  Package manager is slow, but continuing..."
fi

# Give emulator a moment to settle after installations
echo ""
echo "⏳ Allowing 5 seconds for system to settle..."
sleep 5

echo ""
echo "✅✅✅ EMULATOR WARM-UP COMPLETE ✅✅✅"
echo "   Package manager is responsive and optimized"
echo "   Appium helper APKs pre-installed (or attempted)"
echo "   Ready for Play Store automation"
echo "============================================================================"
