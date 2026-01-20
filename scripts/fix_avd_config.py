import re

with open('../azure-pipelines.yml', 'r', encoding='utf-8') as f:
    content = f.read()

old_text = '''echo "no" | avdmanager create avd -n test_emulator -k "system-images;android-30;google_apis_playstore;x86_64" -d pixel_4 --force
              
              echo "✅ Android Emulator created"'''

new_text = '''echo "no" | avdmanager create avd -n test_emulator -k "system-images;android-30;google_apis_playstore;x86_64" -d pixel_4 --force
              
              # Configure AVD with proper screen settings for Pixel 4
              AVD_DIR="$HOME/.android/avd/test_emulator.avd"
              if [ -f "$AVD_DIR/config.ini" ]; then
                echo "📝 Configuring AVD screen settings..."
                echo "hw.lcd.density=440" >> "$AVD_DIR/config.ini"
                echo "hw.lcd.width=1080" >> "$AVD_DIR/config.ini"
                echo "hw.lcd.height=2280" >> "$AVD_DIR/config.ini"
                echo "hw.keyboard=yes" >> "$AVD_DIR/config.ini"
              fi
              
              echo "✅ Android Emulator created with Pixel 4 profile (1080x2280)"'''

content = content.replace(old_text, new_text)

with open('../azure-pipelines.yml', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Updated azure-pipelines.yml with AVD screen configuration')
