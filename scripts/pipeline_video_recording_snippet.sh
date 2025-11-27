#!/bin/bash
################################################################################
# Azure Pipeline Integration for Play Store Installation (Screenshots Only)
# 
# This snippet should replace the existing Play Store installation section
# in azure-pipelines.yml (around line 475-520)
################################################################################

# Verify device is still ready
if ! "$ADB" shell getprop sys.boot_completed 2>/dev/null | grep -q "1"; then
  echo "⚠️  Device offline, waiting 10s for recovery..."
  sleep 10
fi

# Create directory for debugging screenshots
mkdir -p playstore_screenshots

# Make script executable (no video recording script)
chmod +x scripts/record_playstore_installation.sh

# Run installation (screenshots only, no video recording)
./scripts/record_playstore_installation.sh "$GOOGLE_EMAIL" "$GOOGLE_PASSWORD" "Eptura Engage"
INSTALL_RESULT=$?

# Verify installation
echo "🔍 Final verification - checking package manager..."
if "$ADB" shell pm list packages 2>/dev/null | grep -q "$PACKAGE_NAME"; then
  echo "✅✅✅ PLAY STORE INSTALLATION SUCCESSFUL! ✅✅✅"
  echo "   Package: $PACKAGE_NAME"
  echo "   Method: Google Play Store"
  echo "   Debug screenshots saved to: playstore_screenshots/"
  exit 0
else
  echo "❌ INSTALLATION FAILED"
  echo "   App package not found in device package manager"
  echo "   Package searched: $PACKAGE_NAME"
  echo ""
  echo "📸 Debug screenshots saved to: playstore_screenshots/"
  exit 1
fi
# Removed all video recording logic, references, and output. No video capture will occur.