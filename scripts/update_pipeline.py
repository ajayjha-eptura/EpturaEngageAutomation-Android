import re

# Read the current pipeline file
with open('../azure-pipelines.yml', 'r', encoding='utf-8') as f:
    content = f.read()

# Old APK installation step pattern
old_step = '''          - script: |
              set -e
              echo "📲 Installing APK on emulator..."
              export PATH=$(ANDROID_HOME)/platform-tools:$PATH
              
              # Wait a bit more for emulator to be fully ready
              sleep 10
              
              # Install the APK
              if [ -f "$(Build.SourcesDirectory)/app.apk" ]; then
                adb install -r "$(Build.SourcesDirectory)/app.apk"
                echo "✅ APK installed successfully"
              else
                echo "⚠️ APK file not found at $(Build.SourcesDirectory)/app.apk"
                ls -la $(Build.SourcesDirectory)/
              fi
            displayName: 'Install APK on Emulator\''''

# New robust APK installation step
new_step = '''          - script: |
              set -e
              echo "📲 Installing APK from Azure Blob Storage on emulator..."
              export PATH=$(ANDROID_HOME)/platform-tools:$PATH
              
              # Wait a bit more for emulator to be fully ready
              sleep 10
              
              echo "🔍 Searching for APK file downloaded from blob storage..."
              echo "Contents of Build.SourcesDirectory:"
              ls -la $(Build.SourcesDirectory)/
              
              # Try to find the APK file - it could be named app.apk or EpturaEngage.apk
              APK_FILE=""
              
              # Check for app.apk (the expected name from blob download)
              if [ -f "$(Build.SourcesDirectory)/app.apk" ]; then
                APK_FILE="$(Build.SourcesDirectory)/app.apk"
                echo "✅ Found APK at: $APK_FILE"
              # Check for any .apk file in the source directory
              elif [ -n "$(find $(Build.SourcesDirectory) -maxdepth 1 -name '*.apk' -type f 2>/dev/null | head -1)" ]; then
                APK_FILE=$(find $(Build.SourcesDirectory) -maxdepth 1 -name '*.apk' -type f | head -1)
                echo "✅ Found APK at: $APK_FILE"
              # Check recursively for any .apk file
              elif [ -n "$(find $(Build.SourcesDirectory) -name '*.apk' -type f 2>/dev/null | head -1)" ]; then
                APK_FILE=$(find $(Build.SourcesDirectory) -name '*.apk' -type f | head -1)
                echo "✅ Found APK at: $APK_FILE"
              fi
              
              if [ -n "$APK_FILE" ] && [ -f "$APK_FILE" ]; then
                echo "📱 APK file details:"
                ls -la "$APK_FILE"
                echo "📲 Installing APK on emulator..."
                adb install -r "$APK_FILE"
                
                # Verify the app is installed
                if adb shell pm list packages | grep -q "com.condecosoftware.condeco"; then
                  echo "✅ APK from blob storage installed and verified successfully!"
                else
                  echo "⚠️ APK installed but package verification failed. Continuing anyway..."
                fi
              else
                echo "❌ ERROR: No APK file found from blob storage!"
                echo "📁 Full directory listing:"
                find $(Build.SourcesDirectory) -type f -name "*.apk" 2>/dev/null || echo "No APK files found"
                echo "📁 All files in source directory:"
                find $(Build.SourcesDirectory) -type f | head -50
                exit 1
              fi
            displayName: 'Install APK on Emulator\''''

# Replace the old step with the new one
if old_step in content:
    content = content.replace(old_step, new_step)
    print("✅ Successfully updated the APK installation step!")
else:
    print("⚠️ Could not find exact match. Trying regex replacement...")
    # Try a more flexible regex pattern
    pattern = r"(- script: \|[^-]*Install APK on emulator[^']*displayName: 'Install APK on Emulator')"
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_step.lstrip(), content, flags=re.DOTALL)
        print("✅ Successfully updated using regex!")
    else:
        print("❌ Could not find the APK installation step to replace")

# Write the updated content back
with open('../azure-pipelines.yml', 'w', encoding='utf-8') as f:
    f.write(content)

print("📝 Pipeline file updated!")
