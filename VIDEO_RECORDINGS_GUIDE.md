# 📹 Play Store Video Recordings - Access Guide

## Overview
The Play Store installation script now automatically records the entire installation process for debugging purposes. Videos are saved when installation fails or succeeds.

## 🎥 What Gets Recorded
- **Duration**: Up to 10 minutes per installation attempt
- **Quality**: Medium (4 Mbps) - good balance between quality and file size
- **Format**: MP4 (playable on any device)
- **Content**: Full screen recording of the Play Store installation flow including:
  - Search field interactions
  - Keyboard inputs
  - Button clicks
  - Installation progress
  - Any error dialogs or issues

## 📂 Where Videos Are Saved

### **Local Development (Windows)**
When running locally on your machine:
```
C:\Users\AjayJha\OneDrive - Eptura\Documents\Automation_Projects\EpturaEngageAutomation-Android\playstore-recordings\
```

File naming pattern:
```
playstore_install_YYYYMMDD_HHMMSS.mp4

Example:
playstore_install_20251125_143052.mp4
```

### **Azure Pipeline (macOS CI/CD)**
When running in the Azure Pipeline, videos are saved in:
```
$(System.DefaultWorkingDirectory)/playstore-recordings/
```

This translates to:
```
/Users/runner/work/1/s/playstore-recordings/
```

## 🔍 How to Access Videos in Azure Pipeline

### Method 1: Pipeline Artifacts (Recommended)

1. **Navigate to your Pipeline Run**
   - Go to Azure DevOps
   - Click on "Pipelines" in the left menu
   - Select your pipeline run

2. **Open the Summary Tab**
   - Click on the pipeline run you want to review
   - You'll see the "Summary" tab

3. **Download the Video Artifact**
   - Scroll down to the "Related" section
   - Look for "X published" or click "Artifacts" 
   - Find the artifact named: **`playstore-video-recordings`**
   - Click to download the entire folder as a ZIP file

4. **Extract and View**
   - Extract the ZIP file
   - Open the MP4 file with any video player (VLC, Windows Media Player, QuickTime, etc.)

### Method 2: Direct Download Link

After the pipeline runs, you'll see a section like this:
```
📦 Published artifacts
├── playstore-video-recordings (Video recordings)
├── playstore-debug-screenshots (Screenshots)
├── test-screenshots (Test screenshots)
├── extent-report (HTML report)
└── appium-logs (Appium logs)
```

Click on **`playstore-video-recordings`** to download.

### Method 3: Azure CLI (Advanced)

```bash
# List artifacts for a specific build
az pipelines runs artifact list --run-id <RUN_ID> --organization <ORG> --project <PROJECT>

# Download specific artifact
az pipelines runs artifact download --run-id <RUN_ID> --artifact-name playstore-video-recordings --path ./downloads
```

## 📋 What to Look For in the Video

When debugging a failed installation, review the video for:

### ✅ Search Phase
- Did the search bar open correctly?
- Was "Eptura Engage" typed successfully?
- Did the Enter/Search key get pressed? (Look for search results appearing)
- Are search results showing the correct app?

### ✅ Selection Phase
- Was the Eptura Engage app clicked?
- Did the app detail page load?

### ✅ Installation Phase
- Was the "Install" button found and clicked?
- Did any permission dialogs appear?
- Is the installation progress bar visible?
- Did any errors occur during download/install?

### ✅ Verification Phase
- Did the "Open" button appear (indicating success)?
- Are there any error messages visible?

## 🎬 Video Recording Logs

In the pipeline logs, you'll see messages like:

```
============================================================
🎬 STARTING VIDEO RECORDING
============================================================
📹 Video recordings will be saved to: /Users/runner/work/1/s/playstore-recordings
🎥 Starting screen recording via ADB...
   Device path: /sdcard/playstore_recording_20251125_074500.mp4
✅ Screen recording started (ADB method)

[... installation process ...]

============================================================
🎬 STOPPING VIDEO RECORDING
============================================================
⏹️  Stopping screen recording...
📥 Pulling recording from device...
✅ Recording saved: /Users/runner/work/1/s/playstore-recordings/playstore_install_20251125_074500.mp4
   File size: 15.43 MB

🎥 Video recording saved for debugging: /Users/runner/work/1/s/playstore-recordings/playstore_install_20251125_074500.mp4
   Review this video to see what went wrong during installation
```

## 🛠️ Troubleshooting

### Video Not Found in Artifacts?

**Check 1**: Verify the step ran
- Look for the "Publish Play Store Video Recordings" step in pipeline logs
- Status should be ✅ (even if installation failed)

**Check 2**: Check if recording was created
- Look in the logs for "Recording saved" message
- If you see "⚠️ Could not start recording", the feature may not be available

**Check 3**: Verify folder exists
- The `playstore-recordings` folder is created automatically
- If missing, check Python script execution logs

### Video File is Empty or Corrupted?

**Cause**: Recording might have been interrupted
- Check emulator logs for crashes
- Verify ADB connection was stable
- Look for "Recording file is empty or missing" warnings

### Multiple Videos in Artifact?

**Expected**: If the pipeline had multiple installation attempts (Method 1 failed, tried Method 2)
- Each attempt creates a separate video
- File timestamps help identify which attempt is which

## 📊 File Sizes

Typical video file sizes:
- **1-2 minutes recording**: ~5-8 MB
- **5 minutes recording**: ~15-25 MB
- **10 minutes recording**: ~30-40 MB

If file size is < 1 MB, the recording may be corrupted or incomplete.

## 🔐 Security Note

**Important**: Videos may contain sensitive information if login credentials are entered. The script is designed to:
- Use environment variables for credentials
- Not show actual passwords in UI (masked by Android)
- Only record when needed for debugging

Keep video files secure and delete after debugging.

## 📞 Support

If you have issues accessing recordings:
1. Check pipeline logs for recording status
2. Verify artifact publishing step completed
3. Ensure you have Azure DevOps permissions to download artifacts
4. Contact DevOps team if artifact storage quota is reached

## 🎯 Quick Reference

| What | Where |
|------|-------|
| **Local Videos** | `playstore-recordings/` in project root |
| **Pipeline Artifact Name** | `playstore-video-recordings` |
| **File Format** | MP4 |
| **Max Duration** | 10 minutes |
| **Quality** | Medium (4 Mbps) |
| **When Created** | Every installation attempt (success or failure) |

---

**Last Updated**: November 25, 2025
