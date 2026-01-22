# CI/CD Pipeline Presentation - Slide Content
## Eptura Engage Android Automation

---

## SLIDE 1: Title Slide

**Eptura Engage Android**
**CI/CD Pipeline Architecture & Demo**

- Presenter: Ajay Jha
- Date: January 2026
- Project: Mobile Test Automation

---

## SLIDE 2: Agenda

1. 🎯 Project Overview
2. 🏗️ Pipeline Architecture
3. 🔄 CI/CD Workflow
4. 🛠️ Technology Stack
5. 📊 Test Reporting
6. ⚡ Key Features
7. 📈 Demo & Results
8. 🚀 Future Roadmap

---

## SLIDE 3: Project Overview

**What is Eptura Engage Android Automation?**

- 📱 Automated testing for Eptura Engage mobile app
- 🤖 BDD-based test framework (Cucumber + TestNG)
- ☁️ Cloud-integrated CI/CD pipeline on Azure DevOps
- 📦 APK sourced from Azure Blob Storage
- 🔄 Continuous testing on every code change

**Test Coverage:**
- Login functionality
- User Profile features
- More features in progress...

---

## SLIDE 4: High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CI/CD PIPELINE FLOW                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   [Git Push] ──▶ [Azure DevOps] ──▶ [Test Results]         │
│                                                              │
│   ┌────────┐   ┌────────┐   ┌────────┐   ┌────────┐        │
│   │ SETUP  │──▶│DOWNLOAD│──▶│ BUILD  │──▶│  TEST  │        │
│   │        │   │  APK   │   │        │   │        │        │
│   └────────┘   └────────┘   └────────┘   └────────┘        │
│       │             │            │            │              │
│       ▼             ▼            ▼            ▼              │
│   Java 11      Azure Blob    Maven       Emulator           │
│   Android SDK  Storage       Compile     Appium             │
│   Appium       SAS Token                 TestNG             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## SLIDE 5: Stage 1 - Setup Environment

**Components Installed:**

| Component | Version | Purpose |
|-----------|---------|---------|
| Java JDK | 11 | Runtime environment |
| Android SDK | API 30 | Emulator & tools |
| Appium | 3.0.0 | Mobile automation |
| UiAutomator2 | Latest | Android driver |

**Optimizations:**
- ✅ Maven dependency caching
- ✅ Pre-installed JDK on agent
- ✅ Non-rooted Play Store image

---

## SLIDE 6: Stage 2 - Download APK

**Azure Blob Storage Integration**

```
┌─────────────────────────────────────┐
│     AZURE BLOB STORAGE              │
│  ┌─────────────────────────────┐   │
│  │ Account: entstorage         │   │
│  │ Container: mobilebuilds     │   │
│  │ Path: Engage/Android/       │   │
│  │       EpturaEngage.apk      │   │
│  └─────────────────────────────┘   │
└─────────────────────────────────────┘
              │
              ▼ SAS Token Auth
┌─────────────────────────────────────┐
│  Python Script downloads APK        │
│  Verifies integrity & publishes     │
│  as pipeline artifact               │
└─────────────────────────────────────┘
```

---

## SLIDE 7: Stage 3 - Build

**Maven Build Process**

```xml
<!-- Key Dependencies -->
├── io.appium:java-client:8.6.0
├── selenium-java:4.16.1
├── cucumber-java:7.27.2
├── testng:7.11.0
├── extentreports:5.1.1
└── allure-cucumber7-jvm:2.29.0
```

**Commands:**
- `mvn clean compile`
- Skip tests during compile
- Cache dependencies for speed

---

## SLIDE 8: Stage 4 - Test Execution

**Emulator Configuration:**
| Setting | Value |
|---------|-------|
| Device | Pixel 4 |
| Android | API 30 (Android 11) |
| Resolution | 1080x2280 |
| System Image | google_apis_playstore |
| Memory | 2048 MB |

**Test Framework:**
- TestNG for test orchestration
- Cucumber for BDD scenarios
- Appium for mobile automation
- 120-minute timeout

---

## SLIDE 9: Test Framework Structure

```
src/
├── main/java/
│   └── com/client/app/pages/
│       └── LoginPage.java          ← Page Objects
│
└── test/java/
    ├── FeatureFiles/
    │   ├── Login.feature           ← BDD Scenarios
    │   └── UserProfile.feature
    │
    └── TestRunner/
        ├── LoginTestRunner.java    ← Test Runners
        └── UserProfileTestRunner.java
```

---

## SLIDE 10: Reporting & Artifacts

**Reports Generated:**

| Report | Format | Purpose |
|--------|--------|---------|
| Extent Report | HTML | Rich visual dashboard |
| TestNG | XML/HTML | Test execution details |
| Cucumber | JSON/HTML | BDD feature status |
| Allure | HTML | Interactive analytics |
| JUnit | XML | Azure DevOps integration |

**Artifacts Published:**
- 📦 AndroidAPK
- 📸 InstallationScreenshots
- 📊 TestExecutionReports
- 🖼️ TestScreenshots

---

## SLIDE 11: Key Features

✅ **Automated APK Management**
- No manual APK uploads
- Always tests latest build

✅ **Non-Rooted Environment**
- Production-like testing
- No root detection issues

✅ **Comprehensive Screenshots**
- Every test captures screenshot
- Installation process documented

✅ **Multi-Format Reporting**
- Extent, TestNG, Cucumber, Allure
- Azure DevOps test dashboard

✅ **Robust Error Handling**
- Timeout management
- Detailed logging

---

## SLIDE 12: Pipeline Triggers

**Automatic Triggers:**

| Trigger Type | Branches | Action |
|--------------|----------|--------|
| Push | main, master, develop | Full test run |
| Pull Request | main, master, develop | Validation tests |
| Manual | Any | On-demand execution |

**Exclusions:**
- README.md changes
- docs/* folder changes

---

## SLIDE 13: Security & Configuration

**Public Variables:**
```
AZURE_STORAGE_ACCOUNT: entstorage
AZURE_STORAGE_CONTAINER: mobilebuilds
APK_BLOB_NAME: Engage/Android/EpturaEngage.apk
APPIUM_VERSION: 3.0.0
```

**Secret Variables (Secured in Azure DevOps):**
```
🔒 AZURE_SAS_TOKEN: ********
```

---

## SLIDE 14: Performance Optimizations

| Optimization | Benefit |
|--------------|---------|
| Maven Caching | 50-70% faster builds |
| KVM Acceleration | Faster emulator boot |
| Disabled Animations | Faster UI interactions |
| SwiftShader GPU | CI-optimized rendering |
| Wipe Data on Start | Clean test state |

---

## SLIDE 15: Demo - Live Pipeline Run

**Demo Steps:**
1. Show Azure DevOps pipeline
2. Trigger manual run
3. Walk through stages
4. View test results
5. Download artifacts
6. Show Extent Report

---

## SLIDE 16: Results & Metrics

**Current Test Suite:**
- ✅ Login Tests
- ✅ User Profile Tests
- 🔄 More in progress...

**Pipeline Metrics:**
- Average Run Time: ~30-45 mins
- Success Rate: Tracking
- Test Coverage: Expanding

---

## SLIDE 17: Future Roadmap

| Enhancement | Priority | Timeline |
|-------------|----------|----------|
| Parallel Test Execution | High | Q1 2026 |
| Real Device Integration | Medium | Q2 2026 |
| Slack/Teams Notifications | Medium | Q1 2026 |
| Visual Regression Testing | Low | Q3 2026 |
| Performance Testing | Low | Q3 2026 |

---

## SLIDE 18: Summary

**What We Achieved:**
- ✅ Fully automated CI/CD pipeline
- ✅ Azure Blob Storage integration
- ✅ BDD test framework
- ✅ Comprehensive reporting
- ✅ Screenshot documentation
- ✅ Scalable architecture

**Impact:**
- 🚀 Faster release cycles
- 🔍 Early bug detection
- 📊 Better visibility
- 🤝 Team collaboration

---

## SLIDE 19: Q&A

**Questions?**

**Resources:**
- GitHub: ajayjha-eptura/EpturaEngageAutomation-Android
- Pipeline: Azure DevOps
- Documentation: /docs folder

---

## SLIDE 20: Thank You

**Thank You!**

Contact: Ajay Jha
Project: Eptura Engage Android Automation

*Empowering Quality Through Automation*
