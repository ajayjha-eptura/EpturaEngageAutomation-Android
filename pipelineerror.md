2025-11-24T13:18:57.4823374Z ##[section]Starting: Setup Android SDK and Create Emulator with Google Play
2025-11-24T13:18:57.4828727Z ==============================================================================
2025-11-24T13:18:57.4828832Z Task         : Bash
2025-11-24T13:18:57.4828880Z Description  : Run a Bash script on macOS, Linux, or Windows
2025-11-24T13:18:57.4828954Z Version      : 3.259.0
2025-11-24T13:18:57.4829004Z Author       : Microsoft Corporation
2025-11-24T13:18:57.4829067Z Help         : https://docs.microsoft.com/azure/devops/pipelines/tasks/utility/bash
2025-11-24T13:18:57.4829145Z ==============================================================================
2025-11-24T13:18:57.6356751Z Generating script.
2025-11-24T13:18:57.6468573Z [command]"C:\Program Files\Git\bin\bash.exe" -c pwd
2025-11-24T13:18:57.6784035Z /d/a/_temp
2025-11-24T13:18:57.6815962Z 
2025-11-24T13:18:57.6843565Z [command]"C:\Program Files\Git\bin\bash.exe" -c pwd
2025-11-24T13:18:57.7108321Z /d/a
2025-11-24T13:18:57.7134083Z 
2025-11-24T13:18:57.7139769Z ========================== Starting Command Output ===========================
2025-11-24T13:18:57.7150760Z [command]"C:\Program Files\Git\bin\bash.exe" /d/a/_temp/8669f2f1-9821-4bbf-80c0-0b8ca03d3f38.sh
2025-11-24T13:18:57.7418256Z 📱 Configuring Android SDK with Google Play support...
2025-11-24T13:18:57.7418605Z ANDROID_HOME: C:\Android\android-sdk
2025-11-24T13:18:57.7418840Z ANDROID_SDK_ROOT: C:\Android\android-sdk
2025-11-24T13:18:57.7563195Z 📋 Android SDK structure:
2025-11-24T13:18:57.8491564Z total 84
2025-11-24T13:18:57.8492099Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:20 .
2025-11-24T13:18:57.8492623Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:18:57.8493196Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:22 .temp
2025-11-24T13:18:57.8495020Z -rw-r--r-- 1 VssAdministrator 197121  1698 Nov  2 23:11 android-sdk-licenses.zip
2025-11-24T13:18:57.8500439Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:18 build-tools
2025-11-24T13:18:57.8501059Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:20 cmake
2025-11-24T13:18:57.8501704Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 cmdline-tools
2025-11-24T13:18:57.8502160Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:19 emulator
2025-11-24T13:18:57.8502588Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:19 extras
2025-11-24T13:18:57.8502995Z drwxr-xr-x 1 VssAdministrator 197121     0 Jun 23  2021 licenses
2025-11-24T13:18:57.8503404Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:22 ndk
2025-11-24T13:18:57.8503836Z -rw-r--r-- 1 VssAdministrator 197121 37812 Nov  2 23:11 packages-list.txt
2025-11-24T13:18:57.8504292Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 platform-tools
2025-11-24T13:18:57.8504784Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:17 platforms
2025-11-24T13:18:57.8505325Z 🔍 Searching for sdkmanager...
2025-11-24T13:18:57.8551975Z Searching in cmdline-tools directory...
2025-11-24T13:18:58.5154056Z ❌ sdkmanager not found in cmdline-tools
2025-11-24T13:18:58.5154758Z Available cmdline-tools structure:
2025-11-24T13:18:59.0887833Z C:\Android\android-sdk/cmdline-tools:
2025-11-24T13:18:59.0888349Z total 4
2025-11-24T13:18:59.0888699Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.0889145Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:20 ..
2025-11-24T13:18:59.0889582Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 12.0
2025-11-24T13:18:59.0890032Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 7.0
2025-11-24T13:18:59.0890500Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 latest
2025-11-24T13:18:59.0890706Z 
2025-11-24T13:18:59.0890955Z C:\Android\android-sdk/cmdline-tools/12.0:
2025-11-24T13:18:59.0891173Z total 133
2025-11-24T13:18:59.0891442Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0891739Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.0892071Z -rw-r--r-- 1 VssAdministrator 197121 120464 Jan  1  2010 NOTICE.txt
2025-11-24T13:18:59.0894351Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 bin
2025-11-24T13:18:59.0894730Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 lib
2025-11-24T13:18:59.0895105Z -rw-r--r-- 1 VssAdministrator 197121     86 Jan  1  2010 source.properties
2025-11-24T13:18:59.0895268Z 
2025-11-24T13:18:59.0895532Z C:\Android\android-sdk/cmdline-tools/12.0/bin:
2025-11-24T13:18:59.0895802Z total 36
2025-11-24T13:18:59.0896052Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 .
2025-11-24T13:18:59.0896336Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 ..
2025-11-24T13:18:59.0896620Z -rw-r--r-- 1 VssAdministrator 197121 2297 Jan  1  2010 apkanalyzer.bat
2025-11-24T13:18:59.0896907Z -rw-r--r-- 1 VssAdministrator 197121 2288 Jan  1  2010 avdmanager.bat
2025-11-24T13:18:59.0897202Z -rw-r--r-- 1 VssAdministrator 197121 2242 Jan  1  2010 lint.bat
2025-11-24T13:18:59.0897422Z -rw-r--r-- 1 VssAdministrator 197121 2222 Jan  1  2010 profgen.bat
2025-11-24T13:18:59.0897612Z -rw-r--r-- 1 VssAdministrator 197121 2295 Jan  1  2010 resourceshrinker.bat
2025-11-24T13:18:59.0897797Z -rw-r--r-- 1 VssAdministrator 197121 2222 Jan  1  2010 retrace.bat
2025-11-24T13:18:59.0897972Z -rw-r--r-- 1 VssAdministrator 197121 2285 Jan  1  2010 screenshot2.bat
2025-11-24T13:18:59.0898149Z -rw-r--r-- 1 VssAdministrator 197121 2295 Jan  1  2010 sdkmanager.bat
2025-11-24T13:18:59.0898229Z 
2025-11-24T13:18:59.0898361Z C:\Android\android-sdk/cmdline-tools/12.0/lib:
2025-11-24T13:18:59.0898497Z total 15010
2025-11-24T13:18:59.0898648Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 .
2025-11-24T13:18:59.0898833Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 ..
2025-11-24T13:18:59.0899006Z -rw-r--r-- 1 VssAdministrator 197121      202 Jan  1  2010 README
2025-11-24T13:18:59.0899189Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 analytics-library
2025-11-24T13:18:59.0899386Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 annotations
2025-11-24T13:18:59.0900058Z -rw-r--r-- 1 VssAdministrator 197121     4218 Jan  1  2010 apkanalyzer-classpath.jar
2025-11-24T13:18:59.0900252Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 apkparser
2025-11-24T13:18:59.0900457Z -rw-r--r-- 1 VssAdministrator 197121     3008 Jan  1  2010 avdmanager-classpath.jar
2025-11-24T13:18:59.0900651Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 build-system
2025-11-24T13:18:59.0900848Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 common
2025-11-24T13:18:59.0901035Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 ddmlib
2025-11-24T13:18:59.0901211Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 device_validator
2025-11-24T13:18:59.0901391Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 external
2025-11-24T13:18:59.0901732Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 layoutlib-api
2025-11-24T13:18:59.0901905Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 lint
2025-11-24T13:18:59.0902075Z -rw-r--r-- 1 VssAdministrator 197121     4198 Jan  1  2010 lint-classpath.jar
2025-11-24T13:18:59.0902246Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 misc
2025-11-24T13:18:59.0902412Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 profgen
2025-11-24T13:18:59.0902582Z -rw-r--r-- 1 VssAdministrator 197121      877 Jan  1  2010 profgen-classpath.jar
2025-11-24T13:18:59.0902748Z -rw-r--r-- 1 VssAdministrator 197121 15305887 Jan  1  2010 r8.jar
2025-11-24T13:18:59.0902919Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 repository
2025-11-24T13:18:59.0903097Z -rw-r--r-- 1 VssAdministrator 197121     3609 Jan  1  2010 resourceshrinker-classpath.jar
2025-11-24T13:18:59.0903273Z -rw-r--r-- 1 VssAdministrator 197121      283 Jan  1  2010 retrace-classpath.jar
2025-11-24T13:18:59.0903450Z -rw-r--r-- 1 VssAdministrator 197121     1648 Jan  1  2010 screenshot2-classpath.jar
2025-11-24T13:18:59.0903623Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 sdk-common
2025-11-24T13:18:59.0904089Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 sdklib
2025-11-24T13:18:59.0904265Z -rw-r--r-- 1 VssAdministrator 197121     3008 Jan  1  2010 sdkmanager-classpath.jar
2025-11-24T13:18:59.0904349Z 
2025-11-24T13:18:59.0904480Z C:\Android\android-sdk/cmdline-tools/12.0/lib/analytics-library:
2025-11-24T13:18:59.0904606Z total 8
2025-11-24T13:18:59.0904746Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0904911Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0905076Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 protos
2025-11-24T13:18:59.0905242Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 shared
2025-11-24T13:18:59.0905417Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 tracker
2025-11-24T13:18:59.0905489Z 
2025-11-24T13:18:59.0905620Z C:\Android\android-sdk/cmdline-tools/12.0/lib/analytics-library/protos:
2025-11-24T13:18:59.0905775Z total 0
2025-11-24T13:18:59.0905914Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0906075Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0906236Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 src
2025-11-24T13:18:59.0906315Z 
2025-11-24T13:18:59.0906449Z C:\Android\android-sdk/cmdline-tools/12.0/lib/analytics-library/protos/src:
2025-11-24T13:18:59.0906580Z total 0
2025-11-24T13:18:59.0906712Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0906878Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0907041Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 main
2025-11-24T13:18:59.0907114Z 
2025-11-24T13:18:59.0907256Z C:\Android\android-sdk/cmdline-tools/12.0/lib/analytics-library/protos/src/main:
2025-11-24T13:18:59.0907393Z total 0
2025-11-24T13:18:59.0907521Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0907680Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0907905Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 proto
2025-11-24T13:18:59.0907981Z 
2025-11-24T13:18:59.0908144Z C:\Android\android-sdk/cmdline-tools/12.0/lib/analytics-library/protos/src/main/proto:
2025-11-24T13:18:59.0908294Z total 7196
2025-11-24T13:18:59.0908435Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.0908602Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.0908767Z -rw-r--r-- 1 VssAdministrator 197121 7366170 Jan  1  2010 proto.jar
2025-11-24T13:18:59.0908842Z 
2025-11-24T13:18:59.0908977Z C:\Android\android-sdk/cmdline-tools/12.0/lib/analytics-library/shared:
2025-11-24T13:18:59.0909110Z total 124
2025-11-24T13:18:59.0909252Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0909422Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0909598Z -rw-r--r-- 1 VssAdministrator 197121 126152 Jan  1  2010 tools.analytics-shared.jar
2025-11-24T13:18:59.0909687Z 
2025-11-24T13:18:59.0909823Z C:\Android\android-sdk/cmdline-tools/12.0/lib/analytics-library/tracker:
2025-11-24T13:18:59.0909961Z total 44
2025-11-24T13:18:59.0910099Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0910272Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0910454Z -rw-r--r-- 1 VssAdministrator 197121 41892 Jan  1  2010 tools.analytics-tracker.jar
2025-11-24T13:18:59.0910532Z 
2025-11-24T13:18:59.0910663Z C:\Android\android-sdk/cmdline-tools/12.0/lib/annotations:
2025-11-24T13:18:59.0910791Z total 20
2025-11-24T13:18:59.0910924Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0911086Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0911257Z -rw-r--r-- 1 VssAdministrator 197121 10597 Jan  1  2010 annotations.jar
2025-11-24T13:18:59.0911329Z 
2025-11-24T13:18:59.0911456Z C:\Android\android-sdk/cmdline-tools/12.0/lib/apkparser:
2025-11-24T13:18:59.0911631Z total 92
2025-11-24T13:18:59.0911766Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0911930Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0912096Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 analyzer
2025-11-24T13:18:59.0912271Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 cli
2025-11-24T13:18:59.0912441Z -rw-r--r-- 1 VssAdministrator 197121 84816 Jan  1  2010 tools.binary-resources.jar
2025-11-24T13:18:59.0912519Z 
2025-11-24T13:18:59.0912650Z C:\Android\android-sdk/cmdline-tools/12.0/lib/apkparser/analyzer:
2025-11-24T13:18:59.0912783Z total 108
2025-11-24T13:18:59.0912917Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0913079Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0913239Z -rw-r--r-- 1 VssAdministrator 197121 109104 Jan  1  2010 analyzer.jar
2025-11-24T13:18:59.0913313Z 
2025-11-24T13:18:59.0913441Z C:\Android\android-sdk/cmdline-tools/12.0/lib/apkparser/cli:
2025-11-24T13:18:59.0913568Z total 68
2025-11-24T13:18:59.0913705Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0913866Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0914030Z -rw-r--r-- 1 VssAdministrator 197121 66143 Jan  1  2010 analyzer-cli.jar
2025-11-24T13:18:59.0914119Z 
2025-11-24T13:18:59.0914242Z C:\Android\android-sdk/cmdline-tools/12.0/lib/build-system:
2025-11-24T13:18:59.0914372Z total 256
2025-11-24T13:18:59.0914506Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0914669Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0914836Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 aapt2-proto
2025-11-24T13:18:59.0915017Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 builder-model
2025-11-24T13:18:59.0915189Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 shrinker
2025-11-24T13:18:59.0915366Z -rw-r--r-- 1 VssAdministrator 197121 249365 Jan  1  2010 tools.manifest-merger.jar
2025-11-24T13:18:59.0915485Z 
2025-11-24T13:18:59.0915618Z C:\Android\android-sdk/cmdline-tools/12.0/lib/build-system/aapt2-proto:
2025-11-24T13:18:59.0915751Z total 784
2025-11-24T13:18:59.0915884Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0916052Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0916218Z -rw-r--r-- 1 VssAdministrator 197121 797597 Jan  1  2010 aapt2-proto.jar
2025-11-24T13:18:59.0916290Z 
2025-11-24T13:18:59.0916426Z C:\Android\android-sdk/cmdline-tools/12.0/lib/build-system/builder-model:
2025-11-24T13:18:59.0916561Z total 124
2025-11-24T13:18:59.0916693Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0916857Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0917027Z -rw-r--r-- 1 VssAdministrator 197121 121670 Jan  1  2010 builder-model.jar
2025-11-24T13:18:59.0917104Z 
2025-11-24T13:18:59.0917232Z C:\Android\android-sdk/cmdline-tools/12.0/lib/build-system/shrinker:
2025-11-24T13:18:59.0917367Z total 156
2025-11-24T13:18:59.0917498Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0917660Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0917826Z -rw-r--r-- 1 VssAdministrator 197121 153890 Jan  1  2010 libshrinker.jar
2025-11-24T13:18:59.0917904Z 
2025-11-24T13:18:59.0918026Z C:\Android\android-sdk/cmdline-tools/12.0/lib/common:
2025-11-24T13:18:59.0918148Z total 544
2025-11-24T13:18:59.0918284Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0918446Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0918613Z -rw-r--r-- 1 VssAdministrator 197121 545729 Jan  1  2010 tools.common.jar
2025-11-24T13:18:59.0918692Z 
2025-11-24T13:18:59.0918812Z C:\Android\android-sdk/cmdline-tools/12.0/lib/ddmlib:
2025-11-24T13:18:59.0918979Z total 616
2025-11-24T13:18:59.0919112Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0919273Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0919442Z -rw-r--r-- 1 VssAdministrator 197121 621017 Jan  1  2010 tools.ddmlib.jar
2025-11-24T13:18:59.0919513Z 
2025-11-24T13:18:59.0919637Z C:\Android\android-sdk/cmdline-tools/12.0/lib/device_validator:
2025-11-24T13:18:59.0919771Z total 64
2025-11-24T13:18:59.0919904Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0920065Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0920228Z -rw-r--r-- 1 VssAdministrator 197121 54576 Jan  1  2010 tools.dvlib.jar
2025-11-24T13:18:59.0920302Z 
2025-11-24T13:18:59.0920427Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external:
2025-11-24T13:18:59.0920554Z total 16
2025-11-24T13:18:59.0920691Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0920852Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0921027Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 archive-patcher
2025-11-24T13:18:59.0921197Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 com
2025-11-24T13:18:59.0921370Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-codec
2025-11-24T13:18:59.0921542Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-io
2025-11-24T13:18:59.0921716Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-logging
2025-11-24T13:18:59.0921887Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jakarta
2025-11-24T13:18:59.0922058Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 javax
2025-11-24T13:18:59.0922224Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 lint-psi
2025-11-24T13:18:59.0922387Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 net
2025-11-24T13:18:59.0922548Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 org
2025-11-24T13:18:59.0922720Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xerces
2025-11-24T13:18:59.0922928Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xml-apis
2025-11-24T13:18:59.0923001Z 
2025-11-24T13:18:59.0923139Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/archive-patcher:
2025-11-24T13:18:59.0923271Z total 128
2025-11-24T13:18:59.0923403Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0923565Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0923735Z -rw-r--r-- 1 VssAdministrator 197121 12156 Jan  1  2010 explainer.jar
2025-11-24T13:18:59.0923895Z -rw-r--r-- 1 VssAdministrator 197121 84159 Jan  1  2010 generator.jar
2025-11-24T13:18:59.0924054Z -rw-r--r-- 1 VssAdministrator 197121 28234 Jan  1  2010 shared.jar
2025-11-24T13:18:59.0924129Z 
2025-11-24T13:18:59.0924255Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com:
2025-11-24T13:18:59.0924379Z total 8
2025-11-24T13:18:59.0924563Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0924732Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0924899Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 android
2025-11-24T13:18:59.0925062Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 beust
2025-11-24T13:18:59.0925230Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 google
2025-11-24T13:18:59.0925401Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 sun
2025-11-24T13:18:59.0925471Z 
2025-11-24T13:18:59.0925599Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/android:
2025-11-24T13:18:59.0925734Z total 0
2025-11-24T13:18:59.0925867Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0926027Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0926189Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 tools
2025-11-24T13:18:59.0926266Z 
2025-11-24T13:18:59.0926397Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/android/tools:
2025-11-24T13:18:59.0926809Z total 0
2025-11-24T13:18:59.0926946Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0927119Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0927288Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 smali
2025-11-24T13:18:59.0927360Z 
2025-11-24T13:18:59.0927505Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/android/tools/smali:
2025-11-24T13:18:59.0927641Z total 0
2025-11-24T13:18:59.0927774Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0927935Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0928112Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 smali-baksmali
2025-11-24T13:18:59.0928289Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 smali-dexlib2
2025-11-24T13:18:59.0928461Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 smali-util
2025-11-24T13:18:59.0928542Z 
2025-11-24T13:18:59.0928685Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/android/tools/smali/smali-baksmali:
2025-11-24T13:18:59.0928839Z total 0
2025-11-24T13:18:59.0928971Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0929136Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0929299Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.0.3
2025-11-24T13:18:59.0929371Z 
2025-11-24T13:18:59.0929519Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/android/tools/smali/smali-baksmali/3.0.3:
2025-11-24T13:18:59.0929666Z total 132
2025-11-24T13:18:59.0929801Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0929963Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0930244Z -rw-r--r-- 1 VssAdministrator 197121 133360 Jan  1  2010 smali-baksmali-3.0.3.jar
2025-11-24T13:18:59.0930402Z 
2025-11-24T13:18:59.0930684Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/android/tools/smali/smali-dexlib2:
2025-11-24T13:18:59.0930974Z total 0
2025-11-24T13:18:59.0931237Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0931673Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0932007Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.0.3
2025-11-24T13:18:59.0932160Z 
2025-11-24T13:18:59.0932441Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/android/tools/smali/smali-dexlib2/3.0.3:
2025-11-24T13:18:59.0932736Z total 1152
2025-11-24T13:18:59.0933017Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.0933336Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.0933684Z -rw-r--r-- 1 VssAdministrator 197121 1178232 Jan  1  2010 smali-dexlib2-3.0.3.jar
2025-11-24T13:18:59.0933849Z 
2025-11-24T13:18:59.0934132Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/android/tools/smali/smali-util:
2025-11-24T13:18:59.0934414Z total 0
2025-11-24T13:18:59.0934677Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0935016Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0935353Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.0.3
2025-11-24T13:18:59.0935501Z 
2025-11-24T13:18:59.0935778Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/android/tools/smali/smali-util/3.0.3:
2025-11-24T13:18:59.0936070Z total 36
2025-11-24T13:18:59.0936211Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0936379Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0936547Z -rw-r--r-- 1 VssAdministrator 197121 33447 Jan  1  2010 smali-util-3.0.3.jar
2025-11-24T13:18:59.0936626Z 
2025-11-24T13:18:59.0936754Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/beust:
2025-11-24T13:18:59.0936882Z total 0
2025-11-24T13:18:59.0937018Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0937181Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0937344Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jcommander
2025-11-24T13:18:59.0937530Z 
2025-11-24T13:18:59.0937666Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/beust/jcommander:
2025-11-24T13:18:59.0937929Z total 0
2025-11-24T13:18:59.0938511Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0938707Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0938871Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.78
2025-11-24T13:18:59.0938943Z 
2025-11-24T13:18:59.0939088Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/beust/jcommander/1.78:
2025-11-24T13:18:59.0939231Z total 84
2025-11-24T13:18:59.0939368Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0939533Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0939707Z -rw-r--r-- 1 VssAdministrator 197121 83782 Jan  1  2010 jcommander-1.78.jar
2025-11-24T13:18:59.0939781Z 
2025-11-24T13:18:59.0939909Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google:
2025-11-24T13:18:59.0940051Z total 4
2025-11-24T13:18:59.0940183Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0940343Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0940506Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 code
2025-11-24T13:18:59.0940678Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 errorprone
2025-11-24T13:18:59.0940846Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 guava
2025-11-24T13:18:59.0941011Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 j2objc
2025-11-24T13:18:59.0941175Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jimfs
2025-11-24T13:18:59.0941347Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 protobuf
2025-11-24T13:18:59.0941418Z 
2025-11-24T13:18:59.0941558Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/code:
2025-11-24T13:18:59.0941694Z total 4
2025-11-24T13:18:59.0941824Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0942071Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0942235Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 findbugs
2025-11-24T13:18:59.0942400Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 gson
2025-11-24T13:18:59.0942478Z 
2025-11-24T13:18:59.0942612Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/code/findbugs:
2025-11-24T13:18:59.0942749Z total 0
2025-11-24T13:18:59.0942885Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0943044Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0943207Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jsr305
2025-11-24T13:18:59.0943288Z 
2025-11-24T13:18:59.0943427Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/code/findbugs/jsr305:
2025-11-24T13:18:59.0943564Z total 0
2025-11-24T13:18:59.0943694Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0943863Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0944028Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.0.2
2025-11-24T13:18:59.0944099Z 
2025-11-24T13:18:59.0944243Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/code/findbugs/jsr305/3.0.2:
2025-11-24T13:18:59.0944389Z total 20
2025-11-24T13:18:59.0944520Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0944685Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0944854Z -rw-r--r-- 1 VssAdministrator 197121 19936 Jan  1  2010 jsr305-3.0.2.jar
2025-11-24T13:18:59.0944926Z 
2025-11-24T13:18:59.0945059Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/code/gson:
2025-11-24T13:18:59.0945200Z total 0
2025-11-24T13:18:59.0945331Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0945490Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0945652Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 gson
2025-11-24T13:18:59.0945779Z 
2025-11-24T13:18:59.0945916Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/code/gson/gson:
2025-11-24T13:18:59.0946053Z total 0
2025-11-24T13:18:59.0946185Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0946351Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0946513Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.10
2025-11-24T13:18:59.0946583Z 
2025-11-24T13:18:59.0946728Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/code/gson/gson/2.10:
2025-11-24T13:18:59.0946868Z total 280
2025-11-24T13:18:59.0947004Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0947167Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0947336Z -rw-r--r-- 1 VssAdministrator 197121 286235 Jan  1  2010 gson-2.10.jar
2025-11-24T13:18:59.0947406Z 
2025-11-24T13:18:59.0947539Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/errorprone:
2025-11-24T13:18:59.0947683Z total 4
2025-11-24T13:18:59.0947811Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0947969Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0948140Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 error_prone_annotations
2025-11-24T13:18:59.0948228Z 
2025-11-24T13:18:59.0948373Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/errorprone/error_prone_annotations:
2025-11-24T13:18:59.0948520Z total 0
2025-11-24T13:18:59.0948657Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0948815Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0948976Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.16
2025-11-24T13:18:59.0949051Z 
2025-11-24T13:18:59.0949200Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/errorprone/error_prone_annotations/2.16:
2025-11-24T13:18:59.0949352Z total 16
2025-11-24T13:18:59.0949486Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0949695Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0949868Z -rw-r--r-- 1 VssAdministrator 197121 16016 Jan  1  2010 error_prone_annotations-2.16.jar
2025-11-24T13:18:59.0949949Z 
2025-11-24T13:18:59.0950086Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/guava:
2025-11-24T13:18:59.0950218Z total 4
2025-11-24T13:18:59.0950350Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0950509Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0950682Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 failureaccess
2025-11-24T13:18:59.0950852Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 guava
2025-11-24T13:18:59.0951021Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 listenablefuture
2025-11-24T13:18:59.0951103Z 
2025-11-24T13:18:59.0951239Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/guava/failureaccess:
2025-11-24T13:18:59.0951378Z total 0
2025-11-24T13:18:59.0951507Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0951671Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0951831Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.0.1
2025-11-24T13:18:59.0951901Z 
2025-11-24T13:18:59.0952039Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/guava/failureaccess/1.0.1:
2025-11-24T13:18:59.0952186Z total 8
2025-11-24T13:18:59.0952316Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 .
2025-11-24T13:18:59.0952477Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 ..
2025-11-24T13:18:59.0952645Z -rw-r--r-- 1 VssAdministrator 197121 4617 Jan  1  2010 failureaccess-1.0.1.jar
2025-11-24T13:18:59.0952724Z 
2025-11-24T13:18:59.0952856Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/guava/guava:
2025-11-24T13:18:59.0952987Z total 0
2025-11-24T13:18:59.0953170Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0953332Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0953496Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 31.1-jre
2025-11-24T13:18:59.0953573Z 
2025-11-24T13:18:59.0953713Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/guava/guava/31.1-jre:
2025-11-24T13:18:59.0953855Z total 2892
2025-11-24T13:18:59.0953992Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.0954160Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.0954349Z -rw-r--r-- 1 VssAdministrator 197121 2959479 Jan  1  2010 guava-31.1-jre.jar
2025-11-24T13:18:59.0954423Z 
2025-11-24T13:18:59.0954569Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/guava/listenablefuture:
2025-11-24T13:18:59.0954710Z total 0
2025-11-24T13:18:59.0954839Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0954999Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0955189Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 9999.0-empty-to-avoid-conflict-with-guava
2025-11-24T13:18:59.0955280Z 
2025-11-24T13:18:59.0955442Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava:
2025-11-24T13:18:59.0955612Z total 4
2025-11-24T13:18:59.0955744Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 .
2025-11-24T13:18:59.0955913Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 ..
2025-11-24T13:18:59.0956101Z -rw-r--r-- 1 VssAdministrator 197121 2199 Jan  1  2010 listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
2025-11-24T13:18:59.0956205Z 
2025-11-24T13:18:59.0956337Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/j2objc:
2025-11-24T13:18:59.0956470Z total 4
2025-11-24T13:18:59.0956604Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0956764Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0956978Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 j2objc-annotations
2025-11-24T13:18:59.0957062Z 
2025-11-24T13:18:59.0957202Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/j2objc/j2objc-annotations:
2025-11-24T13:18:59.0957341Z total 0
2025-11-24T13:18:59.0957472Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0957638Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0957799Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.3
2025-11-24T13:18:59.0957870Z 
2025-11-24T13:18:59.0958019Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/j2objc/j2objc-annotations/1.3:
2025-11-24T13:18:59.0958164Z total 12
2025-11-24T13:18:59.0958296Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 .
2025-11-24T13:18:59.0958458Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 ..
2025-11-24T13:18:59.0958633Z -rw-r--r-- 1 VssAdministrator 197121 8781 Jan  1  2010 j2objc-annotations-1.3.jar
2025-11-24T13:18:59.0958712Z 
2025-11-24T13:18:59.0958844Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/jimfs:
2025-11-24T13:18:59.0958985Z total 4
2025-11-24T13:18:59.0959116Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0959275Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0959438Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jimfs
2025-11-24T13:18:59.0959516Z 
2025-11-24T13:18:59.0959651Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/jimfs/jimfs:
2025-11-24T13:18:59.0959785Z total 0
2025-11-24T13:18:59.0959916Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0960085Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0960247Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.1
2025-11-24T13:18:59.0960318Z 
2025-11-24T13:18:59.0960461Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/jimfs/jimfs/1.1:
2025-11-24T13:18:59.0960940Z total 204
2025-11-24T13:18:59.0961083Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0961252Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0961424Z -rw-r--r-- 1 VssAdministrator 197121 206691 Jan  1  2010 jimfs-1.1.jar
2025-11-24T13:18:59.0961495Z 
2025-11-24T13:18:59.0961628Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/protobuf:
2025-11-24T13:18:59.0961768Z total 4
2025-11-24T13:18:59.0961898Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0962058Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0962225Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 protobuf-java
2025-11-24T13:18:59.0962307Z 
2025-11-24T13:18:59.0962446Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/protobuf/protobuf-java:
2025-11-24T13:18:59.0962587Z total 0
2025-11-24T13:18:59.0962725Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0962888Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0963051Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.19.3
2025-11-24T13:18:59.0963128Z 
2025-11-24T13:18:59.0963272Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/google/protobuf/protobuf-java/3.19.3:
2025-11-24T13:18:59.0963419Z total 1644
2025-11-24T13:18:59.0963557Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.0963723Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.0963902Z -rw-r--r-- 1 VssAdministrator 197121 1681866 Jan  1  2010 protobuf-java-3.19.3.jar
2025-11-24T13:18:59.0963980Z 
2025-11-24T13:18:59.0964106Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun:
2025-11-24T13:18:59.0964236Z total 0
2025-11-24T13:18:59.0964383Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0964542Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0964712Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 activation
2025-11-24T13:18:59.0965132Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 istack
2025-11-24T13:18:59.0965302Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xml
2025-11-24T13:18:59.0965373Z 
2025-11-24T13:18:59.0965512Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun/activation:
2025-11-24T13:18:59.0965647Z total 0
2025-11-24T13:18:59.0965779Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0965939Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0966114Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 javax.activation
2025-11-24T13:18:59.0966193Z 
2025-11-24T13:18:59.0966336Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun/activation/javax.activation:
2025-11-24T13:18:59.0966481Z total 0
2025-11-24T13:18:59.0966610Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0966772Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0966938Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.2.0
2025-11-24T13:18:59.0967015Z 
2025-11-24T13:18:59.0967159Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun/activation/javax.activation/1.2.0:
2025-11-24T13:18:59.0967304Z total 80
2025-11-24T13:18:59.0967443Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0967606Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0967775Z -rw-r--r-- 1 VssAdministrator 197121 78030 Jan  1  2010 javax.activation-1.2.0.jar
2025-11-24T13:18:59.0967858Z 
2025-11-24T13:18:59.0967988Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun/istack:
2025-11-24T13:18:59.0968119Z total 0
2025-11-24T13:18:59.0968249Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0968413Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0968587Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 istack-commons-runtime
2025-11-24T13:18:59.0968930Z 
2025-11-24T13:18:59.0969078Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun/istack/istack-commons-runtime:
2025-11-24T13:18:59.0969227Z total 0
2025-11-24T13:18:59.0969358Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0969520Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0969688Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.0.8
2025-11-24T13:18:59.0969760Z 
2025-11-24T13:18:59.0969904Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun/istack/istack-commons-runtime/3.0.8:
2025-11-24T13:18:59.0970049Z total 28
2025-11-24T13:18:59.0970188Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0970358Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0970531Z -rw-r--r-- 1 VssAdministrator 197121 27156 Jan  1  2010 istack-commons-runtime-3.0.8.jar
2025-11-24T13:18:59.0970620Z 
2025-11-24T13:18:59.0970748Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun/xml:
2025-11-24T13:18:59.0970877Z total 0
2025-11-24T13:18:59.0971009Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0971176Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0971363Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 fastinfoset
2025-11-24T13:18:59.0971438Z 
2025-11-24T13:18:59.0971579Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun/xml/fastinfoset:
2025-11-24T13:18:59.0971715Z total 0
2025-11-24T13:18:59.0971846Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0972007Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0972179Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 FastInfoset
2025-11-24T13:18:59.0972253Z 
2025-11-24T13:18:59.0972392Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun/xml/fastinfoset/FastInfoset:
2025-11-24T13:18:59.0972540Z total 0
2025-11-24T13:18:59.0972673Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0973043Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0973210Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.2.16
2025-11-24T13:18:59.0973287Z 
2025-11-24T13:18:59.0973435Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/com/sun/xml/fastinfoset/FastInfoset/1.2.16:
2025-11-24T13:18:59.0973580Z total 312
2025-11-24T13:18:59.0973721Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0973885Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0974052Z -rw-r--r-- 1 VssAdministrator 197121 317195 Jan  1  2010 FastInfoset-1.2.16.jar
2025-11-24T13:18:59.0974134Z 
2025-11-24T13:18:59.0974263Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/commons-codec:
2025-11-24T13:18:59.0974392Z total 4
2025-11-24T13:18:59.0974528Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0974691Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0974869Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-codec
2025-11-24T13:18:59.0974944Z 
2025-11-24T13:18:59.0975080Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/commons-codec/commons-codec:
2025-11-24T13:18:59.0975224Z total 0
2025-11-24T13:18:59.0975353Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0975983Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0976313Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.15
2025-11-24T13:18:59.0976464Z 
2025-11-24T13:18:59.0976740Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/commons-codec/commons-codec/1.15:
2025-11-24T13:18:59.0977015Z total 348
2025-11-24T13:18:59.0977292Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0977631Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0977961Z -rw-r--r-- 1 VssAdministrator 197121 353793 Jan  1  2010 commons-codec-1.15.jar
2025-11-24T13:18:59.0978254Z 
2025-11-24T13:18:59.0978522Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/commons-io:
2025-11-24T13:18:59.0978775Z total 4
2025-11-24T13:18:59.0979043Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0979378Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0979702Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-io
2025-11-24T13:18:59.0979852Z 
2025-11-24T13:18:59.0980127Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/commons-io/commons-io:
2025-11-24T13:18:59.0980397Z total 0
2025-11-24T13:18:59.0980666Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0980987Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0981317Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.4
2025-11-24T13:18:59.0981458Z 
2025-11-24T13:18:59.0981723Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/commons-io/commons-io/2.4:
2025-11-24T13:18:59.0982018Z total 184
2025-11-24T13:18:59.0982285Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0982612Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0982938Z -rw-r--r-- 1 VssAdministrator 197121 185140 Jan  1  2010 commons-io-2.4.jar
2025-11-24T13:18:59.0983091Z 
2025-11-24T13:18:59.0983349Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/commons-logging:
2025-11-24T13:18:59.0983608Z total 4
2025-11-24T13:18:59.0983865Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0984192Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0984532Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-logging
2025-11-24T13:18:59.0984686Z 
2025-11-24T13:18:59.0984968Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/commons-logging/commons-logging:
2025-11-24T13:18:59.0985249Z total 0
2025-11-24T13:18:59.0985512Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0986368Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0986717Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.2
2025-11-24T13:18:59.0986856Z 
2025-11-24T13:18:59.0987137Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/commons-logging/commons-logging/1.2:
2025-11-24T13:18:59.0987415Z total 64
2025-11-24T13:18:59.0987673Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0987993Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0988336Z -rw-r--r-- 1 VssAdministrator 197121 61829 Jan  1  2010 commons-logging-1.2.jar
2025-11-24T13:18:59.0988497Z 
2025-11-24T13:18:59.0988745Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/jakarta:
2025-11-24T13:18:59.0988998Z total 4
2025-11-24T13:18:59.0989266Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0989582Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0989928Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 activation
2025-11-24T13:18:59.0990269Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xml
2025-11-24T13:18:59.0990420Z 
2025-11-24T13:18:59.0990691Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/jakarta/activation:
2025-11-24T13:18:59.0990953Z total 0
2025-11-24T13:18:59.0991205Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0991539Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0991888Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jakarta.activation-api
2025-11-24T13:18:59.0992062Z 
2025-11-24T13:18:59.0992265Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/jakarta/activation/jakarta.activation-api:
2025-11-24T13:18:59.0992414Z total 0
2025-11-24T13:18:59.0992550Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0992711Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0992998Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.2.1
2025-11-24T13:18:59.0993075Z 
2025-11-24T13:18:59.0993221Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/jakarta/activation/jakarta.activation-api/1.2.1:
2025-11-24T13:18:59.0993376Z total 44
2025-11-24T13:18:59.0993513Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.0993676Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.0993852Z -rw-r--r-- 1 VssAdministrator 197121 44399 Jan  1  2010 jakarta.activation-api-1.2.1.jar
2025-11-24T13:18:59.0993941Z 
2025-11-24T13:18:59.0994071Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/jakarta/xml:
2025-11-24T13:18:59.0994198Z total 0
2025-11-24T13:18:59.0994339Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0994499Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0994661Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 bind
2025-11-24T13:18:59.0994739Z 
2025-11-24T13:18:59.0994871Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/jakarta/xml/bind:
2025-11-24T13:18:59.0995005Z total 0
2025-11-24T13:18:59.0995136Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0995302Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0995473Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jakarta.xml.bind-api
2025-11-24T13:18:59.0995552Z 
2025-11-24T13:18:59.0995698Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/jakarta/xml/bind/jakarta.xml.bind-api:
2025-11-24T13:18:59.0995841Z total 0
2025-11-24T13:18:59.0995972Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0996131Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0996298Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.3.2
2025-11-24T13:18:59.0996371Z 
2025-11-24T13:18:59.0996537Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/jakarta/xml/bind/jakarta.xml.bind-api/2.3.2:
2025-11-24T13:18:59.0996707Z total 116
2025-11-24T13:18:59.0997183Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.0997356Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.0997536Z -rw-r--r-- 1 VssAdministrator 197121 115498 Jan  1  2010 jakarta.xml.bind-api-2.3.2.jar
2025-11-24T13:18:59.0997626Z 
2025-11-24T13:18:59.0997753Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/javax:
2025-11-24T13:18:59.0997882Z total 4
2025-11-24T13:18:59.0998016Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0998186Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0998352Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 inject
2025-11-24T13:18:59.0998424Z 
2025-11-24T13:18:59.0998558Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/javax/inject:
2025-11-24T13:18:59.0998686Z total 0
2025-11-24T13:18:59.0998819Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0998983Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0999159Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 javax.inject
2025-11-24T13:18:59.0999236Z 
2025-11-24T13:18:59.0999375Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/javax/inject/javax.inject:
2025-11-24T13:18:59.0999523Z total 0
2025-11-24T13:18:59.0999654Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.0999826Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.0999993Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1
2025-11-24T13:18:59.1000069Z 
2025-11-24T13:18:59.1000212Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/javax/inject/javax.inject/1:
2025-11-24T13:18:59.1000353Z total 4
2025-11-24T13:18:59.1000499Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 .
2025-11-24T13:18:59.1000669Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 ..
2025-11-24T13:18:59.1000845Z -rw-r--r-- 1 VssAdministrator 197121 2497 Jan  1  2010 javax.inject-1.jar
2025-11-24T13:18:59.1000976Z 
2025-11-24T13:18:59.1001109Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/lint-psi:
2025-11-24T13:18:59.1001239Z total 4
2025-11-24T13:18:59.1001374Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1001537Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1001713Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 intellij-core
2025-11-24T13:18:59.1001888Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-compiler
2025-11-24T13:18:59.1002059Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 uast
2025-11-24T13:18:59.1002136Z 
2025-11-24T13:18:59.1002271Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/lint-psi/intellij-core:
2025-11-24T13:18:59.1002415Z total 30248
2025-11-24T13:18:59.1002553Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 .
2025-11-24T13:18:59.1002723Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 ..
2025-11-24T13:18:59.1002897Z -rw-r--r-- 1 VssAdministrator 197121 30973352 Jan  1  2010 intellij-core-mvn.jar
2025-11-24T13:18:59.1002976Z 
2025-11-24T13:18:59.1003116Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/lint-psi/kotlin-compiler:
2025-11-24T13:18:59.1003256Z total 49536
2025-11-24T13:18:59.1003392Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 .
2025-11-24T13:18:59.1003556Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 ..
2025-11-24T13:18:59.1003733Z -rw-r--r-- 1 VssAdministrator 197121 50724487 Jan  1  2010 kotlin-compiler-mvn.jar
2025-11-24T13:18:59.1003811Z 
2025-11-24T13:18:59.1003941Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/lint-psi/uast:
2025-11-24T13:18:59.1004082Z total 2320
2025-11-24T13:18:59.1004220Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1004384Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1004547Z -rw-r--r-- 1 VssAdministrator 197121 2371752 Jan  1  2010 uast.jar
2025-11-24T13:18:59.1004625Z 
2025-11-24T13:18:59.1004990Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net:
2025-11-24T13:18:59.1005115Z total 4
2025-11-24T13:18:59.1005255Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1005418Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1005584Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 java
2025-11-24T13:18:59.1005746Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 sf
2025-11-24T13:18:59.1005820Z 
2025-11-24T13:18:59.1005946Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/java:
2025-11-24T13:18:59.1006071Z total 0
2025-11-24T13:18:59.1006207Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1006367Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1006529Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 dev
2025-11-24T13:18:59.1006601Z 
2025-11-24T13:18:59.1006735Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/java/dev:
2025-11-24T13:18:59.1006868Z total 0
2025-11-24T13:18:59.1006997Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1007157Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1007323Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jna
2025-11-24T13:18:59.1007393Z 
2025-11-24T13:18:59.1007525Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/java/dev/jna:
2025-11-24T13:18:59.1007672Z total 0
2025-11-24T13:18:59.1007805Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1007964Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1008124Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jna
2025-11-24T13:18:59.1008294Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jna-platform
2025-11-24T13:18:59.1008369Z 
2025-11-24T13:18:59.1008501Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/java/dev/jna/jna:
2025-11-24T13:18:59.1008636Z total 0
2025-11-24T13:18:59.1008813Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1008974Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1009137Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 5.6.0
2025-11-24T13:18:59.1009214Z 
2025-11-24T13:18:59.1009349Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/java/dev/jna/jna/5.6.0:
2025-11-24T13:18:59.1009488Z total 1476
2025-11-24T13:18:59.1009626Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1009789Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1009953Z -rw-r--r-- 1 VssAdministrator 197121 1509440 Jan  1  2010 jna-5.6.0.jar
2025-11-24T13:18:59.1010028Z 
2025-11-24T13:18:59.1010164Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/java/dev/jna/jna-platform:
2025-11-24T13:18:59.1010302Z total 0
2025-11-24T13:18:59.1010432Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1010595Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1010765Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 5.6.0
2025-11-24T13:18:59.1010837Z 
2025-11-24T13:18:59.1010975Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/java/dev/jna/jna-platform/5.6.0:
2025-11-24T13:18:59.1011125Z total 2672
2025-11-24T13:18:59.1011260Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1011423Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1011592Z -rw-r--r-- 1 VssAdministrator 197121 2735878 Jan  1  2010 jna-platform-5.6.0.jar
2025-11-24T13:18:59.1011674Z 
2025-11-24T13:18:59.1011801Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/sf:
2025-11-24T13:18:59.1011925Z total 0
2025-11-24T13:18:59.1012060Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1012219Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1012385Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jopt-simple
2025-11-24T13:18:59.1012779Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kxml
2025-11-24T13:18:59.1012857Z 
2025-11-24T13:18:59.1012990Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/sf/jopt-simple:
2025-11-24T13:18:59.1013122Z total 0
2025-11-24T13:18:59.1013257Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1013418Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1013582Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jopt-simple
2025-11-24T13:18:59.1013663Z 
2025-11-24T13:18:59.1013799Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/sf/jopt-simple/jopt-simple:
2025-11-24T13:18:59.1013937Z total 0
2025-11-24T13:18:59.1014067Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1014231Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1014392Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 4.9
2025-11-24T13:18:59.1014465Z 
2025-11-24T13:18:59.1014605Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/sf/jopt-simple/jopt-simple/4.9:
2025-11-24T13:18:59.1014760Z total 68
2025-11-24T13:18:59.1014896Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1015058Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1015229Z -rw-r--r-- 1 VssAdministrator 197121 66469 Jan  1  2010 jopt-simple-4.9.jar
2025-11-24T13:18:59.1015302Z 
2025-11-24T13:18:59.1015430Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/sf/kxml:
2025-11-24T13:18:59.1015558Z total 0
2025-11-24T13:18:59.1015696Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1015856Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1016019Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kxml2
2025-11-24T13:18:59.1016097Z 
2025-11-24T13:18:59.1016228Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/sf/kxml/kxml2:
2025-11-24T13:18:59.1016407Z total 0
2025-11-24T13:18:59.1016542Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1016706Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1016867Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.3.0
2025-11-24T13:18:59.1016937Z 
2025-11-24T13:18:59.1017074Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/net/sf/kxml/kxml2/2.3.0:
2025-11-24T13:18:59.1017207Z total 44
2025-11-24T13:18:59.1017342Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1017507Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1017677Z -rw-r--r-- 1 VssAdministrator 197121 43858 Jan  1  2010 kxml2-2.3.0.jar
2025-11-24T13:18:59.1017748Z 
2025-11-24T13:18:59.1017872Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org:
2025-11-24T13:18:59.1018004Z total 8
2025-11-24T13:18:59.1018135Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1018297Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1018464Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 apache
2025-11-24T13:18:59.1018644Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 bouncycastle
2025-11-24T13:18:59.1018821Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 checkerframework
2025-11-24T13:18:59.1018994Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 glassfish
2025-11-24T13:18:59.1019164Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jetbrains
2025-11-24T13:18:59.1019336Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jvnet
2025-11-24T13:18:59.1019500Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ow2
2025-11-24T13:18:59.1019570Z 
2025-11-24T13:18:59.1019705Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache:
2025-11-24T13:18:59.1019834Z total 4
2025-11-24T13:18:59.1019966Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1020129Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1020302Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons
2025-11-24T13:18:59.1020776Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 httpcomponents
2025-11-24T13:18:59.1020857Z 
2025-11-24T13:18:59.1020997Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache/commons:
2025-11-24T13:18:59.1021141Z total 0
2025-11-24T13:18:59.1021274Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1021438Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1021610Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-compress
2025-11-24T13:18:59.1021696Z 
2025-11-24T13:18:59.1021838Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache/commons/commons-compress:
2025-11-24T13:18:59.1021982Z total 0
2025-11-24T13:18:59.1022117Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1022278Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1022442Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.21
2025-11-24T13:18:59.1022523Z 
2025-11-24T13:18:59.1022668Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache/commons/commons-compress/1.21:
2025-11-24T13:18:59.1022813Z total 996
2025-11-24T13:18:59.1022951Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1023122Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1023294Z -rw-r--r-- 1 VssAdministrator 197121 1018316 Jan  1  2010 commons-compress-1.21.jar
2025-11-24T13:18:59.1023375Z 
2025-11-24T13:18:59.1023516Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache/httpcomponents:
2025-11-24T13:18:59.1023653Z total 0
2025-11-24T13:18:59.1023783Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1023944Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1024128Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 httpclient
2025-11-24T13:18:59.1024298Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 httpcore
2025-11-24T13:18:59.1024565Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 httpmime
2025-11-24T13:18:59.1024642Z 
2025-11-24T13:18:59.1024786Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache/httpcomponents/httpclient:
2025-11-24T13:18:59.1024930Z total 0
2025-11-24T13:18:59.1025059Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1025223Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1025385Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 4.5.14
2025-11-24T13:18:59.1025457Z 
2025-11-24T13:18:59.1025605Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache/httpcomponents/httpclient/4.5.14:
2025-11-24T13:18:59.1025751Z total 768
2025-11-24T13:18:59.1025884Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1026047Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1026220Z -rw-r--r-- 1 VssAdministrator 197121 785639 Jan  1  2010 httpclient-4.5.14.jar
2025-11-24T13:18:59.1026300Z 
2025-11-24T13:18:59.1026438Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache/httpcomponents/httpcore:
2025-11-24T13:18:59.1026583Z total 0
2025-11-24T13:18:59.1026715Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1026878Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1027043Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 4.4.16
2025-11-24T13:18:59.1027120Z 
2025-11-24T13:18:59.1027265Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache/httpcomponents/httpcore/4.4.16:
2025-11-24T13:18:59.1027410Z total 324
2025-11-24T13:18:59.1027541Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1027711Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1027881Z -rw-r--r-- 1 VssAdministrator 197121 327891 Jan  1  2010 httpcore-4.4.16.jar
2025-11-24T13:18:59.1027956Z 
2025-11-24T13:18:59.1028103Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache/httpcomponents/httpmime:
2025-11-24T13:18:59.1028286Z total 0
2025-11-24T13:18:59.1028416Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1028578Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1028749Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 4.5.6
2025-11-24T13:18:59.1028821Z 
2025-11-24T13:18:59.1028965Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/apache/httpcomponents/httpmime/4.5.6:
2025-11-24T13:18:59.1029115Z total 44
2025-11-24T13:18:59.1029248Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1029411Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1029574Z -rw-r--r-- 1 VssAdministrator 197121 41794 Jan  1  2010 httpmime-4.5.6.jar
2025-11-24T13:18:59.1029653Z 
2025-11-24T13:18:59.1029784Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/bouncycastle:
2025-11-24T13:18:59.1029918Z total 4
2025-11-24T13:18:59.1030055Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1030216Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1030384Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 bcpkix-jdk15on
2025-11-24T13:18:59.1030560Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 bcprov-jdk15on
2025-11-24T13:18:59.1030650Z 
2025-11-24T13:18:59.1030791Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/bouncycastle/bcpkix-jdk15on:
2025-11-24T13:18:59.1030929Z total 0
2025-11-24T13:18:59.1031066Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1031228Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1031391Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.67
2025-11-24T13:18:59.1031468Z 
2025-11-24T13:18:59.1031610Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/bouncycastle/bcpkix-jdk15on/1.67:
2025-11-24T13:18:59.1031795Z total 868
2025-11-24T13:18:59.1031930Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1032104Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1032275Z -rw-r--r-- 1 VssAdministrator 197121 887810 Jan  1  2010 bcpkix-jdk15on-1.67.jar
2025-11-24T13:18:59.1032352Z 
2025-11-24T13:18:59.1032494Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/bouncycastle/bcprov-jdk15on:
2025-11-24T13:18:59.1032638Z total 0
2025-11-24T13:18:59.1032770Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1032930Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1033093Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.67
2025-11-24T13:18:59.1033171Z 
2025-11-24T13:18:59.1033312Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/bouncycastle/bcprov-jdk15on/1.67:
2025-11-24T13:18:59.1033455Z total 5824
2025-11-24T13:18:59.1033597Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1033764Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1033937Z -rw-r--r-- 1 VssAdministrator 197121 5961136 Jan  1  2010 bcprov-jdk15on-1.67.jar
2025-11-24T13:18:59.1034020Z 
2025-11-24T13:18:59.1034153Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/checkerframework:
2025-11-24T13:18:59.1034287Z total 4
2025-11-24T13:18:59.1034417Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1034582Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1034754Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 checker-qual
2025-11-24T13:18:59.1034830Z 
2025-11-24T13:18:59.1034977Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/checkerframework/checker-qual:
2025-11-24T13:18:59.1035120Z total 0
2025-11-24T13:18:59.1035251Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1035411Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1035586Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.21.2
2025-11-24T13:18:59.1035697Z 
2025-11-24T13:18:59.1035840Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/checkerframework/checker-qual/3.21.2:
2025-11-24T13:18:59.1035992Z total 220
2025-11-24T13:18:59.1036125Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1036287Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1036454Z -rw-r--r-- 1 VssAdministrator 197121 222142 Jan  1  2010 checker-qual-3.21.2.jar
2025-11-24T13:18:59.1036536Z 
2025-11-24T13:18:59.1037124Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/glassfish:
2025-11-24T13:18:59.1037393Z total 4
2025-11-24T13:18:59.1037672Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1037992Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1038326Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jaxb
2025-11-24T13:18:59.1038477Z 
2025-11-24T13:18:59.1038780Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/glassfish/jaxb:
2025-11-24T13:18:59.1038996Z total 0
2025-11-24T13:18:59.1039130Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1039296Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1039486Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jaxb-runtime
2025-11-24T13:18:59.1039652Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 txw2
2025-11-24T13:18:59.1039723Z 
2025-11-24T13:18:59.1039867Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/glassfish/jaxb/jaxb-runtime:
2025-11-24T13:18:59.1040006Z total 0
2025-11-24T13:18:59.1040137Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1040300Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1040470Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.3.2
2025-11-24T13:18:59.1040543Z 
2025-11-24T13:18:59.1040684Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/glassfish/jaxb/jaxb-runtime/2.3.2:
2025-11-24T13:18:59.1040936Z total 992
2025-11-24T13:18:59.1041072Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1041237Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1041408Z -rw-r--r-- 1 VssAdministrator 197121 1013367 Jan  1  2010 jaxb-runtime-2.3.2.jar
2025-11-24T13:18:59.1041489Z 
2025-11-24T13:18:59.1041622Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/glassfish/jaxb/txw2:
2025-11-24T13:18:59.1041755Z total 0
2025-11-24T13:18:59.1041890Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1042053Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1042217Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.3.2
2025-11-24T13:18:59.1042293Z 
2025-11-24T13:18:59.1042428Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/glassfish/jaxb/txw2/2.3.2:
2025-11-24T13:18:59.1042564Z total 72
2025-11-24T13:18:59.1042701Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1042870Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1043032Z -rw-r--r-- 1 VssAdministrator 197121 72080 Jan  1  2010 txw2-2.3.2.jar
2025-11-24T13:18:59.1043103Z 
2025-11-24T13:18:59.1043236Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains:
2025-11-24T13:18:59.1043363Z total 8
2025-11-24T13:18:59.1043492Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1043652Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1043827Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 annotations
2025-11-24T13:18:59.1043998Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 intellij
2025-11-24T13:18:59.1044164Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin
2025-11-24T13:18:59.1044329Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlinx
2025-11-24T13:18:59.1044405Z 
2025-11-24T13:18:59.1044544Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/annotations:
2025-11-24T13:18:59.1044726Z total 0
2025-11-24T13:18:59.1044856Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1045023Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1045185Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 13.0
2025-11-24T13:18:59.1045256Z 
2025-11-24T13:18:59.1045397Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/annotations/13.0:
2025-11-24T13:18:59.1045537Z total 20
2025-11-24T13:18:59.1045669Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1045834Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1046005Z -rw-r--r-- 1 VssAdministrator 197121 17536 Jan  1  2010 annotations-13.0.jar
2025-11-24T13:18:59.1046078Z 
2025-11-24T13:18:59.1046217Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/intellij:
2025-11-24T13:18:59.1046363Z total 0
2025-11-24T13:18:59.1046494Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1046656Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1046817Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 deps
2025-11-24T13:18:59.1046894Z 
2025-11-24T13:18:59.1047032Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/intellij/deps:
2025-11-24T13:18:59.1047170Z total 0
2025-11-24T13:18:59.1047307Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1047468Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1047633Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 trove4j
2025-11-24T13:18:59.1047712Z 
2025-11-24T13:18:59.1047853Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/intellij/deps/trove4j:
2025-11-24T13:18:59.1047995Z total 0
2025-11-24T13:18:59.1048126Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1048293Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1048501Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.0.20200330
2025-11-24T13:18:59.1048578Z 
2025-11-24T13:18:59.1048725Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/intellij/deps/trove4j/1.0.20200330:
2025-11-24T13:18:59.1048883Z total 560
2025-11-24T13:18:59.1049017Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1049179Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1049350Z -rw-r--r-- 1 VssAdministrator 197121 572985 Jan  1  2010 trove4j-1.0.20200330.jar
2025-11-24T13:18:59.1049434Z 
2025-11-24T13:18:59.1049566Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin:
2025-11-24T13:18:59.1049697Z total 4
2025-11-24T13:18:59.1049832Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1049992Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1050161Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-reflect
2025-11-24T13:18:59.1050340Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-stdlib
2025-11-24T13:18:59.1050531Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-stdlib-common
2025-11-24T13:18:59.1050710Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-stdlib-jdk7
2025-11-24T13:18:59.1050887Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-stdlib-jdk8
2025-11-24T13:18:59.1069663Z 
2025-11-24T13:18:59.1069953Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin/kotlin-reflect:
2025-11-24T13:18:59.1070189Z total 4
2025-11-24T13:18:59.1070413Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1070692Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1070967Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.9.0
2025-11-24T13:18:59.1071089Z 
2025-11-24T13:18:59.1071349Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin/kotlin-reflect/1.9.0:
2025-11-24T13:18:59.1071765Z total 3148
2025-11-24T13:18:59.1071995Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1072288Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1072996Z -rw-r--r-- 1 VssAdministrator 197121 3223171 Jan  1  2010 kotlin-reflect-1.9.0.jar
2025-11-24T13:18:59.1073150Z 
2025-11-24T13:18:59.1073408Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib:
2025-11-24T13:18:59.1073652Z total 4
2025-11-24T13:18:59.1073875Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1074042Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1074206Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.9.0
2025-11-24T13:18:59.1074281Z 
2025-11-24T13:18:59.1074424Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib/1.9.0:
2025-11-24T13:18:59.1074568Z total 1668
2025-11-24T13:18:59.1074715Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1074881Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1075050Z -rw-r--r-- 1 VssAdministrator 197121 1708006 Jan  1  2010 kotlin-stdlib-1.9.0.jar
2025-11-24T13:18:59.1075131Z 
2025-11-24T13:18:59.1075272Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-common:
2025-11-24T13:18:59.1075414Z total 4
2025-11-24T13:18:59.1075541Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1075700Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1075858Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.9.0
2025-11-24T13:18:59.1075930Z 
2025-11-24T13:18:59.1076073Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-common/1.9.0:
2025-11-24T13:18:59.1076223Z total 220
2025-11-24T13:18:59.1076358Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1076639Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1076826Z -rw-r--r-- 1 VssAdministrator 197121 225141 Jan  1  2010 kotlin-stdlib-common-1.9.0.jar
2025-11-24T13:18:59.1076908Z 
2025-11-24T13:18:59.1077053Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk7:
2025-11-24T13:18:59.1077200Z total 4
2025-11-24T13:18:59.1077331Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1077495Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1077660Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.9.0
2025-11-24T13:18:59.1077738Z 
2025-11-24T13:18:59.1077885Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk7/1.9.0:
2025-11-24T13:18:59.1078030Z total 4
2025-11-24T13:18:59.1078163Z drwxr-xr-x 1 VssAdministrator 197121   0 Nov  2 22:04 .
2025-11-24T13:18:59.1078338Z drwxr-xr-x 1 VssAdministrator 197121   0 Nov  2 22:04 ..
2025-11-24T13:18:59.1078514Z -rw-r--r-- 1 VssAdministrator 197121 958 Jan  1  2010 kotlin-stdlib-jdk7-1.9.0.jar
2025-11-24T13:18:59.1078591Z 
2025-11-24T13:18:59.1078740Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk8:
2025-11-24T13:18:59.1078884Z total 4
2025-11-24T13:18:59.1079015Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1079177Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1079348Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.9.0
2025-11-24T13:18:59.1079419Z 
2025-11-24T13:18:59.1079560Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk8/1.9.0:
2025-11-24T13:18:59.1079709Z total 4
2025-11-24T13:18:59.1079840Z drwxr-xr-x 1 VssAdministrator 197121   0 Nov  2 22:04 .
2025-11-24T13:18:59.1080002Z drwxr-xr-x 1 VssAdministrator 197121   0 Nov  2 22:04 ..
2025-11-24T13:18:59.1080174Z -rw-r--r-- 1 VssAdministrator 197121 963 Jan  1  2010 kotlin-stdlib-jdk8-1.9.0.jar
2025-11-24T13:18:59.1080312Z 
2025-11-24T13:18:59.1080447Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlinx:
2025-11-24T13:18:59.1080582Z total 0
2025-11-24T13:18:59.1080726Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1080888Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1081061Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlinx-cli-jvm
2025-11-24T13:18:59.1081143Z 
2025-11-24T13:18:59.1081284Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlinx/kotlinx-cli-jvm:
2025-11-24T13:18:59.1081425Z total 0
2025-11-24T13:18:59.1081557Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1081740Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1081901Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 0.3.1
2025-11-24T13:18:59.1081972Z 
2025-11-24T13:18:59.1082117Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jetbrains/kotlinx/kotlinx-cli-jvm/0.3.1:
2025-11-24T13:18:59.1082274Z total 84
2025-11-24T13:18:59.1082411Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1082571Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1082742Z -rw-r--r-- 1 VssAdministrator 197121 82399 Jan  1  2010 kotlinx-cli-jvm-0.3.1.jar
2025-11-24T13:18:59.1082828Z 
2025-11-24T13:18:59.1083337Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jvnet:
2025-11-24T13:18:59.1083597Z total 4
2025-11-24T13:18:59.1083866Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1084186Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1084518Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 staxex
2025-11-24T13:18:59.1084671Z 
2025-11-24T13:18:59.1084937Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jvnet/staxex:
2025-11-24T13:18:59.1085150Z total 0
2025-11-24T13:18:59.1085390Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1085564Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1085726Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 stax-ex
2025-11-24T13:18:59.1085799Z 
2025-11-24T13:18:59.1085937Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jvnet/staxex/stax-ex:
2025-11-24T13:18:59.1086071Z total 0
2025-11-24T13:18:59.1086202Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1086361Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1086528Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.8.1
2025-11-24T13:18:59.1086599Z 
2025-11-24T13:18:59.1086737Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/jvnet/staxex/stax-ex/1.8.1:
2025-11-24T13:18:59.1086876Z total 40
2025-11-24T13:18:59.1087014Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1087178Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1087350Z -rw-r--r-- 1 VssAdministrator 197121 38099 Jan  1  2010 stax-ex-1.8.1.jar
2025-11-24T13:18:59.1087430Z 
2025-11-24T13:18:59.1087556Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/ow2:
2025-11-24T13:18:59.1087684Z total 4
2025-11-24T13:18:59.1087813Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1087977Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1088138Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 asm
2025-11-24T13:18:59.1088209Z 
2025-11-24T13:18:59.1088340Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/ow2/asm:
2025-11-24T13:18:59.1088469Z total 0
2025-11-24T13:18:59.1088599Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1088759Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1088926Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 asm
2025-11-24T13:18:59.1089094Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 asm-analysis
2025-11-24T13:18:59.1089355Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 asm-tree
2025-11-24T13:18:59.1089439Z 
2025-11-24T13:18:59.1089569Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/ow2/asm/asm:
2025-11-24T13:18:59.1089701Z total 0
2025-11-24T13:18:59.1089829Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1089992Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1090153Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 9.2
2025-11-24T13:18:59.1090223Z 
2025-11-24T13:18:59.1090354Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/ow2/asm/asm/9.2:
2025-11-24T13:18:59.1090496Z total 120
2025-11-24T13:18:59.1090632Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1090796Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1090957Z -rw-r--r-- 1 VssAdministrator 197121 122004 Jan  1  2010 asm-9.2.jar
2025-11-24T13:18:59.1091032Z 
2025-11-24T13:18:59.1091166Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/ow2/asm/asm-analysis:
2025-11-24T13:18:59.1091301Z total 0
2025-11-24T13:18:59.1091436Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1091597Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1091758Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 9.2
2025-11-24T13:18:59.1091834Z 
2025-11-24T13:18:59.1091971Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/ow2/asm/asm-analysis/9.2:
2025-11-24T13:18:59.1092108Z total 36
2025-11-24T13:18:59.1092242Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1092408Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1092575Z -rw-r--r-- 1 VssAdministrator 197121 34257 Jan  1  2010 asm-analysis-9.2.jar
2025-11-24T13:18:59.1092648Z 
2025-11-24T13:18:59.1092795Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/ow2/asm/asm-tree:
2025-11-24T13:18:59.1093106Z total 0
2025-11-24T13:18:59.1093238Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1093397Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1093562Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 9.2
2025-11-24T13:18:59.1093633Z 
2025-11-24T13:18:59.1093766Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/org/ow2/asm/asm-tree/9.2:
2025-11-24T13:18:59.1093910Z total 52
2025-11-24T13:18:59.1094937Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1095238Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1095520Z -rw-r--r-- 1 VssAdministrator 197121 52660 Jan  1  2010 asm-tree-9.2.jar
2025-11-24T13:18:59.1095653Z 
2025-11-24T13:18:59.1095880Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/xerces:
2025-11-24T13:18:59.1096111Z total 4
2025-11-24T13:18:59.1096360Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1096671Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1096959Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xercesImpl
2025-11-24T13:18:59.1097082Z 
2025-11-24T13:18:59.1097312Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/xerces/xercesImpl:
2025-11-24T13:18:59.1097449Z total 0
2025-11-24T13:18:59.1097582Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1097744Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1097911Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.12.0
2025-11-24T13:18:59.1097983Z 
2025-11-24T13:18:59.1098118Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/xerces/xercesImpl/2.12.0:
2025-11-24T13:18:59.1098265Z total 1356
2025-11-24T13:18:59.1098404Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1098567Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1098736Z -rw-r--r-- 1 VssAdministrator 197121 1386397 Jan  1  2010 xercesImpl-2.12.0.jar
2025-11-24T13:18:59.1098916Z 
2025-11-24T13:18:59.1099044Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/xml-apis:
2025-11-24T13:18:59.1099171Z total 4
2025-11-24T13:18:59.1099306Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1099470Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1099634Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xml-apis
2025-11-24T13:18:59.1099712Z 
2025-11-24T13:18:59.1099841Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/xml-apis/xml-apis:
2025-11-24T13:18:59.1099972Z total 0
2025-11-24T13:18:59.1100101Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1100263Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1100431Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.4.01
2025-11-24T13:18:59.1100502Z 
2025-11-24T13:18:59.1100635Z C:\Android\android-sdk/cmdline-tools/12.0/lib/external/xml-apis/xml-apis/1.4.01:
2025-11-24T13:18:59.1100781Z total 216
2025-11-24T13:18:59.1100918Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1101079Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1101246Z -rw-r--r-- 1 VssAdministrator 197121 220536 Jan  1  2010 xml-apis-1.4.01.jar
2025-11-24T13:18:59.1101324Z 
2025-11-24T13:18:59.1101448Z C:\Android\android-sdk/cmdline-tools/12.0/lib/layoutlib-api:
2025-11-24T13:18:59.1101572Z total 128
2025-11-24T13:18:59.1101710Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1101871Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1102037Z -rw-r--r-- 1 VssAdministrator 197121 122368 Jan  1  2010 tools.layoutlib-api.jar
2025-11-24T13:18:59.1102116Z 
2025-11-24T13:18:59.1102235Z C:\Android\android-sdk/cmdline-tools/12.0/lib/lint:
2025-11-24T13:18:59.1102360Z total 7236
2025-11-24T13:18:59.1102495Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1102714Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1102880Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 cli
2025-11-24T13:18:59.1103048Z -rw-r--r-- 1 VssAdministrator 197121  131392 Jan  1  2010 lint-checks-proto.jar
2025-11-24T13:18:59.1103218Z -rw-r--r-- 1 VssAdministrator 197121 1309713 Jan  1  2010 tools.lint-api.jar
2025-11-24T13:18:59.1103392Z -rw-r--r-- 1 VssAdministrator 197121 5773882 Jan  1  2010 tools.lint-checks.jar
2025-11-24T13:18:59.1103564Z -rw-r--r-- 1 VssAdministrator 197121  174893 Jan  1  2010 tools.lint-model.jar
2025-11-24T13:18:59.1103637Z 
2025-11-24T13:18:59.1103767Z C:\Android\android-sdk/cmdline-tools/12.0/lib/lint/cli:
2025-11-24T13:18:59.1103891Z total 652
2025-11-24T13:18:59.1104023Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1104183Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1104349Z -rw-r--r-- 1 VssAdministrator 197121 660355 Jan  1  2010 cli.jar
2025-11-24T13:18:59.1104421Z 
2025-11-24T13:18:59.1104539Z C:\Android\android-sdk/cmdline-tools/12.0/lib/misc:
2025-11-24T13:18:59.1104665Z total 8
2025-11-24T13:18:59.1104796Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1104957Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1105123Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 screenshot2
2025-11-24T13:18:59.1105202Z 
2025-11-24T13:18:59.1105328Z C:\Android\android-sdk/cmdline-tools/12.0/lib/misc/screenshot2:
2025-11-24T13:18:59.1105457Z total 12
2025-11-24T13:18:59.1105592Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1105761Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1105928Z -rw-r--r-- 1 VssAdministrator 197121 11474 Jan  1  2010 libscreenshot2lib.jar
2025-11-24T13:18:59.1106003Z 
2025-11-24T13:18:59.1106131Z C:\Android\android-sdk/cmdline-tools/12.0/lib/profgen:
2025-11-24T13:18:59.1106256Z total 8
2025-11-24T13:18:59.1106428Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1106592Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1106768Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 profgen
2025-11-24T13:18:59.1106936Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 profgen-cli
2025-11-24T13:18:59.1107010Z 
2025-11-24T13:18:59.1107148Z C:\Android\android-sdk/cmdline-tools/12.0/lib/profgen/profgen:
2025-11-24T13:18:59.1107275Z total 216
2025-11-24T13:18:59.1107409Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1107569Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1107748Z -rw-r--r-- 1 VssAdministrator 197121 220347 Jan  1  2010 libprofgen.jar
2025-11-24T13:18:59.1107820Z 
2025-11-24T13:18:59.1107947Z C:\Android\android-sdk/cmdline-tools/12.0/lib/profgen/profgen-cli:
2025-11-24T13:18:59.1108082Z total 32
2025-11-24T13:18:59.1108217Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1108383Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1108549Z -rw-r--r-- 1 VssAdministrator 197121 30738 Jan  1  2010 libprofgen-cli-lib.jar
2025-11-24T13:18:59.1108631Z 
2025-11-24T13:18:59.1108753Z C:\Android\android-sdk/cmdline-tools/12.0/lib/repository:
2025-11-24T13:18:59.1108878Z total 244
2025-11-24T13:18:59.1109016Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1109176Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1109342Z -rw-r--r-- 1 VssAdministrator 197121 241253 Jan  1  2010 tools.repository.jar
2025-11-24T13:18:59.1109420Z 
2025-11-24T13:18:59.1109543Z C:\Android\android-sdk/cmdline-tools/12.0/lib/sdk-common:
2025-11-24T13:18:59.1109669Z total 1604
2025-11-24T13:18:59.1109803Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1109965Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1110182Z -rw-r--r-- 1 VssAdministrator 197121 1633073 Jan  1  2010 tools.sdk-common.jar
2025-11-24T13:18:59.1110258Z 
2025-11-24T13:18:59.1110380Z C:\Android\android-sdk/cmdline-tools/12.0/lib/sdklib:
2025-11-24T13:18:59.1110509Z total 3020
2025-11-24T13:18:59.1110643Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1110802Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1110968Z -rw-r--r-- 1 VssAdministrator 197121   28508 Jan  1  2010 libavdmanager_lib.jar
2025-11-24T13:18:59.1111144Z -rw-r--r-- 1 VssAdministrator 197121   42047 Jan  1  2010 libsdkmanager_lib.jar
2025-11-24T13:18:59.1111310Z -rw-r--r-- 1 VssAdministrator 197121 1464627 Jan  1  2010 sdklib.core.jar
2025-11-24T13:18:59.1111476Z -rw-r--r-- 1 VssAdministrator 197121 1537601 Jan  1  2010 tools.sdklib.jar
2025-11-24T13:18:59.1111554Z 
2025-11-24T13:18:59.1111666Z C:\Android\android-sdk/cmdline-tools/7.0:
2025-11-24T13:18:59.1111784Z total 121
2025-11-24T13:18:59.1111919Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1112090Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.1112251Z -rw-r--r-- 1 VssAdministrator 197121 109836 Jan  1  2010 NOTICE.txt
2025-11-24T13:18:59.1112422Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 bin
2025-11-24T13:18:59.1112587Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 lib
2025-11-24T13:18:59.1112755Z -rw-r--r-- 1 VssAdministrator 197121     84 Jan  1  2010 source.properties
2025-11-24T13:18:59.1112826Z 
2025-11-24T13:18:59.1112942Z C:\Android\android-sdk/cmdline-tools/7.0/bin:
2025-11-24T13:18:59.1113076Z total 32
2025-11-24T13:18:59.1113209Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 .
2025-11-24T13:18:59.1113372Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 ..
2025-11-24T13:18:59.1113534Z -rw-r--r-- 1 VssAdministrator 197121 2297 Jan  1  2010 apkanalyzer.bat
2025-11-24T13:18:59.1113702Z -rw-r--r-- 1 VssAdministrator 197121 2288 Jan  1  2010 avdmanager.bat
2025-11-24T13:18:59.1113901Z -rw-r--r-- 1 VssAdministrator 197121 2242 Jan  1  2010 lint.bat
2025-11-24T13:18:59.1114056Z -rw-r--r-- 1 VssAdministrator 197121 2222 Jan  1  2010 profgen.bat
2025-11-24T13:18:59.1114212Z -rw-r--r-- 1 VssAdministrator 197121 2222 Jan  1  2010 retrace.bat
2025-11-24T13:18:59.1114375Z -rw-r--r-- 1 VssAdministrator 197121 2285 Jan  1  2010 screenshot2.bat
2025-11-24T13:18:59.1114534Z -rw-r--r-- 1 VssAdministrator 197121 2295 Jan  1  2010 sdkmanager.bat
2025-11-24T13:18:59.1114601Z 
2025-11-24T13:18:59.1114722Z C:\Android\android-sdk/cmdline-tools/7.0/lib:
2025-11-24T13:18:59.1114841Z total 7738
2025-11-24T13:18:59.1114975Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1115137Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1115298Z -rw-r--r-- 1 VssAdministrator 197121     202 Jan  1  2010 README
2025-11-24T13:18:59.1115464Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 analytics-library
2025-11-24T13:18:59.1115643Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 annotations
2025-11-24T13:18:59.1115819Z -rw-r--r-- 1 VssAdministrator 197121    4013 Jan  1  2010 apkanalyzer-classpath.jar
2025-11-24T13:18:59.1115996Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 apkparser
2025-11-24T13:18:59.1116169Z -rw-r--r-- 1 VssAdministrator 197121    2893 Jan  1  2010 avdmanager-classpath.jar
2025-11-24T13:18:59.1116340Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 build-system
2025-11-24T13:18:59.1116513Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 common
2025-11-24T13:18:59.1116678Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ddmlib
2025-11-24T13:18:59.1116851Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 device_validator
2025-11-24T13:18:59.1117026Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 external
2025-11-24T13:18:59.1117202Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 layoutlib-api
2025-11-24T13:18:59.1117413Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 lint
2025-11-24T13:18:59.1117579Z -rw-r--r-- 1 VssAdministrator 197121    4118 Jan  1  2010 lint-classpath.jar
2025-11-24T13:18:59.1117743Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 misc
2025-11-24T13:18:59.1117914Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 profgen
2025-11-24T13:18:59.1118082Z -rw-r--r-- 1 VssAdministrator 197121     719 Jan  1  2010 profgen-classpath.jar
2025-11-24T13:18:59.1118244Z -rw-r--r-- 1 VssAdministrator 197121 7870810 Jan  1  2010 r8.jar
2025-11-24T13:18:59.1118407Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 repository
2025-11-24T13:18:59.1118583Z -rw-r--r-- 1 VssAdministrator 197121     160 Jan  1  2010 retrace-classpath.jar
2025-11-24T13:18:59.1118753Z -rw-r--r-- 1 VssAdministrator 197121    1533 Jan  1  2010 screenshot2-classpath.jar
2025-11-24T13:18:59.1118926Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 sdk-common
2025-11-24T13:18:59.1119098Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 sdklib
2025-11-24T13:18:59.1119272Z -rw-r--r-- 1 VssAdministrator 197121    2893 Jan  1  2010 sdkmanager-classpath.jar
2025-11-24T13:18:59.1119346Z 
2025-11-24T13:18:59.1119472Z C:\Android\android-sdk/cmdline-tools/7.0/lib/analytics-library:
2025-11-24T13:18:59.1119604Z total 8
2025-11-24T13:18:59.1119734Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1119896Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1120059Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 protos
2025-11-24T13:18:59.1120229Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 shared
2025-11-24T13:18:59.1120394Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 tracker
2025-11-24T13:18:59.1120466Z 
2025-11-24T13:18:59.1120599Z C:\Android\android-sdk/cmdline-tools/7.0/lib/analytics-library/protos:
2025-11-24T13:18:59.1120730Z total 0
2025-11-24T13:18:59.1120864Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1121072Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1121239Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 src
2025-11-24T13:18:59.1121310Z 
2025-11-24T13:18:59.1121442Z C:\Android\android-sdk/cmdline-tools/7.0/lib/analytics-library/protos/src:
2025-11-24T13:18:59.1121578Z total 0
2025-11-24T13:18:59.1121711Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1121881Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1122043Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 main
2025-11-24T13:18:59.1122119Z 
2025-11-24T13:18:59.1122255Z C:\Android\android-sdk/cmdline-tools/7.0/lib/analytics-library/protos/src/main:
2025-11-24T13:18:59.1122388Z total 0
2025-11-24T13:18:59.1122522Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.1122683Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.1122846Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 proto
2025-11-24T13:18:59.1122925Z 
2025-11-24T13:18:59.1123061Z C:\Android\android-sdk/cmdline-tools/7.0/lib/analytics-library/protos/src/main/proto:
2025-11-24T13:18:59.1123204Z total 5276
2025-11-24T13:18:59.1123339Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.1123501Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.1123669Z -rw-r--r-- 1 VssAdministrator 197121 5401186 Jan  1  2010 proto.jar
2025-11-24T13:18:59.1123737Z 
2025-11-24T13:18:59.1123865Z C:\Android\android-sdk/cmdline-tools/7.0/lib/analytics-library/shared:
2025-11-24T13:18:59.1124000Z total 112
2025-11-24T13:18:59.1124134Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1124301Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1124511Z -rw-r--r-- 1 VssAdministrator 197121 112949 Jan  1  2010 tools.analytics-shared.jar
2025-11-24T13:18:59.1124635Z 
2025-11-24T13:18:59.1124771Z C:\Android\android-sdk/cmdline-tools/7.0/lib/analytics-library/tracker:
2025-11-24T13:18:59.1124902Z total 40
2025-11-24T13:18:59.1125044Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1125206Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1125377Z -rw-r--r-- 1 VssAdministrator 197121 40842 Jan  1  2010 tools.analytics-tracker.jar
2025-11-24T13:18:59.1125459Z 
2025-11-24T13:18:59.1125581Z C:\Android\android-sdk/cmdline-tools/7.0/lib/annotations:
2025-11-24T13:18:59.1125705Z total 20
2025-11-24T13:18:59.1125838Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1126006Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1126169Z -rw-r--r-- 1 VssAdministrator 197121 10561 Jan  1  2010 annotations.jar
2025-11-24T13:18:59.1126239Z 
2025-11-24T13:18:59.1126362Z C:\Android\android-sdk/cmdline-tools/7.0/lib/apkparser:
2025-11-24T13:18:59.1126485Z total 92
2025-11-24T13:18:59.1126616Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1126774Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1126942Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 analyzer
2025-11-24T13:18:59.1127179Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 cli
2025-11-24T13:18:59.1127523Z -rw-r--r-- 1 VssAdministrator 197121 84199 Jan  1  2010 tools.binary-resources.jar
2025-11-24T13:18:59.1127684Z 
2025-11-24T13:18:59.1127932Z C:\Android\android-sdk/cmdline-tools/7.0/lib/apkparser/analyzer:
2025-11-24T13:18:59.1128177Z total 104
2025-11-24T13:18:59.1128436Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1128766Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1129094Z -rw-r--r-- 1 VssAdministrator 197121 106295 Jan  1  2010 analyzer.jar
2025-11-24T13:18:59.1129234Z 
2025-11-24T13:18:59.1129471Z C:\Android\android-sdk/cmdline-tools/7.0/lib/apkparser/cli:
2025-11-24T13:18:59.1129849Z total 60
2025-11-24T13:18:59.1130121Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.1130438Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.1130770Z -rw-r--r-- 1 VssAdministrator 197121 59445 Jan  1  2010 analyzer-cli.jar
2025-11-24T13:18:59.1130932Z 
2025-11-24T13:18:59.1131184Z C:\Android\android-sdk/cmdline-tools/7.0/lib/build-system:
2025-11-24T13:18:59.1131434Z total 216
2025-11-24T13:18:59.1131711Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1132039Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1132376Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 builder-model
2025-11-24T13:18:59.1132724Z -rw-r--r-- 1 VssAdministrator 197121 212799 Jan  1  2010 tools.manifest-merger.jar
2025-11-24T13:18:59.1132884Z 
2025-11-24T13:18:59.1133144Z C:\Android\android-sdk/cmdline-tools/7.0/lib/build-system/builder-model:
2025-11-24T13:18:59.1133427Z total 112
2025-11-24T13:18:59.1133699Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1134037Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1134368Z -rw-r--r-- 1 VssAdministrator 197121 112909 Jan  1  2010 builder-model.jar
2025-11-24T13:18:59.1134515Z 
2025-11-24T13:18:59.1134746Z C:\Android\android-sdk/cmdline-tools/7.0/lib/common:
2025-11-24T13:18:59.1134990Z total 388
2025-11-24T13:18:59.1135263Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.1135593Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.1135921Z -rw-r--r-- 1 VssAdministrator 197121 389060 Jan  1  2010 tools.common.jar
2025-11-24T13:18:59.1136066Z 
2025-11-24T13:18:59.6836084Z C:\Android\android-sdk/cmdline-tools/7.0/lib/ddmlib:
2025-11-24T13:18:59.6836590Z total 588
2025-11-24T13:18:59.6836978Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6837678Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6838121Z -rw-r--r-- 1 VssAdministrator 197121 590587 Jan  1  2010 tools.ddmlib.jar
2025-11-24T13:18:59.6838365Z 
2025-11-24T13:18:59.6838707Z C:\Android\android-sdk/cmdline-tools/7.0/lib/device_validator:
2025-11-24T13:18:59.6839045Z total 56
2025-11-24T13:18:59.6839391Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6839806Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6840227Z -rw-r--r-- 1 VssAdministrator 197121 47256 Jan  1  2010 tools.dvlib.jar
2025-11-24T13:18:59.6840458Z 
2025-11-24T13:18:59.6840774Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external:
2025-11-24T13:18:59.6841100Z total 16
2025-11-24T13:18:59.6841440Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6841885Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6842326Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 archive-patcher
2025-11-24T13:18:59.6842786Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 com
2025-11-24T13:18:59.6843230Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-codec
2025-11-24T13:18:59.6843669Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-io
2025-11-24T13:18:59.6844092Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-logging
2025-11-24T13:18:59.6844537Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jakarta
2025-11-24T13:18:59.6844940Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 javax
2025-11-24T13:18:59.6845460Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 lint-psi
2025-11-24T13:18:59.6845881Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 net
2025-11-24T13:18:59.6846299Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 org
2025-11-24T13:18:59.6846722Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xerces
2025-11-24T13:18:59.6847154Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xml-apis
2025-11-24T13:18:59.6847554Z 
2025-11-24T13:18:59.6847907Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/archive-patcher:
2025-11-24T13:18:59.6848276Z total 128
2025-11-24T13:18:59.6848589Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6848900Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6849087Z -rw-r--r-- 1 VssAdministrator 197121 12156 Jan  1  2010 explainer.jar
2025-11-24T13:18:59.6849258Z -rw-r--r-- 1 VssAdministrator 197121 84159 Jan  1  2010 generator.jar
2025-11-24T13:18:59.6849750Z -rw-r--r-- 1 VssAdministrator 197121 28234 Jan  1  2010 shared.jar
2025-11-24T13:18:59.6850042Z 
2025-11-24T13:18:59.6850313Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com:
2025-11-24T13:18:59.6850488Z total 8
2025-11-24T13:18:59.6850826Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6858974Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6859357Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 android
2025-11-24T13:18:59.6859697Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 beust
2025-11-24T13:18:59.6860042Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 google
2025-11-24T13:18:59.6860370Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 sun
2025-11-24T13:18:59.6860509Z 
2025-11-24T13:18:59.6860769Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/android:
2025-11-24T13:18:59.6861026Z total 0
2025-11-24T13:18:59.6861281Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6861606Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6861934Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 tools
2025-11-24T13:18:59.6862090Z 
2025-11-24T13:18:59.6862353Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/android/tools:
2025-11-24T13:18:59.6862615Z total 0
2025-11-24T13:18:59.6862881Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6863346Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6863684Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 build
2025-11-24T13:18:59.6863833Z 
2025-11-24T13:18:59.6864089Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/android/tools/build:
2025-11-24T13:18:59.6864355Z total 0
2025-11-24T13:18:59.6864506Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6864692Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6864864Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 aapt2-proto
2025-11-24T13:18:59.6864939Z 
2025-11-24T13:18:59.6865083Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/android/tools/build/aapt2-proto:
2025-11-24T13:18:59.6865239Z total 0
2025-11-24T13:18:59.6865370Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6865528Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6865705Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 7.0.0-beta04-7396180
2025-11-24T13:18:59.6865796Z 
2025-11-24T13:18:59.6865945Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/android/tools/build/aapt2-proto/7.0.0-beta04-7396180:
2025-11-24T13:18:59.6866107Z total 732
2025-11-24T13:18:59.6866244Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6866407Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6866581Z -rw-r--r-- 1 VssAdministrator 197121 747666 Jan  1  2010 aapt2-proto-7.0.0-beta04-7396180.jar
2025-11-24T13:18:59.6866676Z 
2025-11-24T13:18:59.6866803Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/beust:
2025-11-24T13:18:59.6866932Z total 0
2025-11-24T13:18:59.6867070Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6867233Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6867398Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jcommander
2025-11-24T13:18:59.6867481Z 
2025-11-24T13:18:59.6867616Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/beust/jcommander:
2025-11-24T13:18:59.6867849Z total 0
2025-11-24T13:18:59.6867982Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6868143Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6868309Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.78
2025-11-24T13:18:59.6868380Z 
2025-11-24T13:18:59.6868517Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/beust/jcommander/1.78:
2025-11-24T13:18:59.6868659Z total 84
2025-11-24T13:18:59.6868795Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6868963Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6869130Z -rw-r--r-- 1 VssAdministrator 197121 83782 Jan  1  2010 jcommander-1.78.jar
2025-11-24T13:18:59.6869210Z 
2025-11-24T13:18:59.6869338Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google:
2025-11-24T13:18:59.6869466Z total 4
2025-11-24T13:18:59.6869605Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6869766Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6869928Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 code
2025-11-24T13:18:59.6870093Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 errorprone
2025-11-24T13:18:59.6870264Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 guava
2025-11-24T13:18:59.6870428Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 j2objc
2025-11-24T13:18:59.6870591Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jimfs
2025-11-24T13:18:59.6870756Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 protobuf
2025-11-24T13:18:59.6870835Z 
2025-11-24T13:18:59.6870962Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/code:
2025-11-24T13:18:59.6871090Z total 4
2025-11-24T13:18:59.6871229Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6871388Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6871602Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 findbugs
2025-11-24T13:18:59.6871771Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 gson
2025-11-24T13:18:59.6871848Z 
2025-11-24T13:18:59.6871979Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/code/findbugs:
2025-11-24T13:18:59.6872113Z total 0
2025-11-24T13:18:59.6872249Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6872410Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6872570Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jsr305
2025-11-24T13:18:59.6872647Z 
2025-11-24T13:18:59.6872783Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/code/findbugs/jsr305:
2025-11-24T13:18:59.6872919Z total 0
2025-11-24T13:18:59.6873048Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6873204Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6873369Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.0.2
2025-11-24T13:18:59.6873443Z 
2025-11-24T13:18:59.6873579Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/code/findbugs/jsr305/3.0.2:
2025-11-24T13:18:59.6873725Z total 20
2025-11-24T13:18:59.6873855Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6874015Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6874177Z -rw-r--r-- 1 VssAdministrator 197121 19936 Jan  1  2010 jsr305-3.0.2.jar
2025-11-24T13:18:59.6874255Z 
2025-11-24T13:18:59.6874384Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/code/gson:
2025-11-24T13:18:59.6874517Z total 0
2025-11-24T13:18:59.6874656Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6874819Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6874981Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 gson
2025-11-24T13:18:59.6875058Z 
2025-11-24T13:18:59.6875193Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/code/gson/gson:
2025-11-24T13:18:59.6875370Z total 0
2025-11-24T13:18:59.6875500Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6875665Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6875826Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.8.6
2025-11-24T13:18:59.6875898Z 
2025-11-24T13:18:59.6876037Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/code/gson/gson/2.8.6:
2025-11-24T13:18:59.6876174Z total 236
2025-11-24T13:18:59.6876307Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6876473Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6876644Z -rw-r--r-- 1 VssAdministrator 197121 240255 Jan  1  2010 gson-2.8.6.jar
2025-11-24T13:18:59.6876715Z 
2025-11-24T13:18:59.6876848Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/errorprone:
2025-11-24T13:18:59.6876985Z total 4
2025-11-24T13:18:59.6877115Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6877277Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6877468Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 error_prone_annotations
2025-11-24T13:18:59.6877646Z 
2025-11-24T13:18:59.6878447Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/errorprone/error_prone_annotations:
2025-11-24T13:18:59.6878749Z total 0
2025-11-24T13:18:59.6878888Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6879059Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6879224Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.3.4
2025-11-24T13:18:59.6879298Z 
2025-11-24T13:18:59.6879454Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/errorprone/error_prone_annotations/2.3.4:
2025-11-24T13:18:59.6879606Z total 16
2025-11-24T13:18:59.6879740Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6879996Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6880177Z -rw-r--r-- 1 VssAdministrator 197121 13879 Jan  1  2010 error_prone_annotations-2.3.4.jar
2025-11-24T13:18:59.6880260Z 
2025-11-24T13:18:59.6880388Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/guava:
2025-11-24T13:18:59.6880523Z total 4
2025-11-24T13:18:59.6880658Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6880855Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6881022Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 failureaccess
2025-11-24T13:18:59.6881198Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 guava
2025-11-24T13:18:59.6881370Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 listenablefuture
2025-11-24T13:18:59.6881448Z 
2025-11-24T13:18:59.6881598Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/guava/failureaccess:
2025-11-24T13:18:59.6881738Z total 0
2025-11-24T13:18:59.6881868Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6882029Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6882197Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.0.1
2025-11-24T13:18:59.6882268Z 
2025-11-24T13:18:59.6882408Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/guava/failureaccess/1.0.1:
2025-11-24T13:18:59.6882555Z total 8
2025-11-24T13:18:59.6882689Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 .
2025-11-24T13:18:59.6882854Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 ..
2025-11-24T13:18:59.6883024Z -rw-r--r-- 1 VssAdministrator 197121 4617 Jan  1  2010 failureaccess-1.0.1.jar
2025-11-24T13:18:59.6883104Z 
2025-11-24T13:18:59.6883236Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/guava/guava:
2025-11-24T13:18:59.6883369Z total 0
2025-11-24T13:18:59.6883504Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6883663Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6883884Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 30.1-jre
2025-11-24T13:18:59.6883958Z 
2025-11-24T13:18:59.6884102Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/guava/guava/30.1-jre:
2025-11-24T13:18:59.6884243Z total 2796
2025-11-24T13:18:59.6884383Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.6884546Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.6884718Z -rw-r--r-- 1 VssAdministrator 197121 2862361 Jan  1  2010 guava-30.1-jre.jar
2025-11-24T13:18:59.6884791Z 
2025-11-24T13:18:59.6884929Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/guava/listenablefuture:
2025-11-24T13:18:59.6885075Z total 0
2025-11-24T13:18:59.6885204Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6885364Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6885545Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 9999.0-empty-to-avoid-conflict-with-guava
2025-11-24T13:18:59.6885645Z 
2025-11-24T13:18:59.6885809Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava:
2025-11-24T13:18:59.6885977Z total 4
2025-11-24T13:18:59.6886112Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 .
2025-11-24T13:18:59.6886273Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 ..
2025-11-24T13:18:59.6886461Z -rw-r--r-- 1 VssAdministrator 197121 2199 Jan  1  2010 listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
2025-11-24T13:18:59.6886565Z 
2025-11-24T13:18:59.6886694Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/j2objc:
2025-11-24T13:18:59.6886826Z total 4
2025-11-24T13:18:59.6886954Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6887134Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6887302Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 j2objc-annotations
2025-11-24T13:18:59.6887422Z 
2025-11-24T13:18:59.6887577Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/j2objc/j2objc-annotations:
2025-11-24T13:18:59.6887718Z total 0
2025-11-24T13:18:59.6887850Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6888009Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6888176Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.3
2025-11-24T13:18:59.6888248Z 
2025-11-24T13:18:59.6888389Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/j2objc/j2objc-annotations/1.3:
2025-11-24T13:18:59.6888539Z total 12
2025-11-24T13:18:59.6888675Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 .
2025-11-24T13:18:59.6888838Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 ..
2025-11-24T13:18:59.6889009Z -rw-r--r-- 1 VssAdministrator 197121 8781 Jan  1  2010 j2objc-annotations-1.3.jar
2025-11-24T13:18:59.6889093Z 
2025-11-24T13:18:59.6889223Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/jimfs:
2025-11-24T13:18:59.6889359Z total 4
2025-11-24T13:18:59.6889495Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6889657Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6889820Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jimfs
2025-11-24T13:18:59.6889896Z 
2025-11-24T13:18:59.6890026Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/jimfs/jimfs:
2025-11-24T13:18:59.6890159Z total 0
2025-11-24T13:18:59.6890289Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6890447Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6890610Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.1
2025-11-24T13:18:59.6890680Z 
2025-11-24T13:18:59.6890813Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/jimfs/jimfs/1.1:
2025-11-24T13:18:59.6890958Z total 204
2025-11-24T13:18:59.6891093Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6891299Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6891461Z -rw-r--r-- 1 VssAdministrator 197121 206691 Jan  1  2010 jimfs-1.1.jar
2025-11-24T13:18:59.6891536Z 
2025-11-24T13:18:59.6891668Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/protobuf:
2025-11-24T13:18:59.6891798Z total 4
2025-11-24T13:18:59.6891932Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6892090Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6892256Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 protobuf-java
2025-11-24T13:18:59.6892337Z 
2025-11-24T13:18:59.6892473Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/protobuf/protobuf-java:
2025-11-24T13:18:59.6892611Z total 0
2025-11-24T13:18:59.6892739Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6892903Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6893065Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.10.0
2025-11-24T13:18:59.6893138Z 
2025-11-24T13:18:59.6893282Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/google/protobuf/protobuf-java/3.10.0:
2025-11-24T13:18:59.6893426Z total 1628
2025-11-24T13:18:59.6893561Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.6893720Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.6893893Z -rw-r--r-- 1 VssAdministrator 197121 1664677 Jan  1  2010 protobuf-java-3.10.0.jar
2025-11-24T13:18:59.6893970Z 
2025-11-24T13:18:59.6894093Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun:
2025-11-24T13:18:59.6894222Z total 0
2025-11-24T13:18:59.6894350Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6894508Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6894673Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 activation
2025-11-24T13:18:59.6894884Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 istack
2025-11-24T13:18:59.6895050Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xml
2025-11-24T13:18:59.6895119Z 
2025-11-24T13:18:59.6895249Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun/activation:
2025-11-24T13:18:59.6895386Z total 0
2025-11-24T13:18:59.6895514Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6895670Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6895838Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 javax.activation
2025-11-24T13:18:59.6895920Z 
2025-11-24T13:18:59.6896056Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun/activation/javax.activation:
2025-11-24T13:18:59.6896196Z total 0
2025-11-24T13:18:59.6896329Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6896489Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6896650Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.2.0
2025-11-24T13:18:59.6896729Z 
2025-11-24T13:18:59.6896868Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun/activation/javax.activation/1.2.0:
2025-11-24T13:18:59.6897011Z total 80
2025-11-24T13:18:59.6897142Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6897307Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6897476Z -rw-r--r-- 1 VssAdministrator 197121 78030 Jan  1  2010 javax.activation-1.2.0.jar
2025-11-24T13:18:59.6897552Z 
2025-11-24T13:18:59.6897684Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun/istack:
2025-11-24T13:18:59.6897812Z total 0
2025-11-24T13:18:59.6897941Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6898097Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6898272Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 istack-commons-runtime
2025-11-24T13:18:59.6898353Z 
2025-11-24T13:18:59.6898491Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun/istack/istack-commons-runtime:
2025-11-24T13:18:59.6898678Z total 0
2025-11-24T13:18:59.6898806Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6898964Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6899135Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.0.8
2025-11-24T13:18:59.6899210Z 
2025-11-24T13:18:59.6899352Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun/istack/istack-commons-runtime/3.0.8:
2025-11-24T13:18:59.6899496Z total 28
2025-11-24T13:18:59.6899627Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6899797Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6899967Z -rw-r--r-- 1 VssAdministrator 197121 27156 Jan  1  2010 istack-commons-runtime-3.0.8.jar
2025-11-24T13:18:59.6900050Z 
2025-11-24T13:18:59.6900175Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun/xml:
2025-11-24T13:18:59.6900303Z total 0
2025-11-24T13:18:59.6900435Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6900595Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6900771Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 fastinfoset
2025-11-24T13:18:59.6900845Z 
2025-11-24T13:18:59.6900975Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun/xml/fastinfoset:
2025-11-24T13:18:59.6901112Z total 0
2025-11-24T13:18:59.6901240Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6901399Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6901564Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 FastInfoset
2025-11-24T13:18:59.6901645Z 
2025-11-24T13:18:59.6901781Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun/xml/fastinfoset/FastInfoset:
2025-11-24T13:18:59.6901920Z total 0
2025-11-24T13:18:59.6902055Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6902215Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6902872Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.2.16
2025-11-24T13:18:59.6902950Z 
2025-11-24T13:18:59.6903092Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/com/sun/xml/fastinfoset/FastInfoset/1.2.16:
2025-11-24T13:18:59.6903236Z total 312
2025-11-24T13:18:59.6903372Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6903540Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6903709Z -rw-r--r-- 1 VssAdministrator 197121 317195 Jan  1  2010 FastInfoset-1.2.16.jar
2025-11-24T13:18:59.6903785Z 
2025-11-24T13:18:59.6903918Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/commons-codec:
2025-11-24T13:18:59.6904044Z total 4
2025-11-24T13:18:59.6904173Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6904332Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6904520Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-codec
2025-11-24T13:18:59.6904598Z 
2025-11-24T13:18:59.6904736Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/commons-codec/commons-codec:
2025-11-24T13:18:59.6904878Z total 0
2025-11-24T13:18:59.6905006Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6905164Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6905324Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.11
2025-11-24T13:18:59.6905400Z 
2025-11-24T13:18:59.6905539Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/commons-codec/commons-codec/1.11:
2025-11-24T13:18:59.6905678Z total 328
2025-11-24T13:18:59.6905816Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6905976Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6906144Z -rw-r--r-- 1 VssAdministrator 197121 335042 Jan  1  2010 commons-codec-1.11.jar
2025-11-24T13:18:59.6906224Z 
2025-11-24T13:18:59.6906351Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/commons-io:
2025-11-24T13:18:59.6906531Z total 4
2025-11-24T13:18:59.6906661Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6906821Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6906993Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-io
2025-11-24T13:18:59.6907067Z 
2025-11-24T13:18:59.6907197Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/commons-io/commons-io:
2025-11-24T13:18:59.6907338Z total 0
2025-11-24T13:18:59.6907467Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6907625Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6907788Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.4
2025-11-24T13:18:59.6907866Z 
2025-11-24T13:18:59.6908000Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/commons-io/commons-io/2.4:
2025-11-24T13:18:59.6908136Z total 184
2025-11-24T13:18:59.6908273Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6908436Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6908601Z -rw-r--r-- 1 VssAdministrator 197121 185140 Jan  1  2010 commons-io-2.4.jar
2025-11-24T13:18:59.6908679Z 
2025-11-24T13:18:59.6908808Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/commons-logging:
2025-11-24T13:18:59.6908935Z total 4
2025-11-24T13:18:59.6909062Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6909226Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6909394Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-logging
2025-11-24T13:18:59.6909470Z 
2025-11-24T13:18:59.6909609Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/commons-logging/commons-logging:
2025-11-24T13:18:59.6909745Z total 0
2025-11-24T13:18:59.6909872Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6910029Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6910235Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.2
2025-11-24T13:18:59.6910307Z 
2025-11-24T13:18:59.6910443Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/commons-logging/commons-logging/1.2:
2025-11-24T13:18:59.6910584Z total 64
2025-11-24T13:18:59.6910720Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6910881Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6911047Z -rw-r--r-- 1 VssAdministrator 197121 61829 Jan  1  2010 commons-logging-1.2.jar
2025-11-24T13:18:59.6911127Z 
2025-11-24T13:18:59.6911250Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/jakarta:
2025-11-24T13:18:59.6911372Z total 4
2025-11-24T13:18:59.6911500Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6911662Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6911825Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 activation
2025-11-24T13:18:59.6911989Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xml
2025-11-24T13:18:59.6912068Z 
2025-11-24T13:18:59.6912197Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/jakarta/activation:
2025-11-24T13:18:59.6912327Z total 0
2025-11-24T13:18:59.6912455Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6912618Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6912787Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jakarta.activation-api
2025-11-24T13:18:59.6912866Z 
2025-11-24T13:18:59.6913013Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/jakarta/activation/jakarta.activation-api:
2025-11-24T13:18:59.6913571Z total 0
2025-11-24T13:18:59.6913841Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6914163Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6914491Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.2.1
2025-11-24T13:18:59.6914633Z 
2025-11-24T13:18:59.6914930Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/jakarta/activation/jakarta.activation-api/1.2.1:
2025-11-24T13:18:59.6915360Z total 44
2025-11-24T13:18:59.6915616Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6915949Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6916292Z -rw-r--r-- 1 VssAdministrator 197121 44399 Jan  1  2010 jakarta.activation-api-1.2.1.jar
2025-11-24T13:18:59.6916461Z 
2025-11-24T13:18:59.6916717Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/jakarta/xml:
2025-11-24T13:18:59.6916971Z total 0
2025-11-24T13:18:59.6917233Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6917569Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6917897Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 bind
2025-11-24T13:18:59.6918038Z 
2025-11-24T13:18:59.6918295Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/jakarta/xml/bind:
2025-11-24T13:18:59.6918554Z total 0
2025-11-24T13:18:59.6918817Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6919129Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6919480Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jakarta.xml.bind-api
2025-11-24T13:18:59.6919640Z 
2025-11-24T13:18:59.6919910Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/jakarta/xml/bind/jakarta.xml.bind-api:
2025-11-24T13:18:59.6920190Z total 0
2025-11-24T13:18:59.6920450Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6920763Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6921081Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.3.2
2025-11-24T13:18:59.6921236Z 
2025-11-24T13:18:59.6921519Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/jakarta/xml/bind/jakarta.xml.bind-api/2.3.2:
2025-11-24T13:18:59.6921816Z total 116
2025-11-24T13:18:59.6922095Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6922549Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6922899Z -rw-r--r-- 1 VssAdministrator 197121 115498 Jan  1  2010 jakarta.xml.bind-api-2.3.2.jar
2025-11-24T13:18:59.6923096Z 
2025-11-24T13:18:59.6923353Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/javax:
2025-11-24T13:18:59.6923599Z total 4
2025-11-24T13:18:59.6923864Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6924122Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6924287Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 inject
2025-11-24T13:18:59.6924360Z 
2025-11-24T13:18:59.6924492Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/javax/inject:
2025-11-24T13:18:59.6924619Z total 0
2025-11-24T13:18:59.6924751Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6924910Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6925082Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 javax.inject
2025-11-24T13:18:59.6925166Z 
2025-11-24T13:18:59.6925304Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/javax/inject/javax.inject:
2025-11-24T13:18:59.6925440Z total 0
2025-11-24T13:18:59.6925578Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6925741Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6925897Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1
2025-11-24T13:18:59.6925972Z 
2025-11-24T13:18:59.6926107Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/javax/inject/javax.inject/1:
2025-11-24T13:18:59.6926245Z total 4
2025-11-24T13:18:59.6926375Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 .
2025-11-24T13:18:59.6926546Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 22:04 ..
2025-11-24T13:18:59.6926713Z -rw-r--r-- 1 VssAdministrator 197121 2497 Jan  1  2010 javax.inject-1.jar
2025-11-24T13:18:59.6926786Z 
2025-11-24T13:18:59.6926915Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/lint-psi:
2025-11-24T13:18:59.6927044Z total 4
2025-11-24T13:18:59.6927264Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6927423Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6927599Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 intellij-core
2025-11-24T13:18:59.6927773Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-compiler
2025-11-24T13:18:59.6927942Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 uast
2025-11-24T13:18:59.6928020Z 
2025-11-24T13:18:59.6928153Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/lint-psi/intellij-core:
2025-11-24T13:18:59.6928291Z total 19404
2025-11-24T13:18:59.6928429Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 .
2025-11-24T13:18:59.6928598Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 ..
2025-11-24T13:18:59.6928766Z -rw-r--r-- 1 VssAdministrator 197121 19869676 Jan  1  2010 intellij-core-mvn.jar
2025-11-24T13:18:59.6928840Z 
2025-11-24T13:18:59.6928980Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/lint-psi/kotlin-compiler:
2025-11-24T13:18:59.6929120Z total 38164
2025-11-24T13:18:59.6929253Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 .
2025-11-24T13:18:59.6929415Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 22:04 ..
2025-11-24T13:18:59.6929588Z -rw-r--r-- 1 VssAdministrator 197121 39078264 Jan  1  2010 kotlin-compiler-mvn.jar
2025-11-24T13:18:59.6929664Z 
2025-11-24T13:18:59.6929793Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/lint-psi/uast:
2025-11-24T13:18:59.6929929Z total 2424
2025-11-24T13:18:59.6930062Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.6930222Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.6930381Z -rw-r--r-- 1 VssAdministrator 197121 2479017 Jan  1  2010 uast.jar
2025-11-24T13:18:59.6930455Z 
2025-11-24T13:18:59.6930575Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net:
2025-11-24T13:18:59.6930748Z total 4
2025-11-24T13:18:59.6930877Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6931043Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6931202Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 java
2025-11-24T13:18:59.6931362Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 sf
2025-11-24T13:18:59.6931436Z 
2025-11-24T13:18:59.6931560Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/java:
2025-11-24T13:18:59.6931692Z total 0
2025-11-24T13:18:59.6931820Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6931982Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6932141Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 dev
2025-11-24T13:18:59.6932211Z 
2025-11-24T13:18:59.6932339Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/java/dev:
2025-11-24T13:18:59.6932463Z total 0
2025-11-24T13:18:59.6932591Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6932750Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6932916Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jna
2025-11-24T13:18:59.6932986Z 
2025-11-24T13:18:59.6933113Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/java/dev/jna:
2025-11-24T13:18:59.6933246Z total 0
2025-11-24T13:18:59.6933373Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6933530Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6933688Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jna
2025-11-24T13:18:59.6933854Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jna-platform
2025-11-24T13:18:59.6933934Z 
2025-11-24T13:18:59.6934062Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/java/dev/jna/jna:
2025-11-24T13:18:59.6934194Z total 0
2025-11-24T13:18:59.6934328Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6934487Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6934651Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 5.6.0
2025-11-24T13:18:59.6934770Z 
2025-11-24T13:18:59.6934904Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/java/dev/jna/jna/5.6.0:
2025-11-24T13:18:59.6935039Z total 1476
2025-11-24T13:18:59.6935173Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.6935342Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.6935506Z -rw-r--r-- 1 VssAdministrator 197121 1509440 Jan  1  2010 jna-5.6.0.jar
2025-11-24T13:18:59.6935577Z 
2025-11-24T13:18:59.6935717Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/java/dev/jna/jna-platform:
2025-11-24T13:18:59.6935852Z total 0
2025-11-24T13:18:59.6935981Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6936138Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6936305Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 5.6.0
2025-11-24T13:18:59.6936378Z 
2025-11-24T13:18:59.6936513Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/java/dev/jna/jna-platform/5.6.0:
2025-11-24T13:18:59.6936662Z total 2672
2025-11-24T13:18:59.6936847Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.6937010Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.6937177Z -rw-r--r-- 1 VssAdministrator 197121 2735878 Jan  1  2010 jna-platform-5.6.0.jar
2025-11-24T13:18:59.6937259Z 
2025-11-24T13:18:59.6937384Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/sf:
2025-11-24T13:18:59.6937507Z total 0
2025-11-24T13:18:59.6937641Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6937800Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6937966Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jopt-simple
2025-11-24T13:18:59.6938132Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kxml
2025-11-24T13:18:59.6938208Z 
2025-11-24T13:18:59.6938379Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/sf/jopt-simple:
2025-11-24T13:18:59.6938511Z total 0
2025-11-24T13:18:59.6938641Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6938806Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6938970Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jopt-simple
2025-11-24T13:18:59.6939045Z 
2025-11-24T13:18:59.6939186Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/sf/jopt-simple/jopt-simple:
2025-11-24T13:18:59.6939321Z total 0
2025-11-24T13:18:59.6939449Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6939606Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6939770Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 4.9
2025-11-24T13:18:59.6939841Z 
2025-11-24T13:18:59.6939977Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/sf/jopt-simple/jopt-simple/4.9:
2025-11-24T13:18:59.6940127Z total 68
2025-11-24T13:18:59.6940263Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6940424Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6940588Z -rw-r--r-- 1 VssAdministrator 197121 66469 Jan  1  2010 jopt-simple-4.9.jar
2025-11-24T13:18:59.6940666Z 
2025-11-24T13:18:59.6940792Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/sf/kxml:
2025-11-24T13:18:59.6940918Z total 0
2025-11-24T13:18:59.6941052Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6941212Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6941376Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kxml2
2025-11-24T13:18:59.6941454Z 
2025-11-24T13:18:59.6941584Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/sf/kxml/kxml2:
2025-11-24T13:18:59.6941722Z total 0
2025-11-24T13:18:59.6941852Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6942020Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6942182Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.3.0
2025-11-24T13:18:59.6942295Z 
2025-11-24T13:18:59.6942428Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/net/sf/kxml/kxml2/2.3.0:
2025-11-24T13:18:59.6942569Z total 44
2025-11-24T13:18:59.6942702Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6942866Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6943029Z -rw-r--r-- 1 VssAdministrator 197121 43858 Jan  1  2010 kxml2-2.3.0.jar
2025-11-24T13:18:59.6943106Z 
2025-11-24T13:18:59.6943227Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org:
2025-11-24T13:18:59.6943350Z total 8
2025-11-24T13:18:59.6943506Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6943664Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6943825Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 apache
2025-11-24T13:18:59.6943993Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 bouncycastle
2025-11-24T13:18:59.6944178Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 checkerframework
2025-11-24T13:18:59.6944351Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 glassfish
2025-11-24T13:18:59.6944520Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jetbrains
2025-11-24T13:18:59.6944686Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jvnet
2025-11-24T13:18:59.6944854Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ow2
2025-11-24T13:18:59.6945016Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 smali
2025-11-24T13:18:59.6945085Z 
2025-11-24T13:18:59.6945217Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache:
2025-11-24T13:18:59.6945342Z total 4
2025-11-24T13:18:59.6945474Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6945633Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6945801Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons
2025-11-24T13:18:59.6946009Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 httpcomponents
2025-11-24T13:18:59.6946087Z 
2025-11-24T13:18:59.6946230Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache/commons:
2025-11-24T13:18:59.6946360Z total 0
2025-11-24T13:18:59.6946487Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6946644Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6946814Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 commons-compress
2025-11-24T13:18:59.6946890Z 
2025-11-24T13:18:59.6947027Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache/commons/commons-compress:
2025-11-24T13:18:59.6947173Z total 0
2025-11-24T13:18:59.6947302Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6947459Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6947618Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.20
2025-11-24T13:18:59.6947693Z 
2025-11-24T13:18:59.6947836Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache/commons/commons-compress/1.20:
2025-11-24T13:18:59.6947982Z total 620
2025-11-24T13:18:59.6948115Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6948281Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6948447Z -rw-r--r-- 1 VssAdministrator 197121 632424 Jan  1  2010 commons-compress-1.20.jar
2025-11-24T13:18:59.6948529Z 
2025-11-24T13:18:59.6948662Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache/httpcomponents:
2025-11-24T13:18:59.6948796Z total 0
2025-11-24T13:18:59.6948926Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6949085Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6949254Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 httpclient
2025-11-24T13:18:59.6949421Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 httpcore
2025-11-24T13:18:59.6949588Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 httpmime
2025-11-24T13:18:59.6949707Z 
2025-11-24T13:18:59.6949845Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache/httpcomponents/httpclient:
2025-11-24T13:18:59.6949984Z total 0
2025-11-24T13:18:59.6950115Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6950278Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6950438Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 4.5.9
2025-11-24T13:18:59.6950509Z 
2025-11-24T13:18:59.6950655Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache/httpcomponents/httpclient/4.5.9:
2025-11-24T13:18:59.6950800Z total 760
2025-11-24T13:18:59.6950932Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6951093Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6951263Z -rw-r--r-- 1 VssAdministrator 197121 774384 Jan  1  2010 httpclient-4.5.9.jar
2025-11-24T13:18:59.6951337Z 
2025-11-24T13:18:59.6951474Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache/httpcomponents/httpcore:
2025-11-24T13:18:59.6951621Z total 0
2025-11-24T13:18:59.6951758Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6951915Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6952077Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 4.4.11
2025-11-24T13:18:59.6952154Z 
2025-11-24T13:18:59.6952294Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache/httpcomponents/httpcore/4.4.11:
2025-11-24T13:18:59.6952436Z total 320
2025-11-24T13:18:59.6952574Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6952734Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6952900Z -rw-r--r-- 1 VssAdministrator 197121 326874 Jan  1  2010 httpcore-4.4.11.jar
2025-11-24T13:18:59.6952979Z 
2025-11-24T13:18:59.6953115Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache/httpcomponents/httpmime:
2025-11-24T13:18:59.6953296Z total 0
2025-11-24T13:18:59.6953425Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6953589Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6953750Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 4.5.6
2025-11-24T13:18:59.6953819Z 
2025-11-24T13:18:59.6953959Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/apache/httpcomponents/httpmime/4.5.6:
2025-11-24T13:18:59.6954104Z total 44
2025-11-24T13:18:59.6954236Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6954396Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6954562Z -rw-r--r-- 1 VssAdministrator 197121 41794 Jan  1  2010 httpmime-4.5.6.jar
2025-11-24T13:18:59.6954634Z 
2025-11-24T13:18:59.6954761Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/bouncycastle:
2025-11-24T13:18:59.6954891Z total 4
2025-11-24T13:18:59.6955027Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6955188Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6955355Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 bcpkix-jdk15on
2025-11-24T13:18:59.6955528Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 bcprov-jdk15on
2025-11-24T13:18:59.6955609Z 
2025-11-24T13:18:59.6955747Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/bouncycastle/bcpkix-jdk15on:
2025-11-24T13:18:59.6955883Z total 0
2025-11-24T13:18:59.6956017Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6956175Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6956336Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.56
2025-11-24T13:18:59.6956412Z 
2025-11-24T13:18:59.6956550Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/bouncycastle/bcpkix-jdk15on/1.56:
2025-11-24T13:18:59.6956696Z total 672
2025-11-24T13:18:59.6956830Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6957001Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6957208Z -rw-r--r-- 1 VssAdministrator 197121 685403 Jan  1  2010 bcpkix-jdk15on-1.56.jar
2025-11-24T13:18:59.6957284Z 
2025-11-24T13:18:59.6957427Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/bouncycastle/bcprov-jdk15on:
2025-11-24T13:18:59.6957562Z total 0
2025-11-24T13:18:59.6957692Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6957848Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6958020Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.56
2025-11-24T13:18:59.6958091Z 
2025-11-24T13:18:59.6958227Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/bouncycastle/bcprov-jdk15on/1.56:
2025-11-24T13:18:59.6958374Z total 3368
2025-11-24T13:18:59.6958508Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.6958669Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.6958839Z -rw-r--r-- 1 VssAdministrator 197121 3448507 Jan  1  2010 bcprov-jdk15on-1.56.jar
2025-11-24T13:18:59.6958922Z 
2025-11-24T13:18:59.6959052Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/checkerframework:
2025-11-24T13:18:59.6959184Z total 4
2025-11-24T13:18:59.6959318Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6959477Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6959641Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 checker-qual
2025-11-24T13:18:59.6959717Z 
2025-11-24T13:18:59.6959859Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/checkerframework/checker-qual:
2025-11-24T13:18:59.6959997Z total 0
2025-11-24T13:18:59.6960126Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6960282Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6960450Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 3.5.0
2025-11-24T13:18:59.6960522Z 
2025-11-24T13:18:59.6960705Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/checkerframework/checker-qual/3.5.0:
2025-11-24T13:18:59.6960858Z total 212
2025-11-24T13:18:59.6960990Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6961153Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6961319Z -rw-r--r-- 1 VssAdministrator 197121 214381 Jan  1  2010 checker-qual-3.5.0.jar
2025-11-24T13:18:59.6961400Z 
2025-11-24T13:18:59.6961533Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/glassfish:
2025-11-24T13:18:59.6961661Z total 4
2025-11-24T13:18:59.6961793Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6961951Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6962110Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jaxb
2025-11-24T13:18:59.6962184Z 
2025-11-24T13:18:59.6962313Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/glassfish/jaxb:
2025-11-24T13:18:59.6962445Z total 0
2025-11-24T13:18:59.6962572Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6962735Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6962901Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 jaxb-runtime
2025-11-24T13:18:59.6963069Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 txw2
2025-11-24T13:18:59.6963143Z 
2025-11-24T13:18:59.6963278Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/glassfish/jaxb/jaxb-runtime:
2025-11-24T13:18:59.6963413Z total 0
2025-11-24T13:18:59.6963539Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6963702Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6963863Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.3.2
2025-11-24T13:18:59.6963934Z 
2025-11-24T13:18:59.6964071Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/glassfish/jaxb/jaxb-runtime/2.3.2:
2025-11-24T13:18:59.6964218Z total 992
2025-11-24T13:18:59.6964352Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.6964555Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.6964721Z -rw-r--r-- 1 VssAdministrator 197121 1013367 Jan  1  2010 jaxb-runtime-2.3.2.jar
2025-11-24T13:18:59.6964802Z 
2025-11-24T13:18:59.6964933Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/glassfish/jaxb/txw2:
2025-11-24T13:18:59.6965063Z total 0
2025-11-24T13:18:59.6965199Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6965357Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6965520Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.3.2
2025-11-24T13:18:59.6965595Z 
2025-11-24T13:18:59.6965730Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/glassfish/jaxb/txw2/2.3.2:
2025-11-24T13:18:59.6965867Z total 72
2025-11-24T13:18:59.6966001Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6966167Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6966333Z -rw-r--r-- 1 VssAdministrator 197121 72080 Jan  1  2010 txw2-2.3.2.jar
2025-11-24T13:18:59.6966402Z 
2025-11-24T13:18:59.6966537Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains:
2025-11-24T13:18:59.6966665Z total 8
2025-11-24T13:18:59.6966804Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6966971Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6967141Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 annotations
2025-11-24T13:18:59.6967310Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 intellij
2025-11-24T13:18:59.6967475Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin
2025-11-24T13:18:59.6967638Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlinx
2025-11-24T13:18:59.6967716Z 
2025-11-24T13:18:59.6967849Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/annotations:
2025-11-24T13:18:59.6967984Z total 0
2025-11-24T13:18:59.6968160Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6968322Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6968485Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 13.0
2025-11-24T13:18:59.6968563Z 
2025-11-24T13:18:59.6968700Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/annotations/13.0:
2025-11-24T13:18:59.6968835Z total 20
2025-11-24T13:18:59.6968965Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6969128Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6969299Z -rw-r--r-- 1 VssAdministrator 197121 17536 Jan  1  2010 annotations-13.0.jar
2025-11-24T13:18:59.6969372Z 
2025-11-24T13:18:59.6969504Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/intellij:
2025-11-24T13:18:59.6969643Z total 0
2025-11-24T13:18:59.6969773Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6969935Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6970099Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 deps
2025-11-24T13:18:59.6970175Z 
2025-11-24T13:18:59.6970308Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/intellij/deps:
2025-11-24T13:18:59.6970441Z total 0
2025-11-24T13:18:59.6970576Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6970734Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6970896Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 trove4j
2025-11-24T13:18:59.6970974Z 
2025-11-24T13:18:59.6971111Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/intellij/deps/trove4j:
2025-11-24T13:18:59.6971250Z total 0
2025-11-24T13:18:59.6971379Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6971546Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6971712Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.0.20181211
2025-11-24T13:18:59.6971789Z 
2025-11-24T13:18:59.6972286Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/intellij/deps/trove4j/1.0.20181211:
2025-11-24T13:18:59.6972446Z total 560
2025-11-24T13:18:59.6972585Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6972748Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6972925Z -rw-r--r-- 1 VssAdministrator 197121 572966 Jan  1  2010 trove4j-1.0.20181211.jar
2025-11-24T13:18:59.6973002Z 
2025-11-24T13:18:59.6973135Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin:
2025-11-24T13:18:59.6973275Z total 4
2025-11-24T13:18:59.6973405Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6973565Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6973731Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-reflect
2025-11-24T13:18:59.6973913Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-stdlib
2025-11-24T13:18:59.6974096Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-stdlib-common
2025-11-24T13:18:59.6974276Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-stdlib-jdk7
2025-11-24T13:18:59.6974453Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlin-stdlib-jdk8
2025-11-24T13:18:59.6974537Z 
2025-11-24T13:18:59.6974674Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin/kotlin-reflect:
2025-11-24T13:18:59.6974816Z total 4
2025-11-24T13:18:59.6974951Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6975112Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6975274Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.5.31
2025-11-24T13:18:59.6975354Z 
2025-11-24T13:18:59.6975497Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin/kotlin-reflect/1.5.31:
2025-11-24T13:18:59.6975644Z total 2964
2025-11-24T13:18:59.6975783Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.6976001Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.6976171Z -rw-r--r-- 1 VssAdministrator 197121 3031425 Jan  1  2010 kotlin-reflect-1.5.31.jar
2025-11-24T13:18:59.6976248Z 
2025-11-24T13:18:59.6976385Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib:
2025-11-24T13:18:59.6976530Z total 4
2025-11-24T13:18:59.6976660Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6976819Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6976981Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.5.31
2025-11-24T13:18:59.6977058Z 
2025-11-24T13:18:59.6977197Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib/1.5.31:
2025-11-24T13:18:59.6977342Z total 1472
2025-11-24T13:18:59.6977482Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.6977642Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.6977815Z -rw-r--r-- 1 VssAdministrator 197121 1505952 Jan  1  2010 kotlin-stdlib-1.5.31.jar
2025-11-24T13:18:59.6977896Z 
2025-11-24T13:18:59.6978036Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-common:
2025-11-24T13:18:59.6978178Z total 4
2025-11-24T13:18:59.6978307Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6978470Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6978631Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.5.31
2025-11-24T13:18:59.6978703Z 
2025-11-24T13:18:59.6978854Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-common/1.5.31:
2025-11-24T13:18:59.6979001Z total 196
2025-11-24T13:18:59.6979132Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6979292Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6979472Z -rw-r--r-- 1 VssAdministrator 197121 198322 Jan  1  2010 kotlin-stdlib-common-1.5.31.jar
2025-11-24T13:18:59.6979791Z 
2025-11-24T13:18:59.6979937Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk7:
2025-11-24T13:18:59.6980086Z total 4
2025-11-24T13:18:59.6980219Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6980379Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6980542Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.5.31
2025-11-24T13:18:59.6980620Z 
2025-11-24T13:18:59.6980815Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk7/1.5.31:
2025-11-24T13:18:59.6980962Z total 24
2025-11-24T13:18:59.6981101Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6981262Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6981431Z -rw-r--r-- 1 VssAdministrator 197121 22986 Jan  1  2010 kotlin-stdlib-jdk7-1.5.31.jar
2025-11-24T13:18:59.6981519Z 
2025-11-24T13:18:59.6981659Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk8:
2025-11-24T13:18:59.6981799Z total 4
2025-11-24T13:18:59.6981927Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6982090Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6982251Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.5.31
2025-11-24T13:18:59.6982322Z 
2025-11-24T13:18:59.6982469Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk8/1.5.31:
2025-11-24T13:18:59.6982614Z total 16
2025-11-24T13:18:59.6982746Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6982905Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6983078Z -rw-r--r-- 1 VssAdministrator 197121 16121 Jan  1  2010 kotlin-stdlib-jdk8-1.5.31.jar
2025-11-24T13:18:59.6983156Z 
2025-11-24T13:18:59.6983286Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlinx:
2025-11-24T13:18:59.6983471Z total 0
2025-11-24T13:18:59.6983600Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6983760Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6983926Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 kotlinx-cli-jvm
2025-11-24T13:18:59.6984019Z 
2025-11-24T13:18:59.6984171Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlinx/kotlinx-cli-jvm:
2025-11-24T13:18:59.6984311Z total 0
2025-11-24T13:18:59.6984438Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6984604Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6984763Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 0.3.1
2025-11-24T13:18:59.6984833Z 
2025-11-24T13:18:59.6984980Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jetbrains/kotlinx/kotlinx-cli-jvm/0.3.1:
2025-11-24T13:18:59.6985124Z total 84
2025-11-24T13:18:59.6985257Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6985421Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6985595Z -rw-r--r-- 1 VssAdministrator 197121 82399 Jan  1  2010 kotlinx-cli-jvm-0.3.1.jar
2025-11-24T13:18:59.6985671Z 
2025-11-24T13:18:59.6985795Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jvnet:
2025-11-24T13:18:59.6985927Z total 4
2025-11-24T13:18:59.6986061Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6986220Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6986381Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 staxex
2025-11-24T13:18:59.6986458Z 
2025-11-24T13:18:59.6986586Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jvnet/staxex:
2025-11-24T13:18:59.6986716Z total 0
2025-11-24T13:18:59.6986850Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6987010Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6987393Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 stax-ex
2025-11-24T13:18:59.6987472Z 
2025-11-24T13:18:59.6987608Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jvnet/staxex/stax-ex:
2025-11-24T13:18:59.6987742Z total 0
2025-11-24T13:18:59.6987874Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6988035Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6988203Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.8.1
2025-11-24T13:18:59.6988274Z 
2025-11-24T13:18:59.6988410Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/jvnet/staxex/stax-ex/1.8.1:
2025-11-24T13:18:59.6988553Z total 40
2025-11-24T13:18:59.6988685Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6988849Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6989015Z -rw-r--r-- 1 VssAdministrator 197121 38099 Jan  1  2010 stax-ex-1.8.1.jar
2025-11-24T13:18:59.6989096Z 
2025-11-24T13:18:59.6989225Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/ow2:
2025-11-24T13:18:59.6989350Z total 4
2025-11-24T13:18:59.6989486Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6989651Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6989812Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 asm
2025-11-24T13:18:59.6989888Z 
2025-11-24T13:18:59.6990014Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/ow2/asm:
2025-11-24T13:18:59.6990141Z total 0
2025-11-24T13:18:59.6990273Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6990436Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6990598Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 asm
2025-11-24T13:18:59.6990766Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 asm-analysis
2025-11-24T13:18:59.6990933Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 asm-tree
2025-11-24T13:18:59.6991053Z 
2025-11-24T13:18:59.6991184Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/ow2/asm/asm:
2025-11-24T13:18:59.6991312Z total 0
2025-11-24T13:18:59.6991453Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6991613Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6991773Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 9.1
2025-11-24T13:18:59.6991843Z 
2025-11-24T13:18:59.6991980Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/ow2/asm/asm/9.1:
2025-11-24T13:18:59.6992113Z total 120
2025-11-24T13:18:59.6992248Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6992411Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6992581Z -rw-r--r-- 1 VssAdministrator 197121 121790 Jan  1  2010 asm-9.1.jar
2025-11-24T13:18:59.6992649Z 
2025-11-24T13:18:59.6992780Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/ow2/asm/asm-analysis:
2025-11-24T13:18:59.6992922Z total 0
2025-11-24T13:18:59.6993051Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6993209Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6993369Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 9.1
2025-11-24T13:18:59.6993443Z 
2025-11-24T13:18:59.6993575Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/ow2/asm/asm-analysis/9.1:
2025-11-24T13:18:59.6993709Z total 36
2025-11-24T13:18:59.6993845Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6994006Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6994169Z -rw-r--r-- 1 VssAdministrator 197121 34257 Jan  1  2010 asm-analysis-9.1.jar
2025-11-24T13:18:59.6994248Z 
2025-11-24T13:18:59.6994378Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/ow2/asm/asm-tree:
2025-11-24T13:18:59.6994509Z total 0
2025-11-24T13:18:59.6994640Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6994806Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6995176Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 9.1
2025-11-24T13:18:59.6995246Z 
2025-11-24T13:18:59.6995384Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/ow2/asm/asm-tree/9.1:
2025-11-24T13:18:59.6995515Z total 52
2025-11-24T13:18:59.6995645Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.6995807Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.6995973Z -rw-r--r-- 1 VssAdministrator 197121 52662 Jan  1  2010 asm-tree-9.1.jar
2025-11-24T13:18:59.6996043Z 
2025-11-24T13:18:59.6996167Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/smali:
2025-11-24T13:18:59.6996294Z total 4
2025-11-24T13:18:59.6996427Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6996584Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6996746Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 baksmali
2025-11-24T13:18:59.6996914Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 dexlib2
2025-11-24T13:18:59.6997083Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 util
2025-11-24T13:18:59.6997154Z 
2025-11-24T13:18:59.6997282Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/smali/baksmali:
2025-11-24T13:18:59.6997432Z total 0
2025-11-24T13:18:59.6997561Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6997720Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6997882Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.2.4
2025-11-24T13:18:59.6997960Z 
2025-11-24T13:18:59.6998093Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/smali/baksmali/2.2.4:
2025-11-24T13:18:59.6998226Z total 128
2025-11-24T13:18:59.6998364Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.6998524Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.6998688Z -rw-r--r-- 1 VssAdministrator 197121 128039 Jan  1  2010 baksmali-2.2.4.jar
2025-11-24T13:18:59.6998811Z 
2025-11-24T13:18:59.6998939Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/smali/dexlib2:
2025-11-24T13:18:59.6999067Z total 0
2025-11-24T13:18:59.6999196Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.6999357Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.6999515Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.2.4
2025-11-24T13:18:59.6999584Z 
2025-11-24T13:18:59.6999719Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/smali/dexlib2/2.2.4:
2025-11-24T13:18:59.6999853Z total 972
2025-11-24T13:18:59.6999984Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.7000143Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.7000313Z -rw-r--r-- 1 VssAdministrator 197121 993003 Jan  1  2010 dexlib2-2.2.4.jar
2025-11-24T13:18:59.7000385Z 
2025-11-24T13:18:59.7000514Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/smali/util:
2025-11-24T13:18:59.7000643Z total 0
2025-11-24T13:18:59.7000776Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.7000933Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.7001093Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.2.4
2025-11-24T13:18:59.7001168Z 
2025-11-24T13:18:59.7001297Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/org/smali/util/2.2.4:
2025-11-24T13:18:59.7001426Z total 72
2025-11-24T13:18:59.7001557Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.7001723Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.7001882Z -rw-r--r-- 1 VssAdministrator 197121 72328 Jan  1  2010 util-2.2.4.jar
2025-11-24T13:18:59.7001950Z 
2025-11-24T13:18:59.7002077Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/xerces:
2025-11-24T13:18:59.7002200Z total 4
2025-11-24T13:18:59.7002329Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.7002696Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.7002867Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xercesImpl
2025-11-24T13:18:59.7002941Z 
2025-11-24T13:18:59.7003071Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/xerces/xercesImpl:
2025-11-24T13:18:59.7003204Z total 0
2025-11-24T13:18:59.7003332Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.7003490Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.7004317Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 2.12.0
2025-11-24T13:18:59.7004481Z 
2025-11-24T13:18:59.7004631Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/xerces/xercesImpl/2.12.0:
2025-11-24T13:18:59.7004767Z total 1356
2025-11-24T13:18:59.7004901Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.7005067Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.7005242Z -rw-r--r-- 1 VssAdministrator 197121 1386397 Jan  1  2010 xercesImpl-2.12.0.jar
2025-11-24T13:18:59.7005318Z 
2025-11-24T13:18:59.7005447Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/xml-apis:
2025-11-24T13:18:59.7005572Z total 4
2025-11-24T13:18:59.7005702Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.7005860Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.7006029Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 xml-apis
2025-11-24T13:18:59.7006101Z 
2025-11-24T13:18:59.7006231Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/xml-apis/xml-apis:
2025-11-24T13:18:59.7006365Z total 0
2025-11-24T13:18:59.7006495Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.7006650Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.7006811Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 1.4.01
2025-11-24T13:18:59.7006888Z 
2025-11-24T13:18:59.7007018Z C:\Android\android-sdk/cmdline-tools/7.0/lib/external/xml-apis/xml-apis/1.4.01:
2025-11-24T13:18:59.7007236Z total 216
2025-11-24T13:18:59.7007375Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.7007535Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.7007699Z -rw-r--r-- 1 VssAdministrator 197121 220536 Jan  1  2010 xml-apis-1.4.01.jar
2025-11-24T13:18:59.7007778Z 
2025-11-24T13:18:59.7007899Z C:\Android\android-sdk/cmdline-tools/7.0/lib/layoutlib-api:
2025-11-24T13:18:59.7008022Z total 128
2025-11-24T13:18:59.7008153Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.7008320Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.7008487Z -rw-r--r-- 1 VssAdministrator 197121 119315 Jan  1  2010 tools.layoutlib-api.jar
2025-11-24T13:18:59.7008562Z 
2025-11-24T13:18:59.7008682Z C:\Android\android-sdk/cmdline-tools/7.0/lib/lint:
2025-11-24T13:18:59.7008810Z total 6248
2025-11-24T13:18:59.7008947Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.7009111Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.7009272Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 cli
2025-11-24T13:18:59.7009442Z -rw-r--r-- 1 VssAdministrator 197121  993490 Jan  1  2010 tools.lint-api.jar
2025-11-24T13:18:59.7009610Z -rw-r--r-- 1 VssAdministrator 197121 5225993 Jan  1  2010 tools.lint-checks.jar
2025-11-24T13:18:59.7009781Z -rw-r--r-- 1 VssAdministrator 197121  159890 Jan  1  2010 tools.lint-model.jar
2025-11-24T13:18:59.7009861Z 
2025-11-24T13:18:59.7009982Z C:\Android\android-sdk/cmdline-tools/7.0/lib/lint/cli:
2025-11-24T13:18:59.7010104Z total 504
2025-11-24T13:18:59.7010236Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.7010403Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.7010562Z -rw-r--r-- 1 VssAdministrator 197121 509627 Jan  1  2010 cli.jar
2025-11-24T13:18:59.7010631Z 
2025-11-24T13:18:59.7010754Z C:\Android\android-sdk/cmdline-tools/7.0/lib/misc:
2025-11-24T13:18:59.7011168Z total 8
2025-11-24T13:18:59.7011304Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.7011462Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.7011630Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 screenshot2
2025-11-24T13:18:59.7011705Z 
2025-11-24T13:18:59.7011827Z C:\Android\android-sdk/cmdline-tools/7.0/lib/misc/screenshot2:
2025-11-24T13:18:59.7011958Z total 12
2025-11-24T13:18:59.7012091Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.7012252Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.7012419Z -rw-r--r-- 1 VssAdministrator 197121 11156 Jan  1  2010 libscreenshot2lib.jar
2025-11-24T13:18:59.7012498Z 
2025-11-24T13:18:59.7012623Z C:\Android\android-sdk/cmdline-tools/7.0/lib/profgen:
2025-11-24T13:18:59.7012742Z total 8
2025-11-24T13:18:59.7012880Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 .
2025-11-24T13:18:59.7013041Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 ..
2025-11-24T13:18:59.7013204Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 profgen
2025-11-24T13:18:59.7013370Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 22:04 profgen-cli
2025-11-24T13:18:59.7013450Z 
2025-11-24T13:18:59.7013574Z C:\Android\android-sdk/cmdline-tools/7.0/lib/profgen/profgen:
2025-11-24T13:18:59.7013700Z total 144
2025-11-24T13:18:59.7013833Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.7013997Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.7014158Z -rw-r--r-- 1 VssAdministrator 197121 143465 Jan  1  2010 libprofgen.jar
2025-11-24T13:18:59.7014228Z 
2025-11-24T13:18:59.7014359Z C:\Android\android-sdk/cmdline-tools/7.0/lib/profgen/profgen-cli:
2025-11-24T13:18:59.7014485Z total 16
2025-11-24T13:18:59.7014616Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 .
2025-11-24T13:18:59.7014822Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 22:04 ..
2025-11-24T13:18:59.7015001Z -rw-r--r-- 1 VssAdministrator 197121 13013 Jan  1  2010 libprofgen-cli-lib.jar
2025-11-24T13:18:59.7015076Z 
2025-11-24T13:18:59.7015197Z C:\Android\android-sdk/cmdline-tools/7.0/lib/repository:
2025-11-24T13:18:59.7015325Z total 244
2025-11-24T13:18:59.7015460Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.7015620Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.7015789Z -rw-r--r-- 1 VssAdministrator 197121 237707 Jan  1  2010 tools.repository.jar
2025-11-24T13:18:59.7015871Z 
2025-11-24T13:18:59.7015993Z C:\Android\android-sdk/cmdline-tools/7.0/lib/sdk-common:
2025-11-24T13:18:59.7016117Z total 1468
2025-11-24T13:18:59.7016256Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 .
2025-11-24T13:18:59.7016416Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 22:04 ..
2025-11-24T13:18:59.7016582Z -rw-r--r-- 1 VssAdministrator 197121 1494965 Jan  1  2010 tools.sdk-common.jar
2025-11-24T13:18:59.7016664Z 
2025-11-24T13:18:59.7016783Z C:\Android\android-sdk/cmdline-tools/7.0/lib/sdklib:
2025-11-24T13:18:59.7016905Z total 1392
2025-11-24T13:18:59.7017038Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 .
2025-11-24T13:18:59.7017203Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 22:04 ..
2025-11-24T13:18:59.7017368Z -rw-r--r-- 1 VssAdministrator 197121  26730 Jan  1  2010 libavdmanager_lib.jar
2025-11-24T13:18:59.7017535Z -rw-r--r-- 1 VssAdministrator 197121  41249 Jan  1  2010 libsdkmanager_lib.jar
2025-11-24T13:18:59.7017700Z -rw-r--r-- 1 VssAdministrator 197121 632787 Jan  1  2010 sdklib.core.jar
2025-11-24T13:18:59.7017872Z -rw-r--r-- 1 VssAdministrator 197121 703185 Jan  1  2010 tools.sdklib.jar
2025-11-24T13:18:59.7017944Z 
2025-11-24T13:18:59.7018062Z C:\Android\android-sdk/cmdline-tools/latest:
2025-11-24T13:18:59.7018187Z total 121
2025-11-24T13:18:59.7018321Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:18:59.7018714Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.7018877Z -rw-r--r-- 1 VssAdministrator 197121 109015 Jan  1  2010 NOTICE.txt
2025-11-24T13:18:59.7019046Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 bin
2025-11-24T13:18:59.7019208Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 lib
2025-11-24T13:18:59.7019373Z -rw-r--r-- 1 VssAdministrator 197121     84 Jan  1  2010 source.properties
2025-11-24T13:18:59.7019452Z 
2025-11-24T13:18:59.7019576Z C:\Android\android-sdk/cmdline-tools/latest/bin:
2025-11-24T13:18:59.7019695Z total 32
2025-11-24T13:18:59.7019827Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 23:11 .
2025-11-24T13:18:59.7019989Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 23:11 ..
2025-11-24T13:18:59.7020159Z -rw-r--r-- 1 VssAdministrator 197121 2297 Jan  1  2010 apkanalyzer.bat
2025-11-24T13:18:59.7020324Z -rw-r--r-- 1 VssAdministrator 197121 2288 Jan  1  2010 avdmanager.bat
2025-11-24T13:18:59.7020484Z -rw-r--r-- 1 VssAdministrator 197121 2242 Jan  1  2010 lint.bat
2025-11-24T13:18:59.7020645Z -rw-r--r-- 1 VssAdministrator 197121 2222 Jan  1  2010 profgen.bat
2025-11-24T13:18:59.7020814Z -rw-r--r-- 1 VssAdministrator 197121 2222 Jan  1  2010 retrace.bat
2025-11-24T13:18:59.7020999Z -rw-r--r-- 1 VssAdministrator 197121 2285 Jan  1  2010 screenshot2.bat
2025-11-24T13:18:59.7021158Z -rw-r--r-- 1 VssAdministrator 197121 2295 Jan  1  2010 sdkmanager.bat
2025-11-24T13:18:59.7021232Z 
2025-11-24T13:18:59.7021350Z C:\Android\android-sdk/cmdline-tools/latest/lib:
2025-11-24T13:18:59.7021471Z total 8194
2025-11-24T13:18:59.7021606Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:18:59.7021775Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:18:59.7021931Z -rw-r--r-- 1 VssAdministrator 197121     202 Jan  1  2010 README
2025-11-24T13:18:59.7022099Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 analytics-library
2025-11-24T13:18:59.7022325Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 annotations
2025-11-24T13:18:59.7022503Z -rw-r--r-- 1 VssAdministrator 197121    4137 Jan  1  2010 apkanalyzer-classpath.jar
2025-11-24T13:18:59.7022676Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 apkparser
2025-11-24T13:18:59.7022847Z -rw-r--r-- 1 VssAdministrator 197121    3017 Jan  1  2010 avdmanager-classpath.jar
2025-11-24T13:18:59.7023024Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 build-system
2025-11-24T13:18:59.7023194Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 common
2025-11-24T13:18:59.7023359Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ddmlib
2025-11-24T13:18:59.7023532Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 device_validator
2025-11-24T13:18:59.7023713Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 external
2025-11-24T13:18:59.7023883Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 layoutlib-api
2025-11-24T13:18:59.7024054Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 lint
2025-11-24T13:18:59.7024221Z -rw-r--r-- 1 VssAdministrator 197121    4242 Jan  1  2010 lint-classpath.jar
2025-11-24T13:18:59.7024395Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 misc
2025-11-24T13:18:59.7024562Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 profgen
2025-11-24T13:18:59.7024730Z -rw-r--r-- 1 VssAdministrator 197121     841 Jan  1  2010 profgen-classpath.jar
2025-11-24T13:18:59.7024892Z -rw-r--r-- 1 VssAdministrator 197121 8331764 Jan  1  2010 r8.jar
2025-11-24T13:18:59.7025062Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 repository
2025-11-24T13:18:59.7025231Z -rw-r--r-- 1 VssAdministrator 197121     282 Jan  1  2010 retrace-classpath.jar
2025-11-24T13:18:59.7025404Z -rw-r--r-- 1 VssAdministrator 197121    1655 Jan  1  2010 screenshot2-classpath.jar
2025-11-24T13:18:59.7025582Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 sdk-common
2025-11-24T13:18:59.7025752Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 sdklib
2025-11-24T13:18:59.7026129Z -rw-r--r-- 1 VssAdministrator 197121    3017 Jan  1  2010 sdkmanager-classpath.jar
2025-11-24T13:18:59.7026211Z 
2025-11-24T13:18:59.7026337Z C:\Android\android-sdk/cmdline-tools/latest/lib/analytics-library:
2025-11-24T13:18:59.7026465Z total 8
2025-11-24T13:18:59.7026596Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7026760Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7026922Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 protos
2025-11-24T13:18:59.7027085Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 shared
2025-11-24T13:18:59.7027249Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 tracker
2025-11-24T13:18:59.7027327Z 
2025-11-24T13:18:59.7027458Z C:\Android\android-sdk/cmdline-tools/latest/lib/analytics-library/protos:
2025-11-24T13:18:59.7027589Z total 0
2025-11-24T13:18:59.7027716Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7027883Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7028044Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 src
2025-11-24T13:18:59.7028114Z 
2025-11-24T13:18:59.7028249Z C:\Android\android-sdk/cmdline-tools/latest/lib/analytics-library/protos/src:
2025-11-24T13:18:59.7028381Z total 0
2025-11-24T13:18:59.7028509Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7028666Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7028831Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 main
2025-11-24T13:18:59.7028902Z 
2025-11-24T13:18:59.7029036Z C:\Android\android-sdk/cmdline-tools/latest/lib/analytics-library/protos/src/main:
2025-11-24T13:18:59.7029174Z total 0
2025-11-24T13:18:59.7029301Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7029457Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7029864Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 proto
2025-11-24T13:18:59.7029945Z 
2025-11-24T13:18:59.7030083Z C:\Android\android-sdk/cmdline-tools/latest/lib/analytics-library/protos/src/main/proto:
2025-11-24T13:18:59.7030226Z total 5616
2025-11-24T13:18:59.7030365Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:18:59.7030528Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:18:59.7030688Z -rw-r--r-- 1 VssAdministrator 197121 5747656 Jan  1  2010 proto.jar
2025-11-24T13:18:59.7030762Z 
2025-11-24T13:18:59.7030891Z C:\Android\android-sdk/cmdline-tools/latest/lib/analytics-library/shared:
2025-11-24T13:18:59.7031023Z total 116
2025-11-24T13:18:59.7031156Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:18:59.7031321Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.7031489Z -rw-r--r-- 1 VssAdministrator 197121 115430 Jan  1  2010 tools.analytics-shared.jar
2025-11-24T13:18:59.7031888Z 
2025-11-24T13:18:59.7032166Z C:\Android\android-sdk/cmdline-tools/latest/lib/analytics-library/tracker:
2025-11-24T13:18:59.7032491Z total 40
2025-11-24T13:18:59.7032752Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:18:59.7033067Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:18:59.7033409Z -rw-r--r-- 1 VssAdministrator 197121 40452 Jan  1  2010 tools.analytics-tracker.jar
2025-11-24T13:18:59.7033571Z 
2025-11-24T13:18:59.7033818Z C:\Android\android-sdk/cmdline-tools/latest/lib/annotations:
2025-11-24T13:18:59.7034058Z total 20
2025-11-24T13:18:59.7034896Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:18:59.7035237Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:18:59.7035567Z -rw-r--r-- 1 VssAdministrator 197121 10561 Jan  1  2010 annotations.jar
2025-11-24T13:18:59.7035718Z 
2025-11-24T13:18:59.7035967Z C:\Android\android-sdk/cmdline-tools/latest/lib/apkparser:
2025-11-24T13:18:59.7036225Z total 92
2025-11-24T13:18:59.7036486Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:18:59.7037334Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:18:59.7037671Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 analyzer
2025-11-24T13:18:59.7037991Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 cli
2025-11-24T13:18:59.7038334Z -rw-r--r-- 1 VssAdministrator 197121 84199 Jan  1  2010 tools.binary-resources.jar
2025-11-24T13:18:59.7038500Z 
2025-11-24T13:18:59.7038754Z C:\Android\android-sdk/cmdline-tools/latest/lib/apkparser/analyzer:
2025-11-24T13:18:59.7039003Z total 108
2025-11-24T13:18:59.7039277Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:18:59.7039594Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.7039915Z -rw-r--r-- 1 VssAdministrator 197121 106580 Jan  1  2010 analyzer.jar
2025-11-24T13:18:59.7040062Z 
2025-11-24T13:18:59.7040307Z C:\Android\android-sdk/cmdline-tools/latest/lib/apkparser/cli:
2025-11-24T13:18:59.7040570Z total 60
2025-11-24T13:18:59.7040831Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:18:59.7041163Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:18:59.7041491Z -rw-r--r-- 1 VssAdministrator 197121 59445 Jan  1  2010 analyzer-cli.jar
2025-11-24T13:18:59.7041635Z 
2025-11-24T13:18:59.7041880Z C:\Android\android-sdk/cmdline-tools/latest/lib/build-system:
2025-11-24T13:18:59.7042119Z total 228
2025-11-24T13:18:59.7042379Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:18:59.7042703Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.7043042Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 builder-model
2025-11-24T13:18:59.7043398Z -rw-r--r-- 1 VssAdministrator 197121 223266 Jan  1  2010 tools.manifest-merger.jar
2025-11-24T13:18:59.7043553Z 
2025-11-24T13:18:59.7051279Z C:\Android\android-sdk/cmdline-tools/latest/lib/build-system/builder-model:
2025-11-24T13:18:59.7051710Z total 112
2025-11-24T13:18:59.7051917Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:18:59.7052105Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.7052277Z -rw-r--r-- 1 VssAdministrator 197121 114024 Jan  1  2010 builder-model.jar
2025-11-24T13:18:59.7052359Z 
2025-11-24T13:18:59.7052490Z C:\Android\android-sdk/cmdline-tools/latest/lib/common:
2025-11-24T13:18:59.7052803Z total 388
2025-11-24T13:18:59.7052945Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:18:59.7053120Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.7053290Z -rw-r--r-- 1 VssAdministrator 197121 387161 Jan  1  2010 tools.common.jar
2025-11-24T13:18:59.7053364Z 
2025-11-24T13:18:59.7053493Z C:\Android\android-sdk/cmdline-tools/latest/lib/ddmlib:
2025-11-24T13:18:59.7053620Z total 588
2025-11-24T13:18:59.7053758Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:18:59.7053928Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.7054102Z -rw-r--r-- 1 VssAdministrator 197121 593553 Jan  1  2010 tools.ddmlib.jar
2025-11-24T13:18:59.7054175Z 
2025-11-24T13:18:59.7054306Z C:\Android\android-sdk/cmdline-tools/latest/lib/device_validator:
2025-11-24T13:18:59.7054445Z total 56
2025-11-24T13:18:59.7054582Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:18:59.7054747Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:18:59.7054911Z -rw-r--r-- 1 VssAdministrator 197121 47266 Jan  1  2010 tools.dvlib.jar
2025-11-24T13:18:59.7054987Z 
2025-11-24T13:18:59.7055110Z C:\Android\android-sdk/cmdline-tools/latest/lib/external:
2025-11-24T13:18:59.7055235Z total 16
2025-11-24T13:18:59.7055374Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7055543Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7055714Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 archive-patcher
2025-11-24T13:18:59.7056310Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 com
2025-11-24T13:18:59.7056491Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 commons-codec
2025-11-24T13:18:59.7056982Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 commons-io
2025-11-24T13:18:59.7057162Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 commons-logging
2025-11-24T13:18:59.7057336Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jakarta
2025-11-24T13:18:59.7057507Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 javax
2025-11-24T13:18:59.7057673Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 lint-psi
2025-11-24T13:18:59.7057838Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 net
2025-11-24T13:18:59.7058000Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 org
2025-11-24T13:18:59.7058171Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 xerces
2025-11-24T13:18:59.7058338Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 xml-apis
2025-11-24T13:18:59.7058416Z 
2025-11-24T13:18:59.7058556Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/archive-patcher:
2025-11-24T13:18:59.7058691Z total 128
2025-11-24T13:18:59.7058826Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:18:59.7058988Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:18:59.7059154Z -rw-r--r-- 1 VssAdministrator 197121 12156 Jan  1  2010 explainer.jar
2025-11-24T13:18:59.7059314Z -rw-r--r-- 1 VssAdministrator 197121 84159 Jan  1  2010 generator.jar
2025-11-24T13:18:59.7059473Z -rw-r--r-- 1 VssAdministrator 197121 28234 Jan  1  2010 shared.jar
2025-11-24T13:18:59.7059545Z 
2025-11-24T13:18:59.7059668Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com:
2025-11-24T13:18:59.7059792Z total 8
2025-11-24T13:18:59.7059924Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7060092Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7060325Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 android
2025-11-24T13:18:59.7060495Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 beust
2025-11-24T13:18:59.7060660Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 google
2025-11-24T13:18:59.7060830Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 sun
2025-11-24T13:18:59.7060902Z 
2025-11-24T13:18:59.7061033Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/android:
2025-11-24T13:18:59.7061162Z total 0
2025-11-24T13:18:59.7061300Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7061463Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7061627Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 tools
2025-11-24T13:18:59.7061706Z 
2025-11-24T13:18:59.7061847Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/android/tools:
2025-11-24T13:18:59.7061983Z total 0
2025-11-24T13:18:59.7062116Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7062286Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7062458Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 build
2025-11-24T13:18:59.7062532Z 
2025-11-24T13:18:59.7062674Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/android/tools/build:
2025-11-24T13:18:59.7062813Z total 0
2025-11-24T13:18:59.7062950Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7063113Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7063288Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 aapt2-proto
2025-11-24T13:18:59.7063367Z 
2025-11-24T13:18:59.7063509Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/android/tools/build/aapt2-proto:
2025-11-24T13:18:59.7063665Z total 0
2025-11-24T13:18:59.7063796Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7063961Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7064140Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 7.0.0-beta04-7396180
2025-11-24T13:18:59.7064504Z 
2025-11-24T13:18:59.7064674Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/android/tools/build/aapt2-proto/7.0.0-beta04-7396180:
2025-11-24T13:18:59.7080786Z total 732
2025-11-24T13:18:59.7081055Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:18:59.7081339Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.7081653Z -rw-r--r-- 1 VssAdministrator 197121 747666 Jan  1  2010 aapt2-proto-7.0.0-beta04-7396180.jar
2025-11-24T13:18:59.7081795Z 
2025-11-24T13:18:59.7082017Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/beust:
2025-11-24T13:18:59.7082244Z total 0
2025-11-24T13:18:59.7082482Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7082764Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7083034Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jcommander
2025-11-24T13:18:59.7083130Z 
2025-11-24T13:18:59.7083271Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/beust/jcommander:
2025-11-24T13:18:59.7083417Z total 0
2025-11-24T13:18:59.7083560Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7083724Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7083892Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.78
2025-11-24T13:18:59.7083970Z 
2025-11-24T13:18:59.7084108Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/beust/jcommander/1.78:
2025-11-24T13:18:59.7084247Z total 84
2025-11-24T13:18:59.7084382Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:18:59.7084556Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:18:59.7084727Z -rw-r--r-- 1 VssAdministrator 197121 83782 Jan  1  2010 jcommander-1.78.jar
2025-11-24T13:18:59.7084803Z 
2025-11-24T13:18:59.7084943Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google:
2025-11-24T13:18:59.7085196Z total 4
2025-11-24T13:18:59.7085334Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7085499Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7085670Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 code
2025-11-24T13:18:59.7085840Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 errorprone
2025-11-24T13:18:59.7086012Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 guava
2025-11-24T13:18:59.7086180Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 j2objc
2025-11-24T13:18:59.7086352Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jimfs
2025-11-24T13:18:59.7086522Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 protobuf
2025-11-24T13:18:59.7086597Z 
2025-11-24T13:18:59.7086730Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/code:
2025-11-24T13:18:59.7086871Z total 4
2025-11-24T13:18:59.7087005Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7087169Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7087343Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 findbugs
2025-11-24T13:18:59.7087516Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 gson
2025-11-24T13:18:59.7087589Z 
2025-11-24T13:18:59.7087727Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/code/findbugs:
2025-11-24T13:18:59.7087871Z total 0
2025-11-24T13:18:59.7088003Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7088164Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7088656Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jsr305
2025-11-24T13:18:59.7088826Z 
2025-11-24T13:18:59.7089121Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/code/findbugs/jsr305:
2025-11-24T13:18:59.7089400Z total 0
2025-11-24T13:18:59.7089662Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7089986Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7090331Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 3.0.2
2025-11-24T13:18:59.7090992Z 
2025-11-24T13:18:59.7091304Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/code/findbugs/jsr305/3.0.2:
2025-11-24T13:18:59.7091592Z total 20
2025-11-24T13:18:59.7091860Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:18:59.7092210Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:18:59.7092553Z -rw-r--r-- 1 VssAdministrator 197121 19936 Jan  1  2010 jsr305-3.0.2.jar
2025-11-24T13:18:59.7092699Z 
2025-11-24T13:18:59.7092980Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/code/gson:
2025-11-24T13:18:59.7093249Z total 0
2025-11-24T13:18:59.7093511Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7093843Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7094183Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 gson
2025-11-24T13:18:59.7094326Z 
2025-11-24T13:18:59.7094603Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/code/gson/gson:
2025-11-24T13:18:59.7094888Z total 0
2025-11-24T13:18:59.7095150Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7095468Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7095798Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.8.6
2025-11-24T13:18:59.7095949Z 
2025-11-24T13:18:59.7096217Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/code/gson/gson/2.8.6:
2025-11-24T13:18:59.7096508Z total 236
2025-11-24T13:18:59.7096780Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:18:59.7097128Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:18:59.7097459Z -rw-r--r-- 1 VssAdministrator 197121 240255 Jan  1  2010 gson-2.8.6.jar
2025-11-24T13:18:59.7097602Z 
2025-11-24T13:18:59.7097879Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/errorprone:
2025-11-24T13:18:59.7098271Z total 4
2025-11-24T13:18:59.7098531Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7098854Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7099216Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 error_prone_annotations
2025-11-24T13:18:59.7099382Z 
2025-11-24T13:18:59.7099677Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/errorprone/error_prone_annotations:
2025-11-24T13:18:59.7099985Z total 0
2025-11-24T13:18:59.7100264Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:18:59.7100593Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:18:59.7100933Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.4.0
2025-11-24T13:18:59.7101086Z 
2025-11-24T13:18:59.7101393Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/errorprone/error_prone_annotations/2.4.0:
2025-11-24T13:18:59.7101718Z total 16
2025-11-24T13:18:59.7101993Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0094970Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0101457Z -rw-r--r-- 1 VssAdministrator 197121 13854 Jan  1  2010 error_prone_annotations-2.4.0.jar
2025-11-24T13:19:00.0123321Z 
2025-11-24T13:19:00.0128962Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/guava:
2025-11-24T13:19:00.0141198Z total 4
2025-11-24T13:19:00.0159844Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0174100Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0179989Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 failureaccess
2025-11-24T13:19:00.0182244Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 guava
2025-11-24T13:19:00.0182775Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 listenablefuture
2025-11-24T13:19:00.0183053Z 
2025-11-24T13:19:00.0183450Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/guava/failureaccess:
2025-11-24T13:19:00.0183996Z total 0
2025-11-24T13:19:00.0186135Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0186600Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0187028Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.0.1
2025-11-24T13:19:00.0187273Z 
2025-11-24T13:19:00.0187645Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/guava/failureaccess/1.0.1:
2025-11-24T13:19:00.0188027Z total 8
2025-11-24T13:19:00.0188393Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 23:11 .
2025-11-24T13:19:00.0188804Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 23:11 ..
2025-11-24T13:19:00.0189227Z -rw-r--r-- 1 VssAdministrator 197121 4617 Jan  1  2010 failureaccess-1.0.1.jar
2025-11-24T13:19:00.0189485Z 
2025-11-24T13:19:00.0189840Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/guava/guava:
2025-11-24T13:19:00.0190184Z total 0
2025-11-24T13:19:00.0190539Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0190958Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0191368Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 30.1-jre
2025-11-24T13:19:00.0191621Z 
2025-11-24T13:19:00.0192148Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/guava/guava/30.1-jre:
2025-11-24T13:19:00.0192511Z total 2796
2025-11-24T13:19:00.0192762Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0193138Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0193462Z -rw-r--r-- 1 VssAdministrator 197121 2862361 Jan  1  2010 guava-30.1-jre.jar
2025-11-24T13:19:00.0193619Z 
2025-11-24T13:19:00.0193903Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/guava/listenablefuture:
2025-11-24T13:19:00.0194185Z total 0
2025-11-24T13:19:00.0194809Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0195115Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0195624Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 9999.0-empty-to-avoid-conflict-with-guava
2025-11-24T13:19:00.0195809Z 
2025-11-24T13:19:00.0196111Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava:
2025-11-24T13:19:00.0196411Z total 4
2025-11-24T13:19:00.0196651Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 23:11 .
2025-11-24T13:19:00.0196956Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 23:11 ..
2025-11-24T13:19:00.0197306Z -rw-r--r-- 1 VssAdministrator 197121 2199 Jan  1  2010 listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
2025-11-24T13:19:00.0197484Z 
2025-11-24T13:19:00.0197712Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/j2objc:
2025-11-24T13:19:00.0197940Z total 4
2025-11-24T13:19:00.0198169Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0198452Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0198809Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 j2objc-annotations
2025-11-24T13:19:00.0198957Z 
2025-11-24T13:19:00.0199226Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/j2objc/j2objc-annotations:
2025-11-24T13:19:00.0199509Z total 0
2025-11-24T13:19:00.0199749Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0200050Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0200329Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.3
2025-11-24T13:19:00.0200469Z 
2025-11-24T13:19:00.0200738Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/j2objc/j2objc-annotations/1.3:
2025-11-24T13:19:00.0201000Z total 12
2025-11-24T13:19:00.0201260Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 23:11 .
2025-11-24T13:19:00.0201590Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 23:11 ..
2025-11-24T13:19:00.0201909Z -rw-r--r-- 1 VssAdministrator 197121 8781 Jan  1  2010 j2objc-annotations-1.3.jar
2025-11-24T13:19:00.0203576Z 
2025-11-24T13:19:00.0203893Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/jimfs:
2025-11-24T13:19:00.0204167Z total 4
2025-11-24T13:19:00.0204416Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0204724Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0205070Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jimfs
2025-11-24T13:19:00.0205220Z 
2025-11-24T13:19:00.0205482Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/jimfs/jimfs:
2025-11-24T13:19:00.0205749Z total 0
2025-11-24T13:19:00.0206434Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0206748Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0207073Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.1
2025-11-24T13:19:00.0207223Z 
2025-11-24T13:19:00.0207485Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/jimfs/jimfs/1.1:
2025-11-24T13:19:00.0207731Z total 204
2025-11-24T13:19:00.0207975Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0208262Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0208580Z -rw-r--r-- 1 VssAdministrator 197121 206691 Jan  1  2010 jimfs-1.1.jar
2025-11-24T13:19:00.0208722Z 
2025-11-24T13:19:00.0208973Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/protobuf:
2025-11-24T13:19:00.0209239Z total 4
2025-11-24T13:19:00.0209477Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0209801Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0210138Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 protobuf-java
2025-11-24T13:19:00.0210291Z 
2025-11-24T13:19:00.0210553Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/protobuf/protobuf-java:
2025-11-24T13:19:00.0210828Z total 0
2025-11-24T13:19:00.0211085Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0211564Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0211883Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 3.17.2
2025-11-24T13:19:00.0212041Z 
2025-11-24T13:19:00.0212647Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/google/protobuf/protobuf-java/3.17.2:
2025-11-24T13:19:00.0212943Z total 1640
2025-11-24T13:19:00.0213228Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0213791Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0214347Z -rw-r--r-- 1 VssAdministrator 197121 1676023 Jan  1  2010 protobuf-java-3.17.2.jar
2025-11-24T13:19:00.0214511Z 
2025-11-24T13:19:00.0214756Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun:
2025-11-24T13:19:00.0215001Z total 0
2025-11-24T13:19:00.0215245Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0215543Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0215844Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 activation
2025-11-24T13:19:00.0216128Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 istack
2025-11-24T13:19:00.0216402Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 xml
2025-11-24T13:19:00.0216532Z 
2025-11-24T13:19:00.0216764Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun/activation:
2025-11-24T13:19:00.0216994Z total 0
2025-11-24T13:19:00.0217226Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0217495Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0217794Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 javax.activation
2025-11-24T13:19:00.0217931Z 
2025-11-24T13:19:00.0218170Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun/activation/javax.activation:
2025-11-24T13:19:00.0218413Z total 0
2025-11-24T13:19:00.0218632Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0218912Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0219315Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.2.0
2025-11-24T13:19:00.0219450Z 
2025-11-24T13:19:00.0219689Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun/activation/javax.activation/1.2.0:
2025-11-24T13:19:00.0219949Z total 80
2025-11-24T13:19:00.0220171Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0220450Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0220740Z -rw-r--r-- 1 VssAdministrator 197121 78030 Jan  1  2010 javax.activation-1.2.0.jar
2025-11-24T13:19:00.0220876Z 
2025-11-24T13:19:00.0221096Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun/istack:
2025-11-24T13:19:00.0221310Z total 0
2025-11-24T13:19:00.0221534Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0221808Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0222105Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 istack-commons-runtime
2025-11-24T13:19:00.0222256Z 
2025-11-24T13:19:00.0222499Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun/istack/istack-commons-runtime:
2025-11-24T13:19:00.0222746Z total 0
2025-11-24T13:19:00.0222965Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0223249Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0223522Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 3.0.8
2025-11-24T13:19:00.0223643Z 
2025-11-24T13:19:00.0223890Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun/istack/istack-commons-runtime/3.0.8:
2025-11-24T13:19:00.0224133Z total 28
2025-11-24T13:19:00.0224361Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0224634Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0224933Z -rw-r--r-- 1 VssAdministrator 197121 27156 Jan  1  2010 istack-commons-runtime-3.0.8.jar
2025-11-24T13:19:00.0225153Z 
2025-11-24T13:19:00.0225370Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun/xml:
2025-11-24T13:19:00.0225607Z total 0
2025-11-24T13:19:00.0225831Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0226105Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0226393Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 fastinfoset
2025-11-24T13:19:00.0226533Z 
2025-11-24T13:19:00.0226753Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun/xml/fastinfoset:
2025-11-24T13:19:00.0226984Z total 0
2025-11-24T13:19:00.0227207Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0227480Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0227767Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 FastInfoset
2025-11-24T13:19:00.0227907Z 
2025-11-24T13:19:00.0228142Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun/xml/fastinfoset/FastInfoset:
2025-11-24T13:19:00.0228381Z total 0
2025-11-24T13:19:00.0228604Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0228877Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0229161Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.2.16
2025-11-24T13:19:00.0229288Z 
2025-11-24T13:19:00.0229531Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/com/sun/xml/fastinfoset/FastInfoset/1.2.16:
2025-11-24T13:19:00.0229781Z total 312
2025-11-24T13:19:00.0230028Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0230317Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0230608Z -rw-r--r-- 1 VssAdministrator 197121 317195 Jan  1  2010 FastInfoset-1.2.16.jar
2025-11-24T13:19:00.0230752Z 
2025-11-24T13:19:00.0230975Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/commons-codec:
2025-11-24T13:19:00.0231197Z total 4
2025-11-24T13:19:00.0231438Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0231747Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0232159Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 commons-codec
2025-11-24T13:19:00.0232301Z 
2025-11-24T13:19:00.0232555Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/commons-codec/commons-codec:
2025-11-24T13:19:00.0232801Z total 0
2025-11-24T13:19:00.0233036Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0233351Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0233648Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.11
2025-11-24T13:19:00.0233777Z 
2025-11-24T13:19:00.0234006Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/commons-codec/commons-codec/1.11:
2025-11-24T13:19:00.0234228Z total 328
2025-11-24T13:19:00.0234458Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0234736Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0235037Z -rw-r--r-- 1 VssAdministrator 197121 335042 Jan  1  2010 commons-codec-1.11.jar
2025-11-24T13:19:00.0235176Z 
2025-11-24T13:19:00.0235403Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/commons-io:
2025-11-24T13:19:00.0235626Z total 4
2025-11-24T13:19:00.0236309Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0237993Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0238507Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 commons-io
2025-11-24T13:19:00.0238665Z 
2025-11-24T13:19:00.0238918Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/commons-io/commons-io:
2025-11-24T13:19:00.0239170Z total 0
2025-11-24T13:19:00.0239420Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0239944Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0240229Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.4
2025-11-24T13:19:00.0240351Z 
2025-11-24T13:19:00.0240579Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/commons-io/commons-io/2.4:
2025-11-24T13:19:00.0240937Z total 184
2025-11-24T13:19:00.0241149Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0241416Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0241694Z -rw-r--r-- 1 VssAdministrator 197121 185140 Jan  1  2010 commons-io-2.4.jar
2025-11-24T13:19:00.0241815Z 
2025-11-24T13:19:00.0242031Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/commons-logging:
2025-11-24T13:19:00.0242259Z total 4
2025-11-24T13:19:00.0242473Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0242756Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0243073Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 commons-logging
2025-11-24T13:19:00.0243215Z 
2025-11-24T13:19:00.0243443Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/commons-logging/commons-logging:
2025-11-24T13:19:00.0243679Z total 0
2025-11-24T13:19:00.0243922Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0244210Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0244504Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.2
2025-11-24T13:19:00.0244642Z 
2025-11-24T13:19:00.0244896Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/commons-logging/commons-logging/1.2:
2025-11-24T13:19:00.0245123Z total 64
2025-11-24T13:19:00.0245338Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0245624Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0245932Z -rw-r--r-- 1 VssAdministrator 197121 61829 Jan  1  2010 commons-logging-1.2.jar
2025-11-24T13:19:00.0246075Z 
2025-11-24T13:19:00.0246297Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/jakarta:
2025-11-24T13:19:00.0246518Z total 4
2025-11-24T13:19:00.0246752Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0247017Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0247409Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 activation
2025-11-24T13:19:00.0247703Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 xml
2025-11-24T13:19:00.0247820Z 
2025-11-24T13:19:00.0248047Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/jakarta/activation:
2025-11-24T13:19:00.0248274Z total 0
2025-11-24T13:19:00.0248483Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0248754Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0249049Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jakarta.activation-api
2025-11-24T13:19:00.0249199Z 
2025-11-24T13:19:00.0249443Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/jakarta/activation/jakarta.activation-api:
2025-11-24T13:19:00.0249684Z total 0
2025-11-24T13:19:00.0249917Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0250186Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0250452Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.2.1
2025-11-24T13:19:00.0250586Z 
2025-11-24T13:19:00.0250861Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/jakarta/activation/jakarta.activation-api/1.2.1:
2025-11-24T13:19:00.0251127Z total 44
2025-11-24T13:19:00.0251359Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0251654Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0251957Z -rw-r--r-- 1 VssAdministrator 197121 44399 Jan  1  2010 jakarta.activation-api-1.2.1.jar
2025-11-24T13:19:00.0252099Z 
2025-11-24T13:19:00.0252336Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/jakarta/xml:
2025-11-24T13:19:00.0252562Z total 0
2025-11-24T13:19:00.0252793Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0253079Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0253374Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 bind
2025-11-24T13:19:00.0253605Z 
2025-11-24T13:19:00.0253851Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/jakarta/xml/bind:
2025-11-24T13:19:00.0254083Z total 0
2025-11-24T13:19:00.0254312Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0254662Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0254963Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jakarta.xml.bind-api
2025-11-24T13:19:00.0255111Z 
2025-11-24T13:19:00.0255514Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/jakarta/xml/bind/jakarta.xml.bind-api:
2025-11-24T13:19:00.0255777Z total 0
2025-11-24T13:19:00.0256271Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0256601Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0257242Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.3.2
2025-11-24T13:19:00.0257543Z 
2025-11-24T13:19:00.0258096Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/jakarta/xml/bind/jakarta.xml.bind-api/2.3.2:
2025-11-24T13:19:00.0258403Z total 116
2025-11-24T13:19:00.0258876Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0259228Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0259539Z -rw-r--r-- 1 VssAdministrator 197121 115498 Jan  1  2010 jakarta.xml.bind-api-2.3.2.jar
2025-11-24T13:19:00.0259681Z 
2025-11-24T13:19:00.0259910Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/javax:
2025-11-24T13:19:00.0260151Z total 4
2025-11-24T13:19:00.0260388Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0260690Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0260998Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 inject
2025-11-24T13:19:00.0261145Z 
2025-11-24T13:19:00.0261386Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/javax/inject:
2025-11-24T13:19:00.0261632Z total 0
2025-11-24T13:19:00.0261883Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0262322Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0262638Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 javax.inject
2025-11-24T13:19:00.0262789Z 
2025-11-24T13:19:00.0263029Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/javax/inject/javax.inject:
2025-11-24T13:19:00.0263272Z total 0
2025-11-24T13:19:00.0263524Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0263851Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0264163Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1
2025-11-24T13:19:00.0264298Z 
2025-11-24T13:19:00.0264710Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/javax/inject/javax.inject/1:
2025-11-24T13:19:00.0265534Z total 4
2025-11-24T13:19:00.0266116Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 23:11 .
2025-11-24T13:19:00.0266426Z drwxr-xr-x 1 VssAdministrator 197121    0 Nov  2 23:11 ..
2025-11-24T13:19:00.0266890Z -rw-r--r-- 1 VssAdministrator 197121 2497 Jan  1  2010 javax.inject-1.jar
2025-11-24T13:19:00.0267151Z 
2025-11-24T13:19:00.0268393Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/lint-psi:
2025-11-24T13:19:00.0268689Z total 4
2025-11-24T13:19:00.0268943Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0269249Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0269553Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 intellij-core
2025-11-24T13:19:00.0269859Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kotlin-compiler
2025-11-24T13:19:00.0270166Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 uast
2025-11-24T13:19:00.0270300Z 
2025-11-24T13:19:00.0270547Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/lint-psi/intellij-core:
2025-11-24T13:19:00.0270801Z total 21052
2025-11-24T13:19:00.0271040Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 23:11 .
2025-11-24T13:19:00.0271338Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 23:11 ..
2025-11-24T13:19:00.0271740Z -rw-r--r-- 1 VssAdministrator 197121 21555552 Jan  1  2010 intellij-core-mvn.jar
2025-11-24T13:19:00.0271873Z 
2025-11-24T13:19:00.0272104Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/lint-psi/kotlin-compiler:
2025-11-24T13:19:00.0272342Z total 39404
2025-11-24T13:19:00.0272597Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 23:11 .
2025-11-24T13:19:00.0272899Z drwxr-xr-x 1 VssAdministrator 197121        0 Nov  2 23:11 ..
2025-11-24T13:19:00.0273215Z -rw-r--r-- 1 VssAdministrator 197121 40346136 Jan  1  2010 kotlin-compiler-mvn.jar
2025-11-24T13:19:00.0273367Z 
2025-11-24T13:19:00.0273590Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/lint-psi/uast:
2025-11-24T13:19:00.0273813Z total 2440
2025-11-24T13:19:00.0274042Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0274350Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0274652Z -rw-r--r-- 1 VssAdministrator 197121 2494893 Jan  1  2010 uast.jar
2025-11-24T13:19:00.0274779Z 
2025-11-24T13:19:00.0275009Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net:
2025-11-24T13:19:00.0275236Z total 4
2025-11-24T13:19:00.0275463Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0275763Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0276062Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 java
2025-11-24T13:19:00.0276360Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 sf
2025-11-24T13:19:00.0276495Z 
2025-11-24T13:19:00.0276719Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/java:
2025-11-24T13:19:00.0276984Z total 0
2025-11-24T13:19:00.0277230Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0277521Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0277804Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 dev
2025-11-24T13:19:00.0277928Z 
2025-11-24T13:19:00.0278143Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/java/dev:
2025-11-24T13:19:00.0278452Z total 0
2025-11-24T13:19:00.0278690Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0278989Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0279287Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jna
2025-11-24T13:19:00.0279418Z 
2025-11-24T13:19:00.0279655Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/java/dev/jna:
2025-11-24T13:19:00.0279899Z total 0
2025-11-24T13:19:00.0280113Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0280378Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0280652Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jna
2025-11-24T13:19:00.0280972Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jna-platform
2025-11-24T13:19:00.0281113Z 
2025-11-24T13:19:00.0281358Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/java/dev/jna/jna:
2025-11-24T13:19:00.0281613Z total 0
2025-11-24T13:19:00.0281853Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0282146Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0282432Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 5.6.0
2025-11-24T13:19:00.0282561Z 
2025-11-24T13:19:00.0282783Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/java/dev/jna/jna/5.6.0:
2025-11-24T13:19:00.0283012Z total 1476
2025-11-24T13:19:00.0283255Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0283554Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0283853Z -rw-r--r-- 1 VssAdministrator 197121 1509440 Jan  1  2010 jna-5.6.0.jar
2025-11-24T13:19:00.0283992Z 
2025-11-24T13:19:00.0284244Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/java/dev/jna/jna-platform:
2025-11-24T13:19:00.0284494Z total 0
2025-11-24T13:19:00.0284731Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0285109Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0285393Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 5.6.0
2025-11-24T13:19:00.0285526Z 
2025-11-24T13:19:00.0285785Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/java/dev/jna/jna-platform/5.6.0:
2025-11-24T13:19:00.0286028Z total 2672
2025-11-24T13:19:00.0286251Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0286542Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0286859Z -rw-r--r-- 1 VssAdministrator 197121 2735878 Jan  1  2010 jna-platform-5.6.0.jar
2025-11-24T13:19:00.0287003Z 
2025-11-24T13:19:00.0287231Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/sf:
2025-11-24T13:19:00.0287460Z total 0
2025-11-24T13:19:00.0287705Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0287979Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0288258Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jopt-simple
2025-11-24T13:19:00.0288560Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kxml
2025-11-24T13:19:00.0288701Z 
2025-11-24T13:19:00.0288942Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/sf/jopt-simple:
2025-11-24T13:19:00.0289183Z total 0
2025-11-24T13:19:00.0289427Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0289722Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0290016Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jopt-simple
2025-11-24T13:19:00.0290168Z 
2025-11-24T13:19:00.0290407Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/sf/jopt-simple/jopt-simple:
2025-11-24T13:19:00.0290662Z total 0
2025-11-24T13:19:00.0290894Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0291179Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0291475Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 4.9
2025-11-24T13:19:00.0291669Z 
2025-11-24T13:19:00.0291910Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/sf/jopt-simple/jopt-simple/4.9:
2025-11-24T13:19:00.0292152Z total 68
2025-11-24T13:19:00.0292393Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0292694Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0293007Z -rw-r--r-- 1 VssAdministrator 197121 66469 Jan  1  2010 jopt-simple-4.9.jar
2025-11-24T13:19:00.0293144Z 
2025-11-24T13:19:00.0293379Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/sf/kxml:
2025-11-24T13:19:00.0293602Z total 0
2025-11-24T13:19:00.0293840Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0294130Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0294431Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kxml2
2025-11-24T13:19:00.0294557Z 
2025-11-24T13:19:00.0294795Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/sf/kxml/kxml2:
2025-11-24T13:19:00.0295031Z total 0
2025-11-24T13:19:00.0295244Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0295521Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0295815Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.3.0
2025-11-24T13:19:00.0295948Z 
2025-11-24T13:19:00.0296200Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/net/sf/kxml/kxml2/2.3.0:
2025-11-24T13:19:00.0296449Z total 44
2025-11-24T13:19:00.0296688Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0296986Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0297290Z -rw-r--r-- 1 VssAdministrator 197121 43858 Jan  1  2010 kxml2-2.3.0.jar
2025-11-24T13:19:00.0297415Z 
2025-11-24T13:19:00.0297643Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org:
2025-11-24T13:19:00.0297872Z total 8
2025-11-24T13:19:00.0298097Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0298443Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0298718Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 apache
2025-11-24T13:19:00.0299019Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 bouncycastle
2025-11-24T13:19:00.0299333Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 checkerframework
2025-11-24T13:19:00.0299645Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 glassfish
2025-11-24T13:19:00.0299955Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jetbrains
2025-11-24T13:19:00.0300267Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jvnet
2025-11-24T13:19:00.0300571Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ow2
2025-11-24T13:19:00.0300863Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 smali
2025-11-24T13:19:00.0301002Z 
2025-11-24T13:19:00.0301235Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache:
2025-11-24T13:19:00.0301470Z total 4
2025-11-24T13:19:00.0301707Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0302008Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0302298Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 commons
2025-11-24T13:19:00.0302609Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 httpcomponents
2025-11-24T13:19:00.0302764Z 
2025-11-24T13:19:00.0302999Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache/commons:
2025-11-24T13:19:00.0303233Z total 0
2025-11-24T13:19:00.0303472Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0303770Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0304080Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 commons-compress
2025-11-24T13:19:00.0304226Z 
2025-11-24T13:19:00.0304498Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache/commons/commons-compress:
2025-11-24T13:19:00.0304769Z total 0
2025-11-24T13:19:00.0305007Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0305374Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0305667Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.20
2025-11-24T13:19:00.0305804Z 
2025-11-24T13:19:00.0306058Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache/commons/commons-compress/1.20:
2025-11-24T13:19:00.0306316Z total 620
2025-11-24T13:19:00.0306547Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0306830Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0307121Z -rw-r--r-- 1 VssAdministrator 197121 632424 Jan  1  2010 commons-compress-1.20.jar
2025-11-24T13:19:00.0307265Z 
2025-11-24T13:19:00.0307505Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache/httpcomponents:
2025-11-24T13:19:00.0307727Z total 0
2025-11-24T13:19:00.0307869Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0308039Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0308213Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 httpclient
2025-11-24T13:19:00.0308382Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 httpcore
2025-11-24T13:19:00.0308555Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 httpmime
2025-11-24T13:19:00.0308628Z 
2025-11-24T13:19:00.0308769Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache/httpcomponents/httpclient:
2025-11-24T13:19:00.0308919Z total 0
2025-11-24T13:19:00.0309050Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0309211Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0309377Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 4.5.13
2025-11-24T13:19:00.0309457Z 
2025-11-24T13:19:00.0309604Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache/httpcomponents/httpclient/4.5.13:
2025-11-24T13:19:00.0309752Z total 764
2025-11-24T13:19:00.0309897Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0310129Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0310299Z -rw-r--r-- 1 VssAdministrator 197121 780321 Jan  1  2010 httpclient-4.5.13.jar
2025-11-24T13:19:00.0310380Z 
2025-11-24T13:19:00.0310523Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache/httpcomponents/httpcore:
2025-11-24T13:19:00.0310666Z total 0
2025-11-24T13:19:00.0310798Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0310965Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0311130Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 4.4.13
2025-11-24T13:19:00.0311202Z 
2025-11-24T13:19:00.0311353Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache/httpcomponents/httpcore/4.4.13:
2025-11-24T13:19:00.0311498Z total 324
2025-11-24T13:19:00.0311631Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0311792Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0311967Z -rw-r--r-- 1 VssAdministrator 197121 328593 Jan  1  2010 httpcore-4.4.13.jar
2025-11-24T13:19:00.0312042Z 
2025-11-24T13:19:00.0312180Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache/httpcomponents/httpmime:
2025-11-24T13:19:00.0312324Z total 0
2025-11-24T13:19:00.0312453Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0312613Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0312776Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 4.5.6
2025-11-24T13:19:00.0312856Z 
2025-11-24T13:19:00.0313000Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/apache/httpcomponents/httpmime/4.5.6:
2025-11-24T13:19:00.0313143Z total 44
2025-11-24T13:19:00.0313275Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0313443Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0313607Z -rw-r--r-- 1 VssAdministrator 197121 41794 Jan  1  2010 httpmime-4.5.6.jar
2025-11-24T13:19:00.0313725Z 
2025-11-24T13:19:00.0313863Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/bouncycastle:
2025-11-24T13:19:00.0313996Z total 4
2025-11-24T13:19:00.0314125Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0314285Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0314458Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 bcpkix-jdk15on
2025-11-24T13:19:00.0314637Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 bcprov-jdk15on
2025-11-24T13:19:00.0314712Z 
2025-11-24T13:19:00.0314856Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/bouncycastle/bcpkix-jdk15on:
2025-11-24T13:19:00.0314998Z total 0
2025-11-24T13:19:00.0315128Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0315291Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0315590Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.67
2025-11-24T13:19:00.0316102Z 
2025-11-24T13:19:00.0316310Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/bouncycastle/bcpkix-jdk15on/1.67:
2025-11-24T13:19:00.0316463Z total 868
2025-11-24T13:19:00.0316600Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0316765Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0316935Z -rw-r--r-- 1 VssAdministrator 197121 887810 Jan  1  2010 bcpkix-jdk15on-1.67.jar
2025-11-24T13:19:00.0317020Z 
2025-11-24T13:19:00.0317161Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/bouncycastle/bcprov-jdk15on:
2025-11-24T13:19:00.0317302Z total 0
2025-11-24T13:19:00.0317439Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0317599Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0317762Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.67
2025-11-24T13:19:00.0317839Z 
2025-11-24T13:19:00.0317982Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/bouncycastle/bcprov-jdk15on/1.67:
2025-11-24T13:19:00.0318216Z total 5824
2025-11-24T13:19:00.0318354Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0318520Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0318691Z -rw-r--r-- 1 VssAdministrator 197121 5961136 Jan  1  2010 bcprov-jdk15on-1.67.jar
2025-11-24T13:19:00.0318768Z 
2025-11-24T13:19:00.0318907Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/checkerframework:
2025-11-24T13:19:00.0319040Z total 4
2025-11-24T13:19:00.0319171Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0319329Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0319501Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 checker-qual
2025-11-24T13:19:00.0319576Z 
2025-11-24T13:19:00.0319714Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/checkerframework/checker-qual:
2025-11-24T13:19:00.0319866Z total 0
2025-11-24T13:19:00.0320000Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0320160Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0320323Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 3.5.0
2025-11-24T13:19:00.0320402Z 
2025-11-24T13:19:00.0320547Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/checkerframework/checker-qual/3.5.0:
2025-11-24T13:19:00.0320695Z total 212
2025-11-24T13:19:00.0320829Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0320998Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0321165Z -rw-r--r-- 1 VssAdministrator 197121 214381 Jan  1  2010 checker-qual-3.5.0.jar
2025-11-24T13:19:00.0321241Z 
2025-11-24T13:19:00.0321379Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/glassfish:
2025-11-24T13:19:00.0321509Z total 4
2025-11-24T13:19:00.0321639Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0321802Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0322018Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jaxb
2025-11-24T13:19:00.0322089Z 
2025-11-24T13:19:00.0322223Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/glassfish/jaxb:
2025-11-24T13:19:00.0322366Z total 0
2025-11-24T13:19:00.0322498Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0322657Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0322826Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 jaxb-runtime
2025-11-24T13:19:00.0323004Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 txw2
2025-11-24T13:19:00.0323074Z 
2025-11-24T13:19:00.0323212Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/glassfish/jaxb/jaxb-runtime:
2025-11-24T13:19:00.0323359Z total 0
2025-11-24T13:19:00.0323491Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0323651Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0323823Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.3.2
2025-11-24T13:19:00.0323900Z 
2025-11-24T13:19:00.0324044Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/glassfish/jaxb/jaxb-runtime/2.3.2:
2025-11-24T13:19:00.0324187Z total 992
2025-11-24T13:19:00.0324320Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0324490Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0324660Z -rw-r--r-- 1 VssAdministrator 197121 1013367 Jan  1  2010 jaxb-runtime-2.3.2.jar
2025-11-24T13:19:00.0324743Z 
2025-11-24T13:19:00.0324879Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/glassfish/jaxb/txw2:
2025-11-24T13:19:00.0325016Z total 0
2025-11-24T13:19:00.0325146Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0325305Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0325474Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.3.2
2025-11-24T13:19:00.0325587Z 
2025-11-24T13:19:00.0325727Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/glassfish/jaxb/txw2/2.3.2:
2025-11-24T13:19:00.0325874Z total 72
2025-11-24T13:19:00.0326008Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0326169Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0326330Z -rw-r--r-- 1 VssAdministrator 197121 72080 Jan  1  2010 txw2-2.3.2.jar
2025-11-24T13:19:00.0326405Z 
2025-11-24T13:19:00.0326535Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains:
2025-11-24T13:19:00.0326665Z total 8
2025-11-24T13:19:00.0326799Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0326960Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0327126Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 annotations
2025-11-24T13:19:00.0327295Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 intellij
2025-11-24T13:19:00.0327470Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kotlin
2025-11-24T13:19:00.0327635Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kotlinx
2025-11-24T13:19:00.0327706Z 
2025-11-24T13:19:00.0327847Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/annotations:
2025-11-24T13:19:00.0327982Z total 0
2025-11-24T13:19:00.0328111Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0328271Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0328435Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 13.0
2025-11-24T13:19:00.0328506Z 
2025-11-24T13:19:00.0328643Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/annotations/13.0:
2025-11-24T13:19:00.0328787Z total 20
2025-11-24T13:19:00.0328918Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0329079Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0329244Z -rw-r--r-- 1 VssAdministrator 197121 17536 Jan  1  2010 annotations-13.0.jar
2025-11-24T13:19:00.0329362Z 
2025-11-24T13:19:00.0329498Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/intellij:
2025-11-24T13:19:00.0329634Z total 0
2025-11-24T13:19:00.0329764Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0329927Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0330087Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 deps
2025-11-24T13:19:00.0330157Z 
2025-11-24T13:19:00.0330300Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/intellij/deps:
2025-11-24T13:19:00.0330436Z total 0
2025-11-24T13:19:00.0330565Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0330723Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0330892Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 trove4j
2025-11-24T13:19:00.0330963Z 
2025-11-24T13:19:00.0331104Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/intellij/deps/trove4j:
2025-11-24T13:19:00.0331259Z total 0
2025-11-24T13:19:00.0331387Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0331546Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0331713Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.0.20181211
2025-11-24T13:19:00.0331794Z 
2025-11-24T13:19:00.0331942Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/intellij/deps/trove4j/1.0.20181211:
2025-11-24T13:19:00.0332095Z total 560
2025-11-24T13:19:00.0332233Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0332397Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0332568Z -rw-r--r-- 1 VssAdministrator 197121 572966 Jan  1  2010 trove4j-1.0.20181211.jar
2025-11-24T13:19:00.0332651Z 
2025-11-24T13:19:00.0332784Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin:
2025-11-24T13:19:00.0333376Z total 4
2025-11-24T13:19:00.0333514Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0333682Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0333880Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kotlin-reflect
2025-11-24T13:19:00.0334059Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kotlin-stdlib
2025-11-24T13:19:00.0334243Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kotlin-stdlib-common
2025-11-24T13:19:00.0334432Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kotlin-stdlib-jdk7
2025-11-24T13:19:00.0334609Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kotlin-stdlib-jdk8
2025-11-24T13:19:00.0334687Z 
2025-11-24T13:19:00.0334836Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin/kotlin-reflect:
2025-11-24T13:19:00.0334980Z total 4
2025-11-24T13:19:00.0335110Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0335270Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0335443Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.5.31
2025-11-24T13:19:00.0335516Z 
2025-11-24T13:19:00.0335659Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin/kotlin-reflect/1.5.31:
2025-11-24T13:19:00.0335815Z total 2964
2025-11-24T13:19:00.0335949Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0336114Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0336286Z -rw-r--r-- 1 VssAdministrator 197121 3031425 Jan  1  2010 kotlin-reflect-1.5.31.jar
2025-11-24T13:19:00.0336369Z 
2025-11-24T13:19:00.0336511Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin/kotlin-stdlib:
2025-11-24T13:19:00.0336653Z total 4
2025-11-24T13:19:00.0336791Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0336950Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0337115Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.5.31
2025-11-24T13:19:00.0337241Z 
2025-11-24T13:19:00.0337390Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin/kotlin-stdlib/1.5.31:
2025-11-24T13:19:00.0337538Z total 1472
2025-11-24T13:19:00.0337673Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0337836Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0338010Z -rw-r--r-- 1 VssAdministrator 197121 1505952 Jan  1  2010 kotlin-stdlib-1.5.31.jar
2025-11-24T13:19:00.0338088Z 
2025-11-24T13:19:00.0338231Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin/kotlin-stdlib-common:
2025-11-24T13:19:00.0338379Z total 4
2025-11-24T13:19:00.0338509Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0338673Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0338839Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.5.31
2025-11-24T13:19:00.0338918Z 
2025-11-24T13:19:00.0339069Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin/kotlin-stdlib-common/1.5.31:
2025-11-24T13:19:00.0339223Z total 196
2025-11-24T13:19:00.0339362Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0339524Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0339698Z -rw-r--r-- 1 VssAdministrator 197121 198322 Jan  1  2010 kotlin-stdlib-common-1.5.31.jar
2025-11-24T13:19:00.0339785Z 
2025-11-24T13:19:00.0339928Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk7:
2025-11-24T13:19:00.0340070Z total 4
2025-11-24T13:19:00.0340199Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0340368Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0340533Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.5.31
2025-11-24T13:19:00.0340604Z 
2025-11-24T13:19:00.0340758Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk7/1.5.31:
2025-11-24T13:19:00.0340951Z total 24
2025-11-24T13:19:00.0341086Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0341248Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0341425Z -rw-r--r-- 1 VssAdministrator 197121 22986 Jan  1  2010 kotlin-stdlib-jdk7-1.5.31.jar
2025-11-24T13:19:00.0341503Z 
2025-11-24T13:19:00.0341647Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk8:
2025-11-24T13:19:00.0341796Z total 4
2025-11-24T13:19:00.0341925Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0342084Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0342248Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.5.31
2025-11-24T13:19:00.0342328Z 
2025-11-24T13:19:00.0342474Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlin/kotlin-stdlib-jdk8/1.5.31:
2025-11-24T13:19:00.0342623Z total 16
2025-11-24T13:19:00.0342762Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0342923Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0343091Z -rw-r--r-- 1 VssAdministrator 197121 16121 Jan  1  2010 kotlin-stdlib-jdk8-1.5.31.jar
2025-11-24T13:19:00.0343175Z 
2025-11-24T13:19:00.0343307Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlinx:
2025-11-24T13:19:00.0343439Z total 0
2025-11-24T13:19:00.0343570Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0343738Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0343907Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 kotlinx-cli-jvm
2025-11-24T13:19:00.0343985Z 
2025-11-24T13:19:00.0344131Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlinx/kotlinx-cli-jvm:
2025-11-24T13:19:00.0344273Z total 0
2025-11-24T13:19:00.0344403Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0344605Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0344774Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 0.3.1
2025-11-24T13:19:00.0344845Z 
2025-11-24T13:19:00.0344991Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jetbrains/kotlinx/kotlinx-cli-jvm/0.3.1:
2025-11-24T13:19:00.0345142Z total 84
2025-11-24T13:19:00.0345275Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0345435Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0345605Z -rw-r--r-- 1 VssAdministrator 197121 82399 Jan  1  2010 kotlinx-cli-jvm-0.3.1.jar
2025-11-24T13:19:00.0345686Z 
2025-11-24T13:19:00.0345813Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jvnet:
2025-11-24T13:19:00.0345940Z total 4
2025-11-24T13:19:00.0346069Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0346233Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0346397Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 staxex
2025-11-24T13:19:00.0346470Z 
2025-11-24T13:19:00.0346605Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jvnet/staxex:
2025-11-24T13:19:00.0346736Z total 0
2025-11-24T13:19:00.0346864Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0347021Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0347189Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 stax-ex
2025-11-24T13:19:00.0347260Z 
2025-11-24T13:19:00.0347395Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jvnet/staxex/stax-ex:
2025-11-24T13:19:00.0347535Z total 0
2025-11-24T13:19:00.0347663Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0347823Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0347985Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.8.1
2025-11-24T13:19:00.0348064Z 
2025-11-24T13:19:00.0348244Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/jvnet/staxex/stax-ex/1.8.1:
2025-11-24T13:19:00.0348385Z total 40
2025-11-24T13:19:00.0348522Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0348683Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0348849Z -rw-r--r-- 1 VssAdministrator 197121 38099 Jan  1  2010 stax-ex-1.8.1.jar
2025-11-24T13:19:00.0348926Z 
2025-11-24T13:19:00.0349053Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/ow2:
2025-11-24T13:19:00.0349180Z total 4
2025-11-24T13:19:00.0349310Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0349468Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0349639Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 asm
2025-11-24T13:19:00.0349710Z 
2025-11-24T13:19:00.0349837Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/ow2/asm:
2025-11-24T13:19:00.0349970Z total 0
2025-11-24T13:19:00.0350102Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0350263Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0350424Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 asm
2025-11-24T13:19:00.0350600Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 asm-analysis
2025-11-24T13:19:00.0350767Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 asm-tree
2025-11-24T13:19:00.0350840Z 
2025-11-24T13:19:00.0350976Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/ow2/asm/asm:
2025-11-24T13:19:00.0351107Z total 0
2025-11-24T13:19:00.0351235Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0351394Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0351563Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 9.1
2025-11-24T13:19:00.0351633Z 
2025-11-24T13:19:00.0351765Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/ow2/asm/asm/9.1:
2025-11-24T13:19:00.0351906Z total 120
2025-11-24T13:19:00.0352043Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0352246Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0352409Z -rw-r--r-- 1 VssAdministrator 197121 121790 Jan  1  2010 asm-9.1.jar
2025-11-24T13:19:00.0352483Z 
2025-11-24T13:19:00.0352619Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/ow2/asm/asm-analysis:
2025-11-24T13:19:00.0352756Z total 0
2025-11-24T13:19:00.0352891Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0353050Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0353212Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 9.1
2025-11-24T13:19:00.0353281Z 
2025-11-24T13:19:00.0353422Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/ow2/asm/asm-analysis/9.1:
2025-11-24T13:19:00.0353561Z total 36
2025-11-24T13:19:00.0353696Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0353858Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0354042Z -rw-r--r-- 1 VssAdministrator 197121 34257 Jan  1  2010 asm-analysis-9.1.jar
2025-11-24T13:19:00.0354116Z 
2025-11-24T13:19:00.0354248Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/ow2/asm/asm-tree:
2025-11-24T13:19:00.0354391Z total 0
2025-11-24T13:19:00.0354521Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0354681Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0354843Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 9.1
2025-11-24T13:19:00.0354918Z 
2025-11-24T13:19:00.0355051Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/ow2/asm/asm-tree/9.1:
2025-11-24T13:19:00.0355186Z total 52
2025-11-24T13:19:00.0355326Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0355486Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0355653Z -rw-r--r-- 1 VssAdministrator 197121 52662 Jan  1  2010 asm-tree-9.1.jar
2025-11-24T13:19:00.0355771Z 
2025-11-24T13:19:00.0355900Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/smali:
2025-11-24T13:19:00.0356029Z total 4
2025-11-24T13:19:00.0356158Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0356325Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0356492Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 baksmali
2025-11-24T13:19:00.0356660Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 dexlib2
2025-11-24T13:19:00.0356825Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 util
2025-11-24T13:19:00.0356903Z 
2025-11-24T13:19:00.0357036Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/smali/baksmali:
2025-11-24T13:19:00.0357168Z total 0
2025-11-24T13:19:00.0357302Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0357460Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0357623Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.5.2
2025-11-24T13:19:00.0357697Z 
2025-11-24T13:19:00.0357839Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/smali/baksmali/2.5.2:
2025-11-24T13:19:00.0357976Z total 124
2025-11-24T13:19:00.0358108Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0358270Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0358441Z -rw-r--r-- 1 VssAdministrator 197121 123309 Jan  1  2010 baksmali-2.5.2.jar
2025-11-24T13:19:00.0358514Z 
2025-11-24T13:19:00.0358649Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/smali/dexlib2:
2025-11-24T13:19:00.0358802Z total 0
2025-11-24T13:19:00.0358932Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0359090Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0359251Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.5.2
2025-11-24T13:19:00.0359327Z 
2025-11-24T13:19:00.0359460Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/smali/dexlib2/2.5.2:
2025-11-24T13:19:00.0359639Z total 1080
2025-11-24T13:19:00.0359778Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0359940Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0360104Z -rw-r--r-- 1 VssAdministrator 197121 1103473 Jan  1  2010 dexlib2-2.5.2.jar
2025-11-24T13:19:00.0360181Z 
2025-11-24T13:19:00.0360313Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/smali/util:
2025-11-24T13:19:00.0360441Z total 0
2025-11-24T13:19:00.0360572Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0360734Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0360895Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.5.2
2025-11-24T13:19:00.0360965Z 
2025-11-24T13:19:00.0361101Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/org/smali/util/2.5.2:
2025-11-24T13:19:00.0361234Z total 28
2025-11-24T13:19:00.0361367Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0361533Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0361700Z -rw-r--r-- 1 VssAdministrator 197121 27118 Jan  1  2010 util-2.5.2.jar
2025-11-24T13:19:00.0361770Z 
2025-11-24T13:19:00.0361896Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/xerces:
2025-11-24T13:19:00.0362024Z total 4
2025-11-24T13:19:00.0362163Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0362328Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0362494Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 xercesImpl
2025-11-24T13:19:00.0362577Z 
2025-11-24T13:19:00.0362709Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/xerces/xercesImpl:
2025-11-24T13:19:00.0362841Z total 0
2025-11-24T13:19:00.0362971Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0363137Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0363341Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 2.12.0
2025-11-24T13:19:00.0363416Z 
2025-11-24T13:19:00.0363556Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/xerces/xercesImpl/2.12.0:
2025-11-24T13:19:00.0363696Z total 1356
2025-11-24T13:19:00.0363831Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0363993Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0364167Z -rw-r--r-- 1 VssAdministrator 197121 1386397 Jan  1  2010 xercesImpl-2.12.0.jar
2025-11-24T13:19:00.0364242Z 
2025-11-24T13:19:00.0364370Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/xml-apis:
2025-11-24T13:19:00.0364503Z total 4
2025-11-24T13:19:00.0364633Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0364792Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0364954Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 xml-apis
2025-11-24T13:19:00.0365033Z 
2025-11-24T13:19:00.0365167Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/xml-apis/xml-apis:
2025-11-24T13:19:00.0365306Z total 0
2025-11-24T13:19:00.0365440Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0365609Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0365776Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 1.4.01
2025-11-24T13:19:00.0365851Z 
2025-11-24T13:19:00.0365995Z C:\Android\android-sdk/cmdline-tools/latest/lib/external/xml-apis/xml-apis/1.4.01:
2025-11-24T13:19:00.0366136Z total 216
2025-11-24T13:19:00.0366273Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0366438Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0366612Z -rw-r--r-- 1 VssAdministrator 197121 220536 Jan  1  2010 xml-apis-1.4.01.jar
2025-11-24T13:19:00.0366688Z 
2025-11-24T13:19:00.0366814Z C:\Android\android-sdk/cmdline-tools/latest/lib/layoutlib-api:
2025-11-24T13:19:00.0366954Z total 124
2025-11-24T13:19:00.0367243Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0367408Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0367581Z -rw-r--r-- 1 VssAdministrator 197121 118630 Jan  1  2010 tools.layoutlib-api.jar
2025-11-24T13:19:00.0367664Z 
2025-11-24T13:19:00.0367788Z C:\Android\android-sdk/cmdline-tools/latest/lib/lint:
2025-11-24T13:19:00.0367914Z total 6336
2025-11-24T13:19:00.0368056Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0368221Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0368385Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 cli
2025-11-24T13:19:00.0368551Z -rw-r--r-- 1 VssAdministrator 197121 1041928 Jan  1  2010 tools.lint-api.jar
2025-11-24T13:19:00.0368729Z -rw-r--r-- 1 VssAdministrator 197121 5263468 Jan  1  2010 tools.lint-checks.jar
2025-11-24T13:19:00.0368901Z -rw-r--r-- 1 VssAdministrator 197121  160287 Jan  1  2010 tools.lint-model.jar
2025-11-24T13:19:00.0368979Z 
2025-11-24T13:19:00.0369113Z C:\Android\android-sdk/cmdline-tools/latest/lib/lint/cli:
2025-11-24T13:19:00.0369240Z total 508
2025-11-24T13:19:00.0369375Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0369538Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0369706Z -rw-r--r-- 1 VssAdministrator 197121 512865 Jan  1  2010 cli.jar
2025-11-24T13:19:00.0369774Z 
2025-11-24T13:19:00.0369896Z C:\Android\android-sdk/cmdline-tools/latest/lib/misc:
2025-11-24T13:19:00.0370026Z total 8
2025-11-24T13:19:00.0370160Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0370321Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0370490Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 screenshot2
2025-11-24T13:19:00.0370570Z 
2025-11-24T13:19:00.0370701Z C:\Android\android-sdk/cmdline-tools/latest/lib/misc/screenshot2:
2025-11-24T13:19:00.0370874Z total 12
2025-11-24T13:19:00.0371011Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0371181Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0371350Z -rw-r--r-- 1 VssAdministrator 197121 11156 Jan  1  2010 libscreenshot2lib.jar
2025-11-24T13:19:00.0371425Z 
2025-11-24T13:19:00.0371556Z C:\Android\android-sdk/cmdline-tools/latest/lib/profgen:
2025-11-24T13:19:00.0371682Z total 8
2025-11-24T13:19:00.0371814Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 .
2025-11-24T13:19:00.0371974Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 ..
2025-11-24T13:19:00.0372145Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 profgen
2025-11-24T13:19:00.0372315Z drwxr-xr-x 1 VssAdministrator 197121 0 Nov  2 23:11 profgen-cli
2025-11-24T13:19:00.0372388Z 
2025-11-24T13:19:00.0372522Z C:\Android\android-sdk/cmdline-tools/latest/lib/profgen/profgen:
2025-11-24T13:19:00.0372651Z total 168
2025-11-24T13:19:00.0372789Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0372952Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0373121Z -rw-r--r-- 1 VssAdministrator 197121 168762 Jan  1  2010 libprofgen.jar
2025-11-24T13:19:00.0373192Z 
2025-11-24T13:19:00.0373320Z C:\Android\android-sdk/cmdline-tools/latest/lib/profgen/profgen-cli:
2025-11-24T13:19:00.0373455Z total 16
2025-11-24T13:19:00.0373589Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 .
2025-11-24T13:19:00.0373753Z drwxr-xr-x 1 VssAdministrator 197121     0 Nov  2 23:11 ..
2025-11-24T13:19:00.0373919Z -rw-r--r-- 1 VssAdministrator 197121 12673 Jan  1  2010 libprofgen-cli-lib.jar
2025-11-24T13:19:00.0373999Z 
2025-11-24T13:19:00.0374121Z C:\Android\android-sdk/cmdline-tools/latest/lib/repository:
2025-11-24T13:19:00.0374245Z total 244
2025-11-24T13:19:00.0374384Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0374557Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0374823Z -rw-r--r-- 1 VssAdministrator 197121 237901 Jan  1  2010 tools.repository.jar
2025-11-24T13:19:00.0374902Z 
2025-11-24T13:19:00.0375027Z C:\Android\android-sdk/cmdline-tools/latest/lib/sdk-common:
2025-11-24T13:19:00.0375155Z total 1512
2025-11-24T13:19:00.0375290Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 .
2025-11-24T13:19:00.0375452Z drwxr-xr-x 1 VssAdministrator 197121       0 Nov  2 23:11 ..
2025-11-24T13:19:00.0375624Z -rw-r--r-- 1 VssAdministrator 197121 1536378 Jan  1  2010 tools.sdk-common.jar
2025-11-24T13:19:00.0375700Z 
2025-11-24T13:19:00.0375822Z C:\Android\android-sdk/cmdline-tools/latest/lib/sdklib:
2025-11-24T13:19:00.0375952Z total 1396
2025-11-24T13:19:00.0376085Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 .
2025-11-24T13:19:00.0376248Z drwxr-xr-x 1 VssAdministrator 197121      0 Nov  2 23:11 ..
2025-11-24T13:19:00.0376413Z -rw-r--r-- 1 VssAdministrator 197121  28021 Jan  1  2010 libavdmanager_lib.jar
2025-11-24T13:19:00.0376591Z -rw-r--r-- 1 VssAdministrator 197121  41249 Jan  1  2010 libsdkmanager_lib.jar
2025-11-24T13:19:00.0376763Z -rw-r--r-- 1 VssAdministrator 197121 634458 Jan  1  2010 sdklib.core.jar
2025-11-24T13:19:00.0376973Z -rw-r--r-- 1 VssAdministrator 197121 706147 Jan  1  2010 tools.sdklib.jar
2025-11-24T13:19:00.0377051Z 
2025-11-24T13:19:00.0393573Z ##[error]Bash exited with code '1'.
2025-11-24T13:19:00.0403559Z ##[section]Finishing: Setup Android SDK and Create Emulator with Google Play