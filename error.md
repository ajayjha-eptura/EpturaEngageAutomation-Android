2026-01-22T16:06:36.2627329Z ##[section]Starting: Maven Clean Compile
2026-01-22T16:06:36.2638922Z ==============================================================================
2026-01-22T16:06:36.2639138Z Task         : Maven
2026-01-22T16:06:36.2639290Z Description  : Build, test, and deploy with Apache Maven
2026-01-22T16:06:36.2639460Z Version      : 3.264.1
2026-01-22T16:06:36.2639588Z Author       : Microsoft Corporation
2026-01-22T16:06:36.2639751Z Help         : https://docs.microsoft.com/azure/devops/pipelines/tasks/build/maven
2026-01-22T16:06:36.2639929Z ==============================================================================
2026-01-22T16:06:37.0057775Z [command]/usr/bin/mvn -version
2026-01-22T16:06:43.3701186Z Apache Maven 3.9.12 (848fbb4bf2d427b72bdb2471c22fced7ebd9a7a1)
2026-01-22T16:06:43.3702450Z Maven home: /usr/share/apache-maven-3.9.12
2026-01-22T16:06:43.3707836Z Java version: 11.0.29, vendor: Eclipse Adoptium, runtime: /usr/lib/jvm/temurin-11-jdk-amd64
2026-01-22T16:06:43.3708283Z Default locale: en, platform encoding: UTF-8
2026-01-22T16:06:43.3708757Z OS name: "linux", version: "6.11.0-1018-azure", arch: "amd64", family: "unix"
2026-01-22T16:06:43.3865815Z 
2026-01-22T16:06:43.3919394Z [command]/usr/bin/mvn -f /home/vsts/work/1/s/pom.xml -DskipTests -Dmaven.repo.local=/home/vsts/work/1/.m2/repository clean compile
2026-01-22T16:06:46.3437203Z [INFO] Scanning for projects...
2026-01-22T16:06:46.4907785Z [INFO] 
2026-01-22T16:06:46.4927495Z [INFO] ----------< com.eptura.appium:EpturaEngageAutomation-Android >----------
2026-01-22T16:06:46.4928671Z [INFO] Building EpturaEngageAutomation-Android 0.0.1-SNAPSHOT
2026-01-22T16:06:46.4929217Z [INFO]   from pom.xml
2026-01-22T16:06:46.4930290Z [INFO] --------------------------------[ jar ]---------------------------------
2026-01-22T16:06:47.9917572Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/3.2.0/maven-clean-plugin-3.2.0.pom
2026-01-22T16:06:48.9405309Z Progress (1): 779 B
2026-01-22T16:06:48.9405690Z Progress (1): 1.8 kB
2026-01-22T16:06:48.9406039Z Progress (1): 4.2 kB
2026-01-22T16:06:48.9503885Z Progress (1): 5.3 kB
2026-01-22T16:06:48.9509880Z                     
2026-01-22T16:06:48.9510325Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/3.2.0/maven-clean-plugin-3.2.0.pom (5.3 kB at 5.5 kB/s)
2026-01-22T16:06:49.0404316Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/35/maven-plugins-35.pom
2026-01-22T16:06:49.0610943Z Progress (1): 755 B
2026-01-22T16:06:49.0643707Z Progress (1): 1.8 kB
2026-01-22T16:06:49.0644278Z Progress (1): 3.7 kB
2026-01-22T16:06:49.0644702Z Progress (1): 6.4 kB
2026-01-22T16:06:49.0645115Z Progress (1): 8.2 kB
2026-01-22T16:06:49.0656778Z Progress (1): 9.9 kB
2026-01-22T16:06:49.0658268Z                     
2026-01-22T16:06:49.0659712Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/35/maven-plugins-35.pom (9.9 kB at 367 kB/s)
2026-01-22T16:06:49.0737452Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/35/maven-parent-35.pom
2026-01-22T16:06:49.0944405Z Progress (1): 717 B
2026-01-22T16:06:49.0999609Z Progress (1): 1.6 kB
2026-01-22T16:06:49.1000377Z Progress (1): 4.2 kB
2026-01-22T16:06:49.1000962Z Progress (1): 8.4 kB
2026-01-22T16:06:49.1001611Z Progress (1): 11 kB 
2026-01-22T16:06:49.1002274Z Progress (1): 16 kB
2026-01-22T16:06:49.1002680Z Progress (1): 20 kB
2026-01-22T16:06:49.1023498Z Progress (1): 23 kB
2026-01-22T16:06:49.1024367Z Progress (1): 26 kB
2026-01-22T16:06:49.1025198Z Progress (1): 28 kB
2026-01-22T16:06:49.1025951Z Progress (1): 30 kB
2026-01-22T16:06:49.1026719Z Progress (1): 33 kB
2026-01-22T16:06:49.1027374Z Progress (1): 37 kB
2026-01-22T16:06:49.1027982Z Progress (1): 38 kB
2026-01-22T16:06:49.1073490Z Progress (1): 42 kB
2026-01-22T16:06:49.1073970Z Progress (1): 45 kB
2026-01-22T16:06:49.1074368Z                    
2026-01-22T16:06:49.1075097Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/35/maven-parent-35.pom (45 kB at 1.5 MB/s)
2026-01-22T16:06:49.1194332Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/25/apache-25.pom
2026-01-22T16:06:49.1380261Z Progress (1): 743 B
2026-01-22T16:06:49.1396499Z Progress (1): 1.6 kB
2026-01-22T16:06:49.1419832Z Progress (1): 3.4 kB
2026-01-22T16:06:49.1424096Z Progress (1): 5.5 kB
2026-01-22T16:06:49.1428132Z Progress (1): 9.0 kB
2026-01-22T16:06:49.1430054Z Progress (1): 14 kB 
2026-01-22T16:06:49.1431971Z Progress (1): 17 kB
2026-01-22T16:06:49.1434299Z Progress (1): 19 kB
2026-01-22T16:06:49.1436171Z Progress (1): 21 kB
2026-01-22T16:06:49.1437962Z                    
2026-01-22T16:06:49.1439797Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/25/apache-25.pom (21 kB at 822 kB/s)
2026-01-22T16:06:49.1726780Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/3.2.0/maven-clean-plugin-3.2.0.jar
2026-01-22T16:06:49.1933778Z Progress (1): 0.9/36 kB
2026-01-22T16:06:49.1936534Z Progress (1): 2.3/36 kB
2026-01-22T16:06:49.1937483Z Progress (1): 3.6/36 kB
2026-01-22T16:06:49.1939183Z Progress (1): 5.0/36 kB
2026-01-22T16:06:49.1939517Z Progress (1): 6.4/36 kB
2026-01-22T16:06:49.1946202Z Progress (1): 7.7/36 kB
2026-01-22T16:06:49.1954963Z Progress (1): 9.1/36 kB
2026-01-22T16:06:49.1978953Z Progress (1): 10/36 kB 
2026-01-22T16:06:49.1981944Z Progress (1): 12/36 kB
2026-01-22T16:06:49.2023455Z Progress (1): 13/36 kB
2026-01-22T16:06:49.2024108Z Progress (1): 15/36 kB
2026-01-22T16:06:49.2028259Z Progress (1): 16/36 kB
2026-01-22T16:06:49.2028601Z Progress (1): 17/36 kB
2026-01-22T16:06:49.2028908Z Progress (1): 19/36 kB
2026-01-22T16:06:49.2029207Z Progress (1): 20/36 kB
2026-01-22T16:06:49.2029499Z Progress (1): 21/36 kB
2026-01-22T16:06:49.2029796Z Progress (1): 23/36 kB
2026-01-22T16:06:49.2034370Z Progress (1): 24/36 kB
2026-01-22T16:06:49.2044479Z Progress (1): 26/36 kB
2026-01-22T16:06:49.2052169Z Progress (1): 27/36 kB
2026-01-22T16:06:49.2059281Z Progress (1): 28/36 kB
2026-01-22T16:06:49.2084825Z Progress (1): 30/36 kB
2026-01-22T16:06:49.2085151Z Progress (1): 31/36 kB
2026-01-22T16:06:49.2089674Z Progress (1): 32/36 kB
2026-01-22T16:06:49.2090837Z Progress (1): 36 kB   
2026-01-22T16:06:49.2096735Z                    
2026-01-22T16:06:49.2098181Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-clean-plugin/3.2.0/maven-clean-plugin-3.2.0.jar (36 kB at 915 kB/s)
2026-01-22T16:06:49.2243751Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.3.1/maven-resources-plugin-3.3.1.pom
2026-01-22T16:06:49.2461065Z Progress (1): 766 B
2026-01-22T16:06:49.2461444Z Progress (1): 2.1 kB
2026-01-22T16:06:49.2461768Z Progress (1): 4.9 kB
2026-01-22T16:06:49.2462078Z Progress (1): 7.5 kB
2026-01-22T16:06:49.2468840Z Progress (1): 8.2 kB
2026-01-22T16:06:49.2469152Z                     
2026-01-22T16:06:49.2469590Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.3.1/maven-resources-plugin-3.3.1.pom (8.2 kB at 326 kB/s)
2026-01-22T16:06:49.2516496Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/39/maven-plugins-39.pom
2026-01-22T16:06:49.2723708Z Progress (1): 763 B
2026-01-22T16:06:49.2724244Z Progress (1): 2.3 kB
2026-01-22T16:06:49.2724655Z Progress (1): 4.9 kB
2026-01-22T16:06:49.2725046Z Progress (1): 7.3 kB
2026-01-22T16:06:49.2748450Z Progress (1): 8.1 kB
2026-01-22T16:06:49.2748798Z                     
2026-01-22T16:06:49.2749225Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/39/maven-plugins-39.pom (8.1 kB at 352 kB/s)
2026-01-22T16:06:49.2792671Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/39/maven-parent-39.pom
2026-01-22T16:06:49.3004694Z Progress (1): 724 B
2026-01-22T16:06:49.3005337Z Progress (1): 1.9 kB
2026-01-22T16:06:49.3005827Z Progress (1): 5.5 kB
2026-01-22T16:06:49.3006302Z Progress (1): 9.7 kB
2026-01-22T16:06:49.3006834Z Progress (1): 14 kB 
2026-01-22T16:06:49.3007305Z Progress (1): 19 kB
2026-01-22T16:06:49.3007763Z Progress (1): 23 kB
2026-01-22T16:06:49.3008230Z Progress (1): 25 kB
2026-01-22T16:06:49.3008687Z Progress (1): 27 kB
2026-01-22T16:06:49.3009165Z Progress (1): 28 kB
2026-01-22T16:06:49.3009631Z Progress (1): 31 kB
2026-01-22T16:06:49.3011935Z Progress (1): 35 kB
2026-01-22T16:06:49.3012597Z Progress (1): 38 kB
2026-01-22T16:06:49.3013291Z Progress (1): 41 kB
2026-01-22T16:06:49.3013785Z Progress (1): 44 kB
2026-01-22T16:06:49.3014244Z Progress (1): 48 kB
2026-01-22T16:06:49.3014725Z                    
2026-01-22T16:06:49.3015351Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/39/maven-parent-39.pom (48 kB at 2.4 MB/s)
2026-01-22T16:06:49.3078655Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/29/apache-29.pom
2026-01-22T16:06:49.3271129Z Progress (1): 745 B
2026-01-22T16:06:49.3273771Z Progress (1): 2.1 kB
2026-01-22T16:06:49.3306196Z Progress (1): 4.0 kB
2026-01-22T16:06:49.3307509Z Progress (1): 6.7 kB
2026-01-22T16:06:49.3309546Z Progress (1): 12 kB 
2026-01-22T16:06:49.3310052Z Progress (1): 16 kB
2026-01-22T16:06:49.3310360Z Progress (1): 19 kB
2026-01-22T16:06:49.3325114Z Progress (1): 19 kB
2026-01-22T16:06:49.3331125Z Progress (1): 21 kB
2026-01-22T16:06:49.3333207Z                    
2026-01-22T16:06:49.3335228Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/29/apache-29.pom (21 kB at 829 kB/s)
2026-01-22T16:06:49.3475168Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.3.1/maven-resources-plugin-3.3.1.jar
2026-01-22T16:06:49.3660385Z Progress (1): 3.8/31 kB
2026-01-22T16:06:49.3662022Z Progress (1): 8.0/31 kB
2026-01-22T16:06:49.3663869Z Progress (1): 12/31 kB 
2026-01-22T16:06:49.3666205Z Progress (1): 16/31 kB
2026-01-22T16:06:49.3704385Z Progress (1): 21/31 kB
2026-01-22T16:06:49.3708462Z Progress (1): 25/31 kB
2026-01-22T16:06:49.3712591Z Progress (1): 29/31 kB
2026-01-22T16:06:49.3716901Z Progress (1): 31 kB   
2026-01-22T16:06:49.3721337Z                    
2026-01-22T16:06:49.3723521Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.3.1/maven-resources-plugin-3.3.1.jar (31 kB at 1.3 MB/s)
2026-01-22T16:06:49.3876455Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.11.0/maven-compiler-plugin-3.11.0.pom
2026-01-22T16:06:49.4114252Z Progress (1): 756 B
2026-01-22T16:06:49.4128242Z Progress (1): 2.2 kB
2026-01-22T16:06:49.4128576Z Progress (1): 3.9 kB
2026-01-22T16:06:49.4128925Z Progress (1): 7.6 kB
2026-01-22T16:06:49.4155528Z Progress (1): 9.8 kB
2026-01-22T16:06:49.4155842Z                     
2026-01-22T16:06:49.4156312Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.11.0/maven-compiler-plugin-3.11.0.pom (9.8 kB at 378 kB/s)
2026-01-22T16:06:49.4254088Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.11.0/maven-compiler-plugin-3.11.0.jar
2026-01-22T16:06:49.4402959Z Progress (1): 3.8/66 kB
2026-01-22T16:06:49.4412056Z Progress (1): 4.1/66 kB
2026-01-22T16:06:49.4436073Z Progress (1): 8.3/66 kB
2026-01-22T16:06:49.4436412Z Progress (1): 13/66 kB 
2026-01-22T16:06:49.4436729Z Progress (1): 17/66 kB
2026-01-22T16:06:49.4437032Z Progress (1): 21/66 kB
2026-01-22T16:06:49.4444917Z Progress (1): 25/66 kB
2026-01-22T16:06:49.4466136Z Progress (1): 29/66 kB
2026-01-22T16:06:49.4469882Z Progress (1): 34/66 kB
2026-01-22T16:06:49.4470490Z Progress (1): 38/66 kB
2026-01-22T16:06:49.4471681Z Progress (1): 42/66 kB
2026-01-22T16:06:49.4472232Z Progress (1): 46/66 kB
2026-01-22T16:06:49.4499279Z Progress (1): 51/66 kB
2026-01-22T16:06:49.4500177Z Progress (1): 55/66 kB
2026-01-22T16:06:49.4500662Z Progress (1): 59/66 kB
2026-01-22T16:06:49.4503033Z Progress (1): 63/66 kB
2026-01-22T16:06:49.4503621Z Progress (1): 66 kB   
2026-01-22T16:06:49.4505214Z                    
2026-01-22T16:06:49.4505914Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.11.0/maven-compiler-plugin-3.11.0.jar (66 kB at 2.6 MB/s)
2026-01-22T16:06:49.4795515Z Downloading from central: https://repo.maven.apache.org/maven2/io/appium/java-client/8.6.0/java-client-8.6.0.pom
2026-01-22T16:06:49.5003603Z Progress (1): 958 B
2026-01-22T16:06:49.5019197Z Progress (1): 3.6 kB
2026-01-22T16:06:49.5019870Z                     
2026-01-22T16:06:49.5020566Z Downloaded from central: https://repo.maven.apache.org/maven2/io/appium/java-client/8.6.0/java-client-8.6.0.pom (3.6 kB at 149 kB/s)
2026-01-22T16:06:49.5124210Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/maven-metadata.xml
2026-01-22T16:06:49.5294796Z Progress (1): 4.6 kB
2026-01-22T16:06:49.5299834Z Progress (1): 6.1 kB
2026-01-22T16:06:49.5300558Z                     
2026-01-22T16:06:49.5301338Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/maven-metadata.xml (6.1 kB at 339 kB/s)
2026-01-22T16:06:49.5434778Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.9.1/selenium-api-4.9.1.pom
2026-01-22T16:06:49.5606984Z Progress (1): 1.1 kB
2026-01-22T16:06:49.5616727Z Progress (1): 2.1 kB
2026-01-22T16:06:49.5633461Z                     
2026-01-22T16:06:49.5634256Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.9.1/selenium-api-4.9.1.pom (2.1 kB at 109 kB/s)
2026-01-22T16:06:49.5675574Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.10.0/selenium-api-4.10.0.pom
2026-01-22T16:06:49.5865554Z Progress (1): 1.1 kB
2026-01-22T16:06:49.5866150Z Progress (1): 2.1 kB
2026-01-22T16:06:49.5866657Z                     
2026-01-22T16:06:49.5867568Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.10.0/selenium-api-4.10.0.pom (2.1 kB at 122 kB/s)
2026-01-22T16:06:49.5894403Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.11.0/selenium-api-4.11.0.pom
2026-01-22T16:06:49.6075869Z Progress (1): 1.1 kB
2026-01-22T16:06:49.6085176Z Progress (1): 2.1 kB
2026-01-22T16:06:49.6085908Z                     
2026-01-22T16:06:49.6087277Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.11.0/selenium-api-4.11.0.pom (2.1 kB at 109 kB/s)
2026-01-22T16:06:49.6133007Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.12.0/selenium-api-4.12.0.pom
2026-01-22T16:06:49.6305759Z Progress (1): 1.1 kB
2026-01-22T16:06:49.6353214Z Progress (1): 2.1 kB
2026-01-22T16:06:49.6353905Z                     
2026-01-22T16:06:49.6354621Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.12.0/selenium-api-4.12.0.pom (2.1 kB at 109 kB/s)
2026-01-22T16:06:49.6355467Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.12.1/selenium-api-4.12.1.pom
2026-01-22T16:06:49.6533936Z Progress (1): 1.1 kB
2026-01-22T16:06:49.6564411Z Progress (1): 2.1 kB
2026-01-22T16:06:49.6565204Z                     
2026-01-22T16:06:49.6565878Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.12.1/selenium-api-4.12.1.pom (2.1 kB at 104 kB/s)
2026-01-22T16:06:49.6615283Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.13.0/selenium-api-4.13.0.pom
2026-01-22T16:06:49.6788710Z Progress (1): 1.1 kB
2026-01-22T16:06:49.6834625Z Progress (1): 2.1 kB
2026-01-22T16:06:49.6835547Z                     
2026-01-22T16:06:49.6836250Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.13.0/selenium-api-4.13.0.pom (2.1 kB at 99 kB/s)
2026-01-22T16:06:49.6852186Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/maven-metadata.xml
2026-01-22T16:06:49.7008926Z Progress (1): 4.5 kB
2026-01-22T16:06:49.7010475Z Progress (1): 6.1 kB
2026-01-22T16:06:49.7011013Z                     
2026-01-22T16:06:49.7011591Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/maven-metadata.xml (6.1 kB at 382 kB/s)
2026-01-22T16:06:49.7087331Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.9.1/selenium-remote-driver-4.9.1.pom
2026-01-22T16:06:49.7254060Z Progress (1): 1.0 kB
2026-01-22T16:06:49.7254462Z Progress (1): 6.9 kB
2026-01-22T16:06:49.7264374Z Progress (1): 8.4 kB
2026-01-22T16:06:49.7264709Z                     
2026-01-22T16:06:49.7265161Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.9.1/selenium-remote-driver-4.9.1.pom (8.4 kB at 443 kB/s)
2026-01-22T16:06:49.7312911Z Downloading from central: https://repo.maven.apache.org/maven2/com/beust/jcommander/1.82/jcommander-1.82.pom
2026-01-22T16:06:49.7533613Z Progress (1): 1.0 kB
2026-01-22T16:06:49.7533987Z Progress (1): 1.5 kB
2026-01-22T16:06:49.7536576Z                     
2026-01-22T16:06:49.7537027Z Downloaded from central: https://repo.maven.apache.org/maven2/com/beust/jcommander/1.82/jcommander-1.82.pom (1.5 kB at 69 kB/s)
2026-01-22T16:06:49.7601082Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.0.1/auto-service-annotations-1.0.1.pom
2026-01-22T16:06:49.7784449Z Progress (1): 832 B
2026-01-22T16:06:49.7823500Z Progress (1): 2.3 kB
2026-01-22T16:06:49.7824039Z                     
2026-01-22T16:06:49.7824623Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.0.1/auto-service-annotations-1.0.1.pom (2.3 kB at 104 kB/s)
2026-01-22T16:06:49.7834446Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-aggregator/1.0.1/auto-service-aggregator-1.0.1.pom
2026-01-22T16:06:49.8013720Z Progress (1): 813 B
2026-01-22T16:06:49.8016543Z Progress (1): 2.4 kB
2026-01-22T16:06:49.8026187Z Progress (1): 4.3 kB
2026-01-22T16:06:49.8033773Z                     
2026-01-22T16:06:49.8034453Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-aggregator/1.0.1/auto-service-aggregator-1.0.1.pom (4.3 kB at 213 kB/s)
2026-01-22T16:06:49.8063994Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
2026-01-22T16:06:49.8242955Z Progress (1): 847 B
2026-01-22T16:06:49.8243514Z Progress (1): 2.5 kB
2026-01-22T16:06:49.8243968Z Progress (1): 4.8 kB
2026-01-22T16:06:49.8244390Z                     
2026-01-22T16:06:49.8244909Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/oss/oss-parent/7/oss-parent-7.pom (4.8 kB at 254 kB/s)
2026-01-22T16:06:49.8281594Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service/1.0.1/auto-service-1.0.1.pom
2026-01-22T16:06:49.8492173Z Progress (1): 821 B
2026-01-22T16:06:49.8492518Z Progress (1): 2.9 kB
2026-01-22T16:06:49.8556243Z Progress (1): 3.1 kB
2026-01-22T16:06:49.8559608Z                     
2026-01-22T16:06:49.8560149Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service/1.0.1/auto-service-1.0.1.pom (3.1 kB at 124 kB/s)
2026-01-22T16:06:49.8625668Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/auto-common/1.2/auto-common-1.2.pom
2026-01-22T16:06:49.8810688Z Progress (1): 811 B
2026-01-22T16:06:49.8821705Z Progress (1): 2.4 kB
2026-01-22T16:06:49.8822068Z Progress (1): 4.4 kB
2026-01-22T16:06:49.8822442Z                     
2026-01-22T16:06:49.8834517Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/auto-common/1.2/auto-common-1.2.pom (4.4 kB at 210 kB/s)
2026-01-22T16:06:49.8904547Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/31.0.1-jre/guava-31.0.1-jre.pom
2026-01-22T16:06:49.9105921Z Progress (1): 1.1 kB
2026-01-22T16:06:49.9117976Z Progress (1): 2.9 kB
2026-01-22T16:06:49.9119143Z Progress (1): 4.9 kB
2026-01-22T16:06:49.9119470Z Progress (1): 6.8 kB
2026-01-22T16:06:49.9119788Z Progress (1): 8.6 kB
2026-01-22T16:06:49.9120094Z Progress (1): 11 kB 
2026-01-22T16:06:49.9120392Z                    
2026-01-22T16:06:49.9120795Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/31.0.1-jre/guava-31.0.1-jre.pom (11 kB at 477 kB/s)
2026-01-22T16:06:49.9199211Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/31.0.1-jre/guava-parent-31.0.1-jre.pom
2026-01-22T16:06:49.9385095Z Progress (1): 903 B
2026-01-22T16:06:49.9385560Z Progress (1): 2.7 kB
2026-01-22T16:06:49.9386048Z Progress (1): 5.2 kB
2026-01-22T16:06:49.9389585Z Progress (1): 7.7 kB
2026-01-22T16:06:49.9389928Z Progress (1): 9.4 kB
2026-01-22T16:06:49.9414525Z Progress (1): 14 kB 
2026-01-22T16:06:49.9414879Z                    
2026-01-22T16:06:49.9415387Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/31.0.1-jre/guava-parent-31.0.1-jre.pom (14 kB at 691 kB/s)
2026-01-22T16:06:49.9452675Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.pom
2026-01-22T16:06:49.9625002Z Progress (1): 981 B
2026-01-22T16:06:49.9627677Z Progress (1): 2.4 kB
2026-01-22T16:06:49.9628002Z                     
2026-01-22T16:06:49.9628405Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.pom (2.4 kB at 134 kB/s)
2026-01-22T16:06:49.9672594Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/26.0-android/guava-parent-26.0-android.pom
2026-01-22T16:06:49.9863472Z Progress (1): 982 B
2026-01-22T16:06:49.9864091Z Progress (1): 2.7 kB
2026-01-22T16:06:49.9864502Z Progress (1): 5.4 kB
2026-01-22T16:06:49.9864924Z Progress (1): 7.4 kB
2026-01-22T16:06:49.9865311Z Progress (1): 10 kB 
2026-01-22T16:06:49.9865691Z                    
2026-01-22T16:06:49.9866196Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/26.0-android/guava-parent-26.0-android.pom (10 kB at 566 kB/s)
2026-01-22T16:06:49.9993993Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/oss/oss-parent/9/oss-parent-9.pom
2026-01-22T16:06:50.0163162Z Progress (1): 835 B
2026-01-22T16:06:50.0168802Z Progress (1): 2.7 kB
2026-01-22T16:06:50.0169160Z Progress (1): 6.2 kB
2026-01-22T16:06:50.0176201Z Progress (1): 6.6 kB
2026-01-22T16:06:50.0177078Z                     
2026-01-22T16:06:50.0177533Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/oss/oss-parent/9/oss-parent-9.pom (6.6 kB at 346 kB/s)
2026-01-22T16:06:50.0254646Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.pom
2026-01-22T16:06:50.0415762Z Progress (1): 1.0 kB
2026-01-22T16:06:50.0422288Z Progress (1): 2.3 kB
2026-01-22T16:06:50.0422614Z                     
2026-01-22T16:06:50.0423350Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.pom (2.3 kB at 120 kB/s)
2026-01-22T16:06:50.0495863Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.pom
2026-01-22T16:06:50.0634852Z Progress (1): 1.0 kB
2026-01-22T16:06:50.0635720Z Progress (1): 3.7 kB
2026-01-22T16:06:50.0636216Z Progress (1): 4.3 kB
2026-01-22T16:06:50.0641047Z                     
2026-01-22T16:06:50.0646522Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.pom (4.3 kB at 268 kB/s)
2026-01-22T16:06:50.0705026Z Downloading from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.12.0/checker-qual-3.12.0.pom
2026-01-22T16:06:50.0865204Z Progress (1): 951 B
2026-01-22T16:06:50.0865566Z Progress (1): 2.1 kB
2026-01-22T16:06:50.0865839Z                     
2026-01-22T16:06:50.0866241Z Downloaded from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.12.0/checker-qual-3.12.0.pom (2.1 kB at 131 kB/s)
2026-01-22T16:06:50.0900072Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.7.1/error_prone_annotations-2.7.1.pom
2026-01-22T16:06:50.1038927Z Progress (1): 835 B
2026-01-22T16:06:50.1047803Z Progress (1): 2.1 kB
2026-01-22T16:06:50.1051705Z                     
2026-01-22T16:06:50.1054668Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.7.1/error_prone_annotations-2.7.1.pom (2.1 kB at 132 kB/s)
2026-01-22T16:06:50.1085639Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.7.1/error_prone_parent-2.7.1.pom
2026-01-22T16:06:50.1254605Z Progress (1): 743 B
2026-01-22T16:06:50.1255504Z Progress (1): 2.4 kB
2026-01-22T16:06:50.1256445Z Progress (1): 4.9 kB
2026-01-22T16:06:50.1256796Z Progress (1): 7.0 kB
2026-01-22T16:06:50.1257097Z                     
2026-01-22T16:06:50.1257534Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.7.1/error_prone_parent-2.7.1.pom (7.0 kB at 410 kB/s)
2026-01-22T16:06:50.1302916Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/1.3/j2objc-annotations-1.3.pom
2026-01-22T16:06:50.1479762Z Progress (1): 857 B
2026-01-22T16:06:50.1485354Z Progress (1): 2.8 kB
2026-01-22T16:06:50.1490320Z                     
2026-01-22T16:06:50.1491121Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/1.3/j2objc-annotations-1.3.pom (2.8 kB at 145 kB/s)
2026-01-22T16:06:50.1574567Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/31.1-jre/guava-31.1-jre.pom
2026-01-22T16:06:50.1720212Z Progress (1): 1.0 kB
2026-01-22T16:06:50.1728008Z Progress (1): 2.9 kB
2026-01-22T16:06:50.1734629Z Progress (1): 4.9 kB
2026-01-22T16:06:50.1735391Z Progress (1): 6.8 kB
2026-01-22T16:06:50.1736179Z Progress (1): 8.5 kB
2026-01-22T16:06:50.1736966Z Progress (1): 11 kB 
2026-01-22T16:06:50.1753568Z                    
2026-01-22T16:06:50.1754306Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/31.1-jre/guava-31.1-jre.pom (11 kB at 578 kB/s)
2026-01-22T16:06:50.1795299Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/31.1-jre/guava-parent-31.1-jre.pom
2026-01-22T16:06:50.1968192Z Progress (1): 913 B
2026-01-22T16:06:50.1968726Z Progress (1): 2.7 kB
2026-01-22T16:06:50.1969190Z Progress (1): 5.2 kB
2026-01-22T16:06:50.1969607Z Progress (1): 7.8 kB
2026-01-22T16:06:50.1970320Z Progress (1): 9.4 kB
2026-01-22T16:06:50.1971055Z Progress (1): 14 kB 
2026-01-22T16:06:50.1973459Z Progress (1): 15 kB
2026-01-22T16:06:50.1994751Z                    
2026-01-22T16:06:50.1995791Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/31.1-jre/guava-parent-31.1-jre.pom (15 kB at 776 kB/s)
2026-01-22T16:06:50.2050167Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.11.0/error_prone_annotations-2.11.0.pom
2026-01-22T16:06:50.2215444Z Progress (1): 835 B
2026-01-22T16:06:50.2220394Z Progress (1): 2.2 kB
2026-01-22T16:06:50.2220992Z                     
2026-01-22T16:06:50.2221709Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.11.0/error_prone_annotations-2.11.0.pom (2.2 kB at 120 kB/s)
2026-01-22T16:06:50.2259312Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.11.0/error_prone_parent-2.11.0.pom
2026-01-22T16:06:50.2438037Z Progress (1): 724 B
2026-01-22T16:06:50.2440702Z Progress (1): 2.2 kB
2026-01-22T16:06:50.2442420Z Progress (1): 4.2 kB
2026-01-22T16:06:50.2446811Z Progress (1): 8.4 kB
2026-01-22T16:06:50.2449329Z Progress (1): 11 kB 
2026-01-22T16:06:50.2450056Z                    
2026-01-22T16:06:50.2451789Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.11.0/error_prone_parent-2.11.0.pom (11 kB at 565 kB/s)
2026-01-22T16:06:50.2500749Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.91.Final/netty-buffer-4.1.91.Final.pom
2026-01-22T16:06:50.2679503Z Progress (1): 885 B
2026-01-22T16:06:50.2688105Z Progress (1): 1.6 kB
2026-01-22T16:06:50.2688460Z                     
2026-01-22T16:06:50.2688896Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.91.Final/netty-buffer-4.1.91.Final.pom (1.6 kB at 83 kB/s)
2026-01-22T16:06:50.2722362Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.91.Final/netty-parent-4.1.91.Final.pom
2026-01-22T16:06:50.2938854Z Progress (1): 718 B
2026-01-22T16:06:50.2939498Z Progress (1): 2.1 kB
2026-01-22T16:06:50.2940109Z Progress (1): 4.2 kB
2026-01-22T16:06:50.2940660Z Progress (1): 7.0 kB
2026-01-22T16:06:50.2941163Z Progress (1): 8.5 kB
2026-01-22T16:06:50.2941708Z Progress (1): 19 kB 
2026-01-22T16:06:50.2942237Z Progress (1): 22 kB
2026-01-22T16:06:50.2942966Z Progress (1): 24 kB
2026-01-22T16:06:50.2943505Z Progress (1): 26 kB
2026-01-22T16:06:50.2944021Z Progress (1): 29 kB
2026-01-22T16:06:50.2944523Z Progress (1): 32 kB
2026-01-22T16:06:50.2945122Z Progress (1): 36 kB
2026-01-22T16:06:50.2945666Z Progress (1): 41 kB
2026-01-22T16:06:50.2946324Z Progress (1): 44 kB
2026-01-22T16:06:50.2946939Z Progress (1): 47 kB
2026-01-22T16:06:50.2947496Z Progress (1): 47 kB
2026-01-22T16:06:50.2947969Z Progress (1): 51 kB
2026-01-22T16:06:50.2948497Z Progress (1): 53 kB
2026-01-22T16:06:50.2949315Z Progress (1): 56 kB
2026-01-22T16:06:50.2950140Z Progress (1): 59 kB
2026-01-22T16:06:50.2950651Z Progress (1): 61 kB
2026-01-22T16:06:50.2951123Z Progress (1): 64 kB
2026-01-22T16:06:50.2951668Z Progress (1): 66 kB
2026-01-22T16:06:50.2952201Z Progress (1): 68 kB
2026-01-22T16:06:50.2952941Z Progress (1): 72 kB
2026-01-22T16:06:50.2953538Z Progress (1): 75 kB
2026-01-22T16:06:50.2954105Z Progress (1): 81 kB
2026-01-22T16:06:50.2954600Z Progress (1): 83 kB
2026-01-22T16:06:50.2955185Z                    
2026-01-22T16:06:50.2955861Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.91.Final/netty-parent-4.1.91.Final.pom (83 kB at 3.8 MB/s)
2026-01-22T16:06:50.3133704Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.91.Final/netty-common-4.1.91.Final.pom
2026-01-22T16:06:50.3301519Z Progress (1): 1.3 kB
2026-01-22T16:06:50.3305456Z Progress (1): 4.5 kB
2026-01-22T16:06:50.3307360Z Progress (1): 10 kB 
2026-01-22T16:06:50.3317051Z Progress (1): 12 kB
2026-01-22T16:06:50.3318618Z                    
2026-01-22T16:06:50.3320861Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.91.Final/netty-common-4.1.91.Final.pom (12 kB at 589 kB/s)
2026-01-22T16:06:50.3465808Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.91.Final/netty-codec-http-4.1.91.Final.pom
2026-01-22T16:06:50.3734543Z Progress (1): 810 B
2026-01-22T16:06:50.3743211Z Progress (1): 4.2 kB
2026-01-22T16:06:50.3744211Z Progress (1): 4.2 kB
2026-01-22T16:06:50.3745187Z                     
2026-01-22T16:06:50.3745968Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.91.Final/netty-codec-http-4.1.91.Final.pom (4.2 kB at 150 kB/s)
2026-01-22T16:06:50.3864611Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.91.Final/netty-transport-4.1.91.Final.pom
2026-01-22T16:06:50.4011905Z Progress (1): 859 B
2026-01-22T16:06:50.4053556Z Progress (1): 2.2 kB
2026-01-22T16:06:50.4054138Z                     
2026-01-22T16:06:50.4054834Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.91.Final/netty-transport-4.1.91.Final.pom (2.2 kB at 114 kB/s)
2026-01-22T16:06:50.4175369Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.91.Final/netty-resolver-4.1.91.Final.pom
2026-01-22T16:06:50.4332548Z Progress (1): 885 B
2026-01-22T16:06:50.4345547Z Progress (1): 1.6 kB
2026-01-22T16:06:50.4357331Z                     
2026-01-22T16:06:50.4403639Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.91.Final/netty-resolver-4.1.91.Final.pom (1.6 kB at 79 kB/s)
2026-01-22T16:06:50.4485304Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.91.Final/netty-codec-4.1.91.Final.pom
2026-01-22T16:06:50.4651172Z Progress (1): 807 B
2026-01-22T16:06:50.4657593Z Progress (1): 4.3 kB
2026-01-22T16:06:50.4670897Z Progress (1): 5.3 kB
2026-01-22T16:06:50.4678171Z                     
2026-01-22T16:06:50.4682176Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.91.Final/netty-codec-4.1.91.Final.pom (5.3 kB at 241 kB/s)
2026-01-22T16:06:50.4799575Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.91.Final/netty-handler-4.1.91.Final.pom
2026-01-22T16:06:50.5011068Z Progress (1): 801 B
2026-01-22T16:06:50.5015856Z Progress (1): 3.9 kB
2026-01-22T16:06:50.5021950Z Progress (1): 4.6 kB
2026-01-22T16:06:50.5039197Z                     
2026-01-22T16:06:50.5039879Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.91.Final/netty-handler-4.1.91.Final.pom (4.6 kB at 192 kB/s)
2026-01-22T16:06:50.5158603Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.91.Final/netty-transport-native-unix-common-4.1.91.Final.pom
2026-01-22T16:06:50.5373827Z Progress (1): 767 B
2026-01-22T16:06:50.5374570Z Progress (1): 2.2 kB
2026-01-22T16:06:50.5375189Z Progress (1): 4.5 kB
2026-01-22T16:06:50.5375824Z Progress (1): 6.8 kB
2026-01-22T16:06:50.5376331Z Progress (1): 18 kB 
2026-01-22T16:06:50.5376836Z Progress (1): 29 kB
2026-01-22T16:06:50.5377339Z                    
2026-01-22T16:06:50.5378045Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.91.Final/netty-transport-native-unix-common-4.1.91.Final.pom (29 kB at 1.5 MB/s)
2026-01-22T16:06:50.5425338Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.91.Final/netty-transport-classes-epoll-4.1.91.Final.pom
2026-01-22T16:06:50.5615828Z Progress (1): 850 B
2026-01-22T16:06:50.5622177Z Progress (1): 2.1 kB
2026-01-22T16:06:50.5628086Z                     
2026-01-22T16:06:50.5629767Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.91.Final/netty-transport-classes-epoll-4.1.91.Final.pom (2.1 kB at 107 kB/s)
2026-01-22T16:06:50.5703835Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.91.Final/netty-transport-classes-kqueue-4.1.91.Final.pom
2026-01-22T16:06:50.5933944Z Progress (1): 859 B
2026-01-22T16:06:50.5964455Z Progress (1): 2.1 kB
2026-01-22T16:06:50.5964980Z                     
2026-01-22T16:06:50.5965563Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.91.Final/netty-transport-classes-kqueue-4.1.91.Final.pom (2.1 kB at 82 kB/s)
2026-01-22T16:06:50.6020240Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.91.Final/netty-transport-native-epoll-4.1.91.Final.pom
2026-01-22T16:06:50.6220008Z Progress (1): 766 B
2026-01-22T16:06:50.6220508Z Progress (1): 2.1 kB
2026-01-22T16:06:50.6220928Z Progress (1): 3.4 kB
2026-01-22T16:06:50.6221364Z Progress (1): 6.1 kB
2026-01-22T16:06:50.6221762Z Progress (1): 9.0 kB
2026-01-22T16:06:50.6222172Z Progress (1): 18 kB 
2026-01-22T16:06:50.6222566Z Progress (1): 19 kB
2026-01-22T16:06:50.6223331Z                    
2026-01-22T16:06:50.6223901Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.91.Final/netty-transport-native-epoll-4.1.91.Final.pom (19 kB at 914 kB/s)
2026-01-22T16:06:50.6344683Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.91.Final/netty-transport-native-kqueue-4.1.91.Final.pom
2026-01-22T16:06:50.6535760Z Progress (1): 752 B
2026-01-22T16:06:50.6552561Z Progress (1): 2.1 kB
2026-01-22T16:06:50.6566530Z Progress (1): 3.9 kB
2026-01-22T16:06:50.6566995Z Progress (1): 6.2 kB
2026-01-22T16:06:50.6567401Z Progress (1): 19 kB 
2026-01-22T16:06:50.6567791Z Progress (1): 29 kB
2026-01-22T16:06:50.6570321Z Progress (1): 30 kB
2026-01-22T16:06:50.6572347Z                    
2026-01-22T16:06:50.6574375Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.91.Final/netty-transport-native-kqueue-4.1.91.Final.pom (30 kB at 1.2 MB/s)
2026-01-22T16:06:50.6735471Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.25.0/opentelemetry-api-1.25.0.pom
2026-01-22T16:06:50.6890819Z Progress (1): 1.0 kB
2026-01-22T16:06:50.6899834Z Progress (1): 1.8 kB
2026-01-22T16:06:50.6900880Z                     
2026-01-22T16:06:50.6901923Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.25.0/opentelemetry-api-1.25.0.pom (1.8 kB at 89 kB/s)
2026-01-22T16:06:50.6933869Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.25.0/opentelemetry-context-1.25.0.pom
2026-01-22T16:06:50.7124046Z Progress (1): 989 B
2026-01-22T16:06:50.7133078Z Progress (1): 1.6 kB
2026-01-22T16:06:50.7135601Z                     
2026-01-22T16:06:50.7137305Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.25.0/opentelemetry-context-1.25.0.pom (1.6 kB at 79 kB/s)
2026-01-22T16:06:50.7174826Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.25.0/opentelemetry-exporter-logging-1.25.0.pom
2026-01-22T16:06:50.7376323Z Progress (1): 988 B
2026-01-22T16:06:50.7387229Z Progress (1): 2.4 kB
2026-01-22T16:06:50.7387950Z                     
2026-01-22T16:06:50.7388624Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.25.0/opentelemetry-exporter-logging-1.25.0.pom (2.4 kB at 110 kB/s)
2026-01-22T16:06:50.7416758Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.25.0/opentelemetry-sdk-1.25.0.pom
2026-01-22T16:06:50.7649015Z Progress (1): 994 B
2026-01-22T16:06:50.7655811Z Progress (1): 2.6 kB
2026-01-22T16:06:50.7657268Z                     
2026-01-22T16:06:50.7657732Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.25.0/opentelemetry-sdk-1.25.0.pom (2.6 kB at 106 kB/s)
2026-01-22T16:06:50.7704145Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.25.0/opentelemetry-sdk-common-1.25.0.pom
2026-01-22T16:06:50.7857770Z Progress (1): 995 B
2026-01-22T16:06:50.7864956Z Progress (1): 2.0 kB
2026-01-22T16:06:50.7866232Z                     
2026-01-22T16:06:50.7866698Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.25.0/opentelemetry-sdk-common-1.25.0.pom (2.0 kB at 105 kB/s)
2026-01-22T16:06:50.7905266Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.25.0-alpha/opentelemetry-semconv-1.25.0-alpha.pom
2026-01-22T16:06:50.8071698Z Progress (1): 985 B
2026-01-22T16:06:50.8085337Z Progress (1): 1.8 kB
2026-01-22T16:06:50.8086560Z                     
2026-01-22T16:06:50.8087019Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.25.0-alpha/opentelemetry-semconv-1.25.0-alpha.pom (1.8 kB at 100 kB/s)
2026-01-22T16:06:50.8114190Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.25.0/opentelemetry-sdk-trace-1.25.0.pom
2026-01-22T16:06:50.8299066Z Progress (1): 977 B
2026-01-22T16:06:50.8299611Z Progress (1): 2.2 kB
2026-01-22T16:06:50.8300814Z                     
2026-01-22T16:06:50.8301271Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.25.0/opentelemetry-sdk-trace-1.25.0.pom (2.2 kB at 115 kB/s)
2026-01-22T16:06:50.8332433Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.25.0/opentelemetry-sdk-metrics-1.25.0.pom
2026-01-22T16:06:50.8509799Z Progress (1): 997 B
2026-01-22T16:06:50.8520349Z Progress (1): 2.0 kB
2026-01-22T16:06:50.8520824Z                     
2026-01-22T16:06:50.8521380Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.25.0/opentelemetry-sdk-metrics-1.25.0.pom (2.0 kB at 104 kB/s)
2026-01-22T16:06:50.8552105Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.25.0-alpha/opentelemetry-sdk-logs-1.25.0-alpha.pom
2026-01-22T16:06:50.8756689Z Progress (1): 975 B
2026-01-22T16:06:50.8757020Z Progress (1): 2.2 kB
2026-01-22T16:06:50.8757314Z                     
2026-01-22T16:06:50.8757774Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.25.0-alpha/opentelemetry-sdk-logs-1.25.0-alpha.pom (2.2 kB at 110 kB/s)
2026-01-22T16:06:50.8786796Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-logs/1.25.0-alpha/opentelemetry-api-logs-1.25.0-alpha.pom
2026-01-22T16:06:50.8957340Z Progress (1): 985 B
2026-01-22T16:06:50.8959481Z Progress (1): 1.8 kB
2026-01-22T16:06:50.8959953Z                     
2026-01-22T16:06:50.8960537Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-logs/1.25.0-alpha/opentelemetry-api-logs-1.25.0-alpha.pom (1.8 kB at 100 kB/s)
2026-01-22T16:06:50.8991705Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.25.0-alpha/opentelemetry-api-events-1.25.0-alpha.pom
2026-01-22T16:06:50.9184153Z Progress (1): 989 B
2026-01-22T16:06:50.9184798Z Progress (1): 1.8 kB
2026-01-22T16:06:50.9185315Z                     
2026-01-22T16:06:50.9185942Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.25.0-alpha/opentelemetry-api-events-1.25.0-alpha.pom (1.8 kB at 90 kB/s)
2026-01-22T16:06:50.9211949Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.25.0/opentelemetry-sdk-extension-autoconfigure-spi-1.25.0.pom
2026-01-22T16:06:50.9390936Z Progress (1): 964 B
2026-01-22T16:06:50.9404562Z Progress (1): 2.2 kB
2026-01-22T16:06:50.9405107Z                     
2026-01-22T16:06:50.9405714Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.25.0/opentelemetry-sdk-extension-autoconfigure-spi-1.25.0.pom (2.2 kB at 117 kB/s)
2026-01-22T16:06:50.9431691Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.25.0-alpha/opentelemetry-sdk-extension-autoconfigure-1.25.0-alpha.pom
2026-01-22T16:06:50.9601404Z Progress (1): 962 B
2026-01-22T16:06:50.9607552Z Progress (1): 2.6 kB
2026-01-22T16:06:50.9611728Z                     
2026-01-22T16:06:50.9612627Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.25.0-alpha/opentelemetry-sdk-extension-autoconfigure-1.25.0-alpha.pom (2.6 kB at 146 kB/s)
2026-01-22T16:06:50.9643423Z Downloading from central: https://repo.maven.apache.org/maven2/io/ous/jtoml/2.0.0/jtoml-2.0.0.pom
2026-01-22T16:06:50.9805409Z Progress (1): 1.3 kB
2026-01-22T16:06:50.9833499Z Progress (1): 4.0 kB
2026-01-22T16:06:50.9835536Z                     
2026-01-22T16:06:50.9835937Z Downloaded from central: https://repo.maven.apache.org/maven2/io/ous/jtoml/2.0.0/jtoml-2.0.0.pom (4.0 kB at 220 kB/s)
2026-01-22T16:06:50.9853457Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.4/byte-buddy-1.14.4.pom
2026-01-22T16:06:51.0032624Z Progress (1): 958 B
2026-01-22T16:06:51.0033622Z Progress (1): 3.7 kB
2026-01-22T16:06:51.0035500Z Progress (1): 7.0 kB
2026-01-22T16:06:51.0035835Z Progress (1): 14 kB 
2026-01-22T16:06:51.0039029Z Progress (1): 16 kB
2026-01-22T16:06:51.0041571Z                    
2026-01-22T16:06:51.0042026Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.4/byte-buddy-1.14.4.pom (16 kB at 833 kB/s)
2026-01-22T16:06:51.0088469Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.14.4/byte-buddy-parent-1.14.4.pom
2026-01-22T16:06:51.0264596Z Progress (1): 832 B
2026-01-22T16:06:51.0265323Z Progress (1): 2.1 kB
2026-01-22T16:06:51.0266573Z Progress (1): 3.6 kB
2026-01-22T16:06:51.0266937Z Progress (1): 6.2 kB
2026-01-22T16:06:51.0270697Z Progress (1): 8.1 kB
2026-01-22T16:06:51.0271090Z Progress (1): 11 kB 
2026-01-22T16:06:51.0271440Z Progress (1): 13 kB
2026-01-22T16:06:51.0271766Z Progress (1): 17 kB
2026-01-22T16:06:51.0272101Z Progress (1): 22 kB
2026-01-22T16:06:51.0272417Z Progress (1): 25 kB
2026-01-22T16:06:51.0272927Z Progress (1): 36 kB
2026-01-22T16:06:51.0273257Z Progress (1): 45 kB
2026-01-22T16:06:51.0273565Z Progress (1): 50 kB
2026-01-22T16:06:51.0273872Z Progress (1): 55 kB
2026-01-22T16:06:51.0278928Z Progress (1): 58 kB
2026-01-22T16:06:51.0282221Z                    
2026-01-22T16:06:51.0282689Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.14.4/byte-buddy-parent-1.14.4.pom (58 kB at 2.9 MB/s)
2026-01-22T16:06:51.0375326Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-exec/1.3/commons-exec-1.3.pom
2026-01-22T16:06:51.0585095Z Progress (1): 778 B
2026-01-22T16:06:51.0585834Z Progress (1): 2.3 kB
2026-01-22T16:06:51.0586537Z Progress (1): 5.2 kB
2026-01-22T16:06:51.0593408Z Progress (1): 7.7 kB
2026-01-22T16:06:51.0594068Z Progress (1): 10 kB 
2026-01-22T16:06:51.0594677Z Progress (1): 11 kB
2026-01-22T16:06:51.0595259Z                    
2026-01-22T16:06:51.0595982Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-exec/1.3/commons-exec-1.3.pom (11 kB at 478 kB/s)
2026-01-22T16:06:51.0667937Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/35/commons-parent-35.pom
2026-01-22T16:06:51.0883731Z Progress (1): 715 B
2026-01-22T16:06:51.0889495Z Progress (1): 2.0 kB
2026-01-22T16:06:51.0892476Z Progress (1): 3.3 kB
2026-01-22T16:06:51.0895275Z Progress (1): 4.8 kB
2026-01-22T16:06:51.0896977Z Progress (1): 8.2 kB
2026-01-22T16:06:51.0899106Z Progress (1): 11 kB 
2026-01-22T16:06:51.0901439Z Progress (1): 15 kB
2026-01-22T16:06:51.0901783Z Progress (1): 18 kB
2026-01-22T16:06:51.0902396Z Progress (1): 21 kB
2026-01-22T16:06:51.0903377Z Progress (1): 24 kB
2026-01-22T16:06:51.0905031Z Progress (1): 26 kB
2026-01-22T16:06:51.0906353Z Progress (1): 30 kB
2026-01-22T16:06:51.0907044Z Progress (1): 32 kB
2026-01-22T16:06:51.0909066Z Progress (1): 36 kB
2026-01-22T16:06:51.0909777Z Progress (1): 41 kB
2026-01-22T16:06:51.0912382Z Progress (1): 42 kB
2026-01-22T16:06:51.0912691Z Progress (1): 46 kB
2026-01-22T16:06:51.0913195Z Progress (1): 48 kB
2026-01-22T16:06:51.0913440Z Progress (1): 51 kB
2026-01-22T16:06:51.0913672Z Progress (1): 53 kB
2026-01-22T16:06:51.0913945Z Progress (1): 56 kB
2026-01-22T16:06:51.0914203Z Progress (1): 57 kB
2026-01-22T16:06:51.0918256Z Progress (1): 58 kB
2026-01-22T16:06:51.0918485Z                    
2026-01-22T16:06:51.0918811Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/35/commons-parent-35.pom (58 kB at 2.2 MB/s)
2026-01-22T16:06:51.0981111Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/15/apache-15.pom
2026-01-22T16:06:51.1149446Z Progress (1): 749 B
2026-01-22T16:06:51.1151191Z Progress (1): 2.1 kB
2026-01-22T16:06:51.1151798Z Progress (1): 3.9 kB
2026-01-22T16:06:51.1159049Z Progress (1): 7.8 kB
2026-01-22T16:06:51.1159409Z Progress (1): 11 kB 
2026-01-22T16:06:51.1160381Z Progress (1): 14 kB
2026-01-22T16:06:51.1160668Z Progress (1): 15 kB
2026-01-22T16:06:51.1160952Z                    
2026-01-22T16:06:51.1161314Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/15/apache-15.pom (15 kB at 896 kB/s)
2026-01-22T16:06:51.1208001Z Downloading from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client/2.12.3/async-http-client-2.12.3.pom
2026-01-22T16:06:51.1385653Z Progress (1): 1.7 kB
2026-01-22T16:06:51.1391689Z Progress (1): 2.7 kB
2026-01-22T16:06:51.1392025Z                     
2026-01-22T16:06:51.1392471Z Downloaded from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client/2.12.3/async-http-client-2.12.3.pom (2.7 kB at 159 kB/s)
2026-01-22T16:06:51.1407875Z Downloading from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-project/2.12.3/async-http-client-project-2.12.3.pom
2026-01-22T16:06:51.1575602Z Progress (1): 910 B
2026-01-22T16:06:51.1582246Z Progress (1): 2.8 kB
2026-01-22T16:06:51.1584309Z Progress (1): 5.6 kB
2026-01-22T16:06:51.1603511Z Progress (1): 8.3 kB
2026-01-22T16:06:51.1604267Z Progress (1): 13 kB 
2026-01-22T16:06:51.1604887Z Progress (1): 16 kB
2026-01-22T16:06:51.1605429Z                    
2026-01-22T16:06:51.1606076Z Downloaded from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-project/2.12.3/async-http-client-project-2.12.3.pom (16 kB at 861 kB/s)
2026-01-22T16:06:51.1656228Z Downloading from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-netty-utils/2.12.3/async-http-client-netty-utils-2.12.3.pom
2026-01-22T16:06:51.1843806Z Progress (1): 757 B
2026-01-22T16:06:51.1844446Z                    
2026-01-22T16:06:51.1845172Z Downloaded from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-netty-utils/2.12.3/async-http-client-netty-utils-2.12.3.pom (757 B at 40 kB/s)
2026-01-22T16:06:51.1904640Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.60.Final/netty-buffer-4.1.60.Final.pom
2026-01-22T16:06:51.2118642Z Progress (1): 885 B
2026-01-22T16:06:51.2122606Z Progress (1): 1.6 kB
2026-01-22T16:06:51.2127604Z                     
2026-01-22T16:06:51.2128067Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.60.Final/netty-buffer-4.1.60.Final.pom (1.6 kB at 72 kB/s)
2026-01-22T16:06:51.2155868Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.60.Final/netty-parent-4.1.60.Final.pom
2026-01-22T16:06:51.2328540Z Progress (1): 717 B
2026-01-22T16:06:51.2332087Z Progress (1): 2.1 kB
2026-01-22T16:06:51.2332419Z Progress (1): 3.7 kB
2026-01-22T16:06:51.2332913Z Progress (1): 11 kB 
2026-01-22T16:06:51.2333235Z Progress (1): 13 kB
2026-01-22T16:06:51.2333526Z Progress (1): 15 kB
2026-01-22T16:06:51.2333827Z Progress (1): 17 kB
2026-01-22T16:06:51.2334116Z Progress (1): 19 kB
2026-01-22T16:06:51.2334650Z Progress (1): 22 kB
2026-01-22T16:06:51.2334929Z Progress (1): 27 kB
2026-01-22T16:06:51.2335203Z Progress (1): 31 kB
2026-01-22T16:06:51.2335486Z Progress (1): 33 kB
2026-01-22T16:06:51.2335730Z Progress (1): 35 kB
2026-01-22T16:06:51.2336016Z Progress (1): 39 kB
2026-01-22T16:06:51.2336294Z Progress (1): 41 kB
2026-01-22T16:06:51.2336585Z Progress (1): 41 kB
2026-01-22T16:06:51.2336894Z Progress (1): 44 kB
2026-01-22T16:06:51.2337209Z Progress (1): 46 kB
2026-01-22T16:06:51.2337512Z Progress (1): 48 kB
2026-01-22T16:06:51.2337823Z Progress (1): 51 kB
2026-01-22T16:06:51.2367394Z Progress (1): 56 kB
2026-01-22T16:06:51.2367753Z Progress (1): 60 kB
2026-01-22T16:06:51.2368055Z Progress (1): 62 kB
2026-01-22T16:06:51.2368335Z                    
2026-01-22T16:06:51.2368735Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.60.Final/netty-parent-4.1.60.Final.pom (62 kB at 2.9 MB/s)
2026-01-22T16:06:51.2452101Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.60.Final/netty-common-4.1.60.Final.pom
2026-01-22T16:06:51.2664882Z Progress (1): 1.3 kB
2026-01-22T16:06:51.2667515Z Progress (1): 4.6 kB
2026-01-22T16:06:51.2678538Z Progress (1): 10 kB 
2026-01-22T16:06:51.2679251Z Progress (1): 12 kB
2026-01-22T16:06:51.2681377Z                    
2026-01-22T16:06:51.2682436Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.60.Final/netty-common-4.1.60.Final.pom (12 kB at 526 kB/s)
2026-01-22T16:06:51.2773044Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.pom
2026-01-22T16:06:51.2949517Z Progress (1): 1.0 kB
2026-01-22T16:06:51.2954649Z Progress (1): 3.3 kB
2026-01-22T16:06:51.2959158Z Progress (1): 3.8 kB
2026-01-22T16:06:51.2961675Z                     
2026-01-22T16:06:51.2965198Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.pom (3.8 kB at 202 kB/s)
2026-01-22T16:06:51.2995628Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.30/slf4j-parent-1.7.30.pom
2026-01-22T16:06:51.3172986Z Progress (1): 1.0 kB
2026-01-22T16:06:51.3176238Z Progress (1): 3.1 kB
2026-01-22T16:06:51.3176546Z Progress (1): 6.0 kB
2026-01-22T16:06:51.3176845Z Progress (1): 9.0 kB
2026-01-22T16:06:51.3177132Z Progress (1): 12 kB 
2026-01-22T16:06:51.3177456Z Progress (1): 14 kB
2026-01-22T16:06:51.3177741Z                    
2026-01-22T16:06:51.3178151Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.30/slf4j-parent-1.7.30.pom (14 kB at 767 kB/s)
2026-01-22T16:06:51.3222549Z Downloading from central: https://repo.maven.apache.org/maven2/com/sun/activation/jakarta.activation/1.2.2/jakarta.activation-1.2.2.pom
2026-01-22T16:06:51.3424809Z Progress (1): 885 B
2026-01-22T16:06:51.3431060Z Progress (1): 2.6 kB
2026-01-22T16:06:51.3433956Z Progress (1): 4.3 kB
2026-01-22T16:06:51.3436515Z Progress (1): 4.6 kB
2026-01-22T16:06:51.3439804Z                     
2026-01-22T16:06:51.3443613Z Downloaded from central: https://repo.maven.apache.org/maven2/com/sun/activation/jakarta.activation/1.2.2/jakarta.activation-1.2.2.pom (4.6 kB at 210 kB/s)
2026-01-22T16:06:51.3505005Z Downloading from central: https://repo.maven.apache.org/maven2/com/sun/activation/all/1.2.2/all-1.2.2.pom
2026-01-22T16:06:51.3669381Z Progress (1): 781 B
2026-01-22T16:06:51.3673517Z Progress (1): 2.8 kB
2026-01-22T16:06:51.3675354Z Progress (1): 4.3 kB
2026-01-22T16:06:51.3677063Z Progress (1): 6.0 kB
2026-01-22T16:06:51.3679349Z Progress (1): 8.2 kB
2026-01-22T16:06:51.3680954Z Progress (1): 11 kB 
2026-01-22T16:06:51.3682579Z Progress (1): 14 kB
2026-01-22T16:06:51.3684304Z Progress (1): 15 kB
2026-01-22T16:06:51.3684610Z                    
2026-01-22T16:06:51.3685010Z Downloaded from central: https://repo.maven.apache.org/maven2/com/sun/activation/all/1.2.2/all-1.2.2.pom (15 kB at 842 kB/s)
2026-01-22T16:06:51.3736039Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/ee4j/project/1.0.6/project-1.0.6.pom
2026-01-22T16:06:51.3910458Z Progress (1): 839 B
2026-01-22T16:06:51.3911802Z Progress (1): 2.5 kB
2026-01-22T16:06:51.3918441Z Progress (1): 5.0 kB
2026-01-22T16:06:51.3918862Z Progress (1): 7.6 kB
2026-01-22T16:06:51.3919737Z Progress (1): 12 kB 
2026-01-22T16:06:51.3933585Z Progress (1): 13 kB
2026-01-22T16:06:51.3934745Z                    
2026-01-22T16:06:51.3935160Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/ee4j/project/1.0.6/project-1.0.6.pom (13 kB at 667 kB/s)
2026-01-22T16:06:51.3979412Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.60.Final/netty-codec-http-4.1.60.Final.pom
2026-01-22T16:06:51.4143331Z Progress (1): 859 B
2026-01-22T16:06:51.4143908Z Progress (1): 2.4 kB
2026-01-22T16:06:51.4144367Z                     
2026-01-22T16:06:51.4145575Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.60.Final/netty-codec-http-4.1.60.Final.pom (2.4 kB at 134 kB/s)
2026-01-22T16:06:51.4219227Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.60.Final/netty-transport-4.1.60.Final.pom
2026-01-22T16:06:51.5591862Z Progress (1): 881 B
2026-01-22T16:06:51.5596509Z Progress (1): 1.9 kB
2026-01-22T16:06:51.5596833Z                     
2026-01-22T16:06:51.5597317Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.60.Final/netty-transport-4.1.60.Final.pom (1.9 kB at 14 kB/s)
2026-01-22T16:06:51.5698365Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.60.Final/netty-resolver-4.1.60.Final.pom
2026-01-22T16:06:51.5859054Z Progress (1): 884 B
2026-01-22T16:06:51.5860711Z Progress (1): 1.6 kB
2026-01-22T16:06:51.5862182Z                     
2026-01-22T16:06:51.5864104Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.60.Final/netty-resolver-4.1.60.Final.pom (1.6 kB at 88 kB/s)
2026-01-22T16:06:51.5923737Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.60.Final/netty-codec-4.1.60.Final.pom
2026-01-22T16:06:51.6059638Z Progress (1): 810 B
2026-01-22T16:06:51.6062201Z Progress (1): 3.6 kB
2026-01-22T16:06:51.6063615Z                     
2026-01-22T16:06:51.6065255Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.60.Final/netty-codec-4.1.60.Final.pom (3.6 kB at 239 kB/s)
2026-01-22T16:06:51.6134633Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.60.Final/netty-handler-4.1.60.Final.pom
2026-01-22T16:06:51.6272364Z Progress (1): 807 B
2026-01-22T16:06:51.6273063Z Progress (1): 3.4 kB
2026-01-22T16:06:51.6282281Z Progress (1): 3.6 kB
2026-01-22T16:06:51.6283083Z                     
2026-01-22T16:06:51.6283690Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.60.Final/netty-handler-4.1.60.Final.pom (3.6 kB at 198 kB/s)
2026-01-22T16:06:51.6364469Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-socks/4.1.60.Final/netty-codec-socks-4.1.60.Final.pom
2026-01-22T16:06:51.6533288Z Progress (1): 882 B
2026-01-22T16:06:51.6545535Z Progress (1): 2.0 kB
2026-01-22T16:06:51.6557827Z                     
2026-01-22T16:06:51.6558581Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-socks/4.1.60.Final/netty-codec-socks-4.1.60.Final.pom (2.0 kB at 99 kB/s)
2026-01-22T16:06:51.6628368Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler-proxy/4.1.60.Final/netty-handler-proxy-4.1.60.Final.pom
2026-01-22T16:06:51.6836157Z Progress (1): 850 B
2026-01-22T16:06:51.6836511Z Progress (1): 2.8 kB
2026-01-22T16:06:51.6836803Z                     
2026-01-22T16:06:51.6837246Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler-proxy/4.1.60.Final/netty-handler-proxy-4.1.60.Final.pom (2.8 kB at 147 kB/s)
2026-01-22T16:06:51.6873497Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.60.Final/netty-transport-native-epoll-4.1.60.Final.pom
2026-01-22T16:06:51.7038335Z Progress (1): 767 B
2026-01-22T16:06:51.7041948Z Progress (1): 2.1 kB
2026-01-22T16:06:51.7042294Z Progress (1): 3.7 kB
2026-01-22T16:06:51.7043241Z Progress (1): 6.4 kB
2026-01-22T16:06:51.7043603Z Progress (1): 9.0 kB
2026-01-22T16:06:51.7043932Z Progress (1): 18 kB 
2026-01-22T16:06:51.7049771Z Progress (1): 18 kB
2026-01-22T16:06:51.7053167Z                    
2026-01-22T16:06:51.7053891Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.60.Final/netty-transport-native-epoll-4.1.60.Final.pom (18 kB at 994 kB/s)
2026-01-22T16:06:51.7114635Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.60.Final/netty-transport-native-unix-common-4.1.60.Final.pom
2026-01-22T16:06:51.7256246Z Progress (1): 772 B
2026-01-22T16:06:51.7263656Z Progress (1): 2.2 kB
2026-01-22T16:06:51.7264308Z Progress (1): 4.5 kB
2026-01-22T16:06:51.7264934Z Progress (1): 6.9 kB
2026-01-22T16:06:51.7265434Z Progress (1): 18 kB 
2026-01-22T16:06:51.7265906Z Progress (1): 22 kB
2026-01-22T16:06:51.7266364Z                    
2026-01-22T16:06:51.7267007Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.60.Final/netty-transport-native-unix-common-4.1.60.Final.pom (22 kB at 1.3 MB/s)
2026-01-22T16:06:51.7360140Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.60.Final/netty-transport-native-kqueue-4.1.60.Final.pom
2026-01-22T16:06:51.7573559Z Progress (1): 767 B
2026-01-22T16:06:51.7577955Z Progress (1): 2.2 kB
2026-01-22T16:06:51.7580594Z Progress (1): 3.9 kB
2026-01-22T16:06:51.7582944Z Progress (1): 6.4 kB
2026-01-22T16:06:51.7583873Z Progress (1): 16 kB 
2026-01-22T16:06:51.7585859Z Progress (1): 19 kB
2026-01-22T16:06:51.7586179Z                    
2026-01-22T16:06:51.7586653Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.60.Final/netty-transport-native-kqueue-4.1.60.Final.pom (19 kB at 929 kB/s)
2026-01-22T16:06:51.7644402Z Downloading from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.3/reactive-streams-1.0.3.pom
2026-01-22T16:06:51.7834544Z Progress (1): 1.2 kB
2026-01-22T16:06:51.7835309Z                     
2026-01-22T16:06:51.7837373Z Downloaded from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.3/reactive-streams-1.0.3.pom (1.2 kB at 64 kB/s)
2026-01-22T16:06:51.7838349Z Downloading from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams/2.0.4/netty-reactive-streams-2.0.4.pom
2026-01-22T16:06:51.8044748Z Progress (1): 1.8 kB
2026-01-22T16:06:51.8049081Z Progress (1): 2.1 kB
2026-01-22T16:06:51.8053426Z                     
2026-01-22T16:06:51.8053918Z Downloaded from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams/2.0.4/netty-reactive-streams-2.0.4.pom (2.1 kB at 98 kB/s)
2026-01-22T16:06:51.8072010Z Downloading from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams-parent/2.0.4/netty-reactive-streams-parent-2.0.4.pom
2026-01-22T16:06:51.8256497Z Progress (1): 1.1 kB
2026-01-22T16:06:51.8264749Z Progress (1): 4.1 kB
2026-01-22T16:06:51.8265180Z Progress (1): 8.2 kB
2026-01-22T16:06:51.8269136Z Progress (1): 8.4 kB
2026-01-22T16:06:51.8269451Z                     
2026-01-22T16:06:51.8269908Z Downloaded from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams-parent/2.0.4/netty-reactive-streams-parent-2.0.4.pom (8.4 kB at 420 kB/s)
2026-01-22T16:06:51.8294427Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.43.Final/netty-handler-4.1.43.Final.pom
2026-01-22T16:06:51.8478739Z Progress (1): 814 B
2026-01-22T16:06:51.8480354Z Progress (1): 3.3 kB
2026-01-22T16:06:51.8480659Z Progress (1): 3.4 kB
2026-01-22T16:06:51.8480950Z                     
2026-01-22T16:06:51.8481362Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.43.Final/netty-handler-4.1.43.Final.pom (3.4 kB at 178 kB/s)
2026-01-22T16:06:51.8496152Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.43.Final/netty-parent-4.1.43.Final.pom
2026-01-22T16:06:51.8702675Z Progress (1): 733 B
2026-01-22T16:06:51.8707369Z Progress (1): 2.1 kB
2026-01-22T16:06:51.8716015Z Progress (1): 3.7 kB
2026-01-22T16:06:51.8716335Z Progress (1): 8.5 kB
2026-01-22T16:06:51.8716625Z Progress (1): 10 kB 
2026-01-22T16:06:51.8716913Z Progress (1): 12 kB
2026-01-22T16:06:51.8717194Z Progress (1): 14 kB
2026-01-22T16:06:51.8717484Z Progress (1): 17 kB
2026-01-22T16:06:51.8717768Z Progress (1): 20 kB
2026-01-22T16:06:51.8718044Z Progress (1): 25 kB
2026-01-22T16:06:51.8718391Z Progress (1): 27 kB
2026-01-22T16:06:51.8718703Z Progress (1): 29 kB
2026-01-22T16:06:51.8719025Z Progress (1): 32 kB
2026-01-22T16:06:51.8719334Z Progress (1): 35 kB
2026-01-22T16:06:51.8719657Z Progress (1): 37 kB
2026-01-22T16:06:51.8723147Z Progress (1): 37 kB
2026-01-22T16:06:51.8724054Z Progress (1): 39 kB
2026-01-22T16:06:51.8724932Z Progress (1): 42 kB
2026-01-22T16:06:51.8726029Z Progress (1): 45 kB
2026-01-22T16:06:51.8726550Z Progress (1): 48 kB
2026-01-22T16:06:51.8726983Z Progress (1): 54 kB
2026-01-22T16:06:51.8728741Z Progress (1): 56 kB
2026-01-22T16:06:51.8729211Z                    
2026-01-22T16:06:51.8729744Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.43.Final/netty-parent-4.1.43.Final.pom (56 kB at 2.6 MB/s)
2026-01-22T16:06:51.8781697Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.43.Final/netty-common-4.1.43.Final.pom
2026-01-22T16:06:51.9010533Z Progress (1): 1.4 kB
2026-01-22T16:06:51.9016017Z Progress (1): 4.8 kB
2026-01-22T16:06:51.9017786Z Progress (1): 9.8 kB
2026-01-22T16:06:51.9019491Z Progress (1): 10 kB 
2026-01-22T16:06:51.9021145Z                    
2026-01-22T16:06:51.9023096Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.43.Final/netty-common-4.1.43.Final.pom (10 kB at 437 kB/s)
2026-01-22T16:06:51.9103518Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.43.Final/netty-buffer-4.1.43.Final.pom
2026-01-22T16:06:51.9275629Z Progress (1): 888 B
2026-01-22T16:06:51.9305161Z Progress (1): 1.6 kB
2026-01-22T16:06:51.9309288Z                     
2026-01-22T16:06:51.9313395Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.43.Final/netty-buffer-4.1.43.Final.pom (1.6 kB at 72 kB/s)
2026-01-22T16:06:51.9388059Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.43.Final/netty-transport-4.1.43.Final.pom
2026-01-22T16:06:51.9565449Z Progress (1): 882 B
2026-01-22T16:06:51.9569811Z Progress (1): 1.9 kB
2026-01-22T16:06:51.9571675Z                     
2026-01-22T16:06:51.9574762Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.43.Final/netty-transport-4.1.43.Final.pom (1.9 kB at 101 kB/s)
2026-01-22T16:06:51.9620889Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.43.Final/netty-resolver-4.1.43.Final.pom
2026-01-22T16:06:51.9803794Z Progress (1): 888 B
2026-01-22T16:06:51.9815608Z Progress (1): 1.6 kB
2026-01-22T16:06:51.9815917Z                     
2026-01-22T16:06:51.9816321Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.43.Final/netty-resolver-4.1.43.Final.pom (1.6 kB at 79 kB/s)
2026-01-22T16:06:51.9899062Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.43.Final/netty-codec-4.1.43.Final.pom
2026-01-22T16:06:52.0100022Z Progress (1): 814 B
2026-01-22T16:06:52.0110574Z Progress (1): 3.6 kB
2026-01-22T16:06:52.0112086Z                     
2026-01-22T16:06:52.0113972Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.43.Final/netty-codec-4.1.43.Final.pom (3.6 kB at 163 kB/s)
2026-01-22T16:06:52.0184392Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.9.1/selenium-http-4.9.1.pom
2026-01-22T16:06:52.0393847Z Progress (1): 1.1 kB
2026-01-22T16:06:52.0413714Z Progress (1): 2.8 kB
2026-01-22T16:06:52.0414409Z                     
2026-01-22T16:06:52.0415047Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.9.1/selenium-http-4.9.1.pom (2.8 kB at 140 kB/s)
2026-01-22T16:06:52.0426083Z Downloading from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.1/failsafe-3.3.1.pom
2026-01-22T16:06:52.0700328Z Progress (1): 1.0 kB
2026-01-22T16:06:52.0704723Z                     
2026-01-22T16:06:52.0705424Z Downloaded from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.1/failsafe-3.3.1.pom (1.0 kB at 37 kB/s)
2026-01-22T16:06:52.0734678Z Downloading from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe-parent/3.3.1/failsafe-parent-3.3.1.pom
2026-01-22T16:06:52.0940570Z Progress (1): 1.1 kB
2026-01-22T16:06:52.0944712Z Progress (1): 3.4 kB
2026-01-22T16:06:52.0950275Z Progress (1): 5.8 kB
2026-01-22T16:06:52.0954241Z Progress (1): 8.7 kB
2026-01-22T16:06:52.1013580Z Progress (1): 9.2 kB
2026-01-22T16:06:52.1014167Z                     
2026-01-22T16:06:52.1014811Z Downloaded from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe-parent/3.3.1/failsafe-parent-3.3.1.pom (9.2 kB at 399 kB/s)
2026-01-22T16:06:52.1039153Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.9.1/selenium-json-4.9.1.pom
2026-01-22T16:06:52.1240026Z Progress (1): 1.1 kB
2026-01-22T16:06:52.1251028Z Progress (1): 2.3 kB
2026-01-22T16:06:52.1255682Z                     
2026-01-22T16:06:52.1259402Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.9.1/selenium-json-4.9.1.pom (2.3 kB at 103 kB/s)
2026-01-22T16:06:52.1315519Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.9.1/selenium-manager-4.9.1.pom
2026-01-22T16:06:52.1479850Z Progress (1): 1.1 kB
2026-01-22T16:06:52.1484568Z Progress (1): 2.6 kB
2026-01-22T16:06:52.1485303Z                     
2026-01-22T16:06:52.1492131Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.9.1/selenium-manager-4.9.1.pom (2.6 kB at 146 kB/s)
2026-01-22T16:06:52.1554645Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.10.0/selenium-remote-driver-4.10.0.pom
2026-01-22T16:06:52.1750872Z Progress (1): 1.0 kB
2026-01-22T16:06:52.1751224Z Progress (1): 6.9 kB
2026-01-22T16:06:52.1751567Z Progress (1): 8.1 kB
2026-01-22T16:06:52.1751851Z                     
2026-01-22T16:06:52.1752303Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.10.0/selenium-remote-driver-4.10.0.pom (8.1 kB at 385 kB/s)
2026-01-22T16:06:52.1773340Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.92.Final/netty-buffer-4.1.92.Final.pom
2026-01-22T16:06:52.1933373Z Progress (1): 885 B
2026-01-22T16:06:52.1954567Z Progress (1): 1.6 kB
2026-01-22T16:06:52.1956929Z                     
2026-01-22T16:06:52.1957724Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.92.Final/netty-buffer-4.1.92.Final.pom (1.6 kB at 93 kB/s)
2026-01-22T16:06:52.1961622Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.92.Final/netty-parent-4.1.92.Final.pom
2026-01-22T16:06:52.2165440Z Progress (1): 717 B
2026-01-22T16:06:52.2168858Z Progress (1): 2.1 kB
2026-01-22T16:06:52.2171536Z Progress (1): 4.2 kB
2026-01-22T16:06:52.2171852Z Progress (1): 7.0 kB
2026-01-22T16:06:52.2172152Z Progress (1): 8.5 kB
2026-01-22T16:06:52.2172435Z Progress (1): 19 kB 
2026-01-22T16:06:52.2172909Z Progress (1): 22 kB
2026-01-22T16:06:52.2173208Z Progress (1): 24 kB
2026-01-22T16:06:52.2173505Z Progress (1): 26 kB
2026-01-22T16:06:52.2173787Z Progress (1): 29 kB
2026-01-22T16:06:52.2174087Z Progress (1): 32 kB
2026-01-22T16:06:52.2175742Z Progress (1): 36 kB
2026-01-22T16:06:52.2177994Z Progress (1): 41 kB
2026-01-22T16:06:52.2179618Z Progress (1): 44 kB
2026-01-22T16:06:52.2180124Z Progress (1): 47 kB
2026-01-22T16:06:52.2182330Z Progress (1): 47 kB
2026-01-22T16:06:52.2183220Z Progress (1): 51 kB
2026-01-22T16:06:52.2185392Z Progress (1): 54 kB
2026-01-22T16:06:52.2187538Z Progress (1): 56 kB
2026-01-22T16:06:52.2187932Z Progress (1): 59 kB
2026-01-22T16:06:52.2188223Z Progress (1): 61 kB
2026-01-22T16:06:52.2188505Z Progress (1): 64 kB
2026-01-22T16:06:52.2188804Z Progress (1): 66 kB
2026-01-22T16:06:52.2189115Z Progress (1): 69 kB
2026-01-22T16:06:52.2189417Z Progress (1): 72 kB
2026-01-22T16:06:52.2189717Z Progress (1): 76 kB
2026-01-22T16:06:52.2190043Z Progress (1): 81 kB
2026-01-22T16:06:52.2190354Z Progress (1): 83 kB
2026-01-22T16:06:52.2190642Z                    
2026-01-22T16:06:52.2191057Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.92.Final/netty-parent-4.1.92.Final.pom (83 kB at 3.6 MB/s)
2026-01-22T16:06:52.2293342Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.92.Final/netty-common-4.1.92.Final.pom
2026-01-22T16:06:52.2466150Z Progress (1): 1.3 kB
2026-01-22T16:06:52.2474131Z Progress (1): 4.5 kB
2026-01-22T16:06:52.2474634Z Progress (1): 10 kB 
2026-01-22T16:06:52.2475749Z Progress (1): 12 kB
2026-01-22T16:06:52.2476053Z                    
2026-01-22T16:06:52.2476471Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.92.Final/netty-common-4.1.92.Final.pom (12 kB at 620 kB/s)
2026-01-22T16:06:52.2549587Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.92.Final/netty-codec-http-4.1.92.Final.pom
2026-01-22T16:06:52.2707102Z Progress (1): 810 B
2026-01-22T16:06:52.2709871Z Progress (1): 4.2 kB
2026-01-22T16:06:52.2715445Z Progress (1): 4.2 kB
2026-01-22T16:06:52.2715976Z                     
2026-01-22T16:06:52.2716615Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.92.Final/netty-codec-http-4.1.92.Final.pom (4.2 kB at 247 kB/s)
2026-01-22T16:06:52.2794686Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.92.Final/netty-transport-4.1.92.Final.pom
2026-01-22T16:06:52.2952650Z Progress (1): 859 B
2026-01-22T16:06:52.2958534Z Progress (1): 2.2 kB
2026-01-22T16:06:52.2959743Z                     
2026-01-22T16:06:52.2960917Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.92.Final/netty-transport-4.1.92.Final.pom (2.2 kB at 127 kB/s)
2026-01-22T16:06:52.2998298Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.92.Final/netty-resolver-4.1.92.Final.pom
2026-01-22T16:06:52.3154507Z Progress (1): 885 B
2026-01-22T16:06:52.3158671Z Progress (1): 1.6 kB
2026-01-22T16:06:52.3160131Z                     
2026-01-22T16:06:52.3160590Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.92.Final/netty-resolver-4.1.92.Final.pom (1.6 kB at 99 kB/s)
2026-01-22T16:06:52.3201625Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.92.Final/netty-codec-4.1.92.Final.pom
2026-01-22T16:06:52.3457767Z Progress (1): 808 B
2026-01-22T16:06:52.3458314Z Progress (1): 4.3 kB
2026-01-22T16:06:52.3464068Z Progress (1): 5.3 kB
2026-01-22T16:06:52.3465344Z                     
2026-01-22T16:06:52.3465756Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.92.Final/netty-codec-4.1.92.Final.pom (5.3 kB at 196 kB/s)
2026-01-22T16:06:52.3521688Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.92.Final/netty-handler-4.1.92.Final.pom
2026-01-22T16:06:52.3686758Z Progress (1): 801 B
2026-01-22T16:06:52.3688884Z Progress (1): 3.9 kB
2026-01-22T16:06:52.3692011Z Progress (1): 4.6 kB
2026-01-22T16:06:52.3696790Z                     
2026-01-22T16:06:52.3698178Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.92.Final/netty-handler-4.1.92.Final.pom (4.6 kB at 257 kB/s)
2026-01-22T16:06:52.3740673Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.92.Final/netty-transport-native-unix-common-4.1.92.Final.pom
2026-01-22T16:06:52.3899839Z Progress (1): 767 B
2026-01-22T16:06:52.3901783Z Progress (1): 2.2 kB
2026-01-22T16:06:52.3908606Z Progress (1): 4.5 kB
2026-01-22T16:06:52.3909856Z Progress (1): 6.8 kB
2026-01-22T16:06:52.3910214Z Progress (1): 18 kB 
2026-01-22T16:06:52.3911159Z Progress (1): 29 kB
2026-01-22T16:06:52.3912674Z                    
2026-01-22T16:06:52.3914697Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.92.Final/netty-transport-native-unix-common-4.1.92.Final.pom (29 kB at 1.7 MB/s)
2026-01-22T16:06:52.3971963Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.92.Final/netty-transport-classes-epoll-4.1.92.Final.pom
2026-01-22T16:06:52.4129059Z Progress (1): 859 B
2026-01-22T16:06:52.4130231Z Progress (1): 2.1 kB
2026-01-22T16:06:52.4199971Z                     
2026-01-22T16:06:52.4200574Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.92.Final/netty-transport-classes-epoll-4.1.92.Final.pom (2.1 kB at 133 kB/s)
2026-01-22T16:06:52.4251259Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.92.Final/netty-transport-classes-kqueue-4.1.92.Final.pom
2026-01-22T16:06:52.4362453Z Progress (1): 859 B
2026-01-22T16:06:52.4363384Z Progress (1): 2.1 kB
2026-01-22T16:06:52.4363855Z                     
2026-01-22T16:06:52.4364438Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.92.Final/netty-transport-classes-kqueue-4.1.92.Final.pom (2.1 kB at 119 kB/s)
2026-01-22T16:06:52.4412566Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.92.Final/netty-transport-native-epoll-4.1.92.Final.pom
2026-01-22T16:06:52.4601148Z Progress (1): 766 B
2026-01-22T16:06:52.4613411Z Progress (1): 2.1 kB
2026-01-22T16:06:52.4614873Z Progress (1): 3.4 kB
2026-01-22T16:06:52.4615475Z Progress (1): 6.1 kB
2026-01-22T16:06:52.4616016Z Progress (1): 9.0 kB
2026-01-22T16:06:52.4616646Z Progress (1): 18 kB 
2026-01-22T16:06:52.4617122Z Progress (1): 19 kB
2026-01-22T16:06:52.4617415Z                    
2026-01-22T16:06:52.4617847Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.92.Final/netty-transport-native-epoll-4.1.92.Final.pom (19 kB at 914 kB/s)
2026-01-22T16:06:52.4677508Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.92.Final/netty-transport-native-kqueue-4.1.92.Final.pom
2026-01-22T16:06:52.4886116Z Progress (1): 752 B
2026-01-22T16:06:52.4886854Z Progress (1): 2.1 kB
2026-01-22T16:06:52.4887331Z Progress (1): 3.9 kB
2026-01-22T16:06:52.4887983Z Progress (1): 6.2 kB
2026-01-22T16:06:52.4888454Z Progress (1): 19 kB 
2026-01-22T16:06:52.4888946Z Progress (1): 29 kB
2026-01-22T16:06:52.4890195Z Progress (1): 30 kB
2026-01-22T16:06:52.4891302Z                    
2026-01-22T16:06:52.4891786Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.92.Final/netty-transport-native-kqueue-4.1.92.Final.pom (30 kB at 1.4 MB/s)
2026-01-22T16:06:52.4953430Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.26.0/opentelemetry-api-1.26.0.pom
2026-01-22T16:06:52.5128971Z Progress (1): 1.0 kB
2026-01-22T16:06:52.5136200Z Progress (1): 1.8 kB
2026-01-22T16:06:52.5136524Z                     
2026-01-22T16:06:52.5136965Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.26.0/opentelemetry-api-1.26.0.pom (1.8 kB at 94 kB/s)
2026-01-22T16:06:52.5162596Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.26.0/opentelemetry-context-1.26.0.pom
2026-01-22T16:06:52.5333296Z Progress (1): 989 B
2026-01-22T16:06:52.5339572Z Progress (1): 1.6 kB
2026-01-22T16:06:52.5341808Z                     
2026-01-22T16:06:52.5342279Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.26.0/opentelemetry-context-1.26.0.pom (1.6 kB at 87 kB/s)
2026-01-22T16:06:52.5380732Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.26.0/opentelemetry-exporter-logging-1.26.0.pom
2026-01-22T16:06:52.5531448Z Progress (1): 988 B
2026-01-22T16:06:52.5543635Z Progress (1): 2.4 kB
2026-01-22T16:06:52.5544340Z                     
2026-01-22T16:06:52.5545171Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.26.0/opentelemetry-exporter-logging-1.26.0.pom (2.4 kB at 134 kB/s)
2026-01-22T16:06:52.5573371Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.26.0/opentelemetry-sdk-1.26.0.pom
2026-01-22T16:06:52.5761196Z Progress (1): 994 B
2026-01-22T16:06:52.5764006Z Progress (1): 2.6 kB
2026-01-22T16:06:52.5764598Z                     
2026-01-22T16:06:52.5765345Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.26.0/opentelemetry-sdk-1.26.0.pom (2.6 kB at 134 kB/s)
2026-01-22T16:06:52.5799792Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.26.0/opentelemetry-sdk-common-1.26.0.pom
2026-01-22T16:06:52.5964655Z Progress (1): 995 B
2026-01-22T16:06:52.5967294Z Progress (1): 2.0 kB
2026-01-22T16:06:52.5967816Z                     
2026-01-22T16:06:52.5968331Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.26.0/opentelemetry-sdk-common-1.26.0.pom (2.0 kB at 117 kB/s)
2026-01-22T16:06:52.5994211Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.26.0-alpha/opentelemetry-semconv-1.26.0-alpha.pom
2026-01-22T16:06:52.6154379Z Progress (1): 985 B
2026-01-22T16:06:52.6157516Z Progress (1): 1.8 kB
2026-01-22T16:06:52.6157837Z                     
2026-01-22T16:06:52.6158307Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.26.0-alpha/opentelemetry-semconv-1.26.0-alpha.pom (1.8 kB at 120 kB/s)
2026-01-22T16:06:52.6177423Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.26.0/opentelemetry-sdk-trace-1.26.0.pom
2026-01-22T16:06:52.6345972Z Progress (1): 977 B
2026-01-22T16:06:52.6353705Z Progress (1): 2.2 kB
2026-01-22T16:06:52.6354053Z                     
2026-01-22T16:06:52.6354506Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.26.0/opentelemetry-sdk-trace-1.26.0.pom (2.2 kB at 121 kB/s)
2026-01-22T16:06:52.6378190Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.26.0/opentelemetry-sdk-metrics-1.26.0.pom
2026-01-22T16:06:52.6538793Z Progress (1): 989 B
2026-01-22T16:06:52.6549662Z Progress (1): 2.2 kB
2026-01-22T16:06:52.6549978Z                     
2026-01-22T16:06:52.6550409Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.26.0/opentelemetry-sdk-metrics-1.26.0.pom (2.2 kB at 129 kB/s)
2026-01-22T16:06:52.6627234Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-extension-incubator/1.26.0-alpha/opentelemetry-extension-incubator-1.26.0-alpha.pom
2026-01-22T16:06:52.6828318Z Progress (1): 990 B
2026-01-22T16:06:52.6840296Z Progress (1): 1.8 kB
2026-01-22T16:06:52.6840950Z                     
2026-01-22T16:06:52.6841605Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-extension-incubator/1.26.0-alpha/opentelemetry-extension-incubator-1.26.0-alpha.pom (1.8 kB at 75 kB/s)
2026-01-22T16:06:52.6889959Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.26.0-alpha/opentelemetry-sdk-logs-1.26.0-alpha.pom
2026-01-22T16:06:52.7079356Z Progress (1): 975 B
2026-01-22T16:06:52.7080071Z Progress (1): 2.2 kB
2026-01-22T16:06:52.7080667Z                     
2026-01-22T16:06:52.7081304Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.26.0-alpha/opentelemetry-sdk-logs-1.26.0-alpha.pom (2.2 kB at 110 kB/s)
2026-01-22T16:06:52.7119696Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-logs/1.26.0-alpha/opentelemetry-api-logs-1.26.0-alpha.pom
2026-01-22T16:06:52.7308197Z Progress (1): 985 B
2026-01-22T16:06:52.7318026Z Progress (1): 1.8 kB
2026-01-22T16:06:52.7319679Z                     
2026-01-22T16:06:52.7320296Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-logs/1.26.0-alpha/opentelemetry-api-logs-1.26.0-alpha.pom (1.8 kB at 90 kB/s)
2026-01-22T16:06:52.7355123Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.26.0-alpha/opentelemetry-api-events-1.26.0-alpha.pom
2026-01-22T16:06:52.7517124Z Progress (1): 989 B
2026-01-22T16:06:52.7526580Z Progress (1): 1.8 kB
2026-01-22T16:06:52.7529864Z                     
2026-01-22T16:06:52.7531436Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.26.0-alpha/opentelemetry-api-events-1.26.0-alpha.pom (1.8 kB at 100 kB/s)
2026-01-22T16:06:52.7573439Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.26.0/opentelemetry-sdk-extension-autoconfigure-spi-1.26.0.pom
2026-01-22T16:06:52.7735156Z Progress (1): 964 B
2026-01-22T16:06:52.7738064Z Progress (1): 2.2 kB
2026-01-22T16:06:52.7738545Z                     
2026-01-22T16:06:52.7740041Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.26.0/opentelemetry-sdk-extension-autoconfigure-spi-1.26.0.pom (2.2 kB at 131 kB/s)
2026-01-22T16:06:52.7778967Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.26.0-alpha/opentelemetry-sdk-extension-autoconfigure-1.26.0-alpha.pom
2026-01-22T16:06:52.7957108Z Progress (1): 962 B
2026-01-22T16:06:52.7964011Z Progress (1): 2.6 kB
2026-01-22T16:06:52.7964635Z                     
2026-01-22T16:06:52.7965319Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.26.0-alpha/opentelemetry-sdk-extension-autoconfigure-1.26.0-alpha.pom (2.6 kB at 138 kB/s)
2026-01-22T16:06:52.8024496Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.10.0/selenium-http-4.10.0.pom
2026-01-22T16:06:52.8183445Z Progress (1): 1.1 kB
2026-01-22T16:06:52.8183977Z Progress (1): 2.8 kB
2026-01-22T16:06:52.8184426Z                     
2026-01-22T16:06:52.8185178Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.10.0/selenium-http-4.10.0.pom (2.8 kB at 165 kB/s)
2026-01-22T16:06:52.8232925Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.10.0/selenium-json-4.10.0.pom
2026-01-22T16:06:52.8421682Z Progress (1): 1.1 kB
2026-01-22T16:06:52.8433432Z Progress (1): 2.3 kB
2026-01-22T16:06:52.8462296Z                     
2026-01-22T16:06:52.8463343Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.10.0/selenium-json-4.10.0.pom (2.3 kB at 108 kB/s)
2026-01-22T16:06:52.8483157Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.10.0/selenium-manager-4.10.0.pom
2026-01-22T16:06:52.8633986Z Progress (1): 1.1 kB
2026-01-22T16:06:52.8634315Z Progress (1): 2.6 kB
2026-01-22T16:06:52.8634606Z                     
2026-01-22T16:06:52.8635036Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.10.0/selenium-manager-4.10.0.pom (2.6 kB at 176 kB/s)
2026-01-22T16:06:52.8658741Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.11.0/selenium-remote-driver-4.11.0.pom
2026-01-22T16:06:52.8798814Z Progress (1): 1.0 kB
2026-01-22T16:06:52.8801677Z Progress (1): 6.7 kB
2026-01-22T16:06:52.8824005Z Progress (1): 7.9 kB
2026-01-22T16:06:52.8824627Z                     
2026-01-22T16:06:52.8825355Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.11.0/selenium-remote-driver-4.11.0.pom (7.9 kB at 527 kB/s)
2026-01-22T16:06:52.8849961Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.11.0/selenium-http-4.11.0.pom
2026-01-22T16:06:52.9008040Z Progress (1): 1.1 kB
2026-01-22T16:06:52.9014447Z Progress (1): 2.8 kB
2026-01-22T16:06:52.9017620Z                     
2026-01-22T16:06:52.9018287Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.11.0/selenium-http-4.11.0.pom (2.8 kB at 165 kB/s)
2026-01-22T16:06:52.9044620Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.11.0/selenium-json-4.11.0.pom
2026-01-22T16:06:52.9188756Z Progress (1): 1.1 kB
2026-01-22T16:06:52.9193807Z Progress (1): 2.3 kB
2026-01-22T16:06:52.9195863Z                     
2026-01-22T16:06:52.9196324Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.11.0/selenium-json-4.11.0.pom (2.3 kB at 142 kB/s)
2026-01-22T16:06:52.9226096Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.11.0/selenium-manager-4.11.0.pom
2026-01-22T16:06:52.9386237Z Progress (1): 1.1 kB
2026-01-22T16:06:52.9392000Z Progress (1): 2.6 kB
2026-01-22T16:06:52.9396312Z                     
2026-01-22T16:06:52.9397100Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.11.0/selenium-manager-4.11.0.pom (2.6 kB at 146 kB/s)
2026-01-22T16:06:52.9426695Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.12.0/selenium-remote-driver-4.12.0.pom
2026-01-22T16:06:52.9590104Z Progress (1): 1.0 kB
2026-01-22T16:06:52.9590679Z Progress (1): 6.7 kB
2026-01-22T16:06:52.9595155Z Progress (1): 7.9 kB
2026-01-22T16:06:52.9596443Z                     
2026-01-22T16:06:52.9598621Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.12.0/selenium-remote-driver-4.12.0.pom (7.9 kB at 439 kB/s)
2026-01-22T16:06:52.9614941Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.1.1/auto-service-annotations-1.1.1.pom
2026-01-22T16:06:52.9774775Z Progress (1): 832 B
2026-01-22T16:06:52.9781068Z Progress (1): 2.3 kB
2026-01-22T16:06:52.9781451Z                     
2026-01-22T16:06:52.9783547Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.1.1/auto-service-annotations-1.1.1.pom (2.3 kB at 143 kB/s)
2026-01-22T16:06:52.9795692Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-aggregator/1.1.1/auto-service-aggregator-1.1.1.pom
2026-01-22T16:06:52.9962201Z Progress (1): 813 B
2026-01-22T16:06:52.9962562Z Progress (1): 2.4 kB
2026-01-22T16:06:52.9966956Z Progress (1): 4.3 kB
2026-01-22T16:06:52.9967424Z                     
2026-01-22T16:06:52.9967868Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-aggregator/1.1.1/auto-service-aggregator-1.1.1.pom (4.3 kB at 250 kB/s)
2026-01-22T16:06:52.9994619Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/32.1.2-jre/guava-32.1.2-jre.pom
2026-01-22T16:06:53.0168528Z Progress (1): 850 B
2026-01-22T16:06:53.0169910Z Progress (1): 2.5 kB
2026-01-22T16:06:53.0170213Z Progress (1): 4.6 kB
2026-01-22T16:06:53.0170484Z Progress (1): 6.2 kB
2026-01-22T16:06:53.0170749Z Progress (1): 8.1 kB
2026-01-22T16:06:53.0171031Z Progress (1): 11 kB 
2026-01-22T16:06:53.0171329Z Progress (1): 13 kB
2026-01-22T16:06:53.0171632Z                    
2026-01-22T16:06:53.0172024Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/32.1.2-jre/guava-32.1.2-jre.pom (13 kB at 755 kB/s)
2026-01-22T16:06:53.0204657Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/32.1.2-jre/guava-parent-32.1.2-jre.pom
2026-01-22T16:06:53.0376409Z Progress (1): 887 B
2026-01-22T16:06:53.0381213Z Progress (1): 2.6 kB
2026-01-22T16:06:53.0383625Z Progress (1): 4.8 kB
2026-01-22T16:06:53.0384037Z Progress (1): 6.7 kB
2026-01-22T16:06:53.0384433Z Progress (1): 9.4 kB
2026-01-22T16:06:53.0384815Z Progress (1): 11 kB 
2026-01-22T16:06:53.0385189Z Progress (1): 14 kB
2026-01-22T16:06:53.0388575Z Progress (1): 16 kB
2026-01-22T16:06:53.0388930Z Progress (1): 18 kB
2026-01-22T16:06:53.0389245Z Progress (1): 20 kB
2026-01-22T16:06:53.0389542Z                    
2026-01-22T16:06:53.0389970Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/32.1.2-jre/guava-parent-32.1.2-jre.pom (20 kB at 1.0 MB/s)
2026-01-22T16:06:53.0413731Z Downloading from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.33.0/checker-qual-3.33.0.pom
2026-01-22T16:06:53.0571541Z Progress (1): 952 B
2026-01-22T16:06:53.0579747Z Progress (1): 2.1 kB
2026-01-22T16:06:53.0580072Z                     
2026-01-22T16:06:53.0580510Z Downloaded from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.33.0/checker-qual-3.33.0.pom (2.1 kB at 131 kB/s)
2026-01-22T16:06:53.0599361Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.18.0/error_prone_annotations-2.18.0.pom
2026-01-22T16:06:53.0759608Z Progress (1): 835 B
2026-01-22T16:06:53.0764341Z Progress (1): 2.2 kB
2026-01-22T16:06:53.0765674Z                     
2026-01-22T16:06:53.0766171Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.18.0/error_prone_annotations-2.18.0.pom (2.2 kB at 127 kB/s)
2026-01-22T16:06:53.0803656Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.18.0/error_prone_parent-2.18.0.pom
2026-01-22T16:06:53.0955347Z Progress (1): 722 B
2026-01-22T16:06:53.0955889Z Progress (1): 2.2 kB
2026-01-22T16:06:53.0956307Z Progress (1): 4.2 kB
2026-01-22T16:06:53.0956728Z Progress (1): 8.5 kB
2026-01-22T16:06:53.0960698Z Progress (1): 11 kB 
2026-01-22T16:06:53.0961296Z                    
2026-01-22T16:06:53.0961860Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.18.0/error_prone_parent-2.18.0.pom (11 kB at 652 kB/s)
2026-01-22T16:06:53.0992580Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/2.8/j2objc-annotations-2.8.pom
2026-01-22T16:06:53.1141489Z Progress (1): 859 B
2026-01-22T16:06:53.1147632Z Progress (1): 2.9 kB
2026-01-22T16:06:53.1148979Z                     
2026-01-22T16:06:53.1149655Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/2.8/j2objc-annotations-2.8.pom (2.9 kB at 183 kB/s)
2026-01-22T16:06:53.1177134Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.96.Final/netty-buffer-4.1.96.Final.pom
2026-01-22T16:06:53.1398476Z Progress (1): 884 B
2026-01-22T16:06:53.1404196Z Progress (1): 1.6 kB
2026-01-22T16:06:53.1405527Z                     
2026-01-22T16:06:53.1405971Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.96.Final/netty-buffer-4.1.96.Final.pom (1.6 kB at 66 kB/s)
2026-01-22T16:06:53.1424599Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.96.Final/netty-parent-4.1.96.Final.pom
2026-01-22T16:06:53.1629817Z Progress (1): 717 B
2026-01-22T16:06:53.1630264Z Progress (1): 2.1 kB
2026-01-22T16:06:53.1639291Z Progress (1): 4.2 kB
2026-01-22T16:06:53.1639642Z Progress (1): 7.0 kB
2026-01-22T16:06:53.1639972Z Progress (1): 8.5 kB
2026-01-22T16:06:53.1640274Z Progress (1): 19 kB 
2026-01-22T16:06:53.1640566Z Progress (1): 22 kB
2026-01-22T16:06:53.1640873Z Progress (1): 24 kB
2026-01-22T16:06:53.1641177Z Progress (1): 26 kB
2026-01-22T16:06:53.1641498Z Progress (1): 29 kB
2026-01-22T16:06:53.1641802Z Progress (1): 32 kB
2026-01-22T16:06:53.1642112Z Progress (1): 36 kB
2026-01-22T16:06:53.1642402Z Progress (1): 41 kB
2026-01-22T16:06:53.1642913Z Progress (1): 44 kB
2026-01-22T16:06:53.1643246Z Progress (1): 47 kB
2026-01-22T16:06:53.1643522Z Progress (1): 47 kB
2026-01-22T16:06:53.1643800Z Progress (1): 51 kB
2026-01-22T16:06:53.1644082Z Progress (1): 54 kB
2026-01-22T16:06:53.1644369Z Progress (1): 56 kB
2026-01-22T16:06:53.1644644Z Progress (1): 59 kB
2026-01-22T16:06:53.1644932Z Progress (1): 61 kB
2026-01-22T16:06:53.1645208Z Progress (1): 64 kB
2026-01-22T16:06:53.1645490Z Progress (1): 66 kB
2026-01-22T16:06:53.1645770Z Progress (1): 69 kB
2026-01-22T16:06:53.1646050Z Progress (1): 72 kB
2026-01-22T16:06:53.1646339Z Progress (1): 76 kB
2026-01-22T16:06:53.1646624Z Progress (1): 81 kB
2026-01-22T16:06:53.1647160Z Progress (1): 83 kB
2026-01-22T16:06:53.1648767Z                    
2026-01-22T16:06:53.1649836Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.96.Final/netty-parent-4.1.96.Final.pom (83 kB at 4.0 MB/s)
2026-01-22T16:06:53.1703105Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.96.Final/netty-common-4.1.96.Final.pom
2026-01-22T16:06:53.1853763Z Progress (1): 1.3 kB
2026-01-22T16:06:53.1856601Z Progress (1): 4.5 kB
2026-01-22T16:06:53.1858025Z Progress (1): 10 kB 
2026-01-22T16:06:53.1860464Z Progress (1): 12 kB
2026-01-22T16:06:53.1863418Z                    
2026-01-22T16:06:53.1866228Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.96.Final/netty-common-4.1.96.Final.pom (12 kB at 693 kB/s)
2026-01-22T16:06:53.1920904Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.96.Final/netty-codec-http-4.1.96.Final.pom
2026-01-22T16:06:53.2089463Z Progress (1): 810 B
2026-01-22T16:06:53.2089984Z Progress (1): 4.2 kB
2026-01-22T16:06:53.2091106Z Progress (1): 4.2 kB
2026-01-22T16:06:53.2091407Z                     
2026-01-22T16:06:53.2091824Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.96.Final/netty-codec-http-4.1.96.Final.pom (4.2 kB at 247 kB/s)
2026-01-22T16:06:53.2146747Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.96.Final/netty-transport-4.1.96.Final.pom
2026-01-22T16:06:53.2355056Z Progress (1): 859 B
2026-01-22T16:06:53.2360401Z Progress (1): 2.2 kB
2026-01-22T16:06:53.2363906Z                     
2026-01-22T16:06:53.2365274Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.96.Final/netty-transport-4.1.96.Final.pom (2.2 kB at 98 kB/s)
2026-01-22T16:06:53.2414532Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.96.Final/netty-resolver-4.1.96.Final.pom
2026-01-22T16:06:53.2575804Z Progress (1): 885 B
2026-01-22T16:06:53.2585550Z Progress (1): 1.6 kB
2026-01-22T16:06:53.2586050Z                     
2026-01-22T16:06:53.2586576Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.96.Final/netty-resolver-4.1.96.Final.pom (1.6 kB at 88 kB/s)
2026-01-22T16:06:53.2656266Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.96.Final/netty-codec-4.1.96.Final.pom
2026-01-22T16:06:53.2827580Z Progress (1): 808 B
2026-01-22T16:06:53.2830427Z Progress (1): 4.3 kB
2026-01-22T16:06:53.2838465Z Progress (1): 5.3 kB
2026-01-22T16:06:53.2839016Z                     
2026-01-22T16:06:53.2839564Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.96.Final/netty-codec-4.1.96.Final.pom (5.3 kB at 279 kB/s)
2026-01-22T16:06:53.2905159Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.96.Final/netty-handler-4.1.96.Final.pom
2026-01-22T16:06:53.3055587Z Progress (1): 801 B
2026-01-22T16:06:53.3058674Z Progress (1): 3.9 kB
2026-01-22T16:06:53.3067927Z Progress (1): 4.6 kB
2026-01-22T16:06:53.3069580Z                     
2026-01-22T16:06:53.3070015Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.96.Final/netty-handler-4.1.96.Final.pom (4.6 kB at 257 kB/s)
2026-01-22T16:06:53.3148781Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.96.Final/netty-transport-native-unix-common-4.1.96.Final.pom
2026-01-22T16:06:53.3344065Z Progress (1): 767 B
2026-01-22T16:06:53.3346442Z Progress (1): 2.2 kB
2026-01-22T16:06:53.3348823Z Progress (1): 4.5 kB
2026-01-22T16:06:53.3355162Z Progress (1): 6.8 kB
2026-01-22T16:06:53.3355610Z Progress (1): 18 kB 
2026-01-22T16:06:53.3361379Z Progress (1): 29 kB
2026-01-22T16:06:53.3361853Z                    
2026-01-22T16:06:53.3362413Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.96.Final/netty-transport-native-unix-common-4.1.96.Final.pom (29 kB at 1.3 MB/s)
2026-01-22T16:06:53.3462963Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.96.Final/netty-transport-classes-epoll-4.1.96.Final.pom
2026-01-22T16:06:53.3644643Z Progress (1): 850 B
2026-01-22T16:06:53.3653555Z Progress (1): 2.1 kB
2026-01-22T16:06:53.3654028Z                     
2026-01-22T16:06:53.3654594Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.96.Final/netty-transport-classes-epoll-4.1.96.Final.pom (2.1 kB at 107 kB/s)
2026-01-22T16:06:53.3713769Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.96.Final/netty-transport-classes-kqueue-4.1.96.Final.pom
2026-01-22T16:06:53.3898184Z Progress (1): 859 B
2026-01-22T16:06:53.3907739Z Progress (1): 2.1 kB
2026-01-22T16:06:53.3910825Z                     
2026-01-22T16:06:53.3913859Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.96.Final/netty-transport-classes-kqueue-4.1.96.Final.pom (2.1 kB at 107 kB/s)
2026-01-22T16:06:53.3974577Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final.pom
2026-01-22T16:06:53.4124220Z Progress (1): 766 B
2026-01-22T16:06:53.4125024Z Progress (1): 2.1 kB
2026-01-22T16:06:53.4125799Z Progress (1): 3.4 kB
2026-01-22T16:06:53.4126353Z Progress (1): 6.1 kB
2026-01-22T16:06:53.4126861Z Progress (1): 9.0 kB
2026-01-22T16:06:53.4127316Z Progress (1): 18 kB 
2026-01-22T16:06:53.4127760Z Progress (1): 19 kB
2026-01-22T16:06:53.4128191Z                    
2026-01-22T16:06:53.4128949Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final.pom (19 kB at 1.2 MB/s)
2026-01-22T16:06:53.4194184Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final.pom
2026-01-22T16:06:53.4367478Z Progress (1): 752 B
2026-01-22T16:06:53.4368116Z Progress (1): 2.1 kB
2026-01-22T16:06:53.4368650Z Progress (1): 3.9 kB
2026-01-22T16:06:53.4369237Z Progress (1): 6.2 kB
2026-01-22T16:06:53.4369746Z Progress (1): 19 kB 
2026-01-22T16:06:53.4370255Z Progress (1): 29 kB
2026-01-22T16:06:53.4370867Z Progress (1): 30 kB
2026-01-22T16:06:53.4371320Z                    
2026-01-22T16:06:53.4371778Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final.pom (30 kB at 1.8 MB/s)
2026-01-22T16:06:53.4438739Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.28.0/opentelemetry-api-1.28.0.pom
2026-01-22T16:06:53.4619632Z Progress (1): 1.0 kB
2026-01-22T16:06:53.4625456Z Progress (1): 1.8 kB
2026-01-22T16:06:53.4625781Z                     
2026-01-22T16:06:53.4626411Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.28.0/opentelemetry-api-1.28.0.pom (1.8 kB at 94 kB/s)
2026-01-22T16:06:53.4652356Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.28.0/opentelemetry-context-1.28.0.pom
2026-01-22T16:06:53.4823331Z Progress (1): 989 B
2026-01-22T16:06:53.4827709Z Progress (1): 1.6 kB
2026-01-22T16:06:53.4828059Z                     
2026-01-22T16:06:53.4828520Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.28.0/opentelemetry-context-1.28.0.pom (1.6 kB at 87 kB/s)
2026-01-22T16:06:53.4864362Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.28.0/opentelemetry-exporter-logging-1.28.0.pom
2026-01-22T16:06:53.5036944Z Progress (1): 986 B
2026-01-22T16:06:53.5044248Z Progress (1): 2.4 kB
2026-01-22T16:06:53.5044762Z                     
2026-01-22T16:06:53.5045218Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.28.0/opentelemetry-exporter-logging-1.28.0.pom (2.4 kB at 127 kB/s)
2026-01-22T16:06:53.5071579Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.28.0/opentelemetry-sdk-1.28.0.pom
2026-01-22T16:06:53.5240469Z Progress (1): 994 B
2026-01-22T16:06:53.5254310Z Progress (1): 2.5 kB
2026-01-22T16:06:53.5257393Z                     
2026-01-22T16:06:53.5258070Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.28.0/opentelemetry-sdk-1.28.0.pom (2.5 kB at 134 kB/s)
2026-01-22T16:06:53.5286587Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.28.0/opentelemetry-sdk-common-1.28.0.pom
2026-01-22T16:06:53.5409531Z Progress (1): 995 B
2026-01-22T16:06:53.5413834Z Progress (1): 2.0 kB
2026-01-22T16:06:53.5417031Z                     
2026-01-22T16:06:53.5418861Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.28.0/opentelemetry-sdk-common-1.28.0.pom (2.0 kB at 142 kB/s)
2026-01-22T16:06:53.5440917Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.28.0-alpha/opentelemetry-semconv-1.28.0-alpha.pom
2026-01-22T16:06:53.5595196Z Progress (1): 985 B
2026-01-22T16:06:53.5596608Z Progress (1): 1.8 kB
2026-01-22T16:06:53.5596928Z                     
2026-01-22T16:06:53.5597394Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.28.0-alpha/opentelemetry-semconv-1.28.0-alpha.pom (1.8 kB at 113 kB/s)
2026-01-22T16:06:53.5617983Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.28.0/opentelemetry-sdk-trace-1.28.0.pom
2026-01-22T16:06:53.5761617Z Progress (1): 978 B
2026-01-22T16:06:53.5769325Z Progress (1): 2.2 kB
2026-01-22T16:06:53.5769669Z                     
2026-01-22T16:06:53.5770146Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.28.0/opentelemetry-sdk-trace-1.28.0.pom (2.2 kB at 146 kB/s)
2026-01-22T16:06:53.5783190Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.28.0/opentelemetry-sdk-metrics-1.28.0.pom
2026-01-22T16:06:53.5941740Z Progress (1): 989 B
2026-01-22T16:06:53.5945749Z Progress (1): 2.2 kB
2026-01-22T16:06:53.5947017Z                     
2026-01-22T16:06:53.5947507Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.28.0/opentelemetry-sdk-metrics-1.28.0.pom (2.2 kB at 137 kB/s)
2026-01-22T16:06:53.5969927Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-extension-incubator/1.28.0-alpha/opentelemetry-extension-incubator-1.28.0-alpha.pom
2026-01-22T16:06:53.6125093Z Progress (1): 990 B
2026-01-22T16:06:53.6137432Z Progress (1): 1.8 kB
2026-01-22T16:06:53.6138076Z                     
2026-01-22T16:06:53.6138912Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-extension-incubator/1.28.0-alpha/opentelemetry-extension-incubator-1.28.0-alpha.pom (1.8 kB at 113 kB/s)
2026-01-22T16:06:53.6149853Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.28.0/opentelemetry-sdk-logs-1.28.0.pom
2026-01-22T16:06:53.6302009Z Progress (1): 982 B
2026-01-22T16:06:53.6306514Z Progress (1): 2.2 kB
2026-01-22T16:06:53.6307713Z                     
2026-01-22T16:06:53.6308888Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.28.0/opentelemetry-sdk-logs-1.28.0.pom (2.2 kB at 136 kB/s)
2026-01-22T16:06:53.6328472Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.28.0-alpha/opentelemetry-api-events-1.28.0-alpha.pom
2026-01-22T16:06:53.6490169Z Progress (1): 989 B
2026-01-22T16:06:53.6492130Z Progress (1): 1.8 kB
2026-01-22T16:06:53.6494421Z                     
2026-01-22T16:06:53.6496254Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.28.0-alpha/opentelemetry-api-events-1.28.0-alpha.pom (1.8 kB at 106 kB/s)
2026-01-22T16:06:53.6515293Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.28.0/opentelemetry-sdk-extension-autoconfigure-spi-1.28.0.pom
2026-01-22T16:06:53.6671745Z Progress (1): 977 B
2026-01-22T16:06:53.6674433Z Progress (1): 1.8 kB
2026-01-22T16:06:53.6675713Z                     
2026-01-22T16:06:53.6677230Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.28.0/opentelemetry-sdk-extension-autoconfigure-spi-1.28.0.pom (1.8 kB at 107 kB/s)
2026-01-22T16:06:53.6698491Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.28.0/opentelemetry-sdk-extension-autoconfigure-1.28.0.pom
2026-01-22T16:06:53.6854571Z Progress (1): 975 B
2026-01-22T16:06:53.6859471Z Progress (1): 2.4 kB
2026-01-22T16:06:53.6861164Z                     
2026-01-22T16:06:53.6862468Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.28.0/opentelemetry-sdk-extension-autoconfigure-1.28.0.pom (2.4 kB at 152 kB/s)
2026-01-22T16:06:53.6884896Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.5/byte-buddy-1.14.5.pom
2026-01-22T16:06:53.7048052Z Progress (1): 958 B
2026-01-22T16:06:53.7048383Z Progress (1): 3.7 kB
2026-01-22T16:06:53.7048681Z Progress (1): 7.0 kB
2026-01-22T16:06:53.7048963Z Progress (1): 14 kB 
2026-01-22T16:06:53.7049449Z Progress (1): 16 kB
2026-01-22T16:06:53.7049717Z                    
2026-01-22T16:06:53.7050108Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.5/byte-buddy-1.14.5.pom (16 kB at 931 kB/s)
2026-01-22T16:06:53.7079197Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.14.5/byte-buddy-parent-1.14.5.pom
2026-01-22T16:06:53.7229103Z Progress (1): 828 B
2026-01-22T16:06:53.7232584Z Progress (1): 2.1 kB
2026-01-22T16:06:53.7236514Z Progress (1): 3.6 kB
2026-01-22T16:06:53.7250321Z Progress (1): 6.2 kB
2026-01-22T16:06:53.7254499Z Progress (1): 8.1 kB
2026-01-22T16:06:53.7256688Z Progress (1): 11 kB 
2026-01-22T16:06:53.7257367Z Progress (1): 13 kB
2026-01-22T16:06:53.7260298Z Progress (1): 17 kB
2026-01-22T16:06:53.7260620Z Progress (1): 22 kB
2026-01-22T16:06:53.7260920Z Progress (1): 25 kB
2026-01-22T16:06:53.7261225Z Progress (1): 36 kB
2026-01-22T16:06:53.7261516Z Progress (1): 45 kB
2026-01-22T16:06:53.7261835Z Progress (1): 50 kB
2026-01-22T16:06:53.7262125Z Progress (1): 54 kB
2026-01-22T16:06:53.7262422Z Progress (1): 58 kB
2026-01-22T16:06:53.7262695Z                    
2026-01-22T16:06:53.7263329Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.14.5/byte-buddy-parent-1.14.5.pom (58 kB at 3.1 MB/s)
2026-01-22T16:06:53.7310094Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.12.0/selenium-http-4.12.0.pom
2026-01-22T16:06:53.7474796Z Progress (1): 1.1 kB
2026-01-22T16:06:53.7483381Z Progress (1): 2.8 kB
2026-01-22T16:06:53.7485381Z                     
2026-01-22T16:06:53.7487431Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.12.0/selenium-http-4.12.0.pom (2.8 kB at 165 kB/s)
2026-01-22T16:06:53.7504983Z Downloading from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.2/failsafe-3.3.2.pom
2026-01-22T16:06:53.7671478Z Progress (1): 1.0 kB
2026-01-22T16:06:53.7672514Z                     
2026-01-22T16:06:53.7674679Z Downloaded from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.2/failsafe-3.3.2.pom (1.0 kB at 59 kB/s)
2026-01-22T16:06:53.7687552Z Downloading from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe-parent/3.3.2/failsafe-parent-3.3.2.pom
2026-01-22T16:06:53.7845634Z Progress (1): 1.1 kB
2026-01-22T16:06:53.7845979Z Progress (1): 3.4 kB
2026-01-22T16:06:53.7846286Z Progress (1): 5.8 kB
2026-01-22T16:06:53.7846598Z Progress (1): 8.7 kB
2026-01-22T16:06:53.7846910Z Progress (1): 9.2 kB
2026-01-22T16:06:53.7847191Z                     
2026-01-22T16:06:53.7847574Z Downloaded from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe-parent/3.3.2/failsafe-parent-3.3.2.pom (9.2 kB at 612 kB/s)
2026-01-22T16:06:53.7864691Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.12.0/selenium-json-4.12.0.pom
2026-01-22T16:06:53.8024005Z Progress (1): 1.1 kB
2026-01-22T16:06:53.8027794Z Progress (1): 2.3 kB
2026-01-22T16:06:53.8029146Z                     
2026-01-22T16:06:53.8031575Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.12.0/selenium-json-4.12.0.pom (2.3 kB at 133 kB/s)
2026-01-22T16:06:53.8051199Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.12.0/selenium-manager-4.12.0.pom
2026-01-22T16:06:53.8226906Z Progress (1): 1.1 kB
2026-01-22T16:06:53.8261690Z Progress (1): 2.8 kB
2026-01-22T16:06:53.8262210Z                     
2026-01-22T16:06:53.8262962Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.12.0/selenium-manager-4.12.0.pom (2.8 kB at 148 kB/s)
2026-01-22T16:06:53.8263618Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.12.0/selenium-os-4.12.0.pom
2026-01-22T16:06:53.8465882Z Progress (1): 1.1 kB
2026-01-22T16:06:53.8484675Z Progress (1): 2.6 kB
2026-01-22T16:06:53.8485386Z                     
2026-01-22T16:06:53.8486007Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.12.0/selenium-os-4.12.0.pom (2.6 kB at 125 kB/s)
2026-01-22T16:06:53.8503473Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.12.1/selenium-remote-driver-4.12.1.pom
2026-01-22T16:06:53.8695064Z Progress (1): 1.0 kB
2026-01-22T16:06:53.8695431Z Progress (1): 6.7 kB
2026-01-22T16:06:53.8695753Z Progress (1): 7.9 kB
2026-01-22T16:06:53.8696069Z                     
2026-01-22T16:06:53.8696526Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.12.1/selenium-remote-driver-4.12.1.pom (7.9 kB at 416 kB/s)
2026-01-22T16:06:53.8734559Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.12.1/selenium-http-4.12.1.pom
2026-01-22T16:06:53.8869490Z Progress (1): 1.1 kB
2026-01-22T16:06:53.8873046Z Progress (1): 2.8 kB
2026-01-22T16:06:53.8874657Z                     
2026-01-22T16:06:53.8875289Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.12.1/selenium-http-4.12.1.pom (2.8 kB at 175 kB/s)
2026-01-22T16:06:53.8898026Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.12.1/selenium-json-4.12.1.pom
2026-01-22T16:06:53.9493728Z Progress (1): 1.1 kB
2026-01-22T16:06:53.9494497Z Progress (1): 2.3 kB
2026-01-22T16:06:53.9495043Z                     
2026-01-22T16:06:53.9495828Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.12.1/selenium-json-4.12.1.pom (2.3 kB at 39 kB/s)
2026-01-22T16:06:53.9511414Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.12.1/selenium-manager-4.12.1.pom
2026-01-22T16:06:53.9695835Z Progress (1): 1.1 kB
2026-01-22T16:06:53.9702633Z Progress (1): 2.8 kB
2026-01-22T16:06:53.9703263Z                     
2026-01-22T16:06:53.9703695Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.12.1/selenium-manager-4.12.1.pom (2.8 kB at 141 kB/s)
2026-01-22T16:06:53.9746759Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.12.1/selenium-os-4.12.1.pom
2026-01-22T16:06:53.9892292Z Progress (1): 1.1 kB
2026-01-22T16:06:53.9894900Z Progress (1): 2.6 kB
2026-01-22T16:06:53.9897352Z                     
2026-01-22T16:06:53.9899429Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.12.1/selenium-os-4.12.1.pom (2.6 kB at 154 kB/s)
2026-01-22T16:06:53.9945690Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.13.0/selenium-remote-driver-4.13.0.pom
2026-01-22T16:06:54.0132497Z Progress (1): 1.0 kB
2026-01-22T16:06:54.0134579Z Progress (1): 6.7 kB
2026-01-22T16:06:54.0139301Z Progress (1): 7.9 kB
2026-01-22T16:06:54.0141241Z                     
2026-01-22T16:06:54.0142122Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.13.0/selenium-remote-driver-4.13.0.pom (7.9 kB at 416 kB/s)
2026-01-22T16:06:54.0201391Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.13.0/selenium-http-4.13.0.pom
2026-01-22T16:06:54.0362514Z Progress (1): 1.1 kB
2026-01-22T16:06:54.0365948Z Progress (1): 2.8 kB
2026-01-22T16:06:54.0368476Z                     
2026-01-22T16:06:54.0370136Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.13.0/selenium-http-4.13.0.pom (2.8 kB at 156 kB/s)
2026-01-22T16:06:54.0389283Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.13.0/selenium-json-4.13.0.pom
2026-01-22T16:06:54.0623393Z Progress (1): 1.1 kB
2026-01-22T16:06:54.0625295Z Progress (1): 2.3 kB
2026-01-22T16:06:54.0625861Z                     
2026-01-22T16:06:54.0626619Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.13.0/selenium-json-4.13.0.pom (2.3 kB at 103 kB/s)
2026-01-22T16:06:54.0636225Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.13.0/selenium-manager-4.13.0.pom
2026-01-22T16:06:54.0814968Z Progress (1): 1.1 kB
2026-01-22T16:06:54.0821689Z Progress (1): 2.8 kB
2026-01-22T16:06:54.0822182Z                     
2026-01-22T16:06:54.0822905Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.13.0/selenium-manager-4.13.0.pom (2.8 kB at 157 kB/s)
2026-01-22T16:06:54.0847890Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.13.0/selenium-os-4.13.0.pom
2026-01-22T16:06:54.1001722Z Progress (1): 1.1 kB
2026-01-22T16:06:54.1007679Z Progress (1): 2.6 kB
2026-01-22T16:06:54.1008159Z                     
2026-01-22T16:06:54.1008735Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.13.0/selenium-os-4.13.0.pom (2.6 kB at 164 kB/s)
2026-01-22T16:06:54.1027478Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/maven-metadata.xml
2026-01-22T16:06:54.1203479Z Progress (1): 4.5 kB
2026-01-22T16:06:54.1203983Z Progress (1): 6.3 kB
2026-01-22T16:06:54.1204376Z                     
2026-01-22T16:06:54.1204897Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/maven-metadata.xml (6.3 kB at 372 kB/s)
2026-01-22T16:06:54.1233397Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.9.1/selenium-support-4.9.1.pom
2026-01-22T16:06:54.1389725Z Progress (1): 1.1 kB
2026-01-22T16:06:54.1394930Z Progress (1): 3.4 kB
2026-01-22T16:06:54.1395841Z                     
2026-01-22T16:06:54.1396566Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.9.1/selenium-support-4.9.1.pom (3.4 kB at 188 kB/s)
2026-01-22T16:06:54.1418782Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.10.0/selenium-support-4.10.0.pom
2026-01-22T16:06:54.1577239Z Progress (1): 1.1 kB
2026-01-22T16:06:54.1590879Z Progress (1): 3.4 kB
2026-01-22T16:06:54.1591531Z                     
2026-01-22T16:06:54.1592210Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.10.0/selenium-support-4.10.0.pom (3.4 kB at 199 kB/s)
2026-01-22T16:06:54.1620799Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.11.0/selenium-support-4.11.0.pom
2026-01-22T16:06:54.1769920Z Progress (1): 1.1 kB
2026-01-22T16:06:54.1775060Z Progress (1): 3.2 kB
2026-01-22T16:06:54.1776465Z                     
2026-01-22T16:06:54.1777142Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.11.0/selenium-support-4.11.0.pom (3.2 kB at 188 kB/s)
2026-01-22T16:06:54.1803855Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.12.0/selenium-support-4.12.0.pom
2026-01-22T16:06:54.1942491Z Progress (1): 1.1 kB
2026-01-22T16:06:54.1946843Z Progress (1): 3.2 kB
2026-01-22T16:06:54.1947559Z                     
2026-01-22T16:06:54.1948350Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.12.0/selenium-support-4.12.0.pom (3.2 kB at 213 kB/s)
2026-01-22T16:06:54.1994225Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.12.1/selenium-support-4.12.1.pom
2026-01-22T16:06:54.2132122Z Progress (1): 1.1 kB
2026-01-22T16:06:54.2163671Z Progress (1): 3.2 kB
2026-01-22T16:06:54.2164581Z                     
2026-01-22T16:06:54.2165373Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.12.1/selenium-support-4.12.1.pom (3.2 kB at 178 kB/s)
2026-01-22T16:06:54.2194174Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.13.0/selenium-support-4.13.0.pom
2026-01-22T16:06:54.2353654Z Progress (1): 1.1 kB
2026-01-22T16:06:54.2355789Z Progress (1): 3.2 kB
2026-01-22T16:06:54.2357075Z                     
2026-01-22T16:06:54.2358436Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.13.0/selenium-support-4.13.0.pom (3.2 kB at 178 kB/s)
2026-01-22T16:06:54.2407171Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.pom
2026-01-22T16:06:54.2531020Z Progress (1): 1.1 kB
2026-01-22T16:06:54.2533365Z Progress (1): 3.4 kB
2026-01-22T16:06:54.2560884Z Progress (1): 6.6 kB
2026-01-22T16:06:54.2561562Z Progress (1): 8.7 kB
2026-01-22T16:06:54.2562492Z Progress (1): 9.4 kB
2026-01-22T16:06:54.2563315Z                     
2026-01-22T16:06:54.2564333Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.pom (9.4 kB at 624 kB/s)
2026-01-22T16:06:54.2565138Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson-parent/2.10.1/gson-parent-2.10.1.pom
2026-01-22T16:06:54.2757134Z Progress (1): 1.1 kB
2026-01-22T16:06:54.2757807Z Progress (1): 2.7 kB
2026-01-22T16:06:54.2758679Z Progress (1): 4.3 kB
2026-01-22T16:06:54.2759219Z Progress (1): 6.5 kB
2026-01-22T16:06:54.2760089Z Progress (1): 8.5 kB
2026-01-22T16:06:54.2760721Z Progress (1): 11 kB 
2026-01-22T16:06:54.2761530Z Progress (1): 13 kB
2026-01-22T16:06:54.2783948Z                    
2026-01-22T16:06:54.2784683Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson-parent/2.10.1/gson-parent-2.10.1.pom (13 kB at 596 kB/s)
2026-01-22T16:06:54.2793358Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.13.0/commons-lang3-3.13.0.pom
2026-01-22T16:06:54.2984908Z Progress (1): 728 B
2026-01-22T16:06:54.2985639Z Progress (1): 2.0 kB
2026-01-22T16:06:54.2986529Z Progress (1): 4.7 kB
2026-01-22T16:06:54.2987049Z Progress (1): 8.3 kB
2026-01-22T16:06:54.2987950Z Progress (1): 12 kB 
2026-01-22T16:06:54.2988644Z Progress (1): 15 kB
2026-01-22T16:06:54.2989522Z Progress (1): 16 kB
2026-01-22T16:06:54.2990066Z Progress (1): 18 kB
2026-01-22T16:06:54.2991573Z Progress (1): 21 kB
2026-01-22T16:06:54.2991883Z Progress (1): 24 kB
2026-01-22T16:06:54.2992175Z Progress (1): 27 kB
2026-01-22T16:06:54.2992455Z Progress (1): 30 kB
2026-01-22T16:06:54.2992948Z Progress (1): 31 kB
2026-01-22T16:06:54.2993227Z                    
2026-01-22T16:06:54.2993630Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.13.0/commons-lang3-3.13.0.pom (31 kB at 1.7 MB/s)
2026-01-22T16:06:54.3024275Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/58/commons-parent-58.pom
2026-01-22T16:06:54.3227775Z Progress (1): 704 B
2026-01-22T16:06:54.3230941Z Progress (1): 1.9 kB
2026-01-22T16:06:54.3248515Z Progress (1): 3.1 kB
2026-01-22T16:06:54.3249182Z Progress (1): 4.5 kB
2026-01-22T16:06:54.3250070Z Progress (1): 6.5 kB
2026-01-22T16:06:54.3250815Z Progress (1): 8.3 kB
2026-01-22T16:06:54.3251675Z Progress (1): 10 kB 
2026-01-22T16:06:54.3252215Z Progress (1): 12 kB
2026-01-22T16:06:54.3253312Z Progress (1): 15 kB
2026-01-22T16:06:54.3253861Z Progress (1): 18 kB
2026-01-22T16:06:54.3254750Z Progress (1): 20 kB
2026-01-22T16:06:54.3255276Z Progress (1): 23 kB
2026-01-22T16:06:54.3256128Z Progress (1): 26 kB
2026-01-22T16:06:54.3256721Z Progress (1): 29 kB
2026-01-22T16:06:54.3257567Z Progress (1): 33 kB
2026-01-22T16:06:54.3258096Z Progress (1): 33 kB
2026-01-22T16:06:54.3263932Z Progress (1): 36 kB
2026-01-22T16:06:54.3293391Z Progress (1): 41 kB
2026-01-22T16:06:54.3294559Z Progress (1): 44 kB
2026-01-22T16:06:54.3295332Z Progress (1): 47 kB
2026-01-22T16:06:54.3296371Z Progress (1): 49 kB
2026-01-22T16:06:54.3296961Z Progress (1): 51 kB
2026-01-22T16:06:54.3298382Z Progress (1): 55 kB
2026-01-22T16:06:54.3298695Z Progress (1): 58 kB
2026-01-22T16:06:54.3299003Z Progress (1): 61 kB
2026-01-22T16:06:54.3299302Z Progress (1): 64 kB
2026-01-22T16:06:54.3299614Z Progress (1): 67 kB
2026-01-22T16:06:54.3299904Z Progress (1): 72 kB
2026-01-22T16:06:54.3300197Z Progress (1): 76 kB
2026-01-22T16:06:54.3300499Z Progress (1): 80 kB
2026-01-22T16:06:54.3300817Z Progress (1): 83 kB
2026-01-22T16:06:54.3301100Z                    
2026-01-22T16:06:54.3301490Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/58/commons-parent-58.pom (83 kB at 3.4 MB/s)
2026-01-22T16:06:54.3361608Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.3/junit-bom-5.9.3.pom
2026-01-22T16:06:54.3557673Z Progress (1): 907 B
2026-01-22T16:06:54.3562452Z Progress (1): 4.1 kB
2026-01-22T16:06:54.3570925Z Progress (1): 5.6 kB
2026-01-22T16:06:54.3573001Z                     
2026-01-22T16:06:54.3574974Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.3/junit-bom-5.9.3.pom (5.6 kB at 268 kB/s)
2026-01-22T16:06:54.3632095Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.14.0/commons-io-2.14.0.pom
2026-01-22T16:06:54.3785888Z Progress (1): 764 B
2026-01-22T16:06:54.3786396Z Progress (1): 2.1 kB
2026-01-22T16:06:54.3786791Z Progress (1): 5.2 kB
2026-01-22T16:06:54.3787182Z Progress (1): 7.6 kB
2026-01-22T16:06:54.3787565Z Progress (1): 10 kB 
2026-01-22T16:06:54.3787983Z Progress (1): 12 kB
2026-01-22T16:06:54.3788390Z Progress (1): 15 kB
2026-01-22T16:06:54.3796507Z Progress (1): 18 kB
2026-01-22T16:06:54.3804525Z Progress (1): 20 kB
2026-01-22T16:06:54.3823154Z                    
2026-01-22T16:06:54.3824485Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.14.0/commons-io-2.14.0.pom (20 kB at 1.1 MB/s)
2026-01-22T16:06:54.3825353Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/62/commons-parent-62.pom
2026-01-22T16:06:54.4036319Z Progress (1): 704 B
2026-01-22T16:06:54.4038787Z Progress (1): 1.9 kB
2026-01-22T16:06:54.4064683Z Progress (1): 3.1 kB
2026-01-22T16:06:54.4066649Z Progress (1): 4.6 kB
2026-01-22T16:06:54.4068554Z Progress (1): 6.5 kB
2026-01-22T16:06:54.4070097Z Progress (1): 8.4 kB
2026-01-22T16:06:54.4071089Z Progress (1): 10 kB 
2026-01-22T16:06:54.4071548Z Progress (1): 13 kB
2026-01-22T16:06:54.4071959Z Progress (1): 15 kB
2026-01-22T16:06:54.4072362Z Progress (1): 18 kB
2026-01-22T16:06:54.4072971Z Progress (1): 20 kB
2026-01-22T16:06:54.4073398Z Progress (1): 23 kB
2026-01-22T16:06:54.4073807Z Progress (1): 25 kB
2026-01-22T16:06:54.4074196Z Progress (1): 28 kB
2026-01-22T16:06:54.4074690Z Progress (1): 32 kB
2026-01-22T16:06:54.4075107Z Progress (1): 32 kB
2026-01-22T16:06:54.4075494Z Progress (1): 35 kB
2026-01-22T16:06:54.4075886Z Progress (1): 41 kB
2026-01-22T16:06:54.4076272Z Progress (1): 44 kB
2026-01-22T16:06:54.4076650Z Progress (1): 46 kB
2026-01-22T16:06:54.4077028Z Progress (1): 49 kB
2026-01-22T16:06:54.4077417Z Progress (1): 51 kB
2026-01-22T16:06:54.4077797Z Progress (1): 54 kB
2026-01-22T16:06:54.4078431Z Progress (1): 58 kB
2026-01-22T16:06:54.4078856Z Progress (1): 60 kB
2026-01-22T16:06:54.4079309Z Progress (1): 64 kB
2026-01-22T16:06:54.4079747Z Progress (1): 67 kB
2026-01-22T16:06:54.4080205Z Progress (1): 71 kB
2026-01-22T16:06:54.4081651Z Progress (1): 74 kB
2026-01-22T16:06:54.4081993Z Progress (1): 77 kB
2026-01-22T16:06:54.4082302Z Progress (1): 80 kB
2026-01-22T16:06:54.4082612Z Progress (1): 81 kB
2026-01-22T16:06:54.4089991Z                    
2026-01-22T16:06:54.4090491Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/62/commons-parent-62.pom (81 kB at 3.4 MB/s)
2026-01-22T16:06:54.4199717Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/30/apache-30.pom
2026-01-22T16:06:54.4376364Z Progress (1): 741 B
2026-01-22T16:06:54.4379694Z Progress (1): 2.1 kB
2026-01-22T16:06:54.4382968Z Progress (1): 4.0 kB
2026-01-22T16:06:54.4385161Z Progress (1): 6.2 kB
2026-01-22T16:06:54.4387353Z Progress (1): 11 kB 
2026-01-22T16:06:54.4388458Z Progress (1): 16 kB
2026-01-22T16:06:54.4389154Z Progress (1): 20 kB
2026-01-22T16:06:54.4390184Z Progress (1): 22 kB
2026-01-22T16:06:54.4390818Z Progress (1): 23 kB
2026-01-22T16:06:54.4392164Z                    
2026-01-22T16:06:54.4392561Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/30/apache-30.pom (23 kB at 1.1 MB/s)
2026-01-22T16:06:54.4472186Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.0/junit-bom-5.10.0.pom
2026-01-22T16:06:54.4623235Z Progress (1): 912 B
2026-01-22T16:06:54.4623962Z Progress (1): 4.1 kB
2026-01-22T16:06:54.4627374Z Progress (1): 5.6 kB
2026-01-22T16:06:54.4629486Z                     
2026-01-22T16:06:54.4631304Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.0/junit-bom-5.10.0.pom (5.6 kB at 353 kB/s)
2026-01-22T16:06:54.4654330Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.9/slf4j-api-2.0.9.pom
2026-01-22T16:06:54.4802252Z Progress (1): 1.1 kB
2026-01-22T16:06:54.4809871Z Progress (1): 2.8 kB
2026-01-22T16:06:54.4810935Z                     
2026-01-22T16:06:54.4812567Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.9/slf4j-api-2.0.9.pom (2.8 kB at 176 kB/s)
2026-01-22T16:06:54.4826286Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.9/slf4j-parent-2.0.9.pom
2026-01-22T16:06:54.4976693Z Progress (1): 945 B
2026-01-22T16:06:54.4977059Z Progress (1): 3.2 kB
2026-01-22T16:06:54.4977390Z Progress (1): 6.0 kB
2026-01-22T16:06:54.4977741Z Progress (1): 8.1 kB
2026-01-22T16:06:54.4978059Z Progress (1): 12 kB 
2026-01-22T16:06:54.4978392Z Progress (1): 14 kB
2026-01-22T16:06:54.4981320Z Progress (1): 16 kB
2026-01-22T16:06:54.4982659Z                    
2026-01-22T16:06:54.4984303Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.9/slf4j-parent-2.0.9.pom (16 kB at 1.0 MB/s)
2026-01-22T16:06:54.5002240Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.9/slf4j-bom-2.0.9.pom
2026-01-22T16:06:54.5158141Z Progress (1): 1.0 kB
2026-01-22T16:06:54.5158465Z Progress (1): 4.8 kB
2026-01-22T16:06:54.5158783Z Progress (1): 4.9 kB
2026-01-22T16:06:54.5159064Z                     
2026-01-22T16:06:54.5159459Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.9/slf4j-bom-2.0.9.pom (4.9 kB at 328 kB/s)
2026-01-22T16:06:54.5173459Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-java/4.16.1/selenium-java-4.16.1.pom
2026-01-22T16:06:54.5405353Z Progress (1): 1.1 kB
2026-01-22T16:06:54.5410504Z Progress (1): 4.4 kB
2026-01-22T16:06:54.5412687Z                     
2026-01-22T16:06:54.5415115Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-java/4.16.1/selenium-java-4.16.1.pom (4.4 kB at 184 kB/s)
2026-01-22T16:06:54.5438644Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.16.1/selenium-api-4.16.1.pom
2026-01-22T16:06:54.5625323Z Progress (1): 1.1 kB
2026-01-22T16:06:54.5627702Z Progress (1): 2.1 kB
2026-01-22T16:06:54.5629637Z                     
2026-01-22T16:06:54.5630558Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.16.1/selenium-api-4.16.1.pom (2.1 kB at 104 kB/s)
2026-01-22T16:06:54.5645804Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chrome-driver/4.16.1/selenium-chrome-driver-4.16.1.pom
2026-01-22T16:06:54.5857553Z Progress (1): 1.1 kB
2026-01-22T16:06:54.5862087Z Progress (1): 3.3 kB
2026-01-22T16:06:54.5863257Z                     
2026-01-22T16:06:54.5864588Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chrome-driver/4.16.1/selenium-chrome-driver-4.16.1.pom (3.3 kB at 148 kB/s)
2026-01-22T16:06:54.5888920Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chromium-driver/4.16.1/selenium-chromium-driver-4.16.1.pom
2026-01-22T16:06:54.6058705Z Progress (1): 1.1 kB
2026-01-22T16:06:54.6063722Z Progress (1): 2.7 kB
2026-01-22T16:06:54.6064253Z                     
2026-01-22T16:06:54.6065283Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chromium-driver/4.16.1/selenium-chromium-driver-4.16.1.pom (2.7 kB at 149 kB/s)
2026-01-22T16:06:54.6091023Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.16.1/selenium-json-4.16.1.pom
2026-01-22T16:06:54.6260529Z Progress (1): 1.1 kB
2026-01-22T16:06:54.6264972Z Progress (1): 2.3 kB
2026-01-22T16:06:54.6266019Z                     
2026-01-22T16:06:54.6266851Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.16.1/selenium-json-4.16.1.pom (2.3 kB at 119 kB/s)
2026-01-22T16:06:54.6282317Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.16.1/selenium-remote-driver-4.16.1.pom
2026-01-22T16:06:54.6453756Z Progress (1): 1.1 kB
2026-01-22T16:06:54.6459165Z Progress (1): 5.3 kB
2026-01-22T16:06:54.6466409Z                     
2026-01-22T16:06:54.6466879Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.16.1/selenium-remote-driver-4.16.1.pom (5.3 kB at 296 kB/s)
2026-01-22T16:06:54.6506075Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.16.1/selenium-http-4.16.1.pom
2026-01-22T16:06:54.6633032Z Progress (1): 1.1 kB
2026-01-22T16:06:54.6638494Z Progress (1): 3.0 kB
2026-01-22T16:06:54.6638808Z                     
2026-01-22T16:06:54.6639242Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.16.1/selenium-http-4.16.1.pom (3.0 kB at 187 kB/s)
2026-01-22T16:06:54.6661099Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.16.1/selenium-manager-4.16.1.pom
2026-01-22T16:06:54.6826026Z Progress (1): 1.1 kB
2026-01-22T16:06:54.6832982Z Progress (1): 2.6 kB
2026-01-22T16:06:54.6833341Z                     
2026-01-22T16:06:54.6833791Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.16.1/selenium-manager-4.16.1.pom (2.6 kB at 156 kB/s)
2026-01-22T16:06:54.6846686Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.16.1/selenium-os-4.16.1.pom
2026-01-22T16:06:54.7029090Z Progress (1): 1.1 kB
2026-01-22T16:06:54.7033884Z Progress (1): 2.4 kB
2026-01-22T16:06:54.7034354Z                     
2026-01-22T16:06:54.7034784Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.16.1/selenium-os-4.16.1.pom (2.4 kB at 128 kB/s)
2026-01-22T16:06:54.7051240Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v118/4.16.1/selenium-devtools-v118-4.16.1.pom
2026-01-22T16:06:54.7227934Z Progress (1): 1.1 kB
2026-01-22T16:06:54.7237216Z Progress (1): 2.9 kB
2026-01-22T16:06:54.7237534Z                     
2026-01-22T16:06:54.7237971Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v118/4.16.1/selenium-devtools-v118-4.16.1.pom (2.9 kB at 151 kB/s)
2026-01-22T16:06:54.7251881Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v119/4.16.1/selenium-devtools-v119-4.16.1.pom
2026-01-22T16:06:54.7419641Z Progress (1): 1.1 kB
2026-01-22T16:06:54.7424206Z Progress (1): 2.9 kB
2026-01-22T16:06:54.7428882Z                     
2026-01-22T16:06:54.7429347Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v119/4.16.1/selenium-devtools-v119-4.16.1.pom (2.9 kB at 159 kB/s)
2026-01-22T16:06:54.7446385Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v120/4.16.1/selenium-devtools-v120-4.16.1.pom
2026-01-22T16:06:54.7604567Z Progress (1): 1.1 kB
2026-01-22T16:06:54.7611574Z Progress (1): 2.9 kB
2026-01-22T16:06:54.7612164Z                     
2026-01-22T16:06:54.7612606Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v120/4.16.1/selenium-devtools-v120-4.16.1.pom (2.9 kB at 168 kB/s)
2026-01-22T16:06:54.7638171Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v85/4.16.1/selenium-devtools-v85-4.16.1.pom
2026-01-22T16:06:54.7778851Z Progress (1): 1.1 kB
2026-01-22T16:06:54.7785661Z Progress (1): 2.9 kB
2026-01-22T16:06:54.7788172Z                     
2026-01-22T16:06:54.7789328Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v85/4.16.1/selenium-devtools-v85-4.16.1.pom (2.9 kB at 179 kB/s)
2026-01-22T16:06:54.7808279Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-edge-driver/4.16.1/selenium-edge-driver-4.16.1.pom
2026-01-22T16:06:54.7974261Z Progress (1): 1.1 kB
2026-01-22T16:06:54.7975384Z Progress (1): 3.1 kB
2026-01-22T16:06:54.7975969Z                     
2026-01-22T16:06:54.7976597Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-edge-driver/4.16.1/selenium-edge-driver-4.16.1.pom (3.1 kB at 191 kB/s)
2026-01-22T16:06:54.7988850Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-firefox-driver/4.16.1/selenium-firefox-driver-4.16.1.pom
2026-01-22T16:06:54.8181387Z Progress (1): 1.1 kB
2026-01-22T16:06:54.8189298Z Progress (1): 3.4 kB
2026-01-22T16:06:54.8189599Z                     
2026-01-22T16:06:54.8190025Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-firefox-driver/4.16.1/selenium-firefox-driver-4.16.1.pom (3.4 kB at 172 kB/s)
2026-01-22T16:06:54.8255243Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-ie-driver/4.16.1/selenium-ie-driver-4.16.1.pom
2026-01-22T16:06:54.8409779Z Progress (1): 1.1 kB
2026-01-22T16:06:54.8415238Z Progress (1): 2.9 kB
2026-01-22T16:06:54.8416634Z                     
2026-01-22T16:06:54.8417111Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-ie-driver/4.16.1/selenium-ie-driver-4.16.1.pom (2.9 kB at 179 kB/s)
2026-01-22T16:06:54.8434811Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-safari-driver/4.16.1/selenium-safari-driver-4.16.1.pom
2026-01-22T16:06:54.8597574Z Progress (1): 1.1 kB
2026-01-22T16:06:54.8607393Z Progress (1): 2.7 kB
2026-01-22T16:06:54.8608659Z                     
2026-01-22T16:06:54.8609365Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-safari-driver/4.16.1/selenium-safari-driver-4.16.1.pom (2.7 kB at 157 kB/s)
2026-01-22T16:06:54.8641633Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.16.1/selenium-support-4.16.1.pom
2026-01-22T16:06:54.8813651Z Progress (1): 1.1 kB
2026-01-22T16:06:54.8814307Z Progress (1): 3.2 kB
2026-01-22T16:06:54.8814858Z                     
2026-01-22T16:06:54.8816069Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.16.1/selenium-support-4.16.1.pom (3.2 kB at 200 kB/s)
2026-01-22T16:06:54.8829058Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-core/7.27.2/cucumber-core-7.27.2.pom
2026-01-22T16:06:54.9043435Z Progress (1): 1.3 kB
2026-01-22T16:06:54.9043847Z Progress (1): 6.2 kB
2026-01-22T16:06:54.9044217Z Progress (1): 12 kB 
2026-01-22T16:06:54.9050655Z Progress (1): 13 kB
2026-01-22T16:06:54.9051002Z                    
2026-01-22T16:06:54.9051460Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-core/7.27.2/cucumber-core-7.27.2.pom (13 kB at 585 kB/s)
2026-01-22T16:06:54.9069169Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-jvm/7.27.2/cucumber-jvm-7.27.2.pom
2026-01-22T16:06:54.9247993Z Progress (1): 1.2 kB
2026-01-22T16:06:54.9250493Z Progress (1): 3.7 kB
2026-01-22T16:06:54.9250809Z Progress (1): 8.9 kB
2026-01-22T16:06:54.9251119Z Progress (1): 13 kB 
2026-01-22T16:06:54.9251418Z Progress (1): 18 kB
2026-01-22T16:06:54.9255385Z Progress (1): 20 kB
2026-01-22T16:06:54.9257992Z                    
2026-01-22T16:06:54.9259081Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-jvm/7.27.2/cucumber-jvm-7.27.2.pom (20 kB at 1.1 MB/s)
2026-01-22T16:06:54.9274957Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.3.7/cucumber-parent-4.3.7.pom
2026-01-22T16:06:54.9462406Z Progress (1): 1.2 kB
2026-01-22T16:06:54.9464556Z Progress (1): 3.8 kB
2026-01-22T16:06:54.9467316Z Progress (1): 8.6 kB
2026-01-22T16:06:54.9468203Z Progress (1): 14 kB 
2026-01-22T16:06:54.9473546Z Progress (1): 20 kB
2026-01-22T16:06:54.9475427Z                    
2026-01-22T16:06:54.9476600Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.3.7/cucumber-parent-4.3.7.pom (20 kB at 981 kB/s)
2026-01-22T16:06:54.9513482Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-bom/7.27.2/cucumber-bom-7.27.2.pom
2026-01-22T16:06:54.9690749Z Progress (1): 1.3 kB
2026-01-22T16:06:54.9694039Z Progress (1): 7.4 kB
2026-01-22T16:06:54.9720504Z                     
2026-01-22T16:06:54.9721326Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-bom/7.27.2/cucumber-bom-7.27.2.pom (7.4 kB at 368 kB/s)
2026-01-22T16:06:54.9722079Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.4/junit-bom-5.13.4.pom
2026-01-22T16:06:54.9911379Z Progress (1): 908 B
2026-01-22T16:06:54.9916420Z Progress (1): 4.1 kB
2026-01-22T16:06:54.9918907Z Progress (1): 5.7 kB
2026-01-22T16:06:54.9920324Z                     
2026-01-22T16:06:54.9922146Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.4/junit-bom-5.13.4.pom (5.7 kB at 283 kB/s)
2026-01-22T16:06:54.9936633Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.2/jackson-bom-2.19.2.pom
2026-01-22T16:06:55.0135259Z Progress (1): 926 B
2026-01-22T16:06:55.0138522Z Progress (1): 2.6 kB
2026-01-22T16:06:55.0139634Z Progress (1): 7.3 kB
2026-01-22T16:06:55.0140654Z Progress (1): 16 kB 
2026-01-22T16:06:55.0141684Z Progress (1): 20 kB
2026-01-22T16:06:55.0145330Z Progress (1): 20 kB
2026-01-22T16:06:55.0147072Z                    
2026-01-22T16:06:55.0148213Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.2/jackson-bom-2.19.2.pom (20 kB at 964 kB/s)
2026-01-22T16:06:55.0166567Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19.3/jackson-parent-2.19.3.pom
2026-01-22T16:06:55.0309501Z Progress (1): 1.1 kB
2026-01-22T16:06:55.0310708Z Progress (1): 2.5 kB
2026-01-22T16:06:55.0312135Z Progress (1): 4.2 kB
2026-01-22T16:06:55.0313163Z Progress (1): 6.1 kB
2026-01-22T16:06:55.0314337Z Progress (1): 7.2 kB
2026-01-22T16:06:55.0322572Z                     
2026-01-22T16:06:55.0324001Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19.3/jackson-parent-2.19.3.pom (7.2 kB at 449 kB/s)
2026-01-22T16:06:55.0330867Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/69/oss-parent-69.pom
2026-01-22T16:06:55.0500329Z Progress (1): 949 B
2026-01-22T16:06:55.0501152Z Progress (1): 2.9 kB
2026-01-22T16:06:55.0502248Z Progress (1): 4.1 kB
2026-01-22T16:06:55.0507864Z Progress (1): 6.1 kB
2026-01-22T16:06:55.0509945Z Progress (1): 9.9 kB
2026-01-22T16:06:55.0512042Z Progress (1): 12 kB 
2026-01-22T16:06:55.0524166Z Progress (1): 15 kB
2026-01-22T16:06:55.0525270Z Progress (1): 18 kB
2026-01-22T16:06:55.0526318Z Progress (1): 21 kB
2026-01-22T16:06:55.0527353Z Progress (1): 24 kB
2026-01-22T16:06:55.0528512Z                    
2026-01-22T16:06:55.0529710Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/69/oss-parent-69.pom (24 kB at 1.3 MB/s)
2026-01-22T16:06:55.0546857Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin/7.27.2/cucumber-gherkin-7.27.2.pom
2026-01-22T16:06:55.0725778Z Progress (1): 1.8 kB
2026-01-22T16:06:55.0727671Z                     
2026-01-22T16:06:55.0729019Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin/7.27.2/cucumber-gherkin-7.27.2.pom (1.8 kB at 98 kB/s)
2026-01-22T16:06:55.0753779Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-plugin/7.27.2/cucumber-plugin-7.27.2.pom
2026-01-22T16:06:55.0926797Z Progress (1): 1.8 kB
2026-01-22T16:06:55.0934361Z Progress (1): 1.9 kB
2026-01-22T16:06:55.0936447Z                     
2026-01-22T16:06:55.0937112Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-plugin/7.27.2/cucumber-plugin-7.27.2.pom (1.9 kB at 101 kB/s)
2026-01-22T16:06:55.0965151Z Downloading from central: https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.pom
2026-01-22T16:06:55.1142339Z Progress (1): 1.0 kB
2026-01-22T16:06:55.1145767Z Progress (1): 1.5 kB
2026-01-22T16:06:55.1146567Z                     
2026-01-22T16:06:55.1147698Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.pom (1.5 kB at 85 kB/s)
2026-01-22T16:06:55.1179883Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin-messages/7.27.2/cucumber-gherkin-messages-7.27.2.pom
2026-01-22T16:06:55.1358054Z Progress (1): 1.9 kB
2026-01-22T16:06:55.1359280Z Progress (1): 1.9 kB
2026-01-22T16:06:55.1359986Z                     
2026-01-22T16:06:55.1361680Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin-messages/7.27.2/cucumber-gherkin-messages-7.27.2.pom (1.9 kB at 101 kB/s)
2026-01-22T16:06:55.1404986Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/gherkin/34.0.0/gherkin-34.0.0.pom
2026-01-22T16:06:55.1614931Z Progress (1): 1.2 kB
2026-01-22T16:06:55.1615976Z Progress (1): 4.8 kB
2026-01-22T16:06:55.1616279Z Progress (1): 8.2 kB
2026-01-22T16:06:55.1617323Z                     
2026-01-22T16:06:55.1617750Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/gherkin/34.0.0/gherkin-34.0.0.pom (8.2 kB at 373 kB/s)
2026-01-22T16:06:55.1645429Z Downloading from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-bom/3.27.4/assertj-bom-3.27.4.pom
2026-01-22T16:06:55.1833735Z Progress (1): 1.0 kB
2026-01-22T16:06:55.1834573Z Progress (1): 3.3 kB
2026-01-22T16:06:55.1856774Z                     
2026-01-22T16:06:55.1857632Z Downloaded from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-bom/3.27.4/assertj-bom-3.27.4.pom (3.3 kB at 185 kB/s)
2026-01-22T16:06:55.1858914Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/maven-metadata.xml
2026-01-22T16:06:55.2013268Z Progress (1): 3.2 kB
2026-01-22T16:06:55.2013958Z                     
2026-01-22T16:06:55.2015188Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/maven-metadata.xml (3.2 kB at 185 kB/s)
2026-01-22T16:06:55.2021767Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.4/messages-19.1.4.pom
2026-01-22T16:06:55.2215254Z Progress (1): 1.3 kB
2026-01-22T16:06:55.2235176Z Progress (1): 4.1 kB
2026-01-22T16:06:55.2235667Z                     
2026-01-22T16:06:55.2236186Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.4/messages-19.1.4.pom (4.1 kB at 203 kB/s)
2026-01-22T16:06:55.2250683Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/3.0.0/cucumber-parent-3.0.0.pom
2026-01-22T16:06:55.2433146Z Progress (1): 1.2 kB
2026-01-22T16:06:55.2434064Z Progress (1): 3.7 kB
2026-01-22T16:06:55.2435182Z Progress (1): 8.6 kB
2026-01-22T16:06:55.2435894Z Progress (1): 13 kB 
2026-01-22T16:06:55.2436915Z Progress (1): 19 kB
2026-01-22T16:06:55.2439861Z Progress (1): 22 kB
2026-01-22T16:06:55.2441959Z                    
2026-01-22T16:06:55.2474538Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/3.0.0/cucumber-parent-3.0.0.pom (22 kB at 1.1 MB/s)
2026-01-22T16:06:55.2492329Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.1/junit-bom-5.9.1.pom
2026-01-22T16:06:55.2671184Z Progress (1): 907 B
2026-01-22T16:06:55.2672362Z Progress (1): 4.1 kB
2026-01-22T16:06:55.2685425Z Progress (1): 5.6 kB
2026-01-22T16:06:55.2685900Z                     
2026-01-22T16:06:55.2686465Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.1/junit-bom-5.9.1.pom (5.6 kB at 282 kB/s)
2026-01-22T16:06:55.2726402Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.4/jackson-bom-2.13.4.pom
2026-01-22T16:06:55.2896639Z Progress (1): 931 B
2026-01-22T16:06:55.2899002Z Progress (1): 2.7 kB
2026-01-22T16:06:55.2901005Z Progress (1): 8.7 kB
2026-01-22T16:06:55.2903644Z Progress (1): 17 kB 
2026-01-22T16:06:55.2909407Z Progress (1): 17 kB
2026-01-22T16:06:55.2910874Z                    
2026-01-22T16:06:55.2911526Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.4/jackson-bom-2.13.4.pom (17 kB at 964 kB/s)
2026-01-22T16:06:55.2955353Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.13/jackson-parent-2.13.pom
2026-01-22T16:06:55.3161789Z Progress (1): 1.1 kB
2026-01-22T16:06:55.3162304Z Progress (1): 2.6 kB
2026-01-22T16:06:55.3162973Z Progress (1): 4.1 kB
2026-01-22T16:06:55.3163400Z Progress (1): 6.5 kB
2026-01-22T16:06:55.3163810Z Progress (1): 7.4 kB
2026-01-22T16:06:55.3164203Z                     
2026-01-22T16:06:55.3164717Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.13/jackson-parent-2.13.pom (7.4 kB at 353 kB/s)
2026-01-22T16:06:55.3165389Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/43/oss-parent-43.pom
2026-01-22T16:06:55.3357907Z Progress (1): 949 B
2026-01-22T16:06:55.3363506Z Progress (1): 2.6 kB
2026-01-22T16:06:55.3364031Z Progress (1): 4.0 kB
2026-01-22T16:06:55.3365951Z Progress (1): 6.0 kB
2026-01-22T16:06:55.3366434Z Progress (1): 9.5 kB
2026-01-22T16:06:55.3366849Z Progress (1): 12 kB 
2026-01-22T16:06:55.3367252Z Progress (1): 15 kB
2026-01-22T16:06:55.3367653Z Progress (1): 18 kB
2026-01-22T16:06:55.3368083Z Progress (1): 21 kB
2026-01-22T16:06:55.3383302Z Progress (1): 24 kB
2026-01-22T16:06:55.3383853Z                    
2026-01-22T16:06:55.3384275Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/43/oss-parent-43.pom (24 kB at 1.1 MB/s)
2026-01-22T16:06:55.3421315Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/20.0.0/messages-20.0.0.pom
2026-01-22T16:06:55.3608080Z Progress (1): 1.3 kB
2026-01-22T16:06:55.3608425Z Progress (1): 4.2 kB
2026-01-22T16:06:55.3608701Z                     
2026-01-22T16:06:55.3609090Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/20.0.0/messages-20.0.0.pom (4.2 kB at 222 kB/s)
2026-01-22T16:06:55.3640859Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.1.1/cucumber-parent-4.1.1.pom
2026-01-22T16:06:55.3820689Z Progress (1): 1.2 kB
2026-01-22T16:06:55.3826710Z Progress (1): 3.9 kB
2026-01-22T16:06:55.3828656Z Progress (1): 7.0 kB
2026-01-22T16:06:55.3830264Z Progress (1): 12 kB 
2026-01-22T16:06:55.3831739Z Progress (1): 17 kB
2026-01-22T16:06:55.3838397Z Progress (1): 21 kB
2026-01-22T16:06:55.3842572Z                    
2026-01-22T16:06:55.3843561Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.1.1/cucumber-parent-4.1.1.pom (21 kB at 1.0 MB/s)
2026-01-22T16:06:55.3884846Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.0/jackson-bom-2.14.0.pom
2026-01-22T16:06:55.4039884Z Progress (1): 924 B
2026-01-22T16:06:55.4040211Z Progress (1): 2.7 kB
2026-01-22T16:06:55.4040519Z Progress (1): 8.1 kB
2026-01-22T16:06:55.4040822Z Progress (1): 17 kB 
2026-01-22T16:06:55.4049375Z Progress (1): 17 kB
2026-01-22T16:06:55.4054150Z                    
2026-01-22T16:06:55.4058874Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.0/jackson-bom-2.14.0.pom (17 kB at 972 kB/s)
2026-01-22T16:06:55.4084118Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.14/jackson-parent-2.14.pom
2026-01-22T16:06:55.4246473Z Progress (1): 1.1 kB
2026-01-22T16:06:55.4247435Z Progress (1): 2.5 kB
2026-01-22T16:06:55.4250417Z Progress (1): 4.0 kB
2026-01-22T16:06:55.4250754Z Progress (1): 6.5 kB
2026-01-22T16:06:55.4251063Z Progress (1): 7.7 kB
2026-01-22T16:06:55.4254152Z                     
2026-01-22T16:06:55.4254870Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.14/jackson-parent-2.14.pom (7.7 kB at 450 kB/s)
2026-01-22T16:06:55.4272345Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/48/oss-parent-48.pom
2026-01-22T16:06:55.4441984Z Progress (1): 948 B
2026-01-22T16:06:55.4444391Z Progress (1): 2.6 kB
2026-01-22T16:06:55.4444741Z Progress (1): 4.0 kB
2026-01-22T16:06:55.4445071Z Progress (1): 6.0 kB
2026-01-22T16:06:55.4445409Z Progress (1): 9.7 kB
2026-01-22T16:06:55.4445740Z Progress (1): 12 kB 
2026-01-22T16:06:55.4446098Z Progress (1): 15 kB
2026-01-22T16:06:55.4446455Z Progress (1): 18 kB
2026-01-22T16:06:55.4446789Z Progress (1): 21 kB
2026-01-22T16:06:55.4447098Z Progress (1): 24 kB
2026-01-22T16:06:55.4447377Z                    
2026-01-22T16:06:55.4447757Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/48/oss-parent-48.pom (24 kB at 1.3 MB/s)
2026-01-22T16:06:55.4487257Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/21.0.1/messages-21.0.1.pom
2026-01-22T16:06:55.4641479Z Progress (1): 1.2 kB
2026-01-22T16:06:55.4647244Z Progress (1): 4.4 kB
2026-01-22T16:06:55.4673750Z                     
2026-01-22T16:06:55.4674490Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/21.0.1/messages-21.0.1.pom (4.4 kB at 278 kB/s)
2026-01-22T16:06:55.4699775Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.1/jackson-bom-2.14.1.pom
2026-01-22T16:06:55.4874222Z Progress (1): 924 B
2026-01-22T16:06:55.4877122Z Progress (1): 2.7 kB
2026-01-22T16:06:55.4879975Z Progress (1): 8.1 kB
2026-01-22T16:06:55.4883894Z Progress (1): 17 kB 
2026-01-22T16:06:55.4884213Z Progress (1): 17 kB
2026-01-22T16:06:55.4904531Z                    
2026-01-22T16:06:55.4905262Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.1/jackson-bom-2.14.1.pom (17 kB at 920 kB/s)
2026-01-22T16:06:55.4922545Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/22.0.0/messages-22.0.0.pom
2026-01-22T16:06:55.5071553Z Progress (1): 1.2 kB
2026-01-22T16:06:55.5081827Z Progress (1): 4.4 kB
2026-01-22T16:06:55.5086782Z                     
2026-01-22T16:06:55.5091571Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/22.0.0/messages-22.0.0.pom (4.4 kB at 278 kB/s)
2026-01-22T16:06:55.5122191Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.2/junit-bom-5.9.2.pom
2026-01-22T16:06:55.5259782Z Progress (1): 907 B
2026-01-22T16:06:55.5264787Z Progress (1): 4.1 kB
2026-01-22T16:06:55.5268635Z Progress (1): 5.6 kB
2026-01-22T16:06:55.5270957Z                     
2026-01-22T16:06:55.5271468Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.2/junit-bom-5.9.2.pom (5.6 kB at 375 kB/s)
2026-01-22T16:06:55.5293255Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.2/jackson-bom-2.14.2.pom
2026-01-22T16:06:55.5444251Z Progress (1): 924 B
2026-01-22T16:06:55.5444615Z Progress (1): 2.7 kB
2026-01-22T16:06:55.5444915Z Progress (1): 8.1 kB
2026-01-22T16:06:55.5445241Z Progress (1): 17 kB 
2026-01-22T16:06:55.5445530Z Progress (1): 17 kB
2026-01-22T16:06:55.5445813Z                    
2026-01-22T16:06:55.5446219Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.2/jackson-bom-2.14.2.pom (17 kB at 1.2 MB/s)
2026-01-22T16:06:55.5494971Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/23.0.0/messages-23.0.0.pom
2026-01-22T16:06:55.5650728Z Progress (1): 1.2 kB
2026-01-22T16:06:55.5656036Z Progress (1): 4.4 kB
2026-01-22T16:06:55.5665802Z Progress (1): 4.4 kB
2026-01-22T16:06:55.5668868Z                     
2026-01-22T16:06:55.5669427Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/23.0.0/messages-23.0.0.pom (4.4 kB at 234 kB/s)
2026-01-22T16:06:55.5704941Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.15.3/jackson-bom-2.15.3.pom
2026-01-22T16:06:55.5896031Z Progress (1): 924 B
2026-01-22T16:06:55.5897928Z Progress (1): 2.7 kB
2026-01-22T16:06:55.5898239Z Progress (1): 8.1 kB
2026-01-22T16:06:55.5898542Z Progress (1): 17 kB 
2026-01-22T16:06:55.5898829Z Progress (1): 18 kB
2026-01-22T16:06:55.5899110Z                    
2026-01-22T16:06:55.5899515Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.15.3/jackson-bom-2.15.3.pom (18 kB at 947 kB/s)
2026-01-22T16:06:55.5926451Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.15/jackson-parent-2.15.pom
2026-01-22T16:06:55.6106712Z Progress (1): 1.1 kB
2026-01-22T16:06:55.6108771Z Progress (1): 2.6 kB
2026-01-22T16:06:55.6110829Z Progress (1): 4.1 kB
2026-01-22T16:06:55.6113205Z Progress (1): 6.5 kB
2026-01-22T16:06:55.6115315Z                     
2026-01-22T16:06:55.6116856Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.15/jackson-parent-2.15.pom (6.5 kB at 343 kB/s)
2026-01-22T16:06:55.6129051Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/50/oss-parent-50.pom
2026-01-22T16:06:55.6286232Z Progress (1): 948 B
2026-01-22T16:06:55.6290005Z Progress (1): 2.6 kB
2026-01-22T16:06:55.6292319Z Progress (1): 4.0 kB
2026-01-22T16:06:55.6293630Z Progress (1): 6.0 kB
2026-01-22T16:06:55.6295462Z Progress (1): 9.6 kB
2026-01-22T16:06:55.6296816Z Progress (1): 12 kB 
2026-01-22T16:06:55.6298151Z Progress (1): 15 kB
2026-01-22T16:06:55.6299351Z Progress (1): 18 kB
2026-01-22T16:06:55.6300170Z Progress (1): 21 kB
2026-01-22T16:06:55.6300989Z Progress (1): 24 kB
2026-01-22T16:06:55.6302162Z                    
2026-01-22T16:06:55.6303329Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/50/oss-parent-50.pom (24 kB at 1.4 MB/s)
2026-01-22T16:06:55.6326684Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.0.0/messages-24.0.0.pom
2026-01-22T16:06:55.6582332Z Progress (1): 1.2 kB
2026-01-22T16:06:55.6584916Z Progress (1): 4.4 kB
2026-01-22T16:06:55.6588092Z Progress (1): 4.4 kB
2026-01-22T16:06:55.6589553Z                     
2026-01-22T16:06:55.6590828Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.0.0/messages-24.0.0.pom (4.4 kB at 171 kB/s)
2026-01-22T16:06:55.6610744Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.1/junit-bom-5.10.1.pom
2026-01-22T16:06:55.6755479Z Progress (1): 908 B
2026-01-22T16:06:55.6757192Z Progress (1): 4.1 kB
2026-01-22T16:06:55.6761313Z Progress (1): 5.6 kB
2026-01-22T16:06:55.6762491Z                     
2026-01-22T16:06:55.6764520Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.1/junit-bom-5.10.1.pom (5.6 kB at 377 kB/s)
2026-01-22T16:06:55.6778255Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.16.0/jackson-bom-2.16.0.pom
2026-01-22T16:06:55.6941217Z Progress (1): 924 B
2026-01-22T16:06:55.6943392Z Progress (1): 2.7 kB
2026-01-22T16:06:55.6946174Z Progress (1): 8.1 kB
2026-01-22T16:06:55.6948659Z Progress (1): 17 kB 
2026-01-22T16:06:55.6951070Z Progress (1): 18 kB
2026-01-22T16:06:55.6952298Z                    
2026-01-22T16:06:55.6953496Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.16.0/jackson-bom-2.16.0.pom (18 kB at 1.1 MB/s)
2026-01-22T16:06:55.6970765Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.16/jackson-parent-2.16.pom
2026-01-22T16:06:55.7142027Z Progress (1): 1.1 kB
2026-01-22T16:06:55.7143368Z Progress (1): 2.5 kB
2026-01-22T16:06:55.7144486Z Progress (1): 4.0 kB
2026-01-22T16:06:55.7146364Z Progress (1): 6.5 kB
2026-01-22T16:06:55.7147529Z                     
2026-01-22T16:06:55.7148743Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.16/jackson-parent-2.16.pom (6.5 kB at 362 kB/s)
2026-01-22T16:06:55.7158950Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/56/oss-parent-56.pom
2026-01-22T16:06:55.7319050Z Progress (1): 947 B
2026-01-22T16:06:55.7320926Z Progress (1): 2.6 kB
2026-01-22T16:06:55.7326169Z Progress (1): 4.0 kB
2026-01-22T16:06:55.7327792Z Progress (1): 6.4 kB
2026-01-22T16:06:55.7329001Z Progress (1): 9.6 kB
2026-01-22T16:06:55.7330145Z Progress (1): 12 kB 
2026-01-22T16:06:55.7331821Z Progress (1): 15 kB
2026-01-22T16:06:55.7333023Z Progress (1): 18 kB
2026-01-22T16:06:55.7334419Z Progress (1): 21 kB
2026-01-22T16:06:55.7334733Z Progress (1): 24 kB
2026-01-22T16:06:55.7335016Z                    
2026-01-22T16:06:55.7335377Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/56/oss-parent-56.pom (24 kB at 1.4 MB/s)
2026-01-22T16:06:55.7360391Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.0.1/messages-24.0.1.pom
2026-01-22T16:06:55.7534221Z Progress (1): 1.3 kB
2026-01-22T16:06:55.7534575Z Progress (1): 4.4 kB
2026-01-22T16:06:55.7534870Z                     
2026-01-22T16:06:55.7535260Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.0.1/messages-24.0.1.pom (4.4 kB at 261 kB/s)
2026-01-22T16:06:55.7550678Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.1.0/messages-24.1.0.pom
2026-01-22T16:06:55.7705584Z Progress (1): 1.3 kB
2026-01-22T16:06:55.7708217Z Progress (1): 4.6 kB
2026-01-22T16:06:55.7712116Z Progress (1): 4.7 kB
2026-01-22T16:06:55.7714584Z                     
2026-01-22T16:06:55.7716716Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.1.0/messages-24.1.0.pom (4.7 kB at 296 kB/s)
2026-01-22T16:06:55.7725887Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.2.0/cucumber-parent-4.2.0.pom
2026-01-22T16:06:55.7901357Z Progress (1): 1.2 kB
2026-01-22T16:06:55.7902035Z Progress (1): 3.8 kB
2026-01-22T16:06:55.7903456Z Progress (1): 7.0 kB
2026-01-22T16:06:55.7904023Z Progress (1): 12 kB 
2026-01-22T16:06:55.7904919Z Progress (1): 17 kB
2026-01-22T16:06:55.7905462Z Progress (1): 21 kB
2026-01-22T16:06:55.7906312Z                    
2026-01-22T16:06:55.7907045Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.2.0/cucumber-parent-4.2.0.pom (21 kB at 1.2 MB/s)
2026-01-22T16:06:55.7941227Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom
2026-01-22T16:06:55.8108488Z Progress (1): 908 B
2026-01-22T16:06:55.8113970Z Progress (1): 4.1 kB
2026-01-22T16:06:55.8116104Z Progress (1): 5.6 kB
2026-01-22T16:06:55.8118277Z                     
2026-01-22T16:06:55.8120600Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom (5.6 kB at 314 kB/s)
2026-01-22T16:06:55.8134492Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.0/jackson-bom-2.17.0.pom
2026-01-22T16:06:55.8282144Z Progress (1): 924 B
2026-01-22T16:06:55.8283360Z Progress (1): 2.7 kB
2026-01-22T16:06:55.8284398Z Progress (1): 8.1 kB
2026-01-22T16:06:55.8286002Z Progress (1): 17 kB 
2026-01-22T16:06:55.8287474Z Progress (1): 19 kB
2026-01-22T16:06:55.8288776Z                    
2026-01-22T16:06:55.8289957Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.0/jackson-bom-2.17.0.pom (19 kB at 1.2 MB/s)
2026-01-22T16:06:55.8302681Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.17/jackson-parent-2.17.pom
2026-01-22T16:06:55.8450486Z Progress (1): 1.1 kB
2026-01-22T16:06:55.8450826Z Progress (1): 2.5 kB
2026-01-22T16:06:55.8451154Z Progress (1): 4.0 kB
2026-01-22T16:06:55.8451465Z Progress (1): 6.5 kB
2026-01-22T16:06:55.8451767Z                     
2026-01-22T16:06:55.8452215Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.17/jackson-parent-2.17.pom (6.5 kB at 466 kB/s)
2026-01-22T16:06:55.8472550Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/58/oss-parent-58.pom
2026-01-22T16:06:55.8654628Z Progress (1): 947 B
2026-01-22T16:06:55.8656183Z Progress (1): 2.6 kB
2026-01-22T16:06:55.8656757Z Progress (1): 4.0 kB
2026-01-22T16:06:55.8658367Z Progress (1): 6.0 kB
2026-01-22T16:06:55.8659904Z Progress (1): 9.6 kB
2026-01-22T16:06:55.8660439Z Progress (1): 12 kB 
2026-01-22T16:06:55.8661858Z Progress (1): 15 kB
2026-01-22T16:06:55.8662656Z Progress (1): 18 kB
2026-01-22T16:06:55.8663348Z Progress (1): 21 kB
2026-01-22T16:06:55.8664518Z Progress (1): 24 kB
2026-01-22T16:06:55.8664980Z                    
2026-01-22T16:06:55.8665497Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/58/oss-parent-58.pom (24 kB at 1.2 MB/s)
2026-01-22T16:06:55.8705303Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/25.0.0/messages-25.0.0.pom
2026-01-22T16:06:55.8873027Z Progress (1): 1.3 kB
2026-01-22T16:06:55.8878070Z Progress (1): 4.6 kB
2026-01-22T16:06:55.8882059Z Progress (1): 4.7 kB
2026-01-22T16:06:55.8887027Z                     
2026-01-22T16:06:55.8889149Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/25.0.0/messages-25.0.0.pom (4.7 kB at 278 kB/s)
2026-01-22T16:06:55.8901247Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.1/jackson-bom-2.17.1.pom
2026-01-22T16:06:55.9054063Z Progress (1): 924 B
2026-01-22T16:06:55.9059450Z Progress (1): 2.7 kB
2026-01-22T16:06:55.9062092Z Progress (1): 8.1 kB
2026-01-22T16:06:55.9063094Z Progress (1): 17 kB 
2026-01-22T16:06:55.9063750Z Progress (1): 19 kB
2026-01-22T16:06:55.9064046Z                    
2026-01-22T16:06:55.9064441Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.1/jackson-bom-2.17.1.pom (19 kB at 1.2 MB/s)
2026-01-22T16:06:55.9093069Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/25.0.1/messages-25.0.1.pom
2026-01-22T16:06:55.9250282Z Progress (1): 1.2 kB
2026-01-22T16:06:55.9251601Z Progress (1): 4.6 kB
2026-01-22T16:06:55.9255229Z Progress (1): 4.7 kB
2026-01-22T16:06:55.9258225Z                     
2026-01-22T16:06:55.9258916Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/25.0.1/messages-25.0.1.pom (4.7 kB at 278 kB/s)
2026-01-22T16:06:55.9281897Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/26.0.0/messages-26.0.0.pom
2026-01-22T16:06:55.9457016Z Progress (1): 1.3 kB
2026-01-22T16:06:55.9459838Z Progress (1): 4.6 kB
2026-01-22T16:06:55.9460164Z Progress (1): 4.7 kB
2026-01-22T16:06:55.9460444Z                     
2026-01-22T16:06:55.9460839Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/26.0.0/messages-26.0.0.pom (4.7 kB at 263 kB/s)
2026-01-22T16:06:55.9495332Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom
2026-01-22T16:06:55.9684158Z Progress (1): 908 B
2026-01-22T16:06:55.9694075Z Progress (1): 4.1 kB
2026-01-22T16:06:55.9699368Z Progress (1): 5.6 kB
2026-01-22T16:06:55.9703437Z                     
2026-01-22T16:06:55.9704137Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom (5.6 kB at 282 kB/s)
2026-01-22T16:06:55.9726902Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.2/jackson-bom-2.17.2.pom
2026-01-22T16:06:55.9904160Z Progress (1): 924 B
2026-01-22T16:06:55.9907291Z Progress (1): 2.7 kB
2026-01-22T16:06:55.9908899Z Progress (1): 8.1 kB
2026-01-22T16:06:55.9909320Z Progress (1): 17 kB 
2026-01-22T16:06:55.9909795Z Progress (1): 19 kB
2026-01-22T16:06:55.9912411Z                    
2026-01-22T16:06:55.9913106Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.2/jackson-bom-2.17.2.pom (19 kB at 1.0 MB/s)
2026-01-22T16:06:55.9953332Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/26.0.1/messages-26.0.1.pom
2026-01-22T16:06:56.0118776Z Progress (1): 1.2 kB
2026-01-22T16:06:56.0121196Z Progress (1): 4.6 kB
2026-01-22T16:06:56.0121507Z Progress (1): 4.7 kB
2026-01-22T16:06:56.0121777Z                     
2026-01-22T16:06:56.0122189Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/26.0.1/messages-26.0.1.pom (4.7 kB at 278 kB/s)
2026-01-22T16:06:56.0150303Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.0/messages-27.0.0.pom
2026-01-22T16:06:56.0323029Z Progress (1): 1.2 kB
2026-01-22T16:06:56.0328470Z Progress (1): 4.6 kB
2026-01-22T16:06:56.0332656Z Progress (1): 4.7 kB
2026-01-22T16:06:56.0336843Z                     
2026-01-22T16:06:56.0341074Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.0/messages-27.0.0.pom (4.7 kB at 263 kB/s)
2026-01-22T16:06:56.0348142Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.3/junit-bom-5.11.3.pom
2026-01-22T16:06:56.0501615Z Progress (1): 908 B
2026-01-22T16:06:56.0504683Z Progress (1): 4.1 kB
2026-01-22T16:06:56.0507299Z Progress (1): 5.6 kB
2026-01-22T16:06:56.0509277Z                     
2026-01-22T16:06:56.0511102Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.3/junit-bom-5.11.3.pom (5.6 kB at 353 kB/s)
2026-01-22T16:06:56.0522686Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.0/jackson-bom-2.18.0.pom
2026-01-22T16:06:56.0678751Z Progress (1): 924 B
2026-01-22T16:06:56.0681362Z Progress (1): 2.7 kB
2026-01-22T16:06:56.0685826Z Progress (1): 8.1 kB
2026-01-22T16:06:56.0687840Z Progress (1): 17 kB 
2026-01-22T16:06:56.0690912Z Progress (1): 19 kB
2026-01-22T16:06:56.0691222Z                    
2026-01-22T16:06:56.0691628Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.0/jackson-bom-2.18.0.pom (19 kB at 1.2 MB/s)
2026-01-22T16:06:56.0711385Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.18/jackson-parent-2.18.pom
2026-01-22T16:06:56.0958160Z Progress (1): 1.1 kB
2026-01-22T16:06:56.0958866Z Progress (1): 2.5 kB
2026-01-22T16:06:56.0962930Z Progress (1): 4.0 kB
2026-01-22T16:06:56.0963301Z Progress (1): 6.5 kB
2026-01-22T16:06:56.0965485Z                     
2026-01-22T16:06:56.0965958Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.18/jackson-parent-2.18.pom (6.5 kB at 251 kB/s)
2026-01-22T16:06:56.0978908Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/61/oss-parent-61.pom
2026-01-22T16:06:56.1131525Z Progress (1): 952 B
2026-01-22T16:06:56.1134413Z Progress (1): 2.6 kB
2026-01-22T16:06:56.1135906Z Progress (1): 4.1 kB
2026-01-22T16:06:56.1136755Z Progress (1): 7.2 kB
2026-01-22T16:06:56.1137650Z Progress (1): 9.7 kB
2026-01-22T16:06:56.1137954Z Progress (1): 12 kB 
2026-01-22T16:06:56.1138243Z Progress (1): 15 kB
2026-01-22T16:06:56.1138528Z Progress (1): 18 kB
2026-01-22T16:06:56.1138816Z Progress (1): 23 kB
2026-01-22T16:06:56.1142266Z Progress (1): 23 kB
2026-01-22T16:06:56.1143143Z                    
2026-01-22T16:06:56.1145649Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/61/oss-parent-61.pom (23 kB at 1.4 MB/s)
2026-01-22T16:06:56.1171337Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.1/messages-27.0.1.pom
2026-01-22T16:06:56.1326874Z Progress (1): 1.2 kB
2026-01-22T16:06:56.1328042Z Progress (1): 4.6 kB
2026-01-22T16:06:56.1331526Z Progress (1): 4.7 kB
2026-01-22T16:06:56.1332430Z                     
2026-01-22T16:06:56.1334801Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.1/messages-27.0.1.pom (4.7 kB at 278 kB/s)
2026-01-22T16:06:56.1349547Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.1/jackson-bom-2.18.1.pom
2026-01-22T16:06:56.1529575Z Progress (1): 933 B
2026-01-22T16:06:56.1530481Z Progress (1): 2.7 kB
2026-01-22T16:06:56.1531100Z Progress (1): 8.1 kB
2026-01-22T16:06:56.1531577Z Progress (1): 17 kB 
2026-01-22T16:06:56.1538383Z Progress (1): 19 kB
2026-01-22T16:06:56.1553785Z                    
2026-01-22T16:06:56.1554690Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.1/jackson-bom-2.18.1.pom (19 kB at 984 kB/s)
2026-01-22T16:06:56.1589359Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.18.1/jackson-parent-2.18.1.pom
2026-01-22T16:06:56.1767684Z Progress (1): 1.1 kB
2026-01-22T16:06:56.1768219Z Progress (1): 2.5 kB
2026-01-22T16:06:56.1772955Z Progress (1): 4.1 kB
2026-01-22T16:06:56.1773735Z Progress (1): 6.3 kB
2026-01-22T16:06:56.1784445Z Progress (1): 6.7 kB
2026-01-22T16:06:56.1785052Z                     
2026-01-22T16:06:56.1785918Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.18.1/jackson-parent-2.18.1.pom (6.7 kB at 352 kB/s)
2026-01-22T16:06:56.1821999Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.2/messages-27.0.2.pom
2026-01-22T16:06:56.1968478Z Progress (1): 1.2 kB
2026-01-22T16:06:56.1969694Z Progress (1): 4.6 kB
2026-01-22T16:06:56.1973523Z Progress (1): 4.7 kB
2026-01-22T16:06:56.1975079Z                     
2026-01-22T16:06:56.1975599Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.2/messages-27.0.2.pom (4.7 kB at 296 kB/s)
2026-01-22T16:06:56.2000997Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.1.0/messages-27.1.0.pom
2026-01-22T16:06:56.2145342Z Progress (1): 1.2 kB
2026-01-22T16:06:56.2147087Z Progress (1): 4.6 kB
2026-01-22T16:06:56.2150375Z Progress (1): 4.7 kB
2026-01-22T16:06:56.2151820Z                     
2026-01-22T16:06:56.2152315Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.1.0/messages-27.1.0.pom (4.7 kB at 315 kB/s)
2026-01-22T16:06:56.2175073Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom
2026-01-22T16:06:56.2643190Z Progress (1): 918 B
2026-01-22T16:06:56.2643766Z Progress (1): 4.5 kB
2026-01-22T16:06:56.2646826Z Progress (1): 5.6 kB
2026-01-22T16:06:56.2648177Z                     
2026-01-22T16:06:56.2648768Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom (5.6 kB at 120 kB/s)
2026-01-22T16:06:56.2662090Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.2/jackson-bom-2.18.2.pom
2026-01-22T16:06:56.2894354Z Progress (1): 926 B
2026-01-22T16:06:56.2896913Z Progress (1): 2.7 kB
2026-01-22T16:06:56.2898071Z Progress (1): 8.4 kB
2026-01-22T16:06:56.2901882Z Progress (1): 16 kB 
2026-01-22T16:06:56.2907134Z Progress (1): 19 kB
2026-01-22T16:06:56.2908920Z                    
2026-01-22T16:06:56.2910477Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.2/jackson-bom-2.18.2.pom (19 kB at 748 kB/s)
2026-01-22T16:06:56.2935627Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.2.0/messages-27.2.0.pom
2026-01-22T16:06:56.3227345Z Progress (1): 1.2 kB
2026-01-22T16:06:56.3229542Z Progress (1): 4.6 kB
2026-01-22T16:06:56.3232428Z Progress (1): 4.7 kB
2026-01-22T16:06:56.3235330Z                     
2026-01-22T16:06:56.3236840Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.2.0/messages-27.2.0.pom (4.7 kB at 158 kB/s)
2026-01-22T16:06:56.3276114Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/28.0.0/messages-28.0.0.pom
2026-01-22T16:06:56.3691074Z Progress (1): 1.2 kB
2026-01-22T16:06:56.3695730Z Progress (1): 4.6 kB
2026-01-22T16:06:56.3698334Z Progress (1): 4.7 kB
2026-01-22T16:06:56.3698676Z                     
2026-01-22T16:06:56.3699088Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/28.0.0/messages-28.0.0.pom (4.7 kB at 108 kB/s)
2026-01-22T16:06:56.3722477Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.3/junit-bom-5.13.3.pom
2026-01-22T16:06:56.3885347Z Progress (1): 908 B
2026-01-22T16:06:56.3885687Z Progress (1): 4.1 kB
2026-01-22T16:06:56.3888496Z Progress (1): 5.7 kB
2026-01-22T16:06:56.3889830Z                     
2026-01-22T16:06:56.3891145Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.3/junit-bom-5.13.3.pom (5.7 kB at 333 kB/s)
2026-01-22T16:06:56.3913212Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.1/jackson-bom-2.19.1.pom
2026-01-22T16:06:56.4082949Z Progress (1): 926 B
2026-01-22T16:06:56.4085825Z Progress (1): 2.6 kB
2026-01-22T16:06:56.4086190Z Progress (1): 7.3 kB
2026-01-22T16:06:56.4088218Z Progress (1): 16 kB 
2026-01-22T16:06:56.4088555Z Progress (1): 20 kB
2026-01-22T16:06:56.4090460Z Progress (1): 20 kB
2026-01-22T16:06:56.4091695Z                    
2026-01-22T16:06:56.4093086Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.1/jackson-bom-2.19.1.pom (20 kB at 1.1 MB/s)
2026-01-22T16:06:56.4106504Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19.2/jackson-parent-2.19.2.pom
2026-01-22T16:06:56.4287873Z Progress (1): 1.1 kB
2026-01-22T16:06:56.4292089Z Progress (1): 2.5 kB
2026-01-22T16:06:56.4293576Z Progress (1): 4.2 kB
2026-01-22T16:06:56.4293961Z Progress (1): 6.1 kB
2026-01-22T16:06:56.4295152Z Progress (1): 7.2 kB
2026-01-22T16:06:56.4300782Z                     
2026-01-22T16:06:56.4301925Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19.2/jackson-parent-2.19.2.pom (7.2 kB at 378 kB/s)
2026-01-22T16:06:56.4309961Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/68/oss-parent-68.pom
2026-01-22T16:06:56.4480553Z Progress (1): 948 B
2026-01-22T16:06:56.4484231Z Progress (1): 2.9 kB
2026-01-22T16:06:56.4485429Z Progress (1): 4.1 kB
2026-01-22T16:06:56.4486144Z Progress (1): 6.1 kB
2026-01-22T16:06:56.4486746Z Progress (1): 9.9 kB
2026-01-22T16:06:56.4489864Z Progress (1): 12 kB 
2026-01-22T16:06:56.4491189Z Progress (1): 15 kB
2026-01-22T16:06:56.4492196Z Progress (1): 18 kB
2026-01-22T16:06:56.4493511Z Progress (1): 21 kB
2026-01-22T16:06:56.4494480Z Progress (1): 24 kB
2026-01-22T16:06:56.4495741Z                    
2026-01-22T16:06:56.4496880Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/68/oss-parent-68.pom (24 kB at 1.3 MB/s)
2026-01-22T16:06:56.4519428Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/28.1.0/messages-28.1.0.pom
2026-01-22T16:06:56.4687051Z Progress (1): 1.2 kB
2026-01-22T16:06:56.4688607Z Progress (1): 4.8 kB
2026-01-22T16:06:56.4690744Z Progress (1): 5.0 kB
2026-01-22T16:06:56.4703074Z                     
2026-01-22T16:06:56.4705201Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/28.1.0/messages-28.1.0.pom (5.0 kB at 292 kB/s)
2026-01-22T16:06:56.4714306Z Downloading from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-bom/3.27.3/assertj-bom-3.27.3.pom
2026-01-22T16:06:56.4872385Z Progress (1): 1.0 kB
2026-01-22T16:06:56.4877545Z Progress (1): 3.7 kB
2026-01-22T16:06:56.4878852Z                     
2026-01-22T16:06:56.4879967Z Downloaded from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-bom/3.27.3/assertj-bom-3.27.3.pom (3.7 kB at 230 kB/s)
2026-01-22T16:06:56.4901719Z Downloading from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-core/3.27.4/assertj-core-3.27.4.pom
2026-01-22T16:06:56.5081654Z Progress (1): 1.2 kB
2026-01-22T16:06:56.5082672Z Progress (1): 3.8 kB
2026-01-22T16:06:56.5084219Z                     
2026-01-22T16:06:56.5085312Z Downloaded from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-core/3.27.4/assertj-core-3.27.4.pom (3.8 kB at 238 kB/s)
2026-01-22T16:06:56.5086755Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.15.11/byte-buddy-1.15.11.pom
2026-01-22T16:06:56.5249772Z Progress (1): 948 B
2026-01-22T16:06:56.5250092Z Progress (1): 3.7 kB
2026-01-22T16:06:56.5250381Z Progress (1): 6.8 kB
2026-01-22T16:06:56.5250652Z Progress (1): 15 kB 
2026-01-22T16:06:56.5250930Z Progress (1): 17 kB
2026-01-22T16:06:56.5251189Z                    
2026-01-22T16:06:56.5251563Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.15.11/byte-buddy-1.15.11.pom (17 kB at 1.0 MB/s)
2026-01-22T16:06:56.5268036Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.15.11/byte-buddy-parent-1.15.11.pom
2026-01-22T16:06:56.5436737Z Progress (1): 829 B
2026-01-22T16:06:56.5437453Z Progress (1): 2.1 kB
2026-01-22T16:06:56.5438321Z Progress (1): 3.6 kB
2026-01-22T16:06:56.5440486Z Progress (1): 6.2 kB
2026-01-22T16:06:56.5443024Z Progress (1): 8.0 kB
2026-01-22T16:06:56.5445072Z Progress (1): 11 kB 
2026-01-22T16:06:56.5447432Z Progress (1): 13 kB
2026-01-22T16:06:56.5449236Z Progress (1): 17 kB
2026-01-22T16:06:56.5450441Z Progress (1): 22 kB
2026-01-22T16:06:56.5451563Z Progress (1): 25 kB
2026-01-22T16:06:56.5452559Z Progress (1): 34 kB
2026-01-22T16:06:56.5454005Z Progress (1): 47 kB
2026-01-22T16:06:56.5455036Z Progress (1): 52 kB
2026-01-22T16:06:56.5456008Z Progress (1): 57 kB
2026-01-22T16:06:56.5457029Z Progress (1): 63 kB
2026-01-22T16:06:56.5483450Z Progress (1): 63 kB
2026-01-22T16:06:56.5484164Z                    
2026-01-22T16:06:56.5485367Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.15.11/byte-buddy-parent-1.15.11.pom (63 kB at 3.3 MB/s)
2026-01-22T16:06:56.5502632Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/pretty-formatter/2.1.0/pretty-formatter-2.1.0.pom
2026-01-22T16:06:56.5703510Z Progress (1): 1.2 kB
2026-01-22T16:06:56.5708199Z Progress (1): 3.7 kB
2026-01-22T16:06:56.5708680Z                     
2026-01-22T16:06:56.5709234Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/pretty-formatter/2.1.0/pretty-formatter-2.1.0.pom (3.7 kB at 184 kB/s)
2026-01-22T16:06:56.5742401Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/maven-metadata.xml
2026-01-22T16:06:56.5910955Z Progress (1): 1.1 kB
2026-01-22T16:06:56.5912348Z                     
2026-01-22T16:06:56.5913629Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/maven-metadata.xml (1.1 kB at 66 kB/s)
2026-01-22T16:06:56.5920949Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.5.0/query-13.5.0.pom
2026-01-22T16:06:56.6077266Z Progress (1): 1.2 kB
2026-01-22T16:06:56.6082928Z Progress (1): 3.2 kB
2026-01-22T16:06:56.6084687Z                     
2026-01-22T16:06:56.6085867Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.5.0/query-13.5.0.pom (3.2 kB at 186 kB/s)
2026-01-22T16:06:56.6123771Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.6.0/query-13.6.0.pom
2026-01-22T16:06:56.6307260Z Progress (1): 1.2 kB
2026-01-22T16:06:56.6310946Z Progress (1): 3.2 kB
2026-01-22T16:06:56.6312628Z                     
2026-01-22T16:06:56.6315070Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.6.0/query-13.6.0.pom (3.2 kB at 167 kB/s)
2026-01-22T16:06:56.6332702Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/testng-xml-formatter/0.5.0/testng-xml-formatter-0.5.0.pom
2026-01-22T16:06:56.6530672Z Progress (1): 1.3 kB
2026-01-22T16:06:56.6536911Z Progress (1): 4.1 kB
2026-01-22T16:06:56.6538354Z                     
2026-01-22T16:06:56.6539668Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/testng-xml-formatter/0.5.0/testng-xml-formatter-0.5.0.pom (4.1 kB at 195 kB/s)
2026-01-22T16:06:56.6565930Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.3.0/query-13.3.0.pom
2026-01-22T16:06:56.6710285Z Progress (1): 1.3 kB
2026-01-22T16:06:56.6738078Z Progress (1): 3.2 kB
2026-01-22T16:06:56.6738466Z                     
2026-01-22T16:06:56.6739036Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.3.0/query-13.3.0.pom (3.2 kB at 198 kB/s)
2026-01-22T16:06:56.6739567Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.1/junit-bom-5.13.1.pom
2026-01-22T16:06:56.6903810Z Progress (1): 908 B
2026-01-22T16:06:56.6904221Z Progress (1): 4.1 kB
2026-01-22T16:06:56.6916567Z Progress (1): 5.6 kB
2026-01-22T16:06:56.6916899Z                     
2026-01-22T16:06:56.6917358Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.1/junit-bom-5.13.1.pom (5.6 kB at 314 kB/s)
2026-01-22T16:06:56.6935528Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.0/jackson-bom-2.19.0.pom
2026-01-22T16:06:56.7103770Z Progress (1): 922 B
2026-01-22T16:06:56.7104605Z Progress (1): 2.6 kB
2026-01-22T16:06:56.7105962Z Progress (1): 7.2 kB
2026-01-22T16:06:56.7106784Z Progress (1): 16 kB 
2026-01-22T16:06:56.7107829Z Progress (1): 20 kB
2026-01-22T16:06:56.7108519Z                    
2026-01-22T16:06:56.7109632Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.0/jackson-bom-2.19.0.pom (20 kB at 1.2 MB/s)
2026-01-22T16:06:56.7119695Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19/jackson-parent-2.19.pom
2026-01-22T16:06:56.7315010Z Progress (1): 1.1 kB
2026-01-22T16:06:56.7315703Z Progress (1): 2.5 kB
2026-01-22T16:06:56.7316897Z Progress (1): 4.1 kB
2026-01-22T16:06:56.7317576Z Progress (1): 6.3 kB
2026-01-22T16:06:56.7318711Z Progress (1): 6.7 kB
2026-01-22T16:06:56.7319389Z                     
2026-01-22T16:06:56.7320563Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19/jackson-parent-2.19.pom (6.7 kB at 352 kB/s)
2026-01-22T16:06:56.7325077Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/65/oss-parent-65.pom
2026-01-22T16:06:56.7506676Z Progress (1): 952 B
2026-01-22T16:06:56.7507949Z Progress (1): 2.6 kB
2026-01-22T16:06:56.7510802Z Progress (1): 4.0 kB
2026-01-22T16:06:56.7516227Z Progress (1): 6.6 kB
2026-01-22T16:06:56.7516564Z Progress (1): 9.8 kB
2026-01-22T16:06:56.7525339Z Progress (1): 12 kB 
2026-01-22T16:06:56.7525682Z Progress (1): 15 kB
2026-01-22T16:06:56.7525976Z Progress (1): 18 kB
2026-01-22T16:06:56.7528499Z Progress (1): 23 kB
2026-01-22T16:06:56.7528822Z                    
2026-01-22T16:06:56.7531207Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/65/oss-parent-65.pom (23 kB at 1.1 MB/s)
2026-01-22T16:06:56.7610292Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.4.0/query-13.4.0.pom
2026-01-22T16:06:56.7823396Z Progress (1): 1.2 kB
2026-01-22T16:06:56.7827033Z Progress (1): 3.2 kB
2026-01-22T16:06:56.7827929Z                     
2026-01-22T16:06:56.7829363Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.4.0/query-13.4.0.pom (3.2 kB at 138 kB/s)
2026-01-22T16:06:56.7858842Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/tag-expressions/6.1.2/tag-expressions-6.1.2.pom
2026-01-22T16:06:56.8155040Z Progress (1): 1.3 kB
2026-01-22T16:06:56.8161148Z Progress (1): 2.4 kB
2026-01-22T16:06:56.8162412Z                     
2026-01-22T16:06:56.8163117Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/tag-expressions/6.1.2/tag-expressions-6.1.2.pom (2.4 kB at 77 kB/s)
2026-01-22T16:06:56.8188523Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-expressions/18.0.1/cucumber-expressions-18.0.1.pom
2026-01-22T16:06:56.8348637Z Progress (1): 1.3 kB
2026-01-22T16:06:56.8352943Z Progress (1): 3.3 kB
2026-01-22T16:06:56.8353848Z                     
2026-01-22T16:06:56.8354734Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-expressions/18.0.1/cucumber-expressions-18.0.1.pom (3.3 kB at 196 kB/s)
2026-01-22T16:06:56.8383600Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/datatable/7.27.2/datatable-7.27.2.pom
2026-01-22T16:06:56.8548896Z Progress (1): 1.4 kB
2026-01-22T16:06:56.8549589Z Progress (1): 5.4 kB
2026-01-22T16:06:56.8555311Z Progress (1): 6.0 kB
2026-01-22T16:06:56.8555640Z                     
2026-01-22T16:06:56.8556044Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/datatable/7.27.2/datatable-7.27.2.pom (6.0 kB at 334 kB/s)
2026-01-22T16:06:56.8625763Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/docstring/7.27.2/docstring-7.27.2.pom
2026-01-22T16:06:56.8767691Z Progress (1): 1.6 kB
2026-01-22T16:06:56.8776066Z Progress (1): 2.7 kB
2026-01-22T16:06:56.8776733Z                     
2026-01-22T16:06:56.8777412Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/docstring/7.27.2/docstring-7.27.2.pom (2.7 kB at 157 kB/s)
2026-01-22T16:06:56.8833935Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/html-formatter/21.13.0/html-formatter-21.13.0.pom
2026-01-22T16:06:56.9016657Z Progress (1): 1.2 kB
2026-01-22T16:06:56.9032058Z Progress (1): 3.2 kB
2026-01-22T16:06:56.9032973Z                     
2026-01-22T16:06:56.9033930Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/html-formatter/21.13.0/html-formatter-21.13.0.pom (3.2 kB at 154 kB/s)
2026-01-22T16:06:56.9084015Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/18.0.0/messages-18.0.0.pom
2026-01-22T16:06:56.9241016Z Progress (1): 1.3 kB
2026-01-22T16:06:56.9249583Z Progress (1): 4.0 kB
2026-01-22T16:06:56.9253738Z                     
2026-01-22T16:06:56.9257859Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/18.0.0/messages-18.0.0.pom (4.0 kB at 237 kB/s)
2026-01-22T16:06:56.9275602Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/2.3.2/cucumber-parent-2.3.2.pom
2026-01-22T16:06:56.9459083Z Progress (1): 1.2 kB
2026-01-22T16:06:56.9461906Z Progress (1): 3.7 kB
2026-01-22T16:06:56.9467114Z Progress (1): 8.5 kB
2026-01-22T16:06:56.9469564Z Progress (1): 13 kB 
2026-01-22T16:06:56.9471202Z Progress (1): 18 kB
2026-01-22T16:06:56.9493411Z Progress (1): 22 kB
2026-01-22T16:06:56.9494102Z                    
2026-01-22T16:06:56.9496837Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/2.3.2/cucumber-parent-2.3.2.pom (22 kB at 1.1 MB/s)
2026-01-22T16:06:56.9507538Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.8.2/junit-bom-5.8.2.pom
2026-01-22T16:06:56.9667685Z Progress (1): 907 B
2026-01-22T16:06:56.9671326Z Progress (1): 4.1 kB
2026-01-22T16:06:56.9673413Z Progress (1): 5.6 kB
2026-01-22T16:06:56.9675180Z                     
2026-01-22T16:06:56.9677044Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.8.2/junit-bom-5.8.2.pom (5.6 kB at 352 kB/s)
2026-01-22T16:06:56.9700694Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.2/jackson-bom-2.13.2.pom
2026-01-22T16:06:56.9872493Z Progress (1): 931 B
2026-01-22T16:06:56.9875292Z Progress (1): 2.7 kB
2026-01-22T16:06:56.9875637Z Progress (1): 8.7 kB
2026-01-22T16:06:56.9875959Z Progress (1): 17 kB 
2026-01-22T16:06:56.9880984Z Progress (1): 17 kB
2026-01-22T16:06:56.9883468Z                    
2026-01-22T16:06:56.9884179Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.2/jackson-bom-2.13.2.pom (17 kB at 964 kB/s)
2026-01-22T16:06:56.9906903Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.0.0/messages-19.0.0.pom
2026-01-22T16:06:57.0175944Z Progress (1): 1.3 kB
2026-01-22T16:06:57.0177457Z Progress (1): 4.1 kB
2026-01-22T16:06:57.0178222Z                     
2026-01-22T16:06:57.0179745Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.0.0/messages-19.0.0.pom (4.1 kB at 162 kB/s)
2026-01-22T16:06:57.0180249Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.3/jackson-bom-2.13.3.pom
2026-01-22T16:06:57.0391344Z Progress (1): 931 B
2026-01-22T16:06:57.0397157Z Progress (1): 2.7 kB
2026-01-22T16:06:57.0402509Z Progress (1): 8.9 kB
2026-01-22T16:06:57.0412487Z Progress (1): 17 kB 
2026-01-22T16:06:57.0418303Z Progress (1): 17 kB
2026-01-22T16:06:57.0418899Z                    
2026-01-22T16:06:57.0419550Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.3/jackson-bom-2.13.3.pom (17 kB at 723 kB/s)
2026-01-22T16:06:57.0455094Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.0/messages-19.1.0.pom
2026-01-22T16:06:57.0668443Z Progress (1): 1.3 kB
2026-01-22T16:06:57.0675441Z Progress (1): 4.1 kB
2026-01-22T16:06:57.0678211Z                     
2026-01-22T16:06:57.0679531Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.0/messages-19.1.0.pom (4.1 kB at 185 kB/s)
2026-01-22T16:06:57.0694032Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.1/messages-19.1.1.pom
2026-01-22T16:06:57.0856377Z Progress (1): 1.3 kB
2026-01-22T16:06:57.0860923Z Progress (1): 4.1 kB
2026-01-22T16:06:57.0863000Z                     
2026-01-22T16:06:57.0865528Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.1/messages-19.1.1.pom (4.1 kB at 254 kB/s)
2026-01-22T16:06:57.0890702Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.2/messages-19.1.2.pom
2026-01-22T16:06:57.1052022Z Progress (1): 1.3 kB
2026-01-22T16:06:57.1054891Z Progress (1): 4.1 kB
2026-01-22T16:06:57.1055202Z                     
2026-01-22T16:06:57.1055600Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.2/messages-19.1.2.pom (4.1 kB at 239 kB/s)
2026-01-22T16:06:57.1080198Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.3/messages-19.1.3.pom
2026-01-22T16:06:57.1253252Z Progress (1): 1.3 kB
2026-01-22T16:06:57.1258265Z Progress (1): 4.1 kB
2026-01-22T16:06:57.1258601Z                     
2026-01-22T16:06:57.1259039Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.3/messages-19.1.3.pom (4.1 kB at 226 kB/s)
2026-01-22T16:06:57.1279933Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.0/junit-bom-5.9.0.pom
2026-01-22T16:06:57.1460196Z Progress (1): 911 B
2026-01-22T16:06:57.1461307Z Progress (1): 4.1 kB
2026-01-22T16:06:57.1467044Z Progress (1): 5.6 kB
2026-01-22T16:06:57.1467724Z                     
2026-01-22T16:06:57.1468396Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.0/junit-bom-5.9.0.pom (5.6 kB at 296 kB/s)
2026-01-22T16:06:57.1483684Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/junit-xml-formatter/0.8.1/junit-xml-formatter-0.8.1.pom
2026-01-22T16:06:57.1655813Z Progress (1): 1.3 kB
2026-01-22T16:06:57.1660254Z Progress (1): 4.1 kB
2026-01-22T16:06:57.1663036Z                     
2026-01-22T16:06:57.1665280Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/junit-xml-formatter/0.8.1/junit-xml-formatter-0.8.1.pom (4.1 kB at 241 kB/s)
2026-01-22T16:06:57.1724061Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.0.2/query-13.0.2.pom
2026-01-22T16:06:57.1875840Z Progress (1): 1.3 kB
2026-01-22T16:06:57.1879763Z Progress (1): 3.2 kB
2026-01-22T16:06:57.1881869Z                     
2026-01-22T16:06:57.1884354Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.0.2/query-13.0.2.pom (3.2 kB at 167 kB/s)
2026-01-22T16:06:57.1914608Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.0.3/query-13.0.3.pom
2026-01-22T16:06:57.2081889Z Progress (1): 1.2 kB
2026-01-22T16:06:57.2087117Z Progress (1): 3.2 kB
2026-01-22T16:06:57.2088619Z                     
2026-01-22T16:06:57.2090084Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.0.3/query-13.0.3.pom (3.2 kB at 176 kB/s)
2026-01-22T16:06:57.2123632Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.1.0/query-13.1.0.pom
2026-01-22T16:06:57.2285308Z Progress (1): 1.3 kB
2026-01-22T16:06:57.2291224Z Progress (1): 3.2 kB
2026-01-22T16:06:57.2292987Z                     
2026-01-22T16:06:57.2294813Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.1.0/query-13.1.0.pom (3.2 kB at 186 kB/s)
2026-01-22T16:06:57.2319581Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.2.0/query-13.2.0.pom
2026-01-22T16:06:57.2482011Z Progress (1): 1.3 kB
2026-01-22T16:06:57.2486212Z Progress (1): 3.2 kB
2026-01-22T16:06:57.2488052Z                     
2026-01-22T16:06:57.2488466Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.2.0/query-13.2.0.pom (3.2 kB at 186 kB/s)
2026-01-22T16:06:57.2509311Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/ci-environment/10.0.1/ci-environment-10.0.1.pom
2026-01-22T16:06:57.2685414Z Progress (1): 1.2 kB
2026-01-22T16:06:57.2685762Z Progress (1): 4.1 kB
2026-01-22T16:06:57.2686089Z Progress (1): 6.1 kB
2026-01-22T16:06:57.2686378Z                     
2026-01-22T16:06:57.2686778Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/ci-environment/10.0.1/ci-environment-10.0.1.pom (6.1 kB at 356 kB/s)
2026-01-22T16:06:57.2708627Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.16.1/jackson-bom-2.16.1.pom
2026-01-22T16:06:57.2894289Z Progress (1): 924 B
2026-01-22T16:06:57.2896310Z Progress (1): 2.7 kB
2026-01-22T16:06:57.2897599Z Progress (1): 8.1 kB
2026-01-22T16:06:57.2898763Z Progress (1): 17 kB 
2026-01-22T16:06:57.2900909Z Progress (1): 18 kB
2026-01-22T16:06:57.2903298Z                    
2026-01-22T16:06:57.2905426Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.16.1/jackson-bom-2.16.1.pom (18 kB at 911 kB/s)
2026-01-22T16:06:57.2934049Z Downloading from central: https://repo.maven.apache.org/maven2/org/testng/testng/7.11.0/testng-7.11.0.pom
2026-01-22T16:06:57.3134535Z Progress (1): 999 B
2026-01-22T16:06:57.3134893Z Progress (1): 2.6 kB
2026-01-22T16:06:57.3135179Z                     
2026-01-22T16:06:57.3135618Z Downloaded from central: https://repo.maven.apache.org/maven2/org/testng/testng/7.11.0/testng-7.11.0.pom (2.6 kB at 137 kB/s)
2026-01-22T16:06:57.3141253Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.16/slf4j-api-2.0.16.pom
2026-01-22T16:06:57.3286374Z Progress (1): 1.1 kB
2026-01-22T16:06:57.3291113Z Progress (1): 2.8 kB
2026-01-22T16:06:57.3293533Z                     
2026-01-22T16:06:57.3296711Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.16/slf4j-api-2.0.16.pom (2.8 kB at 188 kB/s)
2026-01-22T16:06:57.3308223Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.16/slf4j-parent-2.0.16.pom
2026-01-22T16:06:57.3466725Z Progress (1): 952 B
2026-01-22T16:06:57.3468346Z Progress (1): 3.2 kB
2026-01-22T16:06:57.3469619Z Progress (1): 6.0 kB
2026-01-22T16:06:57.3471295Z Progress (1): 8.2 kB
2026-01-22T16:06:57.3472519Z Progress (1): 11 kB 
2026-01-22T16:06:57.3473512Z Progress (1): 13 kB
2026-01-22T16:06:57.3474708Z                    
2026-01-22T16:06:57.3475148Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.16/slf4j-parent-2.0.16.pom (13 kB at 786 kB/s)
2026-01-22T16:06:57.3485532Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.16/slf4j-bom-2.0.16.pom
2026-01-22T16:06:57.3649841Z Progress (1): 1.0 kB
2026-01-22T16:06:57.3653340Z Progress (1): 4.6 kB
2026-01-22T16:06:57.3653735Z Progress (1): 7.2 kB
2026-01-22T16:06:57.3656579Z Progress (1): 7.3 kB
2026-01-22T16:06:57.3657971Z                     
2026-01-22T16:06:57.3659241Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.16/slf4j-bom-2.0.16.pom (7.3 kB at 431 kB/s)
2026-01-22T16:06:57.3680129Z Downloading from central: https://repo.maven.apache.org/maven2/org/jcommander/jcommander/1.83/jcommander-1.83.pom
2026-01-22T16:06:57.4554965Z Progress (1): 1.0 kB
2026-01-22T16:06:57.4555326Z Progress (1): 1.5 kB
2026-01-22T16:06:57.4555637Z                     
2026-01-22T16:06:57.4556031Z Downloaded from central: https://repo.maven.apache.org/maven2/org/jcommander/jcommander/1.83/jcommander-1.83.pom (1.5 kB at 17 kB/s)
2026-01-22T16:06:57.4568870Z Downloading from central: https://repo.maven.apache.org/maven2/org/webjars/jquery/3.7.1/jquery-3.7.1.pom
2026-01-22T16:06:57.4774493Z Progress (1): 1.2 kB
2026-01-22T16:06:57.4775400Z Progress (1): 3.7 kB
2026-01-22T16:06:57.4776338Z Progress (1): 7.6 kB
2026-01-22T16:06:57.4776857Z                     
2026-01-22T16:06:57.4777787Z Downloaded from central: https://repo.maven.apache.org/maven2/org/webjars/jquery/3.7.1/jquery-3.7.1.pom (7.6 kB at 399 kB/s)
2026-01-22T16:06:57.4781709Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-testng/7.27.2/cucumber-testng-7.27.2.pom
2026-01-22T16:06:57.4968790Z Progress (1): 1.8 kB
2026-01-22T16:06:57.4975565Z Progress (1): 2.2 kB
2026-01-22T16:06:57.4977424Z                     
2026-01-22T16:06:57.4979146Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-testng/7.27.2/cucumber-testng-7.27.2.pom (2.2 kB at 111 kB/s)
2026-01-22T16:06:57.5014149Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-java/7.27.2/cucumber-java-7.27.2.pom
2026-01-22T16:06:57.5193696Z Progress (1): 1.6 kB
2026-01-22T16:06:57.5195042Z Progress (1): 5.2 kB
2026-01-22T16:06:57.5203443Z Progress (1): 8.4 kB
2026-01-22T16:06:57.5205036Z                     
2026-01-22T16:06:57.5206107Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-java/7.27.2/cucumber-java-7.27.2.pom (8.4 kB at 442 kB/s)
2026-01-22T16:06:57.5226356Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-picocontainer/7.27.2/cucumber-picocontainer-7.27.2.pom
2026-01-22T16:06:57.5403176Z Progress (1): 1.9 kB
2026-01-22T16:06:57.5407625Z Progress (1): 3.8 kB
2026-01-22T16:06:57.5408943Z                     
2026-01-22T16:06:57.5410416Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-picocontainer/7.27.2/cucumber-picocontainer-7.27.2.pom (3.8 kB at 213 kB/s)
2026-01-22T16:06:57.5426995Z Downloading from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer/2.15.2/picocontainer-2.15.2.pom
2026-01-22T16:06:57.5626670Z Progress (1): 1.5 kB
2026-01-22T16:06:57.5633608Z Progress (1): 4.3 kB
2026-01-22T16:06:57.5635292Z                     
2026-01-22T16:06:57.5636426Z Downloaded from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer/2.15.2/picocontainer-2.15.2.pom (4.3 kB at 216 kB/s)
2026-01-22T16:06:57.5644254Z Downloading from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer-parent/2.15.2/picocontainer-parent-2.15.2.pom
2026-01-22T16:06:57.5830175Z Progress (1): 1.5 kB
2026-01-22T16:06:57.5883461Z Progress (1): 4.8 kB
2026-01-22T16:06:57.5884170Z Progress (1): 7.6 kB
2026-01-22T16:06:57.5885195Z Progress (1): 12 kB 
2026-01-22T16:06:57.5885684Z Progress (1): 12 kB
2026-01-22T16:06:57.5886085Z                    
2026-01-22T16:06:57.5886604Z Downloaded from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer-parent/2.15.2/picocontainer-parent-2.15.2.pom (12 kB at 605 kB/s)
2026-01-22T16:06:57.5887295Z Downloading from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer-root/2.15.2/picocontainer-root-2.15.2.pom
2026-01-22T16:06:57.6027776Z Progress (1): 1.3 kB
2026-01-22T16:06:57.6032511Z Progress (1): 2.4 kB
2026-01-22T16:06:57.6034693Z                     
2026-01-22T16:06:57.6036076Z Downloaded from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer-root/2.15.2/picocontainer-root-2.15.2.pom (2.4 kB at 136 kB/s)
2026-01-22T16:06:57.6056513Z Downloading from central: https://repo.maven.apache.org/maven2/net/masterthought/cucumber-reporting/5.8.3/cucumber-reporting-5.8.3.pom
2026-01-22T16:06:57.6223427Z Progress (1): 1.2 kB
2026-01-22T16:06:57.6226216Z Progress (1): 3.0 kB
2026-01-22T16:06:57.6226557Z Progress (1): 5.4 kB
2026-01-22T16:06:57.6226884Z Progress (1): 9.6 kB
2026-01-22T16:06:57.6227197Z Progress (1): 14 kB 
2026-01-22T16:06:57.6229309Z Progress (1): 15 kB
2026-01-22T16:06:57.6230540Z                    
2026-01-22T16:06:57.6231701Z Downloaded from central: https://repo.maven.apache.org/maven2/net/masterthought/cucumber-reporting/5.8.3/cucumber-reporting-5.8.3.pom (15 kB at 813 kB/s)
2026-01-22T16:06:57.6251695Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.18.0/jackson-databind-2.18.0.pom
2026-01-22T16:06:57.6412192Z Progress (1): 973 B
2026-01-22T16:06:57.6413642Z Progress (1): 2.3 kB
2026-01-22T16:06:57.6418082Z Progress (1): 4.0 kB
2026-01-22T16:06:57.6419992Z Progress (1): 6.4 kB
2026-01-22T16:06:57.6421269Z Progress (1): 8.1 kB
2026-01-22T16:06:57.6422667Z Progress (1): 10 kB 
2026-01-22T16:06:57.6433335Z Progress (1): 12 kB
2026-01-22T16:06:57.6434015Z Progress (1): 18 kB
2026-01-22T16:06:57.6435077Z Progress (1): 19 kB
2026-01-22T16:06:57.6435515Z Progress (1): 21 kB
2026-01-22T16:06:57.6436011Z Progress (1): 22 kB
2026-01-22T16:06:57.6436428Z                    
2026-01-22T16:06:57.6437001Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.18.0/jackson-databind-2.18.0.pom (22 kB at 1.3 MB/s)
2026-01-22T16:06:57.6501337Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.18.0/jackson-base-2.18.0.pom
2026-01-22T16:06:57.6665484Z Progress (1): 911 B
2026-01-22T16:06:57.6666181Z Progress (1): 2.7 kB
2026-01-22T16:06:57.6668909Z Progress (1): 4.5 kB
2026-01-22T16:06:57.6669591Z Progress (1): 6.6 kB
2026-01-22T16:06:57.6670142Z Progress (1): 8.7 kB
2026-01-22T16:06:57.6670581Z Progress (1): 11 kB 
2026-01-22T16:06:57.6675397Z Progress (1): 12 kB
2026-01-22T16:06:57.6676298Z                    
2026-01-22T16:06:57.6677920Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.18.0/jackson-base-2.18.0.pom (12 kB at 683 kB/s)
2026-01-22T16:06:57.6716975Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.18.0/jackson-annotations-2.18.0.pom
2026-01-22T16:06:57.6862044Z Progress (1): 946 B
2026-01-22T16:06:57.6862505Z Progress (1): 2.4 kB
2026-01-22T16:06:57.6885327Z Progress (1): 3.9 kB
2026-01-22T16:06:57.6886566Z Progress (1): 6.3 kB
2026-01-22T16:06:57.6887666Z Progress (1): 7.1 kB
2026-01-22T16:06:57.6888916Z                     
2026-01-22T16:06:57.6890074Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.18.0/jackson-annotations-2.18.0.pom (7.1 kB at 394 kB/s)
2026-01-22T16:06:57.6910136Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.18.0/jackson-core-2.18.0.pom
2026-01-22T16:06:57.7076661Z Progress (1): 980 B
2026-01-22T16:06:57.7083332Z Progress (1): 2.9 kB
2026-01-22T16:06:57.7084078Z Progress (1): 7.1 kB
2026-01-22T16:06:57.7084833Z Progress (1): 9.6 kB
2026-01-22T16:06:57.7110523Z Progress (1): 10 kB 
2026-01-22T16:06:57.7112310Z                    
2026-01-22T16:06:57.7113124Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.18.0/jackson-core-2.18.0.pom (10 kB at 477 kB/s)
2026-01-22T16:06:57.7194085Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.18.0/jackson-datatype-jsr310-2.18.0.pom
2026-01-22T16:06:57.7350879Z Progress (1): 983 B
2026-01-22T16:06:57.7353185Z Progress (1): 2.4 kB
2026-01-22T16:06:57.7355237Z Progress (1): 4.6 kB
2026-01-22T16:06:57.7374511Z Progress (1): 4.9 kB
2026-01-22T16:06:57.7376473Z                     
2026-01-22T16:06:57.7378568Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.18.0/jackson-datatype-jsr310-2.18.0.pom (4.9 kB at 258 kB/s)
2026-01-22T16:06:57.7381525Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/module/jackson-modules-java8/2.18.0/jackson-modules-java8-2.18.0.pom
2026-01-22T16:06:57.7567906Z Progress (1): 1.4 kB
2026-01-22T16:06:57.7568260Z Progress (1): 3.1 kB
2026-01-22T16:06:57.7593463Z Progress (1): 3.3 kB
2026-01-22T16:06:57.7594192Z                     
2026-01-22T16:06:57.7595544Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/module/jackson-modules-java8/2.18.0/jackson-modules-java8-2.18.0.pom (3.3 kB at 165 kB/s)
2026-01-22T16:06:57.7630550Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.pom
2026-01-22T16:06:57.8157202Z Progress (1): 1.3 kB
2026-01-22T16:06:57.8157556Z Progress (1): 4.5 kB
2026-01-22T16:06:57.8157861Z Progress (1): 8.2 kB
2026-01-22T16:06:57.8163260Z Progress (1): 10 kB 
2026-01-22T16:06:57.8163599Z                    
2026-01-22T16:06:57.8164242Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.pom (10 kB at 187 kB/s)
2026-01-22T16:06:57.8184840Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-parent/2.3/velocity-engine-parent-2.3.pom
2026-01-22T16:06:57.8353472Z Progress (1): 795 B
2026-01-22T16:06:57.8354978Z Progress (1): 2.2 kB
2026-01-22T16:06:57.8357300Z Progress (1): 5.9 kB
2026-01-22T16:06:57.8358517Z Progress (1): 9.3 kB
2026-01-22T16:06:57.8359862Z Progress (1): 12 kB 
2026-01-22T16:06:57.8360875Z Progress (1): 14 kB
2026-01-22T16:06:57.8362134Z                    
2026-01-22T16:06:57.8363465Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-parent/2.3/velocity-engine-parent-2.3.pom (14 kB at 813 kB/s)
2026-01-22T16:06:57.8381779Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-master/4/velocity-master-4.pom
2026-01-22T16:06:57.8594708Z Progress (1): 806 B
2026-01-22T16:06:57.8595058Z Progress (1): 2.4 kB
2026-01-22T16:06:57.8595366Z Progress (1): 5.9 kB
2026-01-22T16:06:57.8595661Z Progress (1): 7.8 kB
2026-01-22T16:06:57.8595947Z                     
2026-01-22T16:06:57.8596355Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-master/4/velocity-master-4.pom (7.8 kB at 409 kB/s)
2026-01-22T16:06:57.8640828Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/23/apache-23.pom
2026-01-22T16:06:57.8805757Z Progress (1): 749 B
2026-01-22T16:06:57.8808837Z Progress (1): 2.1 kB
2026-01-22T16:06:57.8809898Z Progress (1): 3.9 kB
2026-01-22T16:06:57.8810461Z Progress (1): 7.9 kB
2026-01-22T16:06:57.8811351Z Progress (1): 13 kB 
2026-01-22T16:06:57.8811902Z Progress (1): 16 kB
2026-01-22T16:06:57.8812944Z Progress (1): 18 kB
2026-01-22T16:06:57.8814288Z                    
2026-01-22T16:06:57.8814658Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/23/apache-23.pom (18 kB at 970 kB/s)
2026-01-22T16:06:57.8855636Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.11/commons-lang3-3.11.pom
2026-01-22T16:06:57.9055362Z Progress (1): 728 B
2026-01-22T16:06:57.9056460Z Progress (1): 2.0 kB
2026-01-22T16:06:57.9057231Z Progress (1): 5.2 kB
2026-01-22T16:06:57.9058110Z Progress (1): 8.8 kB
2026-01-22T16:06:57.9083918Z Progress (1): 12 kB 
2026-01-22T16:06:57.9085058Z Progress (1): 15 kB
2026-01-22T16:06:57.9085742Z Progress (1): 17 kB
2026-01-22T16:06:57.9086802Z Progress (1): 18 kB
2026-01-22T16:06:57.9087473Z Progress (1): 21 kB
2026-01-22T16:06:57.9088550Z Progress (1): 24 kB
2026-01-22T16:06:57.9089346Z Progress (1): 27 kB
2026-01-22T16:06:57.9090400Z Progress (1): 30 kB
2026-01-22T16:06:57.9091159Z Progress (1): 30 kB
2026-01-22T16:06:57.9092190Z                    
2026-01-22T16:06:57.9094348Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.11/commons-lang3-3.11.pom (30 kB at 1.5 MB/s)
2026-01-22T16:06:57.9095705Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/51/commons-parent-51.pom
2026-01-22T16:06:57.9350064Z Progress (1): 702 B
2026-01-22T16:06:57.9352525Z Progress (1): 1.8 kB
2026-01-22T16:06:57.9359074Z Progress (1): 3.1 kB
2026-01-22T16:06:57.9361179Z Progress (1): 4.6 kB
2026-01-22T16:06:57.9361882Z Progress (1): 6.7 kB
2026-01-22T16:06:57.9362388Z Progress (1): 8.1 kB
2026-01-22T16:06:57.9363083Z Progress (1): 10 kB 
2026-01-22T16:06:57.9363528Z Progress (1): 12 kB
2026-01-22T16:06:57.9363969Z Progress (1): 14 kB
2026-01-22T16:06:57.9364400Z Progress (1): 17 kB
2026-01-22T16:06:57.9364817Z Progress (1): 20 kB
2026-01-22T16:06:57.9365253Z Progress (1): 22 kB
2026-01-22T16:06:57.9365693Z Progress (1): 25 kB
2026-01-22T16:06:57.9366144Z Progress (1): 29 kB
2026-01-22T16:06:57.9366590Z Progress (1): 32 kB
2026-01-22T16:06:57.9367808Z Progress (1): 32 kB
2026-01-22T16:06:57.9368265Z Progress (1): 36 kB
2026-01-22T16:06:57.9368557Z Progress (1): 40 kB
2026-01-22T16:06:57.9368840Z Progress (1): 42 kB
2026-01-22T16:06:57.9369128Z Progress (1): 44 kB
2026-01-22T16:06:57.9369409Z Progress (1): 47 kB
2026-01-22T16:06:57.9369704Z Progress (1): 51 kB
2026-01-22T16:06:57.9369983Z Progress (1): 54 kB
2026-01-22T16:06:57.9370276Z Progress (1): 56 kB
2026-01-22T16:06:57.9370563Z Progress (1): 61 kB
2026-01-22T16:06:57.9370869Z Progress (1): 65 kB
2026-01-22T16:06:57.9371154Z Progress (1): 72 kB
2026-01-22T16:06:57.9371443Z Progress (1): 75 kB
2026-01-22T16:06:57.9374280Z Progress (1): 78 kB
2026-01-22T16:06:57.9374585Z                    
2026-01-22T16:06:57.9374992Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/51/commons-parent-51.pom (78 kB at 2.8 MB/s)
2026-01-22T16:06:57.9422526Z Downloading from central: https://repo.maven.apache.org/maven2/joda-time/joda-time/2.13.0/joda-time-2.13.0.pom
2026-01-22T16:06:57.9631421Z Progress (1): 889 B
2026-01-22T16:06:57.9632215Z Progress (1): 3.7 kB
2026-01-22T16:06:57.9633385Z Progress (1): 7.3 kB
2026-01-22T16:06:57.9635500Z Progress (1): 11 kB 
2026-01-22T16:06:57.9635871Z Progress (1): 13 kB
2026-01-22T16:06:57.9636181Z Progress (1): 16 kB
2026-01-22T16:06:57.9636480Z Progress (1): 19 kB
2026-01-22T16:06:57.9636783Z Progress (1): 26 kB
2026-01-22T16:06:57.9637069Z Progress (1): 29 kB
2026-01-22T16:06:57.9637388Z Progress (1): 31 kB
2026-01-22T16:06:57.9637677Z Progress (1): 34 kB
2026-01-22T16:06:57.9637973Z Progress (1): 38 kB
2026-01-22T16:06:57.9638265Z Progress (1): 40 kB
2026-01-22T16:06:57.9638543Z                    
2026-01-22T16:06:57.9638926Z Downloaded from central: https://repo.maven.apache.org/maven2/joda-time/joda-time/2.13.0/joda-time-2.13.0.pom (40 kB at 2.0 MB/s)
2026-01-22T16:06:57.9727378Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-configuration2/2.11.0/commons-configuration2-2.11.0.pom
2026-01-22T16:06:57.9920625Z Progress (1): 736 B
2026-01-22T16:06:57.9923381Z Progress (1): 2.2 kB
2026-01-22T16:06:57.9928758Z Progress (1): 3.8 kB
2026-01-22T16:06:57.9930892Z Progress (1): 7.1 kB
2026-01-22T16:06:57.9931454Z Progress (1): 12 kB 
2026-01-22T16:06:57.9931931Z Progress (1): 14 kB
2026-01-22T16:06:57.9933621Z Progress (1): 16 kB
2026-01-22T16:06:57.9933904Z Progress (1): 19 kB
2026-01-22T16:06:57.9934201Z Progress (1): 22 kB
2026-01-22T16:06:57.9934504Z Progress (1): 25 kB
2026-01-22T16:06:57.9934793Z Progress (1): 28 kB
2026-01-22T16:06:57.9935068Z Progress (1): 28 kB
2026-01-22T16:06:57.9935338Z                    
2026-01-22T16:06:57.9935740Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-configuration2/2.11.0/commons-configuration2-2.11.0.pom (28 kB at 1.1 MB/s)
2026-01-22T16:06:57.9959436Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/70/commons-parent-70.pom
2026-01-22T16:06:58.0161132Z Progress (1): 704 B
2026-01-22T16:06:58.0161486Z Progress (1): 1.9 kB
2026-01-22T16:06:58.0161814Z Progress (1): 3.2 kB
2026-01-22T16:06:58.0162116Z Progress (1): 4.6 kB
2026-01-22T16:06:58.0162406Z Progress (1): 6.7 kB
2026-01-22T16:06:58.0162706Z Progress (1): 8.4 kB
2026-01-22T16:06:58.0173473Z Progress (1): 11 kB 
2026-01-22T16:06:58.0173817Z Progress (1): 13 kB
2026-01-22T16:06:58.0174126Z Progress (1): 15 kB
2026-01-22T16:06:58.0174438Z Progress (1): 17 kB
2026-01-22T16:06:58.0174930Z Progress (1): 20 kB
2026-01-22T16:06:58.0175239Z Progress (1): 22 kB
2026-01-22T16:06:58.0175532Z Progress (1): 25 kB
2026-01-22T16:06:58.0175826Z Progress (1): 28 kB
2026-01-22T16:06:58.0176125Z Progress (1): 31 kB
2026-01-22T16:06:58.0176419Z Progress (1): 32 kB
2026-01-22T16:06:58.0176703Z Progress (1): 36 kB
2026-01-22T16:06:58.0176998Z Progress (1): 40 kB
2026-01-22T16:06:58.0177292Z Progress (1): 43 kB
2026-01-22T16:06:58.0177590Z Progress (1): 45 kB
2026-01-22T16:06:58.0177883Z Progress (1): 49 kB
2026-01-22T16:06:58.0178189Z Progress (1): 51 kB
2026-01-22T16:06:58.0178486Z Progress (1): 55 kB
2026-01-22T16:06:58.0178933Z Progress (1): 57 kB
2026-01-22T16:06:58.0179223Z Progress (1): 60 kB
2026-01-22T16:06:58.0179513Z Progress (1): 63 kB
2026-01-22T16:06:58.0179801Z Progress (1): 67 kB
2026-01-22T16:06:58.0180099Z Progress (1): 70 kB
2026-01-22T16:06:58.0180386Z Progress (1): 73 kB
2026-01-22T16:06:58.0180687Z Progress (1): 75 kB
2026-01-22T16:06:58.0180994Z Progress (1): 77 kB
2026-01-22T16:06:58.0181285Z                    
2026-01-22T16:06:58.0181697Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/70/commons-parent-70.pom (77 kB at 3.9 MB/s)
2026-01-22T16:06:58.0229471Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/32/apache-32.pom
2026-01-22T16:06:58.0388502Z Progress (1): 733 B
2026-01-22T16:06:58.0400593Z Progress (1): 2.0 kB
2026-01-22T16:06:58.0403581Z Progress (1): 4.0 kB
2026-01-22T16:06:58.0409845Z Progress (1): 5.9 kB
2026-01-22T16:06:58.0411737Z Progress (1): 10 kB 
2026-01-22T16:06:58.0413457Z Progress (1): 16 kB
2026-01-22T16:06:58.0414388Z Progress (1): 19 kB
2026-01-22T16:06:58.0415008Z Progress (1): 22 kB
2026-01-22T16:06:58.0415902Z Progress (1): 24 kB
2026-01-22T16:06:58.0416307Z                    
2026-01-22T16:06:58.0416777Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/32/apache-32.pom (24 kB at 1.3 MB/s)
2026-01-22T16:06:58.0460313Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0-M1/junit-bom-5.11.0-M1.pom
2026-01-22T16:06:58.0625542Z Progress (1): 903 B
2026-01-22T16:06:58.0653603Z Progress (1): 4.1 kB
2026-01-22T16:06:58.0654302Z Progress (1): 5.7 kB
2026-01-22T16:06:58.0655241Z                     
2026-01-22T16:06:58.0655943Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0-M1/junit-bom-5.11.0-M1.pom (5.7 kB at 300 kB/s)
2026-01-22T16:06:58.0691753Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.pom
2026-01-22T16:06:58.0860789Z Progress (1): 736 B
2026-01-22T16:06:58.0861483Z Progress (1): 2.0 kB
2026-01-22T16:06:58.0861958Z Progress (1): 4.7 kB
2026-01-22T16:06:58.0866006Z Progress (1): 8.3 kB
2026-01-22T16:06:58.0866483Z Progress (1): 12 kB 
2026-01-22T16:06:58.0869596Z Progress (1): 15 kB
2026-01-22T16:06:58.0871364Z Progress (1): 16 kB
2026-01-22T16:06:58.0872609Z Progress (1): 18 kB
2026-01-22T16:06:58.0874155Z Progress (1): 21 kB
2026-01-22T16:06:58.0875113Z Progress (1): 24 kB
2026-01-22T16:06:58.0876033Z Progress (1): 27 kB
2026-01-22T16:06:58.0876942Z Progress (1): 30 kB
2026-01-22T16:06:58.0878079Z Progress (1): 31 kB
2026-01-22T16:06:58.0878933Z                    
2026-01-22T16:06:58.0880115Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.pom (31 kB at 1.6 MB/s)
2026-01-22T16:06:58.0906316Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/64/commons-parent-64.pom
2026-01-22T16:06:58.1203749Z Progress (1): 702 B
2026-01-22T16:06:58.1204542Z Progress (1): 1.9 kB
2026-01-22T16:06:58.1205621Z Progress (1): 3.1 kB
2026-01-22T16:06:58.1207442Z Progress (1): 4.6 kB
2026-01-22T16:06:58.1208677Z Progress (1): 6.4 kB
2026-01-22T16:06:58.1209867Z Progress (1): 8.4 kB
2026-01-22T16:06:58.1210465Z Progress (1): 10 kB 
2026-01-22T16:06:58.1210991Z Progress (1): 13 kB
2026-01-22T16:06:58.1211887Z Progress (1): 14 kB
2026-01-22T16:06:58.1212409Z Progress (1): 18 kB
2026-01-22T16:06:58.1213095Z Progress (1): 19 kB
2026-01-22T16:06:58.1213606Z Progress (1): 23 kB
2026-01-22T16:06:58.1214023Z Progress (1): 25 kB
2026-01-22T16:06:58.1214479Z Progress (1): 28 kB
2026-01-22T16:06:58.1214923Z Progress (1): 32 kB
2026-01-22T16:06:58.1215338Z Progress (1): 32 kB
2026-01-22T16:06:58.1215790Z Progress (1): 35 kB
2026-01-22T16:06:58.1216264Z Progress (1): 41 kB
2026-01-22T16:06:58.1216711Z Progress (1): 43 kB
2026-01-22T16:06:58.1217108Z Progress (1): 46 kB
2026-01-22T16:06:58.1217890Z Progress (1): 49 kB
2026-01-22T16:06:58.1218370Z Progress (1): 51 kB
2026-01-22T16:06:58.1219476Z Progress (1): 54 kB
2026-01-22T16:06:58.1219790Z Progress (1): 58 kB
2026-01-22T16:06:58.1220092Z Progress (1): 60 kB
2026-01-22T16:06:58.1220385Z Progress (1): 64 kB
2026-01-22T16:06:58.1220679Z Progress (1): 67 kB
2026-01-22T16:06:58.1220987Z Progress (1): 71 kB
2026-01-22T16:06:58.1221277Z Progress (1): 74 kB
2026-01-22T16:06:58.1221593Z Progress (1): 76 kB
2026-01-22T16:06:58.1221882Z Progress (1): 78 kB
2026-01-22T16:06:58.1222166Z                    
2026-01-22T16:06:58.1222563Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/64/commons-parent-64.pom (78 kB at 2.5 MB/s)
2026-01-22T16:06:58.1265655Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.pom
2026-01-22T16:06:58.1470945Z Progress (1): 742 B
2026-01-22T16:06:58.1471300Z Progress (1): 2.1 kB
2026-01-22T16:06:58.1524886Z Progress (1): 3.7 kB
2026-01-22T16:06:58.1525599Z Progress (1): 6.7 kB
2026-01-22T16:06:58.1526244Z Progress (1): 9.0 kB
2026-01-22T16:06:58.1526910Z Progress (1): 13 kB 
2026-01-22T16:06:58.1527489Z Progress (1): 16 kB
2026-01-22T16:06:58.1528019Z Progress (1): 18 kB
2026-01-22T16:06:58.1528519Z Progress (1): 20 kB
2026-01-22T16:06:58.1529057Z                    
2026-01-22T16:06:58.1529841Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.pom (20 kB at 902 kB/s)
2026-01-22T16:06:58.1530588Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/69/commons-parent-69.pom
2026-01-22T16:06:58.1842622Z Progress (1): 703 B
2026-01-22T16:06:58.1844057Z Progress (1): 1.9 kB
2026-01-22T16:06:58.1844393Z Progress (1): 3.1 kB
2026-01-22T16:06:58.1844722Z Progress (1): 4.6 kB
2026-01-22T16:06:58.1845048Z Progress (1): 6.4 kB
2026-01-22T16:06:58.1845389Z Progress (1): 8.4 kB
2026-01-22T16:06:58.1845904Z Progress (1): 9.9 kB
2026-01-22T16:06:58.1846587Z Progress (1): 12 kB 
2026-01-22T16:06:58.1848951Z Progress (1): 14 kB
2026-01-22T16:06:58.1849486Z Progress (1): 17 kB
2026-01-22T16:06:58.1850960Z Progress (1): 19 kB
2026-01-22T16:06:58.1851468Z Progress (1): 22 kB
2026-01-22T16:06:58.1854071Z Progress (1): 24 kB
2026-01-22T16:06:58.1854725Z Progress (1): 28 kB
2026-01-22T16:06:58.1855458Z Progress (1): 31 kB
2026-01-22T16:06:58.1860819Z Progress (1): 31 kB
2026-01-22T16:06:58.1861332Z Progress (1): 35 kB
2026-01-22T16:06:58.1861781Z Progress (1): 40 kB
2026-01-22T16:06:58.1862276Z Progress (1): 43 kB
2026-01-22T16:06:58.1864280Z Progress (1): 45 kB
2026-01-22T16:06:58.1864797Z Progress (1): 48 kB
2026-01-22T16:06:58.1865236Z Progress (1): 51 kB
2026-01-22T16:06:58.1865686Z Progress (1): 55 kB
2026-01-22T16:06:58.1866192Z Progress (1): 57 kB
2026-01-22T16:06:58.1867570Z Progress (1): 59 kB
2026-01-22T16:06:58.1868044Z Progress (1): 63 kB
2026-01-22T16:06:58.1868443Z Progress (1): 67 kB
2026-01-22T16:06:58.1868905Z Progress (1): 70 kB
2026-01-22T16:06:58.1869327Z Progress (1): 73 kB
2026-01-22T16:06:58.1869767Z Progress (1): 75 kB
2026-01-22T16:06:58.1870230Z Progress (1): 77 kB
2026-01-22T16:06:58.1870677Z                    
2026-01-22T16:06:58.1871239Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/69/commons-parent-69.pom (77 kB at 2.1 MB/s)
2026-01-22T16:06:58.1899831Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/31/apache-31.pom
2026-01-22T16:06:58.2082054Z Progress (1): 740 B
2026-01-22T16:06:58.2083123Z Progress (1): 2.1 kB
2026-01-22T16:06:58.2083645Z Progress (1): 3.9 kB
2026-01-22T16:06:58.2084903Z Progress (1): 6.2 kB
2026-01-22T16:06:58.2085289Z Progress (1): 11 kB 
2026-01-22T16:06:58.2085764Z Progress (1): 16 kB
2026-01-22T16:06:58.2087083Z Progress (1): 20 kB
2026-01-22T16:06:58.2087485Z Progress (1): 22 kB
2026-01-22T16:06:58.2110414Z Progress (1): 24 kB
2026-01-22T16:06:58.2112479Z                    
2026-01-22T16:06:58.2113448Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/31/apache-31.pom (24 kB at 1.1 MB/s)
2026-01-22T16:06:58.2187782Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.15.0/commons-lang3-3.15.0.pom
2026-01-22T16:06:58.2354018Z Progress (1): 739 B
2026-01-22T16:06:58.2354372Z Progress (1): 1.8 kB
2026-01-22T16:06:58.2354707Z Progress (1): 4.1 kB
2026-01-22T16:06:58.2355003Z Progress (1): 5.7 kB
2026-01-22T16:06:58.2355307Z Progress (1): 7.5 kB
2026-01-22T16:06:58.2355604Z Progress (1): 10.0 kB
2026-01-22T16:06:58.2355906Z Progress (1): 13 kB  
2026-01-22T16:06:58.2356201Z Progress (1): 17 kB
2026-01-22T16:06:58.2356503Z Progress (1): 19 kB
2026-01-22T16:06:58.2356791Z Progress (1): 22 kB
2026-01-22T16:06:58.2357086Z Progress (1): 26 kB
2026-01-22T16:06:58.2357373Z Progress (1): 29 kB
2026-01-22T16:06:58.2357667Z Progress (1): 31 kB
2026-01-22T16:06:58.2357939Z                    
2026-01-22T16:06:58.2358348Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.15.0/commons-lang3-3.15.0.pom (31 kB at 1.7 MB/s)
2026-01-22T16:06:58.2390338Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/71/commons-parent-71.pom
2026-01-22T16:06:58.2736274Z Progress (1): 704 B
2026-01-22T16:06:58.2736948Z Progress (1): 1.9 kB
2026-01-22T16:06:58.2737494Z Progress (1): 3.2 kB
2026-01-22T16:06:58.2737995Z Progress (1): 4.6 kB
2026-01-22T16:06:58.2738508Z Progress (1): 6.8 kB
2026-01-22T16:06:58.2739018Z Progress (1): 8.4 kB
2026-01-22T16:06:58.2739327Z Progress (1): 11 kB 
2026-01-22T16:06:58.2739628Z Progress (1): 13 kB
2026-01-22T16:06:58.2739917Z Progress (1): 15 kB
2026-01-22T16:06:58.2740213Z Progress (1): 17 kB
2026-01-22T16:06:58.2740499Z Progress (1): 20 kB
2026-01-22T16:06:58.2740792Z Progress (1): 22 kB
2026-01-22T16:06:58.2741080Z Progress (1): 25 kB
2026-01-22T16:06:58.2741377Z Progress (1): 28 kB
2026-01-22T16:06:58.2741669Z Progress (1): 32 kB
2026-01-22T16:06:58.2741977Z Progress (1): 32 kB
2026-01-22T16:06:58.2742261Z Progress (1): 36 kB
2026-01-22T16:06:58.2742557Z Progress (1): 40 kB
2026-01-22T16:06:58.2743019Z Progress (1): 43 kB
2026-01-22T16:06:58.2743328Z Progress (1): 45 kB
2026-01-22T16:06:58.2743616Z Progress (1): 49 kB
2026-01-22T16:06:58.2743913Z Progress (1): 51 kB
2026-01-22T16:06:58.2744201Z Progress (1): 55 kB
2026-01-22T16:06:58.2744506Z Progress (1): 57 kB
2026-01-22T16:06:58.2744793Z Progress (1): 60 kB
2026-01-22T16:06:58.2745115Z Progress (1): 63 kB
2026-01-22T16:06:58.2745396Z Progress (1): 67 kB
2026-01-22T16:06:58.2745685Z Progress (1): 70 kB
2026-01-22T16:06:58.2745966Z Progress (1): 73 kB
2026-01-22T16:06:58.2746253Z Progress (1): 75 kB
2026-01-22T16:06:58.2784350Z Progress (1): 78 kB
2026-01-22T16:06:58.2784967Z                    
2026-01-22T16:06:58.2785387Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/71/commons-parent-71.pom (78 kB at 1.9 MB/s)
2026-01-22T16:06:58.2925633Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0-M2/junit-bom-5.11.0-M2.pom
2026-01-22T16:06:58.3175961Z Progress (1): 903 B
2026-01-22T16:06:58.3176749Z Progress (1): 4.1 kB
2026-01-22T16:06:58.3178317Z Progress (1): 5.7 kB
2026-01-22T16:06:58.3178765Z                     
2026-01-22T16:06:58.3179301Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0-M2/junit-bom-5.11.0-M2.pom (5.7 kB at 248 kB/s)
2026-01-22T16:06:58.3181803Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.16.1/commons-io-2.16.1.pom
2026-01-22T16:06:58.3337776Z Progress (1): 761 B
2026-01-22T16:06:58.3348126Z Progress (1): 2.0 kB
2026-01-22T16:06:58.3348483Z Progress (1): 4.9 kB
2026-01-22T16:06:58.3348809Z Progress (1): 6.7 kB
2026-01-22T16:06:58.3349118Z Progress (1): 8.8 kB
2026-01-22T16:06:58.3349427Z Progress (1): 12 kB 
2026-01-22T16:06:58.3351246Z Progress (1): 15 kB
2026-01-22T16:06:58.3351560Z Progress (1): 18 kB
2026-01-22T16:06:58.3352041Z Progress (1): 20 kB
2026-01-22T16:06:58.3352309Z                    
2026-01-22T16:06:58.3352689Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.16.1/commons-io-2.16.1.pom (20 kB at 1.1 MB/s)
2026-01-22T16:06:58.3384240Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.11.0/commons-text-1.11.0.pom
2026-01-22T16:06:58.3575896Z Progress (1): 747 B
2026-01-22T16:06:58.3577586Z Progress (1): 2.3 kB
2026-01-22T16:06:58.3577928Z Progress (1): 3.9 kB
2026-01-22T16:06:58.3578263Z Progress (1): 6.8 kB
2026-01-22T16:06:58.3578586Z Progress (1): 10 kB 
2026-01-22T16:06:58.3578905Z Progress (1): 14 kB
2026-01-22T16:06:58.3579207Z Progress (1): 16 kB
2026-01-22T16:06:58.3579512Z Progress (1): 19 kB
2026-01-22T16:06:58.3604883Z                    
2026-01-22T16:06:58.3606545Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.11.0/commons-text-1.11.0.pom (19 kB at 975 kB/s)
2026-01-22T16:06:58.3664124Z Downloading from central: https://repo.maven.apache.org/maven2/org/jsoup/jsoup/1.18.1/jsoup-1.18.1.pom
2026-01-22T16:06:58.3809011Z Progress (1): 791 B
2026-01-22T16:06:58.3809424Z Progress (1): 2.2 kB
2026-01-22T16:06:58.3812970Z Progress (1): 4.3 kB
2026-01-22T16:06:58.3813281Z Progress (1): 7.1 kB
2026-01-22T16:06:58.3813581Z Progress (1): 9.5 kB
2026-01-22T16:06:58.3813896Z Progress (1): 12 kB 
2026-01-22T16:06:58.3814184Z Progress (1): 15 kB
2026-01-22T16:06:58.3819117Z Progress (1): 16 kB
2026-01-22T16:06:58.3819436Z                    
2026-01-22T16:06:58.3819839Z Downloaded from central: https://repo.maven.apache.org/maven2/org/jsoup/jsoup/1.18.1/jsoup-1.18.1.pom (16 kB at 857 kB/s)
2026-01-22T16:06:58.3875739Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/owasp-java-html-sanitizer/20240325.1/owasp-java-html-sanitizer-20240325.1.pom
2026-01-22T16:06:58.4084571Z Progress (1): 984 B
2026-01-22T16:06:58.4085800Z Progress (1): 4.1 kB
2026-01-22T16:06:58.4086845Z Progress (1): 5.0 kB
2026-01-22T16:06:58.4087144Z                     
2026-01-22T16:06:58.4087612Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/owasp-java-html-sanitizer/20240325.1/owasp-java-html-sanitizer-20240325.1.pom (5.0 kB at 238 kB/s)
2026-01-22T16:06:58.4134472Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/parent/20240325.1/parent-20240325.1.pom
2026-01-22T16:06:58.4296599Z Progress (1): 969 B
2026-01-22T16:06:58.4297756Z Progress (1): 2.8 kB
2026-01-22T16:06:58.4304077Z Progress (1): 4.6 kB
2026-01-22T16:06:58.4304808Z Progress (1): 6.7 kB
2026-01-22T16:06:58.4305608Z Progress (1): 10 kB 
2026-01-22T16:06:58.4307061Z Progress (1): 11 kB
2026-01-22T16:06:58.4307664Z                    
2026-01-22T16:06:58.4308451Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/parent/20240325.1/parent-20240325.1.pom (11 kB at 610 kB/s)
2026-01-22T16:06:58.4333890Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java8-shim/20240325.1/java8-shim-20240325.1.pom
2026-01-22T16:06:58.4543875Z Progress (1): 1.1 kB
2026-01-22T16:06:58.4545000Z Progress (1): 1.2 kB
2026-01-22T16:06:58.4546205Z                     
2026-01-22T16:06:58.4547115Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java8-shim/20240325.1/java8-shim-20240325.1.pom (1.2 kB at 71 kB/s)
2026-01-22T16:06:58.4590104Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java10-shim/20240325.1/java10-shim-20240325.1.pom
2026-01-22T16:06:58.4689013Z Progress (1): 1.2 kB
2026-01-22T16:06:58.4720665Z Progress (1): 1.5 kB
2026-01-22T16:06:58.4721006Z                     
2026-01-22T16:06:58.4721471Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java10-shim/20240325.1/java10-shim-20240325.1.pom (1.5 kB at 86 kB/s)
2026-01-22T16:06:58.4722250Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/jcl-over-slf4j/2.0.16/jcl-over-slf4j-2.0.16.pom
2026-01-22T16:06:58.4879416Z Progress (1): 1.3 kB
2026-01-22T16:06:58.4883283Z Progress (1): 1.7 kB
2026-01-22T16:06:58.4883615Z                     
2026-01-22T16:06:58.4884084Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/jcl-over-slf4j/2.0.16/jcl-over-slf4j-2.0.16.pom (1.7 kB at 102 kB/s)
2026-01-22T16:06:58.4905188Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.17.1/jackson-databind-2.17.1.pom
2026-01-22T16:06:58.5062144Z Progress (1): 968 B
2026-01-22T16:06:58.5063060Z Progress (1): 2.4 kB
2026-01-22T16:06:58.5072295Z Progress (1): 4.0 kB
2026-01-22T16:06:58.5073087Z Progress (1): 6.2 kB
2026-01-22T16:06:58.5073652Z Progress (1): 8.0 kB
2026-01-22T16:06:58.5074284Z Progress (1): 10 kB 
2026-01-22T16:06:58.5074898Z Progress (1): 12 kB
2026-01-22T16:06:58.5075508Z Progress (1): 17 kB
2026-01-22T16:06:58.5076103Z Progress (1): 19 kB
2026-01-22T16:06:58.5076706Z Progress (1): 21 kB
2026-01-22T16:06:58.5077310Z Progress (1): 21 kB
2026-01-22T16:06:58.5077902Z                    
2026-01-22T16:06:58.5078635Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.17.1/jackson-databind-2.17.1.pom (21 kB at 1.2 MB/s)
2026-01-22T16:06:58.5096843Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.17.1/jackson-base-2.17.1.pom
2026-01-22T16:06:58.5237595Z Progress (1): 900 B
2026-01-22T16:06:58.5254854Z Progress (1): 2.4 kB
2026-01-22T16:06:58.5263658Z Progress (1): 4.2 kB
2026-01-22T16:06:58.5264662Z Progress (1): 6.2 kB
2026-01-22T16:06:58.5265231Z Progress (1): 8.5 kB
2026-01-22T16:06:58.5266508Z Progress (1): 11 kB 
2026-01-22T16:06:58.5266811Z Progress (1): 12 kB
2026-01-22T16:06:58.5267094Z                    
2026-01-22T16:06:58.5267516Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.17.1/jackson-base-2.17.1.pom (12 kB at 785 kB/s)
2026-01-22T16:06:58.5284909Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.17.1/jackson-annotations-2.17.1.pom
2026-01-22T16:06:58.5442209Z Progress (1): 946 B
2026-01-22T16:06:58.5444954Z Progress (1): 2.4 kB
2026-01-22T16:06:58.5447043Z Progress (1): 3.9 kB
2026-01-22T16:06:58.5449042Z Progress (1): 6.3 kB
2026-01-22T16:06:58.5451060Z Progress (1): 7.1 kB
2026-01-22T16:06:58.5453312Z                     
2026-01-22T16:06:58.5455699Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.17.1/jackson-annotations-2.17.1.pom (7.1 kB at 441 kB/s)
2026-01-22T16:06:58.5473369Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.17.1/jackson-core-2.17.1.pom
2026-01-22T16:06:58.5634896Z Progress (1): 977 B
2026-01-22T16:06:58.5635221Z Progress (1): 2.9 kB
2026-01-22T16:06:58.5635521Z Progress (1): 6.8 kB
2026-01-22T16:06:58.5635808Z Progress (1): 9.3 kB
2026-01-22T16:06:58.5636108Z Progress (1): 9.6 kB
2026-01-22T16:06:58.5636377Z                     
2026-01-22T16:06:58.5636803Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.17.1/jackson-core-2.17.1.pom (9.6 kB at 567 kB/s)
2026-01-22T16:06:58.5684548Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/2.0.16/slf4j-simple-2.0.16.pom
2026-01-22T16:06:58.5861875Z Progress (1): 1.3 kB
2026-01-22T16:06:58.5864388Z                     
2026-01-22T16:06:58.5865521Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/2.0.16/slf4j-simple-2.0.16.pom (1.3 kB at 69 kB/s)
2026-01-22T16:06:58.5893354Z Downloading from central: https://repo.maven.apache.org/maven2/com/aventstack/extentreports/5.1.1/extentreports-5.1.1.pom
2026-01-22T16:06:58.6066770Z Progress (1): 1.2 kB
2026-01-22T16:06:58.6067537Z Progress (1): 3.7 kB
2026-01-22T16:06:58.6068388Z Progress (1): 5.1 kB
2026-01-22T16:06:58.6086452Z                     
2026-01-22T16:06:58.6087634Z Downloaded from central: https://repo.maven.apache.org/maven2/com/aventstack/extentreports/5.1.1/extentreports-5.1.1.pom (5.1 kB at 283 kB/s)
2026-01-22T16:06:58.6095813Z Downloading from central: https://repo.maven.apache.org/maven2/io/reactivex/rxjava3/rxjava/3.1.6/rxjava-3.1.6.pom
2026-01-22T16:06:58.6248390Z Progress (1): 972 B
2026-01-22T16:06:58.6251261Z Progress (1): 1.8 kB
2026-01-22T16:06:58.6254409Z                     
2026-01-22T16:06:58.6255948Z Downloaded from central: https://repo.maven.apache.org/maven2/io/reactivex/rxjava3/rxjava/3.1.6/rxjava-3.1.6.pom (1.8 kB at 111 kB/s)
2026-01-22T16:06:58.6270931Z Downloading from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom
2026-01-22T16:06:58.6446003Z Progress (1): 1.1 kB
2026-01-22T16:06:58.6448708Z                     
2026-01-22T16:06:58.6449798Z Downloaded from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom (1.1 kB at 64 kB/s)
2026-01-22T16:06:58.6464580Z Downloading from central: https://repo.maven.apache.org/maven2/org/freemarker/freemarker/2.3.32/freemarker-2.3.32.pom
2026-01-22T16:06:58.6602560Z Progress (1): 828 B
2026-01-22T16:06:58.6603314Z Progress (1): 2.4 kB
2026-01-22T16:06:58.6606675Z Progress (1): 3.3 kB
2026-01-22T16:06:58.6609378Z                     
2026-01-22T16:06:58.6611218Z Downloaded from central: https://repo.maven.apache.org/maven2/org/freemarker/freemarker/2.3.32/freemarker-2.3.32.pom (3.3 kB at 222 kB/s)
2026-01-22T16:06:58.6619734Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/17/apache-17.pom
2026-01-22T16:06:58.6776701Z Progress (1): 748 B
2026-01-22T16:06:58.6778475Z Progress (1): 2.1 kB
2026-01-22T16:06:58.6781810Z Progress (1): 3.9 kB
2026-01-22T16:06:58.6782509Z Progress (1): 8.1 kB
2026-01-22T16:06:58.6784404Z Progress (1): 12 kB 
2026-01-22T16:06:58.6785071Z Progress (1): 15 kB
2026-01-22T16:06:58.6786645Z Progress (1): 16 kB
2026-01-22T16:06:58.6786952Z                    
2026-01-22T16:06:58.6787313Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/17/apache-17.pom (16 kB at 1.0 MB/s)
2026-01-22T16:06:58.6797174Z Downloading from central: https://repo.maven.apache.org/maven2/org/projectlombok/lombok/1.18.26/lombok-1.18.26.pom
2026-01-22T16:06:58.6971549Z Progress (1): 1.1 kB
2026-01-22T16:06:58.6975370Z Progress (1): 1.5 kB
2026-01-22T16:06:58.6977269Z                     
2026-01-22T16:06:58.6977964Z Downloaded from central: https://repo.maven.apache.org/maven2/org/projectlombok/lombok/1.18.26/lombok-1.18.26.pom (1.5 kB at 82 kB/s)
2026-01-22T16:06:58.6989210Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-cucumber7-jvm/2.29.0/allure-cucumber7-jvm-2.29.0.pom
2026-01-22T16:06:58.7142081Z Progress (1): 1.2 kB
2026-01-22T16:06:58.7147555Z Progress (1): 2.0 kB
2026-01-22T16:06:58.7148405Z                     
2026-01-22T16:06:58.7149598Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-cucumber7-jvm/2.29.0/allure-cucumber7-jvm-2.29.0.pom (2.0 kB at 125 kB/s)
2026-01-22T16:06:58.7169285Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-java-commons/2.29.0/allure-java-commons-2.29.0.pom
2026-01-22T16:06:58.7335860Z Progress (1): 1.2 kB
2026-01-22T16:06:58.7338858Z Progress (1): 2.2 kB
2026-01-22T16:06:58.7341531Z                     
2026-01-22T16:06:58.7343915Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-java-commons/2.29.0/allure-java-commons-2.29.0.pom (2.2 kB at 127 kB/s)
2026-01-22T16:06:58.7351772Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.13/slf4j-api-2.0.13.pom
2026-01-22T16:06:58.7480058Z Progress (1): 1.1 kB
2026-01-22T16:06:58.7484661Z Progress (1): 2.8 kB
2026-01-22T16:06:58.7488589Z                     
2026-01-22T16:06:58.7489279Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.13/slf4j-api-2.0.13.pom (2.8 kB at 202 kB/s)
2026-01-22T16:06:58.7497185Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.13/slf4j-parent-2.0.13.pom
2026-01-22T16:06:58.7655765Z Progress (1): 952 B
2026-01-22T16:06:58.7658311Z Progress (1): 3.2 kB
2026-01-22T16:06:58.7662227Z Progress (1): 6.0 kB
2026-01-22T16:06:58.7663521Z Progress (1): 8.2 kB
2026-01-22T16:06:58.7664712Z Progress (1): 11 kB 
2026-01-22T16:06:58.7665340Z Progress (1): 13 kB
2026-01-22T16:06:58.7666543Z                    
2026-01-22T16:06:58.7667236Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.13/slf4j-parent-2.0.13.pom (13 kB at 786 kB/s)
2026-01-22T16:06:58.7675974Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.13/slf4j-bom-2.0.13.pom
2026-01-22T16:06:58.7847557Z Progress (1): 1.0 kB
2026-01-22T16:06:58.7848224Z Progress (1): 4.6 kB
2026-01-22T16:06:58.7850489Z Progress (1): 7.2 kB
2026-01-22T16:06:58.7851115Z Progress (1): 7.3 kB
2026-01-22T16:06:58.7851633Z                     
2026-01-22T16:06:58.7852340Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.13/slf4j-bom-2.0.13.pom (7.3 kB at 431 kB/s)
2026-01-22T16:06:58.7865427Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-model/2.29.0/allure-model-2.29.0.pom
2026-01-22T16:06:58.8042942Z Progress (1): 1.3 kB
2026-01-22T16:06:58.8046791Z Progress (1): 1.8 kB
2026-01-22T16:06:58.8050903Z                     
2026-01-22T16:06:58.8051616Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-model/2.29.0/allure-model-2.29.0.pom (1.8 kB at 97 kB/s)
2026-01-22T16:06:58.8741364Z Downloading from central: https://repo.maven.apache.org/maven2/io/appium/java-client/8.6.0/java-client-8.6.0.jar
2026-01-22T16:06:58.8746461Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.13.0/selenium-api-4.13.0.jar
2026-01-22T16:06:58.8747407Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.13.0/selenium-remote-driver-4.13.0.jar
2026-01-22T16:06:58.8751869Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.1.1/auto-service-annotations-1.1.1.jar
2026-01-22T16:06:58.8795715Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/32.1.2-jre/guava-32.1.2-jre.jar
2026-01-22T16:06:58.8986767Z Progress (1): 7.7/441 kB
2026-01-22T16:06:58.8999295Z Progress (1): 16/441 kB 
2026-01-22T16:06:58.9004303Z Progress (1): 32/441 kB
2026-01-22T16:06:58.9004890Z Progress (1): 49/441 kB
2026-01-22T16:06:58.9005737Z Progress (1): 65/441 kB
2026-01-22T16:06:58.9093735Z Progress (1): 81/441 kB
2026-01-22T16:06:58.9097757Z Progress (1): 98/441 kB
2026-01-22T16:06:58.9101686Z Progress (1): 114/441 kB
2026-01-22T16:06:58.9105620Z Progress (1): 131/441 kB
2026-01-22T16:06:58.9112964Z Progress (1): 147/441 kB
2026-01-22T16:06:58.9120218Z Progress (1): 163/441 kB
2026-01-22T16:06:58.9160573Z Progress (1): 180/441 kB
2026-01-22T16:06:58.9173885Z Progress (1): 196/441 kB
2026-01-22T16:06:58.9224027Z Progress (1): 213/441 kB
2026-01-22T16:06:58.9224777Z Progress (1): 229/441 kB
2026-01-22T16:06:58.9225361Z Progress (1): 245/441 kB
2026-01-22T16:06:58.9225984Z Progress (1): 262/441 kB
2026-01-22T16:06:58.9226534Z Progress (1): 278/441 kB
2026-01-22T16:06:58.9227142Z Progress (1): 294/441 kB
2026-01-22T16:06:58.9258366Z Progress (1): 311/441 kB
2026-01-22T16:06:58.9259000Z Progress (1): 327/441 kB
2026-01-22T16:06:58.9259621Z Progress (1): 344/441 kB
2026-01-22T16:06:58.9260130Z Progress (1): 360/441 kB
2026-01-22T16:06:58.9260444Z Progress (1): 376/441 kB
2026-01-22T16:06:58.9260910Z Progress (1): 393/441 kB
2026-01-22T16:06:58.9261208Z Progress (1): 409/441 kB
2026-01-22T16:06:58.9261499Z Progress (1): 426/441 kB
2026-01-22T16:06:58.9323466Z Progress (1): 441 kB    
2026-01-22T16:06:58.9324144Z                     
2026-01-22T16:06:58.9324790Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.13.0/selenium-remote-driver-4.13.0.jar (441 kB at 7.4 MB/s)
2026-01-22T16:06:58.9325589Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar
2026-01-22T16:06:58.9436711Z Progress (1): 0.9/227 kB
2026-01-22T16:06:58.9437320Z Progress (1): 2.3/227 kB
2026-01-22T16:06:58.9437806Z Progress (1): 3.6/227 kB
2026-01-22T16:06:58.9438292Z Progress (1): 4.1/227 kB
2026-01-22T16:06:58.9438760Z Progress (1): 5.5/227 kB
2026-01-22T16:06:58.9439248Z Progress (1): 6.8/227 kB
2026-01-22T16:06:58.9439730Z Progress (1): 8.2/227 kB
2026-01-22T16:06:58.9542075Z Progress (1): 9.6/227 kB
2026-01-22T16:06:58.9542926Z Progress (1): 11/227 kB 
2026-01-22T16:06:58.9543581Z Progress (1): 12/227 kB
2026-01-22T16:06:58.9544090Z Progress (1): 14/227 kB
2026-01-22T16:06:58.9544880Z Progress (1): 15/227 kB
2026-01-22T16:06:58.9545198Z Progress (1): 16/227 kB
2026-01-22T16:06:58.9545492Z Progress (1): 18/227 kB
2026-01-22T16:06:58.9545791Z Progress (1): 19/227 kB
2026-01-22T16:06:58.9546091Z Progress (1): 21/227 kB
2026-01-22T16:06:58.9546388Z Progress (1): 22/227 kB
2026-01-22T16:06:58.9546678Z Progress (1): 23/227 kB
2026-01-22T16:06:58.9546974Z Progress (1): 25/227 kB
2026-01-22T16:06:58.9547295Z Progress (1): 26/227 kB
2026-01-22T16:06:58.9547594Z Progress (1): 27/227 kB
2026-01-22T16:06:58.9547883Z Progress (1): 29/227 kB
2026-01-22T16:06:58.9548179Z Progress (1): 30/227 kB
2026-01-22T16:06:58.9548486Z Progress (1): 31/227 kB
2026-01-22T16:06:58.9548805Z Progress (1): 33/227 kB
2026-01-22T16:06:58.9549116Z Progress (1): 34/227 kB
2026-01-22T16:06:58.9549429Z Progress (1): 36/227 kB
2026-01-22T16:06:58.9549752Z Progress (1): 37/227 kB
2026-01-22T16:06:58.9550076Z Progress (1): 38/227 kB
2026-01-22T16:06:58.9550381Z Progress (1): 40/227 kB
2026-01-22T16:06:58.9550691Z Progress (1): 41/227 kB
2026-01-22T16:06:58.9551003Z Progress (1): 42/227 kB
2026-01-22T16:06:58.9551314Z Progress (1): 44/227 kB
2026-01-22T16:06:58.9551619Z Progress (1): 45/227 kB
2026-01-22T16:06:58.9551932Z Progress (1): 47/227 kB
2026-01-22T16:06:58.9552245Z Progress (1): 48/227 kB
2026-01-22T16:06:58.9552557Z Progress (1): 49/227 kB
2026-01-22T16:06:58.9553146Z Progress (1): 51/227 kB
2026-01-22T16:06:58.9553480Z Progress (1): 52/227 kB
2026-01-22T16:06:58.9553800Z Progress (1): 53/227 kB
2026-01-22T16:06:58.9554125Z Progress (1): 55/227 kB
2026-01-22T16:06:58.9554434Z Progress (1): 59/227 kB
2026-01-22T16:06:58.9554745Z Progress (1): 63/227 kB
2026-01-22T16:06:58.9555057Z Progress (1): 67/227 kB
2026-01-22T16:06:58.9555379Z Progress (1): 72/227 kB
2026-01-22T16:06:58.9555690Z Progress (1): 76/227 kB
2026-01-22T16:06:58.9556020Z Progress (1): 80/227 kB
2026-01-22T16:06:58.9556334Z Progress (1): 84/227 kB
2026-01-22T16:06:58.9556643Z Progress (2): 84/227 kB | 4.6 kB
2026-01-22T16:06:58.9556935Z                                 
2026-01-22T16:06:58.9557348Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar (4.6 kB at 59 kB/s)
2026-01-22T16:06:58.9558163Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
2026-01-22T16:06:58.9627503Z Progress (1): 89/227 kB
2026-01-22T16:06:58.9630436Z Progress (1): 93/227 kB
2026-01-22T16:06:58.9630795Z Progress (1): 97/227 kB
2026-01-22T16:06:58.9631121Z Progress (1): 101/227 kB
2026-01-22T16:06:58.9631450Z Progress (1): 105/227 kB
2026-01-22T16:06:58.9631766Z Progress (1): 110/227 kB
2026-01-22T16:06:58.9632095Z Progress (1): 114/227 kB
2026-01-22T16:06:58.9632397Z Progress (1): 118/227 kB
2026-01-22T16:06:58.9633079Z Progress (1): 122/227 kB
2026-01-22T16:06:58.9633408Z Progress (1): 127/227 kB
2026-01-22T16:06:58.9633975Z Progress (1): 127/227 kB
2026-01-22T16:06:58.9634293Z Progress (1): 131/227 kB
2026-01-22T16:06:58.9634618Z Progress (1): 135/227 kB
2026-01-22T16:06:58.9634929Z Progress (1): 140/227 kB
2026-01-22T16:06:58.9635244Z Progress (1): 144/227 kB
2026-01-22T16:06:58.9635924Z Progress (1): 148/227 kB
2026-01-22T16:06:58.9636368Z Progress (1): 152/227 kB
2026-01-22T16:06:58.9636776Z Progress (1): 157/227 kB
2026-01-22T16:06:58.9637179Z Progress (1): 161/227 kB
2026-01-22T16:06:58.9637564Z Progress (1): 165/227 kB
2026-01-22T16:06:58.9637955Z Progress (1): 169/227 kB
2026-01-22T16:06:58.9694262Z Progress (1): 173/227 kB
2026-01-22T16:06:58.9694830Z Progress (1): 178/227 kB
2026-01-22T16:06:58.9695444Z Progress (1): 182/227 kB
2026-01-22T16:06:58.9695801Z Progress (1): 186/227 kB
2026-01-22T16:06:58.9696138Z Progress (1): 190/227 kB
2026-01-22T16:06:58.9696699Z Progress (2): 190/227 kB | 0.9/635 kB
2026-01-22T16:06:58.9697164Z Progress (2): 190/227 kB | 2.3/635 kB
2026-01-22T16:06:58.9697579Z Progress (2): 190/227 kB | 3.6/635 kB
2026-01-22T16:06:58.9697933Z Progress (2): 195/227 kB | 3.6/635 kB
2026-01-22T16:06:58.9698265Z Progress (2): 199/227 kB | 3.6/635 kB
2026-01-22T16:06:58.9698620Z Progress (2): 203/227 kB | 3.6/635 kB
2026-01-22T16:06:58.9699117Z Progress (2): 207/227 kB | 3.6/635 kB
2026-01-22T16:06:58.9699610Z Progress (2): 212/227 kB | 3.6/635 kB
2026-01-22T16:06:58.9700049Z Progress (2): 216/227 kB | 3.6/635 kB
2026-01-22T16:06:58.9700509Z Progress (2): 220/227 kB | 3.6/635 kB
2026-01-22T16:06:58.9700956Z Progress (2): 220/227 kB | 5.0/635 kB
2026-01-22T16:06:58.9701401Z Progress (2): 220/227 kB | 6.4/635 kB
2026-01-22T16:06:58.9701841Z Progress (2): 227 kB | 6.4/635 kB    
2026-01-22T16:06:58.9702256Z Progress (2): 227 kB | 7.7/635 kB
2026-01-22T16:06:58.9702694Z Progress (2): 227 kB | 9.1/635 kB
2026-01-22T16:06:58.9703350Z Progress (2): 227 kB | 10/635 kB 
2026-01-22T16:06:58.9703815Z Progress (2): 227 kB | 12/635 kB
2026-01-22T16:06:58.9704257Z Progress (2): 227 kB | 13/635 kB
2026-01-22T16:06:58.9704701Z Progress (2): 227 kB | 15/635 kB
2026-01-22T16:06:58.9705102Z Progress (2): 227 kB | 16/635 kB
2026-01-22T16:06:58.9720474Z Progress (2): 227 kB | 17/635 kB
2026-01-22T16:06:58.9720837Z Progress (2): 227 kB | 19/635 kB
2026-01-22T16:06:58.9721160Z Progress (2): 227 kB | 20/635 kB
2026-01-22T16:06:58.9721502Z Progress (2): 227 kB | 21/635 kB
2026-01-22T16:06:58.9721812Z                                 
2026-01-22T16:06:58.9722260Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.13.0/selenium-api-4.13.0.jar (227 kB at 2.4 MB/s)
2026-01-22T16:06:58.9722976Z Progress (1): 23/635 kB
2026-01-22T16:06:58.9723357Z Progress (1): 24/635 kB
2026-01-22T16:06:58.9723694Z Progress (1): 26/635 kB
2026-01-22T16:06:58.9724121Z Progress (1): 27/635 kB
2026-01-22T16:06:58.9724460Z Progress (1): 28/635 kB
2026-01-22T16:06:58.9724815Z Progress (1): 30/635 kB
2026-01-22T16:06:58.9725537Z Progress (1): 31/635 kB
2026-01-22T16:06:58.9725874Z Progress (1): 32/635 kB
2026-01-22T16:06:58.9726353Z Progress (1): 34/635 kB
2026-01-22T16:06:58.9726731Z Progress (1): 35/635 kB
2026-01-22T16:06:58.9727056Z Progress (1): 36/635 kB
2026-01-22T16:06:58.9727524Z Progress (1): 38/635 kB
2026-01-22T16:06:58.9729060Z Progress (1): 39/635 kB
2026-01-22T16:06:58.9729779Z Progress (1): 41/635 kB
2026-01-22T16:06:58.9737272Z Progress (1): 42/635 kB
2026-01-22T16:06:58.9738445Z Progress (1): 43/635 kB
2026-01-22T16:06:58.9738762Z Progress (1): 45/635 kB
2026-01-22T16:06:58.9739074Z Progress (1): 46/635 kB
2026-01-22T16:06:58.9739500Z Progress (1): 47/635 kB
2026-01-22T16:06:58.9739835Z Progress (1): 49/635 kB
2026-01-22T16:06:58.9740158Z Progress (1): 50/635 kB
2026-01-22T16:06:58.9753378Z Progress (1): 52/635 kB
2026-01-22T16:06:58.9753898Z Progress (2): 52/635 kB | 2.2 kB
2026-01-22T16:06:58.9754354Z Progress (2): 53/635 kB | 2.2 kB
2026-01-22T16:06:58.9754978Z Progress (2): 54/635 kB | 2.2 kB
2026-01-22T16:06:58.9755443Z                                 
2026-01-22T16:06:58.9755963Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.jar
2026-01-22T16:06:58.9756539Z Progress (2): 56/635 kB | 2.2 kB
2026-01-22T16:06:58.9756941Z Progress (2): 60/635 kB | 2.2 kB
2026-01-22T16:06:58.9757301Z Progress (2): 64/635 kB | 2.2 kB
2026-01-22T16:06:58.9757718Z Progress (2): 68/635 kB | 2.2 kB
2026-01-22T16:06:58.9758731Z Progress (2): 73/635 kB | 2.2 kB
2026-01-22T16:06:58.9759068Z Progress (2): 77/635 kB | 2.2 kB
2026-01-22T16:06:58.9759428Z Progress (2): 81/635 kB | 2.2 kB
2026-01-22T16:06:58.9759750Z Progress (2): 85/635 kB | 2.2 kB
2026-01-22T16:06:58.9760086Z Progress (2): 89/635 kB | 2.2 kB
2026-01-22T16:06:58.9761165Z Progress (2): 94/635 kB | 2.2 kB
2026-01-22T16:06:58.9761588Z Progress (2): 98/635 kB | 2.2 kB
2026-01-22T16:06:58.9761907Z Progress (2): 102/635 kB | 2.2 kB
2026-01-22T16:06:58.9762456Z Progress (2): 106/635 kB | 2.2 kB
2026-01-22T16:06:58.9763110Z Progress (2): 111/635 kB | 2.2 kB
2026-01-22T16:06:58.9763583Z Progress (2): 115/635 kB | 2.2 kB
2026-01-22T16:06:58.9764034Z Progress (2): 119/635 kB | 2.2 kB
2026-01-22T16:06:58.9764438Z Progress (2): 123/635 kB | 2.2 kB
2026-01-22T16:06:58.9764779Z Progress (2): 128/635 kB | 2.2 kB
2026-01-22T16:06:58.9765120Z Progress (2): 132/635 kB | 2.2 kB
2026-01-22T16:06:58.9765640Z Progress (2): 136/635 kB | 2.2 kB
2026-01-22T16:06:58.9766401Z                                  
2026-01-22T16:06:58.9767136Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar (2.2 kB at 23 kB/s)
2026-01-22T16:06:58.9767927Z Downloading from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.33.0/checker-qual-3.33.0.jar
2026-01-22T16:06:58.9768932Z Progress (1): 140/635 kB
2026-01-22T16:06:58.9769567Z Progress (1): 144/635 kB
2026-01-22T16:06:58.9770027Z Progress (1): 149/635 kB
2026-01-22T16:06:58.9770465Z Progress (1): 153/635 kB
2026-01-22T16:06:58.9770872Z Progress (1): 157/635 kB
2026-01-22T16:06:58.9771297Z Progress (1): 161/635 kB
2026-01-22T16:06:58.9771711Z Progress (1): 166/635 kB
2026-01-22T16:06:58.9773185Z Progress (1): 170/635 kB
2026-01-22T16:06:58.9773682Z Progress (1): 174/635 kB
2026-01-22T16:06:58.9774205Z Progress (1): 178/635 kB
2026-01-22T16:06:58.9774634Z Progress (1): 183/635 kB
2026-01-22T16:06:58.9775090Z Progress (1): 187/635 kB
2026-01-22T16:06:58.9775458Z Progress (1): 191/635 kB
2026-01-22T16:06:58.9775784Z Progress (1): 195/635 kB
2026-01-22T16:06:58.9776096Z Progress (1): 199/635 kB
2026-01-22T16:06:58.9776574Z Progress (1): 204/635 kB
2026-01-22T16:06:58.9776987Z Progress (1): 208/635 kB
2026-01-22T16:06:58.9796258Z Progress (1): 212/635 kB
2026-01-22T16:06:58.9796719Z Progress (1): 216/635 kB
2026-01-22T16:06:58.9797117Z Progress (1): 221/635 kB
2026-01-22T16:06:58.9797532Z Progress (1): 225/635 kB
2026-01-22T16:06:58.9797950Z Progress (1): 241/635 kB
2026-01-22T16:06:58.9798384Z Progress (1): 258/635 kB
2026-01-22T16:06:58.9798793Z Progress (1): 274/635 kB
2026-01-22T16:06:58.9799197Z Progress (1): 290/635 kB
2026-01-22T16:06:58.9799592Z Progress (1): 307/635 kB
2026-01-22T16:06:58.9823830Z Progress (1): 323/635 kB
2026-01-22T16:06:58.9824469Z Progress (1): 340/635 kB
2026-01-22T16:06:58.9846740Z Progress (1): 356/635 kB
2026-01-22T16:06:58.9847244Z Progress (2): 356/635 kB | 0.9/3.2 kB
2026-01-22T16:06:58.9847670Z Progress (2): 356/635 kB | 2.3/3.2 kB
2026-01-22T16:06:58.9848116Z Progress (2): 356/635 kB | 3.2 kB    
2026-01-22T16:06:58.9849011Z                                  
2026-01-22T16:06:58.9849484Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.1.1/auto-service-annotations-1.1.1.jar (3.2 kB at 29 kB/s)
2026-01-22T16:06:58.9850075Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.18.0/error_prone_annotations-2.18.0.jar
2026-01-22T16:06:58.9850676Z Progress (1): 372/635 kB
2026-01-22T16:06:58.9850982Z Progress (1): 389/635 kB
2026-01-22T16:06:58.9851269Z Progress (1): 405/635 kB
2026-01-22T16:06:58.9851609Z Progress (1): 421/635 kB
2026-01-22T16:06:58.9851943Z Progress (1): 438/635 kB
2026-01-22T16:06:58.9852289Z Progress (1): 454/635 kB
2026-01-22T16:06:58.9852625Z Progress (1): 471/635 kB
2026-01-22T16:06:58.9853337Z Progress (1): 487/635 kB
2026-01-22T16:06:58.9853756Z Progress (1): 503/635 kB
2026-01-22T16:06:58.9883204Z Progress (1): 520/635 kB
2026-01-22T16:06:58.9883680Z Progress (1): 536/635 kB
2026-01-22T16:06:58.9884880Z Progress (1): 552/635 kB
2026-01-22T16:06:58.9885618Z Progress (1): 569/635 kB
2026-01-22T16:06:58.9886248Z Progress (1): 585/635 kB
2026-01-22T16:06:58.9886863Z Progress (1): 602/635 kB
2026-01-22T16:06:58.9887291Z Progress (1): 618/635 kB
2026-01-22T16:06:58.9888310Z Progress (2): 618/635 kB | 7.7/20 kB
2026-01-22T16:06:58.9889069Z Progress (2): 634/635 kB | 7.7/20 kB
2026-01-22T16:06:58.9889534Z Progress (2): 634/635 kB | 16/20 kB 
2026-01-22T16:06:58.9889939Z Progress (2): 634/635 kB | 20 kB   
2026-01-22T16:06:58.9890348Z Progress (2): 635 kB | 20 kB    
2026-01-22T16:06:58.9890760Z                             
2026-01-22T16:06:58.9891278Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.jar (20 kB at 178 kB/s)
2026-01-22T16:06:58.9891955Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/2.8/j2objc-annotations-2.8.jar
2026-01-22T16:06:58.9914382Z Progress (2): 635 kB | 0/3.0 MB
2026-01-22T16:06:58.9914997Z Progress (2): 635 kB | 0/3.0 MB
2026-01-22T16:06:58.9915432Z Progress (2): 635 kB | 0/3.0 MB
2026-01-22T16:06:58.9915907Z Progress (2): 635 kB | 0/3.0 MB
2026-01-22T16:06:58.9916358Z Progress (2): 635 kB | 0/3.0 MB
2026-01-22T16:06:58.9916816Z Progress (2): 635 kB | 0/3.0 MB
2026-01-22T16:06:58.9917282Z Progress (2): 635 kB | 0/3.0 MB
2026-01-22T16:06:58.9917746Z Progress (2): 635 kB | 0/3.0 MB
2026-01-22T16:06:58.9918187Z Progress (2): 635 kB | 0/3.0 MB
2026-01-22T16:06:58.9918624Z Progress (2): 635 kB | 0/3.0 MB
2026-01-22T16:06:58.9920350Z                                
2026-01-22T16:06:58.9920814Z Downloaded from central: https://repo.maven.apache.org/maven2/io/appium/java-client/8.6.0/java-client-8.6.0.jar (635 kB at 5.2 MB/s)
2026-01-22T16:06:58.9921388Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.96.Final/netty-buffer-4.1.96.Final.jar
2026-01-22T16:06:58.9966593Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9966921Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9967225Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9967515Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9967807Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9968103Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9968385Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9968679Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9968978Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9969268Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9969554Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9969847Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9970129Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9970419Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9970708Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9970999Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9971429Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9971727Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9972014Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9972309Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9974277Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9974567Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9974897Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9975194Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9975483Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9975779Z Progress (1): 0/3.0 MB
2026-01-22T16:06:58.9976072Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9976375Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9976794Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9977112Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9977403Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9977702Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9977989Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9978285Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9978571Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9978875Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9979160Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9979452Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9979746Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9980045Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9980346Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9980646Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9980954Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9981249Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9981550Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9981852Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9982167Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:58.9982470Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:59.0023072Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:59.0023701Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:59.0034414Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:59.0034886Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:59.0035307Z Progress (1): 0.1/3.0 MB
2026-01-22T16:06:59.0035705Z Progress (1): 0.2/3.0 MB
2026-01-22T16:06:59.0036100Z Progress (1): 0.2/3.0 MB
2026-01-22T16:06:59.0036495Z Progress (1): 0.2/3.0 MB
2026-01-22T16:06:59.0036894Z Progress (2): 0.2/3.0 MB | 7.7/224 kB
2026-01-22T16:06:59.0037311Z Progress (2): 0.2/3.0 MB | 16/224 kB 
2026-01-22T16:06:59.0037722Z Progress (2): 0.2/3.0 MB | 16/224 kB
2026-01-22T16:06:59.0039156Z Progress (2): 0.2/3.0 MB | 16/224 kB
2026-01-22T16:06:59.0040301Z Progress (2): 0.2/3.0 MB | 16/224 kB
2026-01-22T16:06:59.0043175Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0047193Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0047985Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0048384Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0048773Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0049083Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0049458Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0049773Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0050149Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0050520Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0050892Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0051264Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0051681Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0051988Z Progress (2): 0.2/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0079677Z Progress (2): 0.3/3.0 MB | 32/224 kB
2026-01-22T16:06:59.0080499Z Progress (2): 0.3/3.0 MB | 49/224 kB
2026-01-22T16:06:59.0087099Z Progress (2): 0.3/3.0 MB | 49/224 kB
2026-01-22T16:06:59.0088343Z Progress (2): 0.3/3.0 MB | 65/224 kB
2026-01-22T16:06:59.0089079Z Progress (2): 0.3/3.0 MB | 65/224 kB
2026-01-22T16:06:59.0090401Z Progress (2): 0.3/3.0 MB | 81/224 kB
2026-01-22T16:06:59.0091172Z Progress (2): 0.3/3.0 MB | 81/224 kB
2026-01-22T16:06:59.0092969Z Progress (2): 0.3/3.0 MB | 98/224 kB
2026-01-22T16:06:59.0093968Z Progress (2): 0.3/3.0 MB | 114/224 kB
2026-01-22T16:06:59.0094798Z Progress (2): 0.3/3.0 MB | 131/224 kB
2026-01-22T16:06:59.0095510Z Progress (2): 0.3/3.0 MB | 131/224 kB
2026-01-22T16:06:59.0096421Z Progress (2): 0.3/3.0 MB | 131/224 kB
2026-01-22T16:06:59.0097294Z Progress (2): 0.3/3.0 MB | 147/224 kB
2026-01-22T16:06:59.0098725Z Progress (2): 0.4/3.0 MB | 147/224 kB
2026-01-22T16:06:59.0111536Z Progress (2): 0.4/3.0 MB | 163/224 kB
2026-01-22T16:06:59.0112402Z Progress (2): 0.4/3.0 MB | 163/224 kB
2026-01-22T16:06:59.0113660Z Progress (2): 0.4/3.0 MB | 180/224 kB
2026-01-22T16:06:59.0114668Z Progress (2): 0.4/3.0 MB | 180/224 kB
2026-01-22T16:06:59.0115679Z Progress (2): 0.4/3.0 MB | 196/224 kB
2026-01-22T16:06:59.0120337Z Progress (2): 0.4/3.0 MB | 196/224 kB
2026-01-22T16:06:59.0123795Z Progress (2): 0.4/3.0 MB | 213/224 kB
2026-01-22T16:06:59.0124277Z Progress (2): 0.4/3.0 MB | 213/224 kB
2026-01-22T16:06:59.0124901Z Progress (2): 0.4/3.0 MB | 224 kB    
2026-01-22T16:06:59.0125735Z Progress (2): 0.4/3.0 MB | 224 kB
2026-01-22T16:06:59.0126256Z                                  
2026-01-22T16:06:59.0150899Z Downloaded from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.33.0/checker-qual-3.33.0.jar (224 kB at 1.7 MB/s)
2026-01-22T16:06:59.0151404Z Progress (2): 0.4/3.0 MB | 7.7/306 kB
2026-01-22T16:06:59.0151718Z Progress (2): 0.4/3.0 MB | 12/306 kB 
2026-01-22T16:06:59.0152027Z Progress (2): 0.4/3.0 MB | 29/306 kB
2026-01-22T16:06:59.0152344Z Progress (2): 0.4/3.0 MB | 45/306 kB
2026-01-22T16:06:59.0152654Z Progress (2): 0.4/3.0 MB | 61/306 kB
2026-01-22T16:06:59.0153251Z Progress (2): 0.4/3.0 MB | 78/306 kB
2026-01-22T16:06:59.0153564Z Progress (2): 0.4/3.0 MB | 94/306 kB
2026-01-22T16:06:59.0153871Z Progress (2): 0.4/3.0 MB | 111/306 kB
2026-01-22T16:06:59.0154189Z Progress (2): 0.4/3.0 MB | 127/306 kB
2026-01-22T16:06:59.0154471Z                                      
2026-01-22T16:06:59.0154866Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.96.Final/netty-codec-http-4.1.96.Final.jar
2026-01-22T16:06:59.0191732Z Progress (3): 0.4/3.0 MB | 127/306 kB | 0.9/16 kB
2026-01-22T16:06:59.0192141Z Progress (3): 0.4/3.0 MB | 127/306 kB | 2.3/16 kB
2026-01-22T16:06:59.0192474Z Progress (3): 0.4/3.0 MB | 127/306 kB | 3.6/16 kB
2026-01-22T16:06:59.0193012Z Progress (3): 0.4/3.0 MB | 127/306 kB | 5.0/16 kB
2026-01-22T16:06:59.0193374Z Progress (3): 0.4/3.0 MB | 127/306 kB | 6.4/16 kB
2026-01-22T16:06:59.0193744Z Progress (3): 0.4/3.0 MB | 127/306 kB | 7.7/16 kB
2026-01-22T16:06:59.0194105Z Progress (3): 0.4/3.0 MB | 127/306 kB | 9.1/16 kB
2026-01-22T16:06:59.0194467Z Progress (3): 0.4/3.0 MB | 127/306 kB | 10/16 kB 
2026-01-22T16:06:59.0194828Z Progress (3): 0.4/3.0 MB | 127/306 kB | 12/16 kB
2026-01-22T16:06:59.0195211Z Progress (3): 0.4/3.0 MB | 127/306 kB | 13/16 kB
2026-01-22T16:06:59.0195579Z Progress (3): 0.4/3.0 MB | 127/306 kB | 15/16 kB
2026-01-22T16:06:59.0195927Z Progress (3): 0.4/3.0 MB | 127/306 kB | 16/16 kB
2026-01-22T16:06:59.0196323Z Progress (3): 0.4/3.0 MB | 127/306 kB | 16 kB   
2026-01-22T16:06:59.0196614Z                                              
2026-01-22T16:06:59.0197037Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.18.0/error_prone_annotations-2.18.0.jar (16 kB at 114 kB/s)
2026-01-22T16:06:59.0197566Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.96.Final/netty-codec-4.1.96.Final.jar
2026-01-22T16:06:59.0197959Z Progress (2): 0.4/3.0 MB | 143/306 kB
2026-01-22T16:06:59.0198267Z Progress (2): 0.4/3.0 MB | 160/306 kB
2026-01-22T16:06:59.0198572Z Progress (2): 0.4/3.0 MB | 176/306 kB
2026-01-22T16:06:59.0198872Z Progress (2): 0.4/3.0 MB | 193/306 kB
2026-01-22T16:06:59.0199179Z Progress (2): 0.4/3.0 MB | 209/306 kB
2026-01-22T16:06:59.0199480Z Progress (2): 0.4/3.0 MB | 225/306 kB
2026-01-22T16:06:59.0199798Z Progress (2): 0.4/3.0 MB | 242/306 kB
2026-01-22T16:06:59.0200115Z Progress (2): 0.4/3.0 MB | 258/306 kB
2026-01-22T16:06:59.0200441Z Progress (3): 0.4/3.0 MB | 258/306 kB | 7.7/9.3 kB
2026-01-22T16:06:59.0200777Z Progress (3): 0.4/3.0 MB | 258/306 kB | 9.3 kB    
2026-01-22T16:06:59.0201239Z                                               
2026-01-22T16:06:59.0201648Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/2.8/j2objc-annotations-2.8.jar (9.3 kB at 66 kB/s)
2026-01-22T16:06:59.0202180Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.96.Final/netty-handler-4.1.96.Final.jar
2026-01-22T16:06:59.0207261Z Progress (2): 0.4/3.0 MB | 274/306 kB
2026-01-22T16:06:59.0207611Z Progress (2): 0.5/3.0 MB | 274/306 kB
2026-01-22T16:06:59.0207932Z Progress (2): 0.5/3.0 MB | 274/306 kB
2026-01-22T16:06:59.0208389Z Progress (2): 0.5/3.0 MB | 274/306 kB
2026-01-22T16:06:59.0208702Z Progress (2): 0.5/3.0 MB | 274/306 kB
2026-01-22T16:06:59.0209022Z Progress (2): 0.5/3.0 MB | 274/306 kB
2026-01-22T16:06:59.0209333Z Progress (2): 0.5/3.0 MB | 291/306 kB
2026-01-22T16:06:59.0209650Z Progress (2): 0.5/3.0 MB | 291/306 kB
2026-01-22T16:06:59.0209959Z Progress (2): 0.5/3.0 MB | 306 kB    
2026-01-22T16:06:59.0210280Z Progress (2): 0.6/3.0 MB | 306 kB
2026-01-22T16:06:59.0210562Z                                  
2026-01-22T16:06:59.0210977Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.96.Final/netty-buffer-4.1.96.Final.jar (306 kB at 2.1 MB/s)
2026-01-22T16:06:59.0211517Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.96.Final/netty-common-4.1.96.Final.jar
2026-01-22T16:06:59.0211919Z Progress (1): 0.6/3.0 MB
2026-01-22T16:06:59.0221928Z Progress (1): 0.6/3.0 MB
2026-01-22T16:06:59.0222257Z Progress (1): 0.6/3.0 MB
2026-01-22T16:06:59.0222571Z Progress (1): 0.6/3.0 MB
2026-01-22T16:06:59.0227386Z Progress (1): 0.6/3.0 MB
2026-01-22T16:06:59.0232041Z Progress (1): 0.7/3.0 MB
2026-01-22T16:06:59.0236693Z Progress (1): 0.7/3.0 MB
2026-01-22T16:06:59.0241203Z Progress (1): 0.7/3.0 MB
2026-01-22T16:06:59.0245938Z Progress (1): 0.7/3.0 MB
2026-01-22T16:06:59.0250431Z Progress (1): 0.7/3.0 MB
2026-01-22T16:06:59.0273870Z Progress (1): 0.7/3.0 MB
2026-01-22T16:06:59.0274404Z Progress (1): 0.7/3.0 MB
2026-01-22T16:06:59.0274828Z Progress (1): 0.8/3.0 MB
2026-01-22T16:06:59.0275221Z Progress (1): 0.8/3.0 MB
2026-01-22T16:06:59.0275621Z Progress (1): 0.8/3.0 MB
2026-01-22T16:06:59.0276019Z Progress (1): 0.8/3.0 MB
2026-01-22T16:06:59.0278416Z Progress (1): 0.8/3.0 MB
2026-01-22T16:06:59.0279869Z Progress (1): 0.8/3.0 MB
2026-01-22T16:06:59.0281222Z Progress (1): 0.9/3.0 MB
2026-01-22T16:06:59.0289497Z Progress (1): 0.9/3.0 MB
2026-01-22T16:06:59.0294423Z Progress (1): 0.9/3.0 MB
2026-01-22T16:06:59.0298862Z Progress (1): 0.9/3.0 MB
2026-01-22T16:06:59.0314543Z Progress (1): 0.9/3.0 MB
2026-01-22T16:06:59.0315100Z Progress (1): 0.9/3.0 MB
2026-01-22T16:06:59.0315556Z Progress (1): 1.0/3.0 MB
2026-01-22T16:06:59.0315990Z Progress (1): 1.0/3.0 MB
2026-01-22T16:06:59.0316418Z Progress (1): 1.0/3.0 MB
2026-01-22T16:06:59.0319762Z Progress (1): 1.0/3.0 MB
2026-01-22T16:06:59.0324576Z Progress (1): 1.0/3.0 MB
2026-01-22T16:06:59.0329236Z Progress (1): 1.0/3.0 MB
2026-01-22T16:06:59.0331267Z Progress (1): 1.1/3.0 MB
2026-01-22T16:06:59.0332915Z Progress (2): 1.1/3.0 MB | 7.7/657 kB
2026-01-22T16:06:59.0353979Z Progress (2): 1.1/3.0 MB | 16/657 kB 
2026-01-22T16:06:59.0357415Z Progress (2): 1.1/3.0 MB | 16/657 kB
2026-01-22T16:06:59.0358387Z Progress (2): 1.1/3.0 MB | 16/657 kB
2026-01-22T16:06:59.0359982Z Progress (2): 1.1/3.0 MB | 16/657 kB
2026-01-22T16:06:59.0360319Z Progress (2): 1.1/3.0 MB | 16/657 kB
2026-01-22T16:06:59.0360661Z Progress (2): 1.1/3.0 MB | 16/657 kB
2026-01-22T16:06:59.0360968Z Progress (2): 1.1/3.0 MB | 29/657 kB
2026-01-22T16:06:59.0361292Z Progress (2): 1.2/3.0 MB | 29/657 kB
2026-01-22T16:06:59.0361611Z Progress (2): 1.2/3.0 MB | 45/657 kB
2026-01-22T16:06:59.0377710Z Progress (2): 1.2/3.0 MB | 45/657 kB
2026-01-22T16:06:59.0378196Z Progress (2): 1.2/3.0 MB | 45/657 kB
2026-01-22T16:06:59.0378661Z Progress (3): 1.2/3.0 MB | 45/657 kB | 7.7/660 kB
2026-01-22T16:06:59.0379101Z Progress (3): 1.2/3.0 MB | 45/657 kB | 16/660 kB 
2026-01-22T16:06:59.0380786Z Progress (3): 1.2/3.0 MB | 45/657 kB | 32/660 kB
2026-01-22T16:06:59.0381250Z Progress (3): 1.2/3.0 MB | 45/657 kB | 49/660 kB
2026-01-22T16:06:59.0405294Z Progress (3): 1.2/3.0 MB | 45/657 kB | 49/660 kB
2026-01-22T16:06:59.0405834Z Progress (3): 1.2/3.0 MB | 45/657 kB | 65/660 kB
2026-01-22T16:06:59.0406267Z Progress (3): 1.2/3.0 MB | 45/657 kB | 65/660 kB
2026-01-22T16:06:59.0464080Z Progress (3): 1.2/3.0 MB | 45/657 kB | 81/660 kB
2026-01-22T16:06:59.0464621Z Progress (3): 1.2/3.0 MB | 45/657 kB | 81/660 kB
2026-01-22T16:06:59.0465119Z Progress (3): 1.2/3.0 MB | 45/657 kB | 98/660 kB
2026-01-22T16:06:59.0465720Z Progress (3): 1.3/3.0 MB | 45/657 kB | 98/660 kB
2026-01-22T16:06:59.0466253Z Progress (3): 1.3/3.0 MB | 45/657 kB | 114/660 kB
2026-01-22T16:06:59.0466697Z Progress (3): 1.3/3.0 MB | 45/657 kB | 114/660 kB
2026-01-22T16:06:59.0467131Z Progress (3): 1.3/3.0 MB | 61/657 kB | 114/660 kB
2026-01-22T16:06:59.0467609Z Progress (3): 1.3/3.0 MB | 78/657 kB | 114/660 kB
2026-01-22T16:06:59.0468130Z Progress (3): 1.3/3.0 MB | 94/657 kB | 114/660 kB
2026-01-22T16:06:59.0468617Z Progress (3): 1.3/3.0 MB | 111/657 kB | 114/660 kB
2026-01-22T16:06:59.0469078Z Progress (3): 1.3/3.0 MB | 127/657 kB | 114/660 kB
2026-01-22T16:06:59.0470093Z Progress (4): 1.3/3.0 MB | 127/657 kB | 114/660 kB | 7.7/558 kB
2026-01-22T16:06:59.0491687Z Progress (4): 1.3/3.0 MB | 127/657 kB | 114/660 kB | 8.2/558 kB
2026-01-22T16:06:59.0492291Z Progress (4): 1.3/3.0 MB | 143/657 kB | 114/660 kB | 8.2/558 kB
2026-01-22T16:06:59.0492911Z Progress (4): 1.3/3.0 MB | 143/657 kB | 114/660 kB | 25/558 kB 
2026-01-22T16:06:59.0493428Z Progress (4): 1.3/3.0 MB | 160/657 kB | 114/660 kB | 25/558 kB
2026-01-22T16:06:59.0493888Z Progress (4): 1.3/3.0 MB | 160/657 kB | 114/660 kB | 41/558 kB
2026-01-22T16:06:59.0494347Z Progress (4): 1.3/3.0 MB | 160/657 kB | 114/660 kB | 57/558 kB
2026-01-22T16:06:59.0494808Z Progress (4): 1.3/3.0 MB | 160/657 kB | 114/660 kB | 66/558 kB
2026-01-22T16:06:59.0495259Z Progress (4): 1.3/3.0 MB | 160/657 kB | 114/660 kB | 74/558 kB
2026-01-22T16:06:59.0495725Z Progress (4): 1.3/3.0 MB | 160/657 kB | 114/660 kB | 74/558 kB
2026-01-22T16:06:59.0496171Z Progress (4): 1.3/3.0 MB | 160/657 kB | 114/660 kB | 74/558 kB
2026-01-22T16:06:59.0496628Z Progress (4): 1.3/3.0 MB | 160/657 kB | 114/660 kB | 74/558 kB
2026-01-22T16:06:59.0497069Z Progress (4): 1.3/3.0 MB | 160/657 kB | 131/660 kB | 74/558 kB
2026-01-22T16:06:59.0497529Z Progress (4): 1.3/3.0 MB | 160/657 kB | 131/660 kB | 74/558 kB
2026-01-22T16:06:59.0497979Z Progress (4): 1.3/3.0 MB | 160/657 kB | 147/660 kB | 74/558 kB
2026-01-22T16:06:59.0498425Z Progress (4): 1.4/3.0 MB | 160/657 kB | 147/660 kB | 74/558 kB
2026-01-22T16:06:59.0498886Z Progress (4): 1.4/3.0 MB | 160/657 kB | 163/660 kB | 74/558 kB
2026-01-22T16:06:59.0499330Z Progress (4): 1.4/3.0 MB | 160/657 kB | 163/660 kB | 74/558 kB
2026-01-22T16:06:59.0499789Z Progress (4): 1.4/3.0 MB | 160/657 kB | 180/660 kB | 74/558 kB
2026-01-22T16:06:59.0500235Z Progress (4): 1.4/3.0 MB | 160/657 kB | 196/660 kB | 74/558 kB
2026-01-22T16:06:59.0500713Z Progress (5): 1.4/3.0 MB | 160/657 kB | 196/660 kB | 74/558 kB | 0.9/345 kB
2026-01-22T16:06:59.0501181Z Progress (5): 1.4/3.0 MB | 160/657 kB | 196/660 kB | 74/558 kB | 2.3/345 kB
2026-01-22T16:06:59.0501667Z Progress (5): 1.4/3.0 MB | 160/657 kB | 196/660 kB | 74/558 kB | 3.6/345 kB
2026-01-22T16:06:59.0502142Z Progress (5): 1.4/3.0 MB | 160/657 kB | 196/660 kB | 74/558 kB | 5.0/345 kB
2026-01-22T16:06:59.0502599Z Progress (5): 1.4/3.0 MB | 160/657 kB | 213/660 kB | 74/558 kB | 5.0/345 kB
2026-01-22T16:06:59.0503256Z Progress (5): 1.4/3.0 MB | 160/657 kB | 213/660 kB | 74/558 kB | 6.4/345 kB
2026-01-22T16:06:59.0503727Z Progress (5): 1.4/3.0 MB | 160/657 kB | 213/660 kB | 74/558 kB | 7.7/345 kB
2026-01-22T16:06:59.0504219Z Progress (5): 1.4/3.0 MB | 160/657 kB | 213/660 kB | 74/558 kB | 9.1/345 kB
2026-01-22T16:06:59.0504671Z Progress (5): 1.4/3.0 MB | 160/657 kB | 213/660 kB | 74/558 kB | 10/345 kB 
2026-01-22T16:06:59.0536623Z Progress (5): 1.4/3.0 MB | 160/657 kB | 213/660 kB | 74/558 kB | 12/345 kB
2026-01-22T16:06:59.0537148Z Progress (5): 1.4/3.0 MB | 160/657 kB | 213/660 kB | 74/558 kB | 13/345 kB
2026-01-22T16:06:59.0537649Z Progress (5): 1.4/3.0 MB | 160/657 kB | 229/660 kB | 74/558 kB | 13/345 kB
2026-01-22T16:06:59.0538116Z Progress (5): 1.4/3.0 MB | 160/657 kB | 229/660 kB | 74/558 kB | 15/345 kB
2026-01-22T16:06:59.0538598Z Progress (5): 1.4/3.0 MB | 160/657 kB | 229/660 kB | 74/558 kB | 16/345 kB
2026-01-22T16:06:59.0539054Z Progress (5): 1.4/3.0 MB | 160/657 kB | 229/660 kB | 74/558 kB | 17/345 kB
2026-01-22T16:06:59.0539685Z Progress (5): 1.4/3.0 MB | 160/657 kB | 229/660 kB | 74/558 kB | 19/345 kB
2026-01-22T16:06:59.0540913Z Progress (5): 1.4/3.0 MB | 160/657 kB | 229/660 kB | 74/558 kB | 20/345 kB
2026-01-22T16:06:59.0542301Z Progress (5): 1.4/3.0 MB | 160/657 kB | 229/660 kB | 74/558 kB | 21/345 kB
2026-01-22T16:06:59.0563359Z Progress (5): 1.4/3.0 MB | 160/657 kB | 245/660 kB | 74/558 kB | 21/345 kB
2026-01-22T16:06:59.0563951Z Progress (5): 1.4/3.0 MB | 160/657 kB | 245/660 kB | 74/558 kB | 23/345 kB
2026-01-22T16:06:59.0564428Z Progress (5): 1.4/3.0 MB | 160/657 kB | 245/660 kB | 74/558 kB | 24/345 kB
2026-01-22T16:06:59.0564942Z Progress (5): 1.4/3.0 MB | 160/657 kB | 245/660 kB | 74/558 kB | 26/345 kB
2026-01-22T16:06:59.0565412Z Progress (5): 1.4/3.0 MB | 160/657 kB | 245/660 kB | 74/558 kB | 27/345 kB
2026-01-22T16:06:59.0565905Z Progress (5): 1.4/3.0 MB | 176/657 kB | 245/660 kB | 74/558 kB | 27/345 kB
2026-01-22T16:06:59.0566374Z Progress (5): 1.4/3.0 MB | 176/657 kB | 245/660 kB | 74/558 kB | 28/345 kB
2026-01-22T16:06:59.0566842Z Progress (5): 1.4/3.0 MB | 176/657 kB | 245/660 kB | 74/558 kB | 30/345 kB
2026-01-22T16:06:59.0567331Z Progress (5): 1.4/3.0 MB | 176/657 kB | 245/660 kB | 74/558 kB | 31/345 kB
2026-01-22T16:06:59.0567787Z Progress (5): 1.4/3.0 MB | 176/657 kB | 245/660 kB | 74/558 kB | 32/345 kB
2026-01-22T16:06:59.0568278Z Progress (5): 1.4/3.0 MB | 176/657 kB | 245/660 kB | 74/558 kB | 33/345 kB
2026-01-22T16:06:59.0568738Z Progress (5): 1.4/3.0 MB | 193/657 kB | 245/660 kB | 74/558 kB | 33/345 kB
2026-01-22T16:06:59.0569226Z Progress (5): 1.4/3.0 MB | 193/657 kB | 245/660 kB | 74/558 kB | 38/345 kB
2026-01-22T16:06:59.0569685Z Progress (5): 1.4/3.0 MB | 193/657 kB | 245/660 kB | 74/558 kB | 42/345 kB
2026-01-22T16:06:59.0570156Z Progress (5): 1.4/3.0 MB | 193/657 kB | 245/660 kB | 74/558 kB | 46/345 kB
2026-01-22T16:06:59.0570620Z Progress (5): 1.4/3.0 MB | 209/657 kB | 245/660 kB | 74/558 kB | 46/345 kB
2026-01-22T16:06:59.0571138Z Progress (5): 1.4/3.0 MB | 209/657 kB | 245/660 kB | 74/558 kB | 50/345 kB
2026-01-22T16:06:59.0571642Z Progress (5): 1.4/3.0 MB | 225/657 kB | 245/660 kB | 74/558 kB | 50/345 kB
2026-01-22T16:06:59.0572111Z Progress (5): 1.4/3.0 MB | 225/657 kB | 245/660 kB | 74/558 kB | 55/345 kB
2026-01-22T16:06:59.0572589Z Progress (5): 1.4/3.0 MB | 225/657 kB | 245/660 kB | 74/558 kB | 59/345 kB
2026-01-22T16:06:59.0653476Z Progress (5): 1.4/3.0 MB | 225/657 kB | 245/660 kB | 74/558 kB | 63/345 kB
2026-01-22T16:06:59.0654399Z Progress (5): 1.4/3.0 MB | 242/657 kB | 245/660 kB | 74/558 kB | 63/345 kB
2026-01-22T16:06:59.0655142Z Progress (5): 1.4/3.0 MB | 250/657 kB | 245/660 kB | 74/558 kB | 63/345 kB
2026-01-22T16:06:59.0655860Z Progress (5): 1.4/3.0 MB | 266/657 kB | 245/660 kB | 74/558 kB | 63/345 kB
2026-01-22T16:06:59.0656579Z Progress (5): 1.4/3.0 MB | 282/657 kB | 245/660 kB | 74/558 kB | 63/345 kB
2026-01-22T16:06:59.0657287Z Progress (5): 1.4/3.0 MB | 282/657 kB | 245/660 kB | 90/558 kB | 63/345 kB
2026-01-22T16:06:59.0658010Z Progress (5): 1.4/3.0 MB | 282/657 kB | 262/660 kB | 90/558 kB | 63/345 kB
2026-01-22T16:06:59.0658742Z Progress (5): 1.4/3.0 MB | 282/657 kB | 262/660 kB | 106/558 kB | 63/345 kB
2026-01-22T16:06:59.0723470Z Progress (5): 1.4/3.0 MB | 282/657 kB | 278/660 kB | 106/558 kB | 63/345 kB
2026-01-22T16:06:59.0724446Z Progress (5): 1.4/3.0 MB | 282/657 kB | 278/660 kB | 123/558 kB | 63/345 kB
2026-01-22T16:06:59.0725240Z Progress (5): 1.4/3.0 MB | 282/657 kB | 294/660 kB | 123/558 kB | 63/345 kB
2026-01-22T16:06:59.0726188Z Progress (5): 1.4/3.0 MB | 282/657 kB | 294/660 kB | 139/558 kB | 63/345 kB
2026-01-22T16:06:59.0726925Z Progress (5): 1.4/3.0 MB | 282/657 kB | 311/660 kB | 139/558 kB | 63/345 kB
2026-01-22T16:06:59.0727638Z Progress (5): 1.4/3.0 MB | 282/657 kB | 311/660 kB | 156/558 kB | 63/345 kB
2026-01-22T16:06:59.0728373Z Progress (5): 1.4/3.0 MB | 282/657 kB | 327/660 kB | 156/558 kB | 63/345 kB
2026-01-22T16:06:59.0753391Z Progress (5): 1.4/3.0 MB | 282/657 kB | 327/660 kB | 172/558 kB | 63/345 kB
2026-01-22T16:06:59.0754281Z Progress (5): 1.4/3.0 MB | 282/657 kB | 344/660 kB | 172/558 kB | 63/345 kB
2026-01-22T16:06:59.0755280Z Progress (5): 1.4/3.0 MB | 282/657 kB | 344/660 kB | 188/558 kB | 63/345 kB
2026-01-22T16:06:59.0756049Z Progress (5): 1.4/3.0 MB | 282/657 kB | 360/660 kB | 188/558 kB | 63/345 kB
2026-01-22T16:06:59.0756831Z Progress (5): 1.4/3.0 MB | 282/657 kB | 360/660 kB | 205/558 kB | 63/345 kB
2026-01-22T16:06:59.0757591Z Progress (5): 1.4/3.0 MB | 282/657 kB | 376/660 kB | 205/558 kB | 63/345 kB
2026-01-22T16:06:59.0758396Z Progress (5): 1.4/3.0 MB | 282/657 kB | 376/660 kB | 221/558 kB | 63/345 kB
2026-01-22T16:06:59.0759159Z Progress (5): 1.4/3.0 MB | 282/657 kB | 393/660 kB | 221/558 kB | 63/345 kB
2026-01-22T16:06:59.0759902Z Progress (5): 1.4/3.0 MB | 282/657 kB | 393/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0760636Z Progress (5): 1.4/3.0 MB | 282/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0761468Z Progress (5): 1.4/3.0 MB | 299/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0762252Z Progress (5): 1.4/3.0 MB | 315/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0763206Z Progress (5): 1.4/3.0 MB | 331/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0764074Z Progress (5): 1.4/3.0 MB | 348/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0764825Z Progress (5): 1.4/3.0 MB | 364/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0765563Z Progress (5): 1.4/3.0 MB | 381/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0766286Z Progress (5): 1.4/3.0 MB | 397/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0766994Z Progress (5): 1.4/3.0 MB | 397/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0767718Z Progress (5): 1.4/3.0 MB | 397/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0768426Z Progress (5): 1.4/3.0 MB | 413/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0769132Z Progress (5): 1.4/3.0 MB | 430/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0769848Z Progress (5): 1.4/3.0 MB | 430/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0770543Z Progress (5): 1.4/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0771253Z Progress (5): 1.4/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0771964Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0772690Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0773612Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0774320Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 63/345 kB
2026-01-22T16:06:59.0775029Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 67/345 kB
2026-01-22T16:06:59.0775729Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 71/345 kB
2026-01-22T16:06:59.0776437Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 76/345 kB
2026-01-22T16:06:59.0777152Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 80/345 kB
2026-01-22T16:06:59.0777852Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 84/345 kB
2026-01-22T16:06:59.0778553Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 88/345 kB
2026-01-22T16:06:59.0779254Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 93/345 kB
2026-01-22T16:06:59.0780149Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 97/345 kB
2026-01-22T16:06:59.0780876Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 101/345 kB
2026-01-22T16:06:59.0781589Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 105/345 kB
2026-01-22T16:06:59.0782319Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 110/345 kB
2026-01-22T16:06:59.0783212Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 114/345 kB
2026-01-22T16:06:59.0783972Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 118/345 kB
2026-01-22T16:06:59.0784897Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 122/345 kB
2026-01-22T16:06:59.0785705Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 126/345 kB
2026-01-22T16:06:59.0794392Z Progress (5): 1.5/3.0 MB | 446/657 kB | 409/660 kB | 225/558 kB | 131/345 kB
2026-01-22T16:06:59.0795405Z Progress (5): 1.5/3.0 MB | 446/657 kB | 426/660 kB | 225/558 kB | 131/345 kB
2026-01-22T16:06:59.0796214Z Progress (5): 1.5/3.0 MB | 446/657 kB | 426/660 kB | 225/558 kB | 135/345 kB
2026-01-22T16:06:59.0796985Z Progress (5): 1.5/3.0 MB | 446/657 kB | 426/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0797797Z Progress (5): 1.5/3.0 MB | 446/657 kB | 442/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0798561Z Progress (5): 1.5/3.0 MB | 446/657 kB | 458/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0799323Z Progress (5): 1.5/3.0 MB | 446/657 kB | 475/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0800087Z Progress (5): 1.5/3.0 MB | 463/657 kB | 475/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0800793Z Progress (5): 1.5/3.0 MB | 479/657 kB | 475/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0801501Z Progress (5): 1.5/3.0 MB | 495/657 kB | 475/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0802218Z Progress (5): 1.5/3.0 MB | 512/657 kB | 475/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0803134Z Progress (5): 1.5/3.0 MB | 528/657 kB | 475/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0803891Z Progress (5): 1.5/3.0 MB | 544/657 kB | 475/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0804601Z Progress (5): 1.5/3.0 MB | 561/657 kB | 475/660 kB | 225/558 kB | 139/345 kB
2026-01-22T16:06:59.0805311Z Progress (5): 1.5/3.0 MB | 561/657 kB | 475/660 kB | 241/558 kB | 139/345 kB
2026-01-22T16:06:59.0805998Z Progress (5): 1.5/3.0 MB | 561/657 kB | 475/660 kB | 254/558 kB | 139/345 kB
2026-01-22T16:06:59.0806721Z Progress (5): 1.5/3.0 MB | 577/657 kB | 475/660 kB | 254/558 kB | 139/345 kB
2026-01-22T16:06:59.0807437Z Progress (5): 1.5/3.0 MB | 577/657 kB | 475/660 kB | 270/558 kB | 139/345 kB
2026-01-22T16:06:59.0808134Z Progress (5): 1.5/3.0 MB | 594/657 kB | 475/660 kB | 270/558 kB | 139/345 kB
2026-01-22T16:06:59.0808836Z Progress (5): 1.5/3.0 MB | 594/657 kB | 475/660 kB | 287/558 kB | 139/345 kB
2026-01-22T16:06:59.0809541Z Progress (5): 1.5/3.0 MB | 610/657 kB | 475/660 kB | 287/558 kB | 139/345 kB
2026-01-22T16:06:59.0810326Z Progress (5): 1.5/3.0 MB | 610/657 kB | 491/660 kB | 287/558 kB | 139/345 kB
2026-01-22T16:06:59.0811032Z Progress (5): 1.5/3.0 MB | 610/657 kB | 491/660 kB | 303/558 kB | 139/345 kB
2026-01-22T16:06:59.0833366Z Progress (5): 1.5/3.0 MB | 610/657 kB | 507/660 kB | 303/558 kB | 139/345 kB
2026-01-22T16:06:59.0834264Z Progress (5): 1.5/3.0 MB | 610/657 kB | 507/660 kB | 319/558 kB | 139/345 kB
2026-01-22T16:06:59.0835043Z Progress (5): 1.5/3.0 MB | 610/657 kB | 524/660 kB | 319/558 kB | 139/345 kB
2026-01-22T16:06:59.0835804Z Progress (5): 1.5/3.0 MB | 610/657 kB | 524/660 kB | 336/558 kB | 139/345 kB
2026-01-22T16:06:59.0836548Z Progress (5): 1.5/3.0 MB | 610/657 kB | 540/660 kB | 336/558 kB | 139/345 kB
2026-01-22T16:06:59.0837312Z Progress (5): 1.5/3.0 MB | 610/657 kB | 540/660 kB | 352/558 kB | 139/345 kB
2026-01-22T16:06:59.0838086Z Progress (5): 1.5/3.0 MB | 610/657 kB | 540/660 kB | 369/558 kB | 139/345 kB
2026-01-22T16:06:59.0838980Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 139/345 kB
2026-01-22T16:06:59.0839833Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 143/345 kB
2026-01-22T16:06:59.0853426Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 148/345 kB
2026-01-22T16:06:59.0854369Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 152/345 kB
2026-01-22T16:06:59.0855123Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 156/345 kB
2026-01-22T16:06:59.0855899Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 160/345 kB
2026-01-22T16:06:59.0856780Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 163/345 kB
2026-01-22T16:06:59.0857478Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 167/345 kB
2026-01-22T16:06:59.0858176Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 172/345 kB
2026-01-22T16:06:59.0858939Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 176/345 kB
2026-01-22T16:06:59.0860074Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 180/345 kB
2026-01-22T16:06:59.0860447Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 184/345 kB
2026-01-22T16:06:59.0860807Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 188/345 kB
2026-01-22T16:06:59.0861169Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 193/345 kB
2026-01-22T16:06:59.0861529Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 197/345 kB
2026-01-22T16:06:59.0861894Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 201/345 kB
2026-01-22T16:06:59.0862257Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 218/345 kB
2026-01-22T16:06:59.0862631Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 234/345 kB
2026-01-22T16:06:59.0863168Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 250/345 kB
2026-01-22T16:06:59.0863549Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0863964Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0864348Z Progress (5): 1.5/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0864725Z Progress (5): 1.6/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0865121Z Progress (5): 1.6/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0865492Z Progress (5): 1.6/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0865851Z Progress (5): 1.6/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0866253Z Progress (5): 1.6/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0866622Z Progress (5): 1.6/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0867001Z Progress (5): 1.7/3.0 MB | 610/657 kB | 557/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0867367Z Progress (5): 1.7/3.0 MB | 610/657 kB | 573/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0867752Z Progress (5): 1.7/3.0 MB | 610/657 kB | 573/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0868158Z Progress (5): 1.7/3.0 MB | 610/657 kB | 589/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0868558Z Progress (5): 1.7/3.0 MB | 610/657 kB | 606/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0868964Z Progress (5): 1.7/3.0 MB | 610/657 kB | 622/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0869356Z Progress (5): 1.7/3.0 MB | 610/657 kB | 639/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0869781Z Progress (5): 1.7/3.0 MB | 610/657 kB | 655/660 kB | 369/558 kB | 267/345 kB
2026-01-22T16:06:59.0870192Z Progress (5): 1.7/3.0 MB | 610/657 kB | 660 kB | 369/558 kB | 267/345 kB    
2026-01-22T16:06:59.0870548Z                                                                         
2026-01-22T16:06:59.0870986Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.96.Final/netty-common-4.1.96.Final.jar (660 kB at 3.2 MB/s)
2026-01-22T16:06:59.0871629Z Progress (4): 1.7/3.0 MB | 610/657 kB | 385/558 kB | 267/345 kB
2026-01-22T16:06:59.0871981Z Progress (4): 1.7/3.0 MB | 610/657 kB | 401/558 kB | 267/345 kB
2026-01-22T16:06:59.0872331Z Progress (4): 1.7/3.0 MB | 610/657 kB | 418/558 kB | 267/345 kB
2026-01-22T16:06:59.0872672Z Progress (4): 1.7/3.0 MB | 610/657 kB | 434/558 kB | 267/345 kB
2026-01-22T16:06:59.0873244Z Progress (4): 1.7/3.0 MB | 610/657 kB | 451/558 kB | 267/345 kB
2026-01-22T16:06:59.0873627Z Progress (4): 1.7/3.0 MB | 610/657 kB | 467/558 kB | 267/345 kB
2026-01-22T16:06:59.0874165Z Progress (4): 1.7/3.0 MB | 610/657 kB | 483/558 kB | 267/345 kB
2026-01-22T16:06:59.0874556Z Progress (4): 1.7/3.0 MB | 626/657 kB | 483/558 kB | 267/345 kB
2026-01-22T16:06:59.0874937Z Progress (4): 1.7/3.0 MB | 626/657 kB | 500/558 kB | 267/345 kB
2026-01-22T16:06:59.0875329Z Progress (4): 1.7/3.0 MB | 643/657 kB | 500/558 kB | 267/345 kB
2026-01-22T16:06:59.0875724Z Progress (4): 1.7/3.0 MB | 643/657 kB | 516/558 kB | 267/345 kB
2026-01-22T16:06:59.0876111Z Progress (4): 1.7/3.0 MB | 657 kB | 516/558 kB | 267/345 kB    
2026-01-22T16:06:59.0876463Z Progress (4): 1.7/3.0 MB | 657 kB | 532/558 kB | 267/345 kB
2026-01-22T16:06:59.0876882Z                                                            
2026-01-22T16:06:59.0877290Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.96.Final/netty-codec-http-4.1.96.Final.jar (657 kB at 3.2 MB/s)
2026-01-22T16:06:59.0877744Z Progress (3): 1.7/3.0 MB | 549/558 kB | 267/345 kB
2026-01-22T16:06:59.0878048Z                                                   
2026-01-22T16:06:59.0878474Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.96.Final/netty-transport-classes-epoll-4.1.96.Final.jar
2026-01-22T16:06:59.0879224Z Progress (3): 1.7/3.0 MB | 549/558 kB | 283/345 kB
2026-01-22T16:06:59.0879697Z Progress (3): 1.7/3.0 MB | 549/558 kB | 294/345 kB
2026-01-22T16:06:59.0880111Z                                                   
2026-01-22T16:06:59.0880650Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.96.Final/netty-transport-classes-kqueue-4.1.96.Final.jar
2026-01-22T16:06:59.0881209Z Progress (3): 1.7/3.0 MB | 549/558 kB | 311/345 kB
2026-01-22T16:06:59.0881638Z Progress (3): 1.7/3.0 MB | 549/558 kB | 327/345 kB
2026-01-22T16:06:59.0882076Z Progress (3): 1.7/3.0 MB | 549/558 kB | 343/345 kB
2026-01-22T16:06:59.0882521Z Progress (3): 1.7/3.0 MB | 549/558 kB | 345 kB    
2026-01-22T16:06:59.0883088Z                                               
2026-01-22T16:06:59.0883606Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.96.Final/netty-codec-4.1.96.Final.jar (345 kB at 1.7 MB/s)
2026-01-22T16:06:59.0884268Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final.jar
2026-01-22T16:06:59.0884827Z Progress (2): 1.7/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0885243Z Progress (2): 1.7/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0885664Z Progress (2): 1.7/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0886069Z Progress (2): 1.7/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0886487Z Progress (2): 1.7/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0886903Z Progress (2): 1.8/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0887310Z Progress (2): 1.8/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0887738Z Progress (2): 1.8/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0888153Z Progress (2): 1.8/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0888574Z Progress (2): 1.8/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0888980Z Progress (2): 1.8/3.0 MB | 549/558 kB
2026-01-22T16:06:59.0889395Z Progress (2): 1.8/3.0 MB | 558 kB    
2026-01-22T16:06:59.0889770Z                                  
2026-01-22T16:06:59.0890271Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.96.Final/netty-handler-4.1.96.Final.jar (558 kB at 2.7 MB/s)
2026-01-22T16:06:59.0891101Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final.jar
2026-01-22T16:06:59.0891632Z Progress (1): 1.9/3.0 MB
2026-01-22T16:06:59.0892038Z Progress (1): 1.9/3.0 MB
2026-01-22T16:06:59.0892437Z Progress (1): 1.9/3.0 MB
2026-01-22T16:06:59.0892978Z Progress (1): 1.9/3.0 MB
2026-01-22T16:06:59.0893404Z Progress (1): 1.9/3.0 MB
2026-01-22T16:06:59.0893791Z Progress (1): 1.9/3.0 MB
2026-01-22T16:06:59.0894178Z Progress (1): 2.0/3.0 MB
2026-01-22T16:06:59.0894719Z Progress (1): 2.0/3.0 MB
2026-01-22T16:06:59.0895133Z Progress (2): 2.0/3.0 MB | 7.7/108 kB
2026-01-22T16:06:59.0895540Z Progress (2): 2.0/3.0 MB | 7.7/108 kB
2026-01-22T16:06:59.0895959Z Progress (2): 2.0/3.0 MB | 16/108 kB 
2026-01-22T16:06:59.0896359Z Progress (2): 2.0/3.0 MB | 32/108 kB
2026-01-22T16:06:59.0896767Z Progress (2): 2.0/3.0 MB | 49/108 kB
2026-01-22T16:06:59.0897181Z Progress (2): 2.0/3.0 MB | 65/108 kB
2026-01-22T16:06:59.0938560Z Progress (2): 2.0/3.0 MB | 81/108 kB
2026-01-22T16:06:59.0938958Z Progress (2): 2.0/3.0 MB | 98/108 kB
2026-01-22T16:06:59.0943661Z Progress (2): 2.0/3.0 MB | 108 kB   
2026-01-22T16:06:59.0943986Z                                  
2026-01-22T16:06:59.0944448Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.96.Final/netty-transport-classes-kqueue-4.1.96.Final.jar (108 kB at 507 kB/s)
2026-01-22T16:06:59.0945232Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.96.Final/netty-transport-native-unix-common-4.1.96.Final.jar
2026-01-22T16:06:59.0945804Z Progress (1): 2.0/3.0 MB
2026-01-22T16:06:59.0946218Z Progress (1): 2.0/3.0 MB
2026-01-22T16:06:59.0946623Z Progress (1): 2.0/3.0 MB
2026-01-22T16:06:59.0947018Z Progress (1): 2.1/3.0 MB
2026-01-22T16:06:59.0947424Z Progress (1): 2.1/3.0 MB
2026-01-22T16:06:59.0947827Z Progress (1): 2.1/3.0 MB
2026-01-22T16:06:59.0964347Z Progress (1): 2.1/3.0 MB
2026-01-22T16:06:59.0964670Z Progress (1): 2.1/3.0 MB
2026-01-22T16:06:59.0965005Z Progress (1): 2.1/3.0 MB
2026-01-22T16:06:59.0965298Z Progress (1): 2.2/3.0 MB
2026-01-22T16:06:59.0965794Z Progress (2): 2.2/3.0 MB | 7.7/147 kB
2026-01-22T16:06:59.0966230Z Progress (2): 2.2/3.0 MB | 16/147 kB 
2026-01-22T16:06:59.0966644Z Progress (2): 2.2/3.0 MB | 16/147 kB
2026-01-22T16:06:59.0967623Z Progress (2): 2.2/3.0 MB | 29/147 kB
2026-01-22T16:06:59.0968128Z Progress (2): 2.2/3.0 MB | 29/147 kB
2026-01-22T16:06:59.0968555Z Progress (2): 2.2/3.0 MB | 45/147 kB
2026-01-22T16:06:59.0968975Z Progress (2): 2.2/3.0 MB | 45/147 kB
2026-01-22T16:06:59.0969384Z Progress (2): 2.2/3.0 MB | 61/147 kB
2026-01-22T16:06:59.0969781Z Progress (2): 2.2/3.0 MB | 61/147 kB
2026-01-22T16:06:59.0970197Z Progress (2): 2.2/3.0 MB | 78/147 kB
2026-01-22T16:06:59.0970629Z Progress (2): 2.2/3.0 MB | 78/147 kB
2026-01-22T16:06:59.0971062Z Progress (2): 2.2/3.0 MB | 94/147 kB
2026-01-22T16:06:59.0971511Z Progress (3): 2.2/3.0 MB | 94/147 kB | 5.7 kB
2026-01-22T16:06:59.0971906Z                                              
2026-01-22T16:06:59.0972452Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final.jar (5.7 kB at 26 kB/s)
2026-01-22T16:06:59.0973280Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.96.Final/netty-transport-4.1.96.Final.jar
2026-01-22T16:06:59.0977485Z Progress (2): 2.3/3.0 MB | 94/147 kB
2026-01-22T16:06:59.0977919Z Progress (2): 2.3/3.0 MB | 94/147 kB
2026-01-22T16:06:59.0978271Z Progress (2): 2.3/3.0 MB | 94/147 kB
2026-01-22T16:06:59.0978767Z Progress (2): 2.3/3.0 MB | 94/147 kB
2026-01-22T16:06:59.0979212Z Progress (2): 2.3/3.0 MB | 111/147 kB
2026-01-22T16:06:59.0979663Z Progress (2): 2.3/3.0 MB | 127/147 kB
2026-01-22T16:06:59.0980110Z Progress (2): 2.3/3.0 MB | 127/147 kB
2026-01-22T16:06:59.0980791Z Progress (2): 2.3/3.0 MB | 143/147 kB
2026-01-22T16:06:59.0985900Z Progress (2): 2.3/3.0 MB | 147 kB    
2026-01-22T16:06:59.0989949Z Progress (2): 2.3/3.0 MB | 147 kB
2026-01-22T16:06:59.0992528Z Progress (2): 2.4/3.0 MB | 147 kB
2026-01-22T16:06:59.0993175Z                                  
2026-01-22T16:06:59.0993736Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.96.Final/netty-transport-classes-epoll-4.1.96.Final.jar (147 kB at 663 kB/s)
2026-01-22T16:06:59.0996632Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.96.Final/netty-resolver-4.1.96.Final.jar
2026-01-22T16:06:59.1009107Z Progress (1): 2.4/3.0 MB
2026-01-22T16:06:59.1013742Z Progress (1): 2.4/3.0 MB
2026-01-22T16:06:59.1021778Z Progress (1): 2.4/3.0 MB
2026-01-22T16:06:59.1025678Z Progress (1): 2.4/3.0 MB
2026-01-22T16:06:59.1031859Z Progress (2): 2.4/3.0 MB | 7.7/44 kB
2026-01-22T16:06:59.1033802Z Progress (3): 2.4/3.0 MB | 7.7/44 kB | 5.7 kB
2026-01-22T16:06:59.1035396Z Progress (3): 2.4/3.0 MB | 16/44 kB | 5.7 kB 
2026-01-22T16:06:59.1045150Z Progress (3): 2.4/3.0 MB | 28/44 kB | 5.7 kB
2026-01-22T16:06:59.1046490Z                                             
2026-01-22T16:06:59.1047913Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final.jar (5.7 kB at 25 kB/s)
2026-01-22T16:06:59.1049518Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.28.0/opentelemetry-api-1.28.0.jar
2026-01-22T16:06:59.1050798Z Progress (2): 2.4/3.0 MB | 44 kB
2026-01-22T16:06:59.1051314Z Progress (2): 2.4/3.0 MB | 44 kB
2026-01-22T16:06:59.1051836Z                                 
2026-01-22T16:06:59.1052522Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.96.Final/netty-transport-native-unix-common-4.1.96.Final.jar (44 kB at 193 kB/s)
2026-01-22T16:06:59.1054310Z Progress (1): 2.5/3.0 MB
2026-01-22T16:06:59.1054601Z                         
2026-01-22T16:06:59.1054991Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.28.0/opentelemetry-context-1.28.0.jar
2026-01-22T16:06:59.1074059Z Progress (1): 2.5/3.0 MB
2026-01-22T16:06:59.1075118Z Progress (1): 2.5/3.0 MB
2026-01-22T16:06:59.1085034Z Progress (1): 2.5/3.0 MB
2026-01-22T16:06:59.1085511Z Progress (1): 2.5/3.0 MB
2026-01-22T16:06:59.1085928Z Progress (1): 2.5/3.0 MB
2026-01-22T16:06:59.1086446Z Progress (1): 2.6/3.0 MB
2026-01-22T16:06:59.1087492Z Progress (1): 2.6/3.0 MB
2026-01-22T16:06:59.1087842Z Progress (1): 2.6/3.0 MB
2026-01-22T16:06:59.1088153Z Progress (1): 2.6/3.0 MB
2026-01-22T16:06:59.1091333Z Progress (1): 2.6/3.0 MB
2026-01-22T16:06:59.1095973Z Progress (1): 2.6/3.0 MB
2026-01-22T16:06:59.1100646Z Progress (1): 2.6/3.0 MB
2026-01-22T16:06:59.1105549Z Progress (1): 2.7/3.0 MB
2026-01-22T16:06:59.1110050Z Progress (1): 2.7/3.0 MB
2026-01-22T16:06:59.1114877Z Progress (1): 2.7/3.0 MB
2026-01-22T16:06:59.1134198Z Progress (1): 2.7/3.0 MB
2026-01-22T16:06:59.1134711Z Progress (1): 2.7/3.0 MB
2026-01-22T16:06:59.1135151Z Progress (1): 2.7/3.0 MB
2026-01-22T16:06:59.1135590Z Progress (1): 2.8/3.0 MB
2026-01-22T16:06:59.1136014Z Progress (1): 2.8/3.0 MB
2026-01-22T16:06:59.1136440Z Progress (1): 2.8/3.0 MB
2026-01-22T16:06:59.1136988Z Progress (1): 2.8/3.0 MB
2026-01-22T16:06:59.1140580Z Progress (1): 2.8/3.0 MB
2026-01-22T16:06:59.1145196Z Progress (1): 2.8/3.0 MB
2026-01-22T16:06:59.1149403Z Progress (1): 2.9/3.0 MB
2026-01-22T16:06:59.1154099Z Progress (1): 2.9/3.0 MB
2026-01-22T16:06:59.1158975Z Progress (1): 2.9/3.0 MB
2026-01-22T16:06:59.1163360Z Progress (1): 2.9/3.0 MB
2026-01-22T16:06:59.1174491Z Progress (1): 2.9/3.0 MB
2026-01-22T16:06:59.1174840Z Progress (1): 2.9/3.0 MB
2026-01-22T16:06:59.1175139Z Progress (1): 3.0/3.0 MB
2026-01-22T16:06:59.1175434Z Progress (1): 3.0/3.0 MB
2026-01-22T16:06:59.1207979Z Progress (1): 3.0/3.0 MB
2026-01-22T16:06:59.1208667Z Progress (1): 3.0/3.0 MB
2026-01-22T16:06:59.1209082Z Progress (1): 3.0/3.0 MB
2026-01-22T16:06:59.1209476Z Progress (1): 3.0 MB    
2026-01-22T16:06:59.1209861Z Progress (2): 3.0 MB | 7.7/490 kB
2026-01-22T16:06:59.1210268Z Progress (2): 3.0 MB | 16/490 kB 
2026-01-22T16:06:59.1210670Z Progress (2): 3.0 MB | 32/490 kB
2026-01-22T16:06:59.1211823Z Progress (2): 3.0 MB | 49/490 kB
2026-01-22T16:06:59.1212139Z                                 
2026-01-22T16:06:59.1212552Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/32.1.2-jre/guava-32.1.2-jre.jar (3.0 MB at 12 MB/s)
2026-01-22T16:06:59.1213505Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.28.0/opentelemetry-exporter-logging-1.28.0.jar
2026-01-22T16:06:59.1214007Z Progress (1): 65/490 kB
2026-01-22T16:06:59.1214345Z Progress (1): 81/490 kB
2026-01-22T16:06:59.1214672Z Progress (2): 81/490 kB | 7.7/47 kB
2026-01-22T16:06:59.1215027Z Progress (2): 81/490 kB | 16/47 kB 
2026-01-22T16:06:59.1215349Z Progress (2): 81/490 kB | 32/47 kB
2026-01-22T16:06:59.1215679Z Progress (2): 81/490 kB | 47 kB   
2026-01-22T16:06:59.1215970Z                                
2026-01-22T16:06:59.1216414Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.28.0/opentelemetry-context-1.28.0.jar (47 kB at 194 kB/s)
2026-01-22T16:06:59.1217000Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.28.0/opentelemetry-sdk-metrics-1.28.0.jar
2026-01-22T16:06:59.1246564Z Progress (1): 98/490 kB
2026-01-22T16:06:59.1249154Z Progress (1): 114/490 kB
2026-01-22T16:06:59.1253236Z Progress (1): 131/490 kB
2026-01-22T16:06:59.1253612Z Progress (1): 147/490 kB
2026-01-22T16:06:59.1253942Z Progress (1): 163/490 kB
2026-01-22T16:06:59.1254261Z Progress (1): 180/490 kB
2026-01-22T16:06:59.1254601Z Progress (1): 196/490 kB
2026-01-22T16:06:59.1255401Z Progress (1): 213/490 kB
2026-01-22T16:06:59.1256030Z Progress (1): 229/490 kB
2026-01-22T16:06:59.1256963Z Progress (1): 245/490 kB
2026-01-22T16:06:59.1258277Z Progress (1): 262/490 kB
2026-01-22T16:06:59.1258945Z Progress (1): 278/490 kB
2026-01-22T16:06:59.1259384Z Progress (2): 278/490 kB | 7.7/38 kB
2026-01-22T16:06:59.1283368Z Progress (2): 278/490 kB | 16/38 kB 
2026-01-22T16:06:59.1316385Z Progress (2): 278/490 kB | 32/38 kB
2026-01-22T16:06:59.1317623Z Progress (2): 278/490 kB | 38 kB   
2026-01-22T16:06:59.1318216Z                                 
2026-01-22T16:06:59.1327181Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.96.Final/netty-resolver-4.1.96.Final.jar (38 kB at 151 kB/s)
2026-01-22T16:06:59.1327792Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.28.0/opentelemetry-sdk-logs-1.28.0.jar
2026-01-22T16:06:59.1328251Z Progress (2): 278/490 kB | 7.7/138 kB
2026-01-22T16:06:59.1328593Z Progress (2): 278/490 kB | 8.2/138 kB
2026-01-22T16:06:59.1328941Z Progress (2): 278/490 kB | 25/138 kB 
2026-01-22T16:06:59.1329266Z Progress (2): 278/490 kB | 41/138 kB
2026-01-22T16:06:59.1329599Z Progress (2): 278/490 kB | 57/138 kB
2026-01-22T16:06:59.1329930Z Progress (2): 278/490 kB | 74/138 kB
2026-01-22T16:06:59.1330260Z Progress (2): 278/490 kB | 90/138 kB
2026-01-22T16:06:59.1330583Z Progress (2): 278/490 kB | 106/138 kB
2026-01-22T16:06:59.1330919Z Progress (2): 278/490 kB | 110/138 kB
2026-01-22T16:06:59.1331246Z Progress (2): 278/490 kB | 126/138 kB
2026-01-22T16:06:59.1331581Z Progress (2): 278/490 kB | 138 kB    
2026-01-22T16:06:59.1331912Z Progress (2): 294/490 kB | 138 kB
2026-01-22T16:06:59.1332240Z Progress (2): 311/490 kB | 138 kB
2026-01-22T16:06:59.1332559Z Progress (2): 327/490 kB | 138 kB
2026-01-22T16:06:59.1333071Z Progress (2): 344/490 kB | 138 kB
2026-01-22T16:06:59.1333399Z Progress (2): 360/490 kB | 138 kB
2026-01-22T16:06:59.1333726Z Progress (2): 376/490 kB | 138 kB
2026-01-22T16:06:59.1334047Z Progress (2): 393/490 kB | 138 kB
2026-01-22T16:06:59.1334537Z Progress (2): 409/490 kB | 138 kB
2026-01-22T16:06:59.1334862Z Progress (2): 426/490 kB | 138 kB
2026-01-22T16:06:59.1335191Z Progress (2): 442/490 kB | 138 kB
2026-01-22T16:06:59.1335589Z Progress (2): 458/490 kB | 138 kB
2026-01-22T16:06:59.1335919Z Progress (2): 475/490 kB | 138 kB
2026-01-22T16:06:59.1336344Z                                  
2026-01-22T16:06:59.1336779Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.28.0/opentelemetry-api-1.28.0.jar (138 kB at 541 kB/s)
2026-01-22T16:06:59.1337354Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.28.0/opentelemetry-sdk-common-1.28.0.jar
2026-01-22T16:06:59.1351822Z Progress (1): 490 kB
2026-01-22T16:06:59.1352132Z                     
2026-01-22T16:06:59.1352537Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.96.Final/netty-transport-4.1.96.Final.jar (490 kB at 1.9 MB/s)
2026-01-22T16:06:59.1353340Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.28.0/opentelemetry-sdk-extension-autoconfigure-spi-1.28.0.jar
2026-01-22T16:06:59.1375912Z Progress (1): 7.7/259 kB
2026-01-22T16:06:59.1376257Z Progress (1): 16/259 kB 
2026-01-22T16:06:59.1376564Z Progress (1): 32/259 kB
2026-01-22T16:06:59.1376872Z Progress (1): 49/259 kB
2026-01-22T16:06:59.1377179Z Progress (1): 65/259 kB
2026-01-22T16:06:59.1377483Z Progress (1): 81/259 kB
2026-01-22T16:06:59.1377774Z Progress (1): 98/259 kB
2026-01-22T16:06:59.1378090Z Progress (1): 114/259 kB
2026-01-22T16:06:59.1381133Z Progress (1): 131/259 kB
2026-01-22T16:06:59.1385905Z Progress (1): 147/259 kB
2026-01-22T16:06:59.1389791Z Progress (1): 163/259 kB
2026-01-22T16:06:59.1405770Z Progress (1): 180/259 kB
2026-01-22T16:06:59.1406107Z Progress (1): 196/259 kB
2026-01-22T16:06:59.1406426Z Progress (1): 213/259 kB
2026-01-22T16:06:59.1406730Z Progress (1): 229/259 kB
2026-01-22T16:06:59.1407052Z Progress (1): 245/259 kB
2026-01-22T16:06:59.1411020Z Progress (1): 259 kB    
2026-01-22T16:06:59.1411341Z                     
2026-01-22T16:06:59.1411783Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.28.0/opentelemetry-sdk-metrics-1.28.0.jar (259 kB at 984 kB/s)
2026-01-22T16:06:59.1414740Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.28.0/opentelemetry-sdk-extension-autoconfigure-1.28.0.jar
2026-01-22T16:06:59.1449206Z Progress (1): 7.7/11 kB
2026-01-22T16:06:59.1454573Z Progress (1): 11 kB    
2026-01-22T16:06:59.1457457Z                    
2026-01-22T16:06:59.1463803Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.28.0/opentelemetry-exporter-logging-1.28.0.jar (11 kB at 42 kB/s)
2026-01-22T16:06:59.1467059Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.28.0/opentelemetry-sdk-trace-1.28.0.jar
2026-01-22T16:06:59.1512567Z Progress (1): 7.7/47 kB
2026-01-22T16:06:59.1514829Z Progress (1): 16/47 kB 
2026-01-22T16:06:59.1516344Z Progress (1): 32/47 kB
2026-01-22T16:06:59.1517766Z Progress (1): 47 kB   
2026-01-22T16:06:59.1518636Z                    
2026-01-22T16:06:59.1519230Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.28.0/opentelemetry-sdk-logs-1.28.0.jar (47 kB at 172 kB/s)
2026-01-22T16:06:59.1522458Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.28.0/opentelemetry-sdk-1.28.0.jar
2026-01-22T16:06:59.1546744Z Progress (1): 7.7/42 kB
2026-01-22T16:06:59.1551877Z Progress (1): 8.2/42 kB
2026-01-22T16:06:59.1558220Z Progress (1): 25/42 kB 
2026-01-22T16:06:59.1558846Z Progress (1): 41/42 kB
2026-01-22T16:06:59.1590432Z Progress (1): 42 kB   
2026-01-22T16:06:59.1590818Z Progress (2): 42 kB | 7.7/40 kB
2026-01-22T16:06:59.1591313Z Progress (2): 42 kB | 16/40 kB 
2026-01-22T16:06:59.1591861Z Progress (2): 42 kB | 32/40 kB
2026-01-22T16:06:59.1592194Z Progress (2): 42 kB | 40 kB   
2026-01-22T16:06:59.1592638Z                            
2026-01-22T16:06:59.1593398Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.28.0/opentelemetry-sdk-common-1.28.0.jar (42 kB at 151 kB/s)
2026-01-22T16:06:59.1594200Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.28.0-alpha/opentelemetry-semconv-1.28.0-alpha.jar
2026-01-22T16:06:59.1595024Z Progress (2): 40 kB | 7.7/16 kB
2026-01-22T16:06:59.1614763Z Progress (2): 40 kB | 16/16 kB 
2026-01-22T16:06:59.1615224Z                               
2026-01-22T16:06:59.1615811Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.28.0/opentelemetry-sdk-extension-autoconfigure-1.28.0.jar (40 kB at 142 kB/s)
2026-01-22T16:06:59.1616537Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.5/byte-buddy-1.14.5.jar
2026-01-22T16:06:59.1617037Z Progress (1): 16 kB
2026-01-22T16:06:59.1617421Z                    
2026-01-22T16:06:59.1617984Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.28.0/opentelemetry-sdk-extension-autoconfigure-spi-1.28.0.jar (16 kB at 58 kB/s)
2026-01-22T16:06:59.1618694Z Downloading from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client/2.12.3/async-http-client-2.12.3.jar
2026-01-22T16:06:59.1709998Z Progress (1): 7.7/117 kB
2026-01-22T16:06:59.1713421Z Progress (1): 16/117 kB 
2026-01-22T16:06:59.1717745Z Progress (1): 32/117 kB
2026-01-22T16:06:59.1740707Z Progress (1): 49/117 kB
2026-01-22T16:06:59.1741174Z Progress (1): 65/117 kB
2026-01-22T16:06:59.1741576Z Progress (1): 81/117 kB
2026-01-22T16:06:59.1741975Z Progress (1): 98/117 kB
2026-01-22T16:06:59.1742407Z Progress (1): 114/117 kB
2026-01-22T16:06:59.1743014Z Progress (2): 114/117 kB | 6.8 kB
2026-01-22T16:06:59.1743353Z Progress (2): 117 kB | 6.8 kB    
2026-01-22T16:06:59.1750613Z Progress (3): 117 kB | 6.8 kB | 7.7/40 kB
2026-01-22T16:06:59.1750950Z                                          
2026-01-22T16:06:59.1751389Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.28.0/opentelemetry-sdk-trace-1.28.0.jar (117 kB at 395 kB/s)
2026-01-22T16:06:59.1751850Z Progress (2): 6.8 kB | 12/40 kB
2026-01-22T16:06:59.1752152Z                                
2026-01-22T16:06:59.1752590Z Downloading from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-netty-utils/2.12.3/async-http-client-netty-utils-2.12.3.jar
2026-01-22T16:06:59.1768515Z Progress (2): 6.8 kB | 29/40 kB
2026-01-22T16:06:59.1768997Z Progress (2): 6.8 kB | 40 kB   
2026-01-22T16:06:59.1769310Z                             
2026-01-22T16:06:59.1769780Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.28.0/opentelemetry-sdk-1.28.0.jar (6.8 kB at 23 kB/s)
2026-01-22T16:06:59.1770797Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-socks/4.1.60.Final/netty-codec-socks-4.1.60.Final.jar
2026-01-22T16:06:59.1771510Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.28.0-alpha/opentelemetry-semconv-1.28.0-alpha.jar (40 kB at 133 kB/s)
2026-01-22T16:06:59.1772217Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler-proxy/4.1.60.Final/netty-handler-proxy-4.1.60.Final.jar
2026-01-22T16:06:59.1904409Z Progress (1): 0/4.2 MB
2026-01-22T16:06:59.1904851Z Progress (1): 0/4.2 MB
2026-01-22T16:06:59.1905189Z Progress (1): 0/4.2 MB
2026-01-22T16:06:59.1905660Z Progress (2): 0/4.2 MB | 7.7/452 kB
2026-01-22T16:06:59.1906095Z Progress (2): 0/4.2 MB | 16/452 kB 
2026-01-22T16:06:59.1906719Z Progress (2): 0/4.2 MB | 32/452 kB
2026-01-22T16:06:59.1907150Z Progress (2): 0/4.2 MB | 49/452 kB
2026-01-22T16:06:59.1910885Z Progress (2): 0/4.2 MB | 65/452 kB
2026-01-22T16:06:59.1915113Z Progress (2): 0/4.2 MB | 65/452 kB
2026-01-22T16:06:59.1925273Z Progress (2): 0.1/4.2 MB | 65/452 kB
2026-01-22T16:06:59.1925890Z Progress (2): 0.1/4.2 MB | 65/452 kB
2026-01-22T16:06:59.1930143Z Progress (3): 0.1/4.2 MB | 65/452 kB | 7.7/119 kB
2026-01-22T16:06:59.1935525Z Progress (3): 0.1/4.2 MB | 65/452 kB | 16/119 kB 
2026-01-22T16:06:59.1954672Z Progress (3): 0.1/4.2 MB | 65/452 kB | 16/119 kB
2026-01-22T16:06:59.1955367Z Progress (3): 0.1/4.2 MB | 81/452 kB | 16/119 kB
2026-01-22T16:06:59.1955828Z Progress (3): 0.1/4.2 MB | 81/452 kB | 32/119 kB
2026-01-22T16:06:59.1956261Z Progress (3): 0.1/4.2 MB | 98/452 kB | 32/119 kB
2026-01-22T16:06:59.1956694Z Progress (3): 0.1/4.2 MB | 98/452 kB | 32/119 kB
2026-01-22T16:06:59.1957134Z Progress (3): 0.1/4.2 MB | 114/452 kB | 32/119 kB
2026-01-22T16:06:59.1959281Z Progress (3): 0.1/4.2 MB | 114/452 kB | 49/119 kB
2026-01-22T16:06:59.1963144Z Progress (3): 0.1/4.2 MB | 114/452 kB | 49/119 kB
2026-01-22T16:06:59.1966767Z Progress (3): 0.1/4.2 MB | 131/452 kB | 49/119 kB
2026-01-22T16:06:59.2011308Z Progress (3): 0.1/4.2 MB | 131/452 kB | 65/119 kB
2026-01-22T16:06:59.2011764Z Progress (3): 0.1/4.2 MB | 147/452 kB | 65/119 kB
2026-01-22T16:06:59.2012155Z Progress (3): 0.1/4.2 MB | 163/452 kB | 65/119 kB
2026-01-22T16:06:59.2012670Z Progress (3): 0.1/4.2 MB | 180/452 kB | 65/119 kB
2026-01-22T16:06:59.2018888Z Progress (3): 0.1/4.2 MB | 196/452 kB | 65/119 kB
2026-01-22T16:06:59.2019392Z Progress (3): 0.1/4.2 MB | 213/452 kB | 65/119 kB
2026-01-22T16:06:59.2019841Z Progress (3): 0.1/4.2 MB | 229/452 kB | 65/119 kB
2026-01-22T16:06:59.2020281Z Progress (3): 0.1/4.2 MB | 229/452 kB | 65/119 kB
2026-01-22T16:06:59.2020706Z Progress (3): 0.2/4.2 MB | 229/452 kB | 65/119 kB
2026-01-22T16:06:59.2021146Z Progress (4): 0.2/4.2 MB | 229/452 kB | 65/119 kB | 7.7/24 kB
2026-01-22T16:06:59.2021598Z Progress (4): 0.2/4.2 MB | 229/452 kB | 65/119 kB | 7.7/24 kB
2026-01-22T16:06:59.2022047Z Progress (4): 0.2/4.2 MB | 229/452 kB | 65/119 kB | 16/24 kB 
2026-01-22T16:06:59.2022509Z Progress (4): 0.2/4.2 MB | 229/452 kB | 65/119 kB | 24 kB   
2026-01-22T16:06:59.2023089Z Progress (4): 0.2/4.2 MB | 229/452 kB | 65/119 kB | 24 kB
2026-01-22T16:06:59.2023556Z Progress (4): 0.2/4.2 MB | 229/452 kB | 65/119 kB | 24 kB
2026-01-22T16:06:59.2023953Z                                                          
2026-01-22T16:06:59.2024540Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler-proxy/4.1.60.Final/netty-handler-proxy-4.1.60.Final.jar (24 kB at 74 kB/s)
2026-01-22T16:06:59.2025141Z Progress (3): 0.2/4.2 MB | 229/452 kB | 81/119 kB
2026-01-22T16:06:59.2025572Z Progress (3): 0.2/4.2 MB | 229/452 kB | 98/119 kB
2026-01-22T16:06:59.2026013Z Progress (3): 0.2/4.2 MB | 229/452 kB | 114/119 kB
2026-01-22T16:06:59.2026440Z Progress (3): 0.2/4.2 MB | 229/452 kB | 119 kB    
2026-01-22T16:06:59.2026853Z                                               
2026-01-22T16:06:59.2027360Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-socks/4.1.60.Final/netty-codec-socks-4.1.60.Final.jar (119 kB at 368 kB/s)
2026-01-22T16:06:59.2028059Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.60.Final/netty-transport-native-epoll-4.1.60.Final-linux-x86_64.jar
2026-01-22T16:06:59.2078057Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.60.Final/netty-transport-native-kqueue-4.1.60.Final-osx-x86_64.jar
2026-01-22T16:06:59.2078680Z Progress (2): 0.2/4.2 MB | 229/452 kB
2026-01-22T16:06:59.2079178Z Progress (2): 0.2/4.2 MB | 229/452 kB
2026-01-22T16:06:59.2079619Z Progress (2): 0.3/4.2 MB | 229/452 kB
2026-01-22T16:06:59.2080030Z Progress (2): 0.3/4.2 MB | 229/452 kB
2026-01-22T16:06:59.2080455Z Progress (2): 0.3/4.2 MB | 229/452 kB
2026-01-22T16:06:59.2081064Z Progress (2): 0.3/4.2 MB | 229/452 kB
2026-01-22T16:06:59.2081489Z Progress (2): 0.3/4.2 MB | 229/452 kB
2026-01-22T16:06:59.2081897Z Progress (2): 0.3/4.2 MB | 229/452 kB
2026-01-22T16:06:59.2082323Z Progress (2): 0.4/4.2 MB | 229/452 kB
2026-01-22T16:06:59.2082885Z Progress (2): 0.4/4.2 MB | 229/452 kB
2026-01-22T16:06:59.2083322Z Progress (2): 0.4/4.2 MB | 245/452 kB
2026-01-22T16:06:59.2083748Z Progress (2): 0.4/4.2 MB | 262/452 kB
2026-01-22T16:06:59.2084160Z Progress (2): 0.4/4.2 MB | 278/452 kB
2026-01-22T16:06:59.2084581Z Progress (2): 0.4/4.2 MB | 294/452 kB
2026-01-22T16:06:59.2084990Z Progress (2): 0.4/4.2 MB | 311/452 kB
2026-01-22T16:06:59.2085574Z Progress (2): 0.4/4.2 MB | 327/452 kB
2026-01-22T16:06:59.2109985Z Progress (2): 0.4/4.2 MB | 344/452 kB
2026-01-22T16:06:59.2110419Z Progress (3): 0.4/4.2 MB | 344/452 kB | 7.7/9.9 kB
2026-01-22T16:06:59.2124849Z Progress (3): 0.4/4.2 MB | 344/452 kB | 9.9 kB    
2026-01-22T16:06:59.2125333Z                                               
2026-01-22T16:06:59.2125916Z Downloaded from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-netty-utils/2.12.3/async-http-client-netty-utils-2.12.3.jar (9.9 kB at 30 kB/s)
2026-01-22T16:06:59.2126589Z Downloading from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams/2.0.4/netty-reactive-streams-2.0.4.jar
2026-01-22T16:06:59.2127132Z Progress (2): 0.4/4.2 MB | 360/452 kB
2026-01-22T16:06:59.2127557Z Progress (2): 0.4/4.2 MB | 360/452 kB
2026-01-22T16:06:59.2127967Z Progress (2): 0.4/4.2 MB | 360/452 kB
2026-01-22T16:06:59.2128391Z Progress (2): 0.4/4.2 MB | 376/452 kB
2026-01-22T16:06:59.2133599Z Progress (2): 0.4/4.2 MB | 376/452 kB
2026-01-22T16:06:59.2164945Z Progress (2): 0.4/4.2 MB | 393/452 kB
2026-01-22T16:06:59.2165464Z Progress (2): 0.4/4.2 MB | 409/452 kB
2026-01-22T16:06:59.2165934Z Progress (2): 0.4/4.2 MB | 426/452 kB
2026-01-22T16:06:59.2166369Z Progress (2): 0.4/4.2 MB | 442/452 kB
2026-01-22T16:06:59.2166772Z Progress (2): 0.4/4.2 MB | 452 kB    
2026-01-22T16:06:59.2167181Z Progress (2): 0.4/4.2 MB | 452 kB
2026-01-22T16:06:59.2167867Z Progress (2): 0.5/4.2 MB | 452 kB
2026-01-22T16:06:59.2168345Z Progress (2): 0.5/4.2 MB | 452 kB
2026-01-22T16:06:59.2169206Z Progress (2): 0.5/4.2 MB | 452 kB
2026-01-22T16:06:59.2169624Z Progress (2): 0.5/4.2 MB | 452 kB
2026-01-22T16:06:59.2170041Z Progress (3): 0.5/4.2 MB | 452 kB | 4.1/157 kB
2026-01-22T16:06:59.2170469Z Progress (3): 0.5/4.2 MB | 452 kB | 20/157 kB 
2026-01-22T16:06:59.2171570Z                                              
2026-01-22T16:06:59.2172164Z Downloaded from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client/2.12.3/async-http-client-2.12.3.jar (452 kB at 1.3 MB/s)
2026-01-22T16:06:59.2172944Z Progress (2): 0.5/4.2 MB | 29/157 kB
2026-01-22T16:06:59.2173415Z Progress (2): 0.5/4.2 MB | 45/157 kB
2026-01-22T16:06:59.2173840Z Progress (2): 0.5/4.2 MB | 45/157 kB
2026-01-22T16:06:59.2174238Z                                     
2026-01-22T16:06:59.2174739Z Downloading from central: https://repo.maven.apache.org/maven2/com/sun/activation/jakarta.activation/1.2.2/jakarta.activation-1.2.2.jar
2026-01-22T16:06:59.2182237Z Progress (2): 0.5/4.2 MB | 61/157 kB
2026-01-22T16:06:59.2185382Z Progress (2): 0.5/4.2 MB | 78/157 kB
2026-01-22T16:06:59.2185881Z Progress (2): 0.5/4.2 MB | 78/157 kB
2026-01-22T16:06:59.2216419Z Progress (2): 0.5/4.2 MB | 94/157 kB
2026-01-22T16:06:59.2217863Z Progress (2): 0.5/4.2 MB | 111/157 kB
2026-01-22T16:06:59.2218944Z Progress (2): 0.5/4.2 MB | 127/157 kB
2026-01-22T16:06:59.2219445Z Progress (2): 0.6/4.2 MB | 127/157 kB
2026-01-22T16:06:59.2219930Z Progress (2): 0.6/4.2 MB | 143/157 kB
2026-01-22T16:06:59.2220378Z Progress (2): 0.6/4.2 MB | 157 kB    
2026-01-22T16:06:59.2220910Z Progress (2): 0.6/4.2 MB | 157 kB
2026-01-22T16:06:59.2221340Z Progress (2): 0.6/4.2 MB | 157 kB
2026-01-22T16:06:59.2221765Z                                  
2026-01-22T16:06:59.2222343Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.60.Final/netty-transport-native-epoll-4.1.60.Final-linux-x86_64.jar (157 kB at 460 kB/s)
2026-01-22T16:06:59.2223798Z Progress (1): 0.6/4.2 MB
2026-01-22T16:06:59.2226556Z Progress (1): 0.6/4.2 MB
2026-01-22T16:06:59.2227273Z Progress (1): 0.6/4.2 MB
2026-01-22T16:06:59.2228248Z Progress (1): 0.7/4.2 MB
2026-01-22T16:06:59.2233213Z Progress (1): 0.7/4.2 MB
2026-01-22T16:06:59.2233870Z Progress (1): 0.7/4.2 MB
2026-01-22T16:06:59.2234962Z Progress (1): 0.7/4.2 MB
2026-01-22T16:06:59.2235341Z Progress (1): 0.7/4.2 MB
2026-01-22T16:06:59.2235726Z                         
2026-01-22T16:06:59.2236487Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.13.0/selenium-http-4.13.0.jar
2026-01-22T16:06:59.2237710Z Progress (1): 0.7/4.2 MB
2026-01-22T16:06:59.2286507Z Progress (1): 0.8/4.2 MB
2026-01-22T16:06:59.2287050Z Progress (1): 0.8/4.2 MB
2026-01-22T16:06:59.2287494Z Progress (1): 0.8/4.2 MB
2026-01-22T16:06:59.2287929Z Progress (1): 0.8/4.2 MB
2026-01-22T16:06:59.2288336Z Progress (1): 0.8/4.2 MB
2026-01-22T16:06:59.2288741Z Progress (1): 0.8/4.2 MB
2026-01-22T16:06:59.2289135Z Progress (1): 0.9/4.2 MB
2026-01-22T16:06:59.2289544Z Progress (1): 0.9/4.2 MB
2026-01-22T16:06:59.2289947Z Progress (1): 0.9/4.2 MB
2026-01-22T16:06:59.2290348Z Progress (1): 0.9/4.2 MB
2026-01-22T16:06:59.2290745Z Progress (1): 0.9/4.2 MB
2026-01-22T16:06:59.2291131Z Progress (1): 0.9/4.2 MB
2026-01-22T16:06:59.2291538Z Progress (2): 0.9/4.2 MB | 7.7/113 kB
2026-01-22T16:06:59.2291958Z Progress (2): 0.9/4.2 MB | 8.2/113 kB
2026-01-22T16:06:59.2292394Z Progress (2): 0.9/4.2 MB | 25/113 kB 
2026-01-22T16:06:59.2292955Z Progress (2): 0.9/4.2 MB | 41/113 kB
2026-01-22T16:06:59.2293398Z Progress (2): 0.9/4.2 MB | 57/113 kB
2026-01-22T16:06:59.2293818Z Progress (2): 0.9/4.2 MB | 74/113 kB
2026-01-22T16:06:59.2294272Z Progress (2): 0.9/4.2 MB | 90/113 kB
2026-01-22T16:06:59.2294722Z Progress (2): 0.9/4.2 MB | 106/113 kB
2026-01-22T16:06:59.2300158Z Progress (2): 0.9/4.2 MB | 113 kB    
2026-01-22T16:06:59.2314593Z                                  
2026-01-22T16:06:59.2315232Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.60.Final/netty-transport-native-kqueue-4.1.60.Final-osx-x86_64.jar (113 kB at 320 kB/s)
2026-01-22T16:06:59.2315921Z Downloading from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.2/failsafe-3.3.2.jar
2026-01-22T16:06:59.2316413Z Progress (1): 0.9/4.2 MB
2026-01-22T16:06:59.2316819Z Progress (1): 1.0/4.2 MB
2026-01-22T16:06:59.2320125Z Progress (1): 1.0/4.2 MB
2026-01-22T16:06:59.2324920Z Progress (1): 1.0/4.2 MB
2026-01-22T16:06:59.2330093Z Progress (1): 1.0/4.2 MB
2026-01-22T16:06:59.2334794Z Progress (1): 1.0/4.2 MB
2026-01-22T16:06:59.2354926Z Progress (1): 1.0/4.2 MB
2026-01-22T16:06:59.2355395Z Progress (1): 1.1/4.2 MB
2026-01-22T16:06:59.2355821Z Progress (1): 1.1/4.2 MB
2026-01-22T16:06:59.2356225Z Progress (1): 1.1/4.2 MB
2026-01-22T16:06:59.2356915Z Progress (1): 1.1/4.2 MB
2026-01-22T16:06:59.2358048Z Progress (1): 1.1/4.2 MB
2026-01-22T16:06:59.2358537Z Progress (1): 1.1/4.2 MB
2026-01-22T16:06:59.2362429Z Progress (1): 1.2/4.2 MB
2026-01-22T16:06:59.2366952Z Progress (1): 1.2/4.2 MB
2026-01-22T16:06:59.2370607Z Progress (1): 1.2/4.2 MB
2026-01-22T16:06:59.2378098Z Progress (1): 1.2/4.2 MB
2026-01-22T16:06:59.2378845Z Progress (1): 1.2/4.2 MB
2026-01-22T16:06:59.2405155Z Progress (1): 1.2/4.2 MB
2026-01-22T16:06:59.2405642Z Progress (1): 1.3/4.2 MB
2026-01-22T16:06:59.2406058Z Progress (1): 1.3/4.2 MB
2026-01-22T16:06:59.2406467Z Progress (1): 1.3/4.2 MB
2026-01-22T16:06:59.2406884Z Progress (1): 1.3/4.2 MB
2026-01-22T16:06:59.2407291Z Progress (1): 1.3/4.2 MB
2026-01-22T16:06:59.2407697Z Progress (1): 1.3/4.2 MB
2026-01-22T16:06:59.2408096Z Progress (1): 1.4/4.2 MB
2026-01-22T16:06:59.2408504Z Progress (1): 1.4/4.2 MB
2026-01-22T16:06:59.2414251Z Progress (1): 1.4/4.2 MB
2026-01-22T16:06:59.2415398Z Progress (1): 1.4/4.2 MB
2026-01-22T16:06:59.2419427Z Progress (1): 1.4/4.2 MB
2026-01-22T16:06:59.2461664Z Progress (1): 1.4/4.2 MB
2026-01-22T16:06:59.2462146Z Progress (1): 1.5/4.2 MB
2026-01-22T16:06:59.2462581Z Progress (2): 1.5/4.2 MB | 7.7/68 kB
2026-01-22T16:06:59.2463633Z Progress (2): 1.5/4.2 MB | 16/68 kB 
2026-01-22T16:06:59.2464203Z Progress (2): 1.5/4.2 MB | 32/68 kB
2026-01-22T16:06:59.2464867Z Progress (3): 1.5/4.2 MB | 32/68 kB | 7.7/60 kB
2026-01-22T16:06:59.2465694Z Progress (3): 1.5/4.2 MB | 32/68 kB | 16/60 kB 
2026-01-22T16:06:59.2467548Z Progress (3): 1.5/4.2 MB | 49/68 kB | 16/60 kB
2026-01-22T16:06:59.2469152Z Progress (3): 1.5/4.2 MB | 49/68 kB | 32/60 kB
2026-01-22T16:06:59.2469719Z Progress (3): 1.5/4.2 MB | 49/68 kB | 49/60 kB
2026-01-22T16:06:59.2470931Z Progress (3): 1.5/4.2 MB | 65/68 kB | 49/60 kB
2026-01-22T16:06:59.2474609Z Progress (3): 1.5/4.2 MB | 68 kB | 49/60 kB   
2026-01-22T16:06:59.2478803Z Progress (3): 1.5/4.2 MB | 68 kB | 60 kB   
2026-01-22T16:06:59.2484686Z                                         
2026-01-22T16:06:59.2522497Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.13.0/selenium-http-4.13.0.jar (60 kB at 164 kB/s)
2026-01-22T16:06:59.2523271Z Progress (2): 1.5/4.2 MB | 68 kB
2026-01-22T16:06:59.2535284Z Progress (3): 1.5/4.2 MB | 68 kB | 7.7/22 kB
2026-01-22T16:06:59.2565849Z Progress (3): 1.5/4.2 MB | 68 kB | 16/22 kB 
2026-01-22T16:06:59.2566547Z Progress (3): 1.5/4.2 MB | 68 kB | 16/22 kB
2026-01-22T16:06:59.2567207Z Progress (3): 1.5/4.2 MB | 68 kB | 22 kB   
2026-01-22T16:06:59.2572474Z Progress (3): 1.5/4.2 MB | 68 kB | 22 kB
2026-01-22T16:06:59.2574143Z Progress (3): 1.5/4.2 MB | 68 kB | 22 kB
2026-01-22T16:06:59.2578586Z                                         
2026-01-22T16:06:59.2582231Z Downloaded from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams/2.0.4/netty-reactive-streams-2.0.4.jar (22 kB at 59 kB/s)
2026-01-22T16:06:59.2587550Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.13.0/selenium-json-4.13.0.jar
2026-01-22T16:06:59.2588152Z Progress (2): 1.5/4.2 MB | 68 kB
2026-01-22T16:06:59.2591273Z Progress (2): 1.6/4.2 MB | 68 kB
2026-01-22T16:06:59.2593386Z                                 
2026-01-22T16:06:59.2594210Z Downloaded from central: https://repo.maven.apache.org/maven2/com/sun/activation/jakarta.activation/1.2.2/jakarta.activation-1.2.2.jar (68 kB at 185 kB/s)
2026-01-22T16:06:59.2594895Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.13.0/selenium-os-4.13.0.jar
2026-01-22T16:06:59.2595836Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.13.0/selenium-manager-4.13.0.jar
2026-01-22T16:06:59.2600707Z Progress (1): 1.6/4.2 MB
2026-01-22T16:06:59.2603681Z Progress (1): 1.6/4.2 MB
2026-01-22T16:06:59.2614576Z Progress (1): 1.6/4.2 MB
2026-01-22T16:06:59.2623370Z Progress (1): 1.6/4.2 MB
2026-01-22T16:06:59.2625279Z Progress (1): 1.6/4.2 MB
2026-01-22T16:06:59.2631214Z Progress (1): 1.7/4.2 MB
2026-01-22T16:06:59.2631949Z Progress (1): 1.7/4.2 MB
2026-01-22T16:06:59.2636213Z Progress (1): 1.7/4.2 MB
2026-01-22T16:06:59.2636920Z Progress (1): 1.7/4.2 MB
2026-01-22T16:06:59.2637657Z Progress (1): 1.7/4.2 MB
2026-01-22T16:06:59.2638518Z Progress (1): 1.7/4.2 MB
2026-01-22T16:06:59.2639359Z Progress (1): 1.8/4.2 MB
2026-01-22T16:06:59.2640418Z Progress (1): 1.8/4.2 MB
2026-01-22T16:06:59.2643412Z Progress (2): 1.8/4.2 MB | 7.7/144 kB
2026-01-22T16:06:59.2647515Z Progress (2): 1.8/4.2 MB | 8.2/144 kB
2026-01-22T16:06:59.2653423Z Progress (2): 1.8/4.2 MB | 25/144 kB 
2026-01-22T16:06:59.2654865Z Progress (2): 1.8/4.2 MB | 41/144 kB
2026-01-22T16:06:59.2655727Z Progress (2): 1.8/4.2 MB | 57/144 kB
2026-01-22T16:06:59.2656320Z Progress (2): 1.8/4.2 MB | 57/144 kB
2026-01-22T16:06:59.2656902Z Progress (2): 1.8/4.2 MB | 57/144 kB
2026-01-22T16:06:59.2657497Z Progress (2): 1.8/4.2 MB | 57/144 kB
2026-01-22T16:06:59.2658085Z Progress (2): 1.8/4.2 MB | 57/144 kB
2026-01-22T16:06:59.2666457Z Progress (2): 1.9/4.2 MB | 57/144 kB
2026-01-22T16:06:59.2683507Z Progress (2): 1.9/4.2 MB | 57/144 kB
2026-01-22T16:06:59.2685595Z Progress (2): 1.9/4.2 MB | 57/144 kB
2026-01-22T16:06:59.2686488Z Progress (2): 1.9/4.2 MB | 74/144 kB
2026-01-22T16:06:59.2687206Z Progress (2): 1.9/4.2 MB | 90/144 kB
2026-01-22T16:06:59.2704486Z Progress (2): 1.9/4.2 MB | 106/144 kB
2026-01-22T16:06:59.2705267Z Progress (2): 1.9/4.2 MB | 123/144 kB
2026-01-22T16:06:59.2705881Z Progress (2): 1.9/4.2 MB | 139/144 kB
2026-01-22T16:06:59.2706468Z Progress (2): 1.9/4.2 MB | 144 kB    
2026-01-22T16:06:59.2707002Z Progress (2): 1.9/4.2 MB | 144 kB
2026-01-22T16:06:59.2707623Z                                  
2026-01-22T16:06:59.2708341Z Downloaded from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.2/failsafe-3.3.2.jar (144 kB at 379 kB/s)
2026-01-22T16:06:59.2708868Z Progress (1): 1.9/4.2 MB
2026-01-22T16:06:59.2709586Z                         
2026-01-22T16:06:59.2710350Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-exec/1.3/commons-exec-1.3.jar
2026-01-22T16:06:59.2710816Z Progress (1): 1.9/4.2 MB
2026-01-22T16:06:59.2711537Z Progress (1): 1.9/4.2 MB
2026-01-22T16:06:59.2712913Z Progress (1): 2.0/4.2 MB
2026-01-22T16:06:59.2713675Z Progress (1): 2.0/4.2 MB
2026-01-22T16:06:59.2714270Z Progress (1): 2.0/4.2 MB
2026-01-22T16:06:59.2714860Z Progress (1): 2.0/4.2 MB
2026-01-22T16:06:59.2715438Z Progress (1): 2.0/4.2 MB
2026-01-22T16:06:59.2716029Z Progress (1): 2.0/4.2 MB
2026-01-22T16:06:59.2716597Z Progress (1): 2.1/4.2 MB
2026-01-22T16:06:59.2717589Z Progress (1): 2.1/4.2 MB
2026-01-22T16:06:59.2718028Z Progress (1): 2.1/4.2 MB
2026-01-22T16:06:59.2718796Z Progress (1): 2.1/4.2 MB
2026-01-22T16:06:59.2722053Z Progress (2): 2.1/4.2 MB | 7.7/23 kB
2026-01-22T16:06:59.2724714Z Progress (2): 2.1/4.2 MB | 7.7/23 kB
2026-01-22T16:06:59.2726748Z Progress (2): 2.1/4.2 MB | 16/23 kB 
2026-01-22T16:06:59.2727964Z Progress (2): 2.1/4.2 MB | 23 kB   
2026-01-22T16:06:59.2729487Z Progress (2): 2.1/4.2 MB | 23 kB
2026-01-22T16:06:59.2730475Z                                 
2026-01-22T16:06:59.2733219Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.13.0/selenium-os-4.13.0.jar (23 kB at 60 kB/s)
2026-01-22T16:06:59.2735806Z Progress (1): 2.2/4.2 MB
2026-01-22T16:06:59.2738428Z Progress (1): 2.2/4.2 MB
2026-01-22T16:06:59.2740892Z                         
2026-01-22T16:06:59.2743823Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.13.0/selenium-support-4.13.0.jar
2026-01-22T16:06:59.2746025Z Progress (1): 2.2/4.2 MB
2026-01-22T16:06:59.2747248Z Progress (1): 2.2/4.2 MB
2026-01-22T16:06:59.2748310Z Progress (1): 2.2/4.2 MB
2026-01-22T16:06:59.2749324Z Progress (1): 2.2/4.2 MB
2026-01-22T16:06:59.2750275Z Progress (1): 2.3/4.2 MB
2026-01-22T16:06:59.2751460Z Progress (1): 2.3/4.2 MB
2026-01-22T16:06:59.2752587Z Progress (1): 2.3/4.2 MB
2026-01-22T16:06:59.2754070Z Progress (1): 2.3/4.2 MB
2026-01-22T16:06:59.2754385Z Progress (1): 2.3/4.2 MB
2026-01-22T16:06:59.2754701Z Progress (1): 2.3/4.2 MB
2026-01-22T16:06:59.2754986Z Progress (1): 2.4/4.2 MB
2026-01-22T16:06:59.2755279Z Progress (1): 2.4/4.2 MB
2026-01-22T16:06:59.2755583Z Progress (1): 2.4/4.2 MB
2026-01-22T16:06:59.2755859Z Progress (1): 2.4/4.2 MB
2026-01-22T16:06:59.2756187Z Progress (1): 2.4/4.2 MB
2026-01-22T16:06:59.2756482Z Progress (1): 2.4/4.2 MB
2026-01-22T16:06:59.2756777Z Progress (1): 2.5/4.2 MB
2026-01-22T16:06:59.2757064Z Progress (1): 2.5/4.2 MB
2026-01-22T16:06:59.2757382Z Progress (1): 2.5/4.2 MB
2026-01-22T16:06:59.2757672Z Progress (1): 2.5/4.2 MB
2026-01-22T16:06:59.2757953Z Progress (1): 2.5/4.2 MB
2026-01-22T16:06:59.2758235Z Progress (1): 2.5/4.2 MB
2026-01-22T16:06:59.2758539Z Progress (1): 2.6/4.2 MB
2026-01-22T16:06:59.2778401Z Progress (1): 2.6/4.2 MB
2026-01-22T16:06:59.2781686Z Progress (1): 2.6/4.2 MB
2026-01-22T16:06:59.2784964Z Progress (1): 2.6/4.2 MB
2026-01-22T16:06:59.2787966Z Progress (1): 2.6/4.2 MB
2026-01-22T16:06:59.2794425Z Progress (1): 2.6/4.2 MB
2026-01-22T16:06:59.2795522Z Progress (1): 2.7/4.2 MB
2026-01-22T16:06:59.2797331Z Progress (2): 2.7/4.2 MB | 0/8.4 MB
2026-01-22T16:06:59.2798698Z Progress (2): 2.7/4.2 MB | 0/8.4 MB
2026-01-22T16:06:59.2801044Z Progress (2): 2.7/4.2 MB | 0/8.4 MB
2026-01-22T16:06:59.2801904Z Progress (2): 2.7/4.2 MB | 0/8.4 MB
2026-01-22T16:06:59.2804475Z Progress (2): 2.7/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2844982Z Progress (2): 2.7/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2884142Z Progress (2): 2.7/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2885083Z Progress (2): 2.7/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2886070Z Progress (2): 2.7/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2886698Z Progress (2): 2.7/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2887691Z Progress (2): 2.7/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2888279Z Progress (2): 2.7/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2890603Z Progress (2): 2.7/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2890958Z Progress (2): 2.8/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2891275Z Progress (2): 2.8/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2891587Z Progress (2): 2.8/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2891903Z Progress (2): 2.8/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2892234Z Progress (2): 2.8/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2892568Z Progress (3): 2.8/4.2 MB | 0.1/8.4 MB | 7.7/54 kB
2026-01-22T16:06:59.2893086Z Progress (3): 2.8/4.2 MB | 0.1/8.4 MB | 16/54 kB 
2026-01-22T16:06:59.2893525Z Progress (3): 2.8/4.2 MB | 0.1/8.4 MB | 32/54 kB
2026-01-22T16:06:59.2893900Z Progress (3): 2.8/4.2 MB | 0.1/8.4 MB | 49/54 kB
2026-01-22T16:06:59.2894268Z Progress (3): 2.8/4.2 MB | 0.1/8.4 MB | 54 kB   
2026-01-22T16:06:59.2894599Z                                              
2026-01-22T16:06:59.2895022Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-exec/1.3/commons-exec-1.3.jar (54 kB at 135 kB/s)
2026-01-22T16:06:59.2895499Z Progress (3): 2.8/4.2 MB | 0.1/8.4 MB | 7.7/71 kB
2026-01-22T16:06:59.2895867Z Progress (3): 2.8/4.2 MB | 0.1/8.4 MB | 7.7/71 kB
2026-01-22T16:06:59.2896239Z Progress (3): 2.8/4.2 MB | 0.1/8.4 MB | 12/71 kB 
2026-01-22T16:06:59.2896597Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 12/71 kB
2026-01-22T16:06:59.2896968Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 28/71 kB
2026-01-22T16:06:59.2897325Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 44/71 kB
2026-01-22T16:06:59.2897683Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 44/71 kB
2026-01-22T16:06:59.2898037Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 61/71 kB
2026-01-22T16:06:59.2898381Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 61/71 kB
2026-01-22T16:06:59.2898707Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 71 kB   
2026-01-22T16:06:59.2899041Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 71 kB
2026-01-22T16:06:59.2899371Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 71 kB
2026-01-22T16:06:59.2899680Z                                              
2026-01-22T16:06:59.2900105Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.13.0/selenium-json-4.13.0.jar (71 kB at 174 kB/s)
2026-01-22T16:06:59.2900532Z Progress (2): 2.9/4.2 MB | 0.1/8.4 MB
2026-01-22T16:06:59.2900866Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 7.7/192 kB
2026-01-22T16:06:59.2901186Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 16/192 kB 
2026-01-22T16:06:59.2901520Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 32/192 kB
2026-01-22T16:06:59.2901840Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 49/192 kB
2026-01-22T16:06:59.2902166Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 65/192 kB
2026-01-22T16:06:59.2902488Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 81/192 kB
2026-01-22T16:06:59.2903029Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 98/192 kB
2026-01-22T16:06:59.2903390Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2903770Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2904136Z Progress (3): 2.9/4.2 MB | 0.1/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2904510Z Progress (3): 3.0/4.2 MB | 0.1/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2905052Z Progress (3): 3.0/4.2 MB | 0.1/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2905432Z Progress (3): 3.0/4.2 MB | 0.1/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2905798Z Progress (3): 3.0/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2906162Z Progress (3): 3.0/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2906465Z                                                   
2026-01-22T16:06:59.2906836Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar
2026-01-22T16:06:59.2907233Z Progress (3): 3.0/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2907744Z Progress (3): 3.0/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2928375Z Progress (3): 3.0/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2929159Z Progress (3): 3.0/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2930094Z Progress (3): 3.1/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2931910Z Progress (3): 3.1/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2933238Z Progress (3): 3.1/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2934367Z                                                   
2026-01-22T16:06:59.2936927Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.14.0/commons-io-2.14.0.jar
2026-01-22T16:06:59.2939512Z Progress (3): 3.1/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2941843Z Progress (3): 3.1/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2948365Z Progress (3): 3.1/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2950575Z Progress (3): 3.1/4.2 MB | 0.2/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2951769Z Progress (3): 3.1/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2954101Z Progress (3): 3.1/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2955306Z Progress (3): 3.1/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2957453Z Progress (3): 3.1/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2958638Z Progress (3): 3.1/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2960770Z Progress (3): 3.1/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2961960Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2964678Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2965963Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2970860Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2972110Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2973879Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 114/192 kB
2026-01-22T16:06:59.2976257Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 131/192 kB
2026-01-22T16:06:59.3008033Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 147/192 kB
2026-01-22T16:06:59.3012170Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 163/192 kB
2026-01-22T16:06:59.3015555Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 180/192 kB
2026-01-22T16:06:59.3018865Z Progress (3): 3.2/4.2 MB | 0.3/8.4 MB | 192 kB    
2026-01-22T16:06:59.3022624Z Progress (3): 3.3/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3023894Z Progress (3): 3.3/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3024388Z Progress (3): 3.3/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3024933Z Progress (3): 3.3/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3025368Z Progress (3): 3.3/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3025852Z Progress (3): 3.3/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3026304Z Progress (3): 3.4/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3026723Z Progress (3): 3.4/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3027259Z Progress (3): 3.4/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3031867Z Progress (3): 3.4/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3032402Z Progress (3): 3.4/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3033050Z Progress (3): 3.4/4.2 MB | 0.3/8.4 MB | 192 kB
2026-01-22T16:06:59.3033637Z Progress (3): 3.4/4.2 MB | 0.4/8.4 MB | 192 kB
2026-01-22T16:06:59.3034135Z Progress (3): 3.4/4.2 MB | 0.4/8.4 MB | 192 kB
2026-01-22T16:06:59.3037773Z Progress (3): 3.4/4.2 MB | 0.4/8.4 MB | 192 kB
2026-01-22T16:06:59.3038148Z Progress (3): 3.4/4.2 MB | 0.4/8.4 MB | 192 kB
2026-01-22T16:06:59.3038477Z Progress (3): 3.4/4.2 MB | 0.4/8.4 MB | 192 kB
2026-01-22T16:06:59.3038800Z Progress (3): 3.4/4.2 MB | 0.4/8.4 MB | 192 kB
2026-01-22T16:06:59.3039091Z                                               
2026-01-22T16:06:59.3039534Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.13.0/selenium-support-4.13.0.jar (192 kB at 451 kB/s)
2026-01-22T16:06:59.3040044Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.9/slf4j-api-2.0.9.jar
2026-01-22T16:06:59.3070633Z Progress (2): 3.4/4.2 MB | 0.4/8.4 MB
2026-01-22T16:06:59.3070989Z Progress (2): 3.4/4.2 MB | 0.4/8.4 MB
2026-01-22T16:06:59.3072472Z Progress (2): 3.4/4.2 MB | 0.4/8.4 MB
2026-01-22T16:06:59.3072981Z Progress (2): 3.5/4.2 MB | 0.4/8.4 MB
2026-01-22T16:06:59.3073323Z Progress (2): 3.5/4.2 MB | 0.4/8.4 MB
2026-01-22T16:06:59.3073648Z Progress (2): 3.5/4.2 MB | 0.4/8.4 MB
2026-01-22T16:06:59.3073987Z Progress (2): 3.5/4.2 MB | 0.4/8.4 MB
2026-01-22T16:06:59.3074302Z Progress (2): 3.5/4.2 MB | 0.5/8.4 MB
2026-01-22T16:06:59.3074604Z Progress (2): 3.5/4.2 MB | 0.5/8.4 MB
2026-01-22T16:06:59.3074915Z Progress (2): 3.5/4.2 MB | 0.5/8.4 MB
2026-01-22T16:06:59.3093292Z Progress (2): 3.5/4.2 MB | 0.5/8.4 MB
2026-01-22T16:06:59.3093740Z Progress (2): 3.5/4.2 MB | 0.5/8.4 MB
2026-01-22T16:06:59.3094068Z Progress (2): 3.5/4.2 MB | 0.5/8.4 MB
2026-01-22T16:06:59.3094560Z Progress (2): 3.5/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3099016Z Progress (2): 3.5/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3101342Z Progress (2): 3.5/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3104040Z Progress (2): 3.5/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3108263Z Progress (2): 3.5/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3109950Z Progress (2): 3.6/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3116444Z Progress (2): 3.6/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3117119Z Progress (2): 3.6/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3119212Z Progress (2): 3.6/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3119838Z Progress (2): 3.6/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3121814Z Progress (2): 3.6/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3123729Z Progress (2): 3.7/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3126688Z Progress (2): 3.7/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3128514Z Progress (2): 3.7/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3168918Z Progress (2): 3.7/4.2 MB | 0.6/8.4 MB
2026-01-22T16:06:59.3171227Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3174244Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3174939Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3176027Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3177393Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3191299Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3192013Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3196531Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3198654Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3199763Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3200826Z Progress (2): 3.7/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3201948Z Progress (2): 3.8/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3203186Z Progress (2): 3.8/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3203921Z Progress (2): 3.8/4.2 MB | 0.7/8.4 MB
2026-01-22T16:06:59.3207654Z Progress (3): 3.8/4.2 MB | 0.7/8.4 MB | 7.7/494 kB
2026-01-22T16:06:59.3210907Z Progress (3): 3.8/4.2 MB | 0.7/8.4 MB | 16/494 kB 
2026-01-22T16:06:59.3213030Z Progress (3): 3.8/4.2 MB | 0.7/8.4 MB | 32/494 kB
2026-01-22T16:06:59.3216456Z Progress (3): 3.8/4.2 MB | 0.7/8.4 MB | 49/494 kB
2026-01-22T16:06:59.3218063Z Progress (3): 3.8/4.2 MB | 0.7/8.4 MB | 65/494 kB
2026-01-22T16:06:59.3218956Z Progress (3): 3.8/4.2 MB | 0.7/8.4 MB | 81/494 kB
2026-01-22T16:06:59.3220437Z Progress (3): 3.8/4.2 MB | 0.7/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3221464Z Progress (3): 3.8/4.2 MB | 0.8/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3223175Z Progress (3): 3.8/4.2 MB | 0.8/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3224204Z Progress (3): 3.8/4.2 MB | 0.8/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3247583Z Progress (3): 3.8/4.2 MB | 0.8/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3249068Z Progress (3): 3.8/4.2 MB | 0.8/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3249414Z Progress (3): 3.8/4.2 MB | 0.8/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3249749Z Progress (3): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3250072Z Progress (3): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3250537Z Progress (3): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3250867Z Progress (3): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-22T16:06:59.3251211Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 7.7/283 kB
2026-01-22T16:06:59.3251561Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 16/283 kB 
2026-01-22T16:06:59.3251913Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 25/283 kB
2026-01-22T16:06:59.3252261Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 41/283 kB
2026-01-22T16:06:59.3252607Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 57/283 kB
2026-01-22T16:06:59.3253218Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 74/283 kB
2026-01-22T16:06:59.3254014Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 90/283 kB
2026-01-22T16:06:59.3254344Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 106/283 kB
2026-01-22T16:06:59.3254680Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3254969Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3255289Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3255594Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3255900Z Progress (4): 3.8/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3256203Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3256537Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3256875Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3257199Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3257525Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3347919Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB
2026-01-22T16:06:59.3348328Z Progress (5): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB | 7.7/65 kB
2026-01-22T16:06:59.3348686Z Progress (5): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB | 12/65 kB 
2026-01-22T16:06:59.3349077Z Progress (5): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB | 29/65 kB
2026-01-22T16:06:59.3349439Z Progress (5): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB | 45/65 kB
2026-01-22T16:06:59.3349806Z Progress (5): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB | 61/65 kB
2026-01-22T16:06:59.3350140Z Progress (5): 3.9/4.2 MB | 0.9/8.4 MB | 98/494 kB | 123/283 kB | 65 kB   
2026-01-22T16:06:59.3350441Z                                                                       
2026-01-22T16:06:59.3350820Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.9/slf4j-api-2.0.9.jar (65 kB at 142 kB/s)
2026-01-22T16:06:59.3351334Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-java/4.16.1/selenium-java-4.16.1.jar
2026-01-22T16:06:59.3351775Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 114/494 kB | 123/283 kB
2026-01-22T16:06:59.3352131Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 131/494 kB | 123/283 kB
2026-01-22T16:06:59.3352495Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 147/494 kB | 123/283 kB
2026-01-22T16:06:59.3353010Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 163/494 kB | 123/283 kB
2026-01-22T16:06:59.3353367Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 180/494 kB | 123/283 kB
2026-01-22T16:06:59.3353718Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 196/494 kB | 123/283 kB
2026-01-22T16:06:59.3354170Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 213/494 kB | 123/283 kB
2026-01-22T16:06:59.3356593Z Progress (4): 3.9/4.2 MB | 0.9/8.4 MB | 229/494 kB | 123/283 kB
2026-01-22T16:06:59.3360251Z Progress (4): 4.0/4.2 MB | 0.9/8.4 MB | 229/494 kB | 123/283 kB
2026-01-22T16:06:59.3364736Z Progress (4): 4.0/4.2 MB | 0.9/8.4 MB | 229/494 kB | 123/283 kB
2026-01-22T16:06:59.3368979Z Progress (4): 4.0/4.2 MB | 0.9/8.4 MB | 229/494 kB | 123/283 kB
2026-01-22T16:06:59.3374455Z Progress (4): 4.0/4.2 MB | 0.9/8.4 MB | 229/494 kB | 123/283 kB
2026-01-22T16:06:59.3375526Z Progress (4): 4.0/4.2 MB | 0.9/8.4 MB | 229/494 kB | 123/283 kB
2026-01-22T16:06:59.3376384Z Progress (4): 4.0/4.2 MB | 0.9/8.4 MB | 229/494 kB | 123/283 kB
2026-01-22T16:06:59.3379458Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 123/283 kB
2026-01-22T16:06:59.3380101Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 123/283 kB
2026-01-22T16:06:59.3381095Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 123/283 kB
2026-01-22T16:06:59.3381632Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 139/283 kB
2026-01-22T16:06:59.3382088Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 156/283 kB
2026-01-22T16:06:59.3385369Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 172/283 kB
2026-01-22T16:06:59.3388144Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 188/283 kB
2026-01-22T16:06:59.3390995Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 205/283 kB
2026-01-22T16:06:59.3419618Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 221/283 kB
2026-01-22T16:06:59.3421851Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 238/283 kB
2026-01-22T16:06:59.3423136Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 254/283 kB
2026-01-22T16:06:59.3425010Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 270/283 kB
2026-01-22T16:06:59.3426622Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 283 kB    
2026-01-22T16:06:59.3427124Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3427631Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3428177Z Progress (4): 4.1/4.2 MB | 0.9/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3429963Z Progress (4): 4.1/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3430517Z Progress (4): 4.1/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3431049Z Progress (4): 4.1/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3431571Z Progress (4): 4.1/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3432077Z Progress (4): 4.1/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3433510Z Progress (4): 4.1/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3435349Z Progress (4): 4.1/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3438658Z Progress (4): 4.1/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3439369Z Progress (4): 4.1/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3440411Z Progress (4): 4.2/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3443687Z Progress (4): 4.2/4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB
2026-01-22T16:06:59.3444127Z Progress (4): 4.2 MB | 1.0/8.4 MB | 229/494 kB | 283 kB    
2026-01-22T16:06:59.3444432Z                                                        
2026-01-22T16:06:59.3444832Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.5/byte-buddy-1.14.5.jar (4.2 MB at 9.0 MB/s)
2026-01-22T16:06:59.3445259Z Progress (3): 1.0/8.4 MB | 245/494 kB | 283 kB
2026-01-22T16:06:59.3445577Z Progress (3): 1.0/8.4 MB | 262/494 kB | 283 kB
2026-01-22T16:06:59.3445906Z Progress (3): 1.0/8.4 MB | 278/494 kB | 283 kB
2026-01-22T16:06:59.3447974Z Progress (3): 1.0/8.4 MB | 294/494 kB | 283 kB
2026-01-22T16:06:59.3450667Z Progress (3): 1.0/8.4 MB | 311/494 kB | 283 kB
2026-01-22T16:06:59.3453774Z Progress (3): 1.0/8.4 MB | 327/494 kB | 283 kB
2026-01-22T16:06:59.3480841Z Progress (3): 1.0/8.4 MB | 344/494 kB | 283 kB
2026-01-22T16:06:59.3483362Z Progress (3): 1.0/8.4 MB | 360/494 kB | 283 kB
2026-01-22T16:06:59.3486328Z Progress (3): 1.0/8.4 MB | 376/494 kB | 283 kB
2026-01-22T16:06:59.3487529Z Progress (4): 1.0/8.4 MB | 376/494 kB | 283 kB | 545 B
2026-01-22T16:06:59.3489294Z                                                       
2026-01-22T16:06:59.3491033Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-java/4.16.1/selenium-java-4.16.1.jar (545 B at 1.2 kB/s)
2026-01-22T16:06:59.3492458Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chrome-driver/4.16.1/selenium-chrome-driver-4.16.1.jar
2026-01-22T16:06:59.3495393Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar (283 kB at 604 kB/s)
2026-01-22T16:06:59.3497477Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chromium-driver/4.16.1/selenium-chromium-driver-4.16.1.jar
2026-01-22T16:06:59.3499313Z Progress (2): 1.1/8.4 MB | 376/494 kB
2026-01-22T16:06:59.3500450Z Progress (2): 1.1/8.4 MB | 376/494 kB
2026-01-22T16:06:59.3502393Z Progress (2): 1.1/8.4 MB | 376/494 kB
2026-01-22T16:06:59.3506544Z Progress (2): 1.1/8.4 MB | 376/494 kB
2026-01-22T16:06:59.3507257Z Progress (2): 1.1/8.4 MB | 376/494 kB
2026-01-22T16:06:59.3508248Z Progress (2): 1.1/8.4 MB | 376/494 kB
2026-01-22T16:06:59.3508828Z Progress (2): 1.2/8.4 MB | 376/494 kB
2026-01-22T16:06:59.3509721Z                                      
2026-01-22T16:06:59.3510395Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v118/4.16.1/selenium-devtools-v118-4.16.1.jar
2026-01-22T16:06:59.3511434Z Progress (2): 1.2/8.4 MB | 393/494 kB
2026-01-22T16:06:59.3512025Z Progress (2): 1.2/8.4 MB | 409/494 kB
2026-01-22T16:06:59.3513106Z Progress (2): 1.2/8.4 MB | 426/494 kB
2026-01-22T16:06:59.3513734Z Progress (2): 1.2/8.4 MB | 442/494 kB
2026-01-22T16:06:59.3515064Z Progress (2): 1.2/8.4 MB | 458/494 kB
2026-01-22T16:06:59.3515396Z Progress (2): 1.2/8.4 MB | 475/494 kB
2026-01-22T16:06:59.3515690Z Progress (2): 1.2/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3518921Z Progress (2): 1.2/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3521341Z Progress (2): 1.2/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3546112Z Progress (2): 1.2/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3546919Z Progress (2): 1.2/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3548773Z Progress (2): 1.2/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3550170Z Progress (2): 1.3/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3550687Z Progress (2): 1.3/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3551180Z Progress (2): 1.3/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3551612Z Progress (2): 1.3/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3552034Z Progress (2): 1.3/8.4 MB | 491/494 kB
2026-01-22T16:06:59.3553713Z Progress (2): 1.3/8.4 MB | 494 kB    
2026-01-22T16:06:59.3554193Z                                  
2026-01-22T16:06:59.3554677Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.14.0/commons-io-2.14.0.jar (494 kB at 1.0 MB/s)
2026-01-22T16:06:59.3556232Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v119/4.16.1/selenium-devtools-v119-4.16.1.jar
2026-01-22T16:06:59.3556952Z Progress (1): 1.3/8.4 MB
2026-01-22T16:06:59.3559076Z Progress (1): 1.4/8.4 MB
2026-01-22T16:06:59.3559758Z Progress (1): 1.4/8.4 MB
2026-01-22T16:06:59.3562257Z Progress (1): 1.4/8.4 MB
2026-01-22T16:06:59.3562573Z Progress (1): 1.4/8.4 MB
2026-01-22T16:06:59.3563072Z Progress (1): 1.4/8.4 MB
2026-01-22T16:06:59.3563412Z Progress (1): 1.4/8.4 MB
2026-01-22T16:06:59.3563707Z Progress (1): 1.5/8.4 MB
2026-01-22T16:06:59.3564011Z Progress (1): 1.5/8.4 MB
2026-01-22T16:06:59.3564302Z Progress (1): 1.5/8.4 MB
2026-01-22T16:06:59.3564621Z Progress (1): 1.5/8.4 MB
2026-01-22T16:06:59.3564895Z Progress (1): 1.5/8.4 MB
2026-01-22T16:06:59.3568228Z Progress (1): 1.5/8.4 MB
2026-01-22T16:06:59.3569289Z Progress (1): 1.6/8.4 MB
2026-01-22T16:06:59.3571020Z Progress (1): 1.6/8.4 MB
2026-01-22T16:06:59.3573064Z Progress (1): 1.6/8.4 MB
2026-01-22T16:06:59.3576184Z Progress (1): 1.6/8.4 MB
2026-01-22T16:06:59.3579251Z Progress (1): 1.6/8.4 MB
2026-01-22T16:06:59.3582032Z Progress (1): 1.6/8.4 MB
2026-01-22T16:06:59.3605749Z Progress (1): 1.7/8.4 MB
2026-01-22T16:06:59.3606391Z Progress (1): 1.7/8.4 MB
2026-01-22T16:06:59.3609075Z Progress (1): 1.7/8.4 MB
2026-01-22T16:06:59.3609781Z Progress (1): 1.7/8.4 MB
2026-01-22T16:06:59.3611973Z Progress (1): 1.7/8.4 MB
2026-01-22T16:06:59.3613908Z Progress (1): 1.7/8.4 MB
2026-01-22T16:06:59.3615186Z Progress (1): 1.8/8.4 MB
2026-01-22T16:06:59.3615953Z Progress (1): 1.8/8.4 MB
2026-01-22T16:06:59.3617006Z Progress (1): 1.8/8.4 MB
2026-01-22T16:06:59.3618981Z Progress (1): 1.8/8.4 MB
2026-01-22T16:06:59.3620024Z Progress (1): 1.8/8.4 MB
2026-01-22T16:06:59.3621488Z Progress (1): 1.8/8.4 MB
2026-01-22T16:06:59.3623653Z Progress (1): 1.9/8.4 MB
2026-01-22T16:06:59.3624280Z Progress (2): 1.9/8.4 MB | 3.3/15 kB
2026-01-22T16:06:59.3626287Z Progress (2): 1.9/8.4 MB | 15 kB    
2026-01-22T16:06:59.3627785Z                                 
2026-01-22T16:06:59.3630261Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chrome-driver/4.16.1/selenium-chrome-driver-4.16.1.jar (15 kB at 31 kB/s)
2026-01-22T16:06:59.3630746Z Progress (1): 1.9/8.4 MB
2026-01-22T16:06:59.3631050Z Progress (1): 1.9/8.4 MB
2026-01-22T16:06:59.3631350Z Progress (1): 1.9/8.4 MB
2026-01-22T16:06:59.3631649Z Progress (1): 1.9/8.4 MB
2026-01-22T16:06:59.3633682Z Progress (1): 1.9/8.4 MB
2026-01-22T16:06:59.3635394Z Progress (1): 1.9/8.4 MB
2026-01-22T16:06:59.3637319Z Progress (1): 2.0/8.4 MB
2026-01-22T16:06:59.3639980Z Progress (1): 2.0/8.4 MB
2026-01-22T16:06:59.3643457Z Progress (1): 2.0/8.4 MB
2026-01-22T16:06:59.3665970Z Progress (1): 2.0/8.4 MB
2026-01-22T16:06:59.3667678Z                         
2026-01-22T16:06:59.3668759Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v120/4.16.1/selenium-devtools-v120-4.16.1.jar
2026-01-22T16:06:59.3670434Z Progress (1): 2.0/8.4 MB
2026-01-22T16:06:59.3672373Z Progress (1): 2.0/8.4 MB
2026-01-22T16:06:59.3673276Z Progress (1): 2.1/8.4 MB
2026-01-22T16:06:59.3675124Z Progress (1): 2.1/8.4 MB
2026-01-22T16:06:59.3678115Z Progress (1): 2.1/8.4 MB
2026-01-22T16:06:59.3680654Z Progress (1): 2.1/8.4 MB
2026-01-22T16:06:59.3682637Z Progress (1): 2.1/8.4 MB
2026-01-22T16:06:59.3683576Z Progress (1): 2.1/8.4 MB
2026-01-22T16:06:59.3685666Z Progress (1): 2.2/8.4 MB
2026-01-22T16:06:59.3686208Z Progress (1): 2.2/8.4 MB
2026-01-22T16:06:59.3686623Z Progress (1): 2.2/8.4 MB
2026-01-22T16:06:59.3687038Z Progress (1): 2.2/8.4 MB
2026-01-22T16:06:59.3688410Z Progress (1): 2.2/8.4 MB
2026-01-22T16:06:59.3688960Z Progress (1): 2.2/8.4 MB
2026-01-22T16:06:59.3690759Z Progress (1): 2.3/8.4 MB
2026-01-22T16:06:59.3691417Z Progress (1): 2.3/8.4 MB
2026-01-22T16:06:59.3693966Z Progress (1): 2.3/8.4 MB
2026-01-22T16:06:59.3694284Z Progress (1): 2.3/8.4 MB
2026-01-22T16:06:59.3694588Z Progress (1): 2.3/8.4 MB
2026-01-22T16:06:59.3718422Z Progress (1): 2.3/8.4 MB
2026-01-22T16:06:59.3718784Z Progress (1): 2.4/8.4 MB
2026-01-22T16:06:59.3719068Z Progress (1): 2.4/8.4 MB
2026-01-22T16:06:59.3721434Z Progress (1): 2.4/8.4 MB
2026-01-22T16:06:59.3721830Z Progress (1): 2.4/8.4 MB
2026-01-22T16:06:59.3722130Z Progress (1): 2.4/8.4 MB
2026-01-22T16:06:59.3722441Z Progress (1): 2.4/8.4 MB
2026-01-22T16:06:59.3722930Z Progress (1): 2.5/8.4 MB
2026-01-22T16:06:59.3723260Z Progress (1): 2.5/8.4 MB
2026-01-22T16:06:59.3730412Z Progress (1): 2.5/8.4 MB
2026-01-22T16:06:59.3730801Z Progress (1): 2.5/8.4 MB
2026-01-22T16:06:59.3753362Z Progress (1): 2.5/8.4 MB
2026-01-22T16:06:59.3760388Z Progress (2): 2.5/8.4 MB | 7.7/37 kB
2026-01-22T16:06:59.3762927Z Progress (2): 2.5/8.4 MB | 16/37 kB 
2026-01-22T16:06:59.3763592Z Progress (2): 2.5/8.4 MB | 32/37 kB
2026-01-22T16:06:59.3764611Z Progress (2): 2.5/8.4 MB | 37 kB   
2026-01-22T16:06:59.3765376Z Progress (3): 2.5/8.4 MB | 37 kB | 0/1.4 MB
2026-01-22T16:06:59.3767359Z Progress (3): 2.5/8.4 MB | 37 kB | 0/1.4 MB
2026-01-22T16:06:59.3769006Z Progress (3): 2.5/8.4 MB | 37 kB | 0/1.4 MB
2026-01-22T16:06:59.3771620Z Progress (3): 2.5/8.4 MB | 37 kB | 0/1.4 MB
2026-01-22T16:06:59.3772277Z Progress (3): 2.5/8.4 MB | 37 kB | 0.1/1.4 MB
2026-01-22T16:06:59.3773406Z Progress (3): 2.5/8.4 MB | 37 kB | 0.1/1.4 MB
2026-01-22T16:06:59.3774118Z Progress (3): 2.5/8.4 MB | 37 kB | 0.1/1.4 MB
2026-01-22T16:06:59.3775036Z Progress (3): 2.5/8.4 MB | 37 kB | 0.1/1.4 MB
2026-01-22T16:06:59.3775697Z Progress (3): 2.5/8.4 MB | 37 kB | 0.1/1.4 MB
2026-01-22T16:06:59.3776922Z Progress (3): 2.5/8.4 MB | 37 kB | 0.1/1.4 MB
2026-01-22T16:06:59.3777556Z                                              
2026-01-22T16:06:59.3779697Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chromium-driver/4.16.1/selenium-chromium-driver-4.16.1.jar (37 kB at 74 kB/s)
2026-01-22T16:06:59.3780807Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v85/4.16.1/selenium-devtools-v85-4.16.1.jar
2026-01-22T16:06:59.3783840Z Progress (2): 2.5/8.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3784490Z Progress (2): 2.6/8.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3785533Z Progress (2): 2.6/8.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3786244Z Progress (2): 2.6/8.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3787242Z Progress (2): 2.6/8.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3793735Z Progress (2): 2.6/8.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3911620Z Progress (3): 2.6/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-22T16:06:59.3913396Z Progress (3): 2.6/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-22T16:06:59.3917973Z Progress (3): 2.6/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-22T16:06:59.3920405Z Progress (3): 2.6/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-22T16:06:59.3921577Z Progress (3): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3924749Z Progress (3): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3927317Z Progress (4): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-22T16:06:59.3928513Z Progress (4): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-22T16:06:59.3930697Z Progress (4): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-22T16:06:59.3932387Z Progress (4): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-22T16:06:59.3937019Z Progress (4): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3938153Z Progress (4): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3939265Z Progress (4): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3941274Z Progress (4): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3942582Z Progress (4): 2.6/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3943523Z Progress (4): 2.6/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3946899Z Progress (4): 2.6/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3951279Z Progress (4): 2.6/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3955736Z Progress (4): 2.6/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3959686Z Progress (4): 2.6/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3960722Z Progress (4): 2.6/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3961416Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3962363Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3963148Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3964180Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3964680Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3965152Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3965598Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3966188Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3966641Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3967109Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3969825Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3970216Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3970544Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3970897Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3971377Z Progress (4): 2.6/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3971732Z Progress (4): 2.7/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3972067Z Progress (4): 2.7/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3972422Z Progress (4): 2.7/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3972946Z Progress (4): 2.7/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3973302Z Progress (4): 2.7/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3973650Z Progress (4): 2.7/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3973995Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3974323Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-22T16:06:59.3974676Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.2/1.4 MB
2026-01-22T16:06:59.3975022Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.2/1.4 MB
2026-01-22T16:06:59.3975376Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.2/1.4 MB
2026-01-22T16:06:59.3975725Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.2/1.4 MB
2026-01-22T16:06:59.3976060Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.2/1.4 MB
2026-01-22T16:06:59.3976410Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.2/1.4 MB
2026-01-22T16:06:59.3976773Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3977127Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3977484Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3977960Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3978379Z Progress (4): 2.8/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3978737Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3979080Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3979446Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3979775Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3980136Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3980482Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3980841Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3981190Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3981538Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3981875Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3982218Z Progress (4): 2.8/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3982570Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3983083Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3983453Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3983793Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3984135Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3984495Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3985089Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3985443Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3985796Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3986147Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.3986478Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.4019725Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.4020573Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.4025713Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.4026495Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.4028878Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-22T16:06:59.4033616Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4034473Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4036643Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4072937Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4075464Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4076633Z Progress (4): 2.9/8.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4079131Z Progress (4): 2.9/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4083419Z Progress (4): 2.9/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4084625Z Progress (4): 2.9/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4087049Z Progress (4): 2.9/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4089602Z Progress (4): 2.9/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4092219Z Progress (4): 2.9/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4094911Z Progress (4): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4098532Z Progress (4): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4099720Z Progress (4): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB
2026-01-22T16:06:59.4103576Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0/1.0 MB
2026-01-22T16:06:59.4104879Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0/1.0 MB
2026-01-22T16:06:59.4107088Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0/1.0 MB
2026-01-22T16:06:59.4109376Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0/1.0 MB
2026-01-22T16:06:59.4111338Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4113817Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4115853Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4118145Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4121088Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4122264Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4124468Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4128278Z Progress (5): 2.9/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4128658Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4129040Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4129428Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4129791Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4130160Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4130610Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4130958Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4131337Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4131699Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4132065Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4132421Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4133059Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4133438Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4133809Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4134167Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4134542Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4134891Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4135266Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4135634Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4136004Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4136391Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4136733Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4137090Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4137461Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4137839Z Progress (5): 3.0/8.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4138202Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4138564Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4138912Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4139293Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4139655Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4140026Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.1/1.0 MB
2026-01-22T16:06:59.4140394Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.2/1.0 MB
2026-01-22T16:06:59.4140747Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.2/1.0 MB
2026-01-22T16:06:59.4141120Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.2/1.0 MB
2026-01-22T16:06:59.4141509Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.2/1.0 MB
2026-01-22T16:06:59.4141901Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.2/1.0 MB
2026-01-22T16:06:59.4142271Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.2/1.0 MB
2026-01-22T16:06:59.4142642Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4182350Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4183100Z Progress (5): 3.0/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4188046Z Progress (5): 3.1/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4190197Z Progress (5): 3.1/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4192672Z Progress (5): 3.1/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4194799Z Progress (5): 3.1/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4197305Z Progress (5): 3.1/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4199344Z Progress (5): 3.1/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4201586Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4205990Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4208331Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4212597Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4216481Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4218444Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4220949Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4221564Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4222047Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4222536Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4223202Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4223693Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4224163Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4224687Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4225223Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4225791Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4226240Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.6/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4226756Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4227299Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4227772Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4228222Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4228716Z Progress (5): 3.2/8.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4229180Z Progress (5): 3.2/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4229650Z Progress (5): 3.2/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4230217Z Progress (5): 3.2/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4235247Z Progress (5): 3.2/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4235969Z Progress (5): 3.2/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4237460Z Progress (5): 3.2/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4237852Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4238205Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4238567Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4238948Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4239315Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.3/1.0 MB
2026-01-22T16:06:59.4239688Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4240043Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4240390Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4240883Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4241270Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4241647Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4242010Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4242395Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4242915Z Progress (5): 3.2/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4263977Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4276498Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4281050Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4283164Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4285637Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4287608Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4289941Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4290621Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4294294Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4295772Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.7/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4297423Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4298061Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4300325Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4300991Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4301965Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4302612Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4306565Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4307263Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4308911Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4309597Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4310575Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4311167Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4312144Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4312945Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4313963Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4314579Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4315635Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4316257Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4317211Z Progress (5): 3.3/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4317860Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4318860Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4319465Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4320423Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4321127Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4322112Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.4/1.0 MB
2026-01-22T16:06:59.4350845Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.0 MB
2026-01-22T16:06:59.4352044Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.0 MB
2026-01-22T16:06:59.4353296Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.0 MB
2026-01-22T16:06:59.4355737Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.0 MB
2026-01-22T16:06:59.4356967Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.0 MB
2026-01-22T16:06:59.4358908Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.0 MB
2026-01-22T16:06:59.4366990Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4367542Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4368058Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4368538Z Progress (5): 3.3/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4369031Z Progress (5): 3.4/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4369489Z Progress (5): 3.4/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4369973Z Progress (5): 3.4/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4370491Z Progress (5): 3.4/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4370986Z Progress (5): 3.4/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4371429Z Progress (5): 3.4/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4371911Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4372485Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4374156Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4374547Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4374910Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4375282Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4375629Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4376011Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4376378Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4376746Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4377114Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4377466Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4377821Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4421571Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4424080Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4424510Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4424910Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4425361Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4425733Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4426096Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4426450Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4426983Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4427353Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4427715Z Progress (5): 3.5/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4428085Z Progress (5): 3.5/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4428433Z Progress (5): 3.5/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4428911Z Progress (5): 3.5/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4429283Z Progress (5): 3.5/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4429641Z Progress (5): 3.5/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4430013Z Progress (5): 3.5/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4430367Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4430747Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4431116Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4431484Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4431851Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4432199Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4432560Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.0 MB
2026-01-22T16:06:59.4433116Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.0 MB
2026-01-22T16:06:59.4433477Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.0 MB
2026-01-22T16:06:59.4433851Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.0 MB
2026-01-22T16:06:59.4434226Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.0 MB
2026-01-22T16:06:59.4434571Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.0 MB
2026-01-22T16:06:59.4435151Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.0 MB
2026-01-22T16:06:59.4474036Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4475172Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4475849Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4476883Z Progress (5): 3.5/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4477498Z Progress (5): 3.6/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4479981Z Progress (5): 3.6/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4480665Z Progress (5): 3.6/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4483209Z Progress (5): 3.6/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4483929Z Progress (5): 3.6/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4486354Z Progress (5): 3.6/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4487037Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4488000Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4488619Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4489588Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4490195Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4491156Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4491921Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4493075Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4493730Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4494702Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4495355Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4499106Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4499973Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4502282Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4503182Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4504199Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4504855Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4507289Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4508041Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4510315Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4512122Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4513094Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4515423Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4548228Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4549396Z Progress (5): 3.7/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4550422Z Progress (5): 3.7/8.4 MB | 1.3/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4551463Z Progress (5): 3.7/8.4 MB | 1.3/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4552488Z Progress (5): 3.7/8.4 MB | 1.3/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4553959Z Progress (5): 3.7/8.4 MB | 1.3/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4554842Z Progress (5): 3.7/8.4 MB | 1.3/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4564704Z Progress (5): 3.7/8.4 MB | 1.3/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4565473Z Progress (5): 3.7/8.4 MB | 1.3/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4566487Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4567127Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4568085Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4568714Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4569716Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4570220Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.8/1.0 MB
2026-01-22T16:06:59.4570716Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4571184Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4571655Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4572117Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4572588Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4573261Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4573740Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4574288Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4574777Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4575287Z Progress (5): 3.7/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4575761Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4579061Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4580667Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4581185Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4581546Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4581922Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4582274Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.1/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4582652Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4583227Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4583601Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4583963Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4584340Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4584689Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4585055Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4585433Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4585795Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4586173Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4613646Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4645516Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4646659Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4647330Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4648354Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4649031Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4650185Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4650972Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4652228Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4653196Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4654397Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4655097Z Progress (5): 3.8/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4656217Z Progress (5): 3.8/8.4 MB | 1.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB    
2026-01-22T16:06:59.4656935Z                                                                         
2026-01-22T16:06:59.4657995Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v119/4.16.1/selenium-devtools-v119-4.16.1.jar (1.4 MB at 2.4 MB/s)
2026-01-22T16:06:59.4658769Z Progress (4): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4663396Z Progress (4): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 0.9/1.0 MB
2026-01-22T16:06:59.4664055Z Progress (4): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 1.0/1.0 MB
2026-01-22T16:06:59.4684622Z Progress (4): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 1.0/1.0 MB
2026-01-22T16:06:59.4685234Z Progress (4): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 1.0/1.0 MB
2026-01-22T16:06:59.4686160Z Progress (4): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB | 1.0 MB    
2026-01-22T16:06:59.4686836Z                                                            
2026-01-22T16:06:59.4688007Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v85/4.16.1/selenium-devtools-v85-4.16.1.jar (1.0 MB at 1.7 MB/s)
2026-01-22T16:06:59.4689156Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-edge-driver/4.16.1/selenium-edge-driver-4.16.1.jar
2026-01-22T16:06:59.4693471Z Progress (3): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4695351Z Progress (3): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4697457Z Progress (3): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4698972Z Progress (3): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4700088Z Progress (3): 3.8/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4701640Z Progress (3): 3.9/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4703949Z Progress (3): 3.9/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4705516Z Progress (3): 3.9/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4706551Z Progress (3): 3.9/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4708021Z Progress (3): 3.9/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4710272Z Progress (3): 3.9/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4710969Z Progress (3): 3.9/8.4 MB | 1.3/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4711946Z Progress (3): 3.9/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4713885Z Progress (3): 3.9/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4716552Z Progress (3): 3.9/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4717278Z Progress (3): 3.9/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4718370Z Progress (3): 3.9/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4719023Z Progress (3): 4.0/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4721089Z Progress (3): 4.0/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4721770Z Progress (3): 4.0/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4722869Z Progress (3): 4.0/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB
2026-01-22T16:06:59.4724414Z Progress (3): 4.0/8.4 MB | 1.4/1.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4725642Z Progress (3): 4.0/8.4 MB | 1.4/1.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4727182Z Progress (3): 4.0/8.4 MB | 1.4/1.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4729081Z Progress (3): 4.0/8.4 MB | 1.4/1.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4730523Z Progress (3): 4.0/8.4 MB | 1.4/1.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4731549Z Progress (3): 4.0/8.4 MB | 1.4/1.4 MB | 1.4 MB    
2026-01-22T16:06:59.4733264Z                                               
2026-01-22T16:06:59.4735364Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v120/4.16.1/selenium-devtools-v120-4.16.1.jar (1.4 MB at 2.5 MB/s)
2026-01-22T16:06:59.4737490Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-firefox-driver/4.16.1/selenium-firefox-driver-4.16.1.jar
2026-01-22T16:06:59.4738772Z Progress (2): 4.0/8.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4739669Z Progress (2): 4.0/8.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4742116Z Progress (2): 4.0/8.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4745820Z Progress (2): 4.0/8.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4748293Z Progress (2): 4.1/8.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4777710Z Progress (2): 4.1/8.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4778065Z Progress (2): 4.1/8.4 MB | 1.4/1.4 MB
2026-01-22T16:06:59.4778363Z                                      
2026-01-22T16:06:59.4778793Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-ie-driver/4.16.1/selenium-ie-driver-4.16.1.jar
2026-01-22T16:06:59.4779369Z Progress (2): 4.1/8.4 MB | 1.4 MB
2026-01-22T16:06:59.4779685Z Progress (2): 4.1/8.4 MB | 1.4 MB
2026-01-22T16:06:59.4779998Z Progress (2): 4.1/8.4 MB | 1.4 MB
2026-01-22T16:06:59.4780299Z Progress (2): 4.1/8.4 MB | 1.4 MB
2026-01-22T16:06:59.4780585Z Progress (2): 4.2/8.4 MB | 1.4 MB
2026-01-22T16:06:59.4780902Z Progress (2): 4.2/8.4 MB | 1.4 MB
2026-01-22T16:06:59.4781209Z Progress (2): 4.2/8.4 MB | 1.4 MB
2026-01-22T16:06:59.4781513Z Progress (2): 4.2/8.4 MB | 1.4 MB
2026-01-22T16:06:59.4781810Z Progress (2): 4.2/8.4 MB | 1.4 MB
2026-01-22T16:06:59.4782124Z Progress (2): 4.2/8.4 MB | 1.4 MB
2026-01-22T16:06:59.4782480Z                                  
2026-01-22T16:06:59.4783076Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v118/4.16.1/selenium-devtools-v118-4.16.1.jar (1.4 MB at 2.4 MB/s)
2026-01-22T16:06:59.4783683Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-safari-driver/4.16.1/selenium-safari-driver-4.16.1.jar
2026-01-22T16:06:59.4784118Z Progress (1): 4.3/8.4 MB
2026-01-22T16:06:59.4784429Z Progress (1): 4.3/8.4 MB
2026-01-22T16:06:59.4784736Z Progress (1): 4.3/8.4 MB
2026-01-22T16:06:59.4785044Z Progress (1): 4.3/8.4 MB
2026-01-22T16:06:59.4785323Z Progress (1): 4.3/8.4 MB
2026-01-22T16:06:59.4785605Z Progress (1): 4.3/8.4 MB
2026-01-22T16:06:59.4785893Z Progress (1): 4.4/8.4 MB
2026-01-22T16:06:59.4786205Z Progress (1): 4.4/8.4 MB
2026-01-22T16:06:59.4786492Z Progress (1): 4.4/8.4 MB
2026-01-22T16:06:59.4786785Z Progress (1): 4.4/8.4 MB
2026-01-22T16:06:59.4787080Z Progress (1): 4.4/8.4 MB
2026-01-22T16:06:59.4787375Z Progress (1): 4.4/8.4 MB
2026-01-22T16:06:59.4787648Z Progress (1): 4.5/8.4 MB
2026-01-22T16:06:59.4787947Z Progress (1): 4.5/8.4 MB
2026-01-22T16:06:59.4788252Z Progress (1): 4.5/8.4 MB
2026-01-22T16:06:59.4788537Z Progress (1): 4.5/8.4 MB
2026-01-22T16:06:59.4788829Z Progress (1): 4.5/8.4 MB
2026-01-22T16:06:59.4789121Z Progress (1): 4.5/8.4 MB
2026-01-22T16:06:59.4789416Z Progress (1): 4.6/8.4 MB
2026-01-22T16:06:59.4789691Z Progress (1): 4.6/8.4 MB
2026-01-22T16:06:59.4789996Z Progress (1): 4.6/8.4 MB
2026-01-22T16:06:59.4790343Z Progress (1): 4.6/8.4 MB
2026-01-22T16:06:59.4790645Z Progress (1): 4.6/8.4 MB
2026-01-22T16:06:59.4790930Z Progress (1): 4.6/8.4 MB
2026-01-22T16:06:59.4798940Z Progress (1): 4.7/8.4 MB
2026-01-22T16:06:59.4799258Z Progress (1): 4.7/8.4 MB
2026-01-22T16:06:59.4799561Z Progress (1): 4.7/8.4 MB
2026-01-22T16:06:59.4799880Z Progress (1): 4.7/8.4 MB
2026-01-22T16:06:59.4800167Z Progress (1): 4.7/8.4 MB
2026-01-22T16:06:59.4800441Z Progress (1): 4.7/8.4 MB
2026-01-22T16:06:59.4806221Z Progress (1): 4.8/8.4 MB
2026-01-22T16:06:59.4806580Z Progress (1): 4.8/8.4 MB
2026-01-22T16:06:59.4806872Z Progress (1): 4.8/8.4 MB
2026-01-22T16:06:59.4823305Z Progress (1): 4.8/8.4 MB
2026-01-22T16:06:59.4826299Z Progress (1): 4.8/8.4 MB
2026-01-22T16:06:59.4827234Z Progress (1): 4.8/8.4 MB
2026-01-22T16:06:59.4830814Z Progress (1): 4.8/8.4 MB
2026-01-22T16:06:59.4833057Z Progress (1): 4.9/8.4 MB
2026-01-22T16:06:59.4835139Z Progress (1): 4.9/8.4 MB
2026-01-22T16:06:59.4837208Z Progress (1): 4.9/8.4 MB
2026-01-22T16:06:59.4839351Z Progress (1): 4.9/8.4 MB
2026-01-22T16:06:59.4840503Z Progress (1): 4.9/8.4 MB
2026-01-22T16:06:59.4842672Z Progress (1): 4.9/8.4 MB
2026-01-22T16:06:59.4844979Z Progress (1): 5.0/8.4 MB
2026-01-22T16:06:59.4847176Z Progress (1): 5.0/8.4 MB
2026-01-22T16:06:59.4849254Z Progress (1): 5.0/8.4 MB
2026-01-22T16:06:59.4851301Z Progress (1): 5.0/8.4 MB
2026-01-22T16:06:59.4852485Z Progress (1): 5.0/8.4 MB
2026-01-22T16:06:59.4854855Z Progress (1): 5.0/8.4 MB
2026-01-22T16:06:59.4857075Z Progress (1): 5.1/8.4 MB
2026-01-22T16:06:59.4857842Z Progress (1): 5.1/8.4 MB
2026-01-22T16:06:59.4859030Z Progress (1): 5.1/8.4 MB
2026-01-22T16:06:59.4863320Z Progress (1): 5.1/8.4 MB
2026-01-22T16:06:59.4864803Z Progress (1): 5.1/8.4 MB
2026-01-22T16:06:59.4865580Z Progress (1): 5.1/8.4 MB
2026-01-22T16:06:59.4866914Z Progress (1): 5.2/8.4 MB
2026-01-22T16:06:59.4867955Z Progress (1): 5.2/8.4 MB
2026-01-22T16:06:59.4868371Z Progress (1): 5.2/8.4 MB
2026-01-22T16:06:59.4868771Z Progress (2): 5.2/8.4 MB | 7.7/15 kB
2026-01-22T16:06:59.4897094Z Progress (2): 5.2/8.4 MB | 15 kB    
2026-01-22T16:06:59.4900113Z                                 
2026-01-22T16:06:59.4900756Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-edge-driver/4.16.1/selenium-edge-driver-4.16.1.jar (15 kB at 25 kB/s)
2026-01-22T16:06:59.4901524Z Downloading from central: https://repo.maven.apache.org/maven2/net/masterthought/cucumber-reporting/5.8.3/cucumber-reporting-5.8.3.jar
2026-01-22T16:06:59.4902253Z Progress (1): 5.2/8.4 MB
2026-01-22T16:06:59.4902710Z Progress (1): 5.2/8.4 MB
2026-01-22T16:06:59.4905644Z Progress (1): 5.2/8.4 MB
2026-01-22T16:06:59.4905993Z Progress (1): 5.3/8.4 MB
2026-01-22T16:06:59.4906338Z Progress (1): 5.3/8.4 MB
2026-01-22T16:06:59.4906654Z Progress (1): 5.3/8.4 MB
2026-01-22T16:06:59.4906957Z Progress (1): 5.3/8.4 MB
2026-01-22T16:06:59.4907244Z Progress (1): 5.3/8.4 MB
2026-01-22T16:06:59.4907562Z Progress (1): 5.3/8.4 MB
2026-01-22T16:06:59.4907871Z Progress (2): 5.3/8.4 MB | 7.7/17 kB
2026-01-22T16:06:59.4908192Z Progress (2): 5.3/8.4 MB | 12/17 kB 
2026-01-22T16:06:59.4908495Z Progress (2): 5.3/8.4 MB | 17 kB   
2026-01-22T16:06:59.4908795Z                                 
2026-01-22T16:06:59.4909186Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-ie-driver/4.16.1/selenium-ie-driver-4.16.1.jar (17 kB at 28 kB/s)
2026-01-22T16:06:59.4916166Z Progress (2): 5.3/8.4 MB | 7.7/83 kB
2026-01-22T16:06:59.4916500Z Progress (2): 5.3/8.4 MB | 16/83 kB 
2026-01-22T16:06:59.4916971Z Progress (2): 5.3/8.4 MB | 32/83 kB
2026-01-22T16:06:59.4917294Z Progress (2): 5.3/8.4 MB | 48/83 kB
2026-01-22T16:06:59.4917583Z                                    
2026-01-22T16:06:59.4918005Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.18.0/jackson-datatype-jsr310-2.18.0.jar
2026-01-22T16:06:59.4921153Z Progress (2): 5.3/8.4 MB | 65/83 kB
2026-01-22T16:06:59.4924934Z Progress (2): 5.3/8.4 MB | 81/83 kB
2026-01-22T16:06:59.4926830Z Progress (2): 5.3/8.4 MB | 83 kB   
2026-01-22T16:06:59.4928078Z                                 
2026-01-22T16:06:59.4929114Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-firefox-driver/4.16.1/selenium-firefox-driver-4.16.1.jar (83 kB at 136 kB/s)
2026-01-22T16:06:59.4957740Z Progress (1): 5.4/8.4 MB
2026-01-22T16:06:59.4958404Z Progress (1): 5.4/8.4 MB
2026-01-22T16:06:59.4960519Z Progress (1): 5.4/8.4 MB
2026-01-22T16:06:59.4961267Z Progress (1): 5.4/8.4 MB
2026-01-22T16:06:59.4962244Z                         
2026-01-22T16:06:59.4963151Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.jar
2026-01-22T16:06:59.4964320Z Progress (1): 5.4/8.4 MB
2026-01-22T16:06:59.4965137Z Progress (1): 5.4/8.4 MB
2026-01-22T16:06:59.4967894Z Progress (1): 5.5/8.4 MB
2026-01-22T16:06:59.4968605Z Progress (1): 5.5/8.4 MB
2026-01-22T16:06:59.4971659Z Progress (1): 5.5/8.4 MB
2026-01-22T16:06:59.4972338Z Progress (1): 5.5/8.4 MB
2026-01-22T16:06:59.4973423Z Progress (1): 5.5/8.4 MB
2026-01-22T16:06:59.4974081Z Progress (1): 5.5/8.4 MB
2026-01-22T16:06:59.4977565Z Progress (1): 5.6/8.4 MB
2026-01-22T16:06:59.4977867Z Progress (1): 5.6/8.4 MB
2026-01-22T16:06:59.4978172Z Progress (1): 5.6/8.4 MB
2026-01-22T16:06:59.4978494Z Progress (2): 5.6/8.4 MB | 7.7/27 kB
2026-01-22T16:06:59.4978821Z Progress (2): 5.6/8.4 MB | 16/27 kB 
2026-01-22T16:06:59.4979139Z Progress (2): 5.6/8.4 MB | 27 kB   
2026-01-22T16:06:59.4979454Z Progress (2): 5.6/8.4 MB | 27 kB
2026-01-22T16:06:59.4981372Z Progress (2): 5.6/8.4 MB | 27 kB
2026-01-22T16:06:59.4983146Z Progress (2): 5.6/8.4 MB | 27 kB
2026-01-22T16:06:59.4985187Z Progress (2): 5.7/8.4 MB | 27 kB
2026-01-22T16:06:59.4986716Z Progress (2): 5.7/8.4 MB | 27 kB
2026-01-22T16:06:59.4988831Z Progress (2): 5.7/8.4 MB | 27 kB
2026-01-22T16:06:59.4992435Z Progress (2): 5.7/8.4 MB | 27 kB
2026-01-22T16:06:59.4995702Z Progress (2): 5.7/8.4 MB | 27 kB
2026-01-22T16:06:59.4998778Z Progress (2): 5.7/8.4 MB | 27 kB
2026-01-22T16:06:59.5000638Z                                 
2026-01-22T16:06:59.5027255Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-safari-driver/4.16.1/selenium-safari-driver-4.16.1.jar (27 kB at 44 kB/s)
2026-01-22T16:06:59.5029565Z Downloading from central: https://repo.maven.apache.org/maven2/joda-time/joda-time/2.13.0/joda-time-2.13.0.jar
2026-01-22T16:06:59.5031282Z Progress (1): 5.8/8.4 MB
2026-01-22T16:06:59.5033389Z Progress (1): 5.8/8.4 MB
2026-01-22T16:06:59.5034046Z Progress (1): 5.8/8.4 MB
2026-01-22T16:06:59.5036088Z Progress (1): 5.8/8.4 MB
2026-01-22T16:06:59.5036820Z Progress (1): 5.8/8.4 MB
2026-01-22T16:06:59.5037697Z Progress (1): 5.8/8.4 MB
2026-01-22T16:06:59.5040693Z Progress (1): 5.8/8.4 MB
2026-01-22T16:06:59.5042442Z Progress (1): 5.9/8.4 MB
2026-01-22T16:06:59.5044473Z Progress (1): 5.9/8.4 MB
2026-01-22T16:06:59.5045056Z Progress (1): 5.9/8.4 MB
2026-01-22T16:06:59.5047001Z Progress (1): 5.9/8.4 MB
2026-01-22T16:06:59.5047610Z Progress (1): 5.9/8.4 MB
2026-01-22T16:06:59.5049939Z Progress (1): 5.9/8.4 MB
2026-01-22T16:06:59.5050284Z Progress (1): 6.0/8.4 MB
2026-01-22T16:06:59.5050588Z Progress (1): 6.0/8.4 MB
2026-01-22T16:06:59.5050879Z Progress (1): 6.0/8.4 MB
2026-01-22T16:06:59.5051179Z Progress (1): 6.0/8.4 MB
2026-01-22T16:06:59.5051473Z Progress (1): 6.0/8.4 MB
2026-01-22T16:06:59.5051762Z Progress (1): 6.0/8.4 MB
2026-01-22T16:06:59.5052053Z Progress (1): 6.1/8.4 MB
2026-01-22T16:06:59.5052359Z Progress (1): 6.1/8.4 MB
2026-01-22T16:06:59.5052647Z Progress (1): 6.1/8.4 MB
2026-01-22T16:06:59.5056221Z Progress (1): 6.1/8.4 MB
2026-01-22T16:06:59.5056523Z Progress (1): 6.1/8.4 MB
2026-01-22T16:06:59.5056825Z Progress (1): 6.1/8.4 MB
2026-01-22T16:06:59.5058896Z Progress (1): 6.2/8.4 MB
2026-01-22T16:06:59.5086945Z Progress (1): 6.2/8.4 MB
2026-01-22T16:06:59.5088633Z Progress (1): 6.2/8.4 MB
2026-01-22T16:06:59.5090425Z Progress (1): 6.2/8.4 MB
2026-01-22T16:06:59.5093441Z Progress (1): 6.2/8.4 MB
2026-01-22T16:06:59.5095111Z Progress (1): 6.2/8.4 MB
2026-01-22T16:06:59.5097170Z Progress (1): 6.3/8.4 MB
2026-01-22T16:06:59.5097865Z Progress (1): 6.3/8.4 MB
2026-01-22T16:06:59.5098837Z Progress (1): 6.3/8.4 MB
2026-01-22T16:06:59.5100557Z Progress (1): 6.3/8.4 MB
2026-01-22T16:06:59.5101531Z Progress (1): 6.3/8.4 MB
2026-01-22T16:06:59.5102148Z Progress (1): 6.3/8.4 MB
2026-01-22T16:06:59.5104646Z Progress (1): 6.4/8.4 MB
2026-01-22T16:06:59.5104987Z Progress (1): 6.4/8.4 MB
2026-01-22T16:06:59.5105278Z Progress (1): 6.4/8.4 MB
2026-01-22T16:06:59.5105552Z Progress (1): 6.4/8.4 MB
2026-01-22T16:06:59.5105853Z Progress (1): 6.4/8.4 MB
2026-01-22T16:06:59.5106165Z Progress (1): 6.4/8.4 MB
2026-01-22T16:06:59.5106459Z Progress (1): 6.5/8.4 MB
2026-01-22T16:06:59.5106764Z Progress (1): 6.5/8.4 MB
2026-01-22T16:06:59.5109137Z Progress (1): 6.5/8.4 MB
2026-01-22T16:06:59.5111067Z Progress (1): 6.5/8.4 MB
2026-01-22T16:06:59.5139067Z Progress (1): 6.5/8.4 MB
2026-01-22T16:06:59.5140895Z Progress (1): 6.5/8.4 MB
2026-01-22T16:06:59.5141991Z Progress (2): 6.5/8.4 MB | 7.7/936 kB
2026-01-22T16:06:59.5143972Z Progress (2): 6.5/8.4 MB | 12/936 kB 
2026-01-22T16:06:59.5146008Z Progress (2): 6.5/8.4 MB | 28/936 kB
2026-01-22T16:06:59.5149208Z Progress (2): 6.5/8.4 MB | 44/936 kB
2026-01-22T16:06:59.5150612Z Progress (2): 6.5/8.4 MB | 61/936 kB
2026-01-22T16:06:59.5157100Z Progress (2): 6.5/8.4 MB | 77/936 kB
2026-01-22T16:06:59.5159649Z Progress (2): 6.5/8.4 MB | 93/936 kB
2026-01-22T16:06:59.5160439Z Progress (3): 6.5/8.4 MB | 93/936 kB | 8.2/531 kB
2026-01-22T16:06:59.5164728Z Progress (3): 6.5/8.4 MB | 93/936 kB | 25/531 kB 
2026-01-22T16:06:59.5166512Z Progress (3): 6.5/8.4 MB | 93/936 kB | 33/531 kB
2026-01-22T16:06:59.5167194Z Progress (3): 6.5/8.4 MB | 93/936 kB | 49/531 kB
2026-01-22T16:06:59.5168564Z Progress (3): 6.5/8.4 MB | 93/936 kB | 66/531 kB
2026-01-22T16:06:59.5171867Z Progress (4): 6.5/8.4 MB | 93/936 kB | 66/531 kB | 7.7/132 kB
2026-01-22T16:06:59.5201797Z Progress (4): 6.5/8.4 MB | 93/936 kB | 66/531 kB | 12/132 kB 
2026-01-22T16:06:59.5204055Z Progress (4): 6.5/8.4 MB | 93/936 kB | 66/531 kB | 29/132 kB
2026-01-22T16:06:59.5205227Z Progress (4): 6.5/8.4 MB | 93/936 kB | 66/531 kB | 45/132 kB
2026-01-22T16:06:59.5205977Z Progress (4): 6.5/8.4 MB | 93/936 kB | 66/531 kB | 61/132 kB
2026-01-22T16:06:59.5206992Z Progress (4): 6.5/8.4 MB | 93/936 kB | 66/531 kB | 78/132 kB
2026-01-22T16:06:59.5209127Z Progress (4): 6.5/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5210337Z Progress (4): 6.6/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5211478Z Progress (4): 6.6/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5212913Z Progress (4): 6.6/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5214180Z Progress (4): 6.6/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5217431Z Progress (4): 6.6/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5218702Z Progress (4): 6.6/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5221059Z Progress (4): 6.7/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5223592Z Progress (4): 6.7/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5224795Z Progress (4): 6.7/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5227110Z Progress (4): 6.7/8.4 MB | 93/936 kB | 66/531 kB | 94/132 kB
2026-01-22T16:06:59.5227911Z Progress (4): 6.7/8.4 MB | 93/936 kB | 82/531 kB | 94/132 kB
2026-01-22T16:06:59.5231024Z Progress (4): 6.7/8.4 MB | 93/936 kB | 98/531 kB | 94/132 kB
2026-01-22T16:06:59.5234619Z Progress (4): 6.7/8.4 MB | 93/936 kB | 115/531 kB | 94/132 kB
2026-01-22T16:06:59.5237259Z Progress (4): 6.7/8.4 MB | 110/936 kB | 115/531 kB | 94/132 kB
2026-01-22T16:06:59.5269898Z Progress (4): 6.7/8.4 MB | 110/936 kB | 131/531 kB | 94/132 kB
2026-01-22T16:06:59.5270726Z Progress (4): 6.7/8.4 MB | 110/936 kB | 147/531 kB | 94/132 kB
2026-01-22T16:06:59.5271883Z Progress (4): 6.7/8.4 MB | 110/936 kB | 164/531 kB | 94/132 kB
2026-01-22T16:06:59.5274162Z Progress (4): 6.7/8.4 MB | 110/936 kB | 180/531 kB | 94/132 kB
2026-01-22T16:06:59.5279231Z Progress (4): 6.7/8.4 MB | 110/936 kB | 197/531 kB | 94/132 kB
2026-01-22T16:06:59.5280168Z Progress (4): 6.7/8.4 MB | 110/936 kB | 213/531 kB | 94/132 kB
2026-01-22T16:06:59.5281244Z Progress (4): 6.7/8.4 MB | 110/936 kB | 229/531 kB | 94/132 kB
2026-01-22T16:06:59.5285376Z Progress (4): 6.7/8.4 MB | 126/936 kB | 229/531 kB | 94/132 kB
2026-01-22T16:06:59.5287057Z Progress (4): 6.7/8.4 MB | 143/936 kB | 229/531 kB | 94/132 kB
2026-01-22T16:06:59.5288255Z Progress (4): 6.7/8.4 MB | 159/936 kB | 229/531 kB | 94/132 kB
2026-01-22T16:06:59.5288998Z Progress (4): 6.7/8.4 MB | 175/936 kB | 229/531 kB | 94/132 kB
2026-01-22T16:06:59.5291970Z Progress (4): 6.7/8.4 MB | 192/936 kB | 229/531 kB | 94/132 kB
2026-01-22T16:06:59.5292608Z Progress (4): 6.7/8.4 MB | 208/936 kB | 229/531 kB | 94/132 kB
2026-01-22T16:06:59.5293393Z Progress (4): 6.7/8.4 MB | 225/936 kB | 229/531 kB | 94/132 kB
2026-01-22T16:06:59.5293916Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 94/132 kB
2026-01-22T16:06:59.5294465Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 111/132 kB
2026-01-22T16:06:59.5294940Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 127/132 kB
2026-01-22T16:06:59.5295394Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 132 kB    
2026-01-22T16:06:59.5295864Z                                                            
2026-01-22T16:06:59.5296483Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.18.0/jackson-datatype-jsr310-2.18.0.jar (132 kB at 204 kB/s)
2026-01-22T16:06:59.5297190Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-configuration2/2.11.0/commons-configuration2-2.11.0.jar
2026-01-22T16:06:59.5299277Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 7.7/639 kB
2026-01-22T16:06:59.5301734Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 8.2/639 kB
2026-01-22T16:06:59.5303873Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 25/639 kB 
2026-01-22T16:06:59.5306239Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 41/639 kB
2026-01-22T16:06:59.5307692Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 57/639 kB
2026-01-22T16:06:59.5309752Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 57/639 kB
2026-01-22T16:06:59.5312218Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 57/639 kB
2026-01-22T16:06:59.5316091Z Progress (4): 6.7/8.4 MB | 233/936 kB | 229/531 kB | 57/639 kB
2026-01-22T16:06:59.5321867Z Progress (4): 6.8/8.4 MB | 233/936 kB | 229/531 kB | 57/639 kB
2026-01-22T16:06:59.5349011Z Progress (4): 6.8/8.4 MB | 250/936 kB | 229/531 kB | 57/639 kB
2026-01-22T16:06:59.5351323Z Progress (4): 6.8/8.4 MB | 266/936 kB | 229/531 kB | 57/639 kB
2026-01-22T16:06:59.5353343Z Progress (4): 6.8/8.4 MB | 266/936 kB | 229/531 kB | 74/639 kB
2026-01-22T16:06:59.5355488Z Progress (4): 6.8/8.4 MB | 266/936 kB | 229/531 kB | 90/639 kB
2026-01-22T16:06:59.5357393Z Progress (4): 6.8/8.4 MB | 266/936 kB | 229/531 kB | 106/639 kB
2026-01-22T16:06:59.5358556Z Progress (4): 6.8/8.4 MB | 266/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5360533Z Progress (4): 6.8/8.4 MB | 266/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5361524Z Progress (4): 6.8/8.4 MB | 266/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5365991Z Progress (4): 6.8/8.4 MB | 266/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5370291Z Progress (4): 6.8/8.4 MB | 266/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5374686Z Progress (4): 6.8/8.4 MB | 266/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5376915Z Progress (4): 6.8/8.4 MB | 282/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5377667Z Progress (4): 6.8/8.4 MB | 299/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5381527Z Progress (4): 6.8/8.4 MB | 315/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5382090Z Progress (4): 6.8/8.4 MB | 331/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5382538Z Progress (4): 6.8/8.4 MB | 348/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5383894Z Progress (4): 6.8/8.4 MB | 364/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5384407Z Progress (4): 6.8/8.4 MB | 381/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5384886Z Progress (4): 6.8/8.4 MB | 397/936 kB | 229/531 kB | 115/639 kB
2026-01-22T16:06:59.5385463Z Progress (4): 6.8/8.4 MB | 397/936 kB | 246/531 kB | 115/639 kB
2026-01-22T16:06:59.5387887Z Progress (4): 6.8/8.4 MB | 397/936 kB | 262/531 kB | 115/639 kB
2026-01-22T16:06:59.5400110Z Progress (4): 6.8/8.4 MB | 397/936 kB | 279/531 kB | 115/639 kB
2026-01-22T16:06:59.5401789Z Progress (4): 6.8/8.4 MB | 397/936 kB | 295/531 kB | 115/639 kB
2026-01-22T16:06:59.5423442Z Progress (4): 6.8/8.4 MB | 397/936 kB | 311/531 kB | 115/639 kB
2026-01-22T16:06:59.5431393Z Progress (4): 6.8/8.4 MB | 397/936 kB | 328/531 kB | 115/639 kB
2026-01-22T16:06:59.5433906Z Progress (4): 6.8/8.4 MB | 397/936 kB | 344/531 kB | 115/639 kB
2026-01-22T16:06:59.5435785Z Progress (4): 6.8/8.4 MB | 397/936 kB | 360/531 kB | 115/639 kB
2026-01-22T16:06:59.5437909Z Progress (4): 6.8/8.4 MB | 397/936 kB | 377/531 kB | 115/639 kB
2026-01-22T16:06:59.5439728Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 115/639 kB
2026-01-22T16:06:59.5441999Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 131/639 kB
2026-01-22T16:06:59.5444062Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 139/639 kB
2026-01-22T16:06:59.5445783Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 147/639 kB
2026-01-22T16:06:59.5446973Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 156/639 kB
2026-01-22T16:06:59.5449082Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 172/639 kB
2026-01-22T16:06:59.5450968Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 180/639 kB
2026-01-22T16:06:59.5453410Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 188/639 kB
2026-01-22T16:06:59.5457699Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 197/639 kB
2026-01-22T16:06:59.5463280Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 213/639 kB
2026-01-22T16:06:59.5467286Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 229/639 kB
2026-01-22T16:06:59.5469043Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 246/639 kB
2026-01-22T16:06:59.5469681Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 254/639 kB
2026-01-22T16:06:59.5471298Z Progress (4): 6.8/8.4 MB | 397/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5472064Z Progress (4): 6.9/8.4 MB | 397/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5474428Z Progress (4): 6.9/8.4 MB | 397/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5475109Z Progress (4): 6.9/8.4 MB | 397/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5475693Z Progress (4): 6.9/8.4 MB | 397/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5477288Z Progress (4): 6.9/8.4 MB | 397/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5477956Z Progress (4): 6.9/8.4 MB | 397/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5480661Z Progress (4): 7.0/8.4 MB | 397/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5481021Z Progress (4): 7.0/8.4 MB | 397/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5481362Z Progress (4): 7.0/8.4 MB | 397/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5481721Z Progress (4): 7.0/8.4 MB | 413/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5482070Z Progress (4): 7.0/8.4 MB | 430/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5482419Z Progress (4): 7.0/8.4 MB | 446/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5483036Z Progress (4): 7.0/8.4 MB | 463/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5483384Z Progress (4): 7.0/8.4 MB | 479/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5483736Z Progress (4): 7.0/8.4 MB | 495/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5484599Z Progress (4): 7.0/8.4 MB | 512/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5484976Z Progress (4): 7.0/8.4 MB | 528/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5485617Z Progress (4): 7.0/8.4 MB | 544/936 kB | 393/531 kB | 270/639 kB
2026-01-22T16:06:59.5485977Z Progress (4): 7.0/8.4 MB | 544/936 kB | 410/531 kB | 270/639 kB
2026-01-22T16:06:59.5486330Z Progress (4): 7.0/8.4 MB | 544/936 kB | 426/531 kB | 270/639 kB
2026-01-22T16:06:59.5486678Z Progress (4): 7.0/8.4 MB | 544/936 kB | 442/531 kB | 270/639 kB
2026-01-22T16:06:59.5487030Z Progress (4): 7.0/8.4 MB | 544/936 kB | 459/531 kB | 270/639 kB
2026-01-22T16:06:59.5487368Z Progress (4): 7.0/8.4 MB | 544/936 kB | 475/531 kB | 270/639 kB
2026-01-22T16:06:59.5487699Z Progress (4): 7.0/8.4 MB | 544/936 kB | 492/531 kB | 270/639 kB
2026-01-22T16:06:59.5488449Z Progress (4): 7.0/8.4 MB | 544/936 kB | 508/531 kB | 270/639 kB
2026-01-22T16:06:59.5488816Z Progress (4): 7.0/8.4 MB | 544/936 kB | 524/531 kB | 270/639 kB
2026-01-22T16:06:59.5489170Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 270/639 kB    
2026-01-22T16:06:59.5489492Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 287/639 kB
2026-01-22T16:06:59.5489856Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 295/639 kB
2026-01-22T16:06:59.5490201Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 311/639 kB
2026-01-22T16:06:59.5490543Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 328/639 kB
2026-01-22T16:06:59.5490886Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 336/639 kB
2026-01-22T16:06:59.5491226Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 352/639 kB
2026-01-22T16:06:59.5491556Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 369/639 kB
2026-01-22T16:06:59.5559169Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 385/639 kB
2026-01-22T16:06:59.5560565Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 401/639 kB
2026-01-22T16:06:59.5566271Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 418/639 kB
2026-01-22T16:06:59.5568169Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5570948Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5572965Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5575652Z Progress (4): 7.0/8.4 MB | 544/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5577532Z Progress (4): 7.1/8.4 MB | 544/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5579606Z Progress (4): 7.1/8.4 MB | 544/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5581490Z Progress (4): 7.1/8.4 MB | 544/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5583885Z Progress (4): 7.1/8.4 MB | 544/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5585810Z Progress (4): 7.1/8.4 MB | 544/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5587854Z Progress (4): 7.1/8.4 MB | 544/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5589668Z Progress (4): 7.1/8.4 MB | 561/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5592090Z Progress (4): 7.1/8.4 MB | 577/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5593033Z Progress (4): 7.1/8.4 MB | 594/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5595313Z Progress (4): 7.1/8.4 MB | 610/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5596009Z Progress (4): 7.1/8.4 MB | 626/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5598185Z Progress (4): 7.1/8.4 MB | 643/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5600378Z Progress (4): 7.1/8.4 MB | 659/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5602216Z Progress (4): 7.1/8.4 MB | 676/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5604698Z Progress (4): 7.1/8.4 MB | 692/936 kB | 531 kB | 426/639 kB
2026-01-22T16:06:59.5605374Z                                                            
2026-01-22T16:06:59.5607536Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.jar (531 kB at 793 kB/s)
2026-01-22T16:06:59.5611679Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.11.0/commons-text-1.11.0.jar
2026-01-22T16:06:59.5615327Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 7.7/665 kB
2026-01-22T16:06:59.5616545Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 16/665 kB 
2026-01-22T16:06:59.5618752Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 32/665 kB
2026-01-22T16:06:59.5619992Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 49/665 kB
2026-01-22T16:06:59.5622306Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 65/665 kB
2026-01-22T16:06:59.5624397Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 81/665 kB
2026-01-22T16:06:59.5627462Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 98/665 kB
2026-01-22T16:06:59.5630725Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 114/665 kB
2026-01-22T16:06:59.5632935Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 131/665 kB
2026-01-22T16:06:59.5634816Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 147/665 kB
2026-01-22T16:06:59.5637862Z Progress (4): 7.1/8.4 MB | 692/936 kB | 426/639 kB | 163/665 kB
2026-01-22T16:06:59.5639826Z Progress (4): 7.1/8.4 MB | 692/936 kB | 442/639 kB | 163/665 kB
2026-01-22T16:06:59.5668879Z Progress (4): 7.1/8.4 MB | 692/936 kB | 459/639 kB | 163/665 kB
2026-01-22T16:06:59.5677241Z Progress (4): 7.1/8.4 MB | 692/936 kB | 467/639 kB | 163/665 kB
2026-01-22T16:06:59.5677652Z Progress (4): 7.1/8.4 MB | 692/936 kB | 475/639 kB | 163/665 kB
2026-01-22T16:06:59.5678018Z Progress (4): 7.1/8.4 MB | 692/936 kB | 492/639 kB | 163/665 kB
2026-01-22T16:06:59.5678361Z Progress (4): 7.1/8.4 MB | 692/936 kB | 508/639 kB | 163/665 kB
2026-01-22T16:06:59.5678721Z Progress (4): 7.1/8.4 MB | 692/936 kB | 524/639 kB | 163/665 kB
2026-01-22T16:06:59.5679057Z Progress (4): 7.1/8.4 MB | 692/936 kB | 541/639 kB | 163/665 kB
2026-01-22T16:06:59.5679405Z Progress (4): 7.1/8.4 MB | 692/936 kB | 557/639 kB | 163/665 kB
2026-01-22T16:06:59.5679773Z Progress (4): 7.1/8.4 MB | 692/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5680128Z Progress (4): 7.2/8.4 MB | 692/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5680625Z Progress (4): 7.2/8.4 MB | 692/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5680973Z Progress (4): 7.2/8.4 MB | 692/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5681336Z Progress (4): 7.2/8.4 MB | 692/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5681676Z Progress (4): 7.2/8.4 MB | 692/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5682020Z Progress (4): 7.2/8.4 MB | 692/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5682368Z Progress (4): 7.3/8.4 MB | 692/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5682961Z Progress (4): 7.3/8.4 MB | 692/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5683464Z Progress (4): 7.3/8.4 MB | 692/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5683819Z Progress (4): 7.3/8.4 MB | 708/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5684168Z Progress (4): 7.3/8.4 MB | 725/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5684522Z Progress (4): 7.3/8.4 MB | 741/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5684869Z Progress (4): 7.3/8.4 MB | 757/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5685207Z Progress (4): 7.3/8.4 MB | 774/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5685553Z Progress (4): 7.3/8.4 MB | 790/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5685924Z Progress (4): 7.3/8.4 MB | 807/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5686274Z Progress (4): 7.3/8.4 MB | 823/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5686622Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 163/665 kB
2026-01-22T16:06:59.5686962Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 180/665 kB
2026-01-22T16:06:59.5687329Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 196/665 kB
2026-01-22T16:06:59.5687665Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 213/665 kB
2026-01-22T16:06:59.5688001Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 229/665 kB
2026-01-22T16:06:59.5688365Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 245/665 kB
2026-01-22T16:06:59.5688720Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 262/665 kB
2026-01-22T16:06:59.5689069Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 278/665 kB
2026-01-22T16:06:59.5689421Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 294/665 kB
2026-01-22T16:06:59.5689755Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 311/665 kB
2026-01-22T16:06:59.5690084Z Progress (4): 7.3/8.4 MB | 839/936 kB | 573/639 kB | 327/665 kB
2026-01-22T16:06:59.5690505Z Progress (4): 7.3/8.4 MB | 839/936 kB | 590/639 kB | 327/665 kB
2026-01-22T16:06:59.5690847Z Progress (4): 7.3/8.4 MB | 839/936 kB | 606/639 kB | 327/665 kB
2026-01-22T16:06:59.5691200Z Progress (4): 7.3/8.4 MB | 839/936 kB | 623/639 kB | 327/665 kB
2026-01-22T16:06:59.5691574Z Progress (4): 7.3/8.4 MB | 839/936 kB | 631/639 kB | 327/665 kB
2026-01-22T16:06:59.5691921Z Progress (4): 7.3/8.4 MB | 839/936 kB | 639 kB | 327/665 kB    
2026-01-22T16:06:59.5692244Z Progress (4): 7.3/8.4 MB | 839/936 kB | 639 kB | 327/665 kB
2026-01-22T16:06:59.5692612Z Progress (4): 7.3/8.4 MB | 839/936 kB | 639 kB | 327/665 kB
2026-01-22T16:06:59.5733133Z Progress (4): 7.3/8.4 MB | 839/936 kB | 639 kB | 327/665 kB
2026-01-22T16:06:59.5733898Z Progress (5): 7.3/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 7.7/247 kB
2026-01-22T16:06:59.5736068Z Progress (5): 7.3/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 12/247 kB 
2026-01-22T16:06:59.5736761Z Progress (5): 7.3/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 29/247 kB
2026-01-22T16:06:59.5738873Z Progress (5): 7.3/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 45/247 kB
2026-01-22T16:06:59.5740784Z Progress (5): 7.3/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 61/247 kB
2026-01-22T16:06:59.5743078Z Progress (5): 7.3/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 78/247 kB
2026-01-22T16:06:59.5744971Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 78/247 kB
2026-01-22T16:06:59.5747145Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 78/247 kB
2026-01-22T16:06:59.5748849Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 78/247 kB
2026-01-22T16:06:59.5751123Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 78/247 kB
2026-01-22T16:06:59.5753164Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 327/665 kB | 78/247 kB
2026-01-22T16:06:59.5755963Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 344/665 kB | 78/247 kB
2026-01-22T16:06:59.5756684Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 360/665 kB | 78/247 kB
2026-01-22T16:06:59.5757742Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 376/665 kB | 78/247 kB
2026-01-22T16:06:59.5759664Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 393/665 kB | 78/247 kB
2026-01-22T16:06:59.5763597Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 409/665 kB | 78/247 kB
2026-01-22T16:06:59.5765330Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 426/665 kB | 78/247 kB
2026-01-22T16:06:59.5768168Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 442/665 kB | 78/247 kB
2026-01-22T16:06:59.5769810Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 458/665 kB | 78/247 kB
2026-01-22T16:06:59.5772091Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 475/665 kB | 78/247 kB
2026-01-22T16:06:59.5774037Z Progress (5): 7.4/8.4 MB | 839/936 kB | 639 kB | 491/665 kB | 78/247 kB
2026-01-22T16:06:59.5775107Z Progress (5): 7.4/8.4 MB | 856/936 kB | 639 kB | 491/665 kB | 78/247 kB
2026-01-22T16:06:59.5776801Z Progress (5): 7.4/8.4 MB | 872/936 kB | 639 kB | 491/665 kB | 78/247 kB
2026-01-22T16:06:59.5782544Z Progress (5): 7.4/8.4 MB | 889/936 kB | 639 kB | 491/665 kB | 78/247 kB
2026-01-22T16:06:59.5783438Z Progress (5): 7.4/8.4 MB | 905/936 kB | 639 kB | 491/665 kB | 78/247 kB
2026-01-22T16:06:59.5785037Z Progress (5): 7.4/8.4 MB | 921/936 kB | 639 kB | 491/665 kB | 78/247 kB
2026-01-22T16:06:59.5786189Z Progress (5): 7.4/8.4 MB | 936 kB | 639 kB | 491/665 kB | 78/247 kB    
2026-01-22T16:06:59.5788443Z                                                                    
2026-01-22T16:06:59.5789922Z Downloaded from central: https://repo.maven.apache.org/maven2/net/masterthought/cucumber-reporting/5.8.3/cucumber-reporting-5.8.3.jar (936 kB at 1.4 MB/s)
2026-01-22T16:06:59.5792193Z Progress (4): 7.4/8.4 MB | 639 kB | 491/665 kB | 94/247 kB
2026-01-22T16:06:59.5793932Z Progress (4): 7.4/8.4 MB | 639 kB | 491/665 kB | 111/247 kB
2026-01-22T16:06:59.5794903Z Progress (4): 7.4/8.4 MB | 639 kB | 491/665 kB | 111/247 kB
2026-01-22T16:06:59.5795718Z Progress (4): 7.5/8.4 MB | 639 kB | 491/665 kB | 111/247 kB
2026-01-22T16:06:59.5819066Z Progress (4): 7.5/8.4 MB | 639 kB | 491/665 kB | 111/247 kB
2026-01-22T16:06:59.5819431Z Progress (4): 7.5/8.4 MB | 639 kB | 491/665 kB | 111/247 kB
2026-01-22T16:06:59.5819802Z Progress (4): 7.5/8.4 MB | 639 kB | 491/665 kB | 111/247 kB
2026-01-22T16:06:59.5820163Z Progress (4): 7.5/8.4 MB | 639 kB | 491/665 kB | 111/247 kB
2026-01-22T16:06:59.5820504Z Progress (4): 7.5/8.4 MB | 639 kB | 491/665 kB | 111/247 kB
2026-01-22T16:06:59.5820864Z Progress (4): 7.6/8.4 MB | 639 kB | 491/665 kB | 111/247 kB
2026-01-22T16:06:59.5821198Z Progress (4): 7.6/8.4 MB | 639 kB | 491/665 kB | 111/247 kB
2026-01-22T16:06:59.5821495Z                                                            
2026-01-22T16:06:59.5821872Z Downloading from central: https://repo.maven.apache.org/maven2/org/jsoup/jsoup/1.18.1/jsoup-1.18.1.jar
2026-01-22T16:06:59.5822351Z Downloaded from central: https://repo.maven.apache.org/maven2/joda-time/joda-time/2.13.0/joda-time-2.13.0.jar (639 kB at 922 kB/s)
2026-01-22T16:06:59.5823180Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/owasp-java-html-sanitizer/20240325.1/owasp-java-html-sanitizer-20240325.1.jar
2026-01-22T16:06:59.5823713Z Progress (3): 7.6/8.4 MB | 491/665 kB | 127/247 kB
2026-01-22T16:06:59.5824099Z Progress (3): 7.6/8.4 MB | 491/665 kB | 143/247 kB
2026-01-22T16:06:59.5824464Z Progress (3): 7.6/8.4 MB | 491/665 kB | 160/247 kB
2026-01-22T16:06:59.5824838Z Progress (3): 7.6/8.4 MB | 491/665 kB | 164/247 kB
2026-01-22T16:06:59.5825207Z Progress (3): 7.6/8.4 MB | 491/665 kB | 180/247 kB
2026-01-22T16:06:59.5825823Z Progress (3): 7.6/8.4 MB | 491/665 kB | 196/247 kB
2026-01-22T16:06:59.5826189Z Progress (3): 7.6/8.4 MB | 491/665 kB | 213/247 kB
2026-01-22T16:06:59.5826927Z Progress (3): 7.6/8.4 MB | 491/665 kB | 229/247 kB
2026-01-22T16:06:59.5827299Z Progress (3): 7.6/8.4 MB | 491/665 kB | 245/247 kB
2026-01-22T16:06:59.5827663Z Progress (3): 7.6/8.4 MB | 491/665 kB | 247 kB    
2026-01-22T16:06:59.5827993Z                                               
2026-01-22T16:06:59.5828424Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.11.0/commons-text-1.11.0.jar (247 kB at 354 kB/s)
2026-01-22T16:06:59.5829050Z Progress (2): 7.6/8.4 MB | 507/665 kB
2026-01-22T16:06:59.5829399Z Progress (2): 7.6/8.4 MB | 524/665 kB
2026-01-22T16:06:59.5829759Z Progress (2): 7.6/8.4 MB | 540/665 kB
2026-01-22T16:06:59.5830101Z Progress (2): 7.6/8.4 MB | 557/665 kB
2026-01-22T16:06:59.5830452Z Progress (2): 7.6/8.4 MB | 573/665 kB
2026-01-22T16:06:59.5830807Z Progress (2): 7.6/8.4 MB | 589/665 kB
2026-01-22T16:06:59.5831167Z Progress (2): 7.6/8.4 MB | 606/665 kB
2026-01-22T16:06:59.5831518Z Progress (2): 7.6/8.4 MB | 622/665 kB
2026-01-22T16:06:59.5831852Z Progress (2): 7.6/8.4 MB | 639/665 kB
2026-01-22T16:06:59.5832165Z Progress (2): 7.6/8.4 MB | 655/665 kB
2026-01-22T16:06:59.5832465Z Progress (2): 7.6/8.4 MB | 665 kB    
2026-01-22T16:06:59.5832962Z Progress (2): 7.6/8.4 MB | 665 kB
2026-01-22T16:06:59.5833293Z Progress (2): 7.6/8.4 MB | 665 kB
2026-01-22T16:06:59.5833592Z Progress (2): 7.6/8.4 MB | 665 kB
2026-01-22T16:06:59.5833897Z Progress (2): 7.6/8.4 MB | 665 kB
2026-01-22T16:06:59.5834223Z Progress (2): 7.7/8.4 MB | 665 kB
2026-01-22T16:06:59.5834514Z Progress (2): 7.7/8.4 MB | 665 kB
2026-01-22T16:06:59.5834799Z Progress (2): 7.7/8.4 MB | 665 kB
2026-01-22T16:06:59.5865628Z Progress (2): 7.7/8.4 MB | 665 kB
2026-01-22T16:06:59.5866925Z Progress (2): 7.7/8.4 MB | 665 kB
2026-01-22T16:06:59.5868752Z Progress (2): 7.7/8.4 MB | 665 kB
2026-01-22T16:06:59.5870337Z                                  
2026-01-22T16:06:59.5871351Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java8-shim/20240325.1/java8-shim-20240325.1.jar
2026-01-22T16:06:59.5875241Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-configuration2/2.11.0/commons-configuration2-2.11.0.jar (665 kB at 948 kB/s)
2026-01-22T16:06:59.5877545Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java10-shim/20240325.1/java10-shim-20240325.1.jar
2026-01-22T16:06:59.5880475Z Progress (1): 7.7/8.4 MB
2026-01-22T16:06:59.5882484Z Progress (1): 7.8/8.4 MB
2026-01-22T16:06:59.5884718Z Progress (1): 7.8/8.4 MB
2026-01-22T16:06:59.5886648Z Progress (1): 7.8/8.4 MB
2026-01-22T16:06:59.5887480Z Progress (1): 7.8/8.4 MB
2026-01-22T16:06:59.5889308Z Progress (1): 7.8/8.4 MB
2026-01-22T16:06:59.5891796Z Progress (1): 7.8/8.4 MB
2026-01-22T16:06:59.5893758Z Progress (1): 7.9/8.4 MB
2026-01-22T16:06:59.5895302Z Progress (1): 7.9/8.4 MB
2026-01-22T16:06:59.5897165Z Progress (1): 7.9/8.4 MB
2026-01-22T16:06:59.5897660Z Progress (1): 7.9/8.4 MB
2026-01-22T16:06:59.5898068Z Progress (1): 7.9/8.4 MB
2026-01-22T16:06:59.5899394Z Progress (1): 7.9/8.4 MB
2026-01-22T16:06:59.5899827Z Progress (1): 8.0/8.4 MB
2026-01-22T16:06:59.5900246Z Progress (1): 8.0/8.4 MB
2026-01-22T16:06:59.5901443Z Progress (1): 8.0/8.4 MB
2026-01-22T16:06:59.5901858Z Progress (1): 8.0/8.4 MB
2026-01-22T16:06:59.5902285Z Progress (1): 8.0/8.4 MB
2026-01-22T16:06:59.5904006Z Progress (1): 8.0/8.4 MB
2026-01-22T16:06:59.5904586Z Progress (1): 8.1/8.4 MB
2026-01-22T16:06:59.5907678Z Progress (1): 8.1/8.4 MB
2026-01-22T16:06:59.5908319Z Progress (1): 8.1/8.4 MB
2026-01-22T16:06:59.5911532Z Progress (1): 8.1/8.4 MB
2026-01-22T16:06:59.5911856Z Progress (1): 8.1/8.4 MB
2026-01-22T16:06:59.5912141Z Progress (1): 8.1/8.4 MB
2026-01-22T16:06:59.5912427Z Progress (1): 8.2/8.4 MB
2026-01-22T16:06:59.5913051Z Progress (1): 8.2/8.4 MB
2026-01-22T16:06:59.5913346Z Progress (1): 8.2/8.4 MB
2026-01-22T16:06:59.5913631Z Progress (1): 8.2/8.4 MB
2026-01-22T16:06:59.5913934Z Progress (1): 8.2/8.4 MB
2026-01-22T16:06:59.5914223Z Progress (1): 8.2/8.4 MB
2026-01-22T16:06:59.5914510Z Progress (1): 8.3/8.4 MB
2026-01-22T16:06:59.5914791Z Progress (1): 8.3/8.4 MB
2026-01-22T16:06:59.5915100Z Progress (1): 8.3/8.4 MB
2026-01-22T16:06:59.5915389Z Progress (1): 8.3/8.4 MB
2026-01-22T16:06:59.5915684Z Progress (1): 8.3/8.4 MB
2026-01-22T16:06:59.5915976Z Progress (1): 8.3/8.4 MB
2026-01-22T16:06:59.5916262Z Progress (1): 8.4/8.4 MB
2026-01-22T16:06:59.5918829Z Progress (1): 8.4/8.4 MB
2026-01-22T16:06:59.5920824Z Progress (1): 8.4/8.4 MB
2026-01-22T16:06:59.5924341Z Progress (1): 8.4/8.4 MB
2026-01-22T16:06:59.5927471Z Progress (1): 8.4/8.4 MB
2026-01-22T16:06:59.5929942Z Progress (1): 8.4 MB    
2026-01-22T16:06:59.5931739Z                     
2026-01-22T16:06:59.5933856Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.13.0/selenium-manager-4.13.0.jar (8.4 MB at 12 MB/s)
2026-01-22T16:06:59.5935887Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/jcl-over-slf4j/2.0.16/jcl-over-slf4j-2.0.16.jar
2026-01-22T16:06:59.5987347Z Progress (1): 3.9 kB
2026-01-22T16:06:59.5987839Z                     
2026-01-22T16:06:59.5988399Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java10-shim/20240325.1/java10-shim-20240325.1.jar (3.9 kB at 5.4 kB/s)
2026-01-22T16:06:59.5988960Z Progress (1): 16/453 kB
2026-01-22T16:06:59.5989361Z Progress (1): 33/453 kB
2026-01-22T16:06:59.5989769Z Progress (1): 49/453 kB
2026-01-22T16:06:59.5990161Z Progress (1): 66/453 kB
2026-01-22T16:06:59.5991438Z Progress (1): 82/453 kB
2026-01-22T16:06:59.5991729Z                        
2026-01-22T16:06:59.5992146Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.17.1/jackson-databind-2.17.1.jar
2026-01-22T16:06:59.5998979Z Progress (1): 98/453 kB
2026-01-22T16:06:59.6003234Z Progress (1): 115/453 kB
2026-01-22T16:06:59.6024683Z Progress (1): 131/453 kB
2026-01-22T16:06:59.6025341Z Progress (1): 147/453 kB
2026-01-22T16:06:59.6026339Z Progress (1): 164/453 kB
2026-01-22T16:06:59.6026861Z Progress (1): 180/453 kB
2026-01-22T16:06:59.6027704Z Progress (1): 197/453 kB
2026-01-22T16:06:59.6028204Z Progress (1): 213/453 kB
2026-01-22T16:06:59.6029029Z Progress (1): 229/453 kB
2026-01-22T16:06:59.6029600Z Progress (1): 246/453 kB
2026-01-22T16:06:59.6032184Z Progress (1): 262/453 kB
2026-01-22T16:06:59.6037282Z Progress (1): 279/453 kB
2026-01-22T16:06:59.6042183Z Progress (1): 295/453 kB
2026-01-22T16:06:59.6047386Z Progress (1): 311/453 kB
2026-01-22T16:06:59.6051662Z Progress (1): 328/453 kB
2026-01-22T16:06:59.6074762Z Progress (1): 344/453 kB
2026-01-22T16:06:59.6077605Z Progress (1): 360/453 kB
2026-01-22T16:06:59.6080150Z Progress (2): 360/453 kB | 7.7/12 kB
2026-01-22T16:06:59.6084994Z Progress (2): 360/453 kB | 12 kB    
2026-01-22T16:06:59.6085682Z Progress (2): 377/453 kB | 12 kB
2026-01-22T16:06:59.6087230Z Progress (2): 393/453 kB | 12 kB
2026-01-22T16:06:59.6087537Z                                 
2026-01-22T16:06:59.6087962Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java8-shim/20240325.1/java8-shim-20240325.1.jar (12 kB at 16 kB/s)
2026-01-22T16:06:59.6088532Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.17.1/jackson-annotations-2.17.1.jar
2026-01-22T16:06:59.6088954Z Progress (1): 410/453 kB
2026-01-22T16:06:59.6089257Z Progress (1): 426/453 kB
2026-01-22T16:06:59.6089550Z Progress (1): 442/453 kB
2026-01-22T16:06:59.6089847Z Progress (1): 453 kB    
2026-01-22T16:06:59.6090113Z                     
2026-01-22T16:06:59.6090486Z Downloaded from central: https://repo.maven.apache.org/maven2/org/jsoup/jsoup/1.18.1/jsoup-1.18.1.jar (453 kB at 624 kB/s)
2026-01-22T16:06:59.6091114Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.17.1/jackson-core-2.17.1.jar
2026-01-22T16:06:59.6126395Z Progress (1): 3.4/242 kB
2026-01-22T16:06:59.6126739Z Progress (1): 20/242 kB 
2026-01-22T16:06:59.6127050Z Progress (1): 36/242 kB
2026-01-22T16:06:59.6127361Z Progress (1): 53/242 kB
2026-01-22T16:06:59.6127661Z Progress (1): 69/242 kB
2026-01-22T16:06:59.6127958Z Progress (1): 85/242 kB
2026-01-22T16:06:59.6128224Z Progress (1): 102/242 kB
2026-01-22T16:06:59.6130759Z Progress (1): 118/242 kB
2026-01-22T16:06:59.6134820Z Progress (1): 134/242 kB
2026-01-22T16:06:59.6154193Z Progress (1): 151/242 kB
2026-01-22T16:06:59.6164176Z Progress (1): 167/242 kB
2026-01-22T16:06:59.6227048Z Progress (1): 184/242 kB
2026-01-22T16:06:59.6229214Z Progress (1): 200/242 kB
2026-01-22T16:06:59.6230046Z Progress (1): 216/242 kB
2026-01-22T16:06:59.6230962Z Progress (1): 233/242 kB
2026-01-22T16:06:59.6233102Z Progress (1): 242 kB    
2026-01-22T16:06:59.6234927Z                     
2026-01-22T16:06:59.6236993Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/owasp-java-html-sanitizer/20240325.1/owasp-java-html-sanitizer-20240325.1.jar (242 kB at 328 kB/s)
2026-01-22T16:06:59.6239124Z Progress (1): 0/1.6 MB
2026-01-22T16:06:59.6243907Z Progress (1): 0/1.6 MB
2026-01-22T16:06:59.6245507Z Progress (1): 0/1.6 MB
2026-01-22T16:06:59.6245834Z Progress (2): 0/1.6 MB | 7.7/18 kB
2026-01-22T16:06:59.6246163Z Progress (2): 0/1.6 MB | 8.2/18 kB
2026-01-22T16:06:59.6246477Z Progress (2): 0/1.6 MB | 8.2/18 kB
2026-01-22T16:06:59.6246803Z Progress (2): 0/1.6 MB | 18 kB    
2026-01-22T16:06:59.6247111Z Progress (2): 0.1/1.6 MB | 18 kB
2026-01-22T16:06:59.6247446Z Progress (2): 0.1/1.6 MB | 18 kB
2026-01-22T16:06:59.6247745Z                                 
2026-01-22T16:06:59.6248151Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/jcl-over-slf4j/2.0.16/jcl-over-slf4j-2.0.16.jar (18 kB at 25 kB/s)
2026-01-22T16:06:59.6248572Z Progress (1): 0.1/1.6 MB
2026-01-22T16:06:59.6248880Z Progress (1): 0.1/1.6 MB
2026-01-22T16:06:59.6249183Z Progress (1): 0.1/1.6 MB
2026-01-22T16:06:59.6249486Z Progress (1): 0.1/1.6 MB
2026-01-22T16:06:59.6249781Z Progress (1): 0.2/1.6 MB
2026-01-22T16:06:59.6250084Z Progress (1): 0.2/1.6 MB
2026-01-22T16:06:59.6250375Z Progress (1): 0.2/1.6 MB
2026-01-22T16:06:59.6250651Z                         
2026-01-22T16:06:59.6251036Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/2.0.16/slf4j-simple-2.0.16.jar
2026-01-22T16:06:59.6251543Z Downloading from central: https://repo.maven.apache.org/maven2/com/aventstack/extentreports/5.1.1/extentreports-5.1.1.jar
2026-01-22T16:06:59.6273926Z Progress (1): 0.2/1.6 MB
2026-01-22T16:06:59.6274627Z Progress (1): 0.2/1.6 MB
2026-01-22T16:06:59.6275570Z Progress (1): 0.2/1.6 MB
2026-01-22T16:06:59.6276135Z Progress (1): 0.2/1.6 MB
2026-01-22T16:06:59.6277036Z Progress (1): 0.3/1.6 MB
2026-01-22T16:06:59.6277616Z Progress (1): 0.3/1.6 MB
2026-01-22T16:06:59.6278518Z Progress (1): 0.3/1.6 MB
2026-01-22T16:06:59.6279074Z Progress (1): 0.3/1.6 MB
2026-01-22T16:06:59.6280360Z Progress (1): 0.3/1.6 MB
2026-01-22T16:06:59.6280669Z Progress (1): 0.3/1.6 MB
2026-01-22T16:06:59.6280976Z Progress (1): 0.4/1.6 MB
2026-01-22T16:06:59.6281269Z Progress (1): 0.4/1.6 MB
2026-01-22T16:06:59.6281572Z Progress (1): 0.4/1.6 MB
2026-01-22T16:06:59.6281864Z Progress (1): 0.4/1.6 MB
2026-01-22T16:06:59.6282165Z Progress (1): 0.4/1.6 MB
2026-01-22T16:06:59.6284858Z Progress (1): 0.4/1.6 MB
2026-01-22T16:06:59.6289767Z Progress (1): 0.5/1.6 MB
2026-01-22T16:06:59.6322554Z Progress (1): 0.5/1.6 MB
2026-01-22T16:06:59.6323509Z Progress (2): 0.5/1.6 MB | 7.7/78 kB
2026-01-22T16:06:59.6325685Z Progress (2): 0.5/1.6 MB | 16/78 kB 
2026-01-22T16:06:59.6326412Z Progress (2): 0.5/1.6 MB | 16/78 kB
2026-01-22T16:06:59.6327535Z Progress (2): 0.5/1.6 MB | 32/78 kB
2026-01-22T16:06:59.6328249Z Progress (2): 0.5/1.6 MB | 32/78 kB
2026-01-22T16:06:59.6330061Z Progress (2): 0.5/1.6 MB | 49/78 kB
2026-01-22T16:06:59.6330675Z Progress (2): 0.5/1.6 MB | 49/78 kB
2026-01-22T16:06:59.6331587Z Progress (2): 0.5/1.6 MB | 65/78 kB
2026-01-22T16:06:59.6332128Z Progress (2): 0.5/1.6 MB | 65/78 kB
2026-01-22T16:06:59.6333210Z Progress (2): 0.5/1.6 MB | 78 kB   
2026-01-22T16:06:59.6333823Z Progress (2): 0.6/1.6 MB | 78 kB
2026-01-22T16:06:59.6364109Z Progress (2): 0.6/1.6 MB | 78 kB
2026-01-22T16:06:59.6367093Z Progress (2): 0.6/1.6 MB | 78 kB
2026-01-22T16:06:59.6370119Z Progress (2): 0.6/1.6 MB | 78 kB
2026-01-22T16:06:59.6370768Z                                 
2026-01-22T16:06:59.6374104Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.17.1/jackson-annotations-2.17.1.jar (78 kB at 105 kB/s)
2026-01-22T16:06:59.6374823Z Progress (1): 0.6/1.6 MB
2026-01-22T16:06:59.6375684Z Progress (1): 0.6/1.6 MB
2026-01-22T16:06:59.6376217Z Progress (2): 0.6/1.6 MB | 7.7/582 kB
2026-01-22T16:06:59.6377095Z Progress (2): 0.6/1.6 MB | 16/582 kB 
2026-01-22T16:06:59.6377624Z Progress (2): 0.6/1.6 MB | 32/582 kB
2026-01-22T16:06:59.6378508Z Progress (2): 0.6/1.6 MB | 49/582 kB
2026-01-22T16:06:59.6379065Z Progress (2): 0.6/1.6 MB | 65/582 kB
2026-01-22T16:06:59.6379996Z Progress (2): 0.6/1.6 MB | 81/582 kB
2026-01-22T16:06:59.6380596Z Progress (2): 0.6/1.6 MB | 98/582 kB
2026-01-22T16:06:59.6381501Z Progress (2): 0.6/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6382136Z Progress (2): 0.6/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6385278Z                                      
2026-01-22T16:06:59.6386026Z Downloading from central: https://repo.maven.apache.org/maven2/io/reactivex/rxjava3/rxjava/3.1.6/rxjava-3.1.6.jar
2026-01-22T16:06:59.6387106Z Progress (2): 0.7/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6388029Z Progress (2): 0.7/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6391292Z Progress (2): 0.7/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6392035Z Progress (2): 0.7/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6393334Z Progress (2): 0.7/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6394117Z Progress (2): 0.7/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6399433Z Progress (2): 0.8/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6401469Z Progress (2): 0.8/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6402684Z Progress (2): 0.8/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6404136Z Progress (2): 0.8/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6405024Z Progress (2): 0.8/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6410223Z Progress (2): 0.8/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6411995Z Progress (2): 0.9/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6416869Z Progress (2): 0.9/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6417894Z Progress (2): 0.9/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6419245Z Progress (2): 0.9/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6420166Z Progress (2): 0.9/1.6 MB | 114/582 kB
2026-01-22T16:06:59.6421685Z Progress (2): 0.9/1.6 MB | 131/582 kB
2026-01-22T16:06:59.6426891Z Progress (2): 0.9/1.6 MB | 147/582 kB
2026-01-22T16:06:59.6428072Z Progress (2): 0.9/1.6 MB | 163/582 kB
2026-01-22T16:06:59.6429014Z Progress (2): 0.9/1.6 MB | 180/582 kB
2026-01-22T16:06:59.6459147Z Progress (2): 0.9/1.6 MB | 196/582 kB
2026-01-22T16:06:59.6460229Z Progress (2): 0.9/1.6 MB | 212/582 kB
2026-01-22T16:06:59.6461264Z Progress (2): 0.9/1.6 MB | 229/582 kB
2026-01-22T16:06:59.6462280Z Progress (2): 0.9/1.6 MB | 236/582 kB
2026-01-22T16:06:59.6463462Z Progress (2): 0.9/1.6 MB | 252/582 kB
2026-01-22T16:06:59.6464484Z Progress (2): 0.9/1.6 MB | 269/582 kB
2026-01-22T16:06:59.6465573Z Progress (2): 0.9/1.6 MB | 285/582 kB
2026-01-22T16:06:59.6466291Z Progress (2): 0.9/1.6 MB | 301/582 kB
2026-01-22T16:06:59.6483521Z Progress (2): 0.9/1.6 MB | 318/582 kB
2026-01-22T16:06:59.6484152Z Progress (2): 0.9/1.6 MB | 318/582 kB
2026-01-22T16:06:59.6485113Z Progress (2): 0.9/1.6 MB | 334/582 kB
2026-01-22T16:06:59.6485689Z Progress (2): 0.9/1.6 MB | 351/582 kB
2026-01-22T16:06:59.6486567Z Progress (2): 0.9/1.6 MB | 351/582 kB
2026-01-22T16:06:59.6487126Z Progress (2): 1.0/1.6 MB | 351/582 kB
2026-01-22T16:06:59.6488192Z Progress (2): 1.0/1.6 MB | 367/582 kB
2026-01-22T16:06:59.6488819Z Progress (2): 1.0/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6489759Z Progress (2): 1.0/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6490400Z Progress (2): 1.0/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6491374Z Progress (2): 1.0/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6492011Z Progress (2): 1.0/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6493852Z Progress (2): 1.0/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6494202Z Progress (2): 1.1/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6494519Z Progress (2): 1.1/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6494993Z Progress (2): 1.1/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6495307Z Progress (2): 1.1/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6495623Z Progress (2): 1.1/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6495933Z Progress (2): 1.1/1.6 MB | 383/582 kB
2026-01-22T16:06:59.6496253Z Progress (2): 1.1/1.6 MB | 400/582 kB
2026-01-22T16:06:59.6496567Z Progress (2): 1.1/1.6 MB | 416/582 kB
2026-01-22T16:06:59.6496891Z Progress (2): 1.1/1.6 MB | 432/582 kB
2026-01-22T16:06:59.6497204Z Progress (2): 1.1/1.6 MB | 449/582 kB
2026-01-22T16:06:59.6497523Z Progress (2): 1.1/1.6 MB | 465/582 kB
2026-01-22T16:06:59.6497830Z Progress (2): 1.1/1.6 MB | 482/582 kB
2026-01-22T16:06:59.6498151Z Progress (2): 1.1/1.6 MB | 498/582 kB
2026-01-22T16:06:59.6498462Z Progress (2): 1.1/1.6 MB | 514/582 kB
2026-01-22T16:06:59.6498804Z Progress (3): 1.1/1.6 MB | 514/582 kB | 7.7/16 kB
2026-01-22T16:06:59.6499148Z Progress (3): 1.1/1.6 MB | 514/582 kB | 16 kB    
2026-01-22T16:06:59.6499455Z                                              
2026-01-22T16:06:59.6499863Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/2.0.16/slf4j-simple-2.0.16.jar (16 kB at 21 kB/s)
2026-01-22T16:06:59.6500395Z Downloading from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.jar
2026-01-22T16:06:59.6574572Z Progress (2): 1.1/1.6 MB | 531/582 kB
2026-01-22T16:06:59.6575362Z Progress (2): 1.1/1.6 MB | 547/582 kB
2026-01-22T16:06:59.6576783Z Progress (2): 1.1/1.6 MB | 564/582 kB
2026-01-22T16:06:59.6577447Z Progress (3): 1.1/1.6 MB | 564/582 kB | 0/1.0 MB
2026-01-22T16:06:59.6578953Z Progress (3): 1.1/1.6 MB | 564/582 kB | 0/1.0 MB
2026-01-22T16:06:59.6579581Z Progress (3): 1.1/1.6 MB | 580/582 kB | 0/1.0 MB
2026-01-22T16:06:59.6580572Z Progress (3): 1.1/1.6 MB | 582 kB | 0/1.0 MB    
2026-01-22T16:06:59.6581172Z Progress (3): 1.1/1.6 MB | 582 kB | 0/1.0 MB
2026-01-22T16:06:59.6582631Z Progress (3): 1.1/1.6 MB | 582 kB | 0/1.0 MB
2026-01-22T16:06:59.6583192Z Progress (3): 1.1/1.6 MB | 582 kB | 0.1/1.0 MB
2026-01-22T16:06:59.6589483Z Progress (3): 1.1/1.6 MB | 582 kB | 0.1/1.0 MB
2026-01-22T16:06:59.6589865Z Progress (3): 1.1/1.6 MB | 582 kB | 0.1/1.0 MB
2026-01-22T16:06:59.6590176Z Progress (3): 1.1/1.6 MB | 582 kB | 0.1/1.0 MB
2026-01-22T16:06:59.6590489Z Progress (3): 1.1/1.6 MB | 582 kB | 0.1/1.0 MB
2026-01-22T16:06:59.6590821Z Progress (3): 1.1/1.6 MB | 582 kB | 0.1/1.0 MB
2026-01-22T16:06:59.6591153Z Progress (3): 1.1/1.6 MB | 582 kB | 0.2/1.0 MB
2026-01-22T16:06:59.6591458Z Progress (3): 1.1/1.6 MB | 582 kB | 0.2/1.0 MB
2026-01-22T16:06:59.6591791Z Progress (3): 1.1/1.6 MB | 582 kB | 0.2/1.0 MB
2026-01-22T16:06:59.6592119Z Progress (3): 1.1/1.6 MB | 582 kB | 0.2/1.0 MB
2026-01-22T16:06:59.6592694Z Progress (3): 1.1/1.6 MB | 582 kB | 0.2/1.0 MB
2026-01-22T16:06:59.6593474Z Progress (3): 1.1/1.6 MB | 582 kB | 0.2/1.0 MB
2026-01-22T16:06:59.6593800Z Progress (3): 1.1/1.6 MB | 582 kB | 0.2/1.0 MB
2026-01-22T16:06:59.6594121Z Progress (3): 1.1/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6594912Z Progress (3): 1.1/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6595229Z Progress (3): 1.1/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6595580Z Progress (3): 1.2/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6595888Z Progress (3): 1.2/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6596199Z Progress (3): 1.2/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6596646Z Progress (3): 1.2/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6596961Z Progress (3): 1.2/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6597263Z Progress (3): 1.2/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6597595Z Progress (3): 1.2/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6597922Z Progress (3): 1.3/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6598228Z Progress (3): 1.3/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6598537Z Progress (3): 1.3/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6598872Z Progress (3): 1.3/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6599260Z Progress (3): 1.3/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6599572Z Progress (3): 1.3/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6599900Z Progress (3): 1.3/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6600234Z Progress (3): 1.4/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6600535Z Progress (3): 1.4/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6600862Z Progress (3): 1.4/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6601203Z Progress (3): 1.4/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6601752Z Progress (3): 1.4/1.6 MB | 582 kB | 0.3/1.0 MB
2026-01-22T16:06:59.6602302Z                                               
2026-01-22T16:06:59.6602690Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.17.1/jackson-core-2.17.1.jar (582 kB at 753 kB/s)
2026-01-22T16:06:59.6603800Z Downloading from central: https://repo.maven.apache.org/maven2/org/freemarker/freemarker/2.3.32/freemarker-2.3.32.jar
2026-01-22T16:06:59.6623317Z Progress (2): 1.4/1.6 MB | 0.3/1.0 MB
2026-01-22T16:06:59.6625880Z Progress (2): 1.4/1.6 MB | 0.3/1.0 MB
2026-01-22T16:06:59.6630530Z Progress (2): 1.4/1.6 MB | 0.3/1.0 MB
2026-01-22T16:06:59.6631332Z Progress (2): 1.4/1.6 MB | 0.4/1.0 MB
2026-01-22T16:06:59.6632552Z Progress (2): 1.4/1.6 MB | 0.4/1.0 MB
2026-01-22T16:06:59.6633679Z Progress (2): 1.4/1.6 MB | 0.4/1.0 MB
2026-01-22T16:06:59.6635224Z Progress (2): 1.4/1.6 MB | 0.4/1.0 MB
2026-01-22T16:06:59.6636041Z Progress (2): 1.4/1.6 MB | 0.4/1.0 MB
2026-01-22T16:06:59.6638719Z Progress (2): 1.4/1.6 MB | 0.4/1.0 MB
2026-01-22T16:06:59.6641171Z Progress (2): 1.4/1.6 MB | 0.4/1.0 MB
2026-01-22T16:06:59.6643824Z Progress (2): 1.4/1.6 MB | 0.4/1.0 MB
2026-01-22T16:06:59.6644938Z Progress (2): 1.4/1.6 MB | 0.4/1.0 MB
2026-01-22T16:06:59.6645583Z Progress (2): 1.4/1.6 MB | 0.4/1.0 MB
2026-01-22T16:06:59.6648115Z Progress (2): 1.4/1.6 MB | 0.5/1.0 MB
2026-01-22T16:06:59.6648699Z Progress (2): 1.4/1.6 MB | 0.5/1.0 MB
2026-01-22T16:06:59.6649121Z Progress (2): 1.4/1.6 MB | 0.5/1.0 MB
2026-01-22T16:06:59.6649560Z Progress (2): 1.4/1.6 MB | 0.5/1.0 MB
2026-01-22T16:06:59.6650034Z Progress (2): 1.4/1.6 MB | 0.5/1.0 MB
2026-01-22T16:06:59.6650913Z Progress (2): 1.4/1.6 MB | 0.5/1.0 MB
2026-01-22T16:06:59.6651410Z Progress (2): 1.4/1.6 MB | 0.5/1.0 MB
2026-01-22T16:06:59.6651893Z Progress (2): 1.4/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6652598Z Progress (2): 1.4/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6654644Z Progress (2): 1.4/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6655179Z Progress (2): 1.4/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6655664Z Progress (2): 1.4/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6656091Z Progress (2): 1.5/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6658065Z Progress (2): 1.5/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6658420Z Progress (2): 1.5/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6658772Z Progress (2): 1.5/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6659129Z Progress (2): 1.5/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6659503Z Progress (2): 1.5/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6659801Z Progress (2): 1.6/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6660477Z Progress (2): 1.6/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6661133Z Progress (2): 1.6/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6661455Z Progress (2): 1.6/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6661782Z Progress (2): 1.6/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6662128Z Progress (2): 1.6/1.6 MB | 0.6/1.0 MB
2026-01-22T16:06:59.6662582Z Progress (2): 1.6 MB | 0.6/1.0 MB    
2026-01-22T16:06:59.6663039Z                                  
2026-01-22T16:06:59.6663448Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.17.1/jackson-databind-2.17.1.jar (1.6 MB at 2.1 MB/s)
2026-01-22T16:06:59.6663936Z Progress (2): 0.6/1.0 MB | 0/2.7 MB
2026-01-22T16:06:59.6664273Z Progress (2): 0.6/1.0 MB | 0/2.7 MB
2026-01-22T16:06:59.6664586Z Progress (2): 0.6/1.0 MB | 0/2.7 MB
2026-01-22T16:06:59.6664872Z Progress (2): 0.6/1.0 MB | 0/2.7 MB
2026-01-22T16:06:59.6665576Z Progress (2): 0.6/1.0 MB | 0.1/2.7 MB
2026-01-22T16:06:59.6666054Z Progress (2): 0.6/1.0 MB | 0.1/2.7 MB
2026-01-22T16:06:59.6666351Z Progress (2): 0.6/1.0 MB | 0.1/2.7 MB
2026-01-22T16:06:59.6666647Z Progress (2): 0.6/1.0 MB | 0.1/2.7 MB
2026-01-22T16:06:59.6666993Z Progress (2): 0.6/1.0 MB | 0.1/2.7 MB
2026-01-22T16:06:59.6667333Z Progress (2): 0.6/1.0 MB | 0.1/2.7 MB
2026-01-22T16:06:59.6667669Z Progress (2): 0.6/1.0 MB | 0.2/2.7 MB
2026-01-22T16:06:59.6667965Z Progress (2): 0.6/1.0 MB | 0.2/2.7 MB
2026-01-22T16:06:59.6668266Z Progress (2): 0.6/1.0 MB | 0.2/2.7 MB
2026-01-22T16:06:59.6668604Z Progress (2): 0.6/1.0 MB | 0.2/2.7 MB
2026-01-22T16:06:59.6668937Z Progress (2): 0.6/1.0 MB | 0.2/2.7 MB
2026-01-22T16:06:59.6669240Z                                      
2026-01-22T16:06:59.6669596Z Downloading from central: https://repo.maven.apache.org/maven2/org/projectlombok/lombok/1.18.26/lombok-1.18.26.jar
2026-01-22T16:06:59.6669994Z Progress (2): 0.6/1.0 MB | 0.2/2.7 MB
2026-01-22T16:06:59.6670352Z Progress (2): 0.6/1.0 MB | 0.2/2.7 MB
2026-01-22T16:06:59.6670692Z Progress (2): 0.6/1.0 MB | 0.2/2.7 MB
2026-01-22T16:06:59.6671698Z Progress (2): 0.6/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6672026Z Progress (2): 0.6/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6672324Z Progress (2): 0.6/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6672693Z Progress (2): 0.7/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6673183Z Progress (2): 0.7/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6673505Z Progress (2): 0.7/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6674075Z Progress (2): 0.7/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6693400Z Progress (2): 0.7/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6694806Z Progress (2): 0.7/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6695807Z Progress (2): 0.7/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6697679Z Progress (2): 0.7/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6698822Z Progress (2): 0.7/1.0 MB | 0.3/2.7 MB
2026-01-22T16:06:59.6700236Z Progress (2): 0.7/1.0 MB | 0.4/2.7 MB
2026-01-22T16:06:59.6702511Z Progress (2): 0.7/1.0 MB | 0.4/2.7 MB
2026-01-22T16:06:59.6710306Z Progress (2): 0.7/1.0 MB | 0.4/2.7 MB
2026-01-22T16:06:59.6724740Z Progress (2): 0.8/1.0 MB | 0.4/2.7 MB
2026-01-22T16:06:59.6725443Z Progress (2): 0.8/1.0 MB | 0.4/2.7 MB
2026-01-22T16:06:59.6726442Z Progress (2): 0.8/1.0 MB | 0.4/2.7 MB
2026-01-22T16:06:59.6728186Z Progress (2): 0.8/1.0 MB | 0.4/2.7 MB
2026-01-22T16:06:59.6730263Z Progress (2): 0.8/1.0 MB | 0.4/2.7 MB
2026-01-22T16:06:59.6732098Z Progress (2): 0.8/1.0 MB | 0.5/2.7 MB
2026-01-22T16:06:59.6733611Z Progress (2): 0.8/1.0 MB | 0.5/2.7 MB
2026-01-22T16:06:59.6734886Z Progress (2): 0.8/1.0 MB | 0.5/2.7 MB
2026-01-22T16:06:59.6739032Z Progress (2): 0.8/1.0 MB | 0.5/2.7 MB
2026-01-22T16:06:59.6755006Z Progress (2): 0.8/1.0 MB | 0.5/2.7 MB
2026-01-22T16:06:59.6757362Z Progress (2): 0.8/1.0 MB | 0.5/2.7 MB
2026-01-22T16:06:59.6760195Z Progress (2): 0.8/1.0 MB | 0.6/2.7 MB
2026-01-22T16:06:59.6761930Z Progress (2): 0.8/1.0 MB | 0.6/2.7 MB
2026-01-22T16:06:59.6763389Z Progress (2): 0.8/1.0 MB | 0.6/2.7 MB
2026-01-22T16:06:59.6838087Z Progress (2): 0.8/1.0 MB | 0.6/2.7 MB
2026-01-22T16:06:59.6882259Z Progress (2): 0.8/1.0 MB | 0.6/2.7 MB
2026-01-22T16:06:59.6882975Z Progress (2): 0.8/1.0 MB | 0.6/2.7 MB
2026-01-22T16:06:59.6883332Z Progress (2): 0.8/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6883648Z Progress (2): 0.8/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6883960Z Progress (2): 0.8/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6884449Z Progress (2): 0.8/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6885299Z Progress (2): 0.8/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6885934Z Progress (2): 0.8/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6886645Z Progress (2): 0.8/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6887749Z Progress (2): 0.8/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6888838Z Progress (2): 0.8/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6889194Z Progress (2): 0.8/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6889528Z Progress (2): 0.9/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6889839Z Progress (2): 0.9/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6890171Z Progress (2): 0.9/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6890657Z Progress (3): 0.9/1.0 MB | 0.7/2.7 MB | 7.7/12 kB
2026-01-22T16:06:59.6890986Z Progress (3): 0.9/1.0 MB | 0.7/2.7 MB | 12 kB    
2026-01-22T16:06:59.6891283Z                                              
2026-01-22T16:06:59.6891871Z Downloaded from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.jar (12 kB at 15 kB/s)
2026-01-22T16:06:59.6892681Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.jar
2026-01-22T16:06:59.6893783Z Progress (2): 0.9/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6894118Z Progress (2): 0.9/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6894432Z Progress (2): 0.9/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6894750Z Progress (2): 0.9/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6895055Z Progress (2): 1.0/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6895370Z Progress (2): 1.0/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6895686Z Progress (2): 1.0/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6896012Z Progress (2): 1.0/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6896323Z Progress (2): 1.0/1.0 MB | 0.7/2.7 MB
2026-01-22T16:06:59.6896637Z Progress (2): 1.0 MB | 0.7/2.7 MB    
2026-01-22T16:06:59.6897164Z                                  
2026-01-22T16:06:59.6905671Z Downloaded from central: https://repo.maven.apache.org/maven2/com/aventstack/extentreports/5.1.1/extentreports-5.1.1.jar (1.0 MB at 1.3 MB/s)
2026-01-22T16:06:59.6934031Z Progress (1): 0.7/2.7 MB
2026-01-22T16:06:59.6941215Z Progress (1): 0.7/2.7 MB
2026-01-22T16:06:59.7004238Z                         
2026-01-22T16:06:59.7004912Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-cucumber7-jvm/2.29.0/allure-cucumber7-jvm-2.29.0.jar
2026-01-22T16:06:59.7005506Z Progress (1): 0.7/2.7 MB
2026-01-22T16:06:59.7012093Z Progress (1): 0.8/2.7 MB
2026-01-22T16:06:59.7013222Z Progress (1): 0.8/2.7 MB
2026-01-22T16:06:59.7013834Z Progress (1): 0.8/2.7 MB
2026-01-22T16:06:59.7014442Z Progress (1): 0.8/2.7 MB
2026-01-22T16:06:59.7015175Z Progress (1): 0.8/2.7 MB
2026-01-22T16:06:59.7015949Z Progress (1): 0.8/2.7 MB
2026-01-22T16:06:59.7016563Z Progress (1): 0.9/2.7 MB
2026-01-22T16:06:59.7017147Z Progress (1): 0.9/2.7 MB
2026-01-22T16:06:59.7017723Z Progress (1): 0.9/2.7 MB
2026-01-22T16:06:59.7018301Z Progress (1): 0.9/2.7 MB
2026-01-22T16:06:59.7019041Z Progress (1): 0.9/2.7 MB
2026-01-22T16:06:59.7019959Z Progress (1): 0.9/2.7 MB
2026-01-22T16:06:59.7021846Z Progress (1): 0.9/2.7 MB
2026-01-22T16:06:59.7023737Z Progress (1): 1.0/2.7 MB
2026-01-22T16:06:59.7024694Z Progress (1): 1.0/2.7 MB
2026-01-22T16:06:59.7026722Z Progress (1): 1.0/2.7 MB
2026-01-22T16:06:59.7028749Z Progress (1): 1.0/2.7 MB
2026-01-22T16:06:59.7030746Z Progress (1): 1.0/2.7 MB
2026-01-22T16:06:59.7047335Z Progress (1): 1.0/2.7 MB
2026-01-22T16:06:59.7049778Z Progress (1): 1.1/2.7 MB
2026-01-22T16:06:59.7050835Z Progress (2): 1.1/2.7 MB | 0/1.7 MB
2026-01-22T16:06:59.7051303Z Progress (2): 1.1/2.7 MB | 0/1.7 MB
2026-01-22T16:06:59.7051781Z Progress (2): 1.1/2.7 MB | 0/1.7 MB
2026-01-22T16:06:59.7052340Z Progress (2): 1.1/2.7 MB | 0/1.7 MB
2026-01-22T16:06:59.7052924Z Progress (2): 1.1/2.7 MB | 0.1/1.7 MB
2026-01-22T16:06:59.7053401Z Progress (2): 1.1/2.7 MB | 0.1/1.7 MB
2026-01-22T16:06:59.7053801Z Progress (2): 1.1/2.7 MB | 0.1/1.7 MB
2026-01-22T16:06:59.7054243Z Progress (2): 1.1/2.7 MB | 0.1/1.7 MB
2026-01-22T16:06:59.7054776Z Progress (2): 1.1/2.7 MB | 0.1/1.7 MB
2026-01-22T16:06:59.7055205Z Progress (2): 1.1/2.7 MB | 0.1/1.7 MB
2026-01-22T16:06:59.7055751Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0/2.0 MB
2026-01-22T16:06:59.7056677Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0/2.0 MB
2026-01-22T16:06:59.7057296Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0/2.0 MB
2026-01-22T16:06:59.7059207Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0/2.0 MB
2026-01-22T16:06:59.7059551Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.1/2.0 MB
2026-01-22T16:06:59.7059902Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.1/2.0 MB
2026-01-22T16:06:59.7060332Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.1/2.0 MB
2026-01-22T16:06:59.7060642Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.1/2.0 MB
2026-01-22T16:06:59.7060990Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.1/2.0 MB
2026-01-22T16:06:59.7061319Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.1/2.0 MB
2026-01-22T16:06:59.7061635Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7061973Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7062314Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7062627Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7063124Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7063477Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7063801Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7064127Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7064459Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7064810Z Progress (3): 1.1/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7065117Z Progress (3): 1.2/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7065442Z Progress (3): 1.2/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7065786Z Progress (3): 1.2/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7066105Z Progress (3): 1.2/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7066423Z Progress (3): 1.2/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7066770Z Progress (3): 1.2/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7067093Z Progress (3): 1.3/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7067408Z Progress (3): 1.3/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7067743Z Progress (3): 1.3/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7068086Z Progress (3): 1.3/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7068391Z Progress (3): 1.3/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7068717Z Progress (3): 1.3/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7069064Z Progress (3): 1.4/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7069389Z Progress (3): 1.4/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7069697Z Progress (3): 1.4/2.7 MB | 0.1/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7070043Z Progress (3): 1.4/2.7 MB | 0.2/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7070374Z Progress (3): 1.4/2.7 MB | 0.2/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7070696Z Progress (3): 1.4/2.7 MB | 0.2/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7071022Z Progress (3): 1.4/2.7 MB | 0.2/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7071376Z Progress (3): 1.4/2.7 MB | 0.2/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7071686Z Progress (3): 1.4/2.7 MB | 0.2/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7072004Z Progress (3): 1.4/2.7 MB | 0.2/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7072340Z Progress (3): 1.4/2.7 MB | 0.3/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7072671Z Progress (3): 1.4/2.7 MB | 0.3/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7073163Z Progress (3): 1.4/2.7 MB | 0.3/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7073489Z Progress (3): 1.4/2.7 MB | 0.3/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7073807Z Progress (3): 1.4/2.7 MB | 0.3/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7074163Z Progress (3): 1.4/2.7 MB | 0.3/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7074485Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7074801Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.2/2.0 MB
2026-01-22T16:06:59.7075242Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.3/2.0 MB
2026-01-22T16:06:59.7075575Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.3/2.0 MB
2026-01-22T16:06:59.7075899Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.3/2.0 MB
2026-01-22T16:06:59.7076227Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.3/2.0 MB
2026-01-22T16:06:59.7076566Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.3/2.0 MB
2026-01-22T16:06:59.7076875Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.3/2.0 MB
2026-01-22T16:06:59.7077208Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.4/2.0 MB
2026-01-22T16:06:59.7077640Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.4/2.0 MB
2026-01-22T16:06:59.7077960Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.4/2.0 MB
2026-01-22T16:06:59.7078283Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.4/2.0 MB
2026-01-22T16:06:59.7078631Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.4/2.0 MB
2026-01-22T16:06:59.7078944Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.4/2.0 MB
2026-01-22T16:06:59.7079270Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7079604Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7079942Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7080254Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7080584Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7080920Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7081232Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7081549Z Progress (3): 1.4/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7081897Z Progress (3): 1.5/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7082211Z Progress (3): 1.5/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7082527Z Progress (3): 1.5/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7113179Z Progress (3): 1.5/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7113586Z Progress (3): 1.5/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7113919Z Progress (3): 1.5/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7114270Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7114597Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7114918Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7115245Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7115597Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7115924Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7116254Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7116580Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7116911Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7117251Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7117574Z Progress (3): 1.6/2.7 MB | 0.4/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7117887Z Progress (3): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7118245Z Progress (3): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7118572Z Progress (3): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7118897Z Progress (3): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB
2026-01-22T16:06:59.7119234Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 7.7/658 kB
2026-01-22T16:06:59.7119613Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 16/658 kB 
2026-01-22T16:06:59.7119953Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 32/658 kB
2026-01-22T16:06:59.7120277Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 49/658 kB
2026-01-22T16:06:59.7120635Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 65/658 kB
2026-01-22T16:06:59.7120978Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 81/658 kB
2026-01-22T16:06:59.7121313Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 98/658 kB
2026-01-22T16:06:59.7121658Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 114/658 kB
2026-01-22T16:06:59.7122013Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7122448Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7122978Z Progress (4): 1.6/2.7 MB | 0.5/1.7 MB | 0.5/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7123370Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.5/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7128492Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.5/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7128896Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.5/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7129280Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.5/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7129813Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.5/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7130206Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.5/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7130583Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.5/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7130968Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.6/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7131342Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.6/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7131801Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.6/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7132174Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.6/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7132562Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.6/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7154036Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.6/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7154441Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7154787Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7155478Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 131/658 kB
2026-01-22T16:06:59.7161212Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 147/658 kB
2026-01-22T16:06:59.7162355Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 163/658 kB
2026-01-22T16:06:59.7163284Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 180/658 kB
2026-01-22T16:06:59.7164334Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 196/658 kB
2026-01-22T16:06:59.7164971Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 213/658 kB
2026-01-22T16:06:59.7165975Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 229/658 kB
2026-01-22T16:06:59.7166593Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 245/658 kB
2026-01-22T16:06:59.7167593Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 262/658 kB
2026-01-22T16:06:59.7168241Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 278/658 kB
2026-01-22T16:06:59.7169220Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 294/658 kB
2026-01-22T16:06:59.7169966Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 311/658 kB
2026-01-22T16:06:59.7170924Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 327/658 kB
2026-01-22T16:06:59.7171583Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 344/658 kB
2026-01-22T16:06:59.7172540Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 360/658 kB
2026-01-22T16:06:59.7173338Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 376/658 kB
2026-01-22T16:06:59.7174357Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 393/658 kB
2026-01-22T16:06:59.7174991Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 409/658 kB
2026-01-22T16:06:59.7175931Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 426/658 kB
2026-01-22T16:06:59.7176565Z Progress (4): 1.6/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7177527Z Progress (4): 1.7/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7178195Z Progress (4): 1.7/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7179176Z Progress (4): 1.7/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7179810Z Progress (4): 1.7/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7180767Z Progress (4): 1.7/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7181372Z Progress (4): 1.7/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7182355Z Progress (4): 1.8/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7183332Z Progress (4): 1.8/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7184308Z Progress (4): 1.8/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7184967Z Progress (4): 1.8/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7185925Z Progress (4): 1.8/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7186549Z Progress (4): 1.8/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7187506Z Progress (4): 1.9/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7188391Z Progress (4): 1.9/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7189339Z Progress (4): 1.9/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7191602Z Progress (4): 1.9/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7213581Z Progress (4): 1.9/2.7 MB | 0.6/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7214484Z Progress (4): 1.9/2.7 MB | 0.7/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7216012Z Progress (4): 1.9/2.7 MB | 0.7/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7216385Z Progress (4): 1.9/2.7 MB | 0.7/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7216738Z Progress (4): 1.9/2.7 MB | 0.7/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7217109Z Progress (4): 1.9/2.7 MB | 0.7/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7217454Z Progress (4): 1.9/2.7 MB | 0.7/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7217796Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7218155Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7218523Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7218861Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.7/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7219212Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.8/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7219551Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.8/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7219901Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.8/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7220257Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.8/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7220604Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.8/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7220929Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.8/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7221285Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.8/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7221624Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7221987Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7222324Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7222656Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7230677Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7232404Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7233812Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7235453Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7238110Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7240186Z Progress (4): 1.9/2.7 MB | 0.8/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7241453Z Progress (4): 1.9/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7242608Z Progress (4): 1.9/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7243951Z Progress (4): 1.9/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7245087Z Progress (4): 1.9/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7245805Z Progress (4): 2.0/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7247264Z Progress (4): 2.0/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7249165Z Progress (4): 2.0/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7251182Z Progress (4): 2.0/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7253481Z Progress (4): 2.0/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7255363Z Progress (4): 2.0/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7256960Z Progress (4): 2.1/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7273826Z Progress (4): 2.1/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7274553Z Progress (4): 2.1/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7276281Z Progress (4): 2.1/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7276639Z Progress (4): 2.1/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7276985Z Progress (4): 2.1/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7277330Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 442/658 kB
2026-01-22T16:06:59.7291277Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 458/658 kB
2026-01-22T16:06:59.7291693Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 475/658 kB
2026-01-22T16:06:59.7292214Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 491/658 kB
2026-01-22T16:06:59.7292585Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 507/658 kB
2026-01-22T16:06:59.7293958Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 524/658 kB
2026-01-22T16:06:59.7294315Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 540/658 kB
2026-01-22T16:06:59.7294656Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 557/658 kB
2026-01-22T16:06:59.7295025Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 573/658 kB
2026-01-22T16:06:59.7295369Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 589/658 kB
2026-01-22T16:06:59.7295696Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 606/658 kB
2026-01-22T16:06:59.7296047Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 622/658 kB
2026-01-22T16:06:59.7296399Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 639/658 kB
2026-01-22T16:06:59.7296747Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 655/658 kB
2026-01-22T16:06:59.7297104Z Progress (4): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB | 658 kB    
2026-01-22T16:06:59.7297426Z                                                            
2026-01-22T16:06:59.7297836Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.jar (658 kB at 782 kB/s)
2026-01-22T16:06:59.7298289Z Progress (3): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB
2026-01-22T16:06:59.7298628Z Progress (3): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB
2026-01-22T16:06:59.7298960Z Progress (3): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB
2026-01-22T16:06:59.7299298Z Progress (3): 2.2/2.7 MB | 0.9/1.7 MB | 0.9/2.0 MB
2026-01-22T16:06:59.7299669Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 0.9/2.0 MB
2026-01-22T16:06:59.7299993Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 0.9/2.0 MB
2026-01-22T16:06:59.7300337Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 0.9/2.0 MB
2026-01-22T16:06:59.7300681Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 0.9/2.0 MB
2026-01-22T16:06:59.7301037Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 0.9/2.0 MB
2026-01-22T16:06:59.7301383Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 0.9/2.0 MB
2026-01-22T16:06:59.7301703Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.0/2.0 MB
2026-01-22T16:06:59.7302025Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.0/2.0 MB
2026-01-22T16:06:59.7302375Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.0/2.0 MB
2026-01-22T16:06:59.7302877Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.0/2.0 MB
2026-01-22T16:06:59.7303250Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.0/2.0 MB
2026-01-22T16:06:59.7303571Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.0/2.0 MB
2026-01-22T16:06:59.7303909Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.1/2.0 MB
2026-01-22T16:06:59.7304264Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.1/2.0 MB
2026-01-22T16:06:59.7304609Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.1/2.0 MB
2026-01-22T16:06:59.7304922Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.1/2.0 MB
2026-01-22T16:06:59.7305384Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.1/2.0 MB
2026-01-22T16:06:59.7305704Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.1/2.0 MB
2026-01-22T16:06:59.7306026Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.1/2.0 MB
2026-01-22T16:06:59.7326086Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7326484Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7326861Z Progress (3): 2.2/2.7 MB | 1.0/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7327223Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7327750Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7328109Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7328475Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7328836Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7329204Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7329575Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7329933Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7330297Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7330661Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7331003Z Progress (3): 2.2/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7331343Z Progress (3): 2.3/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7331694Z Progress (3): 2.3/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7332051Z Progress (3): 2.3/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7332397Z Progress (3): 2.3/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7332902Z Progress (3): 2.3/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7333236Z Progress (3): 2.3/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7333584Z Progress (3): 2.4/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7333932Z Progress (3): 2.4/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7334257Z Progress (3): 2.4/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7334579Z Progress (3): 2.4/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7334920Z Progress (3): 2.4/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7335246Z Progress (3): 2.4/2.7 MB | 1.1/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7335527Z                                                   
2026-01-22T16:06:59.7335920Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-java-commons/2.29.0/allure-java-commons-2.29.0.jar
2026-01-22T16:06:59.7336343Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7336672Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7337000Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7337332Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7337639Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7337970Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7338314Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7363297Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7363689Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7364057Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7364411Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.2/2.0 MB
2026-01-22T16:06:59.7364769Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.3/2.0 MB
2026-01-22T16:06:59.7365085Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.3/2.0 MB
2026-01-22T16:06:59.7365408Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.3/2.0 MB
2026-01-22T16:06:59.7365754Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.3/2.0 MB
2026-01-22T16:06:59.7366104Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.3/2.0 MB
2026-01-22T16:06:59.7366414Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.3/2.0 MB
2026-01-22T16:06:59.7366755Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7367076Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7367554Z Progress (3): 2.4/2.7 MB | 1.2/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7367891Z Progress (3): 2.4/2.7 MB | 1.3/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7368208Z Progress (3): 2.4/2.7 MB | 1.3/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7368527Z Progress (3): 2.4/2.7 MB | 1.3/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7368879Z Progress (3): 2.4/2.7 MB | 1.3/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7369206Z Progress (3): 2.4/2.7 MB | 1.3/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7369531Z Progress (3): 2.4/2.7 MB | 1.3/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7369992Z Progress (3): 2.4/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7370299Z Progress (3): 2.4/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7370616Z Progress (3): 2.4/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7370946Z Progress (3): 2.5/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7371297Z Progress (3): 2.5/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7371643Z Progress (3): 2.5/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7371967Z Progress (3): 2.5/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7372288Z Progress (3): 2.5/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7374165Z Progress (3): 2.5/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7375083Z Progress (3): 2.6/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7375995Z Progress (3): 2.6/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7377913Z Progress (3): 2.6/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7379043Z Progress (3): 2.6/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7380137Z Progress (3): 2.6/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7381244Z Progress (3): 2.6/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7382367Z Progress (3): 2.6/2.7 MB | 1.4/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7384078Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7385281Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7386382Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7387475Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7397018Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7401279Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7402467Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7403870Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.4/2.0 MB
2026-01-22T16:06:59.7405041Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.5/2.0 MB
2026-01-22T16:06:59.7406147Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.5/2.0 MB
2026-01-22T16:06:59.7407275Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.5/2.0 MB
2026-01-22T16:06:59.7408508Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.5/2.0 MB
2026-01-22T16:06:59.7409687Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.5/2.0 MB
2026-01-22T16:06:59.7410779Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.5/2.0 MB
2026-01-22T16:06:59.7413532Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.5/2.0 MB
2026-01-22T16:06:59.7415807Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.6/2.0 MB
2026-01-22T16:06:59.7417059Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.6/2.0 MB
2026-01-22T16:06:59.7417915Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.6/2.0 MB
2026-01-22T16:06:59.7421845Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.6/2.0 MB
2026-01-22T16:06:59.7422549Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.6/2.0 MB
2026-01-22T16:06:59.7424206Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.6/2.0 MB
2026-01-22T16:06:59.7425235Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7426757Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7427443Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7428887Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7429942Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7430976Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7431994Z Progress (3): 2.6/2.7 MB | 1.5/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7433775Z Progress (3): 2.7/2.7 MB | 1.5/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7434909Z Progress (3): 2.7 MB | 1.5/1.7 MB | 1.7/2.0 MB    
2026-01-22T16:06:59.7436500Z Progress (3): 2.7 MB | 1.5/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7437258Z Progress (3): 2.7 MB | 1.6/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7443541Z Progress (3): 2.7 MB | 1.6/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7445079Z Progress (3): 2.7 MB | 1.6/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7446113Z Progress (3): 2.7 MB | 1.6/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7447238Z Progress (3): 2.7 MB | 1.6/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7448820Z Progress (3): 2.7 MB | 1.6/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7450843Z Progress (3): 2.7 MB | 1.7/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7452205Z                                               
2026-01-22T16:06:59.7452645Z Downloaded from central: https://repo.maven.apache.org/maven2/io/reactivex/rxjava3/rxjava/3.1.6/rxjava-3.1.6.jar (2.7 MB at 3.1 MB/s)
2026-01-22T16:06:59.7453392Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-model/2.29.0/allure-model-2.29.0.jar
2026-01-22T16:06:59.7453810Z Progress (2): 1.7/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7454117Z Progress (2): 1.7/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7454442Z Progress (2): 1.7/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7454786Z Progress (2): 1.7/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7455122Z Progress (2): 1.7/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7455422Z Progress (2): 1.7/1.7 MB | 1.7/2.0 MB
2026-01-22T16:06:59.7455716Z Progress (2): 1.7/1.7 MB | 1.8/2.0 MB
2026-01-22T16:06:59.7456066Z Progress (2): 1.7/1.7 MB | 1.8/2.0 MB
2026-01-22T16:06:59.7456402Z Progress (2): 1.7 MB | 1.8/2.0 MB    
2026-01-22T16:06:59.7456706Z                                  
2026-01-22T16:06:59.7457207Z Downloaded from central: https://repo.maven.apache.org/maven2/org/freemarker/freemarker/2.3.32/freemarker-2.3.32.jar (1.7 MB at 2.0 MB/s)
2026-01-22T16:06:59.7457622Z Progress (1): 1.8/2.0 MB
2026-01-22T16:06:59.7457911Z Progress (1): 1.8/2.0 MB
2026-01-22T16:06:59.7458213Z Progress (1): 1.8/2.0 MB
2026-01-22T16:06:59.7458531Z Progress (1): 1.8/2.0 MB
2026-01-22T16:06:59.7458843Z Progress (1): 1.9/2.0 MB
2026-01-22T16:06:59.7459296Z Progress (1): 1.9/2.0 MB
2026-01-22T16:06:59.7466922Z Progress (1): 1.9/2.0 MB
2026-01-22T16:06:59.7467241Z Progress (1): 1.9/2.0 MB
2026-01-22T16:06:59.7467557Z Progress (1): 1.9/2.0 MB
2026-01-22T16:06:59.7467870Z Progress (1): 1.9/2.0 MB
2026-01-22T16:06:59.7468182Z Progress (1): 1.9/2.0 MB
2026-01-22T16:06:59.7468485Z Progress (1): 2.0/2.0 MB
2026-01-22T16:06:59.7468804Z Progress (1): 2.0/2.0 MB
2026-01-22T16:06:59.7469106Z Progress (1): 2.0 MB    
2026-01-22T16:06:59.7469397Z                     
2026-01-22T16:06:59.7469801Z Downloaded from central: https://repo.maven.apache.org/maven2/org/projectlombok/lombok/1.18.26/lombok-1.18.26.jar (2.0 MB at 2.3 MB/s)
2026-01-22T16:06:59.7509815Z Progress (1): 7.7/25 kB
2026-01-22T16:06:59.7512581Z Progress (1): 16/25 kB 
2026-01-22T16:06:59.7519274Z Progress (1): 25 kB   
2026-01-22T16:06:59.7520324Z                    
2026-01-22T16:06:59.7521047Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-cucumber7-jvm/2.29.0/allure-cucumber7-jvm-2.29.0.jar (25 kB at 29 kB/s)
2026-01-22T16:06:59.7573973Z Progress (1): 0/2.4 MB
2026-01-22T16:06:59.7574626Z Progress (1): 0/2.4 MB
2026-01-22T16:06:59.7575548Z Progress (1): 0/2.4 MB
2026-01-22T16:06:59.7576178Z Progress (1): 0/2.4 MB
2026-01-22T16:06:59.7577083Z Progress (1): 0.1/2.4 MB
2026-01-22T16:06:59.7577691Z Progress (1): 0.1/2.4 MB
2026-01-22T16:06:59.7578534Z Progress (1): 0.1/2.4 MB
2026-01-22T16:06:59.7580701Z Progress (1): 0.1/2.4 MB
2026-01-22T16:06:59.7582469Z Progress (1): 0.1/2.4 MB
2026-01-22T16:06:59.7606335Z Progress (1): 0.1/2.4 MB
2026-01-22T16:06:59.7607127Z Progress (1): 0.2/2.4 MB
2026-01-22T16:06:59.7608095Z Progress (1): 0.2/2.4 MB
2026-01-22T16:06:59.7608641Z Progress (1): 0.2/2.4 MB
2026-01-22T16:06:59.7609643Z Progress (1): 0.2/2.4 MB
2026-01-22T16:06:59.7611343Z Progress (1): 0.2/2.4 MB
2026-01-22T16:06:59.7612396Z Progress (1): 0.2/2.4 MB
2026-01-22T16:06:59.7613646Z Progress (1): 0.3/2.4 MB
2026-01-22T16:06:59.7614722Z Progress (1): 0.3/2.4 MB
2026-01-22T16:06:59.7615398Z Progress (1): 0.3/2.4 MB
2026-01-22T16:06:59.7618311Z Progress (1): 0.3/2.4 MB
2026-01-22T16:06:59.7619032Z Progress (1): 0.3/2.4 MB
2026-01-22T16:06:59.7619895Z Progress (1): 0.3/2.4 MB
2026-01-22T16:06:59.7623218Z Progress (1): 0.4/2.4 MB
2026-01-22T16:06:59.7624221Z Progress (1): 0.4/2.4 MB
2026-01-22T16:06:59.7624888Z Progress (1): 0.4/2.4 MB
2026-01-22T16:06:59.7625985Z Progress (1): 0.4/2.4 MB
2026-01-22T16:06:59.7629263Z Progress (1): 0.4/2.4 MB
2026-01-22T16:06:59.7633371Z Progress (1): 0.4/2.4 MB
2026-01-22T16:06:59.7637322Z Progress (1): 0.4/2.4 MB
2026-01-22T16:06:59.7655951Z Progress (1): 0.5/2.4 MB
2026-01-22T16:06:59.7656583Z Progress (1): 0.5/2.4 MB
2026-01-22T16:06:59.7657461Z Progress (1): 0.5/2.4 MB
2026-01-22T16:06:59.7658086Z Progress (1): 0.5/2.4 MB
2026-01-22T16:06:59.7658866Z Progress (1): 0.5/2.4 MB
2026-01-22T16:06:59.7660544Z Progress (1): 0.5/2.4 MB
2026-01-22T16:06:59.7661539Z Progress (1): 0.6/2.4 MB
2026-01-22T16:06:59.7663535Z Progress (1): 0.6/2.4 MB
2026-01-22T16:06:59.7664753Z Progress (1): 0.6/2.4 MB
2026-01-22T16:06:59.7665675Z Progress (1): 0.6/2.4 MB
2026-01-22T16:06:59.7667703Z Progress (1): 0.6/2.4 MB
2026-01-22T16:06:59.7669540Z Progress (1): 0.6/2.4 MB
2026-01-22T16:06:59.7673363Z Progress (1): 0.7/2.4 MB
2026-01-22T16:06:59.7677783Z Progress (1): 0.7/2.4 MB
2026-01-22T16:06:59.7695674Z Progress (1): 0.7/2.4 MB
2026-01-22T16:06:59.7696334Z Progress (1): 0.7/2.4 MB
2026-01-22T16:06:59.7697280Z Progress (1): 0.7/2.4 MB
2026-01-22T16:06:59.7697867Z Progress (1): 0.7/2.4 MB
2026-01-22T16:06:59.7698776Z Progress (1): 0.8/2.4 MB
2026-01-22T16:06:59.7699379Z Progress (1): 0.8/2.4 MB
2026-01-22T16:06:59.7700252Z Progress (2): 0.8/2.4 MB | 7.7/18 kB
2026-01-22T16:06:59.7700885Z Progress (2): 0.8/2.4 MB | 7.7/18 kB
2026-01-22T16:06:59.7701813Z Progress (2): 0.8/2.4 MB | 16/18 kB 
2026-01-22T16:06:59.7702394Z Progress (2): 0.8/2.4 MB | 18 kB   
2026-01-22T16:06:59.7703480Z Progress (2): 0.8/2.4 MB | 18 kB
2026-01-22T16:06:59.7704051Z Progress (2): 0.8/2.4 MB | 18 kB
2026-01-22T16:06:59.7704894Z Progress (2): 0.8/2.4 MB | 18 kB
2026-01-22T16:06:59.7705424Z                                 
2026-01-22T16:06:59.7706809Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-model/2.29.0/allure-model-2.29.0.jar (18 kB at 20 kB/s)
2026-01-22T16:06:59.7711548Z Progress (1): 0.9/2.4 MB
2026-01-22T16:06:59.7716204Z Progress (1): 0.9/2.4 MB
2026-01-22T16:06:59.7720836Z Progress (1): 0.9/2.4 MB
2026-01-22T16:06:59.7725571Z Progress (1): 0.9/2.4 MB
2026-01-22T16:06:59.7745876Z Progress (1): 0.9/2.4 MB
2026-01-22T16:06:59.7746660Z Progress (1): 0.9/2.4 MB
2026-01-22T16:06:59.7747610Z Progress (1): 1.0/2.4 MB
2026-01-22T16:06:59.7748243Z Progress (1): 1.0/2.4 MB
2026-01-22T16:06:59.7749118Z Progress (1): 1.0/2.4 MB
2026-01-22T16:06:59.7749758Z Progress (1): 1.0/2.4 MB
2026-01-22T16:06:59.7750657Z Progress (1): 1.0/2.4 MB
2026-01-22T16:06:59.7751199Z Progress (1): 1.0/2.4 MB
2026-01-22T16:06:59.7752065Z Progress (1): 1.0/2.4 MB
2026-01-22T16:06:59.7752619Z Progress (1): 1.1/2.4 MB
2026-01-22T16:06:59.7755843Z Progress (1): 1.1/2.4 MB
2026-01-22T16:06:59.7756962Z Progress (1): 1.1/2.4 MB
2026-01-22T16:06:59.7760254Z Progress (1): 1.1/2.4 MB
2026-01-22T16:06:59.7760979Z Progress (1): 1.1/2.4 MB
2026-01-22T16:06:59.7761831Z Progress (1): 1.1/2.4 MB
2026-01-22T16:06:59.7765832Z Progress (1): 1.2/2.4 MB
2026-01-22T16:06:59.7769075Z Progress (1): 1.2/2.4 MB
2026-01-22T16:06:59.7785480Z Progress (1): 1.2/2.4 MB
2026-01-22T16:06:59.7786487Z Progress (1): 1.2/2.4 MB
2026-01-22T16:06:59.7787051Z Progress (1): 1.2/2.4 MB
2026-01-22T16:06:59.7787923Z Progress (1): 1.2/2.4 MB
2026-01-22T16:06:59.7788522Z Progress (1): 1.3/2.4 MB
2026-01-22T16:06:59.7789305Z Progress (1): 1.3/2.4 MB
2026-01-22T16:06:59.7791080Z Progress (1): 1.3/2.4 MB
2026-01-22T16:06:59.7793278Z Progress (1): 1.3/2.4 MB
2026-01-22T16:06:59.7795102Z Progress (1): 1.3/2.4 MB
2026-01-22T16:06:59.7796914Z Progress (1): 1.3/2.4 MB
2026-01-22T16:06:59.7800041Z Progress (1): 1.4/2.4 MB
2026-01-22T16:06:59.7804087Z Progress (1): 1.4/2.4 MB
2026-01-22T16:06:59.7807704Z Progress (1): 1.4/2.4 MB
2026-01-22T16:06:59.7826345Z Progress (1): 1.4/2.4 MB
2026-01-22T16:06:59.7826684Z Progress (1): 1.4/2.4 MB
2026-01-22T16:06:59.7826989Z Progress (1): 1.4/2.4 MB
2026-01-22T16:06:59.7827292Z Progress (1): 1.5/2.4 MB
2026-01-22T16:06:59.7827591Z Progress (1): 1.5/2.4 MB
2026-01-22T16:06:59.7828040Z Progress (1): 1.5/2.4 MB
2026-01-22T16:06:59.7828335Z Progress (1): 1.5/2.4 MB
2026-01-22T16:06:59.7828639Z Progress (1): 1.5/2.4 MB
2026-01-22T16:06:59.7828933Z Progress (1): 1.5/2.4 MB
2026-01-22T16:06:59.7829232Z Progress (1): 1.6/2.4 MB
2026-01-22T16:06:59.7829528Z Progress (1): 1.6/2.4 MB
2026-01-22T16:06:59.7829822Z Progress (1): 1.6/2.4 MB
2026-01-22T16:06:59.7830123Z Progress (1): 1.6/2.4 MB
2026-01-22T16:06:59.7833432Z Progress (1): 1.6/2.4 MB
2026-01-22T16:06:59.7837500Z Progress (1): 1.6/2.4 MB
2026-01-22T16:06:59.7841620Z Progress (1): 1.7/2.4 MB
2026-01-22T16:06:59.7845991Z Progress (1): 1.7/2.4 MB
2026-01-22T16:06:59.7850188Z Progress (1): 1.7/2.4 MB
2026-01-22T16:06:59.7854520Z Progress (1): 1.7/2.4 MB
2026-01-22T16:06:59.7858636Z Progress (1): 1.7/2.4 MB
2026-01-22T16:06:59.7875680Z Progress (1): 1.7/2.4 MB
2026-01-22T16:06:59.7876296Z Progress (1): 1.8/2.4 MB
2026-01-22T16:06:59.7877302Z Progress (1): 1.8/2.4 MB
2026-01-22T16:06:59.7878486Z Progress (1): 1.8/2.4 MB
2026-01-22T16:06:59.7879386Z Progress (1): 1.8/2.4 MB
2026-01-22T16:06:59.7879917Z Progress (1): 1.8/2.4 MB
2026-01-22T16:06:59.7880767Z Progress (1): 1.8/2.4 MB
2026-01-22T16:06:59.7881371Z Progress (1): 1.9/2.4 MB
2026-01-22T16:06:59.7882166Z Progress (1): 1.9/2.4 MB
2026-01-22T16:06:59.7884237Z Progress (1): 1.9/2.4 MB
2026-01-22T16:06:59.7884910Z Progress (1): 1.9/2.4 MB
2026-01-22T16:06:59.7887997Z Progress (1): 1.9/2.4 MB
2026-01-22T16:06:59.7891244Z Progress (1): 1.9/2.4 MB
2026-01-22T16:06:59.7895535Z Progress (1): 1.9/2.4 MB
2026-01-22T16:06:59.7899688Z Progress (1): 2.0/2.4 MB
2026-01-22T16:06:59.7904232Z Progress (1): 2.0/2.4 MB
2026-01-22T16:06:59.7926190Z Progress (1): 2.0/2.4 MB
2026-01-22T16:06:59.7926842Z Progress (1): 2.0/2.4 MB
2026-01-22T16:06:59.7927812Z Progress (1): 2.0/2.4 MB
2026-01-22T16:06:59.7928376Z Progress (1): 2.0/2.4 MB
2026-01-22T16:06:59.7929260Z Progress (1): 2.1/2.4 MB
2026-01-22T16:06:59.7929883Z Progress (1): 2.1/2.4 MB
2026-01-22T16:06:59.7930673Z Progress (1): 2.1/2.4 MB
2026-01-22T16:06:59.7932315Z Progress (1): 2.1/2.4 MB
2026-01-22T16:06:59.7933134Z Progress (1): 2.1/2.4 MB
2026-01-22T16:06:59.7933968Z Progress (1): 2.1/2.4 MB
2026-01-22T16:06:59.7936000Z Progress (1): 2.2/2.4 MB
2026-01-22T16:06:59.7938055Z Progress (1): 2.2/2.4 MB
2026-01-22T16:06:59.7940088Z Progress (1): 2.2/2.4 MB
2026-01-22T16:06:59.7943245Z Progress (1): 2.2/2.4 MB
2026-01-22T16:06:59.7944324Z Progress (1): 2.2/2.4 MB
2026-01-22T16:06:59.7947583Z Progress (1): 2.2/2.4 MB
2026-01-22T16:06:59.7948260Z Progress (1): 2.3/2.4 MB
2026-01-22T16:06:59.7949139Z Progress (1): 2.3/2.4 MB
2026-01-22T16:06:59.7952038Z Progress (1): 2.3/2.4 MB
2026-01-22T16:06:59.7955869Z Progress (1): 2.3/2.4 MB
2026-01-22T16:06:59.7959112Z Progress (1): 2.3/2.4 MB
2026-01-22T16:06:59.7973696Z Progress (1): 2.3/2.4 MB
2026-01-22T16:06:59.7976413Z Progress (1): 2.3/2.4 MB
2026-01-22T16:06:59.7979093Z Progress (1): 2.4/2.4 MB
2026-01-22T16:06:59.7981714Z Progress (1): 2.4/2.4 MB
2026-01-22T16:06:59.7985277Z Progress (1): 2.4/2.4 MB
2026-01-22T16:06:59.7987836Z Progress (1): 2.4/2.4 MB
2026-01-22T16:06:59.7990334Z Progress (1): 2.4/2.4 MB
2026-01-22T16:06:59.7992639Z Progress (1): 2.4 MB    
2026-01-22T16:06:59.7995921Z                     
2026-01-22T16:06:59.7997029Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-java-commons/2.29.0/allure-java-commons-2.29.0.jar (2.4 MB at 2.7 MB/s)
2026-01-22T16:06:59.8403854Z [INFO] 
2026-01-22T16:06:59.8404653Z [INFO] --- clean:3.2.0:clean (default-clean) @ EpturaEngageAutomation-Android ---
2026-01-22T16:06:59.8439762Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.3.4/maven-shared-utils-3.3.4.pom
2026-01-22T16:06:59.8700594Z Progress (1): 787 B
2026-01-22T16:06:59.8701454Z Progress (1): 2.3 kB
2026-01-22T16:06:59.8720837Z Progress (1): 4.3 kB
2026-01-22T16:06:59.8721648Z Progress (1): 5.8 kB
2026-01-22T16:06:59.8722880Z                     
2026-01-22T16:06:59.8725193Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.3.4/maven-shared-utils-3.3.4.pom (5.8 kB at 224 kB/s)
2026-01-22T16:06:59.8727895Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/34/maven-shared-components-34.pom
2026-01-22T16:06:59.8937047Z Progress (1): 798 B
2026-01-22T16:06:59.8939288Z Progress (1): 2.3 kB
2026-01-22T16:06:59.8939880Z Progress (1): 4.6 kB
2026-01-22T16:06:59.8943011Z Progress (1): 5.1 kB
2026-01-22T16:06:59.8943690Z                     
2026-01-22T16:06:59.8944905Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/34/maven-shared-components-34.pom (5.1 kB at 222 kB/s)
2026-01-22T16:06:59.8968840Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/34/maven-parent-34.pom
2026-01-22T16:06:59.9223163Z Progress (1): 721 B
2026-01-22T16:06:59.9226185Z Progress (1): 1.9 kB
2026-01-22T16:06:59.9229010Z Progress (1): 5.4 kB
2026-01-22T16:06:59.9233875Z Progress (1): 9.8 kB
2026-01-22T16:06:59.9234519Z Progress (1): 14 kB 
2026-01-22T16:06:59.9235440Z Progress (1): 19 kB
2026-01-22T16:06:59.9235985Z Progress (1): 23 kB
2026-01-22T16:06:59.9236890Z Progress (1): 26 kB
2026-01-22T16:06:59.9237419Z Progress (1): 27 kB
2026-01-22T16:06:59.9238284Z Progress (1): 30 kB
2026-01-22T16:06:59.9238801Z Progress (1): 34 kB
2026-01-22T16:06:59.9239702Z Progress (1): 37 kB
2026-01-22T16:06:59.9240217Z Progress (1): 40 kB
2026-01-22T16:06:59.9241073Z Progress (1): 43 kB
2026-01-22T16:06:59.9241627Z                    
2026-01-22T16:06:59.9242617Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/34/maven-parent-34.pom (43 kB at 1.6 MB/s)
2026-01-22T16:06:59.9277027Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.6/commons-io-2.6.pom
2026-01-22T16:06:59.9515217Z Progress (1): 774 B
2026-01-22T16:06:59.9518542Z Progress (1): 2.1 kB
2026-01-22T16:06:59.9524605Z Progress (1): 5.3 kB
2026-01-22T16:06:59.9525646Z Progress (1): 7.4 kB
2026-01-22T16:06:59.9526578Z Progress (1): 9.4 kB
2026-01-22T16:06:59.9527707Z Progress (1): 12 kB 
2026-01-22T16:06:59.9528308Z Progress (1): 14 kB
2026-01-22T16:06:59.9529267Z                    
2026-01-22T16:06:59.9529961Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.6/commons-io-2.6.pom (14 kB at 594 kB/s)
2026-01-22T16:06:59.9563509Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/42/commons-parent-42.pom
2026-01-22T16:06:59.9805825Z Progress (1): 707 B
2026-01-22T16:06:59.9807043Z Progress (1): 1.9 kB
2026-01-22T16:06:59.9807908Z Progress (1): 3.1 kB
2026-01-22T16:06:59.9808936Z Progress (1): 4.5 kB
2026-01-22T16:06:59.9809448Z Progress (1): 5.9 kB
2026-01-22T16:06:59.9809907Z Progress (1): 7.5 kB
2026-01-22T16:06:59.9810384Z Progress (1): 11 kB 
2026-01-22T16:06:59.9811270Z Progress (1): 14 kB
2026-01-22T16:06:59.9811733Z Progress (1): 17 kB
2026-01-22T16:06:59.9812184Z Progress (1): 20 kB
2026-01-22T16:06:59.9815001Z Progress (1): 23 kB
2026-01-22T16:06:59.9815342Z Progress (1): 26 kB
2026-01-22T16:06:59.9815658Z Progress (1): 29 kB
2026-01-22T16:06:59.9815971Z Progress (1): 31 kB
2026-01-22T16:06:59.9816274Z Progress (1): 34 kB
2026-01-22T16:06:59.9816590Z Progress (1): 34 kB
2026-01-22T16:06:59.9816889Z Progress (1): 37 kB
2026-01-22T16:06:59.9817397Z Progress (1): 40 kB
2026-01-22T16:06:59.9817701Z Progress (1): 44 kB
2026-01-22T16:06:59.9818010Z Progress (1): 48 kB
2026-01-22T16:06:59.9818282Z Progress (1): 53 kB
2026-01-22T16:06:59.9818556Z Progress (1): 55 kB
2026-01-22T16:06:59.9824507Z Progress (1): 59 kB
2026-01-22T16:06:59.9824847Z Progress (1): 60 kB
2026-01-22T16:06:59.9825161Z Progress (1): 62 kB
2026-01-22T16:06:59.9825468Z Progress (1): 65 kB
2026-01-22T16:06:59.9825787Z Progress (1): 66 kB
2026-01-22T16:06:59.9826092Z Progress (1): 68 kB
2026-01-22T16:06:59.9826387Z                    
2026-01-22T16:06:59.9826797Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/42/commons-parent-42.pom (68 kB at 2.3 MB/s)
2026-01-22T16:06:59.9855113Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/18/apache-18.pom
2026-01-22T16:07:00.0043435Z Progress (1): 745 B
2026-01-22T16:07:00.0046476Z Progress (1): 2.1 kB
2026-01-22T16:07:00.0049934Z Progress (1): 3.9 kB
2026-01-22T16:07:00.0051969Z Progress (1): 8.0 kB
2026-01-22T16:07:00.0054143Z Progress (1): 12 kB 
2026-01-22T16:07:00.0056035Z Progress (1): 14 kB
2026-01-22T16:07:00.0057960Z Progress (1): 16 kB
2026-01-22T16:07:00.0059537Z                    
2026-01-22T16:07:00.0060502Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/18/apache-18.pom (16 kB at 783 kB/s)
2026-01-22T16:07:00.0100873Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.3.4/maven-shared-utils-3.3.4.jar
2026-01-22T16:07:00.0101443Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.6/commons-io-2.6.jar
2026-01-22T16:07:00.0316948Z Progress (1): 7.7/153 kB
2026-01-22T16:07:00.0318516Z Progress (1): 16/153 kB 
2026-01-22T16:07:00.0319826Z Progress (1): 32/153 kB
2026-01-22T16:07:00.0329670Z Progress (1): 49/153 kB
2026-01-22T16:07:00.0330069Z Progress (1): 65/153 kB
2026-01-22T16:07:00.0331516Z Progress (1): 81/153 kB
2026-01-22T16:07:00.0333364Z Progress (1): 98/153 kB
2026-01-22T16:07:00.0333749Z Progress (1): 114/153 kB
2026-01-22T16:07:00.0334085Z Progress (1): 131/153 kB
2026-01-22T16:07:00.0334389Z Progress (1): 147/153 kB
2026-01-22T16:07:00.0334697Z Progress (1): 153 kB    
2026-01-22T16:07:00.0335000Z                     
2026-01-22T16:07:00.0335463Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.3.4/maven-shared-utils-3.3.4.jar (153 kB at 6.4 MB/s)
2026-01-22T16:07:00.0413565Z Progress (1): 7.7/215 kB
2026-01-22T16:07:00.0414717Z Progress (1): 16/215 kB 
2026-01-22T16:07:00.0416700Z Progress (1): 32/215 kB
2026-01-22T16:07:00.0418726Z Progress (1): 48/215 kB
2026-01-22T16:07:00.0420716Z Progress (1): 65/215 kB
2026-01-22T16:07:00.0422941Z Progress (1): 81/215 kB
2026-01-22T16:07:00.0425129Z Progress (1): 98/215 kB
2026-01-22T16:07:00.0427252Z Progress (1): 114/215 kB
2026-01-22T16:07:00.0427774Z Progress (1): 130/215 kB
2026-01-22T16:07:00.0428226Z Progress (1): 147/215 kB
2026-01-22T16:07:00.0428649Z Progress (1): 163/215 kB
2026-01-22T16:07:00.0429099Z Progress (1): 180/215 kB
2026-01-22T16:07:00.0429523Z Progress (1): 196/215 kB
2026-01-22T16:07:00.0429929Z Progress (1): 212/215 kB
2026-01-22T16:07:00.0430346Z Progress (1): 215 kB    
2026-01-22T16:07:00.0430733Z                     
2026-01-22T16:07:00.0431245Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.6/commons-io-2.6.jar (215 kB at 6.5 MB/s)
2026-01-22T16:07:00.1803800Z [INFO] Deleting /home/vsts/work/1/s/target
2026-01-22T16:07:00.1804776Z [INFO] 
2026-01-22T16:07:00.1813466Z [INFO] --- resources:3.3.1:resources (default-resources) @ EpturaEngageAutomation-Android ---
2026-01-22T16:07:00.1850177Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.pom
2026-01-22T16:07:00.2085258Z Progress (1): 1.4 kB
2026-01-22T16:07:00.2091436Z Progress (1): 2.7 kB
2026-01-22T16:07:00.2095168Z                     
2026-01-22T16:07:00.2097414Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.pom (2.7 kB at 106 kB/s)
2026-01-22T16:07:00.2106732Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/5.1/plexus-5.1.pom
2026-01-22T16:07:00.2298717Z Progress (1): 697 B
2026-01-22T16:07:00.2304311Z Progress (1): 2.7 kB
2026-01-22T16:07:00.2304689Z Progress (1): 6.4 kB
2026-01-22T16:07:00.2305956Z Progress (1): 9.1 kB
2026-01-22T16:07:00.2306300Z Progress (1): 11 kB 
2026-01-22T16:07:00.2306843Z Progress (1): 16 kB
2026-01-22T16:07:00.2307183Z Progress (1): 20 kB
2026-01-22T16:07:00.2309708Z Progress (1): 23 kB
2026-01-22T16:07:00.2312055Z                    
2026-01-22T16:07:00.2312553Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/5.1/plexus-5.1.pom (23 kB at 1.1 MB/s)
2026-01-22T16:07:00.2341305Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.pom
2026-01-22T16:07:00.2547186Z Progress (1): 725 B
2026-01-22T16:07:00.2551489Z Progress (1): 2.4 kB
2026-01-22T16:07:00.2558195Z Progress (1): 4.4 kB
2026-01-22T16:07:00.2558517Z Progress (1): 8.5 kB
2026-01-22T16:07:00.2565278Z Progress (1): 8.8 kB
2026-01-22T16:07:00.2566885Z                     
2026-01-22T16:07:00.2568470Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.pom (8.8 kB at 365 kB/s)
2026-01-22T16:07:00.2593886Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/10/plexus-10.pom
2026-01-22T16:07:00.2813700Z Progress (1): 700 B
2026-01-22T16:07:00.2816115Z Progress (1): 2.7 kB
2026-01-22T16:07:00.2818291Z Progress (1): 6.4 kB
2026-01-22T16:07:00.2818846Z Progress (1): 9.2 kB
2026-01-22T16:07:00.2820323Z Progress (1): 11 kB 
2026-01-22T16:07:00.2821837Z Progress (1): 15 kB
2026-01-22T16:07:00.2822458Z Progress (1): 20 kB
2026-01-22T16:07:00.2824348Z Progress (1): 24 kB
2026-01-22T16:07:00.2824872Z Progress (1): 25 kB
2026-01-22T16:07:00.2826386Z                    
2026-01-22T16:07:00.2826953Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/10/plexus-10.pom (25 kB at 1.2 MB/s)
2026-01-22T16:07:00.2831552Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.3.1/maven-filtering-3.3.1.pom
2026-01-22T16:07:00.3114287Z Progress (1): 799 B
2026-01-22T16:07:00.3116388Z Progress (1): 2.3 kB
2026-01-22T16:07:00.3116708Z Progress (1): 5.6 kB
2026-01-22T16:07:00.3117040Z Progress (1): 6.0 kB
2026-01-22T16:07:00.3117324Z                     
2026-01-22T16:07:00.3117753Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.3.1/maven-filtering-3.3.1.pom (6.0 kB at 224 kB/s)
2026-01-22T16:07:00.3124082Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/39/maven-shared-components-39.pom
2026-01-22T16:07:00.3355468Z Progress (1): 812 B
2026-01-22T16:07:00.3356089Z Progress (1): 2.2 kB
2026-01-22T16:07:00.3364008Z Progress (1): 3.2 kB
2026-01-22T16:07:00.3373504Z                     
2026-01-22T16:07:00.3374258Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/39/maven-shared-components-39.pom (3.2 kB at 124 kB/s)
2026-01-22T16:07:00.3414424Z Downloading from central: https://repo.maven.apache.org/maven2/javax/inject/javax.inject/1/javax.inject-1.pom
2026-01-22T16:07:00.3614111Z Progress (1): 612 B
2026-01-22T16:07:00.3618381Z                    
2026-01-22T16:07:00.3619174Z Downloaded from central: https://repo.maven.apache.org/maven2/javax/inject/javax.inject/1/javax.inject-1.pom (612 B at 29 kB/s)
2026-01-22T16:07:00.3639662Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.pom
2026-01-22T16:07:00.3870872Z Progress (1): 1.0 kB
2026-01-22T16:07:00.3871489Z Progress (1): 2.7 kB
2026-01-22T16:07:00.3874444Z                     
2026-01-22T16:07:00.3876466Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.pom (2.7 kB at 125 kB/s)
2026-01-22T16:07:00.3884194Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.36/slf4j-parent-1.7.36.pom
2026-01-22T16:07:00.4094284Z Progress (1): 1.0 kB
2026-01-22T16:07:00.4095296Z Progress (1): 3.0 kB
2026-01-22T16:07:00.4095708Z Progress (1): 5.9 kB
2026-01-22T16:07:00.4096109Z Progress (1): 8.7 kB
2026-01-22T16:07:00.4096762Z Progress (1): 12 kB 
2026-01-22T16:07:00.4098946Z Progress (1): 14 kB
2026-01-22T16:07:00.4102936Z                    
2026-01-22T16:07:00.4104731Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.36/slf4j-parent-1.7.36.pom (14 kB at 613 kB/s)
2026-01-22T16:07:00.4117548Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.pom
2026-01-22T16:07:00.4394424Z Progress (1): 910 B
2026-01-22T16:07:00.4401231Z Progress (1): 3.2 kB
2026-01-22T16:07:00.4404413Z                     
2026-01-22T16:07:00.4404911Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.pom (3.2 kB at 110 kB/s)
2026-01-22T16:07:00.4421675Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/15/spice-parent-15.pom
2026-01-22T16:07:00.4663700Z Progress (1): 1.2 kB
2026-01-22T16:07:00.4665392Z Progress (1): 3.7 kB
2026-01-22T16:07:00.4666174Z Progress (1): 7.3 kB
2026-01-22T16:07:00.4667819Z Progress (1): 8.4 kB
2026-01-22T16:07:00.4668452Z                     
2026-01-22T16:07:00.4669403Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/15/spice-parent-15.pom (8.4 kB at 334 kB/s)
2026-01-22T16:07:00.4682367Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/5/forge-parent-5.pom
2026-01-22T16:07:00.4938196Z Progress (1): 1.3 kB
2026-01-22T16:07:00.4940685Z Progress (1): 5.5 kB
2026-01-22T16:07:00.4944257Z Progress (1): 8.4 kB
2026-01-22T16:07:00.4945456Z                     
2026-01-22T16:07:00.4946377Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/5/forge-parent-5.pom (8.4 kB at 322 kB/s)
2026-01-22T16:07:00.4968643Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.0/plexus-utils-3.5.0.pom
2026-01-22T16:07:00.5183480Z Progress (1): 725 B
2026-01-22T16:07:00.5184191Z Progress (1): 2.4 kB
2026-01-22T16:07:00.5185277Z Progress (1): 4.5 kB
2026-01-22T16:07:00.5185921Z Progress (1): 8.0 kB
2026-01-22T16:07:00.5186963Z                     
2026-01-22T16:07:00.5187701Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.0/plexus-utils-3.5.0.pom (8.0 kB at 382 kB/s)
2026-01-22T16:07:00.5203401Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.11.0/commons-io-2.11.0.pom
2026-01-22T16:07:00.5413788Z Progress (1): 760 B
2026-01-22T16:07:00.5415670Z Progress (1): 2.1 kB
2026-01-22T16:07:00.5416726Z Progress (1): 5.2 kB
2026-01-22T16:07:00.5417703Z Progress (1): 7.6 kB
2026-01-22T16:07:00.5418467Z Progress (1): 10 kB 
2026-01-22T16:07:00.5422373Z Progress (1): 12 kB
2026-01-22T16:07:00.5423250Z Progress (1): 15 kB
2026-01-22T16:07:00.5424207Z Progress (1): 18 kB
2026-01-22T16:07:00.5426016Z Progress (1): 20 kB
2026-01-22T16:07:00.5443319Z                    
2026-01-22T16:07:00.5444969Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.11.0/commons-io-2.11.0.pom (20 kB at 858 kB/s)
2026-01-22T16:07:00.5450316Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/52/commons-parent-52.pom
2026-01-22T16:07:00.5716971Z Progress (1): 702 B
2026-01-22T16:07:00.5738127Z Progress (1): 1.8 kB
2026-01-22T16:07:00.5738811Z Progress (1): 3.1 kB
2026-01-22T16:07:00.5740079Z Progress (1): 4.6 kB
2026-01-22T16:07:00.5740736Z Progress (1): 6.7 kB
2026-01-22T16:07:00.5743675Z Progress (1): 8.1 kB
2026-01-22T16:07:00.5744008Z Progress (1): 10 kB 
2026-01-22T16:07:00.5744322Z Progress (1): 12 kB
2026-01-22T16:07:00.5744619Z Progress (1): 15 kB
2026-01-22T16:07:00.5744921Z Progress (1): 17 kB
2026-01-22T16:07:00.5745222Z Progress (1): 20 kB
2026-01-22T16:07:00.5745516Z Progress (1): 22 kB
2026-01-22T16:07:00.5745813Z Progress (1): 25 kB
2026-01-22T16:07:00.5746102Z Progress (1): 29 kB
2026-01-22T16:07:00.5746581Z Progress (1): 32 kB
2026-01-22T16:07:00.5746873Z Progress (1): 32 kB
2026-01-22T16:07:00.5747178Z Progress (1): 36 kB
2026-01-22T16:07:00.5747466Z Progress (1): 39 kB
2026-01-22T16:07:00.5747764Z Progress (1): 42 kB
2026-01-22T16:07:00.5748050Z Progress (1): 44 kB
2026-01-22T16:07:00.5748353Z Progress (1): 47 kB
2026-01-22T16:07:00.5748641Z Progress (1): 51 kB
2026-01-22T16:07:00.5748949Z Progress (1): 54 kB
2026-01-22T16:07:00.5749244Z Progress (1): 56 kB
2026-01-22T16:07:00.5749539Z Progress (1): 61 kB
2026-01-22T16:07:00.5749826Z Progress (1): 65 kB
2026-01-22T16:07:00.5750125Z Progress (1): 73 kB
2026-01-22T16:07:00.5750412Z Progress (1): 75 kB
2026-01-22T16:07:00.5750709Z Progress (1): 79 kB
2026-01-22T16:07:00.5750987Z                    
2026-01-22T16:07:00.5751393Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/52/commons-parent-52.pom (79 kB at 2.7 MB/s)
2026-01-22T16:07:00.5813912Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.7.2/junit-bom-5.7.2.pom
2026-01-22T16:07:00.6043870Z Progress (1): 911 B
2026-01-22T16:07:00.6044219Z Progress (1): 4.1 kB
2026-01-22T16:07:00.6049029Z Progress (1): 5.1 kB
2026-01-22T16:07:00.6057908Z                     
2026-01-22T16:07:00.6058653Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.7.2/junit-bom-5.7.2.pom (5.1 kB at 212 kB/s)
2026-01-22T16:07:00.6085362Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.pom
2026-01-22T16:07:00.6280959Z Progress (1): 728 B
2026-01-22T16:07:00.6285772Z Progress (1): 2.0 kB
2026-01-22T16:07:00.6286428Z Progress (1): 5.2 kB
2026-01-22T16:07:00.6287778Z Progress (1): 8.8 kB
2026-01-22T16:07:00.6288085Z Progress (1): 12 kB 
2026-01-22T16:07:00.6288369Z Progress (1): 15 kB
2026-01-22T16:07:00.6288656Z Progress (1): 17 kB
2026-01-22T16:07:00.6288937Z Progress (1): 18 kB
2026-01-22T16:07:00.6289224Z Progress (1): 21 kB
2026-01-22T16:07:00.6289564Z Progress (1): 24 kB
2026-01-22T16:07:00.6289849Z Progress (1): 27 kB
2026-01-22T16:07:00.6290141Z Progress (1): 30 kB
2026-01-22T16:07:00.6290423Z Progress (1): 31 kB
2026-01-22T16:07:00.6290694Z                    
2026-01-22T16:07:00.6291087Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.pom (31 kB at 1.5 MB/s)
2026-01-22T16:07:00.6342467Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.7.1/junit-bom-5.7.1.pom
2026-01-22T16:07:00.6573586Z Progress (1): 911 B
2026-01-22T16:07:00.6586975Z Progress (1): 4.1 kB
2026-01-22T16:07:00.6587958Z Progress (1): 5.1 kB
2026-01-22T16:07:00.6588485Z                     
2026-01-22T16:07:00.6589843Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.7.1/junit-bom-5.7.1.pom (5.1 kB at 232 kB/s)
2026-01-22T16:07:00.6603309Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.jar
2026-01-22T16:07:00.6607750Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.jar
2026-01-22T16:07:00.6610459Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.3.1/maven-filtering-3.3.1.jar
2026-01-22T16:07:00.6626781Z Downloading from central: https://repo.maven.apache.org/maven2/javax/inject/javax.inject/1/javax.inject-1.jar
2026-01-22T16:07:00.6631062Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar
2026-01-22T16:07:00.6808465Z Progress (1): 2.5 kB
2026-01-22T16:07:00.6808817Z                     
2026-01-22T16:07:00.6809253Z Downloaded from central: https://repo.maven.apache.org/maven2/javax/inject/javax.inject/1/javax.inject-1.jar (2.5 kB at 125 kB/s)
2026-01-22T16:07:00.6809811Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.jar
2026-01-22T16:07:00.6844512Z Progress (1): 7.7/41 kB
2026-01-22T16:07:00.6844846Z Progress (1): 16/41 kB 
2026-01-22T16:07:00.6845144Z Progress (1): 32/41 kB
2026-01-22T16:07:00.6845445Z Progress (1): 41 kB   
2026-01-22T16:07:00.6845721Z                    
2026-01-22T16:07:00.6846116Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar (41 kB at 1.9 MB/s)
2026-01-22T16:07:00.6846628Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar
2026-01-22T16:07:00.6847027Z Progress (1): 7.7/85 kB
2026-01-22T16:07:00.6847326Z Progress (1): 16/85 kB 
2026-01-22T16:07:00.6847625Z Progress (1): 32/85 kB
2026-01-22T16:07:00.6847915Z Progress (1): 49/85 kB
2026-01-22T16:07:00.6848208Z Progress (1): 65/85 kB
2026-01-22T16:07:00.6848490Z Progress (1): 81/85 kB
2026-01-22T16:07:00.6848782Z Progress (1): 85 kB   
2026-01-22T16:07:00.6849052Z                    
2026-01-22T16:07:00.6849481Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.jar (85 kB at 3.4 MB/s)
2026-01-22T16:07:00.6850015Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar
2026-01-22T16:07:00.6895407Z Progress (1): 7.7/269 kB
2026-01-22T16:07:00.6895755Z Progress (1): 8.2/269 kB
2026-01-22T16:07:00.6896063Z Progress (1): 25/269 kB 
2026-01-22T16:07:00.6896361Z Progress (1): 41/269 kB
2026-01-22T16:07:00.6896666Z Progress (1): 57/269 kB
2026-01-22T16:07:00.6896955Z Progress (1): 74/269 kB
2026-01-22T16:07:00.6897256Z Progress (1): 90/269 kB
2026-01-22T16:07:00.6897549Z Progress (1): 106/269 kB
2026-01-22T16:07:00.6897857Z Progress (1): 123/269 kB
2026-01-22T16:07:00.6898154Z Progress (1): 139/269 kB
2026-01-22T16:07:00.6898454Z Progress (1): 156/269 kB
2026-01-22T16:07:00.6898749Z Progress (1): 172/269 kB
2026-01-22T16:07:00.6899064Z Progress (1): 188/269 kB
2026-01-22T16:07:00.6906134Z Progress (1): 205/269 kB
2026-01-22T16:07:00.6906469Z Progress (1): 221/269 kB
2026-01-22T16:07:00.6906764Z Progress (1): 229/269 kB
2026-01-22T16:07:00.6916167Z Progress (1): 246/269 kB
2026-01-22T16:07:00.6916495Z Progress (1): 262/269 kB
2026-01-22T16:07:00.6916837Z Progress (1): 269 kB    
2026-01-22T16:07:00.6917118Z                     
2026-01-22T16:07:00.6917536Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.jar (269 kB at 8.4 MB/s)
2026-01-22T16:07:00.6944149Z Progress (1): 7.7/55 kB
2026-01-22T16:07:00.6944498Z Progress (1): 16/55 kB 
2026-01-22T16:07:00.6944802Z Progress (1): 32/55 kB
2026-01-22T16:07:00.6945111Z Progress (1): 49/55 kB
2026-01-22T16:07:00.6949152Z Progress (1): 55 kB   
2026-01-22T16:07:00.6949475Z                    
2026-01-22T16:07:00.6949892Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.3.1/maven-filtering-3.3.1.jar (55 kB at 1.6 MB/s)
2026-01-22T16:07:00.6978135Z Progress (1): 7.7/8.5 kB
2026-01-22T16:07:00.6980522Z Progress (1): 8.5 kB    
2026-01-22T16:07:00.6980860Z                     
2026-01-22T16:07:00.6981271Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.jar (8.5 kB at 242 kB/s)
2026-01-22T16:07:00.7029598Z Progress (1): 7.7/587 kB
2026-01-22T16:07:00.7029944Z Progress (1): 16/587 kB 
2026-01-22T16:07:00.7030254Z Progress (1): 32/587 kB
2026-01-22T16:07:00.7030571Z Progress (1): 49/587 kB
2026-01-22T16:07:00.7030870Z Progress (1): 65/587 kB
2026-01-22T16:07:00.7031173Z Progress (1): 81/587 kB
2026-01-22T16:07:00.7031464Z Progress (1): 98/587 kB
2026-01-22T16:07:00.7031766Z Progress (1): 114/587 kB
2026-01-22T16:07:00.7032068Z Progress (1): 131/587 kB
2026-01-22T16:07:00.7051452Z Progress (1): 147/587 kB
2026-01-22T16:07:00.7073485Z Progress (1): 163/587 kB
2026-01-22T16:07:00.7097871Z Progress (1): 180/587 kB
2026-01-22T16:07:00.7099089Z Progress (1): 196/587 kB
2026-01-22T16:07:00.7099663Z Progress (1): 213/587 kB
2026-01-22T16:07:00.7107232Z Progress (1): 229/587 kB
2026-01-22T16:07:00.7107555Z Progress (1): 245/587 kB
2026-01-22T16:07:00.7107857Z Progress (1): 262/587 kB
2026-01-22T16:07:00.7108151Z Progress (1): 278/587 kB
2026-01-22T16:07:00.7108449Z Progress (1): 294/587 kB
2026-01-22T16:07:00.7108757Z Progress (1): 311/587 kB
2026-01-22T16:07:00.7109063Z Progress (1): 327/587 kB
2026-01-22T16:07:00.7109357Z Progress (1): 344/587 kB
2026-01-22T16:07:00.7109659Z Progress (1): 360/587 kB
2026-01-22T16:07:00.7109950Z Progress (1): 376/587 kB
2026-01-22T16:07:00.7110247Z Progress (1): 393/587 kB
2026-01-22T16:07:00.7110540Z Progress (1): 409/587 kB
2026-01-22T16:07:00.7110835Z Progress (1): 426/587 kB
2026-01-22T16:07:00.7111122Z Progress (1): 442/587 kB
2026-01-22T16:07:00.7111422Z Progress (1): 458/587 kB
2026-01-22T16:07:00.7111716Z Progress (1): 475/587 kB
2026-01-22T16:07:00.7112019Z Progress (1): 491/587 kB
2026-01-22T16:07:00.7112315Z Progress (1): 507/587 kB
2026-01-22T16:07:00.7112611Z Progress (1): 524/587 kB
2026-01-22T16:07:00.7129713Z Progress (1): 540/587 kB
2026-01-22T16:07:00.7130069Z Progress (2): 540/587 kB | 7.7/327 kB
2026-01-22T16:07:00.7130391Z Progress (2): 540/587 kB | 16/327 kB 
2026-01-22T16:07:00.7130730Z Progress (2): 540/587 kB | 32/327 kB
2026-01-22T16:07:00.7131074Z Progress (2): 540/587 kB | 49/327 kB
2026-01-22T16:07:00.7131400Z Progress (2): 540/587 kB | 65/327 kB
2026-01-22T16:07:00.7131718Z Progress (2): 540/587 kB | 81/327 kB
2026-01-22T16:07:00.7132035Z Progress (2): 540/587 kB | 98/327 kB
2026-01-22T16:07:00.7132347Z Progress (2): 540/587 kB | 114/327 kB
2026-01-22T16:07:00.7132676Z Progress (2): 540/587 kB | 131/327 kB
2026-01-22T16:07:00.7133195Z Progress (2): 540/587 kB | 147/327 kB
2026-01-22T16:07:00.7133524Z Progress (2): 540/587 kB | 163/327 kB
2026-01-22T16:07:00.7133840Z Progress (2): 540/587 kB | 180/327 kB
2026-01-22T16:07:00.7134163Z Progress (2): 540/587 kB | 196/327 kB
2026-01-22T16:07:00.7134483Z Progress (2): 540/587 kB | 213/327 kB
2026-01-22T16:07:00.7135777Z Progress (2): 540/587 kB | 229/327 kB
2026-01-22T16:07:00.7136117Z Progress (2): 557/587 kB | 229/327 kB
2026-01-22T16:07:00.7136447Z Progress (2): 573/587 kB | 229/327 kB
2026-01-22T16:07:00.7136762Z Progress (2): 587 kB | 229/327 kB    
2026-01-22T16:07:00.7137057Z                                  
2026-01-22T16:07:00.7137467Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar (587 kB at 12 MB/s)
2026-01-22T16:07:00.7137895Z Progress (1): 245/327 kB
2026-01-22T16:07:00.7138200Z Progress (1): 262/327 kB
2026-01-22T16:07:00.7138507Z Progress (1): 278/327 kB
2026-01-22T16:07:00.7138801Z Progress (1): 294/327 kB
2026-01-22T16:07:00.7139103Z Progress (1): 311/327 kB
2026-01-22T16:07:00.7139396Z Progress (1): 327 kB    
2026-01-22T16:07:00.7139677Z                     
2026-01-22T16:07:00.7140067Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar (327 kB at 6.5 MB/s)
2026-01-22T16:07:00.8120678Z [INFO] Copying 4 resources from src/main/resources to target/classes
2026-01-22T16:07:00.8154196Z [INFO] 
2026-01-22T16:07:00.8158110Z [INFO] --- compiler:3.11.0:compile (default-compile) @ EpturaEngageAutomation-Android ---
2026-01-22T16:07:00.8201817Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom
2026-01-22T16:07:00.8420316Z Progress (1): 803 B
2026-01-22T16:07:00.8420799Z Progress (1): 2.3 kB
2026-01-22T16:07:00.8444477Z Progress (1): 4.7 kB
2026-01-22T16:07:00.8446545Z                     
2026-01-22T16:07:00.8448332Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom (4.7 kB at 206 kB/s)
2026-01-22T16:07:00.8449778Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom
2026-01-22T16:07:00.8680234Z Progress (1): 773 B
2026-01-22T16:07:00.8680735Z Progress (1): 2.4 kB
2026-01-22T16:07:00.8681174Z Progress (1): 4.2 kB
2026-01-22T16:07:00.8682490Z Progress (1): 6.4 kB
2026-01-22T16:07:00.8684405Z                     
2026-01-22T16:07:00.8684883Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom (6.4 kB at 265 kB/s)
2026-01-22T16:07:00.8695856Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/23/maven-parent-23.pom
2026-01-22T16:07:00.8934840Z Progress (1): 759 B
2026-01-22T16:07:00.8936045Z Progress (1): 2.0 kB
2026-01-22T16:07:00.8937273Z Progress (1): 6.2 kB
2026-01-22T16:07:00.8938459Z Progress (1): 11 kB 
2026-01-22T16:07:00.8965026Z Progress (1): 12 kB
2026-01-22T16:07:00.8965553Z Progress (1): 15 kB
2026-01-22T16:07:00.8965963Z Progress (1): 19 kB
2026-01-22T16:07:00.8966412Z Progress (1): 22 kB
2026-01-22T16:07:00.8966843Z Progress (1): 25 kB
2026-01-22T16:07:00.8967810Z Progress (1): 27 kB
2026-01-22T16:07:00.8968270Z Progress (1): 31 kB
2026-01-22T16:07:00.8968698Z Progress (1): 33 kB
2026-01-22T16:07:00.8969093Z                    
2026-01-22T16:07:00.8969596Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/23/maven-parent-23.pom (33 kB at 1.3 MB/s)
2026-01-22T16:07:00.8970232Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/13/apache-13.pom
2026-01-22T16:07:00.9161159Z Progress (1): 749 B
2026-01-22T16:07:00.9163614Z Progress (1): 2.1 kB
2026-01-22T16:07:00.9167168Z Progress (1): 4.1 kB
2026-01-22T16:07:00.9170269Z Progress (1): 8.9 kB
2026-01-22T16:07:00.9178107Z Progress (1): 11 kB 
2026-01-22T16:07:00.9181194Z Progress (1): 14 kB
2026-01-22T16:07:00.9183319Z                    
2026-01-22T16:07:00.9184907Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/13/apache-13.pom (14 kB at 665 kB/s)
2026-01-22T16:07:00.9210974Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/1.5.5/plexus-component-annotations-1.5.5.pom
2026-01-22T16:07:00.9515127Z Progress (1): 815 B
2026-01-22T16:07:00.9515758Z                    
2026-01-22T16:07:00.9517202Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/1.5.5/plexus-component-annotations-1.5.5.pom (815 B at 27 kB/s)
2026-01-22T16:07:00.9517779Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/1.5.5/plexus-containers-1.5.5.pom
2026-01-22T16:07:00.9723813Z Progress (1): 1.3 kB
2026-01-22T16:07:00.9728599Z Progress (1): 4.2 kB
2026-01-22T16:07:00.9729308Z                     
2026-01-22T16:07:00.9730295Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/1.5.5/plexus-containers-1.5.5.pom (4.2 kB at 202 kB/s)
2026-01-22T16:07:00.9743747Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/2.0.7/plexus-2.0.7.pom
2026-01-22T16:07:00.9989639Z Progress (1): 711 B
2026-01-22T16:07:00.9989985Z Progress (1): 2.7 kB
2026-01-22T16:07:00.9990325Z Progress (1): 6.3 kB
2026-01-22T16:07:00.9992404Z Progress (1): 9.1 kB
2026-01-22T16:07:00.9992923Z Progress (1): 13 kB 
2026-01-22T16:07:00.9993476Z Progress (1): 17 kB
2026-01-22T16:07:00.9996398Z Progress (1): 17 kB
2026-01-22T16:07:00.9997721Z                    
2026-01-22T16:07:00.9998156Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/2.0.7/plexus-2.0.7.pom (17 kB at 692 kB/s)
2026-01-22T16:07:01.0034120Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-java/1.1.2/plexus-java-1.1.2.pom
2026-01-22T16:07:01.0263910Z Progress (1): 1.3 kB
2026-01-22T16:07:01.0264225Z Progress (1): 4.2 kB
2026-01-22T16:07:01.0264566Z Progress (1): 5.0 kB
2026-01-22T16:07:01.0265013Z                     
2026-01-22T16:07:01.0265372Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-java/1.1.2/plexus-java-1.1.2.pom (5.0 kB at 207 kB/s)
2026-01-22T16:07:01.0304548Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-languages/1.1.2/plexus-languages-1.1.2.pom
2026-01-22T16:07:01.0518260Z Progress (1): 1.3 kB
2026-01-22T16:07:01.0521673Z Progress (1): 4.1 kB
2026-01-22T16:07:01.0532163Z                     
2026-01-22T16:07:01.0532615Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-languages/1.1.2/plexus-languages-1.1.2.pom (4.1 kB at 180 kB/s)
2026-01-22T16:07:01.0544776Z Downloading from central: https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.4/asm-9.4.pom
2026-01-22T16:07:01.0783863Z Progress (1): 1.3 kB
2026-01-22T16:07:01.0788355Z Progress (1): 2.4 kB
2026-01-22T16:07:01.0788964Z                     
2026-01-22T16:07:01.0790191Z Downloaded from central: https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.4/asm-9.4.pom (2.4 kB at 99 kB/s)
2026-01-22T16:07:01.0814607Z Downloading from central: https://repo.maven.apache.org/maven2/org/ow2/ow2/1.5.1/ow2-1.5.1.pom
2026-01-22T16:07:01.1083741Z Progress (1): 707 B
2026-01-22T16:07:01.1092332Z Progress (1): 2.1 kB
2026-01-22T16:07:01.1093614Z Progress (1): 3.6 kB
2026-01-22T16:07:01.1094238Z Progress (1): 5.7 kB
2026-01-22T16:07:01.1095193Z Progress (1): 8.0 kB
2026-01-22T16:07:01.1095756Z Progress (1): 11 kB 
2026-01-22T16:07:01.1096630Z                    
2026-01-22T16:07:01.1097281Z Downloaded from central: https://repo.maven.apache.org/maven2/org/ow2/ow2/1.5.1/ow2-1.5.1.pom (11 kB at 470 kB/s)
2026-01-22T16:07:01.1098429Z Downloading from central: https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.pom
2026-01-22T16:07:01.1350150Z Progress (1): 871 B
2026-01-22T16:07:01.1351509Z Progress (1): 3.4 kB
2026-01-22T16:07:01.1351887Z Progress (1): 6.6 kB
2026-01-22T16:07:01.1352282Z Progress (1): 10 kB 
2026-01-22T16:07:01.1352643Z Progress (1): 13 kB
2026-01-22T16:07:01.1356689Z Progress (1): 17 kB
2026-01-22T16:07:01.1357651Z                    
2026-01-22T16:07:01.1358702Z Downloaded from central: https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.pom (17 kB at 638 kB/s)
2026-01-22T16:07:01.1393778Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-api/2.13.0/plexus-compiler-api-2.13.0.pom
2026-01-22T16:07:01.1664564Z Progress (1): 1.1 kB
2026-01-22T16:07:01.1665406Z                     
2026-01-22T16:07:01.1666652Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-api/2.13.0/plexus-compiler-api-2.13.0.pom (1.1 kB at 39 kB/s)
2026-01-22T16:07:01.1683688Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler/2.13.0/plexus-compiler-2.13.0.pom
2026-01-22T16:07:01.1928437Z Progress (1): 1.2 kB
2026-01-22T16:07:01.1929183Z Progress (1): 4.1 kB
2026-01-22T16:07:01.1930097Z Progress (1): 7.3 kB
2026-01-22T16:07:01.1930713Z Progress (1): 8.4 kB
2026-01-22T16:07:01.1931565Z                     
2026-01-22T16:07:01.1932212Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler/2.13.0/plexus-compiler-2.13.0.pom (8.4 kB at 335 kB/s)
2026-01-22T16:07:01.1948428Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/10.0/plexus-components-10.0.pom
2026-01-22T16:07:01.2204497Z Progress (1): 1.3 kB
2026-01-22T16:07:01.2225104Z Progress (1): 2.7 kB
2026-01-22T16:07:01.2225407Z                     
2026-01-22T16:07:01.2225805Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/10.0/plexus-components-10.0.pom (2.7 kB at 103 kB/s)
2026-01-22T16:07:01.2236288Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-manager/2.13.0/plexus-compiler-manager-2.13.0.pom
2026-01-22T16:07:01.2497171Z Progress (1): 1.1 kB
2026-01-22T16:07:01.2497924Z                     
2026-01-22T16:07:01.2499126Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-manager/2.13.0/plexus-compiler-manager-2.13.0.pom (1.1 kB at 44 kB/s)
2026-01-22T16:07:01.2523559Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/2.1.1/plexus-component-annotations-2.1.1.pom
2026-01-22T16:07:01.2815090Z Progress (1): 770 B
2026-01-22T16:07:01.2815666Z                    
2026-01-22T16:07:01.2816223Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/2.1.1/plexus-component-annotations-2.1.1.pom (770 B at 29 kB/s)
2026-01-22T16:07:01.2816923Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/2.1.1/plexus-containers-2.1.1.pom
2026-01-22T16:07:01.3016261Z Progress (1): 1.3 kB
2026-01-22T16:07:01.3047364Z Progress (1): 4.9 kB
2026-01-22T16:07:01.3048494Z Progress (1): 6.0 kB
2026-01-22T16:07:01.3049064Z                     
2026-01-22T16:07:01.3050075Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/2.1.1/plexus-containers-2.1.1.pom (6.0 kB at 262 kB/s)
2026-01-22T16:07:01.3051258Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/6.5/plexus-6.5.pom
2026-01-22T16:07:01.3284534Z Progress (1): 692 B
2026-01-22T16:07:01.3287781Z Progress (1): 2.7 kB
2026-01-22T16:07:01.3290903Z Progress (1): 6.4 kB
2026-01-22T16:07:01.3299809Z Progress (1): 9.2 kB
2026-01-22T16:07:01.3302267Z Progress (1): 11 kB 
2026-01-22T16:07:01.3304033Z Progress (1): 15 kB
2026-01-22T16:07:01.3304900Z Progress (1): 20 kB
2026-01-22T16:07:01.3323615Z Progress (1): 24 kB
2026-01-22T16:07:01.3324662Z Progress (1): 26 kB
2026-01-22T16:07:01.3325049Z                    
2026-01-22T16:07:01.3325519Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/6.5/plexus-6.5.pom (26 kB at 1.0 MB/s)
2026-01-22T16:07:01.3349942Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.13.0/plexus-compiler-javac-2.13.0.pom
2026-01-22T16:07:01.3590590Z Progress (1): 1.2 kB
2026-01-22T16:07:01.3617139Z                     
2026-01-22T16:07:01.3617941Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.13.0/plexus-compiler-javac-2.13.0.pom (1.2 kB at 50 kB/s)
2026-01-22T16:07:01.3619152Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compilers/2.13.0/plexus-compilers-2.13.0.pom
2026-01-22T16:07:01.3848512Z Progress (1): 1.3 kB
2026-01-22T16:07:01.3850647Z                     
2026-01-22T16:07:01.3852574Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compilers/2.13.0/plexus-compilers-2.13.0.pom (1.3 kB at 55 kB/s)
2026-01-22T16:07:01.3914516Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar
2026-01-22T16:07:01.3917692Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/1.5.5/plexus-component-annotations-1.5.5.jar
2026-01-22T16:07:01.3920037Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-java/1.1.2/plexus-java-1.1.2.jar
2026-01-22T16:07:01.3922377Z Downloading from central: https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.4/asm-9.4.jar
2026-01-22T16:07:01.3924302Z Downloading from central: https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.jar
2026-01-22T16:07:01.4085279Z Progress (1): 7.7/14 kB
2026-01-22T16:07:01.4087297Z Progress (1): 12/14 kB 
2026-01-22T16:07:01.4096261Z Progress (1): 14 kB   
2026-01-22T16:07:01.4107303Z                    
2026-01-22T16:07:01.4108508Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar (14 kB at 645 kB/s)
2026-01-22T16:07:01.4109889Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-api/2.13.0/plexus-compiler-api-2.13.0.jar
2026-01-22T16:07:01.4111736Z Progress (1): 7.7/55 kB
2026-01-22T16:07:01.4122558Z Progress (1): 16/55 kB 
2026-01-22T16:07:01.4124455Z Progress (1): 32/55 kB
2026-01-22T16:07:01.4124763Z Progress (1): 49/55 kB
2026-01-22T16:07:01.4125058Z Progress (1): 55 kB   
2026-01-22T16:07:01.4125326Z                    
2026-01-22T16:07:01.4125746Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-java/1.1.2/plexus-java-1.1.2.jar (55 kB at 2.6 MB/s)
2026-01-22T16:07:01.4126285Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.0/plexus-utils-3.5.0.jar
2026-01-22T16:07:01.4126688Z Progress (1): 4.2 kB
2026-01-22T16:07:01.4126980Z                     
2026-01-22T16:07:01.4127440Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/1.5.5/plexus-component-annotations-1.5.5.jar (4.2 kB at 191 kB/s)
2026-01-22T16:07:01.4128047Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-manager/2.13.0/plexus-compiler-manager-2.13.0.jar
2026-01-22T16:07:01.4174911Z Progress (1): 7.7/334 kB
2026-01-22T16:07:01.4175585Z Progress (1): 16/334 kB 
2026-01-22T16:07:01.4178056Z Progress (1): 32/334 kB
2026-01-22T16:07:01.4178375Z Progress (1): 49/334 kB
2026-01-22T16:07:01.4179661Z Progress (1): 61/334 kB
2026-01-22T16:07:01.4180021Z Progress (1): 77/334 kB
2026-01-22T16:07:01.4180819Z Progress (1): 93/334 kB
2026-01-22T16:07:01.4181122Z Progress (1): 110/334 kB
2026-01-22T16:07:01.4181405Z Progress (1): 126/334 kB
2026-01-22T16:07:01.4182161Z Progress (1): 143/334 kB
2026-01-22T16:07:01.4182509Z Progress (1): 159/334 kB
2026-01-22T16:07:01.4182972Z Progress (1): 175/334 kB
2026-01-22T16:07:01.4183287Z Progress (1): 192/334 kB
2026-01-22T16:07:01.4185746Z Progress (1): 208/334 kB
2026-01-22T16:07:01.4193094Z Progress (1): 225/334 kB
2026-01-22T16:07:01.4193544Z Progress (1): 241/334 kB
2026-01-22T16:07:01.4193893Z Progress (1): 257/334 kB
2026-01-22T16:07:01.4194216Z Progress (1): 274/334 kB
2026-01-22T16:07:01.4194545Z Progress (1): 290/334 kB
2026-01-22T16:07:01.4194874Z Progress (1): 306/334 kB
2026-01-22T16:07:01.4196113Z Progress (1): 323/334 kB
2026-01-22T16:07:01.4196537Z Progress (1): 334 kB    
2026-01-22T16:07:01.4196819Z                     
2026-01-22T16:07:01.4197195Z Downloaded from central: https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.jar (334 kB at 12 MB/s)
2026-01-22T16:07:01.4197740Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.13.0/plexus-compiler-javac-2.13.0.jar
2026-01-22T16:07:01.4228701Z Progress (1): 7.7/122 kB
2026-01-22T16:07:01.4234517Z Progress (1): 8.2/122 kB
2026-01-22T16:07:01.4236587Z Progress (1): 25/122 kB 
2026-01-22T16:07:01.4238590Z Progress (1): 41/122 kB
2026-01-22T16:07:01.4240562Z Progress (1): 57/122 kB
2026-01-22T16:07:01.4243307Z Progress (1): 74/122 kB
2026-01-22T16:07:01.4249763Z Progress (1): 82/122 kB
2026-01-22T16:07:01.4252598Z Progress (1): 90/122 kB
2026-01-22T16:07:01.4253882Z Progress (1): 106/122 kB
2026-01-22T16:07:01.4255056Z Progress (1): 115/122 kB
2026-01-22T16:07:01.4255931Z Progress (1): 122 kB    
2026-01-22T16:07:01.4256759Z                     
2026-01-22T16:07:01.4257859Z Downloaded from central: https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.4/asm-9.4.jar (122 kB at 3.6 MB/s)
2026-01-22T16:07:01.4259213Z Progress (1): 7.7/267 kB
2026-01-22T16:07:01.4259546Z Progress (1): 12/267 kB 
2026-01-22T16:07:01.4259875Z Progress (1): 29/267 kB
2026-01-22T16:07:01.4262016Z Progress (1): 45/267 kB
2026-01-22T16:07:01.4265439Z Progress (1): 61/267 kB
2026-01-22T16:07:01.4268236Z Progress (1): 78/267 kB
2026-01-22T16:07:01.4270665Z Progress (1): 94/267 kB
2026-01-22T16:07:01.4273103Z Progress (1): 111/267 kB
2026-01-22T16:07:01.4274812Z Progress (1): 127/267 kB
2026-01-22T16:07:01.4276517Z Progress (1): 143/267 kB
2026-01-22T16:07:01.4278249Z Progress (1): 160/267 kB
2026-01-22T16:07:01.4279136Z Progress (1): 176/267 kB
2026-01-22T16:07:01.4279981Z Progress (1): 193/267 kB
2026-01-22T16:07:01.4280893Z Progress (1): 209/267 kB
2026-01-22T16:07:01.4281579Z Progress (1): 225/267 kB
2026-01-22T16:07:01.4281877Z Progress (1): 229/267 kB
2026-01-22T16:07:01.4282047Z Progress (1): 246/267 kB
2026-01-22T16:07:01.4282214Z Progress (1): 262/267 kB
2026-01-22T16:07:01.4282597Z Progress (1): 267 kB    
2026-01-22T16:07:01.4283618Z                     
2026-01-22T16:07:01.4298640Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.0/plexus-utils-3.5.0.jar (267 kB at 7.4 MB/s)
2026-01-22T16:07:01.4304637Z Progress (1): 7.7/27 kB
2026-01-22T16:07:01.4305992Z Progress (1): 16/27 kB 
2026-01-22T16:07:01.4308363Z Progress (1): 27 kB   
2026-01-22T16:07:01.4309144Z                    
2026-01-22T16:07:01.4309929Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-api/2.13.0/plexus-compiler-api-2.13.0.jar (27 kB at 693 kB/s)
2026-01-22T16:07:01.4336231Z Progress (1): 4.7 kB
2026-01-22T16:07:01.4337579Z                     
2026-01-22T16:07:01.4338899Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-manager/2.13.0/plexus-compiler-manager-2.13.0.jar (4.7 kB at 111 kB/s)
2026-01-22T16:07:01.4424789Z Progress (1): 7.7/23 kB
2026-01-22T16:07:01.4425926Z Progress (1): 12/23 kB 
2026-01-22T16:07:01.4427109Z Progress (1): 23 kB   
2026-01-22T16:07:01.4427408Z                    
2026-01-22T16:07:01.4427847Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.13.0/plexus-compiler-javac-2.13.0.jar (23 kB at 456 kB/s)
2026-01-22T16:07:01.8354323Z [INFO] Changes detected - recompiling the module! :source
2026-01-22T16:07:01.8371236Z [INFO] Compiling 6 source files with javac [debug target 11] to target/classes
2026-01-22T16:07:03.5314731Z [INFO] -------------------------------------------------------------
2026-01-22T16:07:03.5324505Z [ERROR] COMPILATION ERROR : 
2026-01-22T16:07:03.5324888Z [INFO] -------------------------------------------------------------
2026-01-22T16:07:03.5325352Z [ERROR] /home/vsts/work/1/s/src/main/java/com/client/app/pages/LoginPage.java:[1,1] illegal character: '\ufeff'
2026-01-22T16:07:03.5325843Z [ERROR] /home/vsts/work/1/s/src/main/java/com/client/app/pages/LoginPage.java:[1,10] class, interface, or enum expected
2026-01-22T16:07:03.5326270Z [INFO] 2 errors 
2026-01-22T16:07:03.5326835Z [INFO] -------------------------------------------------------------
2026-01-22T16:07:03.5327738Z [INFO] ------------------------------------------------------------------------
2026-01-22T16:07:03.5328526Z [INFO] BUILD FAILURE
2026-01-22T16:07:03.5329337Z [INFO] ------------------------------------------------------------------------
2026-01-22T16:07:03.5345675Z [INFO] Total time:  17.242 s
2026-01-22T16:07:03.5364286Z [INFO] Finished at: 2026-01-22T16:07:03Z
2026-01-22T16:07:03.5367222Z [INFO] ------------------------------------------------------------------------
2026-01-22T16:07:03.5369234Z [ERROR] Failed to execute goal org.apache.maven.plugins:maven-compiler-plugin:3.11.0:compile (default-compile) on project EpturaEngageAutomation-Android: Compilation failure: Compilation failure: 
2026-01-22T16:07:03.5371737Z [ERROR] /home/vsts/work/1/s/src/main/java/com/client/app/pages/LoginPage.java:[1,1] illegal character: '\ufeff'
2026-01-22T16:07:03.5372686Z [ERROR] /home/vsts/work/1/s/src/main/java/com/client/app/pages/LoginPage.java:[1,10] class, interface, or enum expected
2026-01-22T16:07:03.5383757Z [ERROR] -> [Help 1]
2026-01-22T16:07:03.5384463Z [ERROR] 
2026-01-22T16:07:03.5385129Z [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2026-01-22T16:07:03.5386152Z [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2026-01-22T16:07:03.5386716Z [ERROR] 
2026-01-22T16:07:03.5387283Z [ERROR] For more information about the errors and possible solutions, please read the following articles:
2026-01-22T16:07:03.5387920Z [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
2026-01-22T16:07:03.5749169Z 
2026-01-22T16:07:03.5769081Z The process '/usr/bin/mvn' failed with exit code 1
2026-01-22T16:07:03.5771663Z Could not retrieve code analysis results - Maven run failed.
2026-01-22T16:07:03.5792276Z ##[error]Build failed.
2026-01-22T16:07:03.5849175Z ##[section]Finishing: Maven Clean Compile