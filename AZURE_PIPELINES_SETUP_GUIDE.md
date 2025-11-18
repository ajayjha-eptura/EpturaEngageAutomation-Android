# Azure DevOps CI/CD Integration Guide
## Eptura Engage Android Automation

This guide will help you set up Azure Pipelines for your Android Appium automation project.

---

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Azure DevOps Setup](#azure-devops-setup)
3. [Pipeline Configuration Options](#pipeline-configuration-options)
4. [Self-Hosted Agent Setup (Recommended)](#self-hosted-agent-setup)
5. [Environment Variables & Secrets](#environment-variables--secrets)
6. [Running the Pipeline](#running-the-pipeline)
7. [Viewing Reports](#viewing-reports)
8. [Troubleshooting](#troubleshooting)

---

## 🔧 Prerequisites

Before setting up Azure Pipelines, ensure you have:

- [ ] Azure DevOps account (https://dev.azure.com)
- [ ] Git repository connected to Azure DevOps
- [ ] Android device or emulator accessible to the build agent
- [ ] APK file for the Condeco app (if needed for installation)

---

## 🚀 Azure DevOps Setup

### Step 1: Create Azure DevOps Project

1. Go to https://dev.azure.com
2. Click **+ New Project**
3. Enter project details:
   - **Name**: Eptura Engage Android Automation
   - **Visibility**: Private
   - **Version Control**: Git
4. Click **Create**

### Step 2: Import Your Repository

**Option A: Import from existing Git repo**
```bash
# In your local repository
git remote add azure https://dev.azure.com/{organization}/{project}/_git/{repo}
git push azure master
```

**Option B: Use existing GitHub/GitLab repo**
1. Go to **Project Settings** → **Service connections**
2. Create a service connection to GitHub/GitLab
3. Set up the pipeline to use external repository

### Step 3: Create the Pipeline

1. Navigate to **Pipelines** → **Pipelines**
2. Click **New Pipeline**
3. Select your repository source
4. Choose **Existing Azure Pipelines YAML file**
5. Select `/azure-pipelines.yml`
6. Click **Continue** → **Run**

---

## ⚙️ Pipeline Configuration Options

### Option 1: Microsoft-Hosted Agents (Cloud)

**Pros:**
- No setup required
- macOS agents have Android SDK pre-installed
- Always updated

**Cons:**
- Cannot connect to physical Android devices
- Must use Android emulator
- Limited execution time (60 min for free tier)

**Current Configuration** (in azure-pipelines.yml):
```yaml
pool:
  vmImage: 'macOS-latest'
```

### Option 2: Self-Hosted Agents (Recommended for Physical Devices)

**Pros:**
- Can connect to physical Android devices
- No execution time limits
- Better performance
- Access to local network resources

**Cons:**
- Requires setup and maintenance
- You manage the infrastructure

**Change Configuration to**:
```yaml
pool:
  name: 'YourSelfHostedPool'
  demands:
    - android
    - appium
```

---

## 🖥️ Self-Hosted Agent Setup (Recommended)

### For Windows Agent with Physical Android Device

#### 1. Install Prerequisites

```powershell
# Install Chocolatey (Package Manager)
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# Install Java JDK 11
choco install openjdk11 -y

# Install Node.js
choco install nodejs -y

# Install Maven
choco install maven -y

# Install Android SDK
choco install android-sdk -y
```

#### 2. Install Appium

```powershell
npm install -g appium@2.19.0
appium driver install uiautomator2
```

#### 3. Configure Android SDK

```powershell
# Set environment variables
[System.Environment]::SetEnvironmentVariable('ANDROID_HOME', 'C:\Android\android-sdk', 'Machine')
[System.Environment]::SetEnvironmentVariable('JAVA_HOME', 'C:\Program Files\OpenJDK\jdk-11', 'Machine')

# Update PATH
$path = [System.Environment]::GetEnvironmentVariable('Path', 'Machine')
$newPath = "$path;$env:ANDROID_HOME\platform-tools;$env:ANDROID_HOME\tools"
[System.Environment]::SetEnvironmentVariable('Path', $newPath, 'Machine')
```

#### 4. Connect Android Device

```powershell
# Enable USB Debugging on your Android device
# Connect device via USB
# Verify connection
adb devices

# Output should show:
# List of devices attached
# RZCXA08S2MX    device
```

#### 5. Install Azure Pipelines Agent

1. Go to **Project Settings** → **Agent pools**
2. Click **Add pool** → Create new pool (e.g., "AndroidDevicePool")
3. Click on the pool → **New agent**
4. Download the agent for Windows
5. Extract to `C:\AzureAgent`
6. Run PowerShell as Administrator:

```powershell
cd C:\AzureAgent
.\config.cmd

# Follow prompts:
# - Enter Azure DevOps URL: https://dev.azure.com/{organization}
# - PAT token: (generate from User Settings → Personal Access Tokens)
# - Agent pool: AndroidDevicePool
# - Agent name: AndroidAgent-1
# - Work folder: _work
# - Run as service: Y

.\run.cmd
```

#### 6. Configure Agent Capabilities

Add capabilities to identify the agent:
- Go to **Agent pools** → **AndroidDevicePool** → **Agents** → Your agent
- Add capabilities:
  - `android` = `true`
  - `appium` = `installed`
  - `deviceName` = `RZCXA08S2MX`

---

## 🔐 Environment Variables & Secrets

### Method 1: Using Azure Pipeline Variables

1. Go to **Pipelines** → Select your pipeline → **Edit**
2. Click **Variables** → **New variable**
3. Add variables:

| Variable Name | Value | Secret |
|--------------|-------|--------|
| `DEVICE_NAME` | RZCXA08S2MX | No |
| `APP_PACKAGE` | com.condecosoftware.condeco | No |
| `LOGIN_USERNAME` | user141 | No |
| `LOGIN_PASSWORD` | 1 | **Yes** |
| `SERVER_NAME` | unified1.condecodev.com | No |

### Method 2: Using Variable Groups

1. Go to **Pipelines** → **Library** → **+ Variable group**
2. Name: `Android-Test-Config`
3. Add variables (same as above)
4. Link to pipeline in YAML:

```yaml
variables:
  - group: Android-Test-Config
```

### Method 3: Azure Key Vault (Enterprise)

For production environments, use Azure Key Vault:
1. Create Azure Key Vault
2. Store secrets in Key Vault
3. Link to Azure DevOps:
   - **Pipelines** → **Library** → **+ Variable group**
   - Toggle **Link secrets from an Azure key vault**

---

## ▶️ Running the Pipeline

### Manual Run
1. Go to **Pipelines** → **Pipelines**
2. Select your pipeline
3. Click **Run pipeline**
4. Choose branch and parameters
5. Click **Run**

### Automatic Triggers

The pipeline automatically runs on:
- Push to `main`, `master`, or `develop` branches
- Pull requests to these branches

### Disable Auto-Trigger

To run only manually, comment out triggers in `azure-pipelines.yml`:

```yaml
# trigger: none
# pr: none
```

---

## 📊 Viewing Reports

After pipeline execution, reports are available as artifacts:

### 1. Test Results
- Navigate to the pipeline run
- Click **Tests** tab
- View pass/fail statistics and trends

### 2. Screenshots
- Go to pipeline run → **Summary**
- Under **Artifacts**, click **test-screenshots**
- Download and view captured screenshots

### 3. Extent Reports
- Download **extent-report** artifact
- Open `Extent-report.html` in browser

### 4. TestNG Reports
- Download **testng-reports** artifact
- Open `index.html` in browser

### 5. Appium Logs
- Download **appium-logs** artifact
- Check `appium.log` for server logs

---

## 🐛 Troubleshooting

### Issue 1: "No Android devices found"

**Solution:**
```bash
# On agent machine
adb kill-server
adb start-server
adb devices

# Ensure USB debugging is enabled
# Check USB cable connection
```

### Issue 2: "Appium server failed to start"

**Solution:**
```bash
# Kill any existing Appium processes
taskkill /F /IM node.exe
# Or on Linux/Mac: killall node

# Start Appium manually to check for errors
appium --address 127.0.0.1 --port 4723
```

### Issue 3: "App not found or unable to install"

**Solution:**
- Ensure app is installed on device: `adb shell pm list packages | findstr condeco`
- Verify app package name matches: `com.condecosoftware.condeco`
- Check app activity is correct

### Issue 4: "Maven build fails in CI but works locally"

**Solution:**
```bash
# Clean local Maven cache
mvn clean install -U

# Ensure pom.xml has proper encoding
# Check Java version matches (11)
java -version
```

### Issue 5: "Tests timeout in pipeline"

**Solution:**
Update pipeline timeout in `azure-pipelines.yml`:
```yaml
jobs:
  - job: AndroidTests
    timeoutInMinutes: 120  # Increase from 90
```

### Issue 6: "Agent disconnects during test execution"

**Solution:**
- Configure agent to run as Windows service
- Increase agent timeout settings
- Check network stability

---

## 📝 Best Practices

### 1. Use Self-Hosted Agents for Physical Devices
- More reliable connections
- Better performance
- No execution time limits

### 2. Parameterize Test Configurations
Store device-specific configs in variables:
```yaml
variables:
  deviceName: '$(DEVICE_NAME)'  # From variable group
```

### 3. Archive Important Artifacts
Always publish:
- Screenshots (for debugging)
- Test reports (for analysis)
- Logs (for troubleshooting)

### 4. Implement Retry Logic
For flaky tests, configure retry in TestNG:
```xml
<suite name="..." retry-count="2">
```

### 5. Use Parallel Execution (Multiple Devices)
```yaml
strategy:
  matrix:
    Device1:
      deviceName: 'RZCXA08S2MX'
    Device2:
      deviceName: 'DEVICEID2'
```

### 6. Notification Setup
Configure notifications for test failures:
- **Project Settings** → **Notifications**
- Add rule for "Build completes" and "Test run completes"

---

## 🔄 Pipeline Stages Explained

### Stage 1: Build
- Installs Java JDK 11
- Compiles Maven project
- Publishes build artifacts

### Stage 2: Test
- Sets up Android SDK
- Installs Appium and drivers
- Detects Android device
- Starts Appium server
- Runs TestNG tests
- Publishes all reports and screenshots

### Stage 3: Report
- Aggregates all test artifacts
- Generates summary
- Publishes combined reports

---

## 📧 Support

For issues specific to:
- **Azure DevOps**: Check Azure DevOps documentation
- **Appium**: Visit http://appium.io/docs
- **Android SDK**: Check Android Developer docs
- **This Project**: Contact your team lead

---

## 🎯 Next Steps

1. ✅ Complete self-hosted agent setup (if using physical devices)
2. ✅ Configure environment variables
3. ✅ Run first pipeline execution
4. ✅ Review test results and reports
5. ✅ Set up notifications
6. ✅ Configure scheduled runs (if needed)

---

**Last Updated**: November 2025
**Pipeline Version**: 1.0
**Maintainer**: Eptura QA Team
