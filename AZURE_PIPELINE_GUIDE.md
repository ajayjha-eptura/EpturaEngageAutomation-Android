# Azure Pipeline Configuration - Play Store Only

## ✅ Current Setup

Your project now uses **ONE Azure Pipeline**: `azure-pipelines-playstore.yml`

This pipeline is optimized for **production testing** by installing the app directly from Google Play Store.

---

## 📋 What This Pipeline Does

1. **Builds** your Maven project
2. **Creates** an Android emulator with Google Play Store
3. **Installs** Eptura Engage app from Google Play Store (automated)
4. **Starts** Appium server
5. **Runs** your TestNG test suite
6. **Publishes** test results, screenshots, and reports

---

## 🔧 Required Setup (One-Time)

### Step 1: Configure Google Credentials in Azure DevOps

For automated Play Store installation, you need to set up Google account credentials:

1. Go to **Azure DevOps** → Your Project
2. Navigate to **Pipelines** → Select your pipeline
3. Click **Edit** → **Variables** (top right)
4. Add these **secret variables**:

   | Variable Name | Value | Settings |
   |---------------|-------|----------|
   | `GOOGLE_PLAY_EMAIL` | your-google-account@example.com | ☑️ Keep this value secret |
   | `GOOGLE_PLAY_PASSWORD` | your-password | ☑️ Keep this value secret |

5. Click **Save**

**💡 Security Tip:** Use a dedicated test Google account, not your personal account.

---

## 🚀 How to Run the Pipeline

### Option 1: Automatic Trigger (Default)
The pipeline automatically runs when you:
- ✅ Push code to `main`, `master`, or `develop` branches
- ✅ Create a pull request to these branches

### Option 2: Manual Trigger
1. Go to **Azure DevOps** → **Pipelines**
2. Select your pipeline
3. Click **"Run pipeline"**
4. Select your branch
5. Click **"Run"**

---

## ⏱️ Pipeline Execution Time

- **Average Duration:** 15-25 minutes
- **Stages:**
  - Build: ~3 minutes
  - Emulator Setup: ~5 minutes
  - App Installation: ~3 minutes
  - Test Execution: ~10-15 minutes
  - Report Publishing: ~1 minute

---

## 📊 What Gets Published

After each run, you'll find:

1. **Test Results** - JUnit format, viewable in Azure DevOps
2. **Screenshots** - All captured screenshots (passed and failed tests)
3. **Extent Report** - Detailed HTML test report
4. **Appium Logs** - For debugging test failures
5. **Emulator Logs** - For emulator-related issues

Access them in: **Pipeline Run** → **Summary** → **Artifacts**

---

## 🔍 Monitoring Test Results

### In Azure DevOps:
1. Go to your pipeline run
2. Click on **Tests** tab
3. View:
   - ✅ Passed tests
   - ❌ Failed tests
   - ⏭️ Skipped tests
   - 📊 Test trends over time

### Download Reports:
1. Go to **Summary** tab
2. Scroll to **Published Artifacts**
3. Download:
   - `extent-report` - HTML report
   - `test-screenshots` - All screenshots
   - `appium-logs` - Appium server logs

---

## 🐛 Troubleshooting

### Issue: "GOOGLE_PLAY_EMAIL or GOOGLE_PLAY_PASSWORD not set"

**Solution:**
- Verify secret variables are created in Azure DevOps
- Check variable names match exactly (case-sensitive)
- Ensure "Keep this value secret" is checked

---

### Issue: "App installation failed"

**Possible Causes:**
1. Google credentials are incorrect
2. Account doesn't have access to the app
3. App not available in the account's region
4. Google account has 2FA without app-specific password

**Solutions:**
- Verify credentials are correct
- Use a Google account that has previously installed the app
- Consider using an app-specific password if 2FA is enabled
- Check the `install_from_playstore.py` logs in the pipeline output

---

### Issue: "Emulator failed to boot"

**Solution:**
- This is usually a timeout issue
- The pipeline will retry automatically
- Check emulator logs in artifacts if it persists

---

### Issue: Tests fail but app installs successfully

**Solution:**
- Check the test logs in Azure DevOps
- Download screenshots from artifacts
- Review the Extent Report for detailed error messages
- Check Appium logs for connection issues

---

## 🎯 Best Practices

### 1. **Run Frequency**
- ✅ Before each production release
- ✅ Weekly regression testing
- ✅ After major app updates
- ⚠️ Avoid running on every commit (uses more agent time)

### 2. **Cost Optimization**
If you want to save agent minutes, you can disable auto-trigger:

Edit `azure-pipelines-playstore.yml`:
```yaml
# Disable automatic triggers
trigger: none
pr: none
```

Then run the pipeline manually only when needed.

### 3. **Credential Security**
- Use a dedicated test Google account
- Enable app-specific passwords if using 2FA
- Regularly rotate passwords
- Never commit credentials to code

### 4. **Monitor Test Stability**
- Review test trends in Azure DevOps
- Fix flaky tests promptly
- Keep screenshots for failed tests
- Update test data when app UI changes

---

## 📈 Pipeline Variables (Configurable)

You can customize these in `azure-pipelines-playstore.yml`:

| Variable | Current Value | Purpose |
|----------|---------------|---------|
| `jdkVersion` | `11` | Java version for Maven |
| `appiumVersion` | `3.0.0` | Appium server version |
| `androidSdkVersion` | `30` | Android API level |
| `emulatorName` | `test_emulator_playstore` | Emulator AVD name |

---

## 🔄 Pipeline Workflow

```
📝 Code Push/PR
    ↓
🏗️ Build Stage
    ├─ Install Java JDK 11
    ├─ Maven Clean Compile
    └─ Publish Build Artifacts
    ↓
🧪 Test Stage
    ├─ Setup Android SDK
    ├─ Create Emulator with Play Store
    ├─ Install Python Dependencies
    ├─ Install Appium & Drivers
    ├─ Start Appium Server
    ├─ Install App from Play Store ⭐
    ├─ Run TestNG Tests
    └─ Publish Test Results
    ↓
📊 Report Stage
    ├─ Download All Artifacts
    ├─ Display Summary
    └─ Publish Combined Reports
```

---

## 📞 Support & Maintenance

### Regular Maintenance Tasks:
- ✅ Update Appium version when new releases available
- ✅ Update Android SDK as needed
- ✅ Review and update test data
- ✅ Check for deprecated Appium commands
- ✅ Monitor pipeline execution time trends

### Need Help?
- Check Azure Pipeline logs for errors
- Review Appium logs in artifacts
- Check install_from_playstore.py output
- Verify Google credentials are still valid

---

## ✅ Quick Checklist

Before your first run:
- [ ] Google credentials set as secret variables in Azure DevOps
- [ ] Pipeline file `azure-pipelines-playstore.yml` exists in repo root
- [ ] Test Google account can access/install the app
- [ ] TestNG XML file is configured correctly
- [ ] Config.properties has correct app package/activity

---

## 🎉 You're All Set!

Your pipeline is now configured for **production-grade testing** with:
- ✅ Automated Play Store installation
- ✅ Real emulator environment
- ✅ Comprehensive reporting
- ✅ Secure credential handling
- ✅ Full test automation

**Next Steps:**
1. Set up Google credentials in Azure DevOps (if not done)
2. Commit and push your code
3. Watch the pipeline run automatically
4. Review test results and reports

---

**Last Updated:** November 21, 2025
**Pipeline File:** `azure-pipelines-playstore.yml`
**Status:** Production Ready ✅
