#!/bin/bash
################################################################################
# Azure Pipeline Integration for Play Store Video Recording
# 
# This snippet should replace the existing Play Store installation section
# in azure-pipelines.yml (around line 475-520)
################################################################################

# Replace this section in azure-pipelines.yml:

              # Verify device is still ready
              if ! "$ADB" shell getprop sys.boot_completed 2>/dev/null | grep -q "1"; then
                echo "⚠️  Device offline, waiting 10s for recovery..."
                sleep 10
              fi
              
              # Create directories for debugging artifacts
              mkdir -p playstore_screenshots
              mkdir -p playstore-recordings
              
              # Make script executable
              chmod +x scripts/record_playstore_installation.sh
              
              # Run installation with full video recording
              # The wrapper script handles:
              # 1. Starting ADB screen recording BEFORE the Python script
              # 2. Running the Play Store installation process
              # 3. Stopping recording gracefully
              # 4. Retrieving and saving the video file
              # 5. Providing detailed summary with video location
              ./scripts/record_playstore_installation.sh "$GOOGLE_EMAIL" "$GOOGLE_PASSWORD" "Eptura Engage"
              INSTALL_RESULT=$?
              
              # Verify installation
              echo "🔍 Final verification - checking package manager..."
              if "$ADB" shell pm list packages 2>/dev/null | grep -q "$PACKAGE_NAME"; then
                echo "✅✅✅ PLAY STORE INSTALLATION SUCCESSFUL! ✅✅✅"
                echo "   Package: $PACKAGE_NAME"
                echo "   Method: Google Play Store"
                echo "   Video: Available in playstore-recordings/"
                exit 0
              else
                echo "❌ INSTALLATION FAILED"
                echo "   App package not found in device package manager"
                echo "   Package searched: $PACKAGE_NAME"
                echo ""
                echo "📸 Debug screenshots saved to: playstore_screenshots/"
                echo "🎥 Video recording saved to: playstore-recordings/"
                echo "   ⚠️  REVIEW THE VIDEO to see what went wrong!"
                exit 1
              fi