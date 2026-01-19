2026-01-19T16:15:59.9186719Z ##[section]Starting: Run Tests
2026-01-19T16:15:59.9193147Z ==============================================================================
2026-01-19T16:15:59.9193261Z Task         : Maven
2026-01-19T16:15:59.9193337Z Description  : Build, test, and deploy with Apache Maven
2026-01-19T16:15:59.9193429Z Version      : 3.264.1
2026-01-19T16:15:59.9193496Z Author       : Microsoft Corporation
2026-01-19T16:15:59.9193576Z Help         : https://docs.microsoft.com/azure/devops/pipelines/tasks/build/maven
2026-01-19T16:15:59.9193671Z ==============================================================================
2026-01-19T16:16:00.7029542Z [command]/usr/bin/mvn -version
2026-01-19T16:16:03.4148874Z Apache Maven 3.9.12 (848fbb4bf2d427b72bdb2471c22fced7ebd9a7a1)
2026-01-19T16:16:03.4151299Z Maven home: /usr/share/apache-maven-3.9.12
2026-01-19T16:16:03.4153009Z Java version: 11.0.29, vendor: Eclipse Adoptium, runtime: /usr/lib/jvm/temurin-11-jdk-amd64
2026-01-19T16:16:03.4158432Z Default locale: en, platform encoding: UTF-8
2026-01-19T16:16:03.4159207Z OS name: "linux", version: "6.11.0-1018-azure", arch: "amd64", family: "unix"
2026-01-19T16:16:03.4309191Z 
2026-01-19T16:16:03.4375903Z [command]/usr/bin/mvn -f /home/vsts/work/1/s/pom.xml -Dtestng.xml=testng.xml -Dmaven.repo.local=/home/vsts/work/1/.m2/repository test
2026-01-19T16:16:06.2649310Z [INFO] Scanning for projects...
2026-01-19T16:16:06.3807913Z [INFO] 
2026-01-19T16:16:06.3811041Z [INFO] ----------< com.eptura.appium:EpturaEngageAutomation-Android >----------
2026-01-19T16:16:06.3811956Z [INFO] Building EpturaEngageAutomation-Android 0.0.1-SNAPSHOT
2026-01-19T16:16:06.3812525Z [INFO]   from pom.xml
2026-01-19T16:16:06.3813069Z [INFO] --------------------------------[ jar ]---------------------------------
2026-01-19T16:16:07.6697970Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.3.1/maven-resources-plugin-3.3.1.pom
2026-01-19T16:16:08.6977434Z Progress (1): 810 B
2026-01-19T16:16:08.6987163Z Progress (1): 1.8 kB
2026-01-19T16:16:08.6993586Z Progress (1): 3.4 kB
2026-01-19T16:16:08.6993944Z Progress (1): 6.7 kB
2026-01-19T16:16:08.7159847Z Progress (1): 8.2 kB
2026-01-19T16:16:08.7160537Z                     
2026-01-19T16:16:08.7162704Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.3.1/maven-resources-plugin-3.3.1.pom (8.2 kB at 7.7 kB/s)
2026-01-19T16:16:08.8187602Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/39/maven-plugins-39.pom
2026-01-19T16:16:08.8513545Z Progress (1): 763 B
2026-01-19T16:16:08.8514424Z Progress (1): 1.8 kB
2026-01-19T16:16:08.8514965Z Progress (1): 4.2 kB
2026-01-19T16:16:08.8515622Z Progress (1): 6.6 kB
2026-01-19T16:16:08.8525381Z Progress (1): 8.1 kB
2026-01-19T16:16:08.8527840Z                     
2026-01-19T16:16:08.8528297Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-plugins/39/maven-plugins-39.pom (8.1 kB at 219 kB/s)
2026-01-19T16:16:08.8599086Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/39/maven-parent-39.pom
2026-01-19T16:16:08.8857369Z Progress (1): 724 B
2026-01-19T16:16:08.8867469Z Progress (1): 1.6 kB
2026-01-19T16:16:08.8917353Z Progress (1): 4.2 kB
2026-01-19T16:16:08.8918033Z Progress (1): 8.6 kB
2026-01-19T16:16:08.8918497Z Progress (1): 12 kB 
2026-01-19T16:16:08.8919014Z Progress (1): 16 kB
2026-01-19T16:16:08.8919318Z Progress (1): 21 kB
2026-01-19T16:16:08.8920803Z Progress (1): 23 kB
2026-01-19T16:16:08.8922706Z Progress (1): 27 kB
2026-01-19T16:16:08.8927943Z Progress (1): 28 kB
2026-01-19T16:16:08.8967319Z Progress (1): 30 kB
2026-01-19T16:16:08.8968030Z Progress (1): 33 kB
2026-01-19T16:16:08.8968675Z Progress (1): 36 kB
2026-01-19T16:16:08.8969163Z Progress (1): 38 kB
2026-01-19T16:16:08.8969469Z Progress (1): 41 kB
2026-01-19T16:16:08.8969767Z Progress (1): 45 kB
2026-01-19T16:16:08.8970059Z Progress (1): 48 kB
2026-01-19T16:16:08.8970560Z                    
2026-01-19T16:16:08.8970954Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/39/maven-parent-39.pom (48 kB at 1.2 MB/s)
2026-01-19T16:16:08.9068918Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/29/apache-29.pom
2026-01-19T16:16:08.9320260Z Progress (1): 745 B
2026-01-19T16:16:08.9337211Z Progress (1): 1.6 kB
2026-01-19T16:16:08.9337558Z Progress (1): 3.4 kB
2026-01-19T16:16:08.9340852Z Progress (1): 5.6 kB
2026-01-19T16:16:08.9342452Z Progress (1): 8.9 kB
2026-01-19T16:16:08.9360946Z Progress (1): 14 kB 
2026-01-19T16:16:08.9364953Z Progress (1): 17 kB
2026-01-19T16:16:08.9369099Z Progress (1): 19 kB
2026-01-19T16:16:08.9381512Z Progress (1): 21 kB
2026-01-19T16:16:08.9385580Z                    
2026-01-19T16:16:08.9389871Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/29/apache-29.pom (21 kB at 648 kB/s)
2026-01-19T16:16:08.9662072Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.3.1/maven-resources-plugin-3.3.1.jar
2026-01-19T16:16:08.9895866Z Progress (1): 0.9/31 kB
2026-01-19T16:16:08.9896220Z Progress (1): 2.3/31 kB
2026-01-19T16:16:08.9904313Z Progress (1): 3.6/31 kB
2026-01-19T16:16:08.9918683Z Progress (1): 5.0/31 kB
2026-01-19T16:16:08.9924937Z Progress (1): 6.4/31 kB
2026-01-19T16:16:08.9937571Z Progress (1): 7.7/31 kB
2026-01-19T16:16:08.9939674Z Progress (1): 9.1/31 kB
2026-01-19T16:16:08.9984766Z Progress (1): 10/31 kB 
2026-01-19T16:16:08.9985577Z Progress (1): 12/31 kB
2026-01-19T16:16:08.9986124Z Progress (1): 13/31 kB
2026-01-19T16:16:08.9986771Z Progress (1): 15/31 kB
2026-01-19T16:16:09.0017233Z Progress (1): 16/31 kB
2026-01-19T16:16:09.0028190Z Progress (1): 17/31 kB
2026-01-19T16:16:09.0028803Z Progress (1): 19/31 kB
2026-01-19T16:16:09.0029377Z Progress (1): 20/31 kB
2026-01-19T16:16:09.0029879Z Progress (1): 21/31 kB
2026-01-19T16:16:09.0030432Z Progress (1): 23/31 kB
2026-01-19T16:16:09.0030932Z Progress (1): 24/31 kB
2026-01-19T16:16:09.0031407Z Progress (1): 26/31 kB
2026-01-19T16:16:09.0031877Z Progress (1): 27/31 kB
2026-01-19T16:16:09.0097282Z Progress (1): 28/31 kB
2026-01-19T16:16:09.0097986Z Progress (1): 30/31 kB
2026-01-19T16:16:09.0098539Z Progress (1): 31 kB   
2026-01-19T16:16:09.0099203Z                    
2026-01-19T16:16:09.0099873Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-resources-plugin/3.3.1/maven-resources-plugin-3.3.1.jar (31 kB at 720 kB/s)
2026-01-19T16:16:09.0337496Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.11.0/maven-compiler-plugin-3.11.0.pom
2026-01-19T16:16:09.0614218Z Progress (1): 756 B
2026-01-19T16:16:09.0614919Z Progress (1): 1.7 kB
2026-01-19T16:16:09.0619569Z Progress (1): 3.3 kB
2026-01-19T16:16:09.0620119Z Progress (1): 7.0 kB
2026-01-19T16:16:09.0621699Z Progress (1): 8.4 kB
2026-01-19T16:16:09.0638271Z Progress (1): 9.8 kB
2026-01-19T16:16:09.0642201Z                     
2026-01-19T16:16:09.0645705Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.11.0/maven-compiler-plugin-3.11.0.pom (9.8 kB at 327 kB/s)
2026-01-19T16:16:09.0750323Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.11.0/maven-compiler-plugin-3.11.0.jar
2026-01-19T16:16:09.1023730Z Progress (1): 3.8/66 kB
2026-01-19T16:16:09.1041049Z Progress (1): 8.0/66 kB
2026-01-19T16:16:09.1041413Z Progress (1): 12/66 kB 
2026-01-19T16:16:09.1049212Z Progress (1): 16/66 kB
2026-01-19T16:16:09.1071955Z Progress (1): 20/66 kB
2026-01-19T16:16:09.1072790Z Progress (1): 24/66 kB
2026-01-19T16:16:09.1077659Z Progress (1): 28/66 kB
2026-01-19T16:16:09.1118863Z Progress (1): 33/66 kB
2026-01-19T16:16:09.1119592Z Progress (1): 37/66 kB
2026-01-19T16:16:09.1120697Z Progress (1): 41/66 kB
2026-01-19T16:16:09.1139982Z Progress (1): 45/66 kB
2026-01-19T16:16:09.1144187Z Progress (1): 50/66 kB
2026-01-19T16:16:09.1192191Z Progress (1): 54/66 kB
2026-01-19T16:16:09.1192787Z Progress (1): 58/66 kB
2026-01-19T16:16:09.1193343Z Progress (1): 62/66 kB
2026-01-19T16:16:09.1193917Z Progress (1): 66 kB   
2026-01-19T16:16:09.1197715Z                    
2026-01-19T16:16:09.1198562Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-compiler-plugin/3.11.0/maven-compiler-plugin-3.11.0.jar (66 kB at 1.5 MB/s)
2026-01-19T16:16:09.1452069Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/3.0.0-M9/maven-surefire-plugin-3.0.0-M9.pom
2026-01-19T16:16:09.1754169Z Progress (1): 817 B
2026-01-19T16:16:09.1755056Z Progress (1): 3.0 kB
2026-01-19T16:16:09.1757547Z Progress (1): 6.4 kB
2026-01-19T16:16:09.1788671Z Progress (1): 7.2 kB
2026-01-19T16:16:09.1790427Z                     
2026-01-19T16:16:09.1791990Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/3.0.0-M9/maven-surefire-plugin-3.0.0-M9.pom (7.2 kB at 219 kB/s)
2026-01-19T16:16:09.1900141Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire/3.0.0-M9/surefire-3.0.0-M9.pom
2026-01-19T16:16:09.2198398Z Progress (1): 787 B
2026-01-19T16:16:09.2212746Z Progress (1): 2.5 kB
2026-01-19T16:16:09.2214329Z Progress (1): 4.1 kB
2026-01-19T16:16:09.2239696Z Progress (1): 8.2 kB
2026-01-19T16:16:09.2240232Z Progress (1): 12 kB 
2026-01-19T16:16:09.2242353Z Progress (1): 14 kB
2026-01-19T16:16:09.2242885Z Progress (1): 17 kB
2026-01-19T16:16:09.2244728Z Progress (1): 18 kB
2026-01-19T16:16:09.2245320Z Progress (1): 20 kB
2026-01-19T16:16:09.2247780Z Progress (1): 22 kB
2026-01-19T16:16:09.2248268Z                    
2026-01-19T16:16:09.2249792Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire/3.0.0-M9/surefire-3.0.0-M9.pom (22 kB at 602 kB/s)
2026-01-19T16:16:09.2317500Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/36/maven-parent-36.pom
2026-01-19T16:16:09.2604013Z Progress (1): 721 B
2026-01-19T16:16:09.2608088Z Progress (1): 1.9 kB
2026-01-19T16:16:09.2609239Z Progress (1): 5.4 kB
2026-01-19T16:16:09.2609540Z Progress (1): 9.5 kB
2026-01-19T16:16:09.2609841Z Progress (1): 14 kB 
2026-01-19T16:16:09.2610142Z Progress (1): 19 kB
2026-01-19T16:16:09.2615471Z Progress (1): 22 kB
2026-01-19T16:16:09.2652977Z Progress (1): 25 kB
2026-01-19T16:16:09.2655349Z Progress (1): 27 kB
2026-01-19T16:16:09.2655653Z Progress (1): 28 kB
2026-01-19T16:16:09.2655946Z Progress (1): 31 kB
2026-01-19T16:16:09.2656234Z Progress (1): 35 kB
2026-01-19T16:16:09.2656753Z Progress (1): 38 kB
2026-01-19T16:16:09.2657746Z Progress (1): 41 kB
2026-01-19T16:16:09.2685290Z Progress (1): 45 kB
2026-01-19T16:16:09.2707318Z                    
2026-01-19T16:16:09.2709554Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/36/maven-parent-36.pom (45 kB at 1.2 MB/s)
2026-01-19T16:16:09.2776914Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/26/apache-26.pom
2026-01-19T16:16:09.3040869Z Progress (1): 745 B
2026-01-19T16:16:09.3087427Z Progress (1): 2.1 kB
2026-01-19T16:16:09.3088169Z Progress (1): 3.9 kB
2026-01-19T16:16:09.3088777Z Progress (1): 7.3 kB
2026-01-19T16:16:09.3089380Z Progress (1): 12 kB 
2026-01-19T16:16:09.3089912Z Progress (1): 16 kB
2026-01-19T16:16:09.3090396Z Progress (1): 19 kB
2026-01-19T16:16:09.3090878Z Progress (1): 19 kB
2026-01-19T16:16:09.3091351Z Progress (1): 21 kB
2026-01-19T16:16:09.3091813Z                    
2026-01-19T16:16:09.3092464Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/26/apache-26.pom (21 kB at 663 kB/s)
2026-01-19T16:16:09.3256303Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/3.0.0-M9/maven-surefire-plugin-3.0.0-M9.jar
2026-01-19T16:16:09.3527979Z Progress (1): 3.8/44 kB
2026-01-19T16:16:09.3549199Z Progress (1): 8.0/44 kB
2026-01-19T16:16:09.3570587Z Progress (1): 12/44 kB 
2026-01-19T16:16:09.3574416Z Progress (1): 16/44 kB
2026-01-19T16:16:09.3578333Z Progress (1): 21/44 kB
2026-01-19T16:16:09.3615490Z Progress (1): 25/44 kB
2026-01-19T16:16:09.3619561Z Progress (1): 29/44 kB
2026-01-19T16:16:09.3620150Z Progress (1): 33/44 kB
2026-01-19T16:16:09.3620713Z Progress (1): 38/44 kB
2026-01-19T16:16:09.3637419Z Progress (1): 42/44 kB
2026-01-19T16:16:09.3667269Z Progress (1): 44 kB   
2026-01-19T16:16:09.3687233Z                    
2026-01-19T16:16:09.3687888Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/plugins/maven-surefire-plugin/3.0.0-M9/maven-surefire-plugin-3.0.0-M9.jar (44 kB at 1.1 MB/s)
2026-01-19T16:16:09.3970167Z Downloading from central: https://repo.maven.apache.org/maven2/io/appium/java-client/8.6.0/java-client-8.6.0.pom
2026-01-19T16:16:09.4909886Z Progress (1): 958 B
2026-01-19T16:16:09.4938169Z Progress (1): 3.6 kB
2026-01-19T16:16:09.4942237Z                     
2026-01-19T16:16:09.4946377Z Downloaded from central: https://repo.maven.apache.org/maven2/io/appium/java-client/8.6.0/java-client-8.6.0.pom (3.6 kB at 38 kB/s)
2026-01-19T16:16:09.5085512Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/maven-metadata.xml
2026-01-19T16:16:09.5401586Z Progress (1): 4.6 kB
2026-01-19T16:16:09.5420344Z Progress (1): 6.1 kB
2026-01-19T16:16:09.5424243Z                     
2026-01-19T16:16:09.5426202Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/maven-metadata.xml (6.1 kB at 179 kB/s)
2026-01-19T16:16:09.5548796Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.9.1/selenium-api-4.9.1.pom
2026-01-19T16:16:09.5790427Z Progress (1): 1.1 kB
2026-01-19T16:16:09.5791100Z Progress (1): 2.1 kB
2026-01-19T16:16:09.5793148Z                     
2026-01-19T16:16:09.5794159Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.9.1/selenium-api-4.9.1.pom (2.1 kB at 74 kB/s)
2026-01-19T16:16:09.5845407Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.10.0/selenium-api-4.10.0.pom
2026-01-19T16:16:09.6106038Z Progress (1): 1.1 kB
2026-01-19T16:16:09.6106967Z Progress (1): 2.1 kB
2026-01-19T16:16:09.6107505Z                     
2026-01-19T16:16:09.6108140Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.10.0/selenium-api-4.10.0.pom (2.1 kB at 80 kB/s)
2026-01-19T16:16:09.6155850Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.11.0/selenium-api-4.11.0.pom
2026-01-19T16:16:09.6417398Z Progress (1): 1.1 kB
2026-01-19T16:16:09.6418024Z Progress (1): 2.1 kB
2026-01-19T16:16:09.6418473Z                     
2026-01-19T16:16:09.6419039Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.11.0/selenium-api-4.11.0.pom (2.1 kB at 80 kB/s)
2026-01-19T16:16:09.6448406Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.12.0/selenium-api-4.12.0.pom
2026-01-19T16:16:09.6807548Z Progress (1): 1.1 kB
2026-01-19T16:16:09.6819513Z Progress (1): 2.1 kB
2026-01-19T16:16:09.6820148Z                     
2026-01-19T16:16:09.6820853Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.12.0/selenium-api-4.12.0.pom (2.1 kB at 63 kB/s)
2026-01-19T16:16:09.6864687Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.12.1/selenium-api-4.12.1.pom
2026-01-19T16:16:09.7139172Z Progress (1): 1.1 kB
2026-01-19T16:16:09.7139515Z Progress (1): 2.1 kB
2026-01-19T16:16:09.7144850Z                     
2026-01-19T16:16:09.7147143Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.12.1/selenium-api-4.12.1.pom (2.1 kB at 69 kB/s)
2026-01-19T16:16:09.7199435Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.13.0/selenium-api-4.13.0.pom
2026-01-19T16:16:09.7469417Z Progress (1): 1.1 kB
2026-01-19T16:16:09.7509896Z Progress (1): 2.1 kB
2026-01-19T16:16:09.7510358Z                     
2026-01-19T16:16:09.7510967Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.13.0/selenium-api-4.13.0.pom (2.1 kB at 69 kB/s)
2026-01-19T16:16:09.7558405Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/maven-metadata.xml
2026-01-19T16:16:09.7812249Z Progress (1): 4.5 kB
2026-01-19T16:16:09.7840210Z Progress (1): 6.1 kB
2026-01-19T16:16:09.7840543Z                     
2026-01-19T16:16:09.7840973Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/maven-metadata.xml (6.1 kB at 211 kB/s)
2026-01-19T16:16:09.7895924Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.9.1/selenium-remote-driver-4.9.1.pom
2026-01-19T16:16:09.8147973Z Progress (1): 1.0 kB
2026-01-19T16:16:09.8148577Z Progress (1): 6.9 kB
2026-01-19T16:16:09.8179202Z Progress (1): 8.4 kB
2026-01-19T16:16:09.8179658Z                     
2026-01-19T16:16:09.8180223Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.9.1/selenium-remote-driver-4.9.1.pom (8.4 kB at 323 kB/s)
2026-01-19T16:16:09.8217361Z Downloading from central: https://repo.maven.apache.org/maven2/com/beust/jcommander/1.82/jcommander-1.82.pom
2026-01-19T16:16:09.8439980Z Progress (1): 1.0 kB
2026-01-19T16:16:09.8477240Z Progress (1): 1.5 kB
2026-01-19T16:16:09.8477696Z                     
2026-01-19T16:16:09.8478204Z Downloaded from central: https://repo.maven.apache.org/maven2/com/beust/jcommander/1.82/jcommander-1.82.pom (1.5 kB at 60 kB/s)
2026-01-19T16:16:09.8553529Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.0.1/auto-service-annotations-1.0.1.pom
2026-01-19T16:16:09.8831993Z Progress (1): 832 B
2026-01-19T16:16:09.8847880Z Progress (1): 2.3 kB
2026-01-19T16:16:09.8849843Z                     
2026-01-19T16:16:09.8850301Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.0.1/auto-service-annotations-1.0.1.pom (2.3 kB at 76 kB/s)
2026-01-19T16:16:09.8928639Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-aggregator/1.0.1/auto-service-aggregator-1.0.1.pom
2026-01-19T16:16:09.9169044Z Progress (1): 813 B
2026-01-19T16:16:09.9169483Z Progress (1): 2.4 kB
2026-01-19T16:16:09.9184813Z Progress (1): 4.3 kB
2026-01-19T16:16:09.9185761Z                     
2026-01-19T16:16:09.9186456Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-aggregator/1.0.1/auto-service-aggregator-1.0.1.pom (4.3 kB at 152 kB/s)
2026-01-19T16:16:09.9230304Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/oss/oss-parent/7/oss-parent-7.pom
2026-01-19T16:16:09.9437517Z Progress (1): 847 B
2026-01-19T16:16:09.9439112Z Progress (1): 2.5 kB
2026-01-19T16:16:09.9459041Z Progress (1): 4.8 kB
2026-01-19T16:16:09.9459347Z                     
2026-01-19T16:16:09.9459751Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/oss/oss-parent/7/oss-parent-7.pom (4.8 kB at 201 kB/s)
2026-01-19T16:16:09.9559615Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service/1.0.1/auto-service-1.0.1.pom
2026-01-19T16:16:09.9846246Z Progress (1): 821 B
2026-01-19T16:16:09.9847366Z Progress (1): 2.9 kB
2026-01-19T16:16:09.9848099Z Progress (1): 3.1 kB
2026-01-19T16:16:09.9848837Z                     
2026-01-19T16:16:09.9849496Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service/1.0.1/auto-service-1.0.1.pom (3.1 kB at 103 kB/s)
2026-01-19T16:16:09.9945594Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/auto-common/1.2/auto-common-1.2.pom
2026-01-19T16:16:10.0249553Z Progress (1): 811 B
2026-01-19T16:16:10.0257376Z Progress (1): 2.4 kB
2026-01-19T16:16:10.0257723Z Progress (1): 4.4 kB
2026-01-19T16:16:10.0258008Z                     
2026-01-19T16:16:10.0258400Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/auto-common/1.2/auto-common-1.2.pom (4.4 kB at 152 kB/s)
2026-01-19T16:16:10.0340922Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/31.0.1-jre/guava-31.0.1-jre.pom
2026-01-19T16:16:10.0640997Z Progress (1): 1.1 kB
2026-01-19T16:16:10.0641419Z Progress (1): 2.9 kB
2026-01-19T16:16:10.0641802Z Progress (1): 4.9 kB
2026-01-19T16:16:10.0642452Z Progress (1): 6.8 kB
2026-01-19T16:16:10.0642917Z Progress (1): 8.6 kB
2026-01-19T16:16:10.0653091Z Progress (1): 11 kB 
2026-01-19T16:16:10.0655098Z                    
2026-01-19T16:16:10.0683131Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/31.0.1-jre/guava-31.0.1-jre.pom (11 kB at 332 kB/s)
2026-01-19T16:16:10.0747603Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/31.0.1-jre/guava-parent-31.0.1-jre.pom
2026-01-19T16:16:10.0981274Z Progress (1): 903 B
2026-01-19T16:16:10.0983324Z Progress (1): 2.7 kB
2026-01-19T16:16:10.0984269Z Progress (1): 5.2 kB
2026-01-19T16:16:10.0984777Z Progress (1): 7.7 kB
2026-01-19T16:16:10.0985107Z Progress (1): 9.4 kB
2026-01-19T16:16:10.0992770Z Progress (1): 14 kB 
2026-01-19T16:16:10.0997117Z                    
2026-01-19T16:16:10.0999916Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/31.0.1-jre/guava-parent-31.0.1-jre.pom (14 kB at 512 kB/s)
2026-01-19T16:16:10.1066971Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.pom
2026-01-19T16:16:10.1283270Z Progress (1): 981 B
2026-01-19T16:16:10.1289998Z Progress (1): 2.4 kB
2026-01-19T16:16:10.1291831Z                     
2026-01-19T16:16:10.1293549Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.pom (2.4 kB at 105 kB/s)
2026-01-19T16:16:10.1329533Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/26.0-android/guava-parent-26.0-android.pom
2026-01-19T16:16:10.1571385Z Progress (1): 982 B
2026-01-19T16:16:10.1573319Z Progress (1): 2.7 kB
2026-01-19T16:16:10.1573885Z Progress (1): 5.4 kB
2026-01-19T16:16:10.1574502Z Progress (1): 7.4 kB
2026-01-19T16:16:10.1575045Z Progress (1): 10 kB 
2026-01-19T16:16:10.1575329Z                    
2026-01-19T16:16:10.1575746Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/26.0-android/guava-parent-26.0-android.pom (10 kB at 443 kB/s)
2026-01-19T16:16:10.1586232Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/oss/oss-parent/9/oss-parent-9.pom
2026-01-19T16:16:10.1818122Z Progress (1): 835 B
2026-01-19T16:16:10.1818441Z Progress (1): 2.7 kB
2026-01-19T16:16:10.1821111Z Progress (1): 6.2 kB
2026-01-19T16:16:10.1826205Z Progress (1): 6.6 kB
2026-01-19T16:16:10.1829018Z                     
2026-01-19T16:16:10.1829714Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/oss/oss-parent/9/oss-parent-9.pom (6.6 kB at 274 kB/s)
2026-01-19T16:16:10.1920385Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.pom
2026-01-19T16:16:10.2187310Z Progress (1): 1.0 kB
2026-01-19T16:16:10.2202346Z Progress (1): 2.3 kB
2026-01-19T16:16:10.2202688Z                     
2026-01-19T16:16:10.2203212Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.pom (2.3 kB at 91 kB/s)
2026-01-19T16:16:10.2239783Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.pom
2026-01-19T16:16:10.2437062Z Progress (1): 1.0 kB
2026-01-19T16:16:10.2459103Z Progress (1): 3.7 kB
2026-01-19T16:16:10.2459866Z Progress (1): 4.3 kB
2026-01-19T16:16:10.2460470Z                     
2026-01-19T16:16:10.2460885Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.pom (4.3 kB at 195 kB/s)
2026-01-19T16:16:10.2491747Z Downloading from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.12.0/checker-qual-3.12.0.pom
2026-01-19T16:16:10.2705715Z Progress (1): 951 B
2026-01-19T16:16:10.2712089Z Progress (1): 2.1 kB
2026-01-19T16:16:10.2716441Z                     
2026-01-19T16:16:10.2719348Z Downloaded from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.12.0/checker-qual-3.12.0.pom (2.1 kB at 87 kB/s)
2026-01-19T16:16:10.2770651Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.7.1/error_prone_annotations-2.7.1.pom
2026-01-19T16:16:10.2964414Z Progress (1): 835 B
2026-01-19T16:16:10.2971959Z Progress (1): 2.1 kB
2026-01-19T16:16:10.2977130Z                     
2026-01-19T16:16:10.2979493Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.7.1/error_prone_annotations-2.7.1.pom (2.1 kB at 96 kB/s)
2026-01-19T16:16:10.3018555Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.7.1/error_prone_parent-2.7.1.pom
2026-01-19T16:16:10.3250203Z Progress (1): 743 B
2026-01-19T16:16:10.3250564Z Progress (1): 2.4 kB
2026-01-19T16:16:10.3255274Z Progress (1): 4.9 kB
2026-01-19T16:16:10.3256014Z Progress (1): 7.0 kB
2026-01-19T16:16:10.3257118Z                     
2026-01-19T16:16:10.3257877Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.7.1/error_prone_parent-2.7.1.pom (7.0 kB at 268 kB/s)
2026-01-19T16:16:10.3304311Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/1.3/j2objc-annotations-1.3.pom
2026-01-19T16:16:10.3523615Z Progress (1): 857 B
2026-01-19T16:16:10.3533732Z Progress (1): 2.8 kB
2026-01-19T16:16:10.3547313Z                     
2026-01-19T16:16:10.3547836Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/1.3/j2objc-annotations-1.3.pom (2.8 kB at 115 kB/s)
2026-01-19T16:16:10.3585269Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/31.1-jre/guava-31.1-jre.pom
2026-01-19T16:16:10.3819778Z Progress (1): 1.0 kB
2026-01-19T16:16:10.3821422Z Progress (1): 2.9 kB
2026-01-19T16:16:10.3827041Z Progress (1): 4.9 kB
2026-01-19T16:16:10.3827396Z Progress (1): 6.8 kB
2026-01-19T16:16:10.3827715Z Progress (1): 8.5 kB
2026-01-19T16:16:10.3828018Z Progress (1): 11 kB 
2026-01-19T16:16:10.3828316Z                    
2026-01-19T16:16:10.3830425Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/31.1-jre/guava-31.1-jre.pom (11 kB at 458 kB/s)
2026-01-19T16:16:10.3871487Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/31.1-jre/guava-parent-31.1-jre.pom
2026-01-19T16:16:10.4138689Z Progress (1): 913 B
2026-01-19T16:16:10.4139739Z Progress (1): 2.7 kB
2026-01-19T16:16:10.4140216Z Progress (1): 5.2 kB
2026-01-19T16:16:10.4140525Z Progress (1): 7.8 kB
2026-01-19T16:16:10.4140831Z Progress (1): 9.4 kB
2026-01-19T16:16:10.4141122Z Progress (1): 14 kB 
2026-01-19T16:16:10.4141404Z Progress (1): 15 kB
2026-01-19T16:16:10.4141681Z                    
2026-01-19T16:16:10.4142077Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/31.1-jre/guava-parent-31.1-jre.pom (15 kB at 546 kB/s)
2026-01-19T16:16:10.4209988Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.11.0/error_prone_annotations-2.11.0.pom
2026-01-19T16:16:10.4464343Z Progress (1): 835 B
2026-01-19T16:16:10.4474076Z Progress (1): 2.2 kB
2026-01-19T16:16:10.4484550Z                     
2026-01-19T16:16:10.4485184Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.11.0/error_prone_annotations-2.11.0.pom (2.2 kB at 80 kB/s)
2026-01-19T16:16:10.4514578Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.11.0/error_prone_parent-2.11.0.pom
2026-01-19T16:16:10.4765725Z Progress (1): 724 B
2026-01-19T16:16:10.4766074Z Progress (1): 2.2 kB
2026-01-19T16:16:10.4766399Z Progress (1): 4.2 kB
2026-01-19T16:16:10.4766925Z Progress (1): 8.4 kB
2026-01-19T16:16:10.4781074Z Progress (1): 11 kB 
2026-01-19T16:16:10.4781413Z                    
2026-01-19T16:16:10.4781883Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.11.0/error_prone_parent-2.11.0.pom (11 kB at 398 kB/s)
2026-01-19T16:16:10.4841513Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.91.Final/netty-buffer-4.1.91.Final.pom
2026-01-19T16:16:10.5118745Z Progress (1): 885 B
2026-01-19T16:16:10.5125012Z Progress (1): 1.6 kB
2026-01-19T16:16:10.5130108Z                     
2026-01-19T16:16:10.5130928Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.91.Final/netty-buffer-4.1.91.Final.pom (1.6 kB at 54 kB/s)
2026-01-19T16:16:10.5168862Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.91.Final/netty-parent-4.1.91.Final.pom
2026-01-19T16:16:10.5468565Z Progress (1): 718 B
2026-01-19T16:16:10.5469343Z Progress (1): 2.1 kB
2026-01-19T16:16:10.5474535Z Progress (1): 4.2 kB
2026-01-19T16:16:10.5475044Z Progress (1): 7.0 kB
2026-01-19T16:16:10.5479760Z Progress (1): 8.5 kB
2026-01-19T16:16:10.5480491Z Progress (1): 19 kB 
2026-01-19T16:16:10.5488270Z Progress (1): 22 kB
2026-01-19T16:16:10.5488856Z Progress (1): 24 kB
2026-01-19T16:16:10.5489355Z Progress (1): 26 kB
2026-01-19T16:16:10.5489648Z Progress (1): 29 kB
2026-01-19T16:16:10.5489967Z Progress (1): 32 kB
2026-01-19T16:16:10.5490251Z Progress (1): 36 kB
2026-01-19T16:16:10.5490544Z Progress (1): 41 kB
2026-01-19T16:16:10.5490825Z Progress (1): 44 kB
2026-01-19T16:16:10.5491115Z Progress (1): 47 kB
2026-01-19T16:16:10.5491424Z Progress (1): 47 kB
2026-01-19T16:16:10.5491721Z Progress (1): 51 kB
2026-01-19T16:16:10.5492042Z Progress (1): 53 kB
2026-01-19T16:16:10.5492367Z Progress (1): 56 kB
2026-01-19T16:16:10.5492727Z Progress (1): 59 kB
2026-01-19T16:16:10.5493031Z Progress (1): 61 kB
2026-01-19T16:16:10.5493340Z Progress (1): 64 kB
2026-01-19T16:16:10.5493653Z Progress (1): 66 kB
2026-01-19T16:16:10.5493972Z Progress (1): 68 kB
2026-01-19T16:16:10.5494309Z Progress (1): 72 kB
2026-01-19T16:16:10.5494637Z Progress (1): 75 kB
2026-01-19T16:16:10.5494949Z Progress (1): 81 kB
2026-01-19T16:16:10.5495274Z Progress (1): 83 kB
2026-01-19T16:16:10.5495574Z                    
2026-01-19T16:16:10.5496006Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.91.Final/netty-parent-4.1.91.Final.pom (83 kB at 2.5 MB/s)
2026-01-19T16:16:10.5625874Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.91.Final/netty-common-4.1.91.Final.pom
2026-01-19T16:16:10.5910235Z Progress (1): 1.3 kB
2026-01-19T16:16:10.5910953Z Progress (1): 4.5 kB
2026-01-19T16:16:10.5911460Z Progress (1): 10 kB 
2026-01-19T16:16:10.5911982Z Progress (1): 12 kB
2026-01-19T16:16:10.5912475Z                    
2026-01-19T16:16:10.5913122Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.91.Final/netty-common-4.1.91.Final.pom (12 kB at 407 kB/s)
2026-01-19T16:16:10.5998261Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.91.Final/netty-codec-http-4.1.91.Final.pom
2026-01-19T16:16:10.6239160Z Progress (1): 810 B
2026-01-19T16:16:10.6248722Z Progress (1): 4.2 kB
2026-01-19T16:16:10.6268371Z Progress (1): 4.2 kB
2026-01-19T16:16:10.6273805Z                     
2026-01-19T16:16:10.6278809Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.91.Final/netty-codec-http-4.1.91.Final.pom (4.2 kB at 145 kB/s)
2026-01-19T16:16:10.6449584Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.91.Final/netty-transport-4.1.91.Final.pom
2026-01-19T16:16:10.6663195Z Progress (1): 859 B
2026-01-19T16:16:10.6677531Z Progress (1): 2.2 kB
2026-01-19T16:16:10.6678148Z                     
2026-01-19T16:16:10.6678724Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.91.Final/netty-transport-4.1.91.Final.pom (2.2 kB at 83 kB/s)
2026-01-19T16:16:10.6841298Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.91.Final/netty-resolver-4.1.91.Final.pom
2026-01-19T16:16:10.7072039Z Progress (1): 885 B
2026-01-19T16:16:10.7097837Z Progress (1): 1.6 kB
2026-01-19T16:16:10.7101873Z                     
2026-01-19T16:16:10.7106098Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.91.Final/netty-resolver-4.1.91.Final.pom (1.6 kB at 61 kB/s)
2026-01-19T16:16:10.7248670Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.91.Final/netty-codec-4.1.91.Final.pom
2026-01-19T16:16:10.7497966Z Progress (1): 807 B
2026-01-19T16:16:10.7502128Z Progress (1): 4.3 kB
2026-01-19T16:16:10.7507329Z Progress (1): 5.3 kB
2026-01-19T16:16:10.7511313Z                     
2026-01-19T16:16:10.7515262Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.91.Final/netty-codec-4.1.91.Final.pom (5.3 kB at 196 kB/s)
2026-01-19T16:16:10.7602943Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.91.Final/netty-handler-4.1.91.Final.pom
2026-01-19T16:16:10.7863186Z Progress (1): 801 B
2026-01-19T16:16:10.7865686Z Progress (1): 3.9 kB
2026-01-19T16:16:10.7870146Z Progress (1): 4.6 kB
2026-01-19T16:16:10.7871902Z                     
2026-01-19T16:16:10.7873946Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.91.Final/netty-handler-4.1.91.Final.pom (4.6 kB at 178 kB/s)
2026-01-19T16:16:10.7953844Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.91.Final/netty-transport-native-unix-common-4.1.91.Final.pom
2026-01-19T16:16:10.8234023Z Progress (1): 767 B
2026-01-19T16:16:10.8234922Z Progress (1): 2.2 kB
2026-01-19T16:16:10.8239220Z Progress (1): 4.5 kB
2026-01-19T16:16:10.8240107Z Progress (1): 6.8 kB
2026-01-19T16:16:10.8240694Z Progress (1): 18 kB 
2026-01-19T16:16:10.8241224Z Progress (1): 29 kB
2026-01-19T16:16:10.8241846Z                    
2026-01-19T16:16:10.8242525Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.91.Final/netty-transport-native-unix-common-4.1.91.Final.pom (29 kB at 980 kB/s)
2026-01-19T16:16:10.8395194Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.91.Final/netty-transport-classes-epoll-4.1.91.Final.pom
2026-01-19T16:16:10.8671724Z Progress (1): 850 B
2026-01-19T16:16:10.8673856Z Progress (1): 2.1 kB
2026-01-19T16:16:10.8676775Z                     
2026-01-19T16:16:10.8678203Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.91.Final/netty-transport-classes-epoll-4.1.91.Final.pom (2.1 kB at 74 kB/s)
2026-01-19T16:16:10.8758791Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.91.Final/netty-transport-classes-kqueue-4.1.91.Final.pom
2026-01-19T16:16:10.9008959Z Progress (1): 859 B
2026-01-19T16:16:10.9010329Z Progress (1): 2.1 kB
2026-01-19T16:16:10.9010798Z                     
2026-01-19T16:16:10.9011572Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.91.Final/netty-transport-classes-kqueue-4.1.91.Final.pom (2.1 kB at 85 kB/s)
2026-01-19T16:16:10.9096443Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.91.Final/netty-transport-native-epoll-4.1.91.Final.pom
2026-01-19T16:16:10.9390452Z Progress (1): 766 B
2026-01-19T16:16:10.9391190Z Progress (1): 2.1 kB
2026-01-19T16:16:10.9391789Z Progress (1): 3.4 kB
2026-01-19T16:16:10.9392469Z Progress (1): 6.1 kB
2026-01-19T16:16:10.9393292Z Progress (1): 9.0 kB
2026-01-19T16:16:10.9393787Z Progress (1): 18 kB 
2026-01-19T16:16:10.9394882Z Progress (1): 19 kB
2026-01-19T16:16:10.9395377Z                    
2026-01-19T16:16:10.9395958Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.91.Final/netty-transport-native-epoll-4.1.91.Final.pom (19 kB at 619 kB/s)
2026-01-19T16:16:10.9484920Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.91.Final/netty-transport-native-kqueue-4.1.91.Final.pom
2026-01-19T16:16:10.9783876Z Progress (1): 752 B
2026-01-19T16:16:10.9788553Z Progress (1): 2.1 kB
2026-01-19T16:16:10.9791340Z Progress (1): 3.9 kB
2026-01-19T16:16:10.9791670Z Progress (1): 6.2 kB
2026-01-19T16:16:10.9797765Z Progress (1): 19 kB 
2026-01-19T16:16:10.9798240Z Progress (1): 29 kB
2026-01-19T16:16:10.9798633Z Progress (1): 30 kB
2026-01-19T16:16:10.9798931Z                    
2026-01-19T16:16:10.9802329Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.91.Final/netty-transport-native-kqueue-4.1.91.Final.pom (30 kB at 972 kB/s)
2026-01-19T16:16:11.0072118Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.25.0/opentelemetry-api-1.25.0.pom
2026-01-19T16:16:11.0289554Z Progress (1): 1.0 kB
2026-01-19T16:16:11.0302633Z Progress (1): 1.8 kB
2026-01-19T16:16:11.0307546Z                     
2026-01-19T16:16:11.0308008Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.25.0/opentelemetry-api-1.25.0.pom (1.8 kB at 66 kB/s)
2026-01-19T16:16:11.0369375Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.25.0/opentelemetry-context-1.25.0.pom
2026-01-19T16:16:11.0597840Z Progress (1): 989 B
2026-01-19T16:16:11.0603330Z Progress (1): 1.6 kB
2026-01-19T16:16:11.0603981Z                     
2026-01-19T16:16:11.0605346Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.25.0/opentelemetry-context-1.25.0.pom (1.6 kB at 58 kB/s)
2026-01-19T16:16:11.0657875Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.25.0/opentelemetry-exporter-logging-1.25.0.pom
2026-01-19T16:16:11.0900911Z Progress (1): 988 B
2026-01-19T16:16:11.0908654Z Progress (1): 2.4 kB
2026-01-19T16:16:11.0912705Z                     
2026-01-19T16:16:11.0916906Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.25.0/opentelemetry-exporter-logging-1.25.0.pom (2.4 kB at 93 kB/s)
2026-01-19T16:16:11.0954508Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.25.0/opentelemetry-sdk-1.25.0.pom
2026-01-19T16:16:11.1220412Z Progress (1): 994 B
2026-01-19T16:16:11.1224859Z Progress (1): 2.6 kB
2026-01-19T16:16:11.1230644Z                     
2026-01-19T16:16:11.1236345Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.25.0/opentelemetry-sdk-1.25.0.pom (2.6 kB at 88 kB/s)
2026-01-19T16:16:11.1294270Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.25.0/opentelemetry-sdk-common-1.25.0.pom
2026-01-19T16:16:11.1619685Z Progress (1): 995 B
2026-01-19T16:16:11.1620237Z Progress (1): 2.0 kB
2026-01-19T16:16:11.1621003Z                     
2026-01-19T16:16:11.1621481Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.25.0/opentelemetry-sdk-common-1.25.0.pom (2.0 kB at 58 kB/s)
2026-01-19T16:16:11.1661277Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.25.0-alpha/opentelemetry-semconv-1.25.0-alpha.pom
2026-01-19T16:16:11.1922984Z Progress (1): 985 B
2026-01-19T16:16:11.1957236Z Progress (1): 1.8 kB
2026-01-19T16:16:11.1957880Z                     
2026-01-19T16:16:11.1958780Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.25.0-alpha/opentelemetry-semconv-1.25.0-alpha.pom (1.8 kB at 62 kB/s)
2026-01-19T16:16:11.1963197Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.25.0/opentelemetry-sdk-trace-1.25.0.pom
2026-01-19T16:16:11.2241449Z Progress (1): 977 B
2026-01-19T16:16:11.2248270Z Progress (1): 2.2 kB
2026-01-19T16:16:11.2250848Z                     
2026-01-19T16:16:11.2251564Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.25.0/opentelemetry-sdk-trace-1.25.0.pom (2.2 kB at 78 kB/s)
2026-01-19T16:16:11.2288663Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.25.0/opentelemetry-sdk-metrics-1.25.0.pom
2026-01-19T16:16:11.2556293Z Progress (1): 997 B
2026-01-19T16:16:11.2558424Z Progress (1): 2.0 kB
2026-01-19T16:16:11.2560991Z                     
2026-01-19T16:16:11.2561465Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.25.0/opentelemetry-sdk-metrics-1.25.0.pom (2.0 kB at 74 kB/s)
2026-01-19T16:16:11.2588760Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.25.0-alpha/opentelemetry-sdk-logs-1.25.0-alpha.pom
2026-01-19T16:16:11.2887971Z Progress (1): 975 B
2026-01-19T16:16:11.2928376Z Progress (1): 2.2 kB
2026-01-19T16:16:11.2928985Z                     
2026-01-19T16:16:11.2929652Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.25.0-alpha/opentelemetry-sdk-logs-1.25.0-alpha.pom (2.2 kB at 69 kB/s)
2026-01-19T16:16:11.2968751Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-logs/1.25.0-alpha/opentelemetry-api-logs-1.25.0-alpha.pom
2026-01-19T16:16:11.3219441Z Progress (1): 985 B
2026-01-19T16:16:11.3228286Z Progress (1): 1.8 kB
2026-01-19T16:16:11.3232463Z                     
2026-01-19T16:16:11.3234200Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-logs/1.25.0-alpha/opentelemetry-api-logs-1.25.0-alpha.pom (1.8 kB at 66 kB/s)
2026-01-19T16:16:11.3268585Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.25.0-alpha/opentelemetry-api-events-1.25.0-alpha.pom
2026-01-19T16:16:11.3573008Z Progress (1): 989 B
2026-01-19T16:16:11.3573877Z Progress (1): 1.8 kB
2026-01-19T16:16:11.3574570Z                     
2026-01-19T16:16:11.3575397Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.25.0-alpha/opentelemetry-api-events-1.25.0-alpha.pom (1.8 kB at 56 kB/s)
2026-01-19T16:16:11.3609059Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.25.0/opentelemetry-sdk-extension-autoconfigure-spi-1.25.0.pom
2026-01-19T16:16:11.3884119Z Progress (1): 964 B
2026-01-19T16:16:11.3888381Z Progress (1): 2.2 kB
2026-01-19T16:16:11.3891208Z                     
2026-01-19T16:16:11.3892582Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.25.0/opentelemetry-sdk-extension-autoconfigure-spi-1.25.0.pom (2.2 kB at 79 kB/s)
2026-01-19T16:16:11.3921344Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.25.0-alpha/opentelemetry-sdk-extension-autoconfigure-1.25.0-alpha.pom
2026-01-19T16:16:11.4200248Z Progress (1): 962 B
2026-01-19T16:16:11.4203534Z Progress (1): 2.6 kB
2026-01-19T16:16:11.4205377Z                     
2026-01-19T16:16:11.4205927Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.25.0-alpha/opentelemetry-sdk-extension-autoconfigure-1.25.0-alpha.pom (2.6 kB at 94 kB/s)
2026-01-19T16:16:11.4286270Z Downloading from central: https://repo.maven.apache.org/maven2/io/ous/jtoml/2.0.0/jtoml-2.0.0.pom
2026-01-19T16:16:11.4535739Z Progress (1): 1.3 kB
2026-01-19T16:16:11.4543572Z Progress (1): 4.0 kB
2026-01-19T16:16:11.4544098Z                     
2026-01-19T16:16:11.4545552Z Downloaded from central: https://repo.maven.apache.org/maven2/io/ous/jtoml/2.0.0/jtoml-2.0.0.pom (4.0 kB at 136 kB/s)
2026-01-19T16:16:11.4583243Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.4/byte-buddy-1.14.4.pom
2026-01-19T16:16:11.4859878Z Progress (1): 958 B
2026-01-19T16:16:11.4860273Z Progress (1): 3.7 kB
2026-01-19T16:16:11.4860631Z Progress (1): 7.0 kB
2026-01-19T16:16:11.4860949Z Progress (1): 14 kB 
2026-01-19T16:16:11.4861487Z Progress (1): 16 kB
2026-01-19T16:16:11.4861796Z                    
2026-01-19T16:16:11.4862231Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.4/byte-buddy-1.14.4.pom (16 kB at 565 kB/s)
2026-01-19T16:16:11.4909142Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.14.4/byte-buddy-parent-1.14.4.pom
2026-01-19T16:16:11.5200096Z Progress (1): 832 B
2026-01-19T16:16:11.5200758Z Progress (1): 2.1 kB
2026-01-19T16:16:11.5201365Z Progress (1): 3.6 kB
2026-01-19T16:16:11.5201916Z Progress (1): 6.2 kB
2026-01-19T16:16:11.5202229Z Progress (1): 8.1 kB
2026-01-19T16:16:11.5202525Z Progress (1): 11 kB 
2026-01-19T16:16:11.5207072Z Progress (1): 13 kB
2026-01-19T16:16:11.5207406Z Progress (1): 17 kB
2026-01-19T16:16:11.5207750Z Progress (1): 22 kB
2026-01-19T16:16:11.5211979Z Progress (1): 25 kB
2026-01-19T16:16:11.5212307Z Progress (1): 36 kB
2026-01-19T16:16:11.5212573Z Progress (1): 45 kB
2026-01-19T16:16:11.5212882Z Progress (1): 50 kB
2026-01-19T16:16:11.5213201Z Progress (1): 55 kB
2026-01-19T16:16:11.5213493Z Progress (1): 58 kB
2026-01-19T16:16:11.5213792Z                    
2026-01-19T16:16:11.5214193Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.14.4/byte-buddy-parent-1.14.4.pom (58 kB at 1.9 MB/s)
2026-01-19T16:16:11.5291654Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-exec/1.3/commons-exec-1.3.pom
2026-01-19T16:16:11.5598470Z Progress (1): 778 B
2026-01-19T16:16:11.5607366Z Progress (1): 2.3 kB
2026-01-19T16:16:11.5607955Z Progress (1): 5.2 kB
2026-01-19T16:16:11.5608280Z Progress (1): 7.7 kB
2026-01-19T16:16:11.5608585Z Progress (1): 10 kB 
2026-01-19T16:16:11.5608882Z Progress (1): 11 kB
2026-01-19T16:16:11.5609173Z                    
2026-01-19T16:16:11.5609590Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-exec/1.3/commons-exec-1.3.pom (11 kB at 379 kB/s)
2026-01-19T16:16:11.5633093Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/35/commons-parent-35.pom
2026-01-19T16:16:11.5895719Z Progress (1): 715 B
2026-01-19T16:16:11.5896723Z Progress (1): 2.0 kB
2026-01-19T16:16:11.5902222Z Progress (1): 3.3 kB
2026-01-19T16:16:11.5907585Z Progress (1): 4.8 kB
2026-01-19T16:16:11.5912803Z Progress (1): 8.2 kB
2026-01-19T16:16:11.5918274Z Progress (1): 11 kB 
2026-01-19T16:16:11.5923280Z Progress (1): 15 kB
2026-01-19T16:16:11.5932685Z Progress (1): 18 kB
2026-01-19T16:16:11.5941597Z Progress (1): 21 kB
2026-01-19T16:16:11.5954676Z Progress (1): 24 kB
2026-01-19T16:16:11.5969832Z Progress (1): 26 kB
2026-01-19T16:16:11.5970492Z Progress (1): 30 kB
2026-01-19T16:16:11.5970907Z Progress (1): 32 kB
2026-01-19T16:16:11.5971319Z Progress (1): 36 kB
2026-01-19T16:16:11.5971714Z Progress (1): 41 kB
2026-01-19T16:16:11.5972175Z Progress (1): 42 kB
2026-01-19T16:16:11.5972615Z Progress (1): 46 kB
2026-01-19T16:16:11.5973054Z Progress (1): 48 kB
2026-01-19T16:16:11.5973521Z Progress (1): 51 kB
2026-01-19T16:16:11.5973958Z Progress (1): 53 kB
2026-01-19T16:16:11.5974406Z Progress (1): 56 kB
2026-01-19T16:16:11.5974849Z Progress (1): 57 kB
2026-01-19T16:16:11.5975311Z Progress (1): 58 kB
2026-01-19T16:16:11.5975967Z                    
2026-01-19T16:16:11.5976739Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/35/commons-parent-35.pom (58 kB at 1.8 MB/s)
2026-01-19T16:16:11.6112197Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/15/apache-15.pom
2026-01-19T16:16:11.6368949Z Progress (1): 749 B
2026-01-19T16:16:11.6374195Z Progress (1): 2.1 kB
2026-01-19T16:16:11.6380499Z Progress (1): 3.9 kB
2026-01-19T16:16:11.6384325Z Progress (1): 7.8 kB
2026-01-19T16:16:11.6389585Z Progress (1): 11 kB 
2026-01-19T16:16:11.6391622Z Progress (1): 14 kB
2026-01-19T16:16:11.6396010Z Progress (1): 15 kB
2026-01-19T16:16:11.6396835Z                    
2026-01-19T16:16:11.6399911Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/15/apache-15.pom (15 kB at 491 kB/s)
2026-01-19T16:16:11.6459031Z Downloading from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client/2.12.3/async-http-client-2.12.3.pom
2026-01-19T16:16:11.6776381Z Progress (1): 1.7 kB
2026-01-19T16:16:11.6777236Z Progress (1): 2.7 kB
2026-01-19T16:16:11.6778323Z                     
2026-01-19T16:16:11.6778757Z Downloaded from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client/2.12.3/async-http-client-2.12.3.pom (2.7 kB at 93 kB/s)
2026-01-19T16:16:11.6779352Z Downloading from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-project/2.12.3/async-http-client-project-2.12.3.pom
2026-01-19T16:16:11.7049199Z Progress (1): 910 B
2026-01-19T16:16:11.7054878Z Progress (1): 2.8 kB
2026-01-19T16:16:11.7059573Z Progress (1): 5.6 kB
2026-01-19T16:16:11.7060518Z Progress (1): 8.3 kB
2026-01-19T16:16:11.7060872Z Progress (1): 13 kB 
2026-01-19T16:16:11.7062244Z Progress (1): 16 kB
2026-01-19T16:16:11.7063877Z                    
2026-01-19T16:16:11.7064336Z Downloaded from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-project/2.12.3/async-http-client-project-2.12.3.pom (16 kB at 564 kB/s)
2026-01-19T16:16:11.7102593Z Downloading from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-netty-utils/2.12.3/async-http-client-netty-utils-2.12.3.pom
2026-01-19T16:16:11.7360310Z Progress (1): 757 B
2026-01-19T16:16:11.7361374Z                    
2026-01-19T16:16:11.7362498Z Downloaded from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-netty-utils/2.12.3/async-http-client-netty-utils-2.12.3.pom (757 B at 29 kB/s)
2026-01-19T16:16:11.7401271Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.60.Final/netty-buffer-4.1.60.Final.pom
2026-01-19T16:16:11.7659343Z Progress (1): 885 B
2026-01-19T16:16:11.7663547Z Progress (1): 1.6 kB
2026-01-19T16:16:11.7664450Z                     
2026-01-19T16:16:11.7665986Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.60.Final/netty-buffer-4.1.60.Final.pom (1.6 kB at 59 kB/s)
2026-01-19T16:16:11.7690076Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.60.Final/netty-parent-4.1.60.Final.pom
2026-01-19T16:16:11.7938279Z Progress (1): 717 B
2026-01-19T16:16:11.7939089Z Progress (1): 2.1 kB
2026-01-19T16:16:11.7947070Z Progress (1): 3.7 kB
2026-01-19T16:16:11.7951565Z Progress (1): 11 kB 
2026-01-19T16:16:11.7954795Z Progress (1): 13 kB
2026-01-19T16:16:11.7955131Z Progress (1): 15 kB
2026-01-19T16:16:11.7956685Z Progress (1): 17 kB
2026-01-19T16:16:11.7958889Z Progress (1): 19 kB
2026-01-19T16:16:11.7959423Z Progress (1): 22 kB
2026-01-19T16:16:11.7961271Z Progress (1): 27 kB
2026-01-19T16:16:11.7962416Z Progress (1): 31 kB
2026-01-19T16:16:11.7962960Z Progress (1): 33 kB
2026-01-19T16:16:11.7963947Z Progress (1): 35 kB
2026-01-19T16:16:11.7964483Z Progress (1): 39 kB
2026-01-19T16:16:11.7965083Z Progress (1): 41 kB
2026-01-19T16:16:11.7965674Z Progress (1): 41 kB
2026-01-19T16:16:11.7974869Z Progress (1): 44 kB
2026-01-19T16:16:11.7975895Z Progress (1): 46 kB
2026-01-19T16:16:11.7977198Z Progress (1): 48 kB
2026-01-19T16:16:11.7977647Z Progress (1): 51 kB
2026-01-19T16:16:11.7978096Z Progress (1): 56 kB
2026-01-19T16:16:11.7978628Z Progress (1): 60 kB
2026-01-19T16:16:11.7987043Z Progress (1): 62 kB
2026-01-19T16:16:11.7987723Z                    
2026-01-19T16:16:11.7988473Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.60.Final/netty-parent-4.1.60.Final.pom (62 kB at 2.1 MB/s)
2026-01-19T16:16:11.8068846Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.60.Final/netty-common-4.1.60.Final.pom
2026-01-19T16:16:11.8383062Z Progress (1): 1.3 kB
2026-01-19T16:16:11.8384057Z Progress (1): 4.6 kB
2026-01-19T16:16:11.8385832Z Progress (1): 10 kB 
2026-01-19T16:16:11.8386675Z Progress (1): 12 kB
2026-01-19T16:16:11.8388621Z                    
2026-01-19T16:16:11.8391104Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.60.Final/netty-common-4.1.60.Final.pom (12 kB at 366 kB/s)
2026-01-19T16:16:11.8484265Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.pom
2026-01-19T16:16:11.8717647Z Progress (1): 1.0 kB
2026-01-19T16:16:11.8718321Z Progress (1): 3.3 kB
2026-01-19T16:16:11.8725137Z Progress (1): 3.8 kB
2026-01-19T16:16:11.8725813Z                     
2026-01-19T16:16:11.8731994Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.30/slf4j-api-1.7.30.pom (3.8 kB at 153 kB/s)
2026-01-19T16:16:11.8778743Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.30/slf4j-parent-1.7.30.pom
2026-01-19T16:16:11.9056174Z Progress (1): 1.0 kB
2026-01-19T16:16:11.9057422Z Progress (1): 3.1 kB
2026-01-19T16:16:11.9058555Z Progress (1): 6.0 kB
2026-01-19T16:16:11.9060480Z Progress (1): 9.0 kB
2026-01-19T16:16:11.9067691Z Progress (1): 12 kB 
2026-01-19T16:16:11.9068880Z Progress (1): 14 kB
2026-01-19T16:16:11.9070303Z                    
2026-01-19T16:16:11.9071254Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.30/slf4j-parent-1.7.30.pom (14 kB at 460 kB/s)
2026-01-19T16:16:11.9107815Z Downloading from central: https://repo.maven.apache.org/maven2/com/sun/activation/jakarta.activation/1.2.2/jakarta.activation-1.2.2.pom
2026-01-19T16:16:11.9360976Z Progress (1): 885 B
2026-01-19T16:16:11.9367324Z Progress (1): 2.6 kB
2026-01-19T16:16:11.9367652Z Progress (1): 4.3 kB
2026-01-19T16:16:11.9367948Z Progress (1): 4.6 kB
2026-01-19T16:16:11.9371607Z                     
2026-01-19T16:16:11.9372577Z Downloaded from central: https://repo.maven.apache.org/maven2/com/sun/activation/jakarta.activation/1.2.2/jakarta.activation-1.2.2.pom (4.6 kB at 178 kB/s)
2026-01-19T16:16:11.9412905Z Downloading from central: https://repo.maven.apache.org/maven2/com/sun/activation/all/1.2.2/all-1.2.2.pom
2026-01-19T16:16:11.9660987Z Progress (1): 781 B
2026-01-19T16:16:11.9663163Z Progress (1): 2.8 kB
2026-01-19T16:16:11.9663490Z Progress (1): 4.3 kB
2026-01-19T16:16:11.9663788Z Progress (1): 6.0 kB
2026-01-19T16:16:11.9664084Z Progress (1): 8.2 kB
2026-01-19T16:16:11.9664377Z Progress (1): 11 kB 
2026-01-19T16:16:11.9664677Z Progress (1): 14 kB
2026-01-19T16:16:11.9664969Z Progress (1): 15 kB
2026-01-19T16:16:11.9665443Z                    
2026-01-19T16:16:11.9665824Z Downloaded from central: https://repo.maven.apache.org/maven2/com/sun/activation/all/1.2.2/all-1.2.2.pom (15 kB at 607 kB/s)
2026-01-19T16:16:11.9711985Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/ee4j/project/1.0.6/project-1.0.6.pom
2026-01-19T16:16:12.0013715Z Progress (1): 839 B
2026-01-19T16:16:12.0014565Z Progress (1): 2.5 kB
2026-01-19T16:16:12.0015186Z Progress (1): 5.0 kB
2026-01-19T16:16:12.0018064Z Progress (1): 7.6 kB
2026-01-19T16:16:12.0018531Z Progress (1): 12 kB 
2026-01-19T16:16:12.0019054Z Progress (1): 13 kB
2026-01-19T16:16:12.0019673Z                    
2026-01-19T16:16:12.0029684Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/ee4j/project/1.0.6/project-1.0.6.pom (13 kB at 430 kB/s)
2026-01-19T16:16:12.0099709Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.60.Final/netty-codec-http-4.1.60.Final.pom
2026-01-19T16:16:12.0334030Z Progress (1): 859 B
2026-01-19T16:16:12.0340856Z Progress (1): 2.4 kB
2026-01-19T16:16:12.0341385Z                     
2026-01-19T16:16:12.0341824Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.60.Final/netty-codec-http-4.1.60.Final.pom (2.4 kB at 100 kB/s)
2026-01-19T16:16:12.0418609Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.60.Final/netty-transport-4.1.60.Final.pom
2026-01-19T16:16:12.0649166Z Progress (1): 881 B
2026-01-19T16:16:12.0656858Z Progress (1): 1.9 kB
2026-01-19T16:16:12.0657168Z                     
2026-01-19T16:16:12.0657604Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.60.Final/netty-transport-4.1.60.Final.pom (1.9 kB at 74 kB/s)
2026-01-19T16:16:12.0738668Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.60.Final/netty-resolver-4.1.60.Final.pom
2026-01-19T16:16:12.0945487Z Progress (1): 884 B
2026-01-19T16:16:12.0953410Z Progress (1): 1.6 kB
2026-01-19T16:16:12.0957734Z                     
2026-01-19T16:16:12.0959320Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.60.Final/netty-resolver-4.1.60.Final.pom (1.6 kB at 66 kB/s)
2026-01-19T16:16:12.1034566Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.60.Final/netty-codec-4.1.60.Final.pom
2026-01-19T16:16:12.1265873Z Progress (1): 810 B
2026-01-19T16:16:12.1271909Z Progress (1): 3.6 kB
2026-01-19T16:16:12.1273622Z                     
2026-01-19T16:16:12.1274049Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.60.Final/netty-codec-4.1.60.Final.pom (3.6 kB at 133 kB/s)
2026-01-19T16:16:12.1331509Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.60.Final/netty-handler-4.1.60.Final.pom
2026-01-19T16:16:12.1581218Z Progress (1): 807 B
2026-01-19T16:16:12.1597196Z Progress (1): 3.4 kB
2026-01-19T16:16:12.1598011Z Progress (1): 3.6 kB
2026-01-19T16:16:12.1598563Z                     
2026-01-19T16:16:12.1599203Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.60.Final/netty-handler-4.1.60.Final.pom (3.6 kB at 142 kB/s)
2026-01-19T16:16:12.1668636Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-socks/4.1.60.Final/netty-codec-socks-4.1.60.Final.pom
2026-01-19T16:16:12.1907886Z Progress (1): 882 B
2026-01-19T16:16:12.1920194Z Progress (1): 2.0 kB
2026-01-19T16:16:12.1920537Z                     
2026-01-19T16:16:12.1920995Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-socks/4.1.60.Final/netty-codec-socks-4.1.60.Final.pom (2.0 kB at 71 kB/s)
2026-01-19T16:16:12.1960223Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler-proxy/4.1.60.Final/netty-handler-proxy-4.1.60.Final.pom
2026-01-19T16:16:12.2237628Z Progress (1): 850 B
2026-01-19T16:16:12.2244420Z Progress (1): 2.8 kB
2026-01-19T16:16:12.2246690Z                     
2026-01-19T16:16:12.2251081Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler-proxy/4.1.60.Final/netty-handler-proxy-4.1.60.Final.pom (2.8 kB at 96 kB/s)
2026-01-19T16:16:12.2297842Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.60.Final/netty-transport-native-epoll-4.1.60.Final.pom
2026-01-19T16:16:12.2520114Z Progress (1): 767 B
2026-01-19T16:16:12.2520781Z Progress (1): 2.1 kB
2026-01-19T16:16:12.2523148Z Progress (1): 3.7 kB
2026-01-19T16:16:12.2523605Z Progress (1): 6.4 kB
2026-01-19T16:16:12.2528022Z Progress (1): 9.0 kB
2026-01-19T16:16:12.2530841Z Progress (1): 18 kB 
2026-01-19T16:16:12.2531516Z Progress (1): 18 kB
2026-01-19T16:16:12.2533169Z                    
2026-01-19T16:16:12.2534067Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.60.Final/netty-transport-native-epoll-4.1.60.Final.pom (18 kB at 746 kB/s)
2026-01-19T16:16:12.2588345Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.60.Final/netty-transport-native-unix-common-4.1.60.Final.pom
2026-01-19T16:16:12.2813352Z Progress (1): 772 B
2026-01-19T16:16:12.2814077Z Progress (1): 2.2 kB
2026-01-19T16:16:12.2819792Z Progress (1): 4.5 kB
2026-01-19T16:16:12.2820445Z Progress (1): 6.9 kB
2026-01-19T16:16:12.2820950Z Progress (1): 18 kB 
2026-01-19T16:16:12.2828038Z Progress (1): 22 kB
2026-01-19T16:16:12.2848432Z                    
2026-01-19T16:16:12.2849086Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.60.Final/netty-transport-native-unix-common-4.1.60.Final.pom (22 kB at 883 kB/s)
2026-01-19T16:16:12.2890867Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.60.Final/netty-transport-native-kqueue-4.1.60.Final.pom
2026-01-19T16:16:12.3149594Z Progress (1): 767 B
2026-01-19T16:16:12.3150318Z Progress (1): 2.2 kB
2026-01-19T16:16:12.3150923Z Progress (1): 3.9 kB
2026-01-19T16:16:12.3151463Z Progress (1): 6.4 kB
2026-01-19T16:16:12.3152103Z Progress (1): 16 kB 
2026-01-19T16:16:12.3152740Z Progress (1): 19 kB
2026-01-19T16:16:12.3178113Z                    
2026-01-19T16:16:12.3178901Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.60.Final/netty-transport-native-kqueue-4.1.60.Final.pom (19 kB at 664 kB/s)
2026-01-19T16:16:12.3272545Z Downloading from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.3/reactive-streams-1.0.3.pom
2026-01-19T16:16:12.3517235Z Progress (1): 1.2 kB
2026-01-19T16:16:12.3537247Z                     
2026-01-19T16:16:12.3538336Z Downloaded from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.3/reactive-streams-1.0.3.pom (1.2 kB at 45 kB/s)
2026-01-19T16:16:12.3562032Z Downloading from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams/2.0.4/netty-reactive-streams-2.0.4.pom
2026-01-19T16:16:12.3837731Z Progress (1): 1.8 kB
2026-01-19T16:16:12.3838081Z Progress (1): 2.1 kB
2026-01-19T16:16:12.3838384Z                     
2026-01-19T16:16:12.3838831Z Downloaded from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams/2.0.4/netty-reactive-streams-2.0.4.pom (2.1 kB at 77 kB/s)
2026-01-19T16:16:12.3848478Z Downloading from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams-parent/2.0.4/netty-reactive-streams-parent-2.0.4.pom
2026-01-19T16:16:12.4103893Z Progress (1): 1.1 kB
2026-01-19T16:16:12.4104288Z Progress (1): 4.1 kB
2026-01-19T16:16:12.4104613Z Progress (1): 8.2 kB
2026-01-19T16:16:12.4104943Z Progress (1): 8.4 kB
2026-01-19T16:16:12.4105242Z                     
2026-01-19T16:16:12.4105715Z Downloaded from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams-parent/2.0.4/netty-reactive-streams-parent-2.0.4.pom (8.4 kB at 336 kB/s)
2026-01-19T16:16:12.4130867Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.43.Final/netty-handler-4.1.43.Final.pom
2026-01-19T16:16:12.4378102Z Progress (1): 814 B
2026-01-19T16:16:12.4378454Z Progress (1): 3.3 kB
2026-01-19T16:16:12.4378773Z Progress (1): 3.4 kB
2026-01-19T16:16:12.4379060Z                     
2026-01-19T16:16:12.4379487Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.43.Final/netty-handler-4.1.43.Final.pom (3.4 kB at 135 kB/s)
2026-01-19T16:16:12.4397375Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.43.Final/netty-parent-4.1.43.Final.pom
2026-01-19T16:16:12.4673982Z Progress (1): 733 B
2026-01-19T16:16:12.4674384Z Progress (1): 2.1 kB
2026-01-19T16:16:12.4676999Z Progress (1): 3.7 kB
2026-01-19T16:16:12.4687153Z Progress (1): 8.5 kB
2026-01-19T16:16:12.4687534Z Progress (1): 10 kB 
2026-01-19T16:16:12.4687861Z Progress (1): 12 kB
2026-01-19T16:16:12.4688193Z Progress (1): 14 kB
2026-01-19T16:16:12.4692177Z Progress (1): 17 kB
2026-01-19T16:16:12.4692510Z Progress (1): 20 kB
2026-01-19T16:16:12.4692808Z Progress (1): 25 kB
2026-01-19T16:16:12.4693124Z Progress (1): 27 kB
2026-01-19T16:16:12.4693475Z Progress (1): 29 kB
2026-01-19T16:16:12.4693782Z Progress (1): 32 kB
2026-01-19T16:16:12.4699089Z Progress (1): 35 kB
2026-01-19T16:16:12.4699438Z Progress (1): 37 kB
2026-01-19T16:16:12.4699741Z Progress (1): 37 kB
2026-01-19T16:16:12.4700057Z Progress (1): 39 kB
2026-01-19T16:16:12.4700370Z Progress (1): 42 kB
2026-01-19T16:16:12.4701277Z Progress (1): 45 kB
2026-01-19T16:16:12.4701650Z Progress (1): 48 kB
2026-01-19T16:16:12.4701930Z Progress (1): 54 kB
2026-01-19T16:16:12.4705462Z Progress (1): 56 kB
2026-01-19T16:16:12.4706050Z                    
2026-01-19T16:16:12.4708150Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.43.Final/netty-parent-4.1.43.Final.pom (56 kB at 1.8 MB/s)
2026-01-19T16:16:12.4788527Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.43.Final/netty-common-4.1.43.Final.pom
2026-01-19T16:16:12.5025077Z Progress (1): 1.4 kB
2026-01-19T16:16:12.5043225Z Progress (1): 4.8 kB
2026-01-19T16:16:12.5045888Z Progress (1): 9.8 kB
2026-01-19T16:16:12.5047873Z Progress (1): 10 kB 
2026-01-19T16:16:12.5053910Z                    
2026-01-19T16:16:12.5054660Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.43.Final/netty-common-4.1.43.Final.pom (10 kB at 387 kB/s)
2026-01-19T16:16:12.5091805Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.43.Final/netty-buffer-4.1.43.Final.pom
2026-01-19T16:16:12.5322185Z Progress (1): 888 B
2026-01-19T16:16:12.5339567Z Progress (1): 1.6 kB
2026-01-19T16:16:12.5340167Z                     
2026-01-19T16:16:12.5340776Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.43.Final/netty-buffer-4.1.43.Final.pom (1.6 kB at 61 kB/s)
2026-01-19T16:16:12.5436397Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.43.Final/netty-transport-4.1.43.Final.pom
2026-01-19T16:16:12.5679442Z Progress (1): 882 B
2026-01-19T16:16:12.5691365Z Progress (1): 1.9 kB
2026-01-19T16:16:12.5691944Z                     
2026-01-19T16:16:12.5692518Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.43.Final/netty-transport-4.1.43.Final.pom (1.9 kB at 74 kB/s)
2026-01-19T16:16:12.5742018Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.43.Final/netty-resolver-4.1.43.Final.pom
2026-01-19T16:16:12.5986117Z Progress (1): 888 B
2026-01-19T16:16:12.6008729Z Progress (1): 1.6 kB
2026-01-19T16:16:12.6009453Z                     
2026-01-19T16:16:12.6010195Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.43.Final/netty-resolver-4.1.43.Final.pom (1.6 kB at 61 kB/s)
2026-01-19T16:16:12.6076840Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.43.Final/netty-codec-4.1.43.Final.pom
2026-01-19T16:16:12.6306156Z Progress (1): 814 B
2026-01-19T16:16:12.6314077Z Progress (1): 3.6 kB
2026-01-19T16:16:12.6317250Z                     
2026-01-19T16:16:12.6317678Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.43.Final/netty-codec-4.1.43.Final.pom (3.6 kB at 143 kB/s)
2026-01-19T16:16:12.6374131Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.9.1/selenium-http-4.9.1.pom
2026-01-19T16:16:12.6622208Z Progress (1): 1.1 kB
2026-01-19T16:16:12.6622815Z Progress (1): 2.8 kB
2026-01-19T16:16:12.6623257Z                     
2026-01-19T16:16:12.6623831Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.9.1/selenium-http-4.9.1.pom (2.8 kB at 112 kB/s)
2026-01-19T16:16:12.6654089Z Downloading from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.1/failsafe-3.3.1.pom
2026-01-19T16:16:12.6912966Z Progress (1): 1.0 kB
2026-01-19T16:16:12.6917738Z                     
2026-01-19T16:16:12.6918142Z Downloaded from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.1/failsafe-3.3.1.pom (1.0 kB at 39 kB/s)
2026-01-19T16:16:12.6952118Z Downloading from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe-parent/3.3.1/failsafe-parent-3.3.1.pom
2026-01-19T16:16:12.7280282Z Progress (1): 1.1 kB
2026-01-19T16:16:12.7287256Z Progress (1): 3.4 kB
2026-01-19T16:16:12.7287764Z Progress (1): 5.8 kB
2026-01-19T16:16:12.7288243Z Progress (1): 8.7 kB
2026-01-19T16:16:12.7288669Z Progress (1): 9.2 kB
2026-01-19T16:16:12.7289107Z                     
2026-01-19T16:16:12.7297680Z Downloaded from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe-parent/3.3.1/failsafe-parent-3.3.1.pom (9.2 kB at 278 kB/s)
2026-01-19T16:16:12.7358390Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.9.1/selenium-json-4.9.1.pom
2026-01-19T16:16:12.7684578Z Progress (1): 1.1 kB
2026-01-19T16:16:12.7690460Z Progress (1): 2.3 kB
2026-01-19T16:16:12.7690956Z                     
2026-01-19T16:16:12.7691604Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.9.1/selenium-json-4.9.1.pom (2.3 kB at 69 kB/s)
2026-01-19T16:16:12.7748337Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.9.1/selenium-manager-4.9.1.pom
2026-01-19T16:16:12.7999165Z Progress (1): 1.1 kB
2026-01-19T16:16:12.8004737Z Progress (1): 2.6 kB
2026-01-19T16:16:12.8005670Z                     
2026-01-19T16:16:12.8006158Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.9.1/selenium-manager-4.9.1.pom (2.6 kB at 97 kB/s)
2026-01-19T16:16:12.8054561Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.10.0/selenium-remote-driver-4.10.0.pom
2026-01-19T16:16:12.8293966Z Progress (1): 1.0 kB
2026-01-19T16:16:12.8297904Z Progress (1): 6.9 kB
2026-01-19T16:16:12.8317975Z Progress (1): 8.1 kB
2026-01-19T16:16:12.8320599Z                     
2026-01-19T16:16:12.8321046Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.10.0/selenium-remote-driver-4.10.0.pom (8.1 kB at 299 kB/s)
2026-01-19T16:16:12.8364109Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.92.Final/netty-buffer-4.1.92.Final.pom
2026-01-19T16:16:12.8588503Z Progress (1): 885 B
2026-01-19T16:16:12.8596750Z Progress (1): 1.6 kB
2026-01-19T16:16:12.8597538Z                     
2026-01-19T16:16:12.8598865Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.92.Final/netty-buffer-4.1.92.Final.pom (1.6 kB at 63 kB/s)
2026-01-19T16:16:12.8617350Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.92.Final/netty-parent-4.1.92.Final.pom
2026-01-19T16:16:12.8878019Z Progress (1): 717 B
2026-01-19T16:16:12.8878870Z Progress (1): 2.1 kB
2026-01-19T16:16:12.8879367Z Progress (1): 4.2 kB
2026-01-19T16:16:12.8879727Z Progress (1): 7.0 kB
2026-01-19T16:16:12.8883951Z Progress (1): 8.5 kB
2026-01-19T16:16:12.8885474Z Progress (1): 19 kB 
2026-01-19T16:16:12.8889137Z Progress (1): 22 kB
2026-01-19T16:16:12.8899463Z Progress (1): 24 kB
2026-01-19T16:16:12.8900245Z Progress (1): 26 kB
2026-01-19T16:16:12.8900590Z Progress (1): 29 kB
2026-01-19T16:16:12.8901010Z Progress (1): 32 kB
2026-01-19T16:16:12.8901538Z Progress (1): 36 kB
2026-01-19T16:16:12.8907145Z Progress (1): 41 kB
2026-01-19T16:16:12.8907607Z Progress (1): 44 kB
2026-01-19T16:16:12.8908024Z Progress (1): 47 kB
2026-01-19T16:16:12.8908456Z Progress (1): 47 kB
2026-01-19T16:16:12.8908890Z Progress (1): 51 kB
2026-01-19T16:16:12.8909251Z Progress (1): 54 kB
2026-01-19T16:16:12.8910705Z Progress (1): 56 kB
2026-01-19T16:16:12.8911289Z Progress (1): 59 kB
2026-01-19T16:16:12.8912950Z Progress (1): 61 kB
2026-01-19T16:16:12.8913568Z Progress (1): 64 kB
2026-01-19T16:16:12.8915106Z Progress (1): 66 kB
2026-01-19T16:16:12.8915426Z Progress (1): 69 kB
2026-01-19T16:16:12.8915732Z Progress (1): 72 kB
2026-01-19T16:16:12.8916050Z Progress (1): 76 kB
2026-01-19T16:16:12.8916361Z Progress (1): 81 kB
2026-01-19T16:16:12.8916902Z Progress (1): 83 kB
2026-01-19T16:16:12.8917205Z                    
2026-01-19T16:16:12.8917644Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.92.Final/netty-parent-4.1.92.Final.pom (83 kB at 2.9 MB/s)
2026-01-19T16:16:12.9028819Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.92.Final/netty-common-4.1.92.Final.pom
2026-01-19T16:16:12.9258360Z Progress (1): 1.3 kB
2026-01-19T16:16:12.9271813Z Progress (1): 4.5 kB
2026-01-19T16:16:12.9275758Z Progress (1): 10 kB 
2026-01-19T16:16:12.9283450Z Progress (1): 12 kB
2026-01-19T16:16:12.9287076Z                    
2026-01-19T16:16:12.9287729Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.92.Final/netty-common-4.1.92.Final.pom (12 kB at 437 kB/s)
2026-01-19T16:16:12.9362677Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.92.Final/netty-codec-http-4.1.92.Final.pom
2026-01-19T16:16:12.9597485Z Progress (1): 810 B
2026-01-19T16:16:12.9597957Z Progress (1): 4.2 kB
2026-01-19T16:16:12.9598386Z Progress (1): 4.2 kB
2026-01-19T16:16:12.9598742Z                     
2026-01-19T16:16:12.9599327Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.92.Final/netty-codec-http-4.1.92.Final.pom (4.2 kB at 175 kB/s)
2026-01-19T16:16:12.9647466Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.92.Final/netty-transport-4.1.92.Final.pom
2026-01-19T16:16:12.9881408Z Progress (1): 859 B
2026-01-19T16:16:12.9884750Z Progress (1): 2.2 kB
2026-01-19T16:16:12.9887164Z                     
2026-01-19T16:16:12.9887638Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.92.Final/netty-transport-4.1.92.Final.pom (2.2 kB at 90 kB/s)
2026-01-19T16:16:12.9925819Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.92.Final/netty-resolver-4.1.92.Final.pom
2026-01-19T16:16:13.0154911Z Progress (1): 885 B
2026-01-19T16:16:13.0157928Z Progress (1): 1.6 kB
2026-01-19T16:16:13.0158285Z                     
2026-01-19T16:16:13.0158751Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.92.Final/netty-resolver-4.1.92.Final.pom (1.6 kB at 69 kB/s)
2026-01-19T16:16:13.0201993Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.92.Final/netty-codec-4.1.92.Final.pom
2026-01-19T16:16:13.0412102Z Progress (1): 808 B
2026-01-19T16:16:13.0412974Z Progress (1): 4.3 kB
2026-01-19T16:16:13.0417942Z Progress (1): 5.3 kB
2026-01-19T16:16:13.0418297Z                     
2026-01-19T16:16:13.0418779Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.92.Final/netty-codec-4.1.92.Final.pom (5.3 kB at 241 kB/s)
2026-01-19T16:16:13.0465464Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.92.Final/netty-handler-4.1.92.Final.pom
2026-01-19T16:16:13.0717262Z Progress (1): 801 B
2026-01-19T16:16:13.0717935Z Progress (1): 3.9 kB
2026-01-19T16:16:13.0718479Z Progress (1): 4.6 kB
2026-01-19T16:16:13.0718918Z                     
2026-01-19T16:16:13.0719487Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.92.Final/netty-handler-4.1.92.Final.pom (4.6 kB at 185 kB/s)
2026-01-19T16:16:13.0793181Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.92.Final/netty-transport-native-unix-common-4.1.92.Final.pom
2026-01-19T16:16:13.1025610Z Progress (1): 767 B
2026-01-19T16:16:13.1031261Z Progress (1): 2.2 kB
2026-01-19T16:16:13.1040122Z Progress (1): 4.5 kB
2026-01-19T16:16:13.1044251Z Progress (1): 6.8 kB
2026-01-19T16:16:13.1048749Z Progress (1): 18 kB 
2026-01-19T16:16:13.1053354Z Progress (1): 29 kB
2026-01-19T16:16:13.1059232Z                    
2026-01-19T16:16:13.1061593Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.92.Final/netty-transport-native-unix-common-4.1.92.Final.pom (29 kB at 1.2 MB/s)
2026-01-19T16:16:13.1129994Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.92.Final/netty-transport-classes-epoll-4.1.92.Final.pom
2026-01-19T16:16:13.1371391Z Progress (1): 859 B
2026-01-19T16:16:13.1379689Z Progress (1): 2.1 kB
2026-01-19T16:16:13.1381578Z                     
2026-01-19T16:16:13.1382424Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.92.Final/netty-transport-classes-epoll-4.1.92.Final.pom (2.1 kB at 79 kB/s)
2026-01-19T16:16:13.1446187Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.92.Final/netty-transport-classes-kqueue-4.1.92.Final.pom
2026-01-19T16:16:13.1678983Z Progress (1): 859 B
2026-01-19T16:16:13.1682277Z Progress (1): 2.1 kB
2026-01-19T16:16:13.1686792Z                     
2026-01-19T16:16:13.1687277Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.92.Final/netty-transport-classes-kqueue-4.1.92.Final.pom (2.1 kB at 85 kB/s)
2026-01-19T16:16:13.1749401Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.92.Final/netty-transport-native-epoll-4.1.92.Final.pom
2026-01-19T16:16:13.2007501Z Progress (1): 766 B
2026-01-19T16:16:13.2010975Z Progress (1): 2.1 kB
2026-01-19T16:16:13.2015274Z Progress (1): 3.4 kB
2026-01-19T16:16:13.2040723Z Progress (1): 6.1 kB
2026-01-19T16:16:13.2041374Z Progress (1): 9.0 kB
2026-01-19T16:16:13.2041908Z Progress (1): 18 kB 
2026-01-19T16:16:13.2042217Z Progress (1): 19 kB
2026-01-19T16:16:13.2042485Z                    
2026-01-19T16:16:13.2042922Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.92.Final/netty-transport-native-epoll-4.1.92.Final.pom (19 kB at 662 kB/s)
2026-01-19T16:16:13.2101115Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.92.Final/netty-transport-native-kqueue-4.1.92.Final.pom
2026-01-19T16:16:13.2351448Z Progress (1): 752 B
2026-01-19T16:16:13.2365601Z Progress (1): 2.1 kB
2026-01-19T16:16:13.2369795Z Progress (1): 3.9 kB
2026-01-19T16:16:13.2373646Z Progress (1): 6.2 kB
2026-01-19T16:16:13.2379204Z Progress (1): 19 kB 
2026-01-19T16:16:13.2381148Z Progress (1): 29 kB
2026-01-19T16:16:13.2383341Z Progress (1): 30 kB
2026-01-19T16:16:13.2385119Z                    
2026-01-19T16:16:13.2387337Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.92.Final/netty-transport-native-kqueue-4.1.92.Final.pom (30 kB at 1.1 MB/s)
2026-01-19T16:16:13.2444348Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.26.0/opentelemetry-api-1.26.0.pom
2026-01-19T16:16:13.2703785Z Progress (1): 1.0 kB
2026-01-19T16:16:13.2710199Z Progress (1): 1.8 kB
2026-01-19T16:16:13.2715502Z                     
2026-01-19T16:16:13.2716222Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.26.0/opentelemetry-api-1.26.0.pom (1.8 kB at 66 kB/s)
2026-01-19T16:16:13.2745848Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.26.0/opentelemetry-context-1.26.0.pom
2026-01-19T16:16:13.2988140Z Progress (1): 989 B
2026-01-19T16:16:13.2995261Z Progress (1): 1.6 kB
2026-01-19T16:16:13.3007421Z                     
2026-01-19T16:16:13.3008242Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.26.0/opentelemetry-context-1.26.0.pom (1.6 kB at 63 kB/s)
2026-01-19T16:16:13.3022964Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.26.0/opentelemetry-exporter-logging-1.26.0.pom
2026-01-19T16:16:13.3287472Z Progress (1): 988 B
2026-01-19T16:16:13.3288179Z Progress (1): 2.4 kB
2026-01-19T16:16:13.3288843Z                     
2026-01-19T16:16:13.3289544Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.26.0/opentelemetry-exporter-logging-1.26.0.pom (2.4 kB at 89 kB/s)
2026-01-19T16:16:13.3305653Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.26.0/opentelemetry-sdk-1.26.0.pom
2026-01-19T16:16:13.3545904Z Progress (1): 994 B
2026-01-19T16:16:13.3553240Z Progress (1): 2.6 kB
2026-01-19T16:16:13.3557004Z                     
2026-01-19T16:16:13.3558323Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.26.0/opentelemetry-sdk-1.26.0.pom (2.6 kB at 102 kB/s)
2026-01-19T16:16:13.3579164Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.26.0/opentelemetry-sdk-common-1.26.0.pom
2026-01-19T16:16:13.3824328Z Progress (1): 995 B
2026-01-19T16:16:13.3825424Z Progress (1): 2.0 kB
2026-01-19T16:16:13.3826328Z                     
2026-01-19T16:16:13.3827212Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.26.0/opentelemetry-sdk-common-1.26.0.pom (2.0 kB at 79 kB/s)
2026-01-19T16:16:13.3890017Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.26.0-alpha/opentelemetry-semconv-1.26.0-alpha.pom
2026-01-19T16:16:13.4158726Z Progress (1): 985 B
2026-01-19T16:16:13.4159085Z Progress (1): 1.8 kB
2026-01-19T16:16:13.4162193Z                     
2026-01-19T16:16:13.4165936Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.26.0-alpha/opentelemetry-semconv-1.26.0-alpha.pom (1.8 kB at 67 kB/s)
2026-01-19T16:16:13.4203627Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.26.0/opentelemetry-sdk-trace-1.26.0.pom
2026-01-19T16:16:13.4439529Z Progress (1): 977 B
2026-01-19T16:16:13.4445951Z Progress (1): 2.2 kB
2026-01-19T16:16:13.4446297Z                     
2026-01-19T16:16:13.4446975Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.26.0/opentelemetry-sdk-trace-1.26.0.pom (2.2 kB at 87 kB/s)
2026-01-19T16:16:13.4480288Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.26.0/opentelemetry-sdk-metrics-1.26.0.pom
2026-01-19T16:16:13.4721781Z Progress (1): 989 B
2026-01-19T16:16:13.4726001Z Progress (1): 2.2 kB
2026-01-19T16:16:13.4726982Z                     
2026-01-19T16:16:13.4727435Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.26.0/opentelemetry-sdk-metrics-1.26.0.pom (2.2 kB at 88 kB/s)
2026-01-19T16:16:13.4778513Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-extension-incubator/1.26.0-alpha/opentelemetry-extension-incubator-1.26.0-alpha.pom
2026-01-19T16:16:13.5006370Z Progress (1): 990 B
2026-01-19T16:16:13.5010885Z Progress (1): 1.8 kB
2026-01-19T16:16:13.5011625Z                     
2026-01-19T16:16:13.5012431Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-extension-incubator/1.26.0-alpha/opentelemetry-extension-incubator-1.26.0-alpha.pom (1.8 kB at 72 kB/s)
2026-01-19T16:16:13.5045124Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.26.0-alpha/opentelemetry-sdk-logs-1.26.0-alpha.pom
2026-01-19T16:16:13.5283675Z Progress (1): 975 B
2026-01-19T16:16:13.5288109Z Progress (1): 2.2 kB
2026-01-19T16:16:13.5292458Z                     
2026-01-19T16:16:13.5295058Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.26.0-alpha/opentelemetry-sdk-logs-1.26.0-alpha.pom (2.2 kB at 91 kB/s)
2026-01-19T16:16:13.5307891Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-logs/1.26.0-alpha/opentelemetry-api-logs-1.26.0-alpha.pom
2026-01-19T16:16:13.5534230Z Progress (1): 985 B
2026-01-19T16:16:13.5536968Z Progress (1): 1.8 kB
2026-01-19T16:16:13.5537503Z                     
2026-01-19T16:16:13.5538068Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-logs/1.26.0-alpha/opentelemetry-api-logs-1.26.0-alpha.pom (1.8 kB at 78 kB/s)
2026-01-19T16:16:13.5554912Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.26.0-alpha/opentelemetry-api-events-1.26.0-alpha.pom
2026-01-19T16:16:13.5842575Z Progress (1): 989 B
2026-01-19T16:16:13.5851848Z Progress (1): 1.8 kB
2026-01-19T16:16:13.5852179Z                     
2026-01-19T16:16:13.5852638Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.26.0-alpha/opentelemetry-api-events-1.26.0-alpha.pom (1.8 kB at 62 kB/s)
2026-01-19T16:16:13.5869882Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.26.0/opentelemetry-sdk-extension-autoconfigure-spi-1.26.0.pom
2026-01-19T16:16:13.6092971Z Progress (1): 964 B
2026-01-19T16:16:13.6106076Z Progress (1): 2.2 kB
2026-01-19T16:16:13.6106449Z                     
2026-01-19T16:16:13.6109524Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.26.0/opentelemetry-sdk-extension-autoconfigure-spi-1.26.0.pom (2.2 kB at 96 kB/s)
2026-01-19T16:16:13.6132278Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.26.0-alpha/opentelemetry-sdk-extension-autoconfigure-1.26.0-alpha.pom
2026-01-19T16:16:13.6368794Z Progress (1): 962 B
2026-01-19T16:16:13.6377307Z Progress (1): 2.6 kB
2026-01-19T16:16:13.6378018Z                     
2026-01-19T16:16:13.6378836Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.26.0-alpha/opentelemetry-sdk-extension-autoconfigure-1.26.0-alpha.pom (2.6 kB at 101 kB/s)
2026-01-19T16:16:13.6437307Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.10.0/selenium-http-4.10.0.pom
2026-01-19T16:16:13.6662722Z Progress (1): 1.1 kB
2026-01-19T16:16:13.6663070Z Progress (1): 2.8 kB
2026-01-19T16:16:13.6663352Z                     
2026-01-19T16:16:13.6663772Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.10.0/selenium-http-4.10.0.pom (2.8 kB at 117 kB/s)
2026-01-19T16:16:13.6691496Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.10.0/selenium-json-4.10.0.pom
2026-01-19T16:16:13.6915838Z Progress (1): 1.1 kB
2026-01-19T16:16:13.6927407Z Progress (1): 2.3 kB
2026-01-19T16:16:13.6932732Z                     
2026-01-19T16:16:13.6934448Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.10.0/selenium-json-4.10.0.pom (2.3 kB at 91 kB/s)
2026-01-19T16:16:13.6987884Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.10.0/selenium-manager-4.10.0.pom
2026-01-19T16:16:13.7227057Z Progress (1): 1.1 kB
2026-01-19T16:16:13.7234122Z Progress (1): 2.6 kB
2026-01-19T16:16:13.7234416Z                     
2026-01-19T16:16:13.7234859Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.10.0/selenium-manager-4.10.0.pom (2.6 kB at 101 kB/s)
2026-01-19T16:16:13.7256689Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.11.0/selenium-remote-driver-4.11.0.pom
2026-01-19T16:16:13.7505951Z Progress (1): 1.0 kB
2026-01-19T16:16:13.7506895Z Progress (1): 6.7 kB
2026-01-19T16:16:13.7527213Z Progress (1): 7.9 kB
2026-01-19T16:16:13.7531141Z                     
2026-01-19T16:16:13.7532283Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.11.0/selenium-remote-driver-4.11.0.pom (7.9 kB at 316 kB/s)
2026-01-19T16:16:13.7563667Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.11.0/selenium-http-4.11.0.pom
2026-01-19T16:16:13.7795004Z Progress (1): 1.1 kB
2026-01-19T16:16:13.7795636Z Progress (1): 2.8 kB
2026-01-19T16:16:13.7797985Z                     
2026-01-19T16:16:13.7798457Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.11.0/selenium-http-4.11.0.pom (2.8 kB at 117 kB/s)
2026-01-19T16:16:13.7823470Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.11.0/selenium-json-4.11.0.pom
2026-01-19T16:16:13.8041039Z Progress (1): 1.1 kB
2026-01-19T16:16:13.8068175Z Progress (1): 2.3 kB
2026-01-19T16:16:13.8068700Z                     
2026-01-19T16:16:13.8069838Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.11.0/selenium-json-4.11.0.pom (2.3 kB at 99 kB/s)
2026-01-19T16:16:13.8115905Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.11.0/selenium-manager-4.11.0.pom
2026-01-19T16:16:13.8362719Z Progress (1): 1.1 kB
2026-01-19T16:16:13.8368028Z Progress (1): 2.6 kB
2026-01-19T16:16:13.8369094Z                     
2026-01-19T16:16:13.8369825Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.11.0/selenium-manager-4.11.0.pom (2.6 kB at 101 kB/s)
2026-01-19T16:16:13.8396233Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.12.0/selenium-remote-driver-4.12.0.pom
2026-01-19T16:16:13.8637650Z Progress (1): 1.0 kB
2026-01-19T16:16:13.8638062Z Progress (1): 6.7 kB
2026-01-19T16:16:13.8642450Z Progress (1): 7.9 kB
2026-01-19T16:16:13.8643114Z                     
2026-01-19T16:16:13.8643834Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.12.0/selenium-remote-driver-4.12.0.pom (7.9 kB at 316 kB/s)
2026-01-19T16:16:13.8664129Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.1.1/auto-service-annotations-1.1.1.pom
2026-01-19T16:16:13.8904526Z Progress (1): 832 B
2026-01-19T16:16:13.8910449Z Progress (1): 2.3 kB
2026-01-19T16:16:13.8911089Z                     
2026-01-19T16:16:13.8912779Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.1.1/auto-service-annotations-1.1.1.pom (2.3 kB at 95 kB/s)
2026-01-19T16:16:13.8930551Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-aggregator/1.1.1/auto-service-aggregator-1.1.1.pom
2026-01-19T16:16:13.9154639Z Progress (1): 813 B
2026-01-19T16:16:13.9156821Z Progress (1): 2.4 kB
2026-01-19T16:16:13.9162714Z Progress (1): 4.3 kB
2026-01-19T16:16:13.9163041Z                     
2026-01-19T16:16:13.9163495Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-aggregator/1.1.1/auto-service-aggregator-1.1.1.pom (4.3 kB at 185 kB/s)
2026-01-19T16:16:13.9188813Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/32.1.2-jre/guava-32.1.2-jre.pom
2026-01-19T16:16:13.9425677Z Progress (1): 850 B
2026-01-19T16:16:13.9426439Z Progress (1): 2.5 kB
2026-01-19T16:16:13.9427120Z Progress (1): 4.6 kB
2026-01-19T16:16:13.9427526Z Progress (1): 6.2 kB
2026-01-19T16:16:13.9427914Z Progress (1): 8.1 kB
2026-01-19T16:16:13.9428251Z Progress (1): 11 kB 
2026-01-19T16:16:13.9433954Z Progress (1): 13 kB
2026-01-19T16:16:13.9437658Z                    
2026-01-19T16:16:13.9438355Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/32.1.2-jre/guava-32.1.2-jre.pom (13 kB at 514 kB/s)
2026-01-19T16:16:13.9457503Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/32.1.2-jre/guava-parent-32.1.2-jre.pom
2026-01-19T16:16:13.9695889Z Progress (1): 887 B
2026-01-19T16:16:13.9702391Z Progress (1): 2.6 kB
2026-01-19T16:16:13.9703820Z Progress (1): 4.8 kB
2026-01-19T16:16:13.9704269Z Progress (1): 6.7 kB
2026-01-19T16:16:13.9704708Z Progress (1): 9.4 kB
2026-01-19T16:16:13.9705097Z Progress (1): 11 kB 
2026-01-19T16:16:13.9705507Z Progress (1): 14 kB
2026-01-19T16:16:13.9705864Z Progress (1): 16 kB
2026-01-19T16:16:13.9706198Z Progress (1): 18 kB
2026-01-19T16:16:13.9717062Z Progress (1): 20 kB
2026-01-19T16:16:13.9717969Z                    
2026-01-19T16:16:13.9718406Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/32.1.2-jre/guava-parent-32.1.2-jre.pom (20 kB at 796 kB/s)
2026-01-19T16:16:13.9746788Z Downloading from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.33.0/checker-qual-3.33.0.pom
2026-01-19T16:16:13.9973728Z Progress (1): 952 B
2026-01-19T16:16:13.9979527Z Progress (1): 2.1 kB
2026-01-19T16:16:13.9980131Z                     
2026-01-19T16:16:13.9981982Z Downloaded from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.33.0/checker-qual-3.33.0.pom (2.1 kB at 87 kB/s)
2026-01-19T16:16:14.0007166Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.18.0/error_prone_annotations-2.18.0.pom
2026-01-19T16:16:14.0228173Z Progress (1): 835 B
2026-01-19T16:16:14.0232532Z Progress (1): 2.2 kB
2026-01-19T16:16:14.0233186Z                     
2026-01-19T16:16:14.0235816Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.18.0/error_prone_annotations-2.18.0.pom (2.2 kB at 90 kB/s)
2026-01-19T16:16:14.0259073Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.18.0/error_prone_parent-2.18.0.pom
2026-01-19T16:16:14.0481345Z Progress (1): 722 B
2026-01-19T16:16:14.0484079Z Progress (1): 2.2 kB
2026-01-19T16:16:14.0484763Z Progress (1): 4.2 kB
2026-01-19T16:16:14.0485300Z Progress (1): 8.5 kB
2026-01-19T16:16:14.0489178Z Progress (1): 11 kB 
2026-01-19T16:16:14.0489570Z                    
2026-01-19T16:16:14.0490149Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_parent/2.18.0/error_prone_parent-2.18.0.pom (11 kB at 482 kB/s)
2026-01-19T16:16:14.0520276Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/2.8/j2objc-annotations-2.8.pom
2026-01-19T16:16:14.0743934Z Progress (1): 859 B
2026-01-19T16:16:14.0744696Z Progress (1): 2.9 kB
2026-01-19T16:16:14.0746117Z                     
2026-01-19T16:16:14.0746894Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/2.8/j2objc-annotations-2.8.pom (2.9 kB at 127 kB/s)
2026-01-19T16:16:14.0770542Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.96.Final/netty-buffer-4.1.96.Final.pom
2026-01-19T16:16:14.1004682Z Progress (1): 884 B
2026-01-19T16:16:14.1022129Z Progress (1): 1.6 kB
2026-01-19T16:16:14.1024598Z                     
2026-01-19T16:16:14.1025457Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.96.Final/netty-buffer-4.1.96.Final.pom (1.6 kB at 66 kB/s)
2026-01-19T16:16:14.1036895Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.96.Final/netty-parent-4.1.96.Final.pom
2026-01-19T16:16:14.1306734Z Progress (1): 717 B
2026-01-19T16:16:14.1308379Z Progress (1): 2.1 kB
2026-01-19T16:16:14.1309963Z Progress (1): 4.2 kB
2026-01-19T16:16:14.1313936Z Progress (1): 7.0 kB
2026-01-19T16:16:14.1318176Z Progress (1): 8.5 kB
2026-01-19T16:16:14.1322166Z Progress (1): 19 kB 
2026-01-19T16:16:14.1327157Z Progress (1): 22 kB
2026-01-19T16:16:14.1328145Z Progress (1): 24 kB
2026-01-19T16:16:14.1328746Z Progress (1): 26 kB
2026-01-19T16:16:14.1330033Z Progress (1): 29 kB
2026-01-19T16:16:14.1330614Z Progress (1): 32 kB
2026-01-19T16:16:14.1331294Z Progress (1): 36 kB
2026-01-19T16:16:14.1331921Z Progress (1): 41 kB
2026-01-19T16:16:14.1332230Z Progress (1): 44 kB
2026-01-19T16:16:14.1332537Z Progress (1): 47 kB
2026-01-19T16:16:14.1332831Z Progress (1): 47 kB
2026-01-19T16:16:14.1333119Z Progress (1): 51 kB
2026-01-19T16:16:14.1333411Z Progress (1): 54 kB
2026-01-19T16:16:14.1333695Z Progress (1): 56 kB
2026-01-19T16:16:14.1333986Z Progress (1): 59 kB
2026-01-19T16:16:14.1334281Z Progress (1): 61 kB
2026-01-19T16:16:14.1334578Z Progress (1): 64 kB
2026-01-19T16:16:14.1335788Z Progress (1): 66 kB
2026-01-19T16:16:14.1336175Z Progress (1): 69 kB
2026-01-19T16:16:14.1336673Z Progress (1): 72 kB
2026-01-19T16:16:14.1336969Z Progress (1): 76 kB
2026-01-19T16:16:14.1337263Z Progress (1): 81 kB
2026-01-19T16:16:14.1337576Z Progress (1): 83 kB
2026-01-19T16:16:14.1341139Z                    
2026-01-19T16:16:14.1342482Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-parent/4.1.96.Final/netty-parent-4.1.96.Final.pom (83 kB at 2.8 MB/s)
2026-01-19T16:16:14.1393047Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.96.Final/netty-common-4.1.96.Final.pom
2026-01-19T16:16:14.1644863Z Progress (1): 1.3 kB
2026-01-19T16:16:14.1645611Z Progress (1): 4.5 kB
2026-01-19T16:16:14.1648491Z Progress (1): 10 kB 
2026-01-19T16:16:14.1649170Z Progress (1): 12 kB
2026-01-19T16:16:14.1649733Z                    
2026-01-19T16:16:14.1650996Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.96.Final/netty-common-4.1.96.Final.pom (12 kB at 453 kB/s)
2026-01-19T16:16:14.1901850Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.96.Final/netty-codec-http-4.1.96.Final.pom
2026-01-19T16:16:14.2132522Z Progress (1): 810 B
2026-01-19T16:16:14.2135083Z Progress (1): 4.2 kB
2026-01-19T16:16:14.2140978Z Progress (1): 4.2 kB
2026-01-19T16:16:14.2142836Z                     
2026-01-19T16:16:14.2143278Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.96.Final/netty-codec-http-4.1.96.Final.pom (4.2 kB at 156 kB/s)
2026-01-19T16:16:14.2208374Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.96.Final/netty-transport-4.1.96.Final.pom
2026-01-19T16:16:14.2450002Z Progress (1): 859 B
2026-01-19T16:16:14.2454355Z Progress (1): 2.2 kB
2026-01-19T16:16:14.2457099Z                     
2026-01-19T16:16:14.2457904Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.96.Final/netty-transport-4.1.96.Final.pom (2.2 kB at 83 kB/s)
2026-01-19T16:16:14.2508674Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.96.Final/netty-resolver-4.1.96.Final.pom
2026-01-19T16:16:14.2723646Z Progress (1): 885 B
2026-01-19T16:16:14.2730621Z Progress (1): 1.6 kB
2026-01-19T16:16:14.2730952Z                     
2026-01-19T16:16:14.2731358Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.96.Final/netty-resolver-4.1.96.Final.pom (1.6 kB at 69 kB/s)
2026-01-19T16:16:14.2787850Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.96.Final/netty-codec-4.1.96.Final.pom
2026-01-19T16:16:14.2999685Z Progress (1): 808 B
2026-01-19T16:16:14.3000303Z Progress (1): 4.3 kB
2026-01-19T16:16:14.3000873Z Progress (1): 5.3 kB
2026-01-19T16:16:14.3001483Z                     
2026-01-19T16:16:14.3002054Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.96.Final/netty-codec-4.1.96.Final.pom (5.3 kB at 230 kB/s)
2026-01-19T16:16:14.3063507Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.96.Final/netty-handler-4.1.96.Final.pom
2026-01-19T16:16:14.3306685Z Progress (1): 801 B
2026-01-19T16:16:14.3307489Z Progress (1): 3.9 kB
2026-01-19T16:16:14.3308055Z Progress (1): 4.6 kB
2026-01-19T16:16:14.3308810Z                     
2026-01-19T16:16:14.3309433Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.96.Final/netty-handler-4.1.96.Final.pom (4.6 kB at 201 kB/s)
2026-01-19T16:16:14.3393379Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.96.Final/netty-transport-native-unix-common-4.1.96.Final.pom
2026-01-19T16:16:14.3657795Z Progress (1): 767 B
2026-01-19T16:16:14.3658412Z Progress (1): 2.2 kB
2026-01-19T16:16:14.3658976Z Progress (1): 4.5 kB
2026-01-19T16:16:14.3659583Z Progress (1): 6.8 kB
2026-01-19T16:16:14.3660119Z Progress (1): 18 kB 
2026-01-19T16:16:14.3662689Z Progress (1): 29 kB
2026-01-19T16:16:14.3663194Z                    
2026-01-19T16:16:14.3665484Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.96.Final/netty-transport-native-unix-common-4.1.96.Final.pom (29 kB at 1.0 MB/s)
2026-01-19T16:16:14.3727434Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.96.Final/netty-transport-classes-epoll-4.1.96.Final.pom
2026-01-19T16:16:14.3989810Z Progress (1): 850 B
2026-01-19T16:16:14.3994370Z Progress (1): 2.1 kB
2026-01-19T16:16:14.3997233Z                     
2026-01-19T16:16:14.3997953Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.96.Final/netty-transport-classes-epoll-4.1.96.Final.pom (2.1 kB at 76 kB/s)
2026-01-19T16:16:14.4036252Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.96.Final/netty-transport-classes-kqueue-4.1.96.Final.pom
2026-01-19T16:16:14.4341251Z Progress (1): 859 B
2026-01-19T16:16:14.4341668Z Progress (1): 2.1 kB
2026-01-19T16:16:14.4341964Z                     
2026-01-19T16:16:14.4342450Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.96.Final/netty-transport-classes-kqueue-4.1.96.Final.pom (2.1 kB at 67 kB/s)
2026-01-19T16:16:14.4384343Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final.pom
2026-01-19T16:16:14.4627115Z Progress (1): 766 B
2026-01-19T16:16:14.4628010Z Progress (1): 2.1 kB
2026-01-19T16:16:14.4628416Z Progress (1): 3.4 kB
2026-01-19T16:16:14.4629613Z Progress (1): 6.1 kB
2026-01-19T16:16:14.4630047Z Progress (1): 9.0 kB
2026-01-19T16:16:14.4630905Z Progress (1): 18 kB 
2026-01-19T16:16:14.4669555Z Progress (1): 19 kB
2026-01-19T16:16:14.4671763Z                    
2026-01-19T16:16:14.4673740Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final.pom (19 kB at 662 kB/s)
2026-01-19T16:16:14.4741575Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final.pom
2026-01-19T16:16:14.4955980Z Progress (1): 752 B
2026-01-19T16:16:14.4961101Z Progress (1): 2.1 kB
2026-01-19T16:16:14.4965960Z Progress (1): 3.9 kB
2026-01-19T16:16:14.4971808Z Progress (1): 6.2 kB
2026-01-19T16:16:14.4974778Z Progress (1): 19 kB 
2026-01-19T16:16:14.4976661Z Progress (1): 29 kB
2026-01-19T16:16:14.4982183Z Progress (1): 30 kB
2026-01-19T16:16:14.4982867Z                    
2026-01-19T16:16:14.4983653Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final.pom (30 kB at 1.1 MB/s)
2026-01-19T16:16:14.5032309Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.28.0/opentelemetry-api-1.28.0.pom
2026-01-19T16:16:14.5277613Z Progress (1): 1.0 kB
2026-01-19T16:16:14.5281569Z Progress (1): 1.8 kB
2026-01-19T16:16:14.5282305Z                     
2026-01-19T16:16:14.5282855Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.28.0/opentelemetry-api-1.28.0.pom (1.8 kB at 68 kB/s)
2026-01-19T16:16:14.5315076Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.28.0/opentelemetry-context-1.28.0.pom
2026-01-19T16:16:14.5561163Z Progress (1): 989 B
2026-01-19T16:16:14.5566208Z Progress (1): 1.6 kB
2026-01-19T16:16:14.5571335Z                     
2026-01-19T16:16:14.5573019Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.28.0/opentelemetry-context-1.28.0.pom (1.6 kB at 60 kB/s)
2026-01-19T16:16:14.5588765Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.28.0/opentelemetry-exporter-logging-1.28.0.pom
2026-01-19T16:16:14.5826177Z Progress (1): 986 B
2026-01-19T16:16:14.5827243Z Progress (1): 2.4 kB
2026-01-19T16:16:14.5827654Z                     
2026-01-19T16:16:14.5828247Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.28.0/opentelemetry-exporter-logging-1.28.0.pom (2.4 kB at 100 kB/s)
2026-01-19T16:16:14.5859655Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.28.0/opentelemetry-sdk-1.28.0.pom
2026-01-19T16:16:14.6135507Z Progress (1): 994 B
2026-01-19T16:16:14.6137134Z Progress (1): 2.5 kB
2026-01-19T16:16:14.6137790Z                     
2026-01-19T16:16:14.6139560Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.28.0/opentelemetry-sdk-1.28.0.pom (2.5 kB at 91 kB/s)
2026-01-19T16:16:14.6160855Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.28.0/opentelemetry-sdk-common-1.28.0.pom
2026-01-19T16:16:14.6397589Z Progress (1): 995 B
2026-01-19T16:16:14.6424076Z Progress (1): 2.0 kB
2026-01-19T16:16:14.6424417Z                     
2026-01-19T16:16:14.6424964Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.28.0/opentelemetry-sdk-common-1.28.0.pom (2.0 kB at 83 kB/s)
2026-01-19T16:16:14.6425558Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.28.0-alpha/opentelemetry-semconv-1.28.0-alpha.pom
2026-01-19T16:16:14.6663851Z Progress (1): 985 B
2026-01-19T16:16:14.6670202Z Progress (1): 1.8 kB
2026-01-19T16:16:14.6671493Z                     
2026-01-19T16:16:14.6672014Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.28.0-alpha/opentelemetry-semconv-1.28.0-alpha.pom (1.8 kB at 72 kB/s)
2026-01-19T16:16:14.6689869Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.28.0/opentelemetry-sdk-trace-1.28.0.pom
2026-01-19T16:16:14.6891839Z Progress (1): 978 B
2026-01-19T16:16:14.6897222Z Progress (1): 2.2 kB
2026-01-19T16:16:14.6898497Z                     
2026-01-19T16:16:14.6899012Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.28.0/opentelemetry-sdk-trace-1.28.0.pom (2.2 kB at 104 kB/s)
2026-01-19T16:16:14.6913451Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.28.0/opentelemetry-sdk-metrics-1.28.0.pom
2026-01-19T16:16:14.7188748Z Progress (1): 989 B
2026-01-19T16:16:14.7189407Z Progress (1): 2.2 kB
2026-01-19T16:16:14.7190589Z                     
2026-01-19T16:16:14.7191065Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.28.0/opentelemetry-sdk-metrics-1.28.0.pom (2.2 kB at 88 kB/s)
2026-01-19T16:16:14.7192942Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-extension-incubator/1.28.0-alpha/opentelemetry-extension-incubator-1.28.0-alpha.pom
2026-01-19T16:16:14.7461151Z Progress (1): 990 B
2026-01-19T16:16:14.7464277Z Progress (1): 1.8 kB
2026-01-19T16:16:14.7464679Z                     
2026-01-19T16:16:14.7465197Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-extension-incubator/1.28.0-alpha/opentelemetry-extension-incubator-1.28.0-alpha.pom (1.8 kB at 65 kB/s)
2026-01-19T16:16:14.7483939Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.28.0/opentelemetry-sdk-logs-1.28.0.pom
2026-01-19T16:16:14.7726430Z Progress (1): 982 B
2026-01-19T16:16:14.7732799Z Progress (1): 2.2 kB
2026-01-19T16:16:14.7733434Z                     
2026-01-19T16:16:14.7734835Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.28.0/opentelemetry-sdk-logs-1.28.0.pom (2.2 kB at 87 kB/s)
2026-01-19T16:16:14.7756843Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.28.0-alpha/opentelemetry-api-events-1.28.0-alpha.pom
2026-01-19T16:16:14.7997813Z Progress (1): 989 B
2026-01-19T16:16:14.7998227Z Progress (1): 1.8 kB
2026-01-19T16:16:14.7999042Z                     
2026-01-19T16:16:14.7999582Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.28.0-alpha/opentelemetry-api-events-1.28.0-alpha.pom (1.8 kB at 75 kB/s)
2026-01-19T16:16:14.8018178Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.28.0/opentelemetry-sdk-extension-autoconfigure-spi-1.28.0.pom
2026-01-19T16:16:14.8251108Z Progress (1): 977 B
2026-01-19T16:16:14.8255698Z Progress (1): 1.8 kB
2026-01-19T16:16:14.8256810Z                     
2026-01-19T16:16:14.8257384Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.28.0/opentelemetry-sdk-extension-autoconfigure-spi-1.28.0.pom (1.8 kB at 76 kB/s)
2026-01-19T16:16:14.8280791Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.28.0/opentelemetry-sdk-extension-autoconfigure-1.28.0.pom
2026-01-19T16:16:14.8499503Z Progress (1): 975 B
2026-01-19T16:16:14.8505229Z Progress (1): 2.4 kB
2026-01-19T16:16:14.8505944Z                     
2026-01-19T16:16:14.8507771Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.28.0/opentelemetry-sdk-extension-autoconfigure-1.28.0.pom (2.4 kB at 106 kB/s)
2026-01-19T16:16:14.8526163Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.5/byte-buddy-1.14.5.pom
2026-01-19T16:16:14.8758832Z Progress (1): 958 B
2026-01-19T16:16:14.8759245Z Progress (1): 3.7 kB
2026-01-19T16:16:14.8759612Z Progress (1): 7.0 kB
2026-01-19T16:16:14.8759997Z Progress (1): 14 kB 
2026-01-19T16:16:14.8763194Z Progress (1): 16 kB
2026-01-19T16:16:14.8763819Z                    
2026-01-19T16:16:14.8764596Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.5/byte-buddy-1.14.5.pom (16 kB at 660 kB/s)
2026-01-19T16:16:14.8784380Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.14.5/byte-buddy-parent-1.14.5.pom
2026-01-19T16:16:14.9053639Z Progress (1): 828 B
2026-01-19T16:16:14.9061296Z Progress (1): 2.1 kB
2026-01-19T16:16:14.9062071Z Progress (1): 3.6 kB
2026-01-19T16:16:14.9063383Z Progress (1): 6.2 kB
2026-01-19T16:16:14.9063809Z Progress (1): 8.1 kB
2026-01-19T16:16:14.9064197Z Progress (1): 11 kB 
2026-01-19T16:16:14.9064619Z Progress (1): 13 kB
2026-01-19T16:16:14.9065045Z Progress (1): 17 kB
2026-01-19T16:16:14.9065429Z Progress (1): 22 kB
2026-01-19T16:16:14.9065851Z Progress (1): 25 kB
2026-01-19T16:16:14.9066267Z Progress (1): 36 kB
2026-01-19T16:16:14.9066844Z Progress (1): 45 kB
2026-01-19T16:16:14.9067176Z Progress (1): 50 kB
2026-01-19T16:16:14.9067493Z Progress (1): 54 kB
2026-01-19T16:16:14.9077421Z Progress (1): 58 kB
2026-01-19T16:16:14.9077735Z                    
2026-01-19T16:16:14.9078173Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.14.5/byte-buddy-parent-1.14.5.pom (58 kB at 1.9 MB/s)
2026-01-19T16:16:14.9119525Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.12.0/selenium-http-4.12.0.pom
2026-01-19T16:16:14.9345706Z Progress (1): 1.1 kB
2026-01-19T16:16:14.9353367Z Progress (1): 2.8 kB
2026-01-19T16:16:14.9354933Z                     
2026-01-19T16:16:14.9355574Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.12.0/selenium-http-4.12.0.pom (2.8 kB at 117 kB/s)
2026-01-19T16:16:14.9381891Z Downloading from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.2/failsafe-3.3.2.pom
2026-01-19T16:16:14.9609370Z Progress (1): 1.0 kB
2026-01-19T16:16:14.9609775Z                     
2026-01-19T16:16:14.9610260Z Downloaded from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.2/failsafe-3.3.2.pom (1.0 kB at 44 kB/s)
2026-01-19T16:16:14.9623792Z Downloading from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe-parent/3.3.2/failsafe-parent-3.3.2.pom
2026-01-19T16:16:14.9842416Z Progress (1): 1.1 kB
2026-01-19T16:16:14.9849695Z Progress (1): 3.4 kB
2026-01-19T16:16:14.9850224Z Progress (1): 5.8 kB
2026-01-19T16:16:14.9850669Z Progress (1): 8.7 kB
2026-01-19T16:16:14.9852095Z Progress (1): 9.2 kB
2026-01-19T16:16:14.9866215Z                     
2026-01-19T16:16:14.9867038Z Downloaded from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe-parent/3.3.2/failsafe-parent-3.3.2.pom (9.2 kB at 399 kB/s)
2026-01-19T16:16:14.9878681Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.12.0/selenium-json-4.12.0.pom
2026-01-19T16:16:15.0105767Z Progress (1): 1.1 kB
2026-01-19T16:16:15.0111433Z Progress (1): 2.3 kB
2026-01-19T16:16:15.0112370Z                     
2026-01-19T16:16:15.0114875Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.12.0/selenium-json-4.12.0.pom (2.3 kB at 94 kB/s)
2026-01-19T16:16:15.0141599Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.12.0/selenium-manager-4.12.0.pom
2026-01-19T16:16:15.0353434Z Progress (1): 1.1 kB
2026-01-19T16:16:15.0363410Z Progress (1): 2.8 kB
2026-01-19T16:16:15.0363809Z                     
2026-01-19T16:16:15.0364317Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.12.0/selenium-manager-4.12.0.pom (2.8 kB at 118 kB/s)
2026-01-19T16:16:15.0384057Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.12.0/selenium-os-4.12.0.pom
2026-01-19T16:16:15.0623724Z Progress (1): 1.1 kB
2026-01-19T16:16:15.0643852Z Progress (1): 2.6 kB
2026-01-19T16:16:15.0644485Z                     
2026-01-19T16:16:15.0645147Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.12.0/selenium-os-4.12.0.pom (2.6 kB at 109 kB/s)
2026-01-19T16:16:15.0660258Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.12.1/selenium-remote-driver-4.12.1.pom
2026-01-19T16:16:15.0979027Z Progress (1): 1.0 kB
2026-01-19T16:16:15.0980403Z Progress (1): 6.7 kB
2026-01-19T16:16:15.0983201Z Progress (1): 7.9 kB
2026-01-19T16:16:15.0985658Z                     
2026-01-19T16:16:15.0986825Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.12.1/selenium-remote-driver-4.12.1.pom (7.9 kB at 240 kB/s)
2026-01-19T16:16:15.1017622Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.12.1/selenium-http-4.12.1.pom
2026-01-19T16:16:15.1249319Z Progress (1): 1.1 kB
2026-01-19T16:16:15.1260911Z Progress (1): 2.8 kB
2026-01-19T16:16:15.1261494Z                     
2026-01-19T16:16:15.1262192Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.12.1/selenium-http-4.12.1.pom (2.8 kB at 117 kB/s)
2026-01-19T16:16:15.1314649Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.12.1/selenium-json-4.12.1.pom
2026-01-19T16:16:15.1553523Z Progress (1): 1.1 kB
2026-01-19T16:16:15.1557407Z Progress (1): 2.3 kB
2026-01-19T16:16:15.1560957Z                     
2026-01-19T16:16:15.1564622Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.12.1/selenium-json-4.12.1.pom (2.3 kB at 87 kB/s)
2026-01-19T16:16:15.1596853Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.12.1/selenium-manager-4.12.1.pom
2026-01-19T16:16:15.1849153Z Progress (1): 1.1 kB
2026-01-19T16:16:15.1852943Z Progress (1): 2.8 kB
2026-01-19T16:16:15.1856858Z                     
2026-01-19T16:16:15.1859453Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.12.1/selenium-manager-4.12.1.pom (2.8 kB at 113 kB/s)
2026-01-19T16:16:15.1914688Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.12.1/selenium-os-4.12.1.pom
2026-01-19T16:16:15.2133795Z Progress (1): 1.1 kB
2026-01-19T16:16:15.2139681Z Progress (1): 2.6 kB
2026-01-19T16:16:15.2144781Z                     
2026-01-19T16:16:15.2146964Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.12.1/selenium-os-4.12.1.pom (2.6 kB at 105 kB/s)
2026-01-19T16:16:15.2189882Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.13.0/selenium-remote-driver-4.13.0.pom
2026-01-19T16:16:15.2458499Z Progress (1): 1.0 kB
2026-01-19T16:16:15.2460209Z Progress (1): 6.7 kB
2026-01-19T16:16:15.2465919Z Progress (1): 7.9 kB
2026-01-19T16:16:15.2466255Z                     
2026-01-19T16:16:15.2466997Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.13.0/selenium-remote-driver-4.13.0.pom (7.9 kB at 293 kB/s)
2026-01-19T16:16:15.2498495Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.13.0/selenium-http-4.13.0.pom
2026-01-19T16:16:15.2852140Z Progress (1): 1.1 kB
2026-01-19T16:16:15.2860936Z Progress (1): 2.8 kB
2026-01-19T16:16:15.2864045Z                     
2026-01-19T16:16:15.2864826Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.13.0/selenium-http-4.13.0.pom (2.8 kB at 78 kB/s)
2026-01-19T16:16:15.2903996Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.13.0/selenium-json-4.13.0.pom
2026-01-19T16:16:15.3158962Z Progress (1): 1.1 kB
2026-01-19T16:16:15.3159308Z Progress (1): 2.3 kB
2026-01-19T16:16:15.3159609Z                     
2026-01-19T16:16:15.3160019Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.13.0/selenium-json-4.13.0.pom (2.3 kB at 94 kB/s)
2026-01-19T16:16:15.3173797Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.13.0/selenium-manager-4.13.0.pom
2026-01-19T16:16:15.3419182Z Progress (1): 1.1 kB
2026-01-19T16:16:15.3425388Z Progress (1): 2.8 kB
2026-01-19T16:16:15.3427994Z                     
2026-01-19T16:16:15.3428472Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.13.0/selenium-manager-4.13.0.pom (2.8 kB at 108 kB/s)
2026-01-19T16:16:15.3468642Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.13.0/selenium-os-4.13.0.pom
2026-01-19T16:16:15.3715893Z Progress (1): 1.1 kB
2026-01-19T16:16:15.3725915Z Progress (1): 2.6 kB
2026-01-19T16:16:15.3726365Z                     
2026-01-19T16:16:15.3727099Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.13.0/selenium-os-4.13.0.pom (2.6 kB at 93 kB/s)
2026-01-19T16:16:15.3754335Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/maven-metadata.xml
2026-01-19T16:16:15.4001154Z Progress (1): 4.5 kB
2026-01-19T16:16:15.4001829Z Progress (1): 6.3 kB
2026-01-19T16:16:15.4002242Z                     
2026-01-19T16:16:15.4002758Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/maven-metadata.xml (6.3 kB at 263 kB/s)
2026-01-19T16:16:15.4058377Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.9.1/selenium-support-4.9.1.pom
2026-01-19T16:16:15.4293904Z Progress (1): 1.1 kB
2026-01-19T16:16:15.4303638Z Progress (1): 3.4 kB
2026-01-19T16:16:15.4307223Z                     
2026-01-19T16:16:15.4307758Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.9.1/selenium-support-4.9.1.pom (3.4 kB at 141 kB/s)
2026-01-19T16:16:15.4332084Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.10.0/selenium-support-4.10.0.pom
2026-01-19T16:16:15.4588045Z Progress (1): 1.1 kB
2026-01-19T16:16:15.4595344Z Progress (1): 3.4 kB
2026-01-19T16:16:15.4596371Z                     
2026-01-19T16:16:15.4597976Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.10.0/selenium-support-4.10.0.pom (3.4 kB at 125 kB/s)
2026-01-19T16:16:15.4644923Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.11.0/selenium-support-4.11.0.pom
2026-01-19T16:16:15.4862079Z Progress (1): 1.1 kB
2026-01-19T16:16:15.4868341Z Progress (1): 3.2 kB
2026-01-19T16:16:15.4869015Z                     
2026-01-19T16:16:15.4869458Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.11.0/selenium-support-4.11.0.pom (3.2 kB at 128 kB/s)
2026-01-19T16:16:15.4893888Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.12.0/selenium-support-4.12.0.pom
2026-01-19T16:16:15.5141809Z Progress (1): 1.1 kB
2026-01-19T16:16:15.5167350Z Progress (1): 3.2 kB
2026-01-19T16:16:15.5168643Z                     
2026-01-19T16:16:15.5169212Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.12.0/selenium-support-4.12.0.pom (3.2 kB at 128 kB/s)
2026-01-19T16:16:15.5184995Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.12.1/selenium-support-4.12.1.pom
2026-01-19T16:16:15.5428047Z Progress (1): 1.1 kB
2026-01-19T16:16:15.5428639Z Progress (1): 3.2 kB
2026-01-19T16:16:15.5430081Z                     
2026-01-19T16:16:15.5430628Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.12.1/selenium-support-4.12.1.pom (3.2 kB at 133 kB/s)
2026-01-19T16:16:15.5434087Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.13.0/selenium-support-4.13.0.pom
2026-01-19T16:16:15.5687259Z Progress (1): 1.1 kB
2026-01-19T16:16:15.5689085Z Progress (1): 3.2 kB
2026-01-19T16:16:15.5689872Z                     
2026-01-19T16:16:15.5691856Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.13.0/selenium-support-4.13.0.pom (3.2 kB at 123 kB/s)
2026-01-19T16:16:15.5712619Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.pom
2026-01-19T16:16:15.5949148Z Progress (1): 1.1 kB
2026-01-19T16:16:15.5953934Z Progress (1): 3.4 kB
2026-01-19T16:16:15.5958750Z Progress (1): 6.6 kB
2026-01-19T16:16:15.5963772Z Progress (1): 8.7 kB
2026-01-19T16:16:15.5973846Z Progress (1): 9.4 kB
2026-01-19T16:16:15.5974163Z                     
2026-01-19T16:16:15.5974578Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.pom (9.4 kB at 360 kB/s)
2026-01-19T16:16:15.5998326Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson-parent/2.10.1/gson-parent-2.10.1.pom
2026-01-19T16:16:15.6282164Z Progress (1): 1.1 kB
2026-01-19T16:16:15.6288412Z Progress (1): 2.7 kB
2026-01-19T16:16:15.6288815Z Progress (1): 4.3 kB
2026-01-19T16:16:15.6289161Z Progress (1): 6.5 kB
2026-01-19T16:16:15.6289482Z Progress (1): 8.5 kB
2026-01-19T16:16:15.6289803Z Progress (1): 11 kB 
2026-01-19T16:16:15.6290112Z Progress (1): 13 kB
2026-01-19T16:16:15.6290427Z                    
2026-01-19T16:16:15.6290816Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson-parent/2.10.1/gson-parent-2.10.1.pom (13 kB at 432 kB/s)
2026-01-19T16:16:15.6339022Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.13.0/commons-lang3-3.13.0.pom
2026-01-19T16:16:15.6558467Z Progress (1): 728 B
2026-01-19T16:16:15.6560404Z Progress (1): 2.0 kB
2026-01-19T16:16:15.6562100Z Progress (1): 4.7 kB
2026-01-19T16:16:15.6564131Z Progress (1): 8.3 kB
2026-01-19T16:16:15.6566100Z Progress (1): 12 kB 
2026-01-19T16:16:15.6567797Z Progress (1): 15 kB
2026-01-19T16:16:15.6571083Z Progress (1): 16 kB
2026-01-19T16:16:15.6571406Z Progress (1): 18 kB
2026-01-19T16:16:15.6571709Z Progress (1): 21 kB
2026-01-19T16:16:15.6572009Z Progress (1): 24 kB
2026-01-19T16:16:15.6572298Z Progress (1): 27 kB
2026-01-19T16:16:15.6572594Z Progress (1): 30 kB
2026-01-19T16:16:15.6574567Z Progress (1): 31 kB
2026-01-19T16:16:15.6577115Z                    
2026-01-19T16:16:15.6578766Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.13.0/commons-lang3-3.13.0.pom (31 kB at 1.3 MB/s)
2026-01-19T16:16:15.6605951Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/58/commons-parent-58.pom
2026-01-19T16:16:15.6860650Z Progress (1): 704 B
2026-01-19T16:16:15.6863962Z Progress (1): 1.9 kB
2026-01-19T16:16:15.6865587Z Progress (1): 3.1 kB
2026-01-19T16:16:15.6867492Z Progress (1): 4.5 kB
2026-01-19T16:16:15.6868141Z Progress (1): 6.5 kB
2026-01-19T16:16:15.6872036Z Progress (1): 8.3 kB
2026-01-19T16:16:15.6872898Z Progress (1): 10 kB 
2026-01-19T16:16:15.6875081Z Progress (1): 12 kB
2026-01-19T16:16:15.6875692Z Progress (1): 15 kB
2026-01-19T16:16:15.6877055Z Progress (1): 18 kB
2026-01-19T16:16:15.6877583Z Progress (1): 20 kB
2026-01-19T16:16:15.6878090Z Progress (1): 23 kB
2026-01-19T16:16:15.6878687Z Progress (1): 26 kB
2026-01-19T16:16:15.6879451Z Progress (1): 29 kB
2026-01-19T16:16:15.6879886Z Progress (1): 33 kB
2026-01-19T16:16:15.6880400Z Progress (1): 33 kB
2026-01-19T16:16:15.6881352Z Progress (1): 36 kB
2026-01-19T16:16:15.6881828Z Progress (1): 41 kB
2026-01-19T16:16:15.6888576Z Progress (1): 44 kB
2026-01-19T16:16:15.6888901Z Progress (1): 47 kB
2026-01-19T16:16:15.6889191Z Progress (1): 49 kB
2026-01-19T16:16:15.6889480Z Progress (1): 51 kB
2026-01-19T16:16:15.6889781Z Progress (1): 55 kB
2026-01-19T16:16:15.6890085Z Progress (1): 58 kB
2026-01-19T16:16:15.6890366Z Progress (1): 61 kB
2026-01-19T16:16:15.6890682Z Progress (1): 64 kB
2026-01-19T16:16:15.6890960Z Progress (1): 67 kB
2026-01-19T16:16:15.6891410Z Progress (1): 72 kB
2026-01-19T16:16:15.6891694Z Progress (1): 76 kB
2026-01-19T16:16:15.6891974Z Progress (1): 80 kB
2026-01-19T16:16:15.6895451Z Progress (1): 83 kB
2026-01-19T16:16:15.6896030Z                    
2026-01-19T16:16:15.6897180Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/58/commons-parent-58.pom (83 kB at 2.8 MB/s)
2026-01-19T16:16:15.6973129Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.3/junit-bom-5.9.3.pom
2026-01-19T16:16:15.7209989Z Progress (1): 920 B
2026-01-19T16:16:15.7211690Z Progress (1): 3.4 kB
2026-01-19T16:16:15.7216295Z Progress (1): 5.6 kB
2026-01-19T16:16:15.7217226Z                     
2026-01-19T16:16:15.7218712Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.3/junit-bom-5.9.3.pom (5.6 kB at 225 kB/s)
2026-01-19T16:16:15.7241807Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.14.0/commons-io-2.14.0.pom
2026-01-19T16:16:15.7507404Z Progress (1): 764 B
2026-01-19T16:16:15.7507819Z Progress (1): 2.1 kB
2026-01-19T16:16:15.7510882Z Progress (1): 5.2 kB
2026-01-19T16:16:15.7511198Z Progress (1): 7.6 kB
2026-01-19T16:16:15.7511479Z Progress (1): 10 kB 
2026-01-19T16:16:15.7511776Z Progress (1): 12 kB
2026-01-19T16:16:15.7512088Z Progress (1): 15 kB
2026-01-19T16:16:15.7512384Z Progress (1): 18 kB
2026-01-19T16:16:15.7512680Z Progress (1): 20 kB
2026-01-19T16:16:15.7512965Z                    
2026-01-19T16:16:15.7513372Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.14.0/commons-io-2.14.0.pom (20 kB at 813 kB/s)
2026-01-19T16:16:15.7517243Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/62/commons-parent-62.pom
2026-01-19T16:16:15.7786074Z Progress (1): 704 B
2026-01-19T16:16:15.7795575Z Progress (1): 1.9 kB
2026-01-19T16:16:15.7795958Z Progress (1): 3.1 kB
2026-01-19T16:16:15.7799678Z Progress (1): 4.6 kB
2026-01-19T16:16:15.7800075Z Progress (1): 6.5 kB
2026-01-19T16:16:15.7800420Z Progress (1): 8.4 kB
2026-01-19T16:16:15.7800735Z Progress (1): 10 kB 
2026-01-19T16:16:15.7805087Z Progress (1): 13 kB
2026-01-19T16:16:15.7805427Z Progress (1): 15 kB
2026-01-19T16:16:15.7806175Z Progress (1): 18 kB
2026-01-19T16:16:15.7806714Z Progress (1): 20 kB
2026-01-19T16:16:15.7807039Z Progress (1): 23 kB
2026-01-19T16:16:15.7807366Z Progress (1): 25 kB
2026-01-19T16:16:15.7807684Z Progress (1): 28 kB
2026-01-19T16:16:15.7808000Z Progress (1): 32 kB
2026-01-19T16:16:15.7827081Z Progress (1): 32 kB
2026-01-19T16:16:15.7827817Z Progress (1): 35 kB
2026-01-19T16:16:15.7828321Z Progress (1): 41 kB
2026-01-19T16:16:15.7828784Z Progress (1): 44 kB
2026-01-19T16:16:15.7829233Z Progress (1): 46 kB
2026-01-19T16:16:15.7829673Z Progress (1): 49 kB
2026-01-19T16:16:15.7830127Z Progress (1): 51 kB
2026-01-19T16:16:15.7830576Z Progress (1): 54 kB
2026-01-19T16:16:15.7831016Z Progress (1): 58 kB
2026-01-19T16:16:15.7831453Z Progress (1): 60 kB
2026-01-19T16:16:15.7831920Z Progress (1): 64 kB
2026-01-19T16:16:15.7832373Z Progress (1): 67 kB
2026-01-19T16:16:15.7832833Z Progress (1): 71 kB
2026-01-19T16:16:15.7857232Z Progress (1): 74 kB
2026-01-19T16:16:15.7857808Z Progress (1): 77 kB
2026-01-19T16:16:15.7858299Z Progress (1): 80 kB
2026-01-19T16:16:15.7858987Z Progress (1): 81 kB
2026-01-19T16:16:15.7859457Z                    
2026-01-19T16:16:15.7860031Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/62/commons-parent-62.pom (81 kB at 2.7 MB/s)
2026-01-19T16:16:15.7860754Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/30/apache-30.pom
2026-01-19T16:16:15.8127242Z Progress (1): 741 B
2026-01-19T16:16:15.8127939Z Progress (1): 2.1 kB
2026-01-19T16:16:15.8128381Z Progress (1): 4.0 kB
2026-01-19T16:16:15.8128804Z Progress (1): 6.2 kB
2026-01-19T16:16:15.8129219Z Progress (1): 11 kB 
2026-01-19T16:16:15.8129632Z Progress (1): 16 kB
2026-01-19T16:16:15.8130024Z Progress (1): 20 kB
2026-01-19T16:16:15.8130669Z Progress (1): 22 kB
2026-01-19T16:16:15.8131103Z Progress (1): 23 kB
2026-01-19T16:16:15.8131505Z                    
2026-01-19T16:16:15.8131991Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/30/apache-30.pom (23 kB at 968 kB/s)
2026-01-19T16:16:15.8150366Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.0/junit-bom-5.10.0.pom
2026-01-19T16:16:15.8387372Z Progress (1): 912 B
2026-01-19T16:16:15.8396305Z Progress (1): 4.1 kB
2026-01-19T16:16:15.8396896Z Progress (1): 5.6 kB
2026-01-19T16:16:15.8397191Z                     
2026-01-19T16:16:15.8397542Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.0/junit-bom-5.10.0.pom (5.6 kB at 226 kB/s)
2026-01-19T16:16:15.8418230Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.9/slf4j-api-2.0.9.pom
2026-01-19T16:16:15.8615830Z Progress (1): 1.1 kB
2026-01-19T16:16:15.8621353Z Progress (1): 2.8 kB
2026-01-19T16:16:15.8622703Z                     
2026-01-19T16:16:15.8623177Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.9/slf4j-api-2.0.9.pom (2.8 kB at 128 kB/s)
2026-01-19T16:16:15.8642945Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.9/slf4j-parent-2.0.9.pom
2026-01-19T16:16:15.8863927Z Progress (1): 945 B
2026-01-19T16:16:15.8869037Z Progress (1): 3.2 kB
2026-01-19T16:16:15.8869593Z Progress (1): 6.0 kB
2026-01-19T16:16:15.8870076Z Progress (1): 8.1 kB
2026-01-19T16:16:15.8870575Z Progress (1): 12 kB 
2026-01-19T16:16:15.8871061Z Progress (1): 14 kB
2026-01-19T16:16:15.8872879Z Progress (1): 16 kB
2026-01-19T16:16:15.8873407Z                    
2026-01-19T16:16:15.8873925Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.9/slf4j-parent-2.0.9.pom (16 kB at 705 kB/s)
2026-01-19T16:16:15.8891266Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.9/slf4j-bom-2.0.9.pom
2026-01-19T16:16:15.9127737Z Progress (1): 1.0 kB
2026-01-19T16:16:15.9128149Z Progress (1): 4.8 kB
2026-01-19T16:16:15.9131621Z Progress (1): 4.9 kB
2026-01-19T16:16:15.9132144Z                     
2026-01-19T16:16:15.9132631Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.9/slf4j-bom-2.0.9.pom (4.9 kB at 197 kB/s)
2026-01-19T16:16:15.9155631Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-java/4.16.1/selenium-java-4.16.1.pom
2026-01-19T16:16:15.9388919Z Progress (1): 1.1 kB
2026-01-19T16:16:15.9417150Z Progress (1): 4.4 kB
2026-01-19T16:16:15.9426763Z                     
2026-01-19T16:16:15.9429748Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-java/4.16.1/selenium-java-4.16.1.pom (4.4 kB at 184 kB/s)
2026-01-19T16:16:15.9432483Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.16.1/selenium-api-4.16.1.pom
2026-01-19T16:16:15.9682736Z Progress (1): 1.1 kB
2026-01-19T16:16:15.9686336Z Progress (1): 2.1 kB
2026-01-19T16:16:15.9687447Z                     
2026-01-19T16:16:15.9688039Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.16.1/selenium-api-4.16.1.pom (2.1 kB at 77 kB/s)
2026-01-19T16:16:15.9737985Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chrome-driver/4.16.1/selenium-chrome-driver-4.16.1.pom
2026-01-19T16:16:15.9979753Z Progress (1): 1.1 kB
2026-01-19T16:16:15.9986388Z Progress (1): 3.3 kB
2026-01-19T16:16:15.9990498Z                     
2026-01-19T16:16:15.9992857Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chrome-driver/4.16.1/selenium-chrome-driver-4.16.1.pom (3.3 kB at 116 kB/s)
2026-01-19T16:16:16.0025362Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chromium-driver/4.16.1/selenium-chromium-driver-4.16.1.pom
2026-01-19T16:16:16.0248897Z Progress (1): 1.1 kB
2026-01-19T16:16:16.0265178Z Progress (1): 2.7 kB
2026-01-19T16:16:16.0265805Z                     
2026-01-19T16:16:16.0266687Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chromium-driver/4.16.1/selenium-chromium-driver-4.16.1.pom (2.7 kB at 117 kB/s)
2026-01-19T16:16:16.0301418Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.16.1/selenium-json-4.16.1.pom
2026-01-19T16:16:16.0519349Z Progress (1): 1.1 kB
2026-01-19T16:16:16.0523207Z Progress (1): 2.3 kB
2026-01-19T16:16:16.0527002Z                     
2026-01-19T16:16:16.0527488Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.16.1/selenium-json-4.16.1.pom (2.3 kB at 91 kB/s)
2026-01-19T16:16:16.0558639Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.16.1/selenium-remote-driver-4.16.1.pom
2026-01-19T16:16:16.0796764Z Progress (1): 1.1 kB
2026-01-19T16:16:16.0801405Z Progress (1): 5.3 kB
2026-01-19T16:16:16.0803435Z                     
2026-01-19T16:16:16.0805490Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.16.1/selenium-remote-driver-4.16.1.pom (5.3 kB at 205 kB/s)
2026-01-19T16:16:16.0842216Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.16.1/selenium-http-4.16.1.pom
2026-01-19T16:16:16.1073462Z Progress (1): 1.1 kB
2026-01-19T16:16:16.1073821Z Progress (1): 3.0 kB
2026-01-19T16:16:16.1074120Z                     
2026-01-19T16:16:16.1074561Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.16.1/selenium-http-4.16.1.pom (3.0 kB at 125 kB/s)
2026-01-19T16:16:16.1102588Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.16.1/selenium-manager-4.16.1.pom
2026-01-19T16:16:16.1347260Z Progress (1): 1.1 kB
2026-01-19T16:16:16.1352197Z Progress (1): 2.6 kB
2026-01-19T16:16:16.1355801Z                     
2026-01-19T16:16:16.1358185Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.16.1/selenium-manager-4.16.1.pom (2.6 kB at 102 kB/s)
2026-01-19T16:16:16.1369062Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.16.1/selenium-os-4.16.1.pom
2026-01-19T16:16:16.1620664Z Progress (1): 1.1 kB
2026-01-19T16:16:16.1628384Z Progress (1): 2.4 kB
2026-01-19T16:16:16.1628768Z                     
2026-01-19T16:16:16.1629289Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.16.1/selenium-os-4.16.1.pom (2.4 kB at 94 kB/s)
2026-01-19T16:16:16.1642672Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v118/4.16.1/selenium-devtools-v118-4.16.1.pom
2026-01-19T16:16:16.1893215Z Progress (1): 1.1 kB
2026-01-19T16:16:16.1935382Z Progress (1): 2.9 kB
2026-01-19T16:16:16.1937728Z                     
2026-01-19T16:16:16.1938206Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v118/4.16.1/selenium-devtools-v118-4.16.1.pom (2.9 kB at 110 kB/s)
2026-01-19T16:16:16.1939000Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v119/4.16.1/selenium-devtools-v119-4.16.1.pom
2026-01-19T16:16:16.2174808Z Progress (1): 1.1 kB
2026-01-19T16:16:16.2179100Z Progress (1): 2.9 kB
2026-01-19T16:16:16.2179778Z                     
2026-01-19T16:16:16.2181364Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v119/4.16.1/selenium-devtools-v119-4.16.1.pom (2.9 kB at 110 kB/s)
2026-01-19T16:16:16.2200705Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v120/4.16.1/selenium-devtools-v120-4.16.1.pom
2026-01-19T16:16:16.2498830Z Progress (1): 1.1 kB
2026-01-19T16:16:16.2504741Z Progress (1): 2.9 kB
2026-01-19T16:16:16.2508975Z                     
2026-01-19T16:16:16.2509996Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v120/4.16.1/selenium-devtools-v120-4.16.1.pom (2.9 kB at 92 kB/s)
2026-01-19T16:16:16.2520438Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v85/4.16.1/selenium-devtools-v85-4.16.1.pom
2026-01-19T16:16:16.2841244Z Progress (1): 1.1 kB
2026-01-19T16:16:16.2850006Z Progress (1): 2.9 kB
2026-01-19T16:16:16.2851317Z                     
2026-01-19T16:16:16.2852142Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v85/4.16.1/selenium-devtools-v85-4.16.1.pom (2.9 kB at 87 kB/s)
2026-01-19T16:16:16.2888858Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-edge-driver/4.16.1/selenium-edge-driver-4.16.1.pom
2026-01-19T16:16:16.3142248Z Progress (1): 1.1 kB
2026-01-19T16:16:16.3146439Z Progress (1): 3.1 kB
2026-01-19T16:16:16.3147889Z                     
2026-01-19T16:16:16.3148437Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-edge-driver/4.16.1/selenium-edge-driver-4.16.1.pom (3.1 kB at 118 kB/s)
2026-01-19T16:16:16.3172284Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-firefox-driver/4.16.1/selenium-firefox-driver-4.16.1.pom
2026-01-19T16:16:16.3427957Z Progress (1): 1.1 kB
2026-01-19T16:16:16.3434371Z Progress (1): 3.4 kB
2026-01-19T16:16:16.3438097Z                     
2026-01-19T16:16:16.3438907Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-firefox-driver/4.16.1/selenium-firefox-driver-4.16.1.pom (3.4 kB at 127 kB/s)
2026-01-19T16:16:16.3458485Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-ie-driver/4.16.1/selenium-ie-driver-4.16.1.pom
2026-01-19T16:16:16.3724016Z Progress (1): 1.1 kB
2026-01-19T16:16:16.3729546Z Progress (1): 2.9 kB
2026-01-19T16:16:16.3732743Z                     
2026-01-19T16:16:16.3733618Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-ie-driver/4.16.1/selenium-ie-driver-4.16.1.pom (2.9 kB at 106 kB/s)
2026-01-19T16:16:16.3750863Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-safari-driver/4.16.1/selenium-safari-driver-4.16.1.pom
2026-01-19T16:16:16.3996973Z Progress (1): 1.1 kB
2026-01-19T16:16:16.4005188Z Progress (1): 2.7 kB
2026-01-19T16:16:16.4005531Z                     
2026-01-19T16:16:16.4005966Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-safari-driver/4.16.1/selenium-safari-driver-4.16.1.pom (2.7 kB at 107 kB/s)
2026-01-19T16:16:16.4023486Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.16.1/selenium-support-4.16.1.pom
2026-01-19T16:16:16.4247932Z Progress (1): 1.1 kB
2026-01-19T16:16:16.4267286Z Progress (1): 3.2 kB
2026-01-19T16:16:16.4275400Z                     
2026-01-19T16:16:16.4276115Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.16.1/selenium-support-4.16.1.pom (3.2 kB at 139 kB/s)
2026-01-19T16:16:16.4282129Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-core/7.27.2/cucumber-core-7.27.2.pom
2026-01-19T16:16:16.4563911Z Progress (1): 1.3 kB
2026-01-19T16:16:16.4567166Z Progress (1): 6.2 kB
2026-01-19T16:16:16.4572109Z Progress (1): 12 kB 
2026-01-19T16:16:16.4595666Z Progress (1): 13 kB
2026-01-19T16:16:16.4597477Z                    
2026-01-19T16:16:16.4598109Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-core/7.27.2/cucumber-core-7.27.2.pom (13 kB at 429 kB/s)
2026-01-19T16:16:16.4602015Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-jvm/7.27.2/cucumber-jvm-7.27.2.pom
2026-01-19T16:16:16.4873086Z Progress (1): 1.2 kB
2026-01-19T16:16:16.4874607Z Progress (1): 3.7 kB
2026-01-19T16:16:16.4876364Z Progress (1): 8.9 kB
2026-01-19T16:16:16.4877309Z Progress (1): 13 kB 
2026-01-19T16:16:16.4877802Z Progress (1): 18 kB
2026-01-19T16:16:16.4878120Z Progress (1): 20 kB
2026-01-19T16:16:16.4878395Z                    
2026-01-19T16:16:16.4878802Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-jvm/7.27.2/cucumber-jvm-7.27.2.pom (20 kB at 703 kB/s)
2026-01-19T16:16:16.4902276Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.3.7/cucumber-parent-4.3.7.pom
2026-01-19T16:16:16.5153942Z Progress (1): 1.2 kB
2026-01-19T16:16:16.5159167Z Progress (1): 3.8 kB
2026-01-19T16:16:16.5159631Z Progress (1): 8.6 kB
2026-01-19T16:16:16.5160054Z Progress (1): 14 kB 
2026-01-19T16:16:16.5163161Z Progress (1): 20 kB
2026-01-19T16:16:16.5164998Z                    
2026-01-19T16:16:16.5166003Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.3.7/cucumber-parent-4.3.7.pom (20 kB at 727 kB/s)
2026-01-19T16:16:16.5205581Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-bom/7.27.2/cucumber-bom-7.27.2.pom
2026-01-19T16:16:16.5488445Z Progress (1): 1.3 kB
2026-01-19T16:16:16.5524881Z Progress (1): 7.4 kB
2026-01-19T16:16:16.5525205Z                     
2026-01-19T16:16:16.5525758Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-bom/7.27.2/cucumber-bom-7.27.2.pom (7.4 kB at 237 kB/s)
2026-01-19T16:16:16.5526721Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.4/junit-bom-5.13.4.pom
2026-01-19T16:16:16.5757755Z Progress (1): 908 B
2026-01-19T16:16:16.5759243Z Progress (1): 4.1 kB
2026-01-19T16:16:16.5763545Z Progress (1): 5.7 kB
2026-01-19T16:16:16.5764322Z                     
2026-01-19T16:16:16.5765169Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.4/junit-bom-5.13.4.pom (5.7 kB at 227 kB/s)
2026-01-19T16:16:16.5817767Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.2/jackson-bom-2.19.2.pom
2026-01-19T16:16:16.6023319Z Progress (1): 926 B
2026-01-19T16:16:16.6025843Z Progress (1): 2.6 kB
2026-01-19T16:16:16.6027865Z Progress (1): 7.3 kB
2026-01-19T16:16:16.6028640Z Progress (1): 16 kB 
2026-01-19T16:16:16.6029183Z Progress (1): 20 kB
2026-01-19T16:16:16.6032783Z Progress (1): 20 kB
2026-01-19T16:16:16.6033119Z                    
2026-01-19T16:16:16.6033516Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.2/jackson-bom-2.19.2.pom (20 kB at 779 kB/s)
2026-01-19T16:16:16.6053938Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19.3/jackson-parent-2.19.3.pom
2026-01-19T16:16:16.6315912Z Progress (1): 1.1 kB
2026-01-19T16:16:16.6316370Z Progress (1): 2.5 kB
2026-01-19T16:16:16.6316954Z Progress (1): 4.2 kB
2026-01-19T16:16:16.6317317Z Progress (1): 6.1 kB
2026-01-19T16:16:16.6317697Z Progress (1): 7.2 kB
2026-01-19T16:16:16.6318038Z                     
2026-01-19T16:16:16.6318755Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19.3/jackson-parent-2.19.3.pom (7.2 kB at 266 kB/s)
2026-01-19T16:16:16.6332710Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/69/oss-parent-69.pom
2026-01-19T16:16:16.6586355Z Progress (1): 949 B
2026-01-19T16:16:16.6589182Z Progress (1): 2.9 kB
2026-01-19T16:16:16.6589604Z Progress (1): 4.1 kB
2026-01-19T16:16:16.6619605Z Progress (1): 6.1 kB
2026-01-19T16:16:16.6620644Z Progress (1): 9.9 kB
2026-01-19T16:16:16.6621145Z Progress (1): 12 kB 
2026-01-19T16:16:16.6621441Z Progress (1): 15 kB
2026-01-19T16:16:16.6621898Z Progress (1): 18 kB
2026-01-19T16:16:16.6622209Z Progress (1): 21 kB
2026-01-19T16:16:16.6622532Z Progress (1): 24 kB
2026-01-19T16:16:16.6622842Z                    
2026-01-19T16:16:16.6623265Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/69/oss-parent-69.pom (24 kB at 844 kB/s)
2026-01-19T16:16:16.6638845Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin/7.27.2/cucumber-gherkin-7.27.2.pom
2026-01-19T16:16:16.7441025Z Progress (1): 1.8 kB
2026-01-19T16:16:16.7442409Z                     
2026-01-19T16:16:16.7442836Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin/7.27.2/cucumber-gherkin-7.27.2.pom (1.8 kB at 22 kB/s)
2026-01-19T16:16:16.7466102Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-plugin/7.27.2/cucumber-plugin-7.27.2.pom
2026-01-19T16:16:16.7756960Z Progress (1): 1.8 kB
2026-01-19T16:16:16.7758666Z Progress (1): 1.9 kB
2026-01-19T16:16:16.7759024Z                     
2026-01-19T16:16:16.7759438Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-plugin/7.27.2/cucumber-plugin-7.27.2.pom (1.9 kB at 68 kB/s)
2026-01-19T16:16:16.7783701Z Downloading from central: https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.pom
2026-01-19T16:16:16.7996394Z Progress (1): 1.0 kB
2026-01-19T16:16:16.7997950Z Progress (1): 1.5 kB
2026-01-19T16:16:16.7998248Z                     
2026-01-19T16:16:16.7998653Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.pom (1.5 kB at 69 kB/s)
2026-01-19T16:16:16.8034491Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin-messages/7.27.2/cucumber-gherkin-messages-7.27.2.pom
2026-01-19T16:16:16.8310411Z Progress (1): 1.9 kB
2026-01-19T16:16:16.8329343Z Progress (1): 1.9 kB
2026-01-19T16:16:16.8329947Z                     
2026-01-19T16:16:16.8330573Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin-messages/7.27.2/cucumber-gherkin-messages-7.27.2.pom (1.9 kB at 66 kB/s)
2026-01-19T16:16:16.8362073Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/gherkin/34.0.0/gherkin-34.0.0.pom
2026-01-19T16:16:16.8728456Z Progress (1): 1.2 kB
2026-01-19T16:16:16.8735375Z Progress (1): 4.8 kB
2026-01-19T16:16:16.8735926Z Progress (1): 8.2 kB
2026-01-19T16:16:16.8736381Z                     
2026-01-19T16:16:16.8737234Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/gherkin/34.0.0/gherkin-34.0.0.pom (8.2 kB at 216 kB/s)
2026-01-19T16:16:16.8780780Z Downloading from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-bom/3.27.4/assertj-bom-3.27.4.pom
2026-01-19T16:16:16.9127310Z Progress (1): 1.0 kB
2026-01-19T16:16:16.9127721Z Progress (1): 3.3 kB
2026-01-19T16:16:16.9128015Z                     
2026-01-19T16:16:16.9128436Z Downloaded from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-bom/3.27.4/assertj-bom-3.27.4.pom (3.3 kB at 95 kB/s)
2026-01-19T16:16:16.9164393Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/maven-metadata.xml
2026-01-19T16:16:16.9413147Z Progress (1): 3.1 kB
2026-01-19T16:16:16.9413673Z                     
2026-01-19T16:16:16.9414074Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/maven-metadata.xml (3.1 kB at 120 kB/s)
2026-01-19T16:16:16.9433839Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.4/messages-19.1.4.pom
2026-01-19T16:16:16.9678358Z Progress (1): 1.3 kB
2026-01-19T16:16:16.9682869Z Progress (1): 4.1 kB
2026-01-19T16:16:16.9697516Z                     
2026-01-19T16:16:16.9698141Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.4/messages-19.1.4.pom (4.1 kB at 156 kB/s)
2026-01-19T16:16:16.9704260Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/3.0.0/cucumber-parent-3.0.0.pom
2026-01-19T16:16:16.9937680Z Progress (1): 1.2 kB
2026-01-19T16:16:16.9943527Z Progress (1): 3.7 kB
2026-01-19T16:16:16.9944142Z Progress (1): 8.6 kB
2026-01-19T16:16:16.9944669Z Progress (1): 13 kB 
2026-01-19T16:16:16.9945200Z Progress (1): 19 kB
2026-01-19T16:16:16.9945752Z Progress (1): 22 kB
2026-01-19T16:16:16.9946243Z                    
2026-01-19T16:16:16.9947098Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/3.0.0/cucumber-parent-3.0.0.pom (22 kB at 871 kB/s)
2026-01-19T16:16:16.9967173Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.1/junit-bom-5.9.1.pom
2026-01-19T16:16:17.0211513Z Progress (1): 907 B
2026-01-19T16:16:17.0211920Z Progress (1): 4.1 kB
2026-01-19T16:16:17.0217183Z Progress (1): 5.6 kB
2026-01-19T16:16:17.0241711Z                     
2026-01-19T16:16:17.0257282Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.1/junit-bom-5.9.1.pom (5.6 kB at 225 kB/s)
2026-01-19T16:16:17.0257878Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.4/jackson-bom-2.13.4.pom
2026-01-19T16:16:17.0488100Z Progress (1): 931 B
2026-01-19T16:16:17.0491393Z Progress (1): 2.7 kB
2026-01-19T16:16:17.0491950Z Progress (1): 8.7 kB
2026-01-19T16:16:17.0492284Z Progress (1): 17 kB 
2026-01-19T16:16:17.0492591Z Progress (1): 17 kB
2026-01-19T16:16:17.0492887Z                    
2026-01-19T16:16:17.0493305Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.4/jackson-bom-2.13.4.pom (17 kB at 723 kB/s)
2026-01-19T16:16:17.0517641Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.13/jackson-parent-2.13.pom
2026-01-19T16:16:17.0781534Z Progress (1): 1.1 kB
2026-01-19T16:16:17.0782449Z Progress (1): 2.6 kB
2026-01-19T16:16:17.0784603Z Progress (1): 4.1 kB
2026-01-19T16:16:17.0792716Z Progress (1): 6.5 kB
2026-01-19T16:16:17.0802098Z Progress (1): 7.4 kB
2026-01-19T16:16:17.0803085Z                     
2026-01-19T16:16:17.0804567Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.13/jackson-parent-2.13.pom (7.4 kB at 256 kB/s)
2026-01-19T16:16:17.0831759Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/43/oss-parent-43.pom
2026-01-19T16:16:17.1121954Z Progress (1): 949 B
2026-01-19T16:16:17.1122329Z Progress (1): 2.6 kB
2026-01-19T16:16:17.1122641Z Progress (1): 4.0 kB
2026-01-19T16:16:17.1122946Z Progress (1): 6.0 kB
2026-01-19T16:16:17.1128799Z Progress (1): 9.5 kB
2026-01-19T16:16:17.1129102Z Progress (1): 12 kB 
2026-01-19T16:16:17.1129392Z Progress (1): 15 kB
2026-01-19T16:16:17.1129686Z Progress (1): 18 kB
2026-01-19T16:16:17.1129988Z Progress (1): 21 kB
2026-01-19T16:16:17.1139129Z Progress (1): 24 kB
2026-01-19T16:16:17.1144689Z                    
2026-01-19T16:16:17.1146727Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/43/oss-parent-43.pom (24 kB at 761 kB/s)
2026-01-19T16:16:17.1191354Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/20.0.0/messages-20.0.0.pom
2026-01-19T16:16:17.1439653Z Progress (1): 1.3 kB
2026-01-19T16:16:17.1450160Z Progress (1): 4.2 kB
2026-01-19T16:16:17.1451015Z                     
2026-01-19T16:16:17.1451876Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/20.0.0/messages-20.0.0.pom (4.2 kB at 162 kB/s)
2026-01-19T16:16:17.1475699Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.1.1/cucumber-parent-4.1.1.pom
2026-01-19T16:16:17.1738308Z Progress (1): 1.2 kB
2026-01-19T16:16:17.1739814Z Progress (1): 3.9 kB
2026-01-19T16:16:17.1740438Z Progress (1): 7.0 kB
2026-01-19T16:16:17.1741034Z Progress (1): 12 kB 
2026-01-19T16:16:17.1741713Z Progress (1): 17 kB
2026-01-19T16:16:17.1753071Z Progress (1): 21 kB
2026-01-19T16:16:17.1753906Z                    
2026-01-19T16:16:17.1754586Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.1.1/cucumber-parent-4.1.1.pom (21 kB at 751 kB/s)
2026-01-19T16:16:17.1786995Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.0/jackson-bom-2.14.0.pom
2026-01-19T16:16:17.2015663Z Progress (1): 924 B
2026-01-19T16:16:17.2022193Z Progress (1): 2.7 kB
2026-01-19T16:16:17.2024964Z Progress (1): 8.1 kB
2026-01-19T16:16:17.2032342Z Progress (1): 17 kB 
2026-01-19T16:16:17.2036168Z Progress (1): 17 kB
2026-01-19T16:16:17.2039516Z                    
2026-01-19T16:16:17.2039950Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.0/jackson-bom-2.14.0.pom (17 kB at 699 kB/s)
2026-01-19T16:16:17.2087130Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.14/jackson-parent-2.14.pom
2026-01-19T16:16:17.2354541Z Progress (1): 1.1 kB
2026-01-19T16:16:17.2355895Z Progress (1): 2.5 kB
2026-01-19T16:16:17.2356470Z Progress (1): 4.0 kB
2026-01-19T16:16:17.2357367Z Progress (1): 6.5 kB
2026-01-19T16:16:17.2357661Z Progress (1): 7.7 kB
2026-01-19T16:16:17.2357930Z                     
2026-01-19T16:16:17.2358331Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.14/jackson-parent-2.14.pom (7.7 kB at 284 kB/s)
2026-01-19T16:16:17.2389183Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/48/oss-parent-48.pom
2026-01-19T16:16:17.2640292Z Progress (1): 948 B
2026-01-19T16:16:17.2640732Z Progress (1): 2.6 kB
2026-01-19T16:16:17.2641087Z Progress (1): 4.0 kB
2026-01-19T16:16:17.2641419Z Progress (1): 6.0 kB
2026-01-19T16:16:17.2641749Z Progress (1): 9.7 kB
2026-01-19T16:16:17.2642065Z Progress (1): 12 kB 
2026-01-19T16:16:17.2648522Z Progress (1): 15 kB
2026-01-19T16:16:17.2648847Z Progress (1): 18 kB
2026-01-19T16:16:17.2649158Z Progress (1): 21 kB
2026-01-19T16:16:17.2649473Z Progress (1): 24 kB
2026-01-19T16:16:17.2649756Z                    
2026-01-19T16:16:17.2650145Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/48/oss-parent-48.pom (24 kB at 914 kB/s)
2026-01-19T16:16:17.2674926Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/21.0.1/messages-21.0.1.pom
2026-01-19T16:16:17.2915672Z Progress (1): 1.2 kB
2026-01-19T16:16:17.2924047Z Progress (1): 4.4 kB
2026-01-19T16:16:17.2925711Z                     
2026-01-19T16:16:17.2926911Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/21.0.1/messages-21.0.1.pom (4.4 kB at 178 kB/s)
2026-01-19T16:16:17.2980912Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.1/jackson-bom-2.14.1.pom
2026-01-19T16:16:17.3198740Z Progress (1): 924 B
2026-01-19T16:16:17.3200966Z Progress (1): 2.7 kB
2026-01-19T16:16:17.3201437Z Progress (1): 8.1 kB
2026-01-19T16:16:17.3201796Z Progress (1): 17 kB 
2026-01-19T16:16:17.3204375Z Progress (1): 17 kB
2026-01-19T16:16:17.3209434Z                    
2026-01-19T16:16:17.3211080Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.1/jackson-bom-2.14.1.pom (17 kB at 760 kB/s)
2026-01-19T16:16:17.3236670Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/22.0.0/messages-22.0.0.pom
2026-01-19T16:16:17.3451519Z Progress (1): 1.2 kB
2026-01-19T16:16:17.3455949Z Progress (1): 4.4 kB
2026-01-19T16:16:17.3458079Z                     
2026-01-19T16:16:17.3459582Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/22.0.0/messages-22.0.0.pom (4.4 kB at 202 kB/s)
2026-01-19T16:16:17.3477903Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.2/junit-bom-5.9.2.pom
2026-01-19T16:16:17.3690480Z Progress (1): 907 B
2026-01-19T16:16:17.3691005Z Progress (1): 4.1 kB
2026-01-19T16:16:17.3701284Z Progress (1): 5.6 kB
2026-01-19T16:16:17.3701664Z                     
2026-01-19T16:16:17.3702194Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.2/junit-bom-5.9.2.pom (5.6 kB at 256 kB/s)
2026-01-19T16:16:17.3721143Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.2/jackson-bom-2.14.2.pom
2026-01-19T16:16:17.3985926Z Progress (1): 924 B
2026-01-19T16:16:17.3987960Z Progress (1): 2.7 kB
2026-01-19T16:16:17.3989489Z Progress (1): 8.1 kB
2026-01-19T16:16:17.3989859Z Progress (1): 17 kB 
2026-01-19T16:16:17.3993392Z Progress (1): 17 kB
2026-01-19T16:16:17.4003458Z                    
2026-01-19T16:16:17.4004307Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.14.2/jackson-bom-2.14.2.pom (17 kB at 625 kB/s)
2026-01-19T16:16:17.4039233Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/23.0.0/messages-23.0.0.pom
2026-01-19T16:16:17.4285090Z Progress (1): 1.2 kB
2026-01-19T16:16:17.4288039Z Progress (1): 4.4 kB
2026-01-19T16:16:17.4288738Z Progress (1): 4.4 kB
2026-01-19T16:16:17.4289340Z                     
2026-01-19T16:16:17.4289887Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/23.0.0/messages-23.0.0.pom (4.4 kB at 178 kB/s)
2026-01-19T16:16:17.4319650Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.15.3/jackson-bom-2.15.3.pom
2026-01-19T16:16:17.4582905Z Progress (1): 924 B
2026-01-19T16:16:17.4588207Z Progress (1): 2.7 kB
2026-01-19T16:16:17.4598350Z Progress (1): 8.1 kB
2026-01-19T16:16:17.4599147Z Progress (1): 17 kB 
2026-01-19T16:16:17.4600882Z Progress (1): 18 kB
2026-01-19T16:16:17.4601316Z                    
2026-01-19T16:16:17.4601849Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.15.3/jackson-bom-2.15.3.pom (18 kB at 643 kB/s)
2026-01-19T16:16:17.4632845Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.15/jackson-parent-2.15.pom
2026-01-19T16:16:17.4898984Z Progress (1): 1.1 kB
2026-01-19T16:16:17.4899583Z Progress (1): 2.6 kB
2026-01-19T16:16:17.4900951Z Progress (1): 4.1 kB
2026-01-19T16:16:17.4901253Z Progress (1): 6.5 kB
2026-01-19T16:16:17.4901552Z                     
2026-01-19T16:16:17.4901954Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.15/jackson-parent-2.15.pom (6.5 kB at 242 kB/s)
2026-01-19T16:16:17.4930432Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/50/oss-parent-50.pom
2026-01-19T16:16:17.5179689Z Progress (1): 948 B
2026-01-19T16:16:17.5183685Z Progress (1): 2.6 kB
2026-01-19T16:16:17.5188805Z Progress (1): 4.0 kB
2026-01-19T16:16:17.5189576Z Progress (1): 6.0 kB
2026-01-19T16:16:17.5190125Z Progress (1): 9.6 kB
2026-01-19T16:16:17.5193040Z Progress (1): 12 kB 
2026-01-19T16:16:17.5194924Z Progress (1): 15 kB
2026-01-19T16:16:17.5195473Z Progress (1): 18 kB
2026-01-19T16:16:17.5195962Z Progress (1): 21 kB
2026-01-19T16:16:17.5204327Z Progress (1): 24 kB
2026-01-19T16:16:17.5209237Z                    
2026-01-19T16:16:17.5209684Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/50/oss-parent-50.pom (24 kB at 843 kB/s)
2026-01-19T16:16:17.5260317Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.0.0/messages-24.0.0.pom
2026-01-19T16:16:17.5498711Z Progress (1): 1.2 kB
2026-01-19T16:16:17.5507752Z Progress (1): 4.4 kB
2026-01-19T16:16:17.5508416Z Progress (1): 4.4 kB
2026-01-19T16:16:17.5509017Z                     
2026-01-19T16:16:17.5509574Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.0.0/messages-24.0.0.pom (4.4 kB at 178 kB/s)
2026-01-19T16:16:17.5565578Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.1/junit-bom-5.10.1.pom
2026-01-19T16:16:17.5800898Z Progress (1): 908 B
2026-01-19T16:16:17.5805556Z Progress (1): 4.1 kB
2026-01-19T16:16:17.5813154Z Progress (1): 5.6 kB
2026-01-19T16:16:17.5813759Z                     
2026-01-19T16:16:17.5814324Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.1/junit-bom-5.10.1.pom (5.6 kB at 226 kB/s)
2026-01-19T16:16:17.5841610Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.16.0/jackson-bom-2.16.0.pom
2026-01-19T16:16:17.6065240Z Progress (1): 924 B
2026-01-19T16:16:17.6069421Z Progress (1): 2.7 kB
2026-01-19T16:16:17.6069956Z Progress (1): 8.1 kB
2026-01-19T16:16:17.6072200Z Progress (1): 17 kB 
2026-01-19T16:16:17.6082586Z Progress (1): 18 kB
2026-01-19T16:16:17.6083108Z                    
2026-01-19T16:16:17.6084269Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.16.0/jackson-bom-2.16.0.pom (18 kB at 729 kB/s)
2026-01-19T16:16:17.6111102Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.16/jackson-parent-2.16.pom
2026-01-19T16:16:17.6345244Z Progress (1): 1.1 kB
2026-01-19T16:16:17.6348826Z Progress (1): 2.5 kB
2026-01-19T16:16:17.6349837Z Progress (1): 4.0 kB
2026-01-19T16:16:17.6353681Z Progress (1): 6.5 kB
2026-01-19T16:16:17.6354083Z                     
2026-01-19T16:16:17.6356886Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.16/jackson-parent-2.16.pom (6.5 kB at 272 kB/s)
2026-01-19T16:16:17.6365165Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/56/oss-parent-56.pom
2026-01-19T16:16:17.6603991Z Progress (1): 947 B
2026-01-19T16:16:17.6607157Z Progress (1): 2.6 kB
2026-01-19T16:16:17.6609052Z Progress (1): 4.0 kB
2026-01-19T16:16:17.6610079Z Progress (1): 6.4 kB
2026-01-19T16:16:17.6611399Z Progress (1): 9.6 kB
2026-01-19T16:16:17.6611846Z Progress (1): 12 kB 
2026-01-19T16:16:17.6612363Z Progress (1): 15 kB
2026-01-19T16:16:17.6612861Z Progress (1): 18 kB
2026-01-19T16:16:17.6613346Z Progress (1): 21 kB
2026-01-19T16:16:17.6625260Z Progress (1): 24 kB
2026-01-19T16:16:17.6625639Z                    
2026-01-19T16:16:17.6626256Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/56/oss-parent-56.pom (24 kB at 942 kB/s)
2026-01-19T16:16:17.6645297Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.0.1/messages-24.0.1.pom
2026-01-19T16:16:17.6868952Z Progress (1): 1.3 kB
2026-01-19T16:16:17.6873517Z Progress (1): 4.4 kB
2026-01-19T16:16:17.6874304Z                     
2026-01-19T16:16:17.6876120Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.0.1/messages-24.0.1.pom (4.4 kB at 193 kB/s)
2026-01-19T16:16:17.6890617Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.1.0/messages-24.1.0.pom
2026-01-19T16:16:17.7119031Z Progress (1): 1.3 kB
2026-01-19T16:16:17.7119658Z Progress (1): 4.6 kB
2026-01-19T16:16:17.7123067Z Progress (1): 4.7 kB
2026-01-19T16:16:17.7125139Z                     
2026-01-19T16:16:17.7126044Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/24.1.0/messages-24.1.0.pom (4.7 kB at 197 kB/s)
2026-01-19T16:16:17.7135893Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.2.0/cucumber-parent-4.2.0.pom
2026-01-19T16:16:17.7373134Z Progress (1): 1.2 kB
2026-01-19T16:16:17.7373998Z Progress (1): 3.8 kB
2026-01-19T16:16:17.7376031Z Progress (1): 7.0 kB
2026-01-19T16:16:17.7376378Z Progress (1): 12 kB 
2026-01-19T16:16:17.7376966Z Progress (1): 17 kB
2026-01-19T16:16:17.7383433Z Progress (1): 21 kB
2026-01-19T16:16:17.7384231Z                    
2026-01-19T16:16:17.7388874Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/4.2.0/cucumber-parent-4.2.0.pom (21 kB at 840 kB/s)
2026-01-19T16:16:17.7425135Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom
2026-01-19T16:16:17.7633788Z Progress (1): 908 B
2026-01-19T16:16:17.7634636Z Progress (1): 4.1 kB
2026-01-19T16:16:17.7657869Z Progress (1): 5.6 kB
2026-01-19T16:16:17.7659170Z                     
2026-01-19T16:16:17.7659995Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.10.2/junit-bom-5.10.2.pom (5.6 kB at 257 kB/s)
2026-01-19T16:16:17.7671966Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.0/jackson-bom-2.17.0.pom
2026-01-19T16:16:17.7915183Z Progress (1): 924 B
2026-01-19T16:16:17.7917343Z Progress (1): 2.7 kB
2026-01-19T16:16:17.7919250Z Progress (1): 8.1 kB
2026-01-19T16:16:17.7919803Z Progress (1): 17 kB 
2026-01-19T16:16:17.7920193Z Progress (1): 19 kB
2026-01-19T16:16:17.7920609Z                    
2026-01-19T16:16:17.7937251Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.0/jackson-bom-2.17.0.pom (19 kB at 719 kB/s)
2026-01-19T16:16:17.7940446Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.17/jackson-parent-2.17.pom
2026-01-19T16:16:17.8164618Z Progress (1): 1.1 kB
2026-01-19T16:16:17.8167292Z Progress (1): 2.5 kB
2026-01-19T16:16:17.8172999Z Progress (1): 4.0 kB
2026-01-19T16:16:17.8175126Z Progress (1): 6.5 kB
2026-01-19T16:16:17.8175442Z                     
2026-01-19T16:16:17.8175863Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.17/jackson-parent-2.17.pom (6.5 kB at 284 kB/s)
2026-01-19T16:16:17.8184399Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/58/oss-parent-58.pom
2026-01-19T16:16:17.8538182Z Progress (1): 947 B
2026-01-19T16:16:17.8538988Z Progress (1): 2.6 kB
2026-01-19T16:16:17.8542830Z Progress (1): 4.0 kB
2026-01-19T16:16:17.8546934Z Progress (1): 6.0 kB
2026-01-19T16:16:17.8547332Z Progress (1): 9.6 kB
2026-01-19T16:16:17.8547660Z Progress (1): 12 kB 
2026-01-19T16:16:17.8547998Z Progress (1): 15 kB
2026-01-19T16:16:17.8548342Z Progress (1): 18 kB
2026-01-19T16:16:17.8548673Z Progress (1): 21 kB
2026-01-19T16:16:17.8549018Z Progress (1): 24 kB
2026-01-19T16:16:17.8549334Z                    
2026-01-19T16:16:17.8549766Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/58/oss-parent-58.pom (24 kB at 657 kB/s)
2026-01-19T16:16:17.8580159Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/25.0.0/messages-25.0.0.pom
2026-01-19T16:16:17.8849021Z Progress (1): 1.3 kB
2026-01-19T16:16:17.8850890Z Progress (1): 4.6 kB
2026-01-19T16:16:17.8882739Z Progress (1): 4.7 kB
2026-01-19T16:16:17.8901095Z                     
2026-01-19T16:16:17.8901775Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/25.0.0/messages-25.0.0.pom (4.7 kB at 169 kB/s)
2026-01-19T16:16:17.8902521Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.1/jackson-bom-2.17.1.pom
2026-01-19T16:16:17.9144688Z Progress (1): 924 B
2026-01-19T16:16:17.9149649Z Progress (1): 2.7 kB
2026-01-19T16:16:17.9150025Z Progress (1): 8.1 kB
2026-01-19T16:16:17.9151362Z Progress (1): 17 kB 
2026-01-19T16:16:17.9155874Z Progress (1): 19 kB
2026-01-19T16:16:17.9159183Z                    
2026-01-19T16:16:17.9161442Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.1/jackson-bom-2.17.1.pom (19 kB at 692 kB/s)
2026-01-19T16:16:17.9197238Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/25.0.1/messages-25.0.1.pom
2026-01-19T16:16:17.9448752Z Progress (1): 1.2 kB
2026-01-19T16:16:17.9449516Z Progress (1): 4.6 kB
2026-01-19T16:16:17.9450040Z Progress (1): 4.7 kB
2026-01-19T16:16:17.9450479Z                     
2026-01-19T16:16:17.9451009Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/25.0.1/messages-25.0.1.pom (4.7 kB at 182 kB/s)
2026-01-19T16:16:17.9527705Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/26.0.0/messages-26.0.0.pom
2026-01-19T16:16:17.9770083Z Progress (1): 1.3 kB
2026-01-19T16:16:17.9780103Z Progress (1): 4.6 kB
2026-01-19T16:16:17.9780434Z Progress (1): 4.7 kB
2026-01-19T16:16:17.9780715Z                     
2026-01-19T16:16:17.9781113Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/26.0.0/messages-26.0.0.pom (4.7 kB at 182 kB/s)
2026-01-19T16:16:17.9808389Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom
2026-01-19T16:16:18.0054023Z Progress (1): 908 B
2026-01-19T16:16:18.0054723Z Progress (1): 4.1 kB
2026-01-19T16:16:18.0062204Z Progress (1): 5.6 kB
2026-01-19T16:16:18.0066831Z                     
2026-01-19T16:16:18.0068722Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0/junit-bom-5.11.0.pom (5.6 kB at 209 kB/s)
2026-01-19T16:16:18.0112877Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.2/jackson-bom-2.17.2.pom
2026-01-19T16:16:18.0359179Z Progress (1): 924 B
2026-01-19T16:16:18.0360741Z Progress (1): 2.7 kB
2026-01-19T16:16:18.0362466Z Progress (1): 8.1 kB
2026-01-19T16:16:18.0368521Z Progress (1): 17 kB 
2026-01-19T16:16:18.0368859Z Progress (1): 19 kB
2026-01-19T16:16:18.0369132Z                    
2026-01-19T16:16:18.0369541Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.17.2/jackson-bom-2.17.2.pom (19 kB at 748 kB/s)
2026-01-19T16:16:18.0407413Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/26.0.1/messages-26.0.1.pom
2026-01-19T16:16:18.0650756Z Progress (1): 1.2 kB
2026-01-19T16:16:18.0654860Z Progress (1): 4.6 kB
2026-01-19T16:16:18.0658879Z Progress (1): 4.7 kB
2026-01-19T16:16:18.0662959Z                     
2026-01-19T16:16:18.0666116Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/26.0.1/messages-26.0.1.pom (4.7 kB at 189 kB/s)
2026-01-19T16:16:18.0689238Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.0/messages-27.0.0.pom
2026-01-19T16:16:18.0929091Z Progress (1): 1.2 kB
2026-01-19T16:16:18.0929507Z Progress (1): 4.6 kB
2026-01-19T16:16:18.0935190Z Progress (1): 4.7 kB
2026-01-19T16:16:18.0935906Z                     
2026-01-19T16:16:18.0937998Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.0/messages-27.0.0.pom (4.7 kB at 182 kB/s)
2026-01-19T16:16:18.0967024Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.3/junit-bom-5.11.3.pom
2026-01-19T16:16:18.1168454Z Progress (1): 908 B
2026-01-19T16:16:18.1171544Z Progress (1): 4.1 kB
2026-01-19T16:16:18.1173666Z Progress (1): 5.6 kB
2026-01-19T16:16:18.1174203Z                     
2026-01-19T16:16:18.1174708Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.3/junit-bom-5.11.3.pom (5.6 kB at 257 kB/s)
2026-01-19T16:16:18.1197114Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.0/jackson-bom-2.18.0.pom
2026-01-19T16:16:18.1418921Z Progress (1): 924 B
2026-01-19T16:16:18.1420831Z Progress (1): 2.7 kB
2026-01-19T16:16:18.1437375Z Progress (1): 8.1 kB
2026-01-19T16:16:18.1437973Z Progress (1): 17 kB 
2026-01-19T16:16:18.1438512Z Progress (1): 19 kB
2026-01-19T16:16:18.1439082Z                    
2026-01-19T16:16:18.1439745Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.0/jackson-bom-2.18.0.pom (19 kB at 850 kB/s)
2026-01-19T16:16:18.1447405Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.18/jackson-parent-2.18.pom
2026-01-19T16:16:18.1820045Z Progress (1): 1.1 kB
2026-01-19T16:16:18.1820767Z Progress (1): 2.5 kB
2026-01-19T16:16:18.1821332Z Progress (1): 4.0 kB
2026-01-19T16:16:18.1821808Z Progress (1): 6.5 kB
2026-01-19T16:16:18.1822534Z                     
2026-01-19T16:16:18.1823143Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.18/jackson-parent-2.18.pom (6.5 kB at 272 kB/s)
2026-01-19T16:16:18.1823844Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/61/oss-parent-61.pom
2026-01-19T16:16:18.1953283Z Progress (1): 952 B
2026-01-19T16:16:18.1953923Z Progress (1): 2.6 kB
2026-01-19T16:16:18.1960659Z Progress (1): 4.1 kB
2026-01-19T16:16:18.1964920Z Progress (1): 7.2 kB
2026-01-19T16:16:18.1968442Z Progress (1): 9.7 kB
2026-01-19T16:16:18.1972550Z Progress (1): 12 kB 
2026-01-19T16:16:18.1976678Z Progress (1): 15 kB
2026-01-19T16:16:18.1980707Z Progress (1): 18 kB
2026-01-19T16:16:18.1984648Z Progress (1): 23 kB
2026-01-19T16:16:18.1988829Z Progress (1): 23 kB
2026-01-19T16:16:18.1990602Z                    
2026-01-19T16:16:18.1991264Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/61/oss-parent-61.pom (23 kB at 941 kB/s)
2026-01-19T16:16:18.1998412Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.1/messages-27.0.1.pom
2026-01-19T16:16:18.2258506Z Progress (1): 1.2 kB
2026-01-19T16:16:18.2260484Z Progress (1): 4.6 kB
2026-01-19T16:16:18.2263611Z Progress (1): 4.7 kB
2026-01-19T16:16:18.2266664Z                     
2026-01-19T16:16:18.2267160Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.1/messages-27.0.1.pom (4.7 kB at 175 kB/s)
2026-01-19T16:16:18.2280567Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.1/jackson-bom-2.18.1.pom
2026-01-19T16:16:18.2575205Z Progress (1): 933 B
2026-01-19T16:16:18.2579303Z Progress (1): 2.7 kB
2026-01-19T16:16:18.2580096Z Progress (1): 8.1 kB
2026-01-19T16:16:18.2580624Z Progress (1): 17 kB 
2026-01-19T16:16:18.2584769Z Progress (1): 19 kB
2026-01-19T16:16:18.2588740Z                    
2026-01-19T16:16:18.2589249Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.1/jackson-bom-2.18.1.pom (19 kB at 603 kB/s)
2026-01-19T16:16:18.2601528Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.18.1/jackson-parent-2.18.1.pom
2026-01-19T16:16:18.2833469Z Progress (1): 1.1 kB
2026-01-19T16:16:18.2847183Z Progress (1): 2.5 kB
2026-01-19T16:16:18.2857814Z Progress (1): 4.1 kB
2026-01-19T16:16:18.2858344Z Progress (1): 6.3 kB
2026-01-19T16:16:18.2858903Z Progress (1): 6.7 kB
2026-01-19T16:16:18.2859345Z                     
2026-01-19T16:16:18.2859772Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.18.1/jackson-parent-2.18.1.pom (6.7 kB at 278 kB/s)
2026-01-19T16:16:18.2880358Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.2/messages-27.0.2.pom
2026-01-19T16:16:18.3129824Z Progress (1): 1.2 kB
2026-01-19T16:16:18.3136034Z Progress (1): 4.6 kB
2026-01-19T16:16:18.3136451Z Progress (1): 4.7 kB
2026-01-19T16:16:18.3137183Z                     
2026-01-19T16:16:18.3137685Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.0.2/messages-27.0.2.pom (4.7 kB at 182 kB/s)
2026-01-19T16:16:18.3155733Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.1.0/messages-27.1.0.pom
2026-01-19T16:16:18.3397301Z Progress (1): 1.2 kB
2026-01-19T16:16:18.3405795Z Progress (1): 4.6 kB
2026-01-19T16:16:18.3406124Z Progress (1): 4.7 kB
2026-01-19T16:16:18.3406436Z                     
2026-01-19T16:16:18.3407041Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.1.0/messages-27.1.0.pom (4.7 kB at 189 kB/s)
2026-01-19T16:16:18.3425149Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom
2026-01-19T16:16:18.3637696Z Progress (1): 908 B
2026-01-19T16:16:18.3641935Z Progress (1): 4.1 kB
2026-01-19T16:16:18.3642467Z Progress (1): 5.6 kB
2026-01-19T16:16:18.3642766Z                     
2026-01-19T16:16:18.3643194Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.4/junit-bom-5.11.4.pom (5.6 kB at 269 kB/s)
2026-01-19T16:16:18.3659775Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.2/jackson-bom-2.18.2.pom
2026-01-19T16:16:18.3871321Z Progress (1): 926 B
2026-01-19T16:16:18.3872976Z Progress (1): 2.7 kB
2026-01-19T16:16:18.3875031Z Progress (1): 8.1 kB
2026-01-19T16:16:18.3875377Z Progress (1): 17 kB 
2026-01-19T16:16:18.3877935Z Progress (1): 19 kB
2026-01-19T16:16:18.3879195Z                    
2026-01-19T16:16:18.3879679Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.18.2/jackson-bom-2.18.2.pom (19 kB at 850 kB/s)
2026-01-19T16:16:18.3903684Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.2.0/messages-27.2.0.pom
2026-01-19T16:16:18.4230489Z Progress (1): 1.3 kB
2026-01-19T16:16:18.4230845Z Progress (1): 4.6 kB
2026-01-19T16:16:18.4231133Z Progress (1): 4.7 kB
2026-01-19T16:16:18.4231401Z                     
2026-01-19T16:16:18.4231802Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/27.2.0/messages-27.2.0.pom (4.7 kB at 153 kB/s)
2026-01-19T16:16:18.4253383Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/28.0.0/messages-28.0.0.pom
2026-01-19T16:16:18.4490236Z Progress (1): 1.2 kB
2026-01-19T16:16:18.4490633Z Progress (1): 4.6 kB
2026-01-19T16:16:18.4492952Z Progress (1): 4.7 kB
2026-01-19T16:16:18.4494822Z                     
2026-01-19T16:16:18.4495237Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/28.0.0/messages-28.0.0.pom (4.7 kB at 189 kB/s)
2026-01-19T16:16:18.4519225Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.3/junit-bom-5.13.3.pom
2026-01-19T16:16:18.4745010Z Progress (1): 908 B
2026-01-19T16:16:18.4747303Z Progress (1): 4.1 kB
2026-01-19T16:16:18.4751489Z Progress (1): 5.7 kB
2026-01-19T16:16:18.4751901Z                     
2026-01-19T16:16:18.4754664Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.3/junit-bom-5.13.3.pom (5.7 kB at 246 kB/s)
2026-01-19T16:16:18.4768475Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.1/jackson-bom-2.19.1.pom
2026-01-19T16:16:18.5025817Z Progress (1): 926 B
2026-01-19T16:16:18.5027444Z Progress (1): 2.6 kB
2026-01-19T16:16:18.5028049Z Progress (1): 7.3 kB
2026-01-19T16:16:18.5030275Z Progress (1): 16 kB 
2026-01-19T16:16:18.5030804Z Progress (1): 20 kB
2026-01-19T16:16:18.5031827Z Progress (1): 20 kB
2026-01-19T16:16:18.5033571Z                    
2026-01-19T16:16:18.5035019Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.1/jackson-bom-2.19.1.pom (20 kB at 750 kB/s)
2026-01-19T16:16:18.5049850Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19.2/jackson-parent-2.19.2.pom
2026-01-19T16:16:18.5310465Z Progress (1): 1.1 kB
2026-01-19T16:16:18.5314149Z Progress (1): 2.5 kB
2026-01-19T16:16:18.5315717Z Progress (1): 4.2 kB
2026-01-19T16:16:18.5316299Z Progress (1): 6.1 kB
2026-01-19T16:16:18.5328230Z Progress (1): 7.2 kB
2026-01-19T16:16:18.5329352Z                     
2026-01-19T16:16:18.5330096Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19.2/jackson-parent-2.19.2.pom (7.2 kB at 266 kB/s)
2026-01-19T16:16:18.5337724Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/68/oss-parent-68.pom
2026-01-19T16:16:18.5587971Z Progress (1): 948 B
2026-01-19T16:16:18.5590748Z Progress (1): 2.9 kB
2026-01-19T16:16:18.5591468Z Progress (1): 4.1 kB
2026-01-19T16:16:18.5592395Z Progress (1): 6.1 kB
2026-01-19T16:16:18.5592992Z Progress (1): 9.9 kB
2026-01-19T16:16:18.5593507Z Progress (1): 12 kB 
2026-01-19T16:16:18.5593823Z Progress (1): 15 kB
2026-01-19T16:16:18.5594116Z Progress (1): 18 kB
2026-01-19T16:16:18.5594445Z Progress (1): 21 kB
2026-01-19T16:16:18.5600522Z Progress (1): 24 kB
2026-01-19T16:16:18.5600817Z                    
2026-01-19T16:16:18.5601200Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/68/oss-parent-68.pom (24 kB at 909 kB/s)
2026-01-19T16:16:18.5627792Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/28.1.0/messages-28.1.0.pom
2026-01-19T16:16:18.5944608Z Progress (1): 1.2 kB
2026-01-19T16:16:18.5944967Z Progress (1): 4.8 kB
2026-01-19T16:16:18.5949739Z Progress (1): 5.0 kB
2026-01-19T16:16:18.5950035Z                     
2026-01-19T16:16:18.5950397Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/28.1.0/messages-28.1.0.pom (5.0 kB at 155 kB/s)
2026-01-19T16:16:18.5970503Z Downloading from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-bom/3.27.3/assertj-bom-3.27.3.pom
2026-01-19T16:16:18.6193776Z Progress (1): 1.0 kB
2026-01-19T16:16:18.6199010Z Progress (1): 3.7 kB
2026-01-19T16:16:18.6200678Z                     
2026-01-19T16:16:18.6202503Z Downloaded from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-bom/3.27.3/assertj-bom-3.27.3.pom (3.7 kB at 160 kB/s)
2026-01-19T16:16:18.6219049Z Downloading from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-core/3.27.4/assertj-core-3.27.4.pom
2026-01-19T16:16:18.6453575Z Progress (1): 1.2 kB
2026-01-19T16:16:18.6467981Z Progress (1): 3.8 kB
2026-01-19T16:16:18.6468309Z                     
2026-01-19T16:16:18.6468707Z Downloaded from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-core/3.27.4/assertj-core-3.27.4.pom (3.8 kB at 159 kB/s)
2026-01-19T16:16:18.6477586Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.15.11/byte-buddy-1.15.11.pom
2026-01-19T16:16:18.6705558Z Progress (1): 948 B
2026-01-19T16:16:18.6711532Z Progress (1): 3.7 kB
2026-01-19T16:16:18.6712261Z Progress (1): 6.8 kB
2026-01-19T16:16:18.6712866Z Progress (1): 15 kB 
2026-01-19T16:16:18.6713447Z Progress (1): 17 kB
2026-01-19T16:16:18.6720039Z                    
2026-01-19T16:16:18.6721836Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.15.11/byte-buddy-1.15.11.pom (17 kB at 722 kB/s)
2026-01-19T16:16:18.6748055Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.15.11/byte-buddy-parent-1.15.11.pom
2026-01-19T16:16:18.7000106Z Progress (1): 829 B
2026-01-19T16:16:18.7001374Z Progress (1): 2.1 kB
2026-01-19T16:16:18.7001724Z Progress (1): 3.6 kB
2026-01-19T16:16:18.7002050Z Progress (1): 6.2 kB
2026-01-19T16:16:18.7002399Z Progress (1): 8.0 kB
2026-01-19T16:16:18.7002738Z Progress (1): 11 kB 
2026-01-19T16:16:18.7003072Z Progress (1): 13 kB
2026-01-19T16:16:18.7003417Z Progress (1): 17 kB
2026-01-19T16:16:18.7003755Z Progress (1): 22 kB
2026-01-19T16:16:18.7004102Z Progress (1): 25 kB
2026-01-19T16:16:18.7006701Z Progress (1): 34 kB
2026-01-19T16:16:18.7009451Z Progress (1): 47 kB
2026-01-19T16:16:18.7009939Z Progress (1): 52 kB
2026-01-19T16:16:18.7011333Z Progress (1): 57 kB
2026-01-19T16:16:18.7011630Z Progress (1): 63 kB
2026-01-19T16:16:18.7012078Z Progress (1): 63 kB
2026-01-19T16:16:18.7012384Z                    
2026-01-19T16:16:18.7012787Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.15.11/byte-buddy-parent-1.15.11.pom (63 kB at 2.4 MB/s)
2026-01-19T16:16:18.7039783Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/pretty-formatter/2.1.0/pretty-formatter-2.1.0.pom
2026-01-19T16:16:18.7272658Z Progress (1): 1.2 kB
2026-01-19T16:16:18.7279986Z Progress (1): 3.7 kB
2026-01-19T16:16:18.7280793Z                     
2026-01-19T16:16:18.7281878Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/pretty-formatter/2.1.0/pretty-formatter-2.1.0.pom (3.7 kB at 153 kB/s)
2026-01-19T16:16:18.7327552Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/maven-metadata.xml
2026-01-19T16:16:18.7551129Z Progress (1): 1.1 kB
2026-01-19T16:16:18.7552016Z                     
2026-01-19T16:16:18.7552795Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/maven-metadata.xml (1.1 kB at 44 kB/s)
2026-01-19T16:16:18.7565940Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.5.0/query-13.5.0.pom
2026-01-19T16:16:18.7784221Z Progress (1): 1.2 kB
2026-01-19T16:16:18.7790384Z Progress (1): 3.2 kB
2026-01-19T16:16:18.7792709Z                     
2026-01-19T16:16:18.7793181Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.5.0/query-13.5.0.pom (3.2 kB at 144 kB/s)
2026-01-19T16:16:18.7830526Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.6.0/query-13.6.0.pom
2026-01-19T16:16:18.8036061Z Progress (1): 1.2 kB
2026-01-19T16:16:18.8040476Z Progress (1): 3.2 kB
2026-01-19T16:16:18.8041124Z                     
2026-01-19T16:16:18.8043820Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.6.0/query-13.6.0.pom (3.2 kB at 151 kB/s)
2026-01-19T16:16:18.8087501Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/testng-xml-formatter/0.5.0/testng-xml-formatter-0.5.0.pom
2026-01-19T16:16:18.8312255Z Progress (1): 1.3 kB
2026-01-19T16:16:18.8322194Z Progress (1): 4.1 kB
2026-01-19T16:16:18.8322510Z                     
2026-01-19T16:16:18.8322920Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/testng-xml-formatter/0.5.0/testng-xml-formatter-0.5.0.pom (4.1 kB at 164 kB/s)
2026-01-19T16:16:18.8353473Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.3.0/query-13.3.0.pom
2026-01-19T16:16:18.8562909Z Progress (1): 1.3 kB
2026-01-19T16:16:18.8609845Z Progress (1): 3.2 kB
2026-01-19T16:16:18.8615152Z                     
2026-01-19T16:16:18.8615564Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.3.0/query-13.3.0.pom (3.2 kB at 127 kB/s)
2026-01-19T16:16:18.8623789Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.1/junit-bom-5.13.1.pom
2026-01-19T16:16:18.8847804Z Progress (1): 908 B
2026-01-19T16:16:18.8851707Z Progress (1): 4.1 kB
2026-01-19T16:16:18.8860554Z Progress (1): 5.6 kB
2026-01-19T16:16:18.8862990Z                     
2026-01-19T16:16:18.8865624Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.13.1/junit-bom-5.13.1.pom (5.6 kB at 226 kB/s)
2026-01-19T16:16:18.8892790Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.0/jackson-bom-2.19.0.pom
2026-01-19T16:16:18.9148673Z Progress (1): 922 B
2026-01-19T16:16:18.9150974Z Progress (1): 2.6 kB
2026-01-19T16:16:18.9151293Z Progress (1): 7.2 kB
2026-01-19T16:16:18.9151577Z Progress (1): 16 kB 
2026-01-19T16:16:18.9158532Z Progress (1): 20 kB
2026-01-19T16:16:18.9159062Z                    
2026-01-19T16:16:18.9159767Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.19.0/jackson-bom-2.19.0.pom (20 kB at 730 kB/s)
2026-01-19T16:16:18.9234608Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19/jackson-parent-2.19.pom
2026-01-19T16:16:18.9531242Z Progress (1): 1.1 kB
2026-01-19T16:16:18.9532355Z Progress (1): 2.5 kB
2026-01-19T16:16:18.9533158Z Progress (1): 4.1 kB
2026-01-19T16:16:18.9533839Z Progress (1): 6.3 kB
2026-01-19T16:16:18.9534473Z Progress (1): 6.7 kB
2026-01-19T16:16:18.9535060Z                     
2026-01-19T16:16:18.9535777Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-parent/2.19/jackson-parent-2.19.pom (6.7 kB at 215 kB/s)
2026-01-19T16:16:18.9579134Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/65/oss-parent-65.pom
2026-01-19T16:16:18.9821259Z Progress (1): 952 B
2026-01-19T16:16:18.9821994Z Progress (1): 2.6 kB
2026-01-19T16:16:18.9822638Z Progress (1): 4.0 kB
2026-01-19T16:16:18.9823101Z Progress (1): 6.6 kB
2026-01-19T16:16:18.9823540Z Progress (1): 9.8 kB
2026-01-19T16:16:18.9823986Z Progress (1): 12 kB 
2026-01-19T16:16:18.9824445Z Progress (1): 15 kB
2026-01-19T16:16:18.9824897Z Progress (1): 18 kB
2026-01-19T16:16:18.9825427Z Progress (1): 23 kB
2026-01-19T16:16:18.9826122Z                    
2026-01-19T16:16:18.9827389Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/oss-parent/65/oss-parent-65.pom (23 kB at 940 kB/s)
2026-01-19T16:16:18.9869862Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.4.0/query-13.4.0.pom
2026-01-19T16:16:19.0104602Z Progress (1): 1.2 kB
2026-01-19T16:16:19.0119838Z Progress (1): 3.2 kB
2026-01-19T16:16:19.0129068Z                     
2026-01-19T16:16:19.0133021Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.4.0/query-13.4.0.pom (3.2 kB at 127 kB/s)
2026-01-19T16:16:19.0198591Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/tag-expressions/6.1.2/tag-expressions-6.1.2.pom
2026-01-19T16:16:19.0419690Z Progress (1): 1.3 kB
2026-01-19T16:16:19.0427264Z Progress (1): 2.4 kB
2026-01-19T16:16:19.0427922Z                     
2026-01-19T16:16:19.0431154Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/tag-expressions/6.1.2/tag-expressions-6.1.2.pom (2.4 kB at 104 kB/s)
2026-01-19T16:16:19.0447513Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-expressions/18.0.1/cucumber-expressions-18.0.1.pom
2026-01-19T16:16:19.0675811Z Progress (1): 1.3 kB
2026-01-19T16:16:19.0681250Z Progress (1): 3.3 kB
2026-01-19T16:16:19.0683495Z                     
2026-01-19T16:16:19.0685798Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-expressions/18.0.1/cucumber-expressions-18.0.1.pom (3.3 kB at 145 kB/s)
2026-01-19T16:16:19.0707575Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/datatable/7.27.2/datatable-7.27.2.pom
2026-01-19T16:16:19.1522399Z Progress (1): 1.4 kB
2026-01-19T16:16:19.1523396Z Progress (1): 5.4 kB
2026-01-19T16:16:19.1523981Z Progress (1): 6.0 kB
2026-01-19T16:16:19.1524667Z                     
2026-01-19T16:16:19.1529415Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/datatable/7.27.2/datatable-7.27.2.pom (6.0 kB at 74 kB/s)
2026-01-19T16:16:19.1595879Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/docstring/7.27.2/docstring-7.27.2.pom
2026-01-19T16:16:19.1839271Z Progress (1): 1.6 kB
2026-01-19T16:16:19.1839615Z Progress (1): 2.7 kB
2026-01-19T16:16:19.1839890Z                     
2026-01-19T16:16:19.1840277Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/docstring/7.27.2/docstring-7.27.2.pom (2.7 kB at 99 kB/s)
2026-01-19T16:16:19.1897257Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/html-formatter/21.13.0/html-formatter-21.13.0.pom
2026-01-19T16:16:19.2125689Z Progress (1): 1.2 kB
2026-01-19T16:16:19.2133322Z Progress (1): 3.2 kB
2026-01-19T16:16:19.2134020Z                     
2026-01-19T16:16:19.2157257Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/html-formatter/21.13.0/html-formatter-21.13.0.pom (3.2 kB at 120 kB/s)
2026-01-19T16:16:19.2174342Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/18.0.0/messages-18.0.0.pom
2026-01-19T16:16:19.2396786Z Progress (1): 1.3 kB
2026-01-19T16:16:19.2403480Z Progress (1): 4.0 kB
2026-01-19T16:16:19.2403815Z                     
2026-01-19T16:16:19.2404283Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/18.0.0/messages-18.0.0.pom (4.0 kB at 168 kB/s)
2026-01-19T16:16:19.2431733Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/2.3.2/cucumber-parent-2.3.2.pom
2026-01-19T16:16:19.2669750Z Progress (1): 1.2 kB
2026-01-19T16:16:19.2672973Z Progress (1): 3.7 kB
2026-01-19T16:16:19.2676424Z Progress (1): 8.5 kB
2026-01-19T16:16:19.2677346Z Progress (1): 13 kB 
2026-01-19T16:16:19.2680198Z Progress (1): 18 kB
2026-01-19T16:16:19.2680584Z Progress (1): 22 kB
2026-01-19T16:16:19.2680852Z                    
2026-01-19T16:16:19.2681259Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-parent/2.3.2/cucumber-parent-2.3.2.pom (22 kB at 871 kB/s)
2026-01-19T16:16:19.2703081Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.8.2/junit-bom-5.8.2.pom
2026-01-19T16:16:19.2939333Z Progress (1): 907 B
2026-01-19T16:16:19.2944638Z Progress (1): 4.1 kB
2026-01-19T16:16:19.2944968Z Progress (1): 5.6 kB
2026-01-19T16:16:19.2945237Z                     
2026-01-19T16:16:19.2947815Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.8.2/junit-bom-5.8.2.pom (5.6 kB at 235 kB/s)
2026-01-19T16:16:19.2956853Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.2/jackson-bom-2.13.2.pom
2026-01-19T16:16:19.3181674Z Progress (1): 931 B
2026-01-19T16:16:19.3184953Z Progress (1): 2.7 kB
2026-01-19T16:16:19.3185345Z Progress (1): 8.7 kB
2026-01-19T16:16:19.3185724Z Progress (1): 17 kB 
2026-01-19T16:16:19.3191222Z Progress (1): 17 kB
2026-01-19T16:16:19.3207289Z                    
2026-01-19T16:16:19.3208337Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.2/jackson-bom-2.13.2.pom (17 kB at 755 kB/s)
2026-01-19T16:16:19.3226413Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.0.0/messages-19.0.0.pom
2026-01-19T16:16:19.3463018Z Progress (1): 1.3 kB
2026-01-19T16:16:19.3487902Z Progress (1): 4.1 kB
2026-01-19T16:16:19.3491776Z                     
2026-01-19T16:16:19.3493303Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.0.0/messages-19.0.0.pom (4.1 kB at 162 kB/s)
2026-01-19T16:16:19.3497991Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.3/jackson-bom-2.13.3.pom
2026-01-19T16:16:19.3736991Z Progress (1): 931 B
2026-01-19T16:16:19.3739644Z Progress (1): 2.7 kB
2026-01-19T16:16:19.3740445Z Progress (1): 8.9 kB
2026-01-19T16:16:19.3740761Z Progress (1): 17 kB 
2026-01-19T16:16:19.3741044Z Progress (1): 17 kB
2026-01-19T16:16:19.3741330Z                    
2026-01-19T16:16:19.3741776Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.13.3/jackson-bom-2.13.3.pom (17 kB at 723 kB/s)
2026-01-19T16:16:19.3774240Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.0/messages-19.1.0.pom
2026-01-19T16:16:19.4013764Z Progress (1): 1.3 kB
2026-01-19T16:16:19.4019726Z Progress (1): 4.1 kB
2026-01-19T16:16:19.4020394Z                     
2026-01-19T16:16:19.4021138Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.0/messages-19.1.0.pom (4.1 kB at 162 kB/s)
2026-01-19T16:16:19.4049134Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.1/messages-19.1.1.pom
2026-01-19T16:16:19.4412170Z Progress (1): 1.3 kB
2026-01-19T16:16:19.4416154Z Progress (1): 4.1 kB
2026-01-19T16:16:19.4417068Z                     
2026-01-19T16:16:19.4420116Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.1/messages-19.1.1.pom (4.1 kB at 110 kB/s)
2026-01-19T16:16:19.4452733Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.2/messages-19.1.2.pom
2026-01-19T16:16:19.4664443Z Progress (1): 1.3 kB
2026-01-19T16:16:19.4695405Z Progress (1): 4.1 kB
2026-01-19T16:16:19.4696107Z                     
2026-01-19T16:16:19.4697029Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.2/messages-19.1.2.pom (4.1 kB at 185 kB/s)
2026-01-19T16:16:19.4736959Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.3/messages-19.1.3.pom
2026-01-19T16:16:19.4963314Z Progress (1): 1.3 kB
2026-01-19T16:16:19.4965502Z Progress (1): 4.1 kB
2026-01-19T16:16:19.4969368Z                     
2026-01-19T16:16:19.4971214Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/19.1.3/messages-19.1.3.pom (4.1 kB at 177 kB/s)
2026-01-19T16:16:19.4985217Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.0/junit-bom-5.9.0.pom
2026-01-19T16:16:19.5205761Z Progress (1): 911 B
2026-01-19T16:16:19.5206192Z Progress (1): 4.1 kB
2026-01-19T16:16:19.5211023Z Progress (1): 5.6 kB
2026-01-19T16:16:19.5215404Z                     
2026-01-19T16:16:19.5218132Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.9.0/junit-bom-5.9.0.pom (5.6 kB at 245 kB/s)
2026-01-19T16:16:19.5247281Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/junit-xml-formatter/0.8.1/junit-xml-formatter-0.8.1.pom
2026-01-19T16:16:19.5484708Z Progress (1): 1.3 kB
2026-01-19T16:16:19.5489091Z Progress (1): 4.1 kB
2026-01-19T16:16:19.5491085Z                     
2026-01-19T16:16:19.5493713Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/junit-xml-formatter/0.8.1/junit-xml-formatter-0.8.1.pom (4.1 kB at 164 kB/s)
2026-01-19T16:16:19.5557395Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.0.2/query-13.0.2.pom
2026-01-19T16:16:19.5734920Z Progress (1): 1.3 kB
2026-01-19T16:16:19.5744535Z Progress (1): 3.2 kB
2026-01-19T16:16:19.5748810Z                     
2026-01-19T16:16:19.5751787Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.0.2/query-13.0.2.pom (3.2 kB at 138 kB/s)
2026-01-19T16:16:19.5846131Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.0.3/query-13.0.3.pom
2026-01-19T16:16:19.6053009Z Progress (1): 1.2 kB
2026-01-19T16:16:19.6056847Z Progress (1): 3.2 kB
2026-01-19T16:16:19.6057663Z                     
2026-01-19T16:16:19.6058640Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.0.3/query-13.0.3.pom (3.2 kB at 132 kB/s)
2026-01-19T16:16:19.6083813Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.1.0/query-13.1.0.pom
2026-01-19T16:16:19.6308833Z Progress (1): 1.3 kB
2026-01-19T16:16:19.6312035Z Progress (1): 3.2 kB
2026-01-19T16:16:19.6312812Z                     
2026-01-19T16:16:19.6314640Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.1.0/query-13.1.0.pom (3.2 kB at 132 kB/s)
2026-01-19T16:16:19.6334831Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.2.0/query-13.2.0.pom
2026-01-19T16:16:19.6548729Z Progress (1): 1.3 kB
2026-01-19T16:16:19.6552344Z Progress (1): 3.2 kB
2026-01-19T16:16:19.6555139Z                     
2026-01-19T16:16:19.6557761Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.2.0/query-13.2.0.pom (3.2 kB at 144 kB/s)
2026-01-19T16:16:19.6571080Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/ci-environment/10.0.1/ci-environment-10.0.1.pom
2026-01-19T16:16:19.6789748Z Progress (1): 1.2 kB
2026-01-19T16:16:19.6793052Z Progress (1): 4.1 kB
2026-01-19T16:16:19.6799804Z Progress (1): 6.1 kB
2026-01-19T16:16:19.6800436Z                     
2026-01-19T16:16:19.6801156Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/ci-environment/10.0.1/ci-environment-10.0.1.pom (6.1 kB at 263 kB/s)
2026-01-19T16:16:19.6824300Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.16.1/jackson-bom-2.16.1.pom
2026-01-19T16:16:19.7040504Z Progress (1): 924 B
2026-01-19T16:16:19.7041748Z Progress (1): 2.7 kB
2026-01-19T16:16:19.7042066Z Progress (1): 8.1 kB
2026-01-19T16:16:19.7042371Z Progress (1): 17 kB 
2026-01-19T16:16:19.7042877Z Progress (1): 18 kB
2026-01-19T16:16:19.7043180Z                    
2026-01-19T16:16:19.7043617Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-bom/2.16.1/jackson-bom-2.16.1.pom (18 kB at 829 kB/s)
2026-01-19T16:16:19.7072129Z Downloading from central: https://repo.maven.apache.org/maven2/org/testng/testng/7.11.0/testng-7.11.0.pom
2026-01-19T16:16:19.7329642Z Progress (1): 999 B
2026-01-19T16:16:19.7333719Z Progress (1): 2.6 kB
2026-01-19T16:16:19.7334409Z                     
2026-01-19T16:16:19.7335154Z Downloaded from central: https://repo.maven.apache.org/maven2/org/testng/testng/7.11.0/testng-7.11.0.pom (2.6 kB at 97 kB/s)
2026-01-19T16:16:19.7350134Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.16/slf4j-api-2.0.16.pom
2026-01-19T16:16:19.7565775Z Progress (1): 1.1 kB
2026-01-19T16:16:19.7570033Z Progress (1): 2.8 kB
2026-01-19T16:16:19.7586143Z                     
2026-01-19T16:16:19.7587237Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.16/slf4j-api-2.0.16.pom (2.8 kB at 128 kB/s)
2026-01-19T16:16:19.7587964Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.16/slf4j-parent-2.0.16.pom
2026-01-19T16:16:19.7808970Z Progress (1): 952 B
2026-01-19T16:16:19.7809642Z Progress (1): 3.2 kB
2026-01-19T16:16:19.7812752Z Progress (1): 6.0 kB
2026-01-19T16:16:19.7814059Z Progress (1): 8.2 kB
2026-01-19T16:16:19.7815975Z Progress (1): 11 kB 
2026-01-19T16:16:19.7820251Z Progress (1): 13 kB
2026-01-19T16:16:19.7820945Z                    
2026-01-19T16:16:19.7821666Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.16/slf4j-parent-2.0.16.pom (13 kB at 581 kB/s)
2026-01-19T16:16:19.7837993Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.16/slf4j-bom-2.0.16.pom
2026-01-19T16:16:19.8061528Z Progress (1): 1.0 kB
2026-01-19T16:16:19.8061946Z Progress (1): 4.6 kB
2026-01-19T16:16:19.8062336Z Progress (1): 7.2 kB
2026-01-19T16:16:19.8068090Z Progress (1): 7.3 kB
2026-01-19T16:16:19.8069204Z                     
2026-01-19T16:16:19.8070168Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.16/slf4j-bom-2.0.16.pom (7.3 kB at 319 kB/s)
2026-01-19T16:16:19.8094500Z Downloading from central: https://repo.maven.apache.org/maven2/org/jcommander/jcommander/1.83/jcommander-1.83.pom
2026-01-19T16:16:19.8333929Z Progress (1): 1.0 kB
2026-01-19T16:16:19.8334614Z Progress (1): 1.5 kB
2026-01-19T16:16:19.8335228Z                     
2026-01-19T16:16:19.8336875Z Downloaded from central: https://repo.maven.apache.org/maven2/org/jcommander/jcommander/1.83/jcommander-1.83.pom (1.5 kB at 59 kB/s)
2026-01-19T16:16:19.8364662Z Downloading from central: https://repo.maven.apache.org/maven2/org/webjars/jquery/3.7.1/jquery-3.7.1.pom
2026-01-19T16:16:19.8641643Z Progress (1): 1.2 kB
2026-01-19T16:16:19.8647853Z Progress (1): 3.7 kB
2026-01-19T16:16:19.8652574Z Progress (1): 7.6 kB
2026-01-19T16:16:19.8654280Z                     
2026-01-19T16:16:19.8655092Z Downloaded from central: https://repo.maven.apache.org/maven2/org/webjars/jquery/3.7.1/jquery-3.7.1.pom (7.6 kB at 271 kB/s)
2026-01-19T16:16:19.8682489Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-testng/7.27.2/cucumber-testng-7.27.2.pom
2026-01-19T16:16:19.8934938Z Progress (1): 1.8 kB
2026-01-19T16:16:19.8937474Z Progress (1): 2.2 kB
2026-01-19T16:16:19.8938118Z                     
2026-01-19T16:16:19.8938843Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-testng/7.27.2/cucumber-testng-7.27.2.pom (2.2 kB at 89 kB/s)
2026-01-19T16:16:19.8973761Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-java/7.27.2/cucumber-java-7.27.2.pom
2026-01-19T16:16:19.9194261Z Progress (1): 1.6 kB
2026-01-19T16:16:19.9198759Z Progress (1): 5.2 kB
2026-01-19T16:16:19.9205188Z Progress (1): 8.4 kB
2026-01-19T16:16:19.9209129Z                     
2026-01-19T16:16:19.9209995Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-java/7.27.2/cucumber-java-7.27.2.pom (8.4 kB at 350 kB/s)
2026-01-19T16:16:19.9251031Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-picocontainer/7.27.2/cucumber-picocontainer-7.27.2.pom
2026-01-19T16:16:20.0065080Z Progress (1): 1.9 kB
2026-01-19T16:16:20.0065955Z Progress (1): 3.8 kB
2026-01-19T16:16:20.0066959Z                     
2026-01-19T16:16:20.0068521Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-picocontainer/7.27.2/cucumber-picocontainer-7.27.2.pom (3.8 kB at 46 kB/s)
2026-01-19T16:16:20.0104241Z Downloading from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer/2.15.2/picocontainer-2.15.2.pom
2026-01-19T16:16:20.0347759Z Progress (1): 1.5 kB
2026-01-19T16:16:20.0352801Z Progress (1): 4.3 kB
2026-01-19T16:16:20.0357229Z                     
2026-01-19T16:16:20.0358202Z Downloaded from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer/2.15.2/picocontainer-2.15.2.pom (4.3 kB at 173 kB/s)
2026-01-19T16:16:20.0376847Z Downloading from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer-parent/2.15.2/picocontainer-parent-2.15.2.pom
2026-01-19T16:16:20.0714260Z Progress (1): 1.5 kB
2026-01-19T16:16:20.0717248Z Progress (1): 4.8 kB
2026-01-19T16:16:20.0717672Z Progress (1): 7.6 kB
2026-01-19T16:16:20.0719394Z Progress (1): 12 kB 
2026-01-19T16:16:20.0719913Z Progress (1): 12 kB
2026-01-19T16:16:20.0721764Z                    
2026-01-19T16:16:20.0722357Z Downloaded from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer-parent/2.15.2/picocontainer-parent-2.15.2.pom (12 kB at 346 kB/s)
2026-01-19T16:16:20.0748740Z Downloading from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer-root/2.15.2/picocontainer-root-2.15.2.pom
2026-01-19T16:16:20.0985793Z Progress (1): 1.3 kB
2026-01-19T16:16:20.0989886Z Progress (1): 2.4 kB
2026-01-19T16:16:20.0992649Z                     
2026-01-19T16:16:20.0993451Z Downloaded from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer-root/2.15.2/picocontainer-root-2.15.2.pom (2.4 kB at 98 kB/s)
2026-01-19T16:16:20.1013917Z Downloading from central: https://repo.maven.apache.org/maven2/net/masterthought/cucumber-reporting/5.8.3/cucumber-reporting-5.8.3.pom
2026-01-19T16:16:20.1801659Z Progress (1): 1.2 kB
2026-01-19T16:16:20.1802526Z Progress (1): 3.0 kB
2026-01-19T16:16:20.1804866Z Progress (1): 5.4 kB
2026-01-19T16:16:20.1805577Z Progress (1): 9.6 kB
2026-01-19T16:16:20.1805920Z Progress (1): 14 kB 
2026-01-19T16:16:20.1811779Z Progress (1): 15 kB
2026-01-19T16:16:20.1812087Z                    
2026-01-19T16:16:20.1812489Z Downloaded from central: https://repo.maven.apache.org/maven2/net/masterthought/cucumber-reporting/5.8.3/cucumber-reporting-5.8.3.pom (15 kB at 185 kB/s)
2026-01-19T16:16:20.1837146Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.18.0/jackson-databind-2.18.0.pom
2026-01-19T16:16:20.2078051Z Progress (1): 973 B
2026-01-19T16:16:20.2082223Z Progress (1): 2.3 kB
2026-01-19T16:16:20.2086392Z Progress (1): 4.0 kB
2026-01-19T16:16:20.2091524Z Progress (1): 6.4 kB
2026-01-19T16:16:20.2095710Z Progress (1): 8.1 kB
2026-01-19T16:16:20.2110897Z Progress (1): 10 kB 
2026-01-19T16:16:20.2111229Z Progress (1): 12 kB
2026-01-19T16:16:20.2111535Z Progress (1): 18 kB
2026-01-19T16:16:20.2111827Z Progress (1): 19 kB
2026-01-19T16:16:20.2112125Z Progress (1): 21 kB
2026-01-19T16:16:20.2112419Z Progress (1): 22 kB
2026-01-19T16:16:20.2112698Z                    
2026-01-19T16:16:20.2113129Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.18.0/jackson-databind-2.18.0.pom (22 kB at 862 kB/s)
2026-01-19T16:16:20.2116863Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.18.0/jackson-base-2.18.0.pom
2026-01-19T16:16:20.2334144Z Progress (1): 911 B
2026-01-19T16:16:20.2334889Z Progress (1): 2.7 kB
2026-01-19T16:16:20.2337614Z Progress (1): 4.5 kB
2026-01-19T16:16:20.2338019Z Progress (1): 6.6 kB
2026-01-19T16:16:20.2338371Z Progress (1): 8.7 kB
2026-01-19T16:16:20.2338733Z Progress (1): 11 kB 
2026-01-19T16:16:20.2341214Z Progress (1): 12 kB
2026-01-19T16:16:20.2342464Z                    
2026-01-19T16:16:20.2343007Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.18.0/jackson-base-2.18.0.pom (12 kB at 535 kB/s)
2026-01-19T16:16:20.2383093Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.18.0/jackson-annotations-2.18.0.pom
2026-01-19T16:16:20.2624838Z Progress (1): 946 B
2026-01-19T16:16:20.2625938Z Progress (1): 2.4 kB
2026-01-19T16:16:20.2627798Z Progress (1): 3.9 kB
2026-01-19T16:16:20.2628180Z Progress (1): 6.3 kB
2026-01-19T16:16:20.2630307Z Progress (1): 7.1 kB
2026-01-19T16:16:20.2630925Z                     
2026-01-19T16:16:20.2632359Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.18.0/jackson-annotations-2.18.0.pom (7.1 kB at 284 kB/s)
2026-01-19T16:16:20.2655371Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.18.0/jackson-core-2.18.0.pom
2026-01-19T16:16:20.2900226Z Progress (1): 980 B
2026-01-19T16:16:20.2903343Z Progress (1): 2.9 kB
2026-01-19T16:16:20.2903740Z Progress (1): 7.1 kB
2026-01-19T16:16:20.2904115Z Progress (1): 9.6 kB
2026-01-19T16:16:20.2907975Z Progress (1): 10 kB 
2026-01-19T16:16:20.2910509Z                    
2026-01-19T16:16:20.2916903Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.18.0/jackson-core-2.18.0.pom (10 kB at 400 kB/s)
2026-01-19T16:16:20.2938087Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.18.0/jackson-datatype-jsr310-2.18.0.pom
2026-01-19T16:16:20.3160857Z Progress (1): 983 B
2026-01-19T16:16:20.3161533Z Progress (1): 2.4 kB
2026-01-19T16:16:20.3162969Z Progress (1): 4.6 kB
2026-01-19T16:16:20.3166055Z Progress (1): 4.9 kB
2026-01-19T16:16:20.3167122Z                     
2026-01-19T16:16:20.3167671Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.18.0/jackson-datatype-jsr310-2.18.0.pom (4.9 kB at 213 kB/s)
2026-01-19T16:16:20.3180826Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/module/jackson-modules-java8/2.18.0/jackson-modules-java8-2.18.0.pom
2026-01-19T16:16:20.3427963Z Progress (1): 1.4 kB
2026-01-19T16:16:20.3428795Z Progress (1): 3.1 kB
2026-01-19T16:16:20.3438019Z Progress (1): 3.3 kB
2026-01-19T16:16:20.3438541Z                     
2026-01-19T16:16:20.3439084Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/module/jackson-modules-java8/2.18.0/jackson-modules-java8-2.18.0.pom (3.3 kB at 127 kB/s)
2026-01-19T16:16:20.3478868Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.pom
2026-01-19T16:16:20.3718659Z Progress (1): 1.3 kB
2026-01-19T16:16:20.3725081Z Progress (1): 4.5 kB
2026-01-19T16:16:20.3725439Z Progress (1): 8.2 kB
2026-01-19T16:16:20.3725785Z Progress (1): 10 kB 
2026-01-19T16:16:20.3726089Z                    
2026-01-19T16:16:20.3726741Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.pom (10 kB at 403 kB/s)
2026-01-19T16:16:20.3759210Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-parent/2.3/velocity-engine-parent-2.3.pom
2026-01-19T16:16:20.3994287Z Progress (1): 795 B
2026-01-19T16:16:20.4002105Z Progress (1): 2.2 kB
2026-01-19T16:16:20.4002461Z Progress (1): 5.9 kB
2026-01-19T16:16:20.4004873Z Progress (1): 9.3 kB
2026-01-19T16:16:20.4005492Z Progress (1): 12 kB 
2026-01-19T16:16:20.4005999Z Progress (1): 14 kB
2026-01-19T16:16:20.4007249Z                    
2026-01-19T16:16:20.4007907Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-parent/2.3/velocity-engine-parent-2.3.pom (14 kB at 512 kB/s)
2026-01-19T16:16:20.4021243Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-master/4/velocity-master-4.pom
2026-01-19T16:16:20.4252213Z Progress (1): 806 B
2026-01-19T16:16:20.4252841Z Progress (1): 2.4 kB
2026-01-19T16:16:20.4254237Z Progress (1): 5.9 kB
2026-01-19T16:16:20.4257375Z Progress (1): 7.8 kB
2026-01-19T16:16:20.4258579Z                     
2026-01-19T16:16:20.4259037Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-master/4/velocity-master-4.pom (7.8 kB at 324 kB/s)
2026-01-19T16:16:20.4269150Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/23/apache-23.pom
2026-01-19T16:16:20.4505718Z Progress (1): 749 B
2026-01-19T16:16:20.4509113Z Progress (1): 2.1 kB
2026-01-19T16:16:20.4512201Z Progress (1): 3.9 kB
2026-01-19T16:16:20.4512521Z Progress (1): 7.9 kB
2026-01-19T16:16:20.4512817Z Progress (1): 13 kB 
2026-01-19T16:16:20.4513138Z Progress (1): 16 kB
2026-01-19T16:16:20.4513449Z Progress (1): 18 kB
2026-01-19T16:16:20.4513737Z                    
2026-01-19T16:16:20.4514127Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/23/apache-23.pom (18 kB at 737 kB/s)
2026-01-19T16:16:20.4542913Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.11/commons-lang3-3.11.pom
2026-01-19T16:16:20.4823966Z Progress (1): 728 B
2026-01-19T16:16:20.4830607Z Progress (1): 2.0 kB
2026-01-19T16:16:20.4830954Z Progress (1): 5.2 kB
2026-01-19T16:16:20.4831275Z Progress (1): 8.8 kB
2026-01-19T16:16:20.4831556Z Progress (1): 12 kB 
2026-01-19T16:16:20.4831895Z Progress (1): 15 kB
2026-01-19T16:16:20.4832190Z Progress (1): 17 kB
2026-01-19T16:16:20.4832499Z Progress (1): 18 kB
2026-01-19T16:16:20.4832803Z Progress (1): 21 kB
2026-01-19T16:16:20.4833117Z Progress (1): 24 kB
2026-01-19T16:16:20.4833417Z Progress (1): 27 kB
2026-01-19T16:16:20.4833727Z Progress (1): 30 kB
2026-01-19T16:16:20.4834030Z Progress (1): 30 kB
2026-01-19T16:16:20.4834301Z                    
2026-01-19T16:16:20.4834666Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.11/commons-lang3-3.11.pom (30 kB at 1.0 MB/s)
2026-01-19T16:16:20.4859486Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/51/commons-parent-51.pom
2026-01-19T16:16:20.5151902Z Progress (1): 702 B
2026-01-19T16:16:20.5154145Z Progress (1): 1.8 kB
2026-01-19T16:16:20.5158223Z Progress (1): 3.1 kB
2026-01-19T16:16:20.5159837Z Progress (1): 4.6 kB
2026-01-19T16:16:20.5160481Z Progress (1): 6.7 kB
2026-01-19T16:16:20.5161101Z Progress (1): 8.1 kB
2026-01-19T16:16:20.5162945Z Progress (1): 10 kB 
2026-01-19T16:16:20.5163412Z Progress (1): 12 kB
2026-01-19T16:16:20.5163714Z Progress (1): 14 kB
2026-01-19T16:16:20.5164001Z Progress (1): 17 kB
2026-01-19T16:16:20.5164291Z Progress (1): 20 kB
2026-01-19T16:16:20.5164574Z Progress (1): 22 kB
2026-01-19T16:16:20.5165093Z Progress (1): 25 kB
2026-01-19T16:16:20.5165378Z Progress (1): 29 kB
2026-01-19T16:16:20.5165668Z Progress (1): 32 kB
2026-01-19T16:16:20.5165957Z Progress (1): 32 kB
2026-01-19T16:16:20.5166250Z Progress (1): 36 kB
2026-01-19T16:16:20.5166821Z Progress (1): 40 kB
2026-01-19T16:16:20.5167122Z Progress (1): 42 kB
2026-01-19T16:16:20.5167402Z Progress (1): 44 kB
2026-01-19T16:16:20.5168930Z Progress (1): 47 kB
2026-01-19T16:16:20.5169246Z Progress (1): 51 kB
2026-01-19T16:16:20.5171457Z Progress (1): 54 kB
2026-01-19T16:16:20.5172048Z Progress (1): 56 kB
2026-01-19T16:16:20.5173040Z Progress (1): 61 kB
2026-01-19T16:16:20.5173638Z Progress (1): 65 kB
2026-01-19T16:16:20.5174408Z Progress (1): 72 kB
2026-01-19T16:16:20.5197574Z Progress (1): 75 kB
2026-01-19T16:16:20.5198122Z Progress (1): 78 kB
2026-01-19T16:16:20.5198627Z                    
2026-01-19T16:16:20.5199256Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/51/commons-parent-51.pom (78 kB at 2.5 MB/s)
2026-01-19T16:16:20.5247000Z Downloading from central: https://repo.maven.apache.org/maven2/joda-time/joda-time/2.13.0/joda-time-2.13.0.pom
2026-01-19T16:16:20.5471802Z Progress (1): 889 B
2026-01-19T16:16:20.5474313Z Progress (1): 3.7 kB
2026-01-19T16:16:20.5477131Z Progress (1): 7.3 kB
2026-01-19T16:16:20.5477491Z Progress (1): 11 kB 
2026-01-19T16:16:20.5478730Z Progress (1): 13 kB
2026-01-19T16:16:20.5479078Z Progress (1): 16 kB
2026-01-19T16:16:20.5479400Z Progress (1): 19 kB
2026-01-19T16:16:20.5479714Z Progress (1): 26 kB
2026-01-19T16:16:20.5480049Z Progress (1): 29 kB
2026-01-19T16:16:20.5480370Z Progress (1): 31 kB
2026-01-19T16:16:20.5480673Z Progress (1): 34 kB
2026-01-19T16:16:20.5480992Z Progress (1): 38 kB
2026-01-19T16:16:20.5487814Z Progress (1): 40 kB
2026-01-19T16:16:20.5488117Z                    
2026-01-19T16:16:20.5488504Z Downloaded from central: https://repo.maven.apache.org/maven2/joda-time/joda-time/2.13.0/joda-time-2.13.0.pom (40 kB at 1.7 MB/s)
2026-01-19T16:16:20.5519300Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-configuration2/2.11.0/commons-configuration2-2.11.0.pom
2026-01-19T16:16:20.5768076Z Progress (1): 736 B
2026-01-19T16:16:20.5771140Z Progress (1): 2.2 kB
2026-01-19T16:16:20.5771942Z Progress (1): 3.8 kB
2026-01-19T16:16:20.5774173Z Progress (1): 7.1 kB
2026-01-19T16:16:20.5775089Z Progress (1): 12 kB 
2026-01-19T16:16:20.5777896Z Progress (1): 14 kB
2026-01-19T16:16:20.5778363Z Progress (1): 16 kB
2026-01-19T16:16:20.5778695Z Progress (1): 19 kB
2026-01-19T16:16:20.5779005Z Progress (1): 22 kB
2026-01-19T16:16:20.5779324Z Progress (1): 25 kB
2026-01-19T16:16:20.5779632Z Progress (1): 28 kB
2026-01-19T16:16:20.5779958Z Progress (1): 28 kB
2026-01-19T16:16:20.5781838Z                    
2026-01-19T16:16:20.5782640Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-configuration2/2.11.0/commons-configuration2-2.11.0.pom (28 kB at 1.1 MB/s)
2026-01-19T16:16:20.5810034Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/70/commons-parent-70.pom
2026-01-19T16:16:20.6063275Z Progress (1): 704 B
2026-01-19T16:16:20.6067370Z Progress (1): 1.9 kB
2026-01-19T16:16:20.6067738Z Progress (1): 3.2 kB
2026-01-19T16:16:20.6068055Z Progress (1): 4.6 kB
2026-01-19T16:16:20.6068370Z Progress (1): 6.7 kB
2026-01-19T16:16:20.6068687Z Progress (1): 8.4 kB
2026-01-19T16:16:20.6069001Z Progress (1): 11 kB 
2026-01-19T16:16:20.6069307Z Progress (1): 13 kB
2026-01-19T16:16:20.6069625Z Progress (1): 15 kB
2026-01-19T16:16:20.6069933Z Progress (1): 17 kB
2026-01-19T16:16:20.6070245Z Progress (1): 20 kB
2026-01-19T16:16:20.6070551Z Progress (1): 22 kB
2026-01-19T16:16:20.6070891Z Progress (1): 25 kB
2026-01-19T16:16:20.6071198Z Progress (1): 28 kB
2026-01-19T16:16:20.6071509Z Progress (1): 31 kB
2026-01-19T16:16:20.6072657Z Progress (1): 32 kB
2026-01-19T16:16:20.6073021Z Progress (1): 36 kB
2026-01-19T16:16:20.6073341Z Progress (1): 40 kB
2026-01-19T16:16:20.6073817Z Progress (1): 43 kB
2026-01-19T16:16:20.6074099Z Progress (1): 45 kB
2026-01-19T16:16:20.6074388Z Progress (1): 49 kB
2026-01-19T16:16:20.6077821Z Progress (1): 51 kB
2026-01-19T16:16:20.6078169Z Progress (1): 55 kB
2026-01-19T16:16:20.6080168Z Progress (1): 57 kB
2026-01-19T16:16:20.6085141Z Progress (1): 60 kB
2026-01-19T16:16:20.6085770Z Progress (1): 63 kB
2026-01-19T16:16:20.6086340Z Progress (1): 67 kB
2026-01-19T16:16:20.6087317Z Progress (1): 70 kB
2026-01-19T16:16:20.6087899Z Progress (1): 73 kB
2026-01-19T16:16:20.6088372Z Progress (1): 75 kB
2026-01-19T16:16:20.6090666Z Progress (1): 77 kB
2026-01-19T16:16:20.6090974Z                    
2026-01-19T16:16:20.6091375Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/70/commons-parent-70.pom (77 kB at 2.8 MB/s)
2026-01-19T16:16:20.6139064Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/32/apache-32.pom
2026-01-19T16:16:20.6368769Z Progress (1): 733 B
2026-01-19T16:16:20.6372096Z Progress (1): 2.0 kB
2026-01-19T16:16:20.6381558Z Progress (1): 4.0 kB
2026-01-19T16:16:20.6384911Z Progress (1): 5.9 kB
2026-01-19T16:16:20.6387933Z Progress (1): 10 kB 
2026-01-19T16:16:20.6391017Z Progress (1): 16 kB
2026-01-19T16:16:20.6394326Z Progress (1): 19 kB
2026-01-19T16:16:20.6402347Z Progress (1): 22 kB
2026-01-19T16:16:20.6408081Z Progress (1): 24 kB
2026-01-19T16:16:20.6408544Z                    
2026-01-19T16:16:20.6408935Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/32/apache-32.pom (24 kB at 864 kB/s)
2026-01-19T16:16:20.6453385Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0-M1/junit-bom-5.11.0-M1.pom
2026-01-19T16:16:20.6671543Z Progress (1): 903 B
2026-01-19T16:16:20.6673012Z Progress (1): 4.1 kB
2026-01-19T16:16:20.6718018Z Progress (1): 5.7 kB
2026-01-19T16:16:20.6718519Z                     
2026-01-19T16:16:20.6718939Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0-M1/junit-bom-5.11.0-M1.pom (5.7 kB at 228 kB/s)
2026-01-19T16:16:20.6744746Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.pom
2026-01-19T16:16:20.6971550Z Progress (1): 736 B
2026-01-19T16:16:20.6986032Z Progress (1): 2.0 kB
2026-01-19T16:16:20.6990092Z Progress (1): 4.7 kB
2026-01-19T16:16:20.6994004Z Progress (1): 8.3 kB
2026-01-19T16:16:20.6998303Z Progress (1): 12 kB 
2026-01-19T16:16:20.7002194Z Progress (1): 15 kB
2026-01-19T16:16:20.7003831Z Progress (1): 16 kB
2026-01-19T16:16:20.7004404Z Progress (1): 18 kB
2026-01-19T16:16:20.7004716Z Progress (1): 21 kB
2026-01-19T16:16:20.7005004Z Progress (1): 24 kB
2026-01-19T16:16:20.7005311Z Progress (1): 27 kB
2026-01-19T16:16:20.7005601Z Progress (1): 30 kB
2026-01-19T16:16:20.7005894Z Progress (1): 31 kB
2026-01-19T16:16:20.7006161Z                    
2026-01-19T16:16:20.7006762Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.pom (31 kB at 1.2 MB/s)
2026-01-19T16:16:20.7017440Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/64/commons-parent-64.pom
2026-01-19T16:16:20.7272198Z Progress (1): 702 B
2026-01-19T16:16:20.7275514Z Progress (1): 1.9 kB
2026-01-19T16:16:20.7278795Z Progress (1): 3.1 kB
2026-01-19T16:16:20.7279396Z Progress (1): 4.6 kB
2026-01-19T16:16:20.7279956Z Progress (1): 6.4 kB
2026-01-19T16:16:20.7280550Z Progress (1): 8.4 kB
2026-01-19T16:16:20.7281074Z Progress (1): 10 kB 
2026-01-19T16:16:20.7281596Z Progress (1): 13 kB
2026-01-19T16:16:20.7282963Z Progress (1): 14 kB
2026-01-19T16:16:20.7283697Z Progress (1): 18 kB
2026-01-19T16:16:20.7284023Z Progress (1): 19 kB
2026-01-19T16:16:20.7284339Z Progress (1): 23 kB
2026-01-19T16:16:20.7284630Z Progress (1): 25 kB
2026-01-19T16:16:20.7284915Z Progress (1): 28 kB
2026-01-19T16:16:20.7285206Z Progress (1): 32 kB
2026-01-19T16:16:20.7285500Z Progress (1): 32 kB
2026-01-19T16:16:20.7285943Z Progress (1): 35 kB
2026-01-19T16:16:20.7286231Z Progress (1): 41 kB
2026-01-19T16:16:20.7286791Z Progress (1): 43 kB
2026-01-19T16:16:20.7287091Z Progress (1): 46 kB
2026-01-19T16:16:20.7287382Z Progress (1): 49 kB
2026-01-19T16:16:20.7287667Z Progress (1): 51 kB
2026-01-19T16:16:20.7287951Z Progress (1): 54 kB
2026-01-19T16:16:20.7288250Z Progress (1): 58 kB
2026-01-19T16:16:20.7288537Z Progress (1): 60 kB
2026-01-19T16:16:20.7288857Z Progress (1): 64 kB
2026-01-19T16:16:20.7289167Z Progress (1): 67 kB
2026-01-19T16:16:20.7289491Z Progress (1): 71 kB
2026-01-19T16:16:20.7289787Z Progress (1): 74 kB
2026-01-19T16:16:20.7290095Z Progress (1): 76 kB
2026-01-19T16:16:20.7290417Z Progress (1): 78 kB
2026-01-19T16:16:20.7290886Z                    
2026-01-19T16:16:20.7291243Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/64/commons-parent-64.pom (78 kB at 2.8 MB/s)
2026-01-19T16:16:20.7361877Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.pom
2026-01-19T16:16:20.7594175Z Progress (1): 742 B
2026-01-19T16:16:20.7595553Z Progress (1): 2.1 kB
2026-01-19T16:16:20.7596120Z Progress (1): 3.7 kB
2026-01-19T16:16:20.7597125Z Progress (1): 6.7 kB
2026-01-19T16:16:20.7598558Z Progress (1): 9.0 kB
2026-01-19T16:16:20.7598879Z Progress (1): 13 kB 
2026-01-19T16:16:20.7599184Z Progress (1): 16 kB
2026-01-19T16:16:20.7599480Z Progress (1): 18 kB
2026-01-19T16:16:20.7599777Z Progress (1): 20 kB
2026-01-19T16:16:20.7600060Z                    
2026-01-19T16:16:20.7600466Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.12.0/commons-text-1.12.0.pom (20 kB at 827 kB/s)
2026-01-19T16:16:20.7629511Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/69/commons-parent-69.pom
2026-01-19T16:16:20.7897118Z Progress (1): 703 B
2026-01-19T16:16:20.7907491Z Progress (1): 1.9 kB
2026-01-19T16:16:20.7907835Z Progress (1): 3.1 kB
2026-01-19T16:16:20.7908128Z Progress (1): 4.6 kB
2026-01-19T16:16:20.7908411Z Progress (1): 6.4 kB
2026-01-19T16:16:20.7908699Z Progress (1): 8.4 kB
2026-01-19T16:16:20.7908978Z Progress (1): 9.9 kB
2026-01-19T16:16:20.7909264Z Progress (1): 12 kB 
2026-01-19T16:16:20.7909542Z Progress (1): 14 kB
2026-01-19T16:16:20.7909824Z Progress (1): 17 kB
2026-01-19T16:16:20.7910112Z Progress (1): 19 kB
2026-01-19T16:16:20.7910378Z Progress (1): 22 kB
2026-01-19T16:16:20.7910657Z Progress (1): 24 kB
2026-01-19T16:16:20.7910932Z Progress (1): 28 kB
2026-01-19T16:16:20.7911207Z Progress (1): 31 kB
2026-01-19T16:16:20.7911490Z Progress (1): 31 kB
2026-01-19T16:16:20.7911795Z Progress (1): 35 kB
2026-01-19T16:16:20.7912100Z Progress (1): 40 kB
2026-01-19T16:16:20.7912410Z Progress (1): 43 kB
2026-01-19T16:16:20.7912701Z Progress (1): 45 kB
2026-01-19T16:16:20.7912995Z Progress (1): 48 kB
2026-01-19T16:16:20.7913279Z Progress (1): 51 kB
2026-01-19T16:16:20.7913570Z Progress (1): 55 kB
2026-01-19T16:16:20.7913879Z Progress (1): 57 kB
2026-01-19T16:16:20.7914175Z Progress (1): 59 kB
2026-01-19T16:16:20.7914484Z Progress (1): 63 kB
2026-01-19T16:16:20.7914784Z Progress (1): 67 kB
2026-01-19T16:16:20.7915086Z Progress (1): 70 kB
2026-01-19T16:16:20.7915367Z Progress (1): 73 kB
2026-01-19T16:16:20.7915663Z Progress (1): 75 kB
2026-01-19T16:16:20.7927712Z Progress (1): 77 kB
2026-01-19T16:16:20.7928204Z                    
2026-01-19T16:16:20.7928630Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/69/commons-parent-69.pom (77 kB at 2.7 MB/s)
2026-01-19T16:16:20.7952948Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/31/apache-31.pom
2026-01-19T16:16:20.8195819Z Progress (1): 740 B
2026-01-19T16:16:20.8201643Z Progress (1): 2.1 kB
2026-01-19T16:16:20.8203212Z Progress (1): 3.9 kB
2026-01-19T16:16:20.8204418Z Progress (1): 6.2 kB
2026-01-19T16:16:20.8205224Z Progress (1): 11 kB 
2026-01-19T16:16:20.8205903Z Progress (1): 16 kB
2026-01-19T16:16:20.8206401Z Progress (1): 20 kB
2026-01-19T16:16:20.8206877Z Progress (1): 22 kB
2026-01-19T16:16:20.8207211Z Progress (1): 24 kB
2026-01-19T16:16:20.8207519Z                    
2026-01-19T16:16:20.8207917Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/31/apache-31.pom (24 kB at 941 kB/s)
2026-01-19T16:16:20.8239982Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.15.0/commons-lang3-3.15.0.pom
2026-01-19T16:16:20.8467641Z Progress (1): 739 B
2026-01-19T16:16:20.8469134Z Progress (1): 1.8 kB
2026-01-19T16:16:20.8469510Z Progress (1): 4.1 kB
2026-01-19T16:16:20.8469856Z Progress (1): 5.7 kB
2026-01-19T16:16:20.8470370Z Progress (1): 7.5 kB
2026-01-19T16:16:20.8474952Z Progress (1): 10.0 kB
2026-01-19T16:16:20.8475817Z Progress (1): 13 kB  
2026-01-19T16:16:20.8477888Z Progress (1): 17 kB
2026-01-19T16:16:20.8479221Z Progress (1): 19 kB
2026-01-19T16:16:20.8479555Z Progress (1): 22 kB
2026-01-19T16:16:20.8479875Z Progress (1): 26 kB
2026-01-19T16:16:20.8480194Z Progress (1): 29 kB
2026-01-19T16:16:20.8480515Z Progress (1): 31 kB
2026-01-19T16:16:20.8480799Z                    
2026-01-19T16:16:20.8481173Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.15.0/commons-lang3-3.15.0.pom (31 kB at 1.3 MB/s)
2026-01-19T16:16:20.8508342Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/71/commons-parent-71.pom
2026-01-19T16:16:20.8761898Z Progress (1): 704 B
2026-01-19T16:16:20.8762595Z Progress (1): 1.9 kB
2026-01-19T16:16:20.8763108Z Progress (1): 3.2 kB
2026-01-19T16:16:20.8763542Z Progress (1): 4.6 kB
2026-01-19T16:16:20.8764077Z Progress (1): 6.8 kB
2026-01-19T16:16:20.8764598Z Progress (1): 8.4 kB
2026-01-19T16:16:20.8765109Z Progress (1): 11 kB 
2026-01-19T16:16:20.8765583Z Progress (1): 13 kB
2026-01-19T16:16:20.8766041Z Progress (1): 15 kB
2026-01-19T16:16:20.8766670Z Progress (1): 17 kB
2026-01-19T16:16:20.8768735Z Progress (1): 20 kB
2026-01-19T16:16:20.8769029Z Progress (1): 22 kB
2026-01-19T16:16:20.8769341Z Progress (1): 25 kB
2026-01-19T16:16:20.8769643Z Progress (1): 28 kB
2026-01-19T16:16:20.8769954Z Progress (1): 32 kB
2026-01-19T16:16:20.8770272Z Progress (1): 32 kB
2026-01-19T16:16:20.8770633Z Progress (1): 36 kB
2026-01-19T16:16:20.8770935Z Progress (1): 40 kB
2026-01-19T16:16:20.8771236Z Progress (1): 43 kB
2026-01-19T16:16:20.8771534Z Progress (1): 45 kB
2026-01-19T16:16:20.8771836Z Progress (1): 49 kB
2026-01-19T16:16:20.8772129Z Progress (1): 51 kB
2026-01-19T16:16:20.8772411Z Progress (1): 55 kB
2026-01-19T16:16:20.8772706Z Progress (1): 57 kB
2026-01-19T16:16:20.8772989Z Progress (1): 60 kB
2026-01-19T16:16:20.8773292Z Progress (1): 63 kB
2026-01-19T16:16:20.8773575Z Progress (1): 67 kB
2026-01-19T16:16:20.8773865Z Progress (1): 70 kB
2026-01-19T16:16:20.8774156Z Progress (1): 73 kB
2026-01-19T16:16:20.8774444Z Progress (1): 75 kB
2026-01-19T16:16:20.8774726Z Progress (1): 78 kB
2026-01-19T16:16:20.8775003Z                    
2026-01-19T16:16:20.8775407Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/71/commons-parent-71.pom (78 kB at 2.9 MB/s)
2026-01-19T16:16:20.8813515Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0-M2/junit-bom-5.11.0-M2.pom
2026-01-19T16:16:20.9047296Z Progress (1): 903 B
2026-01-19T16:16:20.9047888Z Progress (1): 4.1 kB
2026-01-19T16:16:20.9048315Z Progress (1): 5.7 kB
2026-01-19T16:16:20.9048718Z                     
2026-01-19T16:16:20.9049156Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.11.0-M2/junit-bom-5.11.0-M2.pom (5.7 kB at 238 kB/s)
2026-01-19T16:16:20.9065526Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.16.1/commons-io-2.16.1.pom
2026-01-19T16:16:20.9305990Z Progress (1): 761 B
2026-01-19T16:16:20.9306335Z Progress (1): 2.0 kB
2026-01-19T16:16:20.9306822Z Progress (1): 4.9 kB
2026-01-19T16:16:20.9307161Z Progress (1): 6.7 kB
2026-01-19T16:16:20.9307648Z Progress (1): 8.8 kB
2026-01-19T16:16:20.9307976Z Progress (1): 12 kB 
2026-01-19T16:16:20.9308311Z Progress (1): 15 kB
2026-01-19T16:16:20.9308641Z Progress (1): 18 kB
2026-01-19T16:16:20.9310990Z Progress (1): 20 kB
2026-01-19T16:16:20.9314464Z                    
2026-01-19T16:16:20.9314904Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.16.1/commons-io-2.16.1.pom (20 kB at 785 kB/s)
2026-01-19T16:16:20.9358466Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.11.0/commons-text-1.11.0.pom
2026-01-19T16:16:20.9566866Z Progress (1): 747 B
2026-01-19T16:16:20.9567296Z Progress (1): 2.3 kB
2026-01-19T16:16:20.9567889Z Progress (1): 3.9 kB
2026-01-19T16:16:20.9568231Z Progress (1): 6.8 kB
2026-01-19T16:16:20.9568630Z Progress (1): 10 kB 
2026-01-19T16:16:20.9569055Z Progress (1): 14 kB
2026-01-19T16:16:20.9569438Z Progress (1): 16 kB
2026-01-19T16:16:20.9582821Z Progress (1): 19 kB
2026-01-19T16:16:20.9583176Z                    
2026-01-19T16:16:20.9583599Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.11.0/commons-text-1.11.0.pom (19 kB at 806 kB/s)
2026-01-19T16:16:20.9615983Z Downloading from central: https://repo.maven.apache.org/maven2/org/jsoup/jsoup/1.18.1/jsoup-1.18.1.pom
2026-01-19T16:16:20.9860925Z Progress (1): 791 B
2026-01-19T16:16:20.9861817Z Progress (1): 2.2 kB
2026-01-19T16:16:20.9862940Z Progress (1): 4.3 kB
2026-01-19T16:16:20.9863547Z Progress (1): 7.1 kB
2026-01-19T16:16:20.9865544Z Progress (1): 9.5 kB
2026-01-19T16:16:20.9866049Z Progress (1): 12 kB 
2026-01-19T16:16:20.9866377Z Progress (1): 15 kB
2026-01-19T16:16:20.9870252Z Progress (1): 16 kB
2026-01-19T16:16:20.9870995Z                    
2026-01-19T16:16:20.9871859Z Downloaded from central: https://repo.maven.apache.org/maven2/org/jsoup/jsoup/1.18.1/jsoup-1.18.1.pom (16 kB at 626 kB/s)
2026-01-19T16:16:20.9918355Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/owasp-java-html-sanitizer/20240325.1/owasp-java-html-sanitizer-20240325.1.pom
2026-01-19T16:16:21.0142525Z Progress (1): 984 B
2026-01-19T16:16:21.0146155Z Progress (1): 4.1 kB
2026-01-19T16:16:21.0165880Z Progress (1): 5.0 kB
2026-01-19T16:16:21.0167995Z                     
2026-01-19T16:16:21.0168498Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/owasp-java-html-sanitizer/20240325.1/owasp-java-html-sanitizer-20240325.1.pom (5.0 kB at 218 kB/s)
2026-01-19T16:16:21.0169320Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/parent/20240325.1/parent-20240325.1.pom
2026-01-19T16:16:21.0403803Z Progress (1): 969 B
2026-01-19T16:16:21.0407018Z Progress (1): 2.8 kB
2026-01-19T16:16:21.0407426Z Progress (1): 4.6 kB
2026-01-19T16:16:21.0407763Z Progress (1): 6.7 kB
2026-01-19T16:16:21.0408088Z Progress (1): 10 kB 
2026-01-19T16:16:21.0413946Z Progress (1): 11 kB
2026-01-19T16:16:21.0414280Z                    
2026-01-19T16:16:21.0414767Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/parent/20240325.1/parent-20240325.1.pom (11 kB at 439 kB/s)
2026-01-19T16:16:21.0432763Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java8-shim/20240325.1/java8-shim-20240325.1.pom
2026-01-19T16:16:21.0675460Z Progress (1): 1.1 kB
2026-01-19T16:16:21.0685917Z Progress (1): 1.2 kB
2026-01-19T16:16:21.0686330Z                     
2026-01-19T16:16:21.0687315Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java8-shim/20240325.1/java8-shim-20240325.1.pom (1.2 kB at 50 kB/s)
2026-01-19T16:16:21.0716368Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java10-shim/20240325.1/java10-shim-20240325.1.pom
2026-01-19T16:16:21.0941613Z Progress (1): 1.2 kB
2026-01-19T16:16:21.0944812Z Progress (1): 1.5 kB
2026-01-19T16:16:21.0945221Z                     
2026-01-19T16:16:21.0945705Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java10-shim/20240325.1/java10-shim-20240325.1.pom (1.5 kB at 64 kB/s)
2026-01-19T16:16:21.0972956Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/jcl-over-slf4j/2.0.16/jcl-over-slf4j-2.0.16.pom
2026-01-19T16:16:21.1197716Z Progress (1): 1.3 kB
2026-01-19T16:16:21.1217342Z Progress (1): 1.7 kB
2026-01-19T16:16:21.1218017Z                     
2026-01-19T16:16:21.1218716Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/jcl-over-slf4j/2.0.16/jcl-over-slf4j-2.0.16.pom (1.7 kB at 75 kB/s)
2026-01-19T16:16:21.1244504Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.17.1/jackson-databind-2.17.1.pom
2026-01-19T16:16:21.1499316Z Progress (1): 968 B
2026-01-19T16:16:21.1500523Z Progress (1): 2.4 kB
2026-01-19T16:16:21.1500967Z Progress (1): 4.0 kB
2026-01-19T16:16:21.1502578Z Progress (1): 6.2 kB
2026-01-19T16:16:21.1502993Z Progress (1): 8.0 kB
2026-01-19T16:16:21.1503391Z Progress (1): 10 kB 
2026-01-19T16:16:21.1506850Z Progress (1): 12 kB
2026-01-19T16:16:21.1507462Z Progress (1): 17 kB
2026-01-19T16:16:21.1512084Z Progress (1): 19 kB
2026-01-19T16:16:21.1512798Z Progress (1): 21 kB
2026-01-19T16:16:21.1513307Z Progress (1): 21 kB
2026-01-19T16:16:21.1513620Z                    
2026-01-19T16:16:21.1514081Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.17.1/jackson-databind-2.17.1.pom (21 kB at 759 kB/s)
2026-01-19T16:16:21.1528972Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.17.1/jackson-base-2.17.1.pom
2026-01-19T16:16:21.1752980Z Progress (1): 900 B
2026-01-19T16:16:21.1753603Z Progress (1): 2.4 kB
2026-01-19T16:16:21.1754893Z Progress (1): 4.2 kB
2026-01-19T16:16:21.1755210Z Progress (1): 6.2 kB
2026-01-19T16:16:21.1755501Z Progress (1): 8.5 kB
2026-01-19T16:16:21.1755785Z Progress (1): 11 kB 
2026-01-19T16:16:21.1756069Z Progress (1): 12 kB
2026-01-19T16:16:21.1756348Z                    
2026-01-19T16:16:21.1756919Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/jackson-base/2.17.1/jackson-base-2.17.1.pom (12 kB at 512 kB/s)
2026-01-19T16:16:21.1794267Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.17.1/jackson-annotations-2.17.1.pom
2026-01-19T16:16:21.2050941Z Progress (1): 946 B
2026-01-19T16:16:21.2053651Z Progress (1): 2.4 kB
2026-01-19T16:16:21.2054747Z Progress (1): 3.9 kB
2026-01-19T16:16:21.2055274Z Progress (1): 6.3 kB
2026-01-19T16:16:21.2058507Z Progress (1): 7.1 kB
2026-01-19T16:16:21.2059301Z                     
2026-01-19T16:16:21.2059715Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.17.1/jackson-annotations-2.17.1.pom (7.1 kB at 261 kB/s)
2026-01-19T16:16:21.2090473Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.17.1/jackson-core-2.17.1.pom
2026-01-19T16:16:21.2343739Z Progress (1): 977 B
2026-01-19T16:16:21.2344240Z Progress (1): 2.9 kB
2026-01-19T16:16:21.2344722Z Progress (1): 6.8 kB
2026-01-19T16:16:21.2345192Z Progress (1): 9.3 kB
2026-01-19T16:16:21.2347263Z Progress (1): 9.6 kB
2026-01-19T16:16:21.2349854Z                     
2026-01-19T16:16:21.2350915Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.17.1/jackson-core-2.17.1.pom (9.6 kB at 371 kB/s)
2026-01-19T16:16:21.2382455Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/2.0.16/slf4j-simple-2.0.16.pom
2026-01-19T16:16:21.2646210Z Progress (1): 1.3 kB
2026-01-19T16:16:21.2647369Z                     
2026-01-19T16:16:21.2648434Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/2.0.16/slf4j-simple-2.0.16.pom (1.3 kB at 49 kB/s)
2026-01-19T16:16:21.2681168Z Downloading from central: https://repo.maven.apache.org/maven2/com/aventstack/extentreports/5.1.1/extentreports-5.1.1.pom
2026-01-19T16:16:21.2964578Z Progress (1): 1.2 kB
2026-01-19T16:16:21.2968624Z Progress (1): 3.7 kB
2026-01-19T16:16:21.2972372Z Progress (1): 5.1 kB
2026-01-19T16:16:21.2972906Z                     
2026-01-19T16:16:21.2975758Z Downloaded from central: https://repo.maven.apache.org/maven2/com/aventstack/extentreports/5.1.1/extentreports-5.1.1.pom (5.1 kB at 176 kB/s)
2026-01-19T16:16:21.3018084Z Downloading from central: https://repo.maven.apache.org/maven2/io/reactivex/rxjava3/rxjava/3.1.6/rxjava-3.1.6.pom
2026-01-19T16:16:21.3245157Z Progress (1): 972 B
2026-01-19T16:16:21.3253916Z Progress (1): 1.8 kB
2026-01-19T16:16:21.3257041Z                     
2026-01-19T16:16:21.3257715Z Downloaded from central: https://repo.maven.apache.org/maven2/io/reactivex/rxjava3/rxjava/3.1.6/rxjava-3.1.6.pom (1.8 kB at 71 kB/s)
2026-01-19T16:16:21.3278772Z Downloading from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom
2026-01-19T16:16:21.3507483Z Progress (1): 1.1 kB
2026-01-19T16:16:21.3509680Z                     
2026-01-19T16:16:21.3510116Z Downloaded from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.pom (1.1 kB at 52 kB/s)
2026-01-19T16:16:21.3518223Z Downloading from central: https://repo.maven.apache.org/maven2/org/freemarker/freemarker/2.3.32/freemarker-2.3.32.pom
2026-01-19T16:16:21.3757484Z Progress (1): 828 B
2026-01-19T16:16:21.3758342Z Progress (1): 2.4 kB
2026-01-19T16:16:21.3764145Z Progress (1): 3.3 kB
2026-01-19T16:16:21.3764933Z                     
2026-01-19T16:16:21.3765806Z Downloaded from central: https://repo.maven.apache.org/maven2/org/freemarker/freemarker/2.3.32/freemarker-2.3.32.pom (3.3 kB at 145 kB/s)
2026-01-19T16:16:21.3780933Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/17/apache-17.pom
2026-01-19T16:16:21.4009373Z Progress (1): 748 B
2026-01-19T16:16:21.4010176Z Progress (1): 2.1 kB
2026-01-19T16:16:21.4010690Z Progress (1): 3.9 kB
2026-01-19T16:16:21.4011193Z Progress (1): 8.1 kB
2026-01-19T16:16:21.4011606Z Progress (1): 12 kB 
2026-01-19T16:16:21.4012034Z Progress (1): 15 kB
2026-01-19T16:16:21.4012496Z Progress (1): 16 kB
2026-01-19T16:16:21.4012983Z                    
2026-01-19T16:16:21.4013610Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/17/apache-17.pom (16 kB at 765 kB/s)
2026-01-19T16:16:21.4014699Z Downloading from central: https://repo.maven.apache.org/maven2/org/projectlombok/lombok/1.18.26/lombok-1.18.26.pom
2026-01-19T16:16:21.4248883Z Progress (1): 1.1 kB
2026-01-19T16:16:21.4251812Z Progress (1): 1.5 kB
2026-01-19T16:16:21.4252318Z                     
2026-01-19T16:16:21.4253024Z Downloaded from central: https://repo.maven.apache.org/maven2/org/projectlombok/lombok/1.18.26/lombok-1.18.26.pom (1.5 kB at 62 kB/s)
2026-01-19T16:16:21.4422006Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-cucumber7-jvm/2.29.0/allure-cucumber7-jvm-2.29.0.pom
2026-01-19T16:16:21.4667986Z Progress (1): 1.2 kB
2026-01-19T16:16:21.4671552Z Progress (1): 2.0 kB
2026-01-19T16:16:21.4671952Z                     
2026-01-19T16:16:21.4673550Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-cucumber7-jvm/2.29.0/allure-cucumber7-jvm-2.29.0.pom (2.0 kB at 77 kB/s)
2026-01-19T16:16:21.4691752Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-java-commons/2.29.0/allure-java-commons-2.29.0.pom
2026-01-19T16:16:21.4909681Z Progress (1): 1.2 kB
2026-01-19T16:16:21.4913939Z Progress (1): 2.2 kB
2026-01-19T16:16:21.4914660Z                     
2026-01-19T16:16:21.4917504Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-java-commons/2.29.0/allure-java-commons-2.29.0.pom (2.2 kB at 94 kB/s)
2026-01-19T16:16:21.4934652Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.13/slf4j-api-2.0.13.pom
2026-01-19T16:16:21.5153595Z Progress (1): 1.1 kB
2026-01-19T16:16:21.5157796Z Progress (1): 2.8 kB
2026-01-19T16:16:21.5158438Z                     
2026-01-19T16:16:21.5161885Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.13/slf4j-api-2.0.13.pom (2.8 kB at 123 kB/s)
2026-01-19T16:16:21.5173288Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.13/slf4j-parent-2.0.13.pom
2026-01-19T16:16:21.5417613Z Progress (1): 952 B
2026-01-19T16:16:21.5419833Z Progress (1): 3.2 kB
2026-01-19T16:16:21.5421986Z Progress (1): 6.0 kB
2026-01-19T16:16:21.5422321Z Progress (1): 8.2 kB
2026-01-19T16:16:21.5422640Z Progress (1): 11 kB 
2026-01-19T16:16:21.5425528Z Progress (1): 13 kB
2026-01-19T16:16:21.5426781Z                    
2026-01-19T16:16:21.5427657Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/2.0.13/slf4j-parent-2.0.13.pom (13 kB at 535 kB/s)
2026-01-19T16:16:21.5447470Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.13/slf4j-bom-2.0.13.pom
2026-01-19T16:16:21.5691918Z Progress (1): 1.0 kB
2026-01-19T16:16:21.5693515Z Progress (1): 4.6 kB
2026-01-19T16:16:21.5694745Z Progress (1): 7.2 kB
2026-01-19T16:16:21.5697563Z Progress (1): 7.3 kB
2026-01-19T16:16:21.5697940Z                     
2026-01-19T16:16:21.5698413Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-bom/2.0.13/slf4j-bom-2.0.13.pom (7.3 kB at 293 kB/s)
2026-01-19T16:16:21.5727335Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-model/2.29.0/allure-model-2.29.0.pom
2026-01-19T16:16:21.5950602Z Progress (1): 1.3 kB
2026-01-19T16:16:21.5954093Z Progress (1): 1.8 kB
2026-01-19T16:16:21.5954456Z                     
2026-01-19T16:16:21.5957398Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-model/2.29.0/allure-model-2.29.0.pom (1.8 kB at 73 kB/s)
2026-01-19T16:16:21.6726696Z Downloading from central: https://repo.maven.apache.org/maven2/io/appium/java-client/8.6.0/java-client-8.6.0.jar
2026-01-19T16:16:21.6733123Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.13.0/selenium-api-4.13.0.jar
2026-01-19T16:16:21.6744926Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.13.0/selenium-remote-driver-4.13.0.jar
2026-01-19T16:16:21.6799714Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/32.1.2-jre/guava-32.1.2-jre.jar
2026-01-19T16:16:21.6817586Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.1.1/auto-service-annotations-1.1.1.jar
2026-01-19T16:16:21.7194384Z Progress (1): 7.7/441 kB
2026-01-19T16:16:21.7200053Z Progress (1): 16/441 kB 
2026-01-19T16:16:21.7238235Z Progress (1): 32/441 kB
2026-01-19T16:16:21.7242383Z Progress (1): 49/441 kB
2026-01-19T16:16:21.7245839Z Progress (1): 65/441 kB
2026-01-19T16:16:21.7287820Z Progress (1): 81/441 kB
2026-01-19T16:16:21.7288396Z Progress (1): 98/441 kB
2026-01-19T16:16:21.7324487Z Progress (1): 114/441 kB
2026-01-19T16:16:21.7373567Z Progress (1): 131/441 kB
2026-01-19T16:16:21.7374149Z Progress (1): 147/441 kB
2026-01-19T16:16:21.7374583Z Progress (1): 163/441 kB
2026-01-19T16:16:21.7374999Z Progress (1): 180/441 kB
2026-01-19T16:16:21.7403916Z Progress (1): 196/441 kB
2026-01-19T16:16:21.7428615Z Progress (1): 213/441 kB
2026-01-19T16:16:21.7429498Z Progress (1): 229/441 kB
2026-01-19T16:16:21.7430015Z Progress (1): 245/441 kB
2026-01-19T16:16:21.7430471Z Progress (1): 262/441 kB
2026-01-19T16:16:21.7474505Z Progress (1): 278/441 kB
2026-01-19T16:16:21.7475104Z Progress (1): 294/441 kB
2026-01-19T16:16:21.7475652Z Progress (2): 294/441 kB | 0.9/635 kB
2026-01-19T16:16:21.7476362Z Progress (2): 294/441 kB | 2.3/635 kB
2026-01-19T16:16:21.7477062Z Progress (2): 294/441 kB | 3.6/635 kB
2026-01-19T16:16:21.7477645Z Progress (2): 294/441 kB | 5.0/635 kB
2026-01-19T16:16:21.7478144Z Progress (2): 294/441 kB | 6.4/635 kB
2026-01-19T16:16:21.7478643Z Progress (2): 294/441 kB | 7.7/635 kB
2026-01-19T16:16:21.7479140Z Progress (2): 294/441 kB | 9.1/635 kB
2026-01-19T16:16:21.7479636Z Progress (2): 294/441 kB | 10/635 kB 
2026-01-19T16:16:21.7480119Z Progress (2): 311/441 kB | 10/635 kB
2026-01-19T16:16:21.7480613Z Progress (2): 311/441 kB | 12/635 kB
2026-01-19T16:16:21.7481191Z Progress (2): 311/441 kB | 13/635 kB
2026-01-19T16:16:21.7481674Z Progress (2): 311/441 kB | 15/635 kB
2026-01-19T16:16:21.7482330Z Progress (2): 311/441 kB | 16/635 kB
2026-01-19T16:16:21.7482821Z Progress (2): 311/441 kB | 17/635 kB
2026-01-19T16:16:21.7483317Z Progress (2): 311/441 kB | 19/635 kB
2026-01-19T16:16:21.7483804Z Progress (2): 311/441 kB | 20/635 kB
2026-01-19T16:16:21.7484296Z Progress (2): 327/441 kB | 20/635 kB
2026-01-19T16:16:21.7484780Z Progress (2): 327/441 kB | 21/635 kB
2026-01-19T16:16:21.7485272Z Progress (2): 327/441 kB | 23/635 kB
2026-01-19T16:16:21.7485754Z Progress (2): 327/441 kB | 24/635 kB
2026-01-19T16:16:21.7486245Z Progress (2): 327/441 kB | 26/635 kB
2026-01-19T16:16:21.7486936Z Progress (2): 327/441 kB | 27/635 kB
2026-01-19T16:16:21.7537297Z Progress (2): 327/441 kB | 28/635 kB
2026-01-19T16:16:21.7537912Z Progress (2): 344/441 kB | 28/635 kB
2026-01-19T16:16:21.7538473Z Progress (2): 344/441 kB | 30/635 kB
2026-01-19T16:16:21.7538977Z Progress (2): 344/441 kB | 31/635 kB
2026-01-19T16:16:21.7539469Z Progress (2): 344/441 kB | 32/635 kB
2026-01-19T16:16:21.7539969Z Progress (2): 344/441 kB | 34/635 kB
2026-01-19T16:16:21.7540454Z Progress (2): 344/441 kB | 35/635 kB
2026-01-19T16:16:21.7540947Z Progress (2): 344/441 kB | 36/635 kB
2026-01-19T16:16:21.7541440Z Progress (2): 360/441 kB | 36/635 kB
2026-01-19T16:16:21.7541916Z Progress (2): 360/441 kB | 38/635 kB
2026-01-19T16:16:21.7542400Z Progress (2): 360/441 kB | 39/635 kB
2026-01-19T16:16:21.7542878Z Progress (2): 360/441 kB | 41/635 kB
2026-01-19T16:16:21.7543424Z Progress (2): 360/441 kB | 42/635 kB
2026-01-19T16:16:21.7543901Z Progress (2): 360/441 kB | 43/635 kB
2026-01-19T16:16:21.7544463Z Progress (2): 360/441 kB | 45/635 kB
2026-01-19T16:16:21.7544981Z Progress (2): 360/441 kB | 46/635 kB
2026-01-19T16:16:21.7545940Z Progress (2): 376/441 kB | 46/635 kB
2026-01-19T16:16:21.7546453Z Progress (2): 376/441 kB | 47/635 kB
2026-01-19T16:16:21.7547076Z Progress (2): 376/441 kB | 49/635 kB
2026-01-19T16:16:21.7548383Z Progress (2): 376/441 kB | 50/635 kB
2026-01-19T16:16:21.7548952Z Progress (2): 376/441 kB | 52/635 kB
2026-01-19T16:16:21.7549431Z Progress (2): 376/441 kB | 53/635 kB
2026-01-19T16:16:21.7549888Z Progress (2): 376/441 kB | 54/635 kB
2026-01-19T16:16:21.7550352Z Progress (2): 376/441 kB | 56/635 kB
2026-01-19T16:16:21.7550805Z Progress (2): 393/441 kB | 56/635 kB
2026-01-19T16:16:21.7572255Z Progress (2): 393/441 kB | 60/635 kB
2026-01-19T16:16:21.7573022Z Progress (2): 409/441 kB | 60/635 kB
2026-01-19T16:16:21.7573617Z Progress (2): 426/441 kB | 60/635 kB
2026-01-19T16:16:21.7604624Z Progress (2): 441 kB | 60/635 kB    
2026-01-19T16:16:21.7605208Z Progress (3): 441 kB | 60/635 kB | 0.9/3.2 kB
2026-01-19T16:16:21.7605709Z Progress (3): 441 kB | 60/635 kB | 2.3/3.2 kB
2026-01-19T16:16:21.7606197Z Progress (3): 441 kB | 60/635 kB | 3.2 kB    
2026-01-19T16:16:21.7606835Z                                          
2026-01-19T16:16:21.7607445Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/auto/service/auto-service-annotations/1.1.1/auto-service-annotations-1.1.1.jar (3.2 kB at 37 kB/s)
2026-01-19T16:16:21.7608190Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar
2026-01-19T16:16:21.7608815Z Progress (2): 441 kB | 64/635 kB
2026-01-19T16:16:21.7609290Z                                 
2026-01-19T16:16:21.7610070Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-remote-driver/4.13.0/selenium-remote-driver-4.13.0.jar (441 kB at 5.0 MB/s)
2026-01-19T16:16:21.7610863Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar
2026-01-19T16:16:21.7611528Z Progress (1): 68/635 kB
2026-01-19T16:16:21.7612003Z Progress (1): 73/635 kB
2026-01-19T16:16:21.7612487Z Progress (1): 77/635 kB
2026-01-19T16:16:21.7612969Z Progress (1): 81/635 kB
2026-01-19T16:16:21.7613451Z Progress (1): 85/635 kB
2026-01-19T16:16:21.7686146Z Progress (1): 89/635 kB
2026-01-19T16:16:21.7687160Z Progress (2): 89/635 kB | 0.9/227 kB
2026-01-19T16:16:21.7687721Z Progress (2): 89/635 kB | 2.3/227 kB
2026-01-19T16:16:21.7688384Z Progress (2): 89/635 kB | 3.6/227 kB
2026-01-19T16:16:21.7688938Z Progress (2): 89/635 kB | 5.0/227 kB
2026-01-19T16:16:21.7689447Z Progress (2): 89/635 kB | 6.4/227 kB
2026-01-19T16:16:21.7689912Z Progress (2): 89/635 kB | 7.7/227 kB
2026-01-19T16:16:21.7690412Z Progress (2): 89/635 kB | 9.1/227 kB
2026-01-19T16:16:21.7690921Z Progress (2): 89/635 kB | 10/227 kB 
2026-01-19T16:16:21.7691379Z Progress (2): 89/635 kB | 12/227 kB
2026-01-19T16:16:21.7691868Z Progress (2): 89/635 kB | 13/227 kB
2026-01-19T16:16:21.7692431Z Progress (2): 89/635 kB | 15/227 kB
2026-01-19T16:16:21.7693011Z Progress (2): 89/635 kB | 16/227 kB
2026-01-19T16:16:21.7693591Z Progress (2): 89/635 kB | 17/227 kB
2026-01-19T16:16:21.7694068Z Progress (2): 89/635 kB | 19/227 kB
2026-01-19T16:16:21.7694523Z Progress (2): 89/635 kB | 20/227 kB
2026-01-19T16:16:21.7695011Z Progress (2): 89/635 kB | 21/227 kB
2026-01-19T16:16:21.7695483Z Progress (2): 89/635 kB | 23/227 kB
2026-01-19T16:16:21.7695951Z Progress (2): 89/635 kB | 24/227 kB
2026-01-19T16:16:21.7696415Z Progress (2): 89/635 kB | 26/227 kB
2026-01-19T16:16:21.7697085Z Progress (2): 89/635 kB | 27/227 kB
2026-01-19T16:16:21.7697577Z Progress (2): 89/635 kB | 28/227 kB
2026-01-19T16:16:21.7698098Z Progress (2): 89/635 kB | 30/227 kB
2026-01-19T16:16:21.7700295Z Progress (2): 89/635 kB | 31/227 kB
2026-01-19T16:16:21.7702020Z Progress (2): 89/635 kB | 32/227 kB
2026-01-19T16:16:21.7704452Z Progress (2): 89/635 kB | 34/227 kB
2026-01-19T16:16:21.7704828Z Progress (2): 89/635 kB | 35/227 kB
2026-01-19T16:16:21.7722528Z Progress (2): 94/635 kB | 35/227 kB
2026-01-19T16:16:21.7727865Z Progress (2): 98/635 kB | 35/227 kB
2026-01-19T16:16:21.7767200Z Progress (2): 102/635 kB | 35/227 kB
2026-01-19T16:16:21.7768988Z Progress (2): 106/635 kB | 35/227 kB
2026-01-19T16:16:21.7769312Z Progress (2): 111/635 kB | 35/227 kB
2026-01-19T16:16:21.7769648Z Progress (2): 115/635 kB | 35/227 kB
2026-01-19T16:16:21.7769970Z Progress (2): 119/635 kB | 35/227 kB
2026-01-19T16:16:21.7770297Z Progress (2): 123/635 kB | 35/227 kB
2026-01-19T16:16:21.7770603Z Progress (2): 128/635 kB | 35/227 kB
2026-01-19T16:16:21.7770923Z Progress (2): 128/635 kB | 36/227 kB
2026-01-19T16:16:21.7836368Z Progress (2): 128/635 kB | 38/227 kB
2026-01-19T16:16:21.7836956Z Progress (2): 128/635 kB | 39/227 kB
2026-01-19T16:16:21.7837292Z Progress (2): 128/635 kB | 41/227 kB
2026-01-19T16:16:21.7837647Z Progress (2): 128/635 kB | 42/227 kB
2026-01-19T16:16:21.7837975Z Progress (2): 128/635 kB | 43/227 kB
2026-01-19T16:16:21.7838274Z Progress (2): 128/635 kB | 45/227 kB
2026-01-19T16:16:21.7838610Z Progress (2): 128/635 kB | 46/227 kB
2026-01-19T16:16:21.7838928Z Progress (2): 128/635 kB | 47/227 kB
2026-01-19T16:16:21.7839234Z Progress (2): 128/635 kB | 49/227 kB
2026-01-19T16:16:21.7839541Z Progress (2): 128/635 kB | 50/227 kB
2026-01-19T16:16:21.7839863Z Progress (2): 128/635 kB | 52/227 kB
2026-01-19T16:16:21.7840187Z Progress (2): 128/635 kB | 53/227 kB
2026-01-19T16:16:21.7840523Z Progress (2): 128/635 kB | 54/227 kB
2026-01-19T16:16:21.7840856Z Progress (2): 128/635 kB | 56/227 kB
2026-01-19T16:16:21.7841203Z Progress (2): 128/635 kB | 60/227 kB
2026-01-19T16:16:21.7841668Z Progress (2): 128/635 kB | 64/227 kB
2026-01-19T16:16:21.7842001Z Progress (2): 128/635 kB | 66/227 kB
2026-01-19T16:16:21.7842310Z Progress (2): 128/635 kB | 70/227 kB
2026-01-19T16:16:21.7842652Z Progress (2): 128/635 kB | 74/227 kB
2026-01-19T16:16:21.7842989Z Progress (2): 128/635 kB | 78/227 kB
2026-01-19T16:16:21.7843301Z Progress (2): 132/635 kB | 78/227 kB
2026-01-19T16:16:21.7843609Z Progress (2): 136/635 kB | 78/227 kB
2026-01-19T16:16:21.7843934Z Progress (2): 140/635 kB | 78/227 kB
2026-01-19T16:16:21.7844244Z Progress (2): 144/635 kB | 78/227 kB
2026-01-19T16:16:21.7844666Z Progress (2): 149/635 kB | 78/227 kB
2026-01-19T16:16:21.7846967Z Progress (2): 153/635 kB | 78/227 kB
2026-01-19T16:16:21.7847917Z Progress (2): 157/635 kB | 78/227 kB
2026-01-19T16:16:21.7848267Z Progress (2): 161/635 kB | 78/227 kB
2026-01-19T16:16:21.7848585Z Progress (2): 166/635 kB | 78/227 kB
2026-01-19T16:16:21.7848887Z Progress (2): 170/635 kB | 78/227 kB
2026-01-19T16:16:21.7849193Z Progress (2): 174/635 kB | 78/227 kB
2026-01-19T16:16:21.7849508Z Progress (2): 178/635 kB | 78/227 kB
2026-01-19T16:16:21.7849807Z Progress (2): 183/635 kB | 78/227 kB
2026-01-19T16:16:21.7850110Z Progress (2): 187/635 kB | 78/227 kB
2026-01-19T16:16:21.7850402Z Progress (2): 191/635 kB | 78/227 kB
2026-01-19T16:16:21.7850702Z Progress (2): 195/635 kB | 78/227 kB
2026-01-19T16:16:21.7850999Z Progress (2): 195/635 kB | 82/227 kB
2026-01-19T16:16:21.7851303Z Progress (2): 195/635 kB | 87/227 kB
2026-01-19T16:16:21.7851609Z Progress (2): 195/635 kB | 91/227 kB
2026-01-19T16:16:21.7851919Z Progress (2): 195/635 kB | 95/227 kB
2026-01-19T16:16:21.7852256Z Progress (2): 195/635 kB | 99/227 kB
2026-01-19T16:16:21.7852616Z Progress (2): 195/635 kB | 104/227 kB
2026-01-19T16:16:21.7852950Z Progress (2): 195/635 kB | 108/227 kB
2026-01-19T16:16:21.7853282Z Progress (2): 195/635 kB | 112/227 kB
2026-01-19T16:16:21.7853609Z Progress (2): 195/635 kB | 116/227 kB
2026-01-19T16:16:21.7853941Z Progress (2): 195/635 kB | 121/227 kB
2026-01-19T16:16:21.7854279Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7854619Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7854949Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7855285Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7855614Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7933183Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7936431Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7937397Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7937907Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7938256Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7938587Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7938911Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7939259Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7939627Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7940040Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7940394Z Progress (4): 195/635 kB | 121/227 kB | 0/3.0 MB | 4.6 kB
2026-01-19T16:16:21.7940718Z                                                          
2026-01-19T16:16:21.7941137Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/failureaccess/1.0.1/failureaccess-1.0.1.jar (4.6 kB at 42 kB/s)
2026-01-19T16:16:21.7941653Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.jar
2026-01-19T16:16:21.7942076Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7942418Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7942759Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7943097Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7943442Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7943920Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7944266Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7944600Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7944939Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7945271Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7945609Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7945942Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7946285Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7946807Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7947330Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7947677Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7948015Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7948352Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7948686Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7949025Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7949359Z Progress (3): 195/635 kB | 121/227 kB | 0/3.0 MB
2026-01-19T16:16:21.7949697Z Progress (3): 195/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7950035Z Progress (3): 195/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7950377Z Progress (3): 195/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7950715Z Progress (3): 199/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7951056Z Progress (3): 204/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7951401Z Progress (3): 208/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7951755Z Progress (3): 212/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7952094Z Progress (3): 216/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7952439Z Progress (3): 221/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7952776Z Progress (3): 225/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7953122Z Progress (3): 241/635 kB | 121/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7953459Z Progress (3): 241/635 kB | 125/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7953799Z Progress (3): 241/635 kB | 129/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7954134Z Progress (3): 241/635 kB | 133/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7954477Z Progress (3): 241/635 kB | 137/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7954814Z Progress (3): 241/635 kB | 142/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7955159Z Progress (3): 241/635 kB | 146/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7955493Z Progress (3): 241/635 kB | 150/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7955834Z Progress (3): 241/635 kB | 154/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7956177Z Progress (3): 241/635 kB | 159/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7987177Z Progress (3): 241/635 kB | 163/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7987587Z Progress (3): 241/635 kB | 167/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.7987948Z Progress (3): 241/635 kB | 171/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8046769Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8047289Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8047737Z Progress (4): 241/635 kB | 175/227 kB | 0.1/3.0 MB | 0.9/2.2 kB
2026-01-19T16:16:21.8048181Z Progress (4): 241/635 kB | 175/227 kB | 0.1/3.0 MB | 2.2 kB    
2026-01-19T16:16:21.8048555Z                                                            
2026-01-19T16:16:21.8086156Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/listenablefuture/9999.0-empty-to-avoid-conflict-with-guava/listenablefuture-9999.0-empty-to-avoid-conflict-with-guava.jar (2.2 kB at 17 kB/s)
2026-01-19T16:16:21.8089706Z Downloading from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.33.0/checker-qual-3.33.0.jar
2026-01-19T16:16:21.8090293Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8090770Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8091426Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8091895Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8092371Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8092853Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8093379Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8094143Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8094666Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8095224Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8095651Z Progress (3): 241/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8096244Z Progress (3): 258/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8096899Z Progress (3): 274/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8097334Z Progress (3): 290/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8097770Z Progress (3): 307/635 kB | 175/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8098203Z Progress (3): 307/635 kB | 180/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8098628Z Progress (3): 307/635 kB | 180/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8099054Z Progress (3): 307/635 kB | 184/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8099488Z Progress (3): 307/635 kB | 189/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8099922Z Progress (3): 307/635 kB | 193/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8100359Z Progress (3): 307/635 kB | 197/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8100817Z Progress (3): 307/635 kB | 201/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8101250Z Progress (3): 307/635 kB | 206/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8101799Z Progress (3): 307/635 kB | 210/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8102173Z Progress (3): 307/635 kB | 214/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8102524Z Progress (3): 307/635 kB | 218/227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8103117Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB    
2026-01-19T16:16:21.8103868Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8104496Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8105005Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8105343Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8105677Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8106002Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8106332Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8106829Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8107169Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8107496Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8107845Z Progress (3): 307/635 kB | 227 kB | 0.1/3.0 MB
2026-01-19T16:16:21.8108184Z Progress (4): 307/635 kB | 227 kB | 0.1/3.0 MB | 7.7/20 kB
2026-01-19T16:16:21.8108537Z Progress (4): 307/635 kB | 227 kB | 0.1/3.0 MB | 16/20 kB 
2026-01-19T16:16:21.8108880Z Progress (4): 307/635 kB | 227 kB | 0.1/3.0 MB | 16/20 kB
2026-01-19T16:16:21.8109265Z Progress (4): 307/635 kB | 227 kB | 0.1/3.0 MB | 20 kB   
2026-01-19T16:16:21.8109607Z Progress (4): 307/635 kB | 227 kB | 0.2/3.0 MB | 20 kB
2026-01-19T16:16:21.8109955Z Progress (4): 307/635 kB | 227 kB | 0.2/3.0 MB | 20 kB
2026-01-19T16:16:21.8110309Z Progress (4): 307/635 kB | 227 kB | 0.2/3.0 MB | 20 kB
2026-01-19T16:16:21.8110647Z                                                       
2026-01-19T16:16:21.8111055Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/code/findbugs/jsr305/3.0.2/jsr305-3.0.2.jar (20 kB at 150 kB/s)
2026-01-19T16:16:21.8111596Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-api/4.13.0/selenium-api-4.13.0.jar (227 kB at 1.7 MB/s)
2026-01-19T16:16:21.8112623Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.18.0/error_prone_annotations-2.18.0.jar
2026-01-19T16:16:21.8114875Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/2.8/j2objc-annotations-2.8.jar
2026-01-19T16:16:21.8128988Z Progress (2): 323/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8129942Z Progress (2): 340/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8139160Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8144299Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8149496Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8170504Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8175211Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8179600Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8180220Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8180848Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8181183Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8181494Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8181810Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8182119Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8182442Z Progress (2): 356/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8182753Z Progress (2): 372/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8183093Z Progress (2): 389/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8303015Z Progress (2): 405/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8304988Z Progress (2): 405/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8305507Z Progress (2): 405/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8305862Z Progress (2): 405/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8306174Z Progress (2): 405/635 kB | 0.2/3.0 MB
2026-01-19T16:16:21.8306814Z Progress (2): 405/635 kB | 0.3/3.0 MB
2026-01-19T16:16:21.8307150Z Progress (2): 421/635 kB | 0.3/3.0 MB
2026-01-19T16:16:21.8307556Z Progress (2): 438/635 kB | 0.3/3.0 MB
2026-01-19T16:16:21.8307901Z Progress (2): 454/635 kB | 0.3/3.0 MB
2026-01-19T16:16:21.8308226Z Progress (2): 471/635 kB | 0.3/3.0 MB
2026-01-19T16:16:21.8308558Z Progress (3): 471/635 kB | 0.3/3.0 MB | 0.9/224 kB
2026-01-19T16:16:21.8308894Z Progress (3): 471/635 kB | 0.3/3.0 MB | 2.3/224 kB
2026-01-19T16:16:21.8309241Z Progress (3): 471/635 kB | 0.3/3.0 MB | 3.6/224 kB
2026-01-19T16:16:21.8309577Z Progress (3): 471/635 kB | 0.3/3.0 MB | 5.0/224 kB
2026-01-19T16:16:21.8309912Z Progress (3): 471/635 kB | 0.3/3.0 MB | 6.4/224 kB
2026-01-19T16:16:21.8310241Z Progress (3): 471/635 kB | 0.3/3.0 MB | 7.7/224 kB
2026-01-19T16:16:21.8310573Z Progress (3): 471/635 kB | 0.3/3.0 MB | 9.1/224 kB
2026-01-19T16:16:21.8310911Z Progress (3): 471/635 kB | 0.3/3.0 MB | 10/224 kB 
2026-01-19T16:16:21.8311241Z Progress (3): 471/635 kB | 0.3/3.0 MB | 12/224 kB
2026-01-19T16:16:21.8311576Z Progress (3): 471/635 kB | 0.3/3.0 MB | 13/224 kB
2026-01-19T16:16:21.8311937Z Progress (3): 471/635 kB | 0.3/3.0 MB | 15/224 kB
2026-01-19T16:16:21.8312258Z Progress (3): 471/635 kB | 0.3/3.0 MB | 16/224 kB
2026-01-19T16:16:21.8312594Z Progress (3): 471/635 kB | 0.3/3.0 MB | 17/224 kB
2026-01-19T16:16:21.8312914Z Progress (3): 471/635 kB | 0.3/3.0 MB | 19/224 kB
2026-01-19T16:16:21.8313265Z Progress (3): 471/635 kB | 0.3/3.0 MB | 20/224 kB
2026-01-19T16:16:21.8313582Z Progress (3): 471/635 kB | 0.3/3.0 MB | 21/224 kB
2026-01-19T16:16:21.8313905Z Progress (3): 471/635 kB | 0.3/3.0 MB | 23/224 kB
2026-01-19T16:16:21.8314232Z Progress (3): 471/635 kB | 0.3/3.0 MB | 24/224 kB
2026-01-19T16:16:21.8314566Z Progress (3): 471/635 kB | 0.3/3.0 MB | 26/224 kB
2026-01-19T16:16:21.8319401Z Progress (3): 471/635 kB | 0.3/3.0 MB | 27/224 kB
2026-01-19T16:16:21.8323145Z Progress (3): 471/635 kB | 0.3/3.0 MB | 28/224 kB
2026-01-19T16:16:21.8331096Z Progress (3): 471/635 kB | 0.3/3.0 MB | 30/224 kB
2026-01-19T16:16:21.8382057Z Progress (3): 471/635 kB | 0.3/3.0 MB | 31/224 kB
2026-01-19T16:16:21.8382602Z Progress (3): 471/635 kB | 0.3/3.0 MB | 31/224 kB
2026-01-19T16:16:21.8383002Z Progress (3): 471/635 kB | 0.3/3.0 MB | 31/224 kB
2026-01-19T16:16:21.8383324Z Progress (3): 471/635 kB | 0.3/3.0 MB | 32/224 kB
2026-01-19T16:16:21.8383679Z Progress (3): 471/635 kB | 0.3/3.0 MB | 34/224 kB
2026-01-19T16:16:21.8384045Z Progress (3): 471/635 kB | 0.3/3.0 MB | 35/224 kB
2026-01-19T16:16:21.8384624Z Progress (3): 471/635 kB | 0.3/3.0 MB | 36/224 kB
2026-01-19T16:16:21.8384963Z Progress (3): 471/635 kB | 0.3/3.0 MB | 38/224 kB
2026-01-19T16:16:21.8385303Z Progress (3): 487/635 kB | 0.3/3.0 MB | 38/224 kB
2026-01-19T16:16:21.8385628Z Progress (3): 503/635 kB | 0.3/3.0 MB | 38/224 kB
2026-01-19T16:16:21.8385963Z Progress (3): 520/635 kB | 0.3/3.0 MB | 38/224 kB
2026-01-19T16:16:21.8386298Z Progress (4): 520/635 kB | 0.3/3.0 MB | 38/224 kB | 7.7/9.3 kB
2026-01-19T16:16:21.8386886Z Progress (4): 520/635 kB | 0.3/3.0 MB | 38/224 kB | 9.3 kB    
2026-01-19T16:16:21.8387235Z Progress (4): 520/635 kB | 0.3/3.0 MB | 39/224 kB | 9.3 kB
2026-01-19T16:16:21.8387721Z Progress (4): 520/635 kB | 0.3/3.0 MB | 41/224 kB | 9.3 kB
2026-01-19T16:16:21.8388059Z                                                           
2026-01-19T16:16:21.8388464Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/j2objc/j2objc-annotations/2.8/j2objc-annotations-2.8.jar (9.3 kB at 57 kB/s)
2026-01-19T16:16:21.8388931Z Progress (3): 520/635 kB | 0.3/3.0 MB | 42/224 kB
2026-01-19T16:16:21.8389239Z                                                  
2026-01-19T16:16:21.8389631Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.96.Final/netty-buffer-4.1.96.Final.jar
2026-01-19T16:16:21.8390061Z Progress (3): 520/635 kB | 0.3/3.0 MB | 43/224 kB
2026-01-19T16:16:21.8390399Z Progress (3): 520/635 kB | 0.3/3.0 MB | 45/224 kB
2026-01-19T16:16:21.8390764Z Progress (3): 520/635 kB | 0.3/3.0 MB | 46/224 kB
2026-01-19T16:16:21.8447423Z Progress (3): 520/635 kB | 0.3/3.0 MB | 47/224 kB
2026-01-19T16:16:21.8448054Z Progress (3): 520/635 kB | 0.3/3.0 MB | 49/224 kB
2026-01-19T16:16:21.8448558Z Progress (3): 520/635 kB | 0.3/3.0 MB | 53/224 kB
2026-01-19T16:16:21.8449065Z Progress (3): 520/635 kB | 0.3/3.0 MB | 57/224 kB
2026-01-19T16:16:21.8453281Z Progress (3): 520/635 kB | 0.3/3.0 MB | 61/224 kB
2026-01-19T16:16:21.8453913Z Progress (3): 520/635 kB | 0.3/3.0 MB | 61/224 kB
2026-01-19T16:16:21.8454506Z Progress (3): 520/635 kB | 0.3/3.0 MB | 61/224 kB
2026-01-19T16:16:21.8454983Z Progress (3): 520/635 kB | 0.3/3.0 MB | 61/224 kB
2026-01-19T16:16:21.8455443Z Progress (4): 520/635 kB | 0.3/3.0 MB | 61/224 kB | 7.7/16 kB
2026-01-19T16:16:21.8455911Z Progress (4): 520/635 kB | 0.3/3.0 MB | 61/224 kB | 16/16 kB 
2026-01-19T16:16:21.8456368Z Progress (4): 520/635 kB | 0.3/3.0 MB | 61/224 kB | 16 kB   
2026-01-19T16:16:21.8457409Z                                                          
2026-01-19T16:16:21.8457980Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/errorprone/error_prone_annotations/2.18.0/error_prone_annotations-2.18.0.jar (16 kB at 95 kB/s)
2026-01-19T16:16:21.8458672Z Progress (3): 520/635 kB | 0.3/3.0 MB | 66/224 kB
2026-01-19T16:16:21.8487745Z Progress (3): 536/635 kB | 0.3/3.0 MB | 66/224 kB
2026-01-19T16:16:21.8488360Z Progress (3): 536/635 kB | 0.3/3.0 MB | 70/224 kB
2026-01-19T16:16:21.8489005Z Progress (3): 536/635 kB | 0.3/3.0 MB | 74/224 kB
2026-01-19T16:16:21.8489583Z Progress (3): 536/635 kB | 0.3/3.0 MB | 78/224 kB
2026-01-19T16:16:21.8490131Z Progress (3): 536/635 kB | 0.3/3.0 MB | 83/224 kB
2026-01-19T16:16:21.8490659Z Progress (3): 536/635 kB | 0.3/3.0 MB | 87/224 kB
2026-01-19T16:16:21.8490978Z                                                  
2026-01-19T16:16:21.8491372Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.96.Final/netty-codec-http-4.1.96.Final.jar
2026-01-19T16:16:21.8491805Z Progress (3): 552/635 kB | 0.3/3.0 MB | 87/224 kB
2026-01-19T16:16:21.8492131Z Progress (3): 569/635 kB | 0.3/3.0 MB | 87/224 kB
2026-01-19T16:16:21.8492493Z Progress (3): 585/635 kB | 0.3/3.0 MB | 87/224 kB
2026-01-19T16:16:21.8492840Z Progress (3): 585/635 kB | 0.4/3.0 MB | 87/224 kB
2026-01-19T16:16:21.8493168Z Progress (3): 585/635 kB | 0.4/3.0 MB | 91/224 kB
2026-01-19T16:16:21.8493504Z Progress (3): 585/635 kB | 0.4/3.0 MB | 95/224 kB
2026-01-19T16:16:21.8493856Z Progress (3): 585/635 kB | 0.4/3.0 MB | 100/224 kB
2026-01-19T16:16:21.8527236Z Progress (3): 585/635 kB | 0.4/3.0 MB | 100/224 kB
2026-01-19T16:16:21.8528203Z Progress (3): 585/635 kB | 0.4/3.0 MB | 104/224 kB
2026-01-19T16:16:21.8528562Z Progress (3): 585/635 kB | 0.4/3.0 MB | 108/224 kB
2026-01-19T16:16:21.8528891Z Progress (3): 585/635 kB | 0.4/3.0 MB | 112/224 kB
2026-01-19T16:16:21.8529218Z Progress (3): 585/635 kB | 0.4/3.0 MB | 116/224 kB
2026-01-19T16:16:21.8529531Z Progress (3): 585/635 kB | 0.4/3.0 MB | 121/224 kB
2026-01-19T16:16:21.8529849Z Progress (3): 585/635 kB | 0.4/3.0 MB | 125/224 kB
2026-01-19T16:16:21.8530160Z Progress (3): 585/635 kB | 0.4/3.0 MB | 129/224 kB
2026-01-19T16:16:21.8530631Z Progress (3): 585/635 kB | 0.4/3.0 MB | 133/224 kB
2026-01-19T16:16:21.8530948Z Progress (3): 585/635 kB | 0.4/3.0 MB | 138/224 kB
2026-01-19T16:16:21.8533450Z Progress (3): 585/635 kB | 0.4/3.0 MB | 142/224 kB
2026-01-19T16:16:21.8535499Z Progress (3): 585/635 kB | 0.4/3.0 MB | 142/224 kB
2026-01-19T16:16:21.8536114Z Progress (3): 602/635 kB | 0.4/3.0 MB | 142/224 kB
2026-01-19T16:16:21.8536801Z Progress (3): 602/635 kB | 0.4/3.0 MB | 142/224 kB
2026-01-19T16:16:21.8540774Z Progress (3): 602/635 kB | 0.4/3.0 MB | 142/224 kB
2026-01-19T16:16:21.8546251Z Progress (3): 602/635 kB | 0.4/3.0 MB | 142/224 kB
2026-01-19T16:16:21.8593404Z Progress (3): 602/635 kB | 0.5/3.0 MB | 142/224 kB
2026-01-19T16:16:21.8594078Z Progress (3): 618/635 kB | 0.5/3.0 MB | 142/224 kB
2026-01-19T16:16:21.8594660Z Progress (3): 634/635 kB | 0.5/3.0 MB | 142/224 kB
2026-01-19T16:16:21.8595255Z Progress (3): 635 kB | 0.5/3.0 MB | 142/224 kB    
2026-01-19T16:16:21.8595909Z Progress (3): 635 kB | 0.5/3.0 MB | 146/224 kB
2026-01-19T16:16:21.8596673Z Progress (3): 635 kB | 0.5/3.0 MB | 150/224 kB
2026-01-19T16:16:21.8597274Z Progress (3): 635 kB | 0.5/3.0 MB | 150/224 kB
2026-01-19T16:16:21.8597846Z Progress (3): 635 kB | 0.5/3.0 MB | 155/224 kB
2026-01-19T16:16:21.8598414Z Progress (3): 635 kB | 0.5/3.0 MB | 159/224 kB
2026-01-19T16:16:21.8598985Z Progress (3): 635 kB | 0.5/3.0 MB | 163/224 kB
2026-01-19T16:16:21.8599561Z Progress (3): 635 kB | 0.5/3.0 MB | 167/224 kB
2026-01-19T16:16:21.8600135Z Progress (3): 635 kB | 0.5/3.0 MB | 171/224 kB
2026-01-19T16:16:21.8601305Z Progress (3): 635 kB | 0.5/3.0 MB | 171/224 kB
2026-01-19T16:16:21.8601881Z Progress (3): 635 kB | 0.5/3.0 MB | 176/224 kB
2026-01-19T16:16:21.8602458Z Progress (3): 635 kB | 0.5/3.0 MB | 180/224 kB
2026-01-19T16:16:21.8603024Z Progress (3): 635 kB | 0.5/3.0 MB | 184/224 kB
2026-01-19T16:16:21.8603612Z Progress (3): 635 kB | 0.5/3.0 MB | 188/224 kB
2026-01-19T16:16:21.8604292Z Progress (3): 635 kB | 0.5/3.0 MB | 188/224 kB
2026-01-19T16:16:21.8637470Z Progress (3): 635 kB | 0.5/3.0 MB | 193/224 kB
2026-01-19T16:16:21.8638205Z Progress (3): 635 kB | 0.5/3.0 MB | 193/224 kB
2026-01-19T16:16:21.8647298Z                                               
2026-01-19T16:16:21.8647714Z Downloaded from central: https://repo.maven.apache.org/maven2/io/appium/java-client/8.6.0/java-client-8.6.0.jar (635 kB at 3.3 MB/s)
2026-01-19T16:16:21.8648257Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.96.Final/netty-codec-4.1.96.Final.jar
2026-01-19T16:16:21.8683911Z Progress (3): 0.5/3.0 MB | 193/224 kB | 7.7/657 kB
2026-01-19T16:16:21.8687927Z Progress (3): 0.5/3.0 MB | 193/224 kB | 16/657 kB 
2026-01-19T16:16:21.8689498Z Progress (3): 0.5/3.0 MB | 193/224 kB | 25/657 kB
2026-01-19T16:16:21.8697114Z Progress (4): 0.5/3.0 MB | 193/224 kB | 25/657 kB | 7.7/306 kB
2026-01-19T16:16:21.8697850Z Progress (4): 0.5/3.0 MB | 193/224 kB | 25/657 kB | 12/306 kB 
2026-01-19T16:16:21.8698600Z Progress (4): 0.5/3.0 MB | 193/224 kB | 25/657 kB | 29/306 kB
2026-01-19T16:16:21.8699390Z Progress (4): 0.5/3.0 MB | 193/224 kB | 25/657 kB | 45/306 kB
2026-01-19T16:16:21.8703720Z Progress (4): 0.5/3.0 MB | 193/224 kB | 25/657 kB | 45/306 kB
2026-01-19T16:16:21.8704302Z Progress (4): 0.5/3.0 MB | 197/224 kB | 25/657 kB | 45/306 kB
2026-01-19T16:16:21.8704840Z Progress (4): 0.5/3.0 MB | 201/224 kB | 25/657 kB | 45/306 kB
2026-01-19T16:16:21.8705532Z Progress (4): 0.5/3.0 MB | 205/224 kB | 25/657 kB | 45/306 kB
2026-01-19T16:16:21.8706232Z Progress (4): 0.5/3.0 MB | 210/224 kB | 25/657 kB | 45/306 kB
2026-01-19T16:16:21.8707120Z Progress (4): 0.5/3.0 MB | 214/224 kB | 25/657 kB | 45/306 kB
2026-01-19T16:16:21.8707642Z Progress (4): 0.5/3.0 MB | 218/224 kB | 25/657 kB | 45/306 kB
2026-01-19T16:16:21.8708988Z Progress (4): 0.5/3.0 MB | 224 kB | 25/657 kB | 45/306 kB    
2026-01-19T16:16:21.8709694Z                                                          
2026-01-19T16:16:21.8710297Z Downloaded from central: https://repo.maven.apache.org/maven2/org/checkerframework/checker-qual/3.33.0/checker-qual-3.33.0.jar (224 kB at 1.1 MB/s)
2026-01-19T16:16:21.8728048Z Progress (3): 0.6/3.0 MB | 25/657 kB | 45/306 kB
2026-01-19T16:16:21.8728617Z Progress (3): 0.6/3.0 MB | 25/657 kB | 61/306 kB
2026-01-19T16:16:21.8758957Z Progress (3): 0.6/3.0 MB | 25/657 kB | 78/306 kB
2026-01-19T16:16:21.8763669Z Progress (3): 0.6/3.0 MB | 41/657 kB | 78/306 kB
2026-01-19T16:16:21.8767539Z Progress (3): 0.6/3.0 MB | 57/657 kB | 78/306 kB
2026-01-19T16:16:21.8772402Z Progress (3): 0.6/3.0 MB | 74/657 kB | 78/306 kB
2026-01-19T16:16:21.8776715Z Progress (3): 0.6/3.0 MB | 90/657 kB | 78/306 kB
2026-01-19T16:16:21.8783156Z Progress (3): 0.6/3.0 MB | 90/657 kB | 78/306 kB
2026-01-19T16:16:21.8783924Z Progress (3): 0.6/3.0 MB | 90/657 kB | 94/306 kB
2026-01-19T16:16:21.8785533Z                                                 
2026-01-19T16:16:21.8786032Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.96.Final/netty-handler-4.1.96.Final.jar
2026-01-19T16:16:21.8786783Z Progress (3): 0.6/3.0 MB | 90/657 kB | 94/306 kB
2026-01-19T16:16:21.8787337Z Progress (3): 0.6/3.0 MB | 90/657 kB | 94/306 kB
2026-01-19T16:16:21.8789938Z Progress (3): 0.6/3.0 MB | 90/657 kB | 111/306 kB
2026-01-19T16:16:21.8790474Z Progress (3): 0.6/3.0 MB | 90/657 kB | 127/306 kB
2026-01-19T16:16:21.8790980Z Progress (3): 0.6/3.0 MB | 106/657 kB | 127/306 kB
2026-01-19T16:16:21.8829806Z Progress (3): 0.6/3.0 MB | 123/657 kB | 127/306 kB
2026-01-19T16:16:21.8830447Z Progress (3): 0.6/3.0 MB | 123/657 kB | 143/306 kB
2026-01-19T16:16:21.8830947Z Progress (3): 0.6/3.0 MB | 123/657 kB | 143/306 kB
2026-01-19T16:16:21.8831448Z Progress (3): 0.6/3.0 MB | 123/657 kB | 143/306 kB
2026-01-19T16:16:21.8833804Z Progress (3): 0.7/3.0 MB | 123/657 kB | 143/306 kB
2026-01-19T16:16:21.8834230Z Progress (3): 0.7/3.0 MB | 131/657 kB | 143/306 kB
2026-01-19T16:16:21.8849739Z Progress (3): 0.7/3.0 MB | 147/657 kB | 143/306 kB
2026-01-19T16:16:21.8854620Z Progress (3): 0.7/3.0 MB | 147/657 kB | 160/306 kB
2026-01-19T16:16:21.8859862Z Progress (3): 0.7/3.0 MB | 147/657 kB | 176/306 kB
2026-01-19T16:16:21.8877187Z Progress (3): 0.7/3.0 MB | 147/657 kB | 193/306 kB
2026-01-19T16:16:21.8880367Z Progress (3): 0.7/3.0 MB | 164/657 kB | 193/306 kB
2026-01-19T16:16:21.8880717Z Progress (3): 0.7/3.0 MB | 180/657 kB | 193/306 kB
2026-01-19T16:16:21.8881093Z Progress (3): 0.7/3.0 MB | 180/657 kB | 193/306 kB
2026-01-19T16:16:21.8885924Z Progress (3): 0.7/3.0 MB | 180/657 kB | 193/306 kB
2026-01-19T16:16:21.8886301Z Progress (3): 0.7/3.0 MB | 197/657 kB | 193/306 kB
2026-01-19T16:16:21.8928181Z Progress (3): 0.7/3.0 MB | 197/657 kB | 193/306 kB
2026-01-19T16:16:21.8934127Z Progress (3): 0.7/3.0 MB | 197/657 kB | 209/306 kB
2026-01-19T16:16:21.8935991Z Progress (3): 0.7/3.0 MB | 197/657 kB | 225/306 kB
2026-01-19T16:16:21.8937906Z Progress (3): 0.7/3.0 MB | 197/657 kB | 242/306 kB
2026-01-19T16:16:21.8939668Z Progress (3): 0.7/3.0 MB | 197/657 kB | 258/306 kB
2026-01-19T16:16:21.8941471Z Progress (3): 0.7/3.0 MB | 197/657 kB | 258/306 kB
2026-01-19T16:16:21.8943376Z Progress (4): 0.7/3.0 MB | 197/657 kB | 258/306 kB | 7.7/345 kB
2026-01-19T16:16:21.8944990Z Progress (4): 0.7/3.0 MB | 197/657 kB | 258/306 kB | 16/345 kB 
2026-01-19T16:16:21.8959353Z Progress (4): 0.7/3.0 MB | 197/657 kB | 258/306 kB | 29/345 kB
2026-01-19T16:16:21.8959987Z Progress (4): 0.7/3.0 MB | 213/657 kB | 258/306 kB | 29/345 kB
2026-01-19T16:16:21.8960751Z Progress (4): 0.7/3.0 MB | 229/657 kB | 258/306 kB | 29/345 kB
2026-01-19T16:16:21.8967331Z Progress (4): 0.7/3.0 MB | 246/657 kB | 258/306 kB | 29/345 kB
2026-01-19T16:16:21.8967984Z Progress (4): 0.7/3.0 MB | 262/657 kB | 258/306 kB | 29/345 kB
2026-01-19T16:16:21.8988799Z Progress (4): 0.7/3.0 MB | 262/657 kB | 258/306 kB | 45/345 kB
2026-01-19T16:16:21.8989584Z Progress (5): 0.7/3.0 MB | 262/657 kB | 258/306 kB | 45/345 kB | 8.2/558 kB
2026-01-19T16:16:21.8993767Z Progress (5): 0.7/3.0 MB | 262/657 kB | 258/306 kB | 45/345 kB | 25/558 kB 
2026-01-19T16:16:21.8994379Z Progress (5): 0.7/3.0 MB | 262/657 kB | 258/306 kB | 45/345 kB | 33/558 kB
2026-01-19T16:16:21.9009139Z Progress (5): 0.7/3.0 MB | 262/657 kB | 258/306 kB | 45/345 kB | 49/558 kB
2026-01-19T16:16:21.9009778Z Progress (5): 0.7/3.0 MB | 262/657 kB | 258/306 kB | 45/345 kB | 49/558 kB
2026-01-19T16:16:21.9010400Z Progress (5): 0.7/3.0 MB | 262/657 kB | 258/306 kB | 45/345 kB | 49/558 kB
2026-01-19T16:16:21.9027688Z Progress (5): 0.8/3.0 MB | 262/657 kB | 258/306 kB | 45/345 kB | 49/558 kB
2026-01-19T16:16:21.9037920Z Progress (5): 0.8/3.0 MB | 262/657 kB | 274/306 kB | 45/345 kB | 49/558 kB
2026-01-19T16:16:21.9038606Z Progress (5): 0.8/3.0 MB | 262/657 kB | 291/306 kB | 45/345 kB | 49/558 kB
2026-01-19T16:16:21.9049239Z Progress (5): 0.8/3.0 MB | 262/657 kB | 306 kB | 45/345 kB | 49/558 kB    
2026-01-19T16:16:21.9050004Z Progress (5): 0.8/3.0 MB | 262/657 kB | 306 kB | 61/345 kB | 49/558 kB
2026-01-19T16:16:21.9050572Z Progress (5): 0.8/3.0 MB | 262/657 kB | 306 kB | 78/345 kB | 49/558 kB
2026-01-19T16:16:21.9067784Z Progress (5): 0.8/3.0 MB | 262/657 kB | 306 kB | 94/345 kB | 49/558 kB
2026-01-19T16:16:21.9073974Z Progress (5): 0.8/3.0 MB | 279/657 kB | 306 kB | 94/345 kB | 49/558 kB
2026-01-19T16:16:21.9078521Z Progress (5): 0.8/3.0 MB | 295/657 kB | 306 kB | 94/345 kB | 49/558 kB
2026-01-19T16:16:21.9100281Z Progress (5): 0.8/3.0 MB | 295/657 kB | 306 kB | 94/345 kB | 49/558 kB
2026-01-19T16:16:21.9100705Z Progress (5): 0.8/3.0 MB | 295/657 kB | 306 kB | 94/345 kB | 49/558 kB
2026-01-19T16:16:21.9101073Z Progress (5): 0.8/3.0 MB | 311/657 kB | 306 kB | 94/345 kB | 49/558 kB
2026-01-19T16:16:21.9101446Z Progress (5): 0.8/3.0 MB | 311/657 kB | 306 kB | 111/345 kB | 49/558 kB
2026-01-19T16:16:21.9104391Z Progress (5): 0.8/3.0 MB | 311/657 kB | 306 kB | 127/345 kB | 49/558 kB
2026-01-19T16:16:21.9105407Z                                                                        
2026-01-19T16:16:21.9105817Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-buffer/4.1.96.Final/netty-buffer-4.1.96.Final.jar (306 kB at 1.3 MB/s)
2026-01-19T16:16:21.9106344Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.96.Final/netty-common-4.1.96.Final.jar
2026-01-19T16:16:21.9117300Z Progress (4): 0.8/3.0 MB | 311/657 kB | 127/345 kB | 49/558 kB
2026-01-19T16:16:21.9138220Z Progress (4): 0.8/3.0 MB | 328/657 kB | 127/345 kB | 49/558 kB
2026-01-19T16:16:21.9157966Z Progress (4): 0.8/3.0 MB | 328/657 kB | 127/345 kB | 66/558 kB
2026-01-19T16:16:21.9158567Z Progress (4): 0.8/3.0 MB | 328/657 kB | 127/345 kB | 82/558 kB
2026-01-19T16:16:21.9159128Z Progress (4): 0.8/3.0 MB | 328/657 kB | 127/345 kB | 98/558 kB
2026-01-19T16:16:21.9159696Z Progress (4): 0.8/3.0 MB | 328/657 kB | 127/345 kB | 98/558 kB
2026-01-19T16:16:21.9160258Z Progress (4): 0.8/3.0 MB | 328/657 kB | 143/345 kB | 98/558 kB
2026-01-19T16:16:21.9165075Z Progress (4): 0.8/3.0 MB | 328/657 kB | 160/345 kB | 98/558 kB
2026-01-19T16:16:21.9171247Z Progress (4): 0.8/3.0 MB | 344/657 kB | 160/345 kB | 98/558 kB
2026-01-19T16:16:21.9176771Z Progress (4): 0.8/3.0 MB | 360/657 kB | 160/345 kB | 98/558 kB
2026-01-19T16:16:21.9182938Z Progress (4): 0.8/3.0 MB | 360/657 kB | 160/345 kB | 98/558 kB
2026-01-19T16:16:21.9207791Z Progress (4): 0.8/3.0 MB | 360/657 kB | 176/345 kB | 98/558 kB
2026-01-19T16:16:21.9208453Z Progress (4): 0.9/3.0 MB | 360/657 kB | 176/345 kB | 98/558 kB
2026-01-19T16:16:21.9211849Z Progress (4): 0.9/3.0 MB | 377/657 kB | 176/345 kB | 98/558 kB
2026-01-19T16:16:21.9228687Z Progress (4): 0.9/3.0 MB | 377/657 kB | 193/345 kB | 98/558 kB
2026-01-19T16:16:21.9229877Z Progress (4): 0.9/3.0 MB | 377/657 kB | 193/345 kB | 115/558 kB
2026-01-19T16:16:21.9230512Z Progress (4): 0.9/3.0 MB | 377/657 kB | 193/345 kB | 131/558 kB
2026-01-19T16:16:21.9231037Z Progress (4): 0.9/3.0 MB | 377/657 kB | 193/345 kB | 135/558 kB
2026-01-19T16:16:21.9231609Z Progress (4): 0.9/3.0 MB | 377/657 kB | 193/345 kB | 151/558 kB
2026-01-19T16:16:21.9236298Z Progress (4): 0.9/3.0 MB | 377/657 kB | 193/345 kB | 151/558 kB
2026-01-19T16:16:21.9242289Z Progress (4): 0.9/3.0 MB | 377/657 kB | 209/345 kB | 151/558 kB
2026-01-19T16:16:21.9248966Z Progress (4): 0.9/3.0 MB | 393/657 kB | 209/345 kB | 151/558 kB
2026-01-19T16:16:21.9254289Z Progress (4): 0.9/3.0 MB | 410/657 kB | 209/345 kB | 151/558 kB
2026-01-19T16:16:21.9257762Z Progress (4): 0.9/3.0 MB | 410/657 kB | 225/345 kB | 151/558 kB
2026-01-19T16:16:21.9263670Z Progress (4): 0.9/3.0 MB | 410/657 kB | 225/345 kB | 164/558 kB
2026-01-19T16:16:21.9269976Z Progress (4): 0.9/3.0 MB | 426/657 kB | 225/345 kB | 164/558 kB
2026-01-19T16:16:21.9276170Z Progress (4): 0.9/3.0 MB | 426/657 kB | 225/345 kB | 180/558 kB
2026-01-19T16:16:21.9298278Z Progress (4): 0.9/3.0 MB | 426/657 kB | 242/345 kB | 180/558 kB
2026-01-19T16:16:21.9299834Z Progress (4): 0.9/3.0 MB | 426/657 kB | 242/345 kB | 180/558 kB
2026-01-19T16:16:21.9300379Z Progress (4): 0.9/3.0 MB | 426/657 kB | 242/345 kB | 180/558 kB
2026-01-19T16:16:21.9300878Z Progress (4): 0.9/3.0 MB | 426/657 kB | 242/345 kB | 180/558 kB
2026-01-19T16:16:21.9328006Z Progress (4): 0.9/3.0 MB | 426/657 kB | 242/345 kB | 180/558 kB
2026-01-19T16:16:21.9331992Z Progress (4): 0.9/3.0 MB | 426/657 kB | 258/345 kB | 180/558 kB
2026-01-19T16:16:21.9332607Z Progress (4): 0.9/3.0 MB | 426/657 kB | 258/345 kB | 197/558 kB
2026-01-19T16:16:21.9338874Z Progress (4): 0.9/3.0 MB | 426/657 kB | 258/345 kB | 213/558 kB
2026-01-19T16:16:21.9339494Z Progress (4): 0.9/3.0 MB | 442/657 kB | 258/345 kB | 213/558 kB
2026-01-19T16:16:21.9345841Z Progress (4): 0.9/3.0 MB | 459/657 kB | 258/345 kB | 213/558 kB
2026-01-19T16:16:21.9354744Z Progress (4): 0.9/3.0 MB | 459/657 kB | 274/345 kB | 213/558 kB
2026-01-19T16:16:21.9377715Z Progress (4): 0.9/3.0 MB | 459/657 kB | 291/345 kB | 213/558 kB
2026-01-19T16:16:21.9378426Z Progress (4): 0.9/3.0 MB | 459/657 kB | 291/345 kB | 229/558 kB
2026-01-19T16:16:21.9388268Z Progress (4): 0.9/3.0 MB | 459/657 kB | 291/345 kB | 246/558 kB
2026-01-19T16:16:21.9392690Z Progress (4): 1.0/3.0 MB | 459/657 kB | 291/345 kB | 246/558 kB
2026-01-19T16:16:21.9397343Z Progress (4): 1.0/3.0 MB | 459/657 kB | 291/345 kB | 246/558 kB
2026-01-19T16:16:21.9397993Z Progress (4): 1.0/3.0 MB | 459/657 kB | 291/345 kB | 246/558 kB
2026-01-19T16:16:21.9401009Z Progress (4): 1.0/3.0 MB | 459/657 kB | 307/345 kB | 246/558 kB
2026-01-19T16:16:21.9437733Z Progress (4): 1.0/3.0 MB | 459/657 kB | 307/345 kB | 262/558 kB
2026-01-19T16:16:21.9438447Z Progress (5): 1.0/3.0 MB | 459/657 kB | 307/345 kB | 262/558 kB | 7.7/660 kB
2026-01-19T16:16:21.9439081Z Progress (5): 1.0/3.0 MB | 459/657 kB | 307/345 kB | 262/558 kB | 16/660 kB 
2026-01-19T16:16:21.9439622Z Progress (5): 1.0/3.0 MB | 459/657 kB | 307/345 kB | 262/558 kB | 32/660 kB
2026-01-19T16:16:21.9440131Z Progress (5): 1.0/3.0 MB | 459/657 kB | 307/345 kB | 262/558 kB | 49/660 kB
2026-01-19T16:16:21.9448707Z Progress (5): 1.0/3.0 MB | 459/657 kB | 307/345 kB | 279/558 kB | 49/660 kB
2026-01-19T16:16:21.9449920Z Progress (5): 1.0/3.0 MB | 475/657 kB | 307/345 kB | 279/558 kB | 49/660 kB
2026-01-19T16:16:21.9450550Z Progress (5): 1.0/3.0 MB | 492/657 kB | 307/345 kB | 279/558 kB | 49/660 kB
2026-01-19T16:16:21.9451219Z Progress (5): 1.0/3.0 MB | 508/657 kB | 307/345 kB | 279/558 kB | 49/660 kB
2026-01-19T16:16:21.9457147Z Progress (5): 1.0/3.0 MB | 524/657 kB | 307/345 kB | 279/558 kB | 49/660 kB
2026-01-19T16:16:21.9478764Z Progress (5): 1.0/3.0 MB | 524/657 kB | 324/345 kB | 279/558 kB | 49/660 kB
2026-01-19T16:16:21.9480131Z Progress (5): 1.0/3.0 MB | 524/657 kB | 340/345 kB | 279/558 kB | 49/660 kB
2026-01-19T16:16:21.9480922Z Progress (5): 1.0/3.0 MB | 524/657 kB | 340/345 kB | 279/558 kB | 49/660 kB
2026-01-19T16:16:21.9482044Z Progress (5): 1.0/3.0 MB | 524/657 kB | 340/345 kB | 279/558 kB | 49/660 kB
2026-01-19T16:16:21.9482622Z Progress (5): 1.0/3.0 MB | 524/657 kB | 340/345 kB | 279/558 kB | 49/660 kB
2026-01-19T16:16:21.9488396Z Progress (5): 1.0/3.0 MB | 524/657 kB | 345 kB | 279/558 kB | 49/660 kB    
2026-01-19T16:16:21.9494243Z Progress (5): 1.0/3.0 MB | 524/657 kB | 345 kB | 295/558 kB | 49/660 kB
2026-01-19T16:16:21.9519900Z Progress (5): 1.0/3.0 MB | 524/657 kB | 345 kB | 311/558 kB | 49/660 kB
2026-01-19T16:16:21.9522548Z Progress (5): 1.0/3.0 MB | 524/657 kB | 345 kB | 311/558 kB | 65/660 kB
2026-01-19T16:16:21.9523091Z Progress (5): 1.0/3.0 MB | 524/657 kB | 345 kB | 311/558 kB | 81/660 kB
2026-01-19T16:16:21.9526158Z Progress (5): 1.0/3.0 MB | 524/657 kB | 345 kB | 311/558 kB | 98/660 kB
2026-01-19T16:16:21.9526819Z Progress (5): 1.0/3.0 MB | 524/657 kB | 345 kB | 311/558 kB | 114/660 kB
2026-01-19T16:16:21.9549685Z Progress (5): 1.0/3.0 MB | 524/657 kB | 345 kB | 328/558 kB | 114/660 kB
2026-01-19T16:16:21.9550701Z Progress (5): 1.0/3.0 MB | 541/657 kB | 345 kB | 328/558 kB | 114/660 kB
2026-01-19T16:16:21.9551376Z Progress (5): 1.0/3.0 MB | 557/657 kB | 345 kB | 328/558 kB | 114/660 kB
2026-01-19T16:16:21.9552055Z Progress (5): 1.0/3.0 MB | 573/657 kB | 345 kB | 328/558 kB | 114/660 kB
2026-01-19T16:16:21.9556421Z Progress (5): 1.0/3.0 MB | 590/657 kB | 345 kB | 328/558 kB | 114/660 kB
2026-01-19T16:16:21.9557575Z                                                                         
2026-01-19T16:16:21.9557971Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec/4.1.96.Final/netty-codec-4.1.96.Final.jar (345 kB at 1.2 MB/s)
2026-01-19T16:16:21.9558506Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.96.Final/netty-transport-classes-epoll-4.1.96.Final.jar
2026-01-19T16:16:21.9578962Z Progress (4): 1.1/3.0 MB | 590/657 kB | 328/558 kB | 114/660 kB
2026-01-19T16:16:21.9579618Z Progress (4): 1.1/3.0 MB | 590/657 kB | 328/558 kB | 114/660 kB
2026-01-19T16:16:21.9607840Z Progress (4): 1.1/3.0 MB | 590/657 kB | 328/558 kB | 114/660 kB
2026-01-19T16:16:21.9615263Z Progress (4): 1.1/3.0 MB | 590/657 kB | 344/558 kB | 114/660 kB
2026-01-19T16:16:21.9615912Z Progress (4): 1.1/3.0 MB | 590/657 kB | 344/558 kB | 131/660 kB
2026-01-19T16:16:21.9617850Z Progress (4): 1.1/3.0 MB | 590/657 kB | 360/558 kB | 131/660 kB
2026-01-19T16:16:21.9618384Z Progress (4): 1.1/3.0 MB | 590/657 kB | 360/558 kB | 147/660 kB
2026-01-19T16:16:21.9619995Z Progress (4): 1.1/3.0 MB | 590/657 kB | 377/558 kB | 147/660 kB
2026-01-19T16:16:21.9620447Z Progress (4): 1.1/3.0 MB | 590/657 kB | 377/558 kB | 163/660 kB
2026-01-19T16:16:21.9621010Z Progress (4): 1.1/3.0 MB | 606/657 kB | 377/558 kB | 163/660 kB
2026-01-19T16:16:21.9623395Z Progress (4): 1.1/3.0 MB | 623/657 kB | 377/558 kB | 163/660 kB
2026-01-19T16:16:21.9623859Z Progress (4): 1.1/3.0 MB | 623/657 kB | 377/558 kB | 163/660 kB
2026-01-19T16:16:21.9624311Z Progress (4): 1.1/3.0 MB | 623/657 kB | 377/558 kB | 163/660 kB
2026-01-19T16:16:21.9628735Z Progress (4): 1.1/3.0 MB | 623/657 kB | 393/558 kB | 163/660 kB
2026-01-19T16:16:21.9634864Z Progress (4): 1.1/3.0 MB | 639/657 kB | 393/558 kB | 163/660 kB
2026-01-19T16:16:21.9640873Z Progress (4): 1.1/3.0 MB | 639/657 kB | 393/558 kB | 163/660 kB
2026-01-19T16:16:21.9677982Z Progress (4): 1.1/3.0 MB | 639/657 kB | 410/558 kB | 163/660 kB
2026-01-19T16:16:21.9679336Z Progress (4): 1.1/3.0 MB | 655/657 kB | 410/558 kB | 163/660 kB
2026-01-19T16:16:21.9679687Z Progress (4): 1.2/3.0 MB | 655/657 kB | 410/558 kB | 163/660 kB
2026-01-19T16:16:21.9680021Z Progress (4): 1.2/3.0 MB | 655/657 kB | 426/558 kB | 163/660 kB
2026-01-19T16:16:21.9680346Z Progress (4): 1.2/3.0 MB | 655/657 kB | 442/558 kB | 163/660 kB
2026-01-19T16:16:21.9681005Z Progress (4): 1.2/3.0 MB | 655/657 kB | 442/558 kB | 180/660 kB
2026-01-19T16:16:21.9681327Z Progress (4): 1.2/3.0 MB | 657 kB | 442/558 kB | 180/660 kB    
2026-01-19T16:16:21.9681617Z                                                            
2026-01-19T16:16:21.9682009Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-http/4.1.96.Final/netty-codec-http-4.1.96.Final.jar (657 kB at 2.2 MB/s)
2026-01-19T16:16:21.9682564Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.96.Final/netty-transport-classes-kqueue-4.1.96.Final.jar
2026-01-19T16:16:21.9685064Z Progress (3): 1.2/3.0 MB | 442/558 kB | 196/660 kB
2026-01-19T16:16:21.9691465Z Progress (3): 1.2/3.0 MB | 442/558 kB | 196/660 kB
2026-01-19T16:16:21.9694159Z Progress (3): 1.2/3.0 MB | 442/558 kB | 213/660 kB
2026-01-19T16:16:21.9701293Z Progress (3): 1.2/3.0 MB | 459/558 kB | 213/660 kB
2026-01-19T16:16:21.9702667Z Progress (3): 1.2/3.0 MB | 475/558 kB | 213/660 kB
2026-01-19T16:16:21.9747764Z Progress (3): 1.2/3.0 MB | 475/558 kB | 213/660 kB
2026-01-19T16:16:21.9748623Z Progress (3): 1.2/3.0 MB | 475/558 kB | 213/660 kB
2026-01-19T16:16:21.9749175Z Progress (3): 1.2/3.0 MB | 475/558 kB | 229/660 kB
2026-01-19T16:16:21.9749732Z Progress (3): 1.2/3.0 MB | 475/558 kB | 245/660 kB
2026-01-19T16:16:21.9750782Z Progress (3): 1.2/3.0 MB | 492/558 kB | 245/660 kB
2026-01-19T16:16:21.9751276Z Progress (3): 1.2/3.0 MB | 492/558 kB | 262/660 kB
2026-01-19T16:16:21.9751766Z Progress (3): 1.2/3.0 MB | 492/558 kB | 262/660 kB
2026-01-19T16:16:21.9752328Z Progress (3): 1.2/3.0 MB | 492/558 kB | 278/660 kB
2026-01-19T16:16:21.9752914Z Progress (3): 1.2/3.0 MB | 508/558 kB | 278/660 kB
2026-01-19T16:16:21.9753407Z Progress (3): 1.2/3.0 MB | 524/558 kB | 278/660 kB
2026-01-19T16:16:21.9753883Z Progress (3): 1.2/3.0 MB | 524/558 kB | 278/660 kB
2026-01-19T16:16:21.9754358Z Progress (3): 1.3/3.0 MB | 524/558 kB | 278/660 kB
2026-01-19T16:16:21.9757225Z Progress (3): 1.3/3.0 MB | 541/558 kB | 278/660 kB
2026-01-19T16:16:21.9763730Z Progress (3): 1.3/3.0 MB | 541/558 kB | 278/660 kB
2026-01-19T16:16:21.9768993Z Progress (3): 1.3/3.0 MB | 557/558 kB | 278/660 kB
2026-01-19T16:16:21.9770223Z Progress (3): 1.3/3.0 MB | 557/558 kB | 278/660 kB
2026-01-19T16:16:21.9775254Z Progress (3): 1.3/3.0 MB | 558 kB | 278/660 kB    
2026-01-19T16:16:21.9775562Z                                               
2026-01-19T16:16:21.9775951Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler/4.1.96.Final/netty-handler-4.1.96.Final.jar (558 kB at 1.9 MB/s)
2026-01-19T16:16:21.9782030Z Progress (2): 1.3/3.0 MB | 278/660 kB
2026-01-19T16:16:21.9782365Z                                      
2026-01-19T16:16:21.9782828Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final.jar
2026-01-19T16:16:21.9829880Z Progress (2): 1.3/3.0 MB | 294/660 kB
2026-01-19T16:16:21.9830215Z Progress (2): 1.3/3.0 MB | 311/660 kB
2026-01-19T16:16:21.9830570Z Progress (3): 1.3/3.0 MB | 311/660 kB | 7.7/147 kB
2026-01-19T16:16:21.9834841Z Progress (3): 1.3/3.0 MB | 311/660 kB | 16/147 kB 
2026-01-19T16:16:21.9835187Z Progress (3): 1.3/3.0 MB | 327/660 kB | 16/147 kB
2026-01-19T16:16:21.9835533Z Progress (3): 1.3/3.0 MB | 327/660 kB | 29/147 kB
2026-01-19T16:16:21.9835861Z Progress (3): 1.3/3.0 MB | 327/660 kB | 29/147 kB
2026-01-19T16:16:21.9836172Z Progress (3): 1.3/3.0 MB | 327/660 kB | 29/147 kB
2026-01-19T16:16:21.9836728Z Progress (3): 1.4/3.0 MB | 327/660 kB | 29/147 kB
2026-01-19T16:16:21.9843147Z Progress (3): 1.4/3.0 MB | 327/660 kB | 45/147 kB
2026-01-19T16:16:21.9843488Z Progress (3): 1.4/3.0 MB | 327/660 kB | 61/147 kB
2026-01-19T16:16:21.9847049Z Progress (3): 1.4/3.0 MB | 327/660 kB | 61/147 kB
2026-01-19T16:16:21.9858522Z Progress (3): 1.4/3.0 MB | 327/660 kB | 61/147 kB
2026-01-19T16:16:21.9859168Z Progress (3): 1.4/3.0 MB | 327/660 kB | 78/147 kB
2026-01-19T16:16:21.9859707Z Progress (3): 1.4/3.0 MB | 344/660 kB | 78/147 kB
2026-01-19T16:16:21.9865332Z Progress (3): 1.4/3.0 MB | 344/660 kB | 78/147 kB
2026-01-19T16:16:21.9871402Z Progress (3): 1.4/3.0 MB | 344/660 kB | 94/147 kB
2026-01-19T16:16:21.9877423Z Progress (3): 1.4/3.0 MB | 344/660 kB | 94/147 kB
2026-01-19T16:16:21.9911079Z Progress (3): 1.4/3.0 MB | 344/660 kB | 111/147 kB
2026-01-19T16:16:21.9911695Z Progress (3): 1.4/3.0 MB | 360/660 kB | 111/147 kB
2026-01-19T16:16:21.9912204Z Progress (3): 1.4/3.0 MB | 376/660 kB | 111/147 kB
2026-01-19T16:16:21.9912719Z Progress (3): 1.4/3.0 MB | 393/660 kB | 111/147 kB
2026-01-19T16:16:21.9948319Z Progress (3): 1.4/3.0 MB | 393/660 kB | 111/147 kB
2026-01-19T16:16:21.9948931Z Progress (3): 1.5/3.0 MB | 393/660 kB | 111/147 kB
2026-01-19T16:16:21.9950694Z Progress (4): 1.5/3.0 MB | 393/660 kB | 111/147 kB | 7.7/108 kB
2026-01-19T16:16:21.9952059Z Progress (4): 1.5/3.0 MB | 393/660 kB | 111/147 kB | 16/108 kB 
2026-01-19T16:16:21.9952776Z Progress (4): 1.5/3.0 MB | 393/660 kB | 111/147 kB | 32/108 kB
2026-01-19T16:16:21.9953497Z Progress (4): 1.5/3.0 MB | 393/660 kB | 127/147 kB | 32/108 kB
2026-01-19T16:16:21.9954091Z Progress (4): 1.5/3.0 MB | 393/660 kB | 143/147 kB | 32/108 kB
2026-01-19T16:16:21.9954805Z Progress (4): 1.5/3.0 MB | 409/660 kB | 143/147 kB | 32/108 kB
2026-01-19T16:16:21.9958029Z Progress (4): 1.5/3.0 MB | 409/660 kB | 147 kB | 32/108 kB    
2026-01-19T16:16:21.9958581Z Progress (4): 1.5/3.0 MB | 409/660 kB | 147 kB | 49/108 kB
2026-01-19T16:16:21.9959081Z Progress (4): 1.5/3.0 MB | 409/660 kB | 147 kB | 65/108 kB
2026-01-19T16:16:21.9959574Z Progress (4): 1.5/3.0 MB | 409/660 kB | 147 kB | 65/108 kB
2026-01-19T16:16:21.9960104Z Progress (4): 1.5/3.0 MB | 409/660 kB | 147 kB | 65/108 kB
2026-01-19T16:16:21.9960662Z                                                           
2026-01-19T16:16:21.9961514Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-epoll/4.1.96.Final/netty-transport-classes-epoll-4.1.96.Final.jar (147 kB at 463 kB/s)
2026-01-19T16:16:21.9962825Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final.jar
2026-01-19T16:16:21.9963472Z Progress (3): 1.5/3.0 MB | 426/660 kB | 65/108 kB
2026-01-19T16:16:21.9969009Z Progress (3): 1.5/3.0 MB | 426/660 kB | 65/108 kB
2026-01-19T16:16:21.9979607Z Progress (3): 1.5/3.0 MB | 426/660 kB | 81/108 kB
2026-01-19T16:16:21.9981059Z Progress (3): 1.5/3.0 MB | 426/660 kB | 81/108 kB
2026-01-19T16:16:21.9984459Z Progress (3): 1.5/3.0 MB | 442/660 kB | 81/108 kB
2026-01-19T16:16:21.9984809Z Progress (4): 1.5/3.0 MB | 442/660 kB | 81/108 kB | 5.7 kB
2026-01-19T16:16:21.9985097Z                                                           
2026-01-19T16:16:21.9985527Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.96.Final/netty-transport-native-epoll-4.1.96.Final.jar (5.7 kB at 18 kB/s)
2026-01-19T16:16:21.9992001Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.96.Final/netty-transport-native-unix-common-4.1.96.Final.jar
2026-01-19T16:16:22.0000117Z Progress (3): 1.5/3.0 MB | 442/660 kB | 81/108 kB
2026-01-19T16:16:22.0004526Z Progress (3): 1.5/3.0 MB | 442/660 kB | 98/108 kB
2026-01-19T16:16:22.0033847Z Progress (3): 1.5/3.0 MB | 442/660 kB | 108 kB   
2026-01-19T16:16:22.0034701Z Progress (3): 1.6/3.0 MB | 442/660 kB | 108 kB
2026-01-19T16:16:22.0035270Z Progress (3): 1.6/3.0 MB | 442/660 kB | 108 kB
2026-01-19T16:16:22.0035782Z Progress (3): 1.6/3.0 MB | 442/660 kB | 108 kB
2026-01-19T16:16:22.0036270Z Progress (3): 1.6/3.0 MB | 442/660 kB | 108 kB
2026-01-19T16:16:22.0037051Z Progress (3): 1.6/3.0 MB | 458/660 kB | 108 kB
2026-01-19T16:16:22.0037612Z                                               
2026-01-19T16:16:22.0038218Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-classes-kqueue/4.1.96.Final/netty-transport-classes-kqueue-4.1.96.Final.jar (108 kB at 332 kB/s)
2026-01-19T16:16:22.0069253Z Progress (2): 1.6/3.0 MB | 475/660 kB
2026-01-19T16:16:22.0069870Z                                      
2026-01-19T16:16:22.0070479Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.96.Final/netty-transport-4.1.96.Final.jar
2026-01-19T16:16:22.0117200Z Progress (2): 1.6/3.0 MB | 491/660 kB
2026-01-19T16:16:22.0117826Z Progress (2): 1.6/3.0 MB | 507/660 kB
2026-01-19T16:16:22.0118381Z Progress (2): 1.6/3.0 MB | 524/660 kB
2026-01-19T16:16:22.0118883Z Progress (2): 1.6/3.0 MB | 524/660 kB
2026-01-19T16:16:22.0119369Z Progress (2): 1.6/3.0 MB | 524/660 kB
2026-01-19T16:16:22.0130005Z Progress (2): 1.7/3.0 MB | 524/660 kB
2026-01-19T16:16:22.0137741Z Progress (2): 1.7/3.0 MB | 540/660 kB
2026-01-19T16:16:22.0167201Z Progress (2): 1.7/3.0 MB | 540/660 kB
2026-01-19T16:16:22.0167802Z Progress (2): 1.7/3.0 MB | 540/660 kB
2026-01-19T16:16:22.0190209Z Progress (2): 1.7/3.0 MB | 540/660 kB
2026-01-19T16:16:22.0191211Z Progress (2): 1.7/3.0 MB | 557/660 kB
2026-01-19T16:16:22.0191742Z Progress (3): 1.7/3.0 MB | 557/660 kB | 4.1/44 kB
2026-01-19T16:16:22.0192334Z Progress (3): 1.7/3.0 MB | 573/660 kB | 4.1/44 kB
2026-01-19T16:16:22.0192829Z Progress (3): 1.7/3.0 MB | 573/660 kB | 20/44 kB 
2026-01-19T16:16:22.0193374Z Progress (3): 1.7/3.0 MB | 589/660 kB | 20/44 kB
2026-01-19T16:16:22.0193868Z Progress (3): 1.7/3.0 MB | 589/660 kB | 37/44 kB
2026-01-19T16:16:22.0194356Z Progress (3): 1.7/3.0 MB | 589/660 kB | 44 kB   
2026-01-19T16:16:22.0194848Z Progress (3): 1.7/3.0 MB | 606/660 kB | 44 kB
2026-01-19T16:16:22.0227404Z Progress (3): 1.7/3.0 MB | 606/660 kB | 44 kB
2026-01-19T16:16:22.0228138Z Progress (3): 1.7/3.0 MB | 606/660 kB | 44 kB
2026-01-19T16:16:22.0228806Z Progress (3): 1.7/3.0 MB | 606/660 kB | 44 kB
2026-01-19T16:16:22.0229464Z Progress (4): 1.7/3.0 MB | 606/660 kB | 44 kB | 5.7 kB
2026-01-19T16:16:22.0229944Z                                                       
2026-01-19T16:16:22.0230563Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.96.Final/netty-transport-native-kqueue-4.1.96.Final.jar (5.7 kB at 16 kB/s)
2026-01-19T16:16:22.0231403Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.96.Final/netty-resolver-4.1.96.Final.jar
2026-01-19T16:16:22.0231995Z Progress (3): 1.8/3.0 MB | 606/660 kB | 44 kB
2026-01-19T16:16:22.0232513Z Progress (3): 1.8/3.0 MB | 622/660 kB | 44 kB
2026-01-19T16:16:22.0232992Z                                              
2026-01-19T16:16:22.0233630Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-unix-common/4.1.96.Final/netty-transport-native-unix-common-4.1.96.Final.jar (44 kB at 127 kB/s)
2026-01-19T16:16:22.0234381Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.28.0/opentelemetry-api-1.28.0.jar
2026-01-19T16:16:22.0275928Z Progress (2): 1.8/3.0 MB | 639/660 kB
2026-01-19T16:16:22.0300476Z Progress (2): 1.8/3.0 MB | 655/660 kB
2026-01-19T16:16:22.0301255Z Progress (2): 1.8/3.0 MB | 660 kB    
2026-01-19T16:16:22.0301838Z Progress (2): 1.8/3.0 MB | 660 kB
2026-01-19T16:16:22.0302346Z Progress (2): 1.8/3.0 MB | 660 kB
2026-01-19T16:16:22.0302843Z Progress (2): 1.8/3.0 MB | 660 kB
2026-01-19T16:16:22.0303310Z                                  
2026-01-19T16:16:22.0303916Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-common/4.1.96.Final/netty-common-4.1.96.Final.jar (660 kB at 1.9 MB/s)
2026-01-19T16:16:22.0304683Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.28.0/opentelemetry-context-1.28.0.jar
2026-01-19T16:16:22.0305410Z Progress (2): 1.8/3.0 MB | 7.7/490 kB
2026-01-19T16:16:22.0305944Z Progress (2): 1.8/3.0 MB | 16/490 kB 
2026-01-19T16:16:22.0306683Z Progress (2): 1.8/3.0 MB | 32/490 kB
2026-01-19T16:16:22.0357267Z Progress (2): 1.8/3.0 MB | 49/490 kB
2026-01-19T16:16:22.0357904Z Progress (2): 1.8/3.0 MB | 49/490 kB
2026-01-19T16:16:22.0358737Z Progress (2): 1.8/3.0 MB | 49/490 kB
2026-01-19T16:16:22.0359284Z Progress (2): 1.9/3.0 MB | 49/490 kB
2026-01-19T16:16:22.0359803Z Progress (2): 1.9/3.0 MB | 49/490 kB
2026-01-19T16:16:22.0360310Z Progress (2): 1.9/3.0 MB | 65/490 kB
2026-01-19T16:16:22.0360824Z Progress (2): 1.9/3.0 MB | 81/490 kB
2026-01-19T16:16:22.0369166Z Progress (2): 1.9/3.0 MB | 98/490 kB
2026-01-19T16:16:22.0379658Z Progress (2): 1.9/3.0 MB | 98/490 kB
2026-01-19T16:16:22.0389084Z Progress (2): 1.9/3.0 MB | 98/490 kB
2026-01-19T16:16:22.0417199Z Progress (2): 1.9/3.0 MB | 114/490 kB
2026-01-19T16:16:22.0421218Z Progress (2): 1.9/3.0 MB | 131/490 kB
2026-01-19T16:16:22.0422078Z Progress (2): 1.9/3.0 MB | 147/490 kB
2026-01-19T16:16:22.0467745Z Progress (2): 1.9/3.0 MB | 147/490 kB
2026-01-19T16:16:22.0471802Z Progress (3): 1.9/3.0 MB | 147/490 kB | 7.7/138 kB
2026-01-19T16:16:22.0472313Z Progress (3): 1.9/3.0 MB | 147/490 kB | 16/138 kB 
2026-01-19T16:16:22.0472835Z Progress (3): 1.9/3.0 MB | 147/490 kB | 16/138 kB
2026-01-19T16:16:22.0476009Z Progress (3): 1.9/3.0 MB | 147/490 kB | 32/138 kB
2026-01-19T16:16:22.0476718Z Progress (3): 2.0/3.0 MB | 147/490 kB | 32/138 kB
2026-01-19T16:16:22.0477297Z Progress (3): 2.0/3.0 MB | 147/490 kB | 48/138 kB
2026-01-19T16:16:22.0478786Z Progress (3): 2.0/3.0 MB | 163/490 kB | 48/138 kB
2026-01-19T16:16:22.0482591Z Progress (3): 2.0/3.0 MB | 180/490 kB | 48/138 kB
2026-01-19T16:16:22.0483045Z Progress (3): 2.0/3.0 MB | 196/490 kB | 48/138 kB
2026-01-19T16:16:22.0483551Z Progress (3): 2.0/3.0 MB | 196/490 kB | 48/138 kB
2026-01-19T16:16:22.0484968Z Progress (3): 2.0/3.0 MB | 196/490 kB | 65/138 kB
2026-01-19T16:16:22.0547442Z Progress (3): 2.0/3.0 MB | 196/490 kB | 65/138 kB
2026-01-19T16:16:22.0548144Z Progress (3): 2.0/3.0 MB | 196/490 kB | 81/138 kB
2026-01-19T16:16:22.0548714Z Progress (3): 2.0/3.0 MB | 196/490 kB | 98/138 kB
2026-01-19T16:16:22.0549299Z Progress (3): 2.0/3.0 MB | 196/490 kB | 98/138 kB
2026-01-19T16:16:22.0549837Z Progress (3): 2.0/3.0 MB | 196/490 kB | 114/138 kB
2026-01-19T16:16:22.0550392Z Progress (3): 2.0/3.0 MB | 196/490 kB | 114/138 kB
2026-01-19T16:16:22.0550955Z Progress (3): 2.0/3.0 MB | 196/490 kB | 114/138 kB
2026-01-19T16:16:22.0551562Z Progress (4): 2.0/3.0 MB | 196/490 kB | 114/138 kB | 7.7/38 kB
2026-01-19T16:16:22.0552196Z Progress (4): 2.0/3.0 MB | 196/490 kB | 114/138 kB | 16/38 kB 
2026-01-19T16:16:22.0552800Z Progress (4): 2.1/3.0 MB | 196/490 kB | 114/138 kB | 16/38 kB
2026-01-19T16:16:22.0553719Z Progress (4): 2.1/3.0 MB | 213/490 kB | 114/138 kB | 16/38 kB
2026-01-19T16:16:22.0554322Z Progress (4): 2.1/3.0 MB | 213/490 kB | 114/138 kB | 32/38 kB
2026-01-19T16:16:22.0554877Z Progress (4): 2.1/3.0 MB | 229/490 kB | 114/138 kB | 32/38 kB
2026-01-19T16:16:22.0555432Z Progress (4): 2.1/3.0 MB | 229/490 kB | 114/138 kB | 38 kB   
2026-01-19T16:16:22.0555979Z Progress (4): 2.1/3.0 MB | 245/490 kB | 114/138 kB | 38 kB
2026-01-19T16:16:22.0600314Z Progress (4): 2.1/3.0 MB | 262/490 kB | 114/138 kB | 38 kB
2026-01-19T16:16:22.0600763Z Progress (5): 2.1/3.0 MB | 262/490 kB | 114/138 kB | 38 kB | 7.7/47 kB
2026-01-19T16:16:22.0601153Z Progress (5): 2.1/3.0 MB | 262/490 kB | 114/138 kB | 38 kB | 16/47 kB 
2026-01-19T16:16:22.0601532Z Progress (5): 2.1/3.0 MB | 262/490 kB | 130/138 kB | 38 kB | 16/47 kB
2026-01-19T16:16:22.0601906Z Progress (5): 2.1/3.0 MB | 262/490 kB | 138 kB | 38 kB | 16/47 kB    
2026-01-19T16:16:22.0602265Z Progress (5): 2.1/3.0 MB | 262/490 kB | 138 kB | 38 kB | 16/47 kB
2026-01-19T16:16:22.0602580Z                                                                  
2026-01-19T16:16:22.0603009Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api/1.28.0/opentelemetry-api-1.28.0.jar (138 kB at 362 kB/s)
2026-01-19T16:16:22.0603605Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.28.0/opentelemetry-exporter-logging-1.28.0.jar
2026-01-19T16:16:22.0604087Z Progress (4): 2.1/3.0 MB | 262/490 kB | 38 kB | 32/47 kB
2026-01-19T16:16:22.0604583Z                                                         
2026-01-19T16:16:22.0605005Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-resolver/4.1.96.Final/netty-resolver-4.1.96.Final.jar (38 kB at 99 kB/s)
2026-01-19T16:16:22.0605577Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.28.0/opentelemetry-sdk-metrics-1.28.0.jar
2026-01-19T16:16:22.0606039Z Progress (3): 2.1/3.0 MB | 262/490 kB | 47 kB
2026-01-19T16:16:22.0606372Z Progress (3): 2.1/3.0 MB | 278/490 kB | 47 kB
2026-01-19T16:16:22.0612735Z Progress (3): 2.1/3.0 MB | 294/490 kB | 47 kB
2026-01-19T16:16:22.0613119Z Progress (3): 2.1/3.0 MB | 294/490 kB | 47 kB
2026-01-19T16:16:22.0613618Z Progress (3): 2.1/3.0 MB | 294/490 kB | 47 kB
2026-01-19T16:16:22.0616343Z Progress (3): 2.1/3.0 MB | 311/490 kB | 47 kB
2026-01-19T16:16:22.0616931Z                                              
2026-01-19T16:16:22.0618091Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-context/1.28.0/opentelemetry-context-1.28.0.jar (47 kB at 123 kB/s)
2026-01-19T16:16:22.0667608Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-extension-incubator/1.28.0-alpha/opentelemetry-extension-incubator-1.28.0-alpha.jar
2026-01-19T16:16:22.0668129Z Progress (2): 2.1/3.0 MB | 311/490 kB
2026-01-19T16:16:22.0668441Z Progress (2): 2.1/3.0 MB | 311/490 kB
2026-01-19T16:16:22.0671125Z Progress (2): 2.1/3.0 MB | 327/490 kB
2026-01-19T16:16:22.0671441Z Progress (2): 2.1/3.0 MB | 344/490 kB
2026-01-19T16:16:22.0671735Z Progress (2): 2.2/3.0 MB | 344/490 kB
2026-01-19T16:16:22.0672041Z Progress (2): 2.2/3.0 MB | 360/490 kB
2026-01-19T16:16:22.0672338Z Progress (2): 2.2/3.0 MB | 360/490 kB
2026-01-19T16:16:22.0672646Z Progress (2): 2.2/3.0 MB | 376/490 kB
2026-01-19T16:16:22.0673012Z Progress (2): 2.2/3.0 MB | 393/490 kB
2026-01-19T16:16:22.0677425Z Progress (2): 2.2/3.0 MB | 409/490 kB
2026-01-19T16:16:22.0681189Z Progress (2): 2.2/3.0 MB | 409/490 kB
2026-01-19T16:16:22.0692657Z Progress (2): 2.2/3.0 MB | 426/490 kB
2026-01-19T16:16:22.0693193Z Progress (2): 2.2/3.0 MB | 426/490 kB
2026-01-19T16:16:22.0693640Z Progress (2): 2.2/3.0 MB | 426/490 kB
2026-01-19T16:16:22.0694091Z Progress (2): 2.2/3.0 MB | 442/490 kB
2026-01-19T16:16:22.0699190Z Progress (2): 2.2/3.0 MB | 442/490 kB
2026-01-19T16:16:22.0705314Z Progress (2): 2.3/3.0 MB | 442/490 kB
2026-01-19T16:16:22.0709821Z Progress (2): 2.3/3.0 MB | 442/490 kB
2026-01-19T16:16:22.0715531Z Progress (2): 2.3/3.0 MB | 442/490 kB
2026-01-19T16:16:22.0719525Z Progress (2): 2.3/3.0 MB | 442/490 kB
2026-01-19T16:16:22.0722956Z Progress (2): 2.3/3.0 MB | 458/490 kB
2026-01-19T16:16:22.0726753Z Progress (2): 2.3/3.0 MB | 458/490 kB
2026-01-19T16:16:22.0731568Z Progress (2): 2.3/3.0 MB | 458/490 kB
2026-01-19T16:16:22.0738881Z Progress (2): 2.4/3.0 MB | 458/490 kB
2026-01-19T16:16:22.0742493Z Progress (2): 2.4/3.0 MB | 458/490 kB
2026-01-19T16:16:22.0767053Z Progress (2): 2.4/3.0 MB | 458/490 kB
2026-01-19T16:16:22.0779495Z Progress (2): 2.4/3.0 MB | 475/490 kB
2026-01-19T16:16:22.0787208Z Progress (2): 2.4/3.0 MB | 475/490 kB
2026-01-19T16:16:22.0787689Z Progress (2): 2.4/3.0 MB | 475/490 kB
2026-01-19T16:16:22.0788094Z Progress (2): 2.4/3.0 MB | 475/490 kB
2026-01-19T16:16:22.0788519Z Progress (2): 2.5/3.0 MB | 475/490 kB
2026-01-19T16:16:22.0788923Z Progress (2): 2.5/3.0 MB | 475/490 kB
2026-01-19T16:16:22.0789317Z Progress (2): 2.5/3.0 MB | 475/490 kB
2026-01-19T16:16:22.0831524Z Progress (2): 2.5/3.0 MB | 475/490 kB
2026-01-19T16:16:22.0832219Z Progress (2): 2.5/3.0 MB | 490 kB    
2026-01-19T16:16:22.0832728Z Progress (2): 2.5/3.0 MB | 490 kB
2026-01-19T16:16:22.0833224Z                                  
2026-01-19T16:16:22.0833870Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport/4.1.96.Final/netty-transport-4.1.96.Final.jar (490 kB at 1.2 MB/s)
2026-01-19T16:16:22.0834716Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.28.0/opentelemetry-sdk-logs-1.28.0.jar
2026-01-19T16:16:22.0835601Z Progress (2): 2.5/3.0 MB | 7.7/259 kB
2026-01-19T16:16:22.0836124Z Progress (2): 2.5/3.0 MB | 16/259 kB 
2026-01-19T16:16:22.0836883Z Progress (2): 2.5/3.0 MB | 16/259 kB
2026-01-19T16:16:22.0837414Z Progress (2): 2.5/3.0 MB | 32/259 kB
2026-01-19T16:16:22.0837929Z Progress (2): 2.6/3.0 MB | 32/259 kB
2026-01-19T16:16:22.0838356Z Progress (3): 2.6/3.0 MB | 32/259 kB | 7.7/11 kB
2026-01-19T16:16:22.0838863Z Progress (3): 2.6/3.0 MB | 32/259 kB | 11 kB    
2026-01-19T16:16:22.0839358Z Progress (3): 2.6/3.0 MB | 32/259 kB | 11 kB
2026-01-19T16:16:22.0839739Z                                             
2026-01-19T16:16:22.0840476Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-exporter-logging/1.28.0/opentelemetry-exporter-logging-1.28.0.jar (11 kB at 27 kB/s)
2026-01-19T16:16:22.0841349Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.28.0/opentelemetry-sdk-common-1.28.0.jar
2026-01-19T16:16:22.0849055Z Progress (2): 2.6/3.0 MB | 32/259 kB
2026-01-19T16:16:22.0850906Z Progress (2): 2.6/3.0 MB | 32/259 kB
2026-01-19T16:16:22.0851471Z Progress (2): 2.6/3.0 MB | 32/259 kB
2026-01-19T16:16:22.0852042Z Progress (2): 2.6/3.0 MB | 32/259 kB
2026-01-19T16:16:22.0852608Z Progress (2): 2.6/3.0 MB | 32/259 kB
2026-01-19T16:16:22.0859828Z Progress (2): 2.6/3.0 MB | 49/259 kB
2026-01-19T16:16:22.0863177Z Progress (2): 2.6/3.0 MB | 65/259 kB
2026-01-19T16:16:22.0865934Z Progress (2): 2.7/3.0 MB | 65/259 kB
2026-01-19T16:16:22.0868177Z Progress (2): 2.7/3.0 MB | 65/259 kB
2026-01-19T16:16:22.0906181Z Progress (2): 2.7/3.0 MB | 65/259 kB
2026-01-19T16:16:22.0907938Z Progress (2): 2.7/3.0 MB | 81/259 kB
2026-01-19T16:16:22.0916439Z Progress (2): 2.7/3.0 MB | 98/259 kB
2026-01-19T16:16:22.0917037Z Progress (2): 2.7/3.0 MB | 114/259 kB
2026-01-19T16:16:22.0917407Z Progress (2): 2.7/3.0 MB | 131/259 kB
2026-01-19T16:16:22.0917754Z Progress (2): 2.7/3.0 MB | 147/259 kB
2026-01-19T16:16:22.0918090Z Progress (2): 2.7/3.0 MB | 163/259 kB
2026-01-19T16:16:22.0918651Z Progress (2): 2.7/3.0 MB | 180/259 kB
2026-01-19T16:16:22.0919111Z Progress (2): 2.7/3.0 MB | 196/259 kB
2026-01-19T16:16:22.0920262Z Progress (2): 2.7/3.0 MB | 213/259 kB
2026-01-19T16:16:22.0920634Z Progress (2): 2.7/3.0 MB | 213/259 kB
2026-01-19T16:16:22.0920948Z Progress (2): 2.7/3.0 MB | 229/259 kB
2026-01-19T16:16:22.0921290Z Progress (2): 2.7/3.0 MB | 229/259 kB
2026-01-19T16:16:22.0921618Z Progress (2): 2.7/3.0 MB | 245/259 kB
2026-01-19T16:16:22.0921958Z Progress (2): 2.7/3.0 MB | 245/259 kB
2026-01-19T16:16:22.0922281Z Progress (2): 2.7/3.0 MB | 259 kB    
2026-01-19T16:16:22.0922703Z Progress (2): 2.8/3.0 MB | 259 kB
2026-01-19T16:16:22.0923027Z Progress (2): 2.8/3.0 MB | 259 kB
2026-01-19T16:16:22.0943430Z                                  
2026-01-19T16:16:22.0945900Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-metrics/1.28.0/opentelemetry-sdk-metrics-1.28.0.jar (259 kB at 625 kB/s)
2026-01-19T16:16:22.0963876Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.28.0/opentelemetry-sdk-extension-autoconfigure-spi-1.28.0.jar
2026-01-19T16:16:22.0964427Z Progress (1): 2.8/3.0 MB
2026-01-19T16:16:22.0964754Z Progress (1): 2.8/3.0 MB
2026-01-19T16:16:22.0965072Z Progress (1): 2.8/3.0 MB
2026-01-19T16:16:22.0965387Z Progress (1): 2.8/3.0 MB
2026-01-19T16:16:22.0965695Z Progress (1): 2.9/3.0 MB
2026-01-19T16:16:22.0966019Z Progress (1): 2.9/3.0 MB
2026-01-19T16:16:22.0966334Z Progress (2): 2.9/3.0 MB | 7.2 kB
2026-01-19T16:16:22.0966875Z                                  
2026-01-19T16:16:22.0967364Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-extension-incubator/1.28.0-alpha/opentelemetry-extension-incubator-1.28.0-alpha.jar (7.2 kB at 17 kB/s)
2026-01-19T16:16:22.0968205Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.28.0/opentelemetry-sdk-extension-autoconfigure-1.28.0.jar
2026-01-19T16:16:22.0968688Z Progress (1): 2.9/3.0 MB
2026-01-19T16:16:22.0969001Z Progress (1): 2.9/3.0 MB
2026-01-19T16:16:22.0969311Z Progress (1): 2.9/3.0 MB
2026-01-19T16:16:22.0969684Z Progress (1): 2.9/3.0 MB
2026-01-19T16:16:22.0969999Z Progress (1): 3.0/3.0 MB
2026-01-19T16:16:22.0970326Z Progress (1): 3.0/3.0 MB
2026-01-19T16:16:22.0970631Z Progress (1): 3.0/3.0 MB
2026-01-19T16:16:22.0970940Z Progress (1): 3.0/3.0 MB
2026-01-19T16:16:22.0971242Z Progress (1): 3.0/3.0 MB
2026-01-19T16:16:22.0971551Z Progress (1): 3.0 MB    
2026-01-19T16:16:22.0971991Z                     
2026-01-19T16:16:22.0972408Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/32.1.2-jre/guava-32.1.2-jre.jar (3.0 MB at 7.2 MB/s)
2026-01-19T16:16:22.0972994Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.28.0-alpha/opentelemetry-api-events-1.28.0-alpha.jar
2026-01-19T16:16:22.1000870Z Progress (1): 7.7/47 kB
2026-01-19T16:16:22.1007591Z Progress (1): 16/47 kB 
2026-01-19T16:16:22.1009048Z Progress (1): 32/47 kB
2026-01-19T16:16:22.1009961Z Progress (1): 47 kB   
2026-01-19T16:16:22.1010413Z                    
2026-01-19T16:16:22.1010995Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-logs/1.28.0/opentelemetry-sdk-logs-1.28.0.jar (47 kB at 111 kB/s)
2026-01-19T16:16:22.1013527Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.28.0/opentelemetry-sdk-trace-1.28.0.jar
2026-01-19T16:16:22.1029079Z Progress (1): 7.7/42 kB
2026-01-19T16:16:22.1029683Z Progress (1): 12/42 kB 
2026-01-19T16:16:22.1041631Z Progress (1): 28/42 kB
2026-01-19T16:16:22.1046770Z Progress (1): 42 kB   
2026-01-19T16:16:22.1047096Z                    
2026-01-19T16:16:22.1047530Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-common/1.28.0/opentelemetry-sdk-common-1.28.0.jar (42 kB at 99 kB/s)
2026-01-19T16:16:22.1048095Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.28.0/opentelemetry-sdk-1.28.0.jar
2026-01-19T16:16:22.1131373Z Progress (1): 7.7/16 kB
2026-01-19T16:16:22.1136150Z Progress (1): 16/16 kB 
2026-01-19T16:16:22.1151151Z Progress (1): 16 kB   
2026-01-19T16:16:22.1152270Z                    
2026-01-19T16:16:22.1152897Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure-spi/1.28.0/opentelemetry-sdk-extension-autoconfigure-spi-1.28.0.jar (16 kB at 37 kB/s)
2026-01-19T16:16:22.1158935Z Downloading from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.28.0-alpha/opentelemetry-semconv-1.28.0-alpha.jar
2026-01-19T16:16:22.1199151Z Progress (1): 7.7/40 kB
2026-01-19T16:16:22.1199773Z Progress (1): 16/40 kB 
2026-01-19T16:16:22.1202673Z Progress (1): 32/40 kB
2026-01-19T16:16:22.1202992Z Progress (1): 40 kB   
2026-01-19T16:16:22.1203269Z                    
2026-01-19T16:16:22.1203743Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-extension-autoconfigure/1.28.0/opentelemetry-sdk-extension-autoconfigure-1.28.0.jar (40 kB at 90 kB/s)
2026-01-19T16:16:22.1204327Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.5/byte-buddy-1.14.5.jar
2026-01-19T16:16:22.1216369Z Progress (1): 6.0 kB
2026-01-19T16:16:22.1219932Z                     
2026-01-19T16:16:22.1220375Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-api-events/1.28.0-alpha/opentelemetry-api-events-1.28.0-alpha.jar (6.0 kB at 14 kB/s)
2026-01-19T16:16:22.1222058Z Progress (1): 7.7/117 kB
2026-01-19T16:16:22.1248747Z Progress (1): 16/117 kB 
2026-01-19T16:16:22.1249083Z Progress (1): 32/117 kB
2026-01-19T16:16:22.1249606Z Progress (1): 49/117 kB
2026-01-19T16:16:22.1249928Z Progress (1): 65/117 kB
2026-01-19T16:16:22.1250226Z                        
2026-01-19T16:16:22.1250639Z Downloading from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client/2.12.3/async-http-client-2.12.3.jar
2026-01-19T16:16:22.1251088Z Progress (1): 81/117 kB
2026-01-19T16:16:22.1252585Z Progress (1): 98/117 kB
2026-01-19T16:16:22.1253053Z Progress (1): 114/117 kB
2026-01-19T16:16:22.1253460Z Progress (1): 117 kB    
2026-01-19T16:16:22.1253863Z                     
2026-01-19T16:16:22.1254391Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk-trace/1.28.0/opentelemetry-sdk-trace-1.28.0.jar (117 kB at 261 kB/s)
2026-01-19T16:16:22.1255154Z Progress (1): 3.4/6.8 kB
2026-01-19T16:16:22.1264047Z Progress (1): 6.8 kB    
2026-01-19T16:16:22.1264358Z                     
2026-01-19T16:16:22.1264785Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-sdk/1.28.0/opentelemetry-sdk-1.28.0.jar (6.8 kB at 15 kB/s)
2026-01-19T16:16:22.1265373Z Downloading from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-netty-utils/2.12.3/async-http-client-netty-utils-2.12.3.jar
2026-01-19T16:16:22.1273966Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-socks/4.1.60.Final/netty-codec-socks-4.1.60.Final.jar
2026-01-19T16:16:22.1398591Z Progress (1): 7.7/40 kB
2026-01-19T16:16:22.1399121Z Progress (1): 16/40 kB 
2026-01-19T16:16:22.1399685Z Progress (1): 32/40 kB
2026-01-19T16:16:22.1400752Z Progress (1): 40 kB   
2026-01-19T16:16:22.1401041Z                    
2026-01-19T16:16:22.1401501Z Downloaded from central: https://repo.maven.apache.org/maven2/io/opentelemetry/opentelemetry-semconv/1.28.0-alpha/opentelemetry-semconv-1.28.0-alpha.jar (40 kB at 86 kB/s)
2026-01-19T16:16:22.1402074Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler-proxy/4.1.60.Final/netty-handler-proxy-4.1.60.Final.jar
2026-01-19T16:16:22.1451801Z Progress (1): 0/4.2 MB
2026-01-19T16:16:22.1457831Z Progress (1): 0/4.2 MB
2026-01-19T16:16:22.1458465Z Progress (2): 0/4.2 MB | 7.7/9.9 kB
2026-01-19T16:16:22.1463189Z Progress (2): 0/4.2 MB | 9.9 kB    
2026-01-19T16:16:22.1543231Z Progress (2): 0/4.2 MB | 9.9 kB
2026-01-19T16:16:22.1547437Z Progress (2): 0/4.2 MB | 9.9 kB
2026-01-19T16:16:22.1548019Z Progress (2): 0.1/4.2 MB | 9.9 kB
2026-01-19T16:16:22.1549307Z Progress (2): 0.1/4.2 MB | 9.9 kB
2026-01-19T16:16:22.1549876Z Progress (2): 0.1/4.2 MB | 9.9 kB
2026-01-19T16:16:22.1550406Z Progress (3): 0.1/4.2 MB | 9.9 kB | 7.7/452 kB
2026-01-19T16:16:22.1550957Z Progress (3): 0.1/4.2 MB | 9.9 kB | 16/452 kB 
2026-01-19T16:16:22.1551438Z Progress (3): 0.1/4.2 MB | 9.9 kB | 16/452 kB
2026-01-19T16:16:22.1551859Z                                              
2026-01-19T16:16:22.1552444Z Downloaded from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client-netty-utils/2.12.3/async-http-client-netty-utils-2.12.3.jar (9.9 kB at 21 kB/s)
2026-01-19T16:16:22.1553314Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.60.Final/netty-transport-native-epoll-4.1.60.Final-linux-x86_64.jar
2026-01-19T16:16:22.1553969Z Progress (2): 0.1/4.2 MB | 16/452 kB
2026-01-19T16:16:22.1554395Z Progress (2): 0.1/4.2 MB | 16/452 kB
2026-01-19T16:16:22.1554844Z Progress (2): 0.2/4.2 MB | 16/452 kB
2026-01-19T16:16:22.1555255Z Progress (2): 0.2/4.2 MB | 16/452 kB
2026-01-19T16:16:22.1556659Z Progress (3): 0.2/4.2 MB | 16/452 kB | 7.7/119 kB
2026-01-19T16:16:22.1557058Z Progress (3): 0.2/4.2 MB | 16/452 kB | 16/119 kB 
2026-01-19T16:16:22.1557408Z Progress (3): 0.2/4.2 MB | 16/452 kB | 16/119 kB
2026-01-19T16:16:22.1557746Z Progress (3): 0.2/4.2 MB | 16/452 kB | 32/119 kB
2026-01-19T16:16:22.1558076Z Progress (3): 0.2/4.2 MB | 16/452 kB | 32/119 kB
2026-01-19T16:16:22.1558412Z Progress (3): 0.2/4.2 MB | 16/452 kB | 49/119 kB
2026-01-19T16:16:22.1558925Z Progress (3): 0.2/4.2 MB | 16/452 kB | 49/119 kB
2026-01-19T16:16:22.1559265Z Progress (3): 0.2/4.2 MB | 16/452 kB | 65/119 kB
2026-01-19T16:16:22.1559595Z Progress (3): 0.2/4.2 MB | 16/452 kB | 81/119 kB
2026-01-19T16:16:22.1560248Z Progress (3): 0.2/4.2 MB | 16/452 kB | 98/119 kB
2026-01-19T16:16:22.1560602Z Progress (3): 0.2/4.2 MB | 16/452 kB | 114/119 kB
2026-01-19T16:16:22.1560956Z Progress (3): 0.2/4.2 MB | 16/452 kB | 119 kB    
2026-01-19T16:16:22.1561294Z Progress (3): 0.2/4.2 MB | 32/452 kB | 119 kB
2026-01-19T16:16:22.1561637Z Progress (3): 0.2/4.2 MB | 49/452 kB | 119 kB
2026-01-19T16:16:22.1561982Z Progress (3): 0.2/4.2 MB | 65/452 kB | 119 kB
2026-01-19T16:16:22.1562453Z Progress (3): 0.2/4.2 MB | 81/452 kB | 119 kB
2026-01-19T16:16:22.1562791Z Progress (3): 0.2/4.2 MB | 98/452 kB | 119 kB
2026-01-19T16:16:22.1563127Z Progress (3): 0.2/4.2 MB | 114/452 kB | 119 kB
2026-01-19T16:16:22.1563437Z                                               
2026-01-19T16:16:22.1563873Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-codec-socks/4.1.60.Final/netty-codec-socks-4.1.60.Final.jar (119 kB at 249 kB/s)
2026-01-19T16:16:22.1564486Z Downloading from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.60.Final/netty-transport-native-kqueue-4.1.60.Final-osx-x86_64.jar
2026-01-19T16:16:22.1597570Z Progress (2): 0.2/4.2 MB | 131/452 kB
2026-01-19T16:16:22.1598082Z Progress (2): 0.2/4.2 MB | 147/452 kB
2026-01-19T16:16:22.1598529Z Progress (2): 0.2/4.2 MB | 163/452 kB
2026-01-19T16:16:22.1600110Z Progress (2): 0.2/4.2 MB | 163/452 kB
2026-01-19T16:16:22.1600615Z Progress (2): 0.3/4.2 MB | 163/452 kB
2026-01-19T16:16:22.1601114Z Progress (2): 0.3/4.2 MB | 163/452 kB
2026-01-19T16:16:22.1601573Z Progress (2): 0.3/4.2 MB | 163/452 kB
2026-01-19T16:16:22.1602068Z Progress (2): 0.3/4.2 MB | 163/452 kB
2026-01-19T16:16:22.1602539Z Progress (2): 0.3/4.2 MB | 163/452 kB
2026-01-19T16:16:22.1602980Z Progress (2): 0.3/4.2 MB | 163/452 kB
2026-01-19T16:16:22.1603405Z Progress (2): 0.4/4.2 MB | 163/452 kB
2026-01-19T16:16:22.1630871Z Progress (2): 0.4/4.2 MB | 163/452 kB
2026-01-19T16:16:22.1631483Z Progress (2): 0.4/4.2 MB | 180/452 kB
2026-01-19T16:16:22.1631948Z Progress (2): 0.4/4.2 MB | 196/452 kB
2026-01-19T16:16:22.1632398Z Progress (2): 0.4/4.2 MB | 213/452 kB
2026-01-19T16:16:22.1632813Z Progress (2): 0.4/4.2 MB | 229/452 kB
2026-01-19T16:16:22.1633233Z Progress (2): 0.4/4.2 MB | 245/452 kB
2026-01-19T16:16:22.1633648Z Progress (2): 0.4/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1660203Z Progress (2): 0.4/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1660833Z Progress (2): 0.4/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1661326Z Progress (2): 0.4/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1661791Z Progress (2): 0.4/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1662256Z Progress (2): 0.5/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1662736Z Progress (2): 0.5/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1663253Z Progress (2): 0.5/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1663754Z Progress (2): 0.5/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1664225Z Progress (2): 0.5/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1668620Z Progress (2): 0.5/4.2 MB | 262/452 kB
2026-01-19T16:16:22.1674758Z Progress (2): 0.5/4.2 MB | 278/452 kB
2026-01-19T16:16:22.1709926Z Progress (2): 0.5/4.2 MB | 294/452 kB
2026-01-19T16:16:22.1710616Z Progress (3): 0.5/4.2 MB | 294/452 kB | 7.7/157 kB
2026-01-19T16:16:22.1711182Z Progress (3): 0.5/4.2 MB | 294/452 kB | 12/157 kB 
2026-01-19T16:16:22.1711632Z Progress (3): 0.5/4.2 MB | 311/452 kB | 12/157 kB
2026-01-19T16:16:22.1712094Z Progress (3): 0.5/4.2 MB | 311/452 kB | 29/157 kB
2026-01-19T16:16:22.1712708Z Progress (3): 0.5/4.2 MB | 327/452 kB | 29/157 kB
2026-01-19T16:16:22.1713243Z Progress (3): 0.5/4.2 MB | 344/452 kB | 29/157 kB
2026-01-19T16:16:22.1713679Z Progress (3): 0.5/4.2 MB | 360/452 kB | 29/157 kB
2026-01-19T16:16:22.1714114Z Progress (3): 0.5/4.2 MB | 376/452 kB | 29/157 kB
2026-01-19T16:16:22.1714546Z Progress (3): 0.5/4.2 MB | 376/452 kB | 45/157 kB
2026-01-19T16:16:22.1715152Z Progress (4): 0.5/4.2 MB | 376/452 kB | 45/157 kB | 7.7/24 kB
2026-01-19T16:16:22.1715613Z Progress (4): 0.5/4.2 MB | 376/452 kB | 45/157 kB | 16/24 kB 
2026-01-19T16:16:22.1716066Z Progress (4): 0.5/4.2 MB | 376/452 kB | 45/157 kB | 24 kB   
2026-01-19T16:16:22.1717426Z                                                          
2026-01-19T16:16:22.1718019Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-handler-proxy/4.1.60.Final/netty-handler-proxy-4.1.60.Final.jar (24 kB at 49 kB/s)
2026-01-19T16:16:22.1718680Z Downloading from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams/2.0.4/netty-reactive-streams-2.0.4.jar
2026-01-19T16:16:22.1719449Z Progress (3): 0.5/4.2 MB | 376/452 kB | 61/157 kB
2026-01-19T16:16:22.1719955Z Progress (3): 0.5/4.2 MB | 376/452 kB | 66/157 kB
2026-01-19T16:16:22.1722244Z Progress (3): 0.5/4.2 MB | 376/452 kB | 82/157 kB
2026-01-19T16:16:22.1747649Z Progress (3): 0.5/4.2 MB | 376/452 kB | 98/157 kB
2026-01-19T16:16:22.1765384Z Progress (3): 0.5/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1765977Z Progress (3): 0.6/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1777691Z Progress (3): 0.6/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1778300Z Progress (3): 0.6/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1778747Z Progress (3): 0.6/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1779180Z Progress (3): 0.6/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1779599Z Progress (3): 0.6/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1780038Z Progress (3): 0.7/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1780487Z Progress (3): 0.7/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1780913Z Progress (3): 0.7/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1781334Z Progress (3): 0.7/4.2 MB | 376/452 kB | 115/157 kB
2026-01-19T16:16:22.1781758Z Progress (3): 0.7/4.2 MB | 376/452 kB | 131/157 kB
2026-01-19T16:16:22.1782183Z Progress (3): 0.7/4.2 MB | 393/452 kB | 131/157 kB
2026-01-19T16:16:22.1782610Z Progress (3): 0.7/4.2 MB | 393/452 kB | 147/157 kB
2026-01-19T16:16:22.1783036Z Progress (3): 0.7/4.2 MB | 409/452 kB | 147/157 kB
2026-01-19T16:16:22.1783449Z Progress (3): 0.7/4.2 MB | 409/452 kB | 157 kB    
2026-01-19T16:16:22.1783871Z Progress (3): 0.7/4.2 MB | 426/452 kB | 157 kB
2026-01-19T16:16:22.1784287Z Progress (3): 0.7/4.2 MB | 442/452 kB | 157 kB
2026-01-19T16:16:22.1784676Z                                               
2026-01-19T16:16:22.1785224Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-epoll/4.1.60.Final/netty-transport-native-epoll-4.1.60.Final-linux-x86_64.jar (157 kB at 314 kB/s)
2026-01-19T16:16:22.1785903Z Downloading from central: https://repo.maven.apache.org/maven2/com/sun/activation/jakarta.activation/1.2.2/jakarta.activation-1.2.2.jar
2026-01-19T16:16:22.1786426Z Progress (3): 0.7/4.2 MB | 442/452 kB | 4.1/113 kB
2026-01-19T16:16:22.1792386Z Progress (3): 0.7/4.2 MB | 442/452 kB | 20/113 kB 
2026-01-19T16:16:22.1830823Z Progress (3): 0.7/4.2 MB | 442/452 kB | 37/113 kB
2026-01-19T16:16:22.1831358Z Progress (3): 0.7/4.2 MB | 442/452 kB | 53/113 kB
2026-01-19T16:16:22.1831808Z Progress (3): 0.7/4.2 MB | 442/452 kB | 61/113 kB
2026-01-19T16:16:22.1832230Z Progress (3): 0.7/4.2 MB | 452 kB | 61/113 kB    
2026-01-19T16:16:22.1832652Z Progress (3): 0.7/4.2 MB | 452 kB | 78/113 kB
2026-01-19T16:16:22.1833075Z Progress (3): 0.7/4.2 MB | 452 kB | 94/113 kB
2026-01-19T16:16:22.1833461Z                                              
2026-01-19T16:16:22.1833967Z Downloaded from central: https://repo.maven.apache.org/maven2/org/asynchttpclient/async-http-client/2.12.3/async-http-client-2.12.3.jar (452 kB at 894 kB/s)
2026-01-19T16:16:22.1834626Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.13.0/selenium-http-4.13.0.jar
2026-01-19T16:16:22.1835154Z Progress (2): 0.7/4.2 MB | 94/113 kB
2026-01-19T16:16:22.1835717Z Progress (2): 0.7/4.2 MB | 94/113 kB
2026-01-19T16:16:22.1836122Z Progress (2): 0.8/4.2 MB | 94/113 kB
2026-01-19T16:16:22.1837471Z Progress (2): 0.8/4.2 MB | 94/113 kB
2026-01-19T16:16:22.1837800Z Progress (2): 0.8/4.2 MB | 94/113 kB
2026-01-19T16:16:22.1838108Z Progress (2): 0.8/4.2 MB | 94/113 kB
2026-01-19T16:16:22.1838420Z Progress (2): 0.8/4.2 MB | 94/113 kB
2026-01-19T16:16:22.1838721Z Progress (2): 0.8/4.2 MB | 94/113 kB
2026-01-19T16:16:22.1839022Z Progress (2): 0.9/4.2 MB | 94/113 kB
2026-01-19T16:16:22.1846274Z Progress (2): 0.9/4.2 MB | 94/113 kB
2026-01-19T16:16:22.1849127Z Progress (2): 0.9/4.2 MB | 111/113 kB
2026-01-19T16:16:22.1851187Z Progress (2): 0.9/4.2 MB | 113 kB    
2026-01-19T16:16:22.1855049Z                                  
2026-01-19T16:16:22.1859522Z Downloaded from central: https://repo.maven.apache.org/maven2/io/netty/netty-transport-native-kqueue/4.1.60.Final/netty-transport-native-kqueue-4.1.60.Final-osx-x86_64.jar (113 kB at 222 kB/s)
2026-01-19T16:16:22.1861930Z Downloading from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.2/failsafe-3.3.2.jar
2026-01-19T16:16:22.1891444Z Progress (1): 0.9/4.2 MB
2026-01-19T16:16:22.1894924Z Progress (1): 0.9/4.2 MB
2026-01-19T16:16:22.1899688Z Progress (1): 0.9/4.2 MB
2026-01-19T16:16:22.1901305Z Progress (1): 0.9/4.2 MB
2026-01-19T16:16:22.1903335Z Progress (1): 0.9/4.2 MB
2026-01-19T16:16:22.1904891Z Progress (1): 1.0/4.2 MB
2026-01-19T16:16:22.1908514Z Progress (1): 1.0/4.2 MB
2026-01-19T16:16:22.1909426Z Progress (1): 1.0/4.2 MB
2026-01-19T16:16:22.1909910Z Progress (1): 1.0/4.2 MB
2026-01-19T16:16:22.1910396Z Progress (1): 1.0/4.2 MB
2026-01-19T16:16:22.1910894Z Progress (1): 1.0/4.2 MB
2026-01-19T16:16:22.1911462Z Progress (1): 1.1/4.2 MB
2026-01-19T16:16:22.1911982Z Progress (1): 1.1/4.2 MB
2026-01-19T16:16:22.1917086Z Progress (1): 1.1/4.2 MB
2026-01-19T16:16:22.1924553Z Progress (1): 1.1/4.2 MB
2026-01-19T16:16:22.1929530Z Progress (1): 1.1/4.2 MB
2026-01-19T16:16:22.1935075Z Progress (1): 1.1/4.2 MB
2026-01-19T16:16:22.1939803Z Progress (1): 1.2/4.2 MB
2026-01-19T16:16:22.1948368Z Progress (1): 1.2/4.2 MB
2026-01-19T16:16:22.1948931Z Progress (1): 1.2/4.2 MB
2026-01-19T16:16:22.1953765Z Progress (1): 1.2/4.2 MB
2026-01-19T16:16:22.1961239Z Progress (1): 1.2/4.2 MB
2026-01-19T16:16:22.1967865Z Progress (1): 1.2/4.2 MB
2026-01-19T16:16:22.1971292Z Progress (1): 1.3/4.2 MB
2026-01-19T16:16:22.1977667Z Progress (1): 1.3/4.2 MB
2026-01-19T16:16:22.1988125Z Progress (1): 1.3/4.2 MB
2026-01-19T16:16:22.1994326Z Progress (1): 1.3/4.2 MB
2026-01-19T16:16:22.2000472Z Progress (1): 1.3/4.2 MB
2026-01-19T16:16:22.2008752Z Progress (2): 1.3/4.2 MB | 7.7/60 kB
2026-01-19T16:16:22.2012645Z Progress (2): 1.3/4.2 MB | 16/60 kB 
2026-01-19T16:16:22.2018564Z Progress (2): 1.3/4.2 MB | 16/60 kB
2026-01-19T16:16:22.2019159Z Progress (2): 1.3/4.2 MB | 32/60 kB
2026-01-19T16:16:22.2050612Z Progress (2): 1.4/4.2 MB | 32/60 kB
2026-01-19T16:16:22.2050967Z Progress (2): 1.4/4.2 MB | 32/60 kB
2026-01-19T16:16:22.2051289Z Progress (2): 1.4/4.2 MB | 32/60 kB
2026-01-19T16:16:22.2051619Z Progress (2): 1.4/4.2 MB | 49/60 kB
2026-01-19T16:16:22.2051928Z Progress (2): 1.4/4.2 MB | 60 kB   
2026-01-19T16:16:22.2052224Z                                 
2026-01-19T16:16:22.2052635Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-http/4.13.0/selenium-http-4.13.0.jar (60 kB at 114 kB/s)
2026-01-19T16:16:22.2053213Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.13.0/selenium-json-4.13.0.jar
2026-01-19T16:16:22.2053637Z Progress (2): 1.4/4.2 MB | 7.7/22 kB
2026-01-19T16:16:22.2053966Z Progress (2): 1.4/4.2 MB | 16/22 kB 
2026-01-19T16:16:22.2054329Z Progress (2): 1.4/4.2 MB | 22 kB   
2026-01-19T16:16:22.2054619Z                                 
2026-01-19T16:16:22.2055029Z Downloaded from central: https://repo.maven.apache.org/maven2/com/typesafe/netty/netty-reactive-streams/2.0.4/netty-reactive-streams-2.0.4.jar (22 kB at 41 kB/s)
2026-01-19T16:16:22.2055736Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.13.0/selenium-manager-4.13.0.jar
2026-01-19T16:16:22.2085753Z Progress (1): 1.4/4.2 MB
2026-01-19T16:16:22.2086824Z Progress (1): 1.4/4.2 MB
2026-01-19T16:16:22.2087302Z Progress (1): 1.4/4.2 MB
2026-01-19T16:16:22.2088256Z Progress (1): 1.5/4.2 MB
2026-01-19T16:16:22.2090062Z Progress (1): 1.5/4.2 MB
2026-01-19T16:16:22.2090393Z Progress (1): 1.5/4.2 MB
2026-01-19T16:16:22.2090705Z Progress (1): 1.5/4.2 MB
2026-01-19T16:16:22.2091021Z Progress (2): 1.5/4.2 MB | 7.7/144 kB
2026-01-19T16:16:22.2091387Z Progress (2): 1.5/4.2 MB | 16/144 kB 
2026-01-19T16:16:22.2091714Z Progress (2): 1.5/4.2 MB | 25/144 kB
2026-01-19T16:16:22.2092193Z Progress (2): 1.5/4.2 MB | 41/144 kB
2026-01-19T16:16:22.2092538Z Progress (2): 1.5/4.2 MB | 57/144 kB
2026-01-19T16:16:22.2128833Z Progress (2): 1.5/4.2 MB | 66/144 kB
2026-01-19T16:16:22.2130417Z Progress (2): 1.5/4.2 MB | 66/144 kB
2026-01-19T16:16:22.2131959Z Progress (2): 1.5/4.2 MB | 66/144 kB
2026-01-19T16:16:22.2133463Z Progress (2): 1.6/4.2 MB | 66/144 kB
2026-01-19T16:16:22.2134868Z Progress (3): 1.6/4.2 MB | 66/144 kB | 7.7/68 kB
2026-01-19T16:16:22.2136263Z Progress (3): 1.6/4.2 MB | 66/144 kB | 16/68 kB 
2026-01-19T16:16:22.2137956Z Progress (3): 1.6/4.2 MB | 66/144 kB | 16/68 kB
2026-01-19T16:16:22.2139358Z Progress (3): 1.6/4.2 MB | 66/144 kB | 32/68 kB
2026-01-19T16:16:22.2146964Z Progress (3): 1.6/4.2 MB | 66/144 kB | 32/68 kB
2026-01-19T16:16:22.2147219Z Progress (3): 1.6/4.2 MB | 82/144 kB | 32/68 kB
2026-01-19T16:16:22.2147411Z Progress (3): 1.6/4.2 MB | 82/144 kB | 32/68 kB
2026-01-19T16:16:22.2147589Z Progress (3): 1.6/4.2 MB | 98/144 kB | 32/68 kB
2026-01-19T16:16:22.2147783Z Progress (3): 1.6/4.2 MB | 98/144 kB | 32/68 kB
2026-01-19T16:16:22.2147962Z Progress (3): 1.6/4.2 MB | 115/144 kB | 32/68 kB
2026-01-19T16:16:22.2148145Z Progress (3): 1.6/4.2 MB | 115/144 kB | 32/68 kB
2026-01-19T16:16:22.2148324Z Progress (3): 1.6/4.2 MB | 131/144 kB | 32/68 kB
2026-01-19T16:16:22.2148510Z Progress (3): 1.7/4.2 MB | 131/144 kB | 32/68 kB
2026-01-19T16:16:22.2148840Z Progress (3): 1.7/4.2 MB | 144 kB | 32/68 kB    
2026-01-19T16:16:22.2149032Z Progress (3): 1.7/4.2 MB | 144 kB | 32/68 kB
2026-01-19T16:16:22.2149314Z Progress (3): 1.7/4.2 MB | 144 kB | 32/68 kB
2026-01-19T16:16:22.2189743Z Progress (3): 1.7/4.2 MB | 144 kB | 32/68 kB
2026-01-19T16:16:22.2191260Z Progress (3): 1.7/4.2 MB | 144 kB | 32/68 kB
2026-01-19T16:16:22.2191789Z Progress (3): 1.7/4.2 MB | 144 kB | 32/68 kB
2026-01-19T16:16:22.2192131Z Progress (3): 1.7/4.2 MB | 144 kB | 49/68 kB
2026-01-19T16:16:22.2192452Z Progress (3): 1.8/4.2 MB | 144 kB | 49/68 kB
2026-01-19T16:16:22.2192793Z Progress (3): 1.8/4.2 MB | 144 kB | 65/68 kB
2026-01-19T16:16:22.2193123Z Progress (3): 1.8/4.2 MB | 144 kB | 68 kB   
2026-01-19T16:16:22.2193462Z Progress (3): 1.8/4.2 MB | 144 kB | 68 kB
2026-01-19T16:16:22.2193813Z Progress (3): 1.8/4.2 MB | 144 kB | 68 kB
2026-01-19T16:16:22.2194125Z                                          
2026-01-19T16:16:22.2194588Z Downloaded from central: https://repo.maven.apache.org/maven2/com/sun/activation/jakarta.activation/1.2.2/jakarta.activation-1.2.2.jar (68 kB at 127 kB/s)
2026-01-19T16:16:22.2195134Z Downloaded from central: https://repo.maven.apache.org/maven2/dev/failsafe/failsafe/3.3.2/failsafe-3.3.2.jar (144 kB at 267 kB/s)
2026-01-19T16:16:22.2195665Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.13.0/selenium-os-4.13.0.jar
2026-01-19T16:16:22.2196094Z Progress (1): 1.8/4.2 MB
2026-01-19T16:16:22.2196401Z Progress (1): 1.8/4.2 MB
2026-01-19T16:16:22.2196891Z Progress (1): 1.8/4.2 MB
2026-01-19T16:16:22.2197203Z Progress (1): 1.9/4.2 MB
2026-01-19T16:16:22.2197507Z Progress (1): 1.9/4.2 MB
2026-01-19T16:16:22.2197806Z Progress (1): 1.9/4.2 MB
2026-01-19T16:16:22.2198091Z                         
2026-01-19T16:16:22.2198478Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-exec/1.3/commons-exec-1.3.jar
2026-01-19T16:16:22.2203938Z Progress (1): 1.9/4.2 MB
2026-01-19T16:16:22.2208282Z Progress (1): 1.9/4.2 MB
2026-01-19T16:16:22.2211930Z Progress (1): 1.9/4.2 MB
2026-01-19T16:16:22.2237881Z Progress (1): 1.9/4.2 MB
2026-01-19T16:16:22.2238246Z Progress (1): 2.0/4.2 MB
2026-01-19T16:16:22.2238543Z Progress (1): 2.0/4.2 MB
2026-01-19T16:16:22.2238843Z Progress (1): 2.0/4.2 MB
2026-01-19T16:16:22.2239144Z Progress (1): 2.0/4.2 MB
2026-01-19T16:16:22.2239456Z Progress (1): 2.0/4.2 MB
2026-01-19T16:16:22.2239756Z Progress (1): 2.0/4.2 MB
2026-01-19T16:16:22.2240066Z Progress (1): 2.1/4.2 MB
2026-01-19T16:16:22.2240380Z Progress (2): 2.1/4.2 MB | 7.7/71 kB
2026-01-19T16:16:22.2240856Z Progress (2): 2.1/4.2 MB | 12/71 kB 
2026-01-19T16:16:22.2281315Z Progress (2): 2.1/4.2 MB | 29/71 kB
2026-01-19T16:16:22.2281696Z Progress (2): 2.1/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2282008Z Progress (2): 2.1/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2282328Z Progress (2): 2.1/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2282657Z Progress (2): 2.1/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2282983Z Progress (2): 2.1/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2283303Z Progress (2): 2.1/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2283608Z Progress (2): 2.2/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2283933Z Progress (2): 2.2/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2284272Z Progress (2): 2.2/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2284597Z Progress (2): 2.2/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2284911Z Progress (2): 2.2/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2285230Z Progress (2): 2.2/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2285544Z Progress (2): 2.3/4.2 MB | 45/71 kB
2026-01-19T16:16:22.2285871Z Progress (2): 2.3/4.2 MB | 61/71 kB
2026-01-19T16:16:22.2286203Z Progress (2): 2.3/4.2 MB | 71 kB   
2026-01-19T16:16:22.2286697Z                                 
2026-01-19T16:16:22.2287127Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-json/4.13.0/selenium-json-4.13.0.jar (71 kB at 128 kB/s)
2026-01-19T16:16:22.2287719Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.13.0/selenium-support-4.13.0.jar
2026-01-19T16:16:22.2298180Z Progress (1): 2.3/4.2 MB
2026-01-19T16:16:22.2298902Z Progress (1): 2.3/4.2 MB
2026-01-19T16:16:22.2302361Z Progress (1): 2.3/4.2 MB
2026-01-19T16:16:22.2305138Z Progress (1): 2.3/4.2 MB
2026-01-19T16:16:22.2328619Z Progress (1): 2.3/4.2 MB
2026-01-19T16:16:22.2329559Z Progress (1): 2.4/4.2 MB
2026-01-19T16:16:22.2329893Z Progress (1): 2.4/4.2 MB
2026-01-19T16:16:22.2330184Z Progress (1): 2.4/4.2 MB
2026-01-19T16:16:22.2330487Z Progress (2): 2.4/4.2 MB | 0/8.4 MB
2026-01-19T16:16:22.2330804Z Progress (2): 2.4/4.2 MB | 0/8.4 MB
2026-01-19T16:16:22.2331136Z Progress (2): 2.4/4.2 MB | 0/8.4 MB
2026-01-19T16:16:22.2331447Z Progress (2): 2.4/4.2 MB | 0/8.4 MB
2026-01-19T16:16:22.2331779Z Progress (2): 2.4/4.2 MB | 0/8.4 MB
2026-01-19T16:16:22.2372430Z Progress (2): 2.4/4.2 MB | 0/8.4 MB
2026-01-19T16:16:22.2372809Z Progress (2): 2.4/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2373134Z Progress (2): 2.4/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2373456Z Progress (2): 2.4/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2373761Z Progress (2): 2.4/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2374100Z Progress (2): 2.4/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2374429Z Progress (2): 2.4/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2374761Z Progress (2): 2.4/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2375077Z Progress (2): 2.5/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2375389Z Progress (2): 2.5/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2375691Z Progress (2): 2.5/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2376012Z Progress (2): 2.5/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2376339Z Progress (2): 2.5/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2376829Z Progress (2): 2.5/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2377155Z Progress (2): 2.6/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2377479Z Progress (2): 2.6/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2377820Z Progress (2): 2.6/4.2 MB | 0.1/8.4 MB
2026-01-19T16:16:22.2384601Z Progress (2): 2.6/4.2 MB | 0.2/8.4 MB
2026-01-19T16:16:22.2419430Z Progress (2): 2.6/4.2 MB | 0.2/8.4 MB
2026-01-19T16:16:22.2420247Z Progress (2): 2.6/4.2 MB | 0.2/8.4 MB
2026-01-19T16:16:22.2421003Z Progress (2): 2.6/4.2 MB | 0.2/8.4 MB
2026-01-19T16:16:22.2421535Z Progress (3): 2.6/4.2 MB | 0.2/8.4 MB | 7.7/54 kB
2026-01-19T16:16:22.2421926Z Progress (3): 2.6/4.2 MB | 0.2/8.4 MB | 16/54 kB 
2026-01-19T16:16:22.2422279Z Progress (3): 2.6/4.2 MB | 0.2/8.4 MB | 16/54 kB
2026-01-19T16:16:22.2422615Z Progress (3): 2.6/4.2 MB | 0.2/8.4 MB | 16/54 kB
2026-01-19T16:16:22.2422941Z Progress (3): 2.6/4.2 MB | 0.2/8.4 MB | 32/54 kB
2026-01-19T16:16:22.2423282Z Progress (3): 2.6/4.2 MB | 0.2/8.4 MB | 49/54 kB
2026-01-19T16:16:22.2423764Z Progress (3): 2.6/4.2 MB | 0.2/8.4 MB | 49/54 kB
2026-01-19T16:16:22.2424105Z Progress (3): 2.6/4.2 MB | 0.2/8.4 MB | 54 kB   
2026-01-19T16:16:22.2424445Z Progress (3): 2.6/4.2 MB | 0.2/8.4 MB | 54 kB
2026-01-19T16:16:22.2424756Z                                              
2026-01-19T16:16:22.2425162Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-exec/1.3/commons-exec-1.3.jar (54 kB at 97 kB/s)
2026-01-19T16:16:22.2425596Z Progress (2): 2.6/4.2 MB | 0.2/8.4 MB
2026-01-19T16:16:22.2425919Z Progress (2): 2.7/4.2 MB | 0.2/8.4 MB
2026-01-19T16:16:22.2426274Z Progress (2): 2.7/4.2 MB | 0.3/8.4 MB
2026-01-19T16:16:22.2426755Z Progress (2): 2.7/4.2 MB | 0.3/8.4 MB
2026-01-19T16:16:22.2483815Z Progress (2): 2.7/4.2 MB | 0.3/8.4 MB
2026-01-19T16:16:22.2484196Z Progress (2): 2.7/4.2 MB | 0.3/8.4 MB
2026-01-19T16:16:22.2484604Z Progress (2): 2.7/4.2 MB | 0.3/8.4 MB
2026-01-19T16:16:22.2484917Z Progress (2): 2.7/4.2 MB | 0.3/8.4 MB
2026-01-19T16:16:22.2485249Z Progress (2): 2.7/4.2 MB | 0.3/8.4 MB
2026-01-19T16:16:22.2485551Z Progress (2): 2.7/4.2 MB | 0.3/8.4 MB
2026-01-19T16:16:22.2485853Z Progress (2): 2.7/4.2 MB | 0.3/8.4 MB
2026-01-19T16:16:22.2486179Z Progress (2): 2.7/4.2 MB | 0.4/8.4 MB
2026-01-19T16:16:22.2486667Z Progress (2): 2.7/4.2 MB | 0.4/8.4 MB
2026-01-19T16:16:22.2486990Z Progress (2): 2.7/4.2 MB | 0.4/8.4 MB
2026-01-19T16:16:22.2487294Z Progress (2): 2.7/4.2 MB | 0.4/8.4 MB
2026-01-19T16:16:22.2487604Z Progress (2): 2.7/4.2 MB | 0.4/8.4 MB
2026-01-19T16:16:22.2487888Z                                      
2026-01-19T16:16:22.2488251Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar
2026-01-19T16:16:22.2488649Z Progress (3): 2.7/4.2 MB | 0.4/8.4 MB | 7.7/23 kB
2026-01-19T16:16:22.2488985Z Progress (3): 2.7/4.2 MB | 0.4/8.4 MB | 12/23 kB 
2026-01-19T16:16:22.2489335Z Progress (3): 2.7/4.2 MB | 0.4/8.4 MB | 23 kB   
2026-01-19T16:16:22.2489674Z Progress (3): 2.7/4.2 MB | 0.4/8.4 MB | 23 kB
2026-01-19T16:16:22.2490005Z Progress (3): 2.7/4.2 MB | 0.4/8.4 MB | 23 kB
2026-01-19T16:16:22.2494002Z Progress (3): 2.8/4.2 MB | 0.4/8.4 MB | 23 kB
2026-01-19T16:16:22.2494386Z Progress (3): 2.8/4.2 MB | 0.4/8.4 MB | 23 kB
2026-01-19T16:16:22.2494713Z Progress (3): 2.8/4.2 MB | 0.4/8.4 MB | 23 kB
2026-01-19T16:16:22.2495047Z Progress (3): 2.8/4.2 MB | 0.4/8.4 MB | 23 kB
2026-01-19T16:16:22.2495381Z Progress (3): 2.8/4.2 MB | 0.4/8.4 MB | 23 kB
2026-01-19T16:16:22.2495704Z Progress (3): 2.8/4.2 MB | 0.4/8.4 MB | 23 kB
2026-01-19T16:16:22.2496040Z Progress (3): 2.9/4.2 MB | 0.4/8.4 MB | 23 kB
2026-01-19T16:16:22.2496342Z                                              
2026-01-19T16:16:22.2499219Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-os/4.13.0/selenium-os-4.13.0.jar (23 kB at 41 kB/s)
2026-01-19T16:16:22.2499795Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.14.0/commons-io-2.14.0.jar
2026-01-19T16:16:22.2502997Z Progress (2): 2.9/4.2 MB | 0.4/8.4 MB
2026-01-19T16:16:22.2507691Z Progress (3): 2.9/4.2 MB | 0.4/8.4 MB | 7.7/192 kB
2026-01-19T16:16:22.2511651Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 7.7/192 kB
2026-01-19T16:16:22.2514646Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 16/192 kB 
2026-01-19T16:16:22.2518203Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 32/192 kB
2026-01-19T16:16:22.2524852Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 32/192 kB
2026-01-19T16:16:22.2528652Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 32/192 kB
2026-01-19T16:16:22.2529035Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2592077Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2592484Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2592817Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2593153Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2593497Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2594006Z Progress (3): 2.9/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2594351Z Progress (3): 3.0/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2594705Z Progress (3): 3.0/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2595043Z Progress (3): 3.0/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2595394Z Progress (3): 3.0/4.2 MB | 0.5/8.4 MB | 49/192 kB
2026-01-19T16:16:22.2595730Z Progress (3): 3.0/4.2 MB | 0.5/8.4 MB | 65/192 kB
2026-01-19T16:16:22.2596075Z Progress (3): 3.0/4.2 MB | 0.5/8.4 MB | 81/192 kB
2026-01-19T16:16:22.2596420Z Progress (3): 3.0/4.2 MB | 0.5/8.4 MB | 98/192 kB
2026-01-19T16:16:22.2596990Z Progress (3): 3.0/4.2 MB | 0.5/8.4 MB | 98/192 kB
2026-01-19T16:16:22.2597337Z Progress (3): 3.0/4.2 MB | 0.5/8.4 MB | 98/192 kB
2026-01-19T16:16:22.2597683Z Progress (3): 3.0/4.2 MB | 0.5/8.4 MB | 98/192 kB
2026-01-19T16:16:22.2598028Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 98/192 kB
2026-01-19T16:16:22.2598376Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 98/192 kB
2026-01-19T16:16:22.2598726Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 98/192 kB
2026-01-19T16:16:22.2599076Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 114/192 kB
2026-01-19T16:16:22.2599424Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 131/192 kB
2026-01-19T16:16:22.2599778Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 147/192 kB
2026-01-19T16:16:22.2600129Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 163/192 kB
2026-01-19T16:16:22.2600485Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 180/192 kB
2026-01-19T16:16:22.2609861Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 192 kB    
2026-01-19T16:16:22.2629567Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 192 kB
2026-01-19T16:16:22.2635483Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 192 kB
2026-01-19T16:16:22.2636092Z Progress (3): 3.0/4.2 MB | 0.6/8.4 MB | 192 kB
2026-01-19T16:16:22.2636728Z Progress (3): 3.1/4.2 MB | 0.6/8.4 MB | 192 kB
2026-01-19T16:16:22.2637180Z Progress (3): 3.1/4.2 MB | 0.6/8.4 MB | 192 kB
2026-01-19T16:16:22.2637663Z Progress (4): 3.1/4.2 MB | 0.6/8.4 MB | 192 kB | 7.7/283 kB
2026-01-19T16:16:22.2638438Z Progress (4): 3.1/4.2 MB | 0.6/8.4 MB | 192 kB | 16/283 kB 
2026-01-19T16:16:22.2639625Z Progress (4): 3.1/4.2 MB | 0.6/8.4 MB | 192 kB | 29/283 kB
2026-01-19T16:16:22.2681309Z Progress (4): 3.1/4.2 MB | 0.6/8.4 MB | 192 kB | 45/283 kB
2026-01-19T16:16:22.2681730Z Progress (4): 3.1/4.2 MB | 0.6/8.4 MB | 192 kB | 45/283 kB
2026-01-19T16:16:22.2684296Z Progress (4): 3.1/4.2 MB | 0.6/8.4 MB | 192 kB | 45/283 kB
2026-01-19T16:16:22.2684693Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 45/283 kB
2026-01-19T16:16:22.2685075Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 45/283 kB
2026-01-19T16:16:22.2685398Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 45/283 kB
2026-01-19T16:16:22.2685723Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 45/283 kB
2026-01-19T16:16:22.2686083Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 61/283 kB
2026-01-19T16:16:22.2688242Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 78/283 kB
2026-01-19T16:16:22.2688651Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 94/283 kB
2026-01-19T16:16:22.2688995Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 111/283 kB
2026-01-19T16:16:22.2689370Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 127/283 kB
2026-01-19T16:16:22.2696920Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 143/283 kB
2026-01-19T16:16:22.2697478Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 160/283 kB
2026-01-19T16:16:22.2697836Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 176/283 kB
2026-01-19T16:16:22.2698184Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 176/283 kB
2026-01-19T16:16:22.2698519Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 176/283 kB
2026-01-19T16:16:22.2698875Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 176/283 kB
2026-01-19T16:16:22.2699253Z Progress (4): 3.1/4.2 MB | 0.7/8.4 MB | 192 kB | 176/283 kB
2026-01-19T16:16:22.2699549Z                                                            
2026-01-19T16:16:22.2699962Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-support/4.13.0/selenium-support-4.13.0.jar (192 kB at 326 kB/s)
2026-01-19T16:16:22.2700557Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.9/slf4j-api-2.0.9.jar
2026-01-19T16:16:22.2700975Z Progress (3): 3.1/4.2 MB | 0.7/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2701312Z Progress (3): 3.1/4.2 MB | 0.7/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2709446Z Progress (3): 3.1/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2710097Z Progress (3): 3.2/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2710587Z Progress (3): 3.2/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2711018Z Progress (3): 3.2/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2711465Z Progress (3): 3.2/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2712830Z Progress (3): 3.2/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2714957Z Progress (3): 3.2/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2716046Z Progress (3): 3.3/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2716386Z Progress (3): 3.3/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2738416Z Progress (3): 3.3/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2739120Z Progress (3): 3.3/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2739575Z Progress (3): 3.3/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2740049Z Progress (3): 3.3/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2740485Z Progress (3): 3.3/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2740930Z Progress (3): 3.3/4.2 MB | 0.8/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2742596Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2749736Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 176/283 kB
2026-01-19T16:16:22.2750409Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 193/283 kB
2026-01-19T16:16:22.2751015Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 209/283 kB
2026-01-19T16:16:22.2751550Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 225/283 kB
2026-01-19T16:16:22.2752088Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 242/283 kB
2026-01-19T16:16:22.2752673Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 258/283 kB
2026-01-19T16:16:22.2753955Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 274/283 kB
2026-01-19T16:16:22.2754502Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 283 kB    
2026-01-19T16:16:22.2754966Z                                               
2026-01-19T16:16:22.2756115Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar (283 kB at 477 kB/s)
2026-01-19T16:16:22.2756857Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-java/4.16.1/selenium-java-4.16.1.jar
2026-01-19T16:16:22.2777922Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 7.7/494 kB
2026-01-19T16:16:22.2778483Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 16/494 kB 
2026-01-19T16:16:22.2778935Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 32/494 kB
2026-01-19T16:16:22.2779383Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 49/494 kB
2026-01-19T16:16:22.2779839Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 65/494 kB
2026-01-19T16:16:22.2780322Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 81/494 kB
2026-01-19T16:16:22.2790506Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2791238Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2791942Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2792497Z Progress (3): 3.3/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2793297Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2793915Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2845482Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2897033Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2897655Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2898148Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2898582Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2899167Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2899704Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2900202Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 98/494 kB
2026-01-19T16:16:22.2900619Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 114/494 kB
2026-01-19T16:16:22.2901083Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 131/494 kB
2026-01-19T16:16:22.2901611Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 147/494 kB
2026-01-19T16:16:22.2902115Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 163/494 kB
2026-01-19T16:16:22.2902580Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 180/494 kB
2026-01-19T16:16:22.2902993Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 196/494 kB
2026-01-19T16:16:22.2903646Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 213/494 kB
2026-01-19T16:16:22.2904117Z Progress (3): 3.4/4.2 MB | 0.9/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2904558Z Progress (3): 3.4/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2904973Z Progress (3): 3.4/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2905502Z Progress (3): 3.4/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2905977Z Progress (3): 3.4/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2906408Z Progress (3): 3.5/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2907154Z Progress (3): 3.5/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2907745Z Progress (3): 3.5/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2908289Z Progress (3): 3.5/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2908800Z Progress (3): 3.5/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2909310Z Progress (3): 3.5/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2909921Z Progress (3): 3.5/4.2 MB | 1.0/8.4 MB | 229/494 kB
2026-01-19T16:16:22.2910479Z Progress (3): 3.5/4.2 MB | 1.0/8.4 MB | 245/494 kB
2026-01-19T16:16:22.2911083Z Progress (4): 3.5/4.2 MB | 1.0/8.4 MB | 245/494 kB | 7.7/65 kB
2026-01-19T16:16:22.2915551Z Progress (4): 3.5/4.2 MB | 1.0/8.4 MB | 245/494 kB | 16/65 kB 
2026-01-19T16:16:22.2915947Z Progress (4): 3.5/4.2 MB | 1.0/8.4 MB | 245/494 kB | 32/65 kB
2026-01-19T16:16:22.2916340Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 245/494 kB | 32/65 kB
2026-01-19T16:16:22.2916893Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 262/494 kB | 32/65 kB
2026-01-19T16:16:22.2917213Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 262/494 kB | 32/65 kB
2026-01-19T16:16:22.2917550Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 262/494 kB | 48/65 kB
2026-01-19T16:16:22.2926988Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 262/494 kB | 48/65 kB
2026-01-19T16:16:22.2927379Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 278/494 kB | 48/65 kB
2026-01-19T16:16:22.2927713Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 278/494 kB | 48/65 kB
2026-01-19T16:16:22.2928059Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 278/494 kB | 65 kB   
2026-01-19T16:16:22.2928459Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 278/494 kB | 65 kB
2026-01-19T16:16:22.2928805Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 278/494 kB | 65 kB
2026-01-19T16:16:22.2929147Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 294/494 kB | 65 kB
2026-01-19T16:16:22.2929483Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 311/494 kB | 65 kB
2026-01-19T16:16:22.2929802Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 327/494 kB | 65 kB
2026-01-19T16:16:22.2930148Z Progress (4): 3.5/4.2 MB | 1.1/8.4 MB | 344/494 kB | 65 kB
2026-01-19T16:16:22.2930488Z Progress (4): 3.6/4.2 MB | 1.1/8.4 MB | 344/494 kB | 65 kB
2026-01-19T16:16:22.2930929Z Progress (4): 3.6/4.2 MB | 1.1/8.4 MB | 344/494 kB | 65 kB
2026-01-19T16:16:22.2931278Z Progress (4): 3.6/4.2 MB | 1.1/8.4 MB | 344/494 kB | 65 kB
2026-01-19T16:16:22.2931593Z Progress (4): 3.6/4.2 MB | 1.1/8.4 MB | 344/494 kB | 65 kB
2026-01-19T16:16:22.2931887Z                                                           
2026-01-19T16:16:22.2932280Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/2.0.9/slf4j-api-2.0.9.jar (65 kB at 106 kB/s)
2026-01-19T16:16:22.2932849Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chrome-driver/4.16.1/selenium-chrome-driver-4.16.1.jar
2026-01-19T16:16:22.2958443Z Progress (3): 3.6/4.2 MB | 1.1/8.4 MB | 344/494 kB
2026-01-19T16:16:22.2960069Z Progress (3): 3.6/4.2 MB | 1.1/8.4 MB | 344/494 kB
2026-01-19T16:16:22.2960662Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 344/494 kB
2026-01-19T16:16:22.2961116Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 344/494 kB
2026-01-19T16:16:22.2961596Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 344/494 kB
2026-01-19T16:16:22.2962220Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 344/494 kB
2026-01-19T16:16:22.2963351Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 344/494 kB
2026-01-19T16:16:22.2963690Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 344/494 kB
2026-01-19T16:16:22.2963995Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 360/494 kB
2026-01-19T16:16:22.2964338Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 376/494 kB
2026-01-19T16:16:22.2964673Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 393/494 kB
2026-01-19T16:16:22.2965014Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 409/494 kB
2026-01-19T16:16:22.2965350Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 426/494 kB
2026-01-19T16:16:22.2965683Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 442/494 kB
2026-01-19T16:16:22.2965990Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 458/494 kB
2026-01-19T16:16:22.2966338Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 475/494 kB
2026-01-19T16:16:22.2979492Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 491/494 kB
2026-01-19T16:16:22.2983586Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 491/494 kB
2026-01-19T16:16:22.2985350Z Progress (3): 3.6/4.2 MB | 1.2/8.4 MB | 491/494 kB
2026-01-19T16:16:22.2987915Z Progress (3): 3.7/4.2 MB | 1.2/8.4 MB | 491/494 kB
2026-01-19T16:16:22.2997810Z Progress (3): 3.7/4.2 MB | 1.2/8.4 MB | 491/494 kB
2026-01-19T16:16:22.2998465Z Progress (3): 3.7/4.2 MB | 1.2/8.4 MB | 491/494 kB
2026-01-19T16:16:22.2998922Z Progress (3): 3.7/4.2 MB | 1.2/8.4 MB | 491/494 kB
2026-01-19T16:16:22.2999370Z Progress (3): 3.7/4.2 MB | 1.2/8.4 MB | 491/494 kB
2026-01-19T16:16:22.3000349Z Progress (3): 3.7/4.2 MB | 1.2/8.4 MB | 491/494 kB
2026-01-19T16:16:22.3000889Z Progress (3): 3.8/4.2 MB | 1.2/8.4 MB | 491/494 kB
2026-01-19T16:16:22.3001370Z Progress (4): 3.8/4.2 MB | 1.2/8.4 MB | 491/494 kB | 545 B
2026-01-19T16:16:22.3002021Z                                                           
2026-01-19T16:16:22.3003213Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-java/4.16.1/selenium-java-4.16.1.jar (545 B at 881 B/s)
2026-01-19T16:16:22.3003971Z Progress (3): 3.8/4.2 MB | 1.3/8.4 MB | 491/494 kB
2026-01-19T16:16:22.3004560Z Progress (3): 3.8/4.2 MB | 1.3/8.4 MB | 491/494 kB
2026-01-19T16:16:22.3005125Z Progress (3): 3.8/4.2 MB | 1.3/8.4 MB | 491/494 kB
2026-01-19T16:16:22.3005660Z                                                   
2026-01-19T16:16:22.3007522Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chromium-driver/4.16.1/selenium-chromium-driver-4.16.1.jar
2026-01-19T16:16:22.3008192Z Progress (3): 3.8/4.2 MB | 1.3/8.4 MB | 494 kB
2026-01-19T16:16:22.3008818Z Progress (3): 3.8/4.2 MB | 1.3/8.4 MB | 494 kB
2026-01-19T16:16:22.3009268Z Progress (3): 3.8/4.2 MB | 1.3/8.4 MB | 494 kB
2026-01-19T16:16:22.3009679Z                                               
2026-01-19T16:16:22.3010900Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.14.0/commons-io-2.14.0.jar (494 kB at 797 kB/s)
2026-01-19T16:16:22.3013492Z Progress (2): 3.8/4.2 MB | 1.3/8.4 MB
2026-01-19T16:16:22.3016934Z Progress (2): 3.8/4.2 MB | 1.3/8.4 MB
2026-01-19T16:16:22.3018788Z Progress (2): 3.8/4.2 MB | 1.3/8.4 MB
2026-01-19T16:16:22.3020835Z Progress (2): 3.8/4.2 MB | 1.3/8.4 MB
2026-01-19T16:16:22.3021165Z                                      
2026-01-19T16:16:22.3021582Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v118/4.16.1/selenium-devtools-v118-4.16.1.jar
2026-01-19T16:16:22.3048106Z Progress (2): 3.8/4.2 MB | 1.3/8.4 MB
2026-01-19T16:16:22.3048907Z Progress (2): 3.8/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3049804Z Progress (2): 3.8/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3050513Z Progress (2): 3.8/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3051231Z Progress (2): 3.8/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3052886Z Progress (2): 3.8/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3053621Z Progress (2): 3.9/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3054313Z Progress (2): 3.9/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3055719Z Progress (2): 3.9/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3056253Z Progress (2): 3.9/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3056869Z Progress (2): 3.9/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3057357Z Progress (2): 3.9/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3085011Z Progress (2): 3.9/4.2 MB | 1.4/8.4 MB
2026-01-19T16:16:22.3089955Z Progress (2): 3.9/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3094198Z Progress (2): 3.9/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3098108Z Progress (2): 3.9/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3101775Z Progress (2): 3.9/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3105431Z Progress (2): 3.9/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3110613Z Progress (2): 3.9/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3111207Z Progress (2): 3.9/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3111807Z Progress (2): 4.0/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3112376Z Progress (2): 4.0/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3113038Z Progress (2): 4.0/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3114087Z Progress (2): 4.0/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3116138Z Progress (2): 4.0/4.2 MB | 1.5/8.4 MB
2026-01-19T16:16:22.3116896Z Progress (3): 4.0/4.2 MB | 1.5/8.4 MB | 7.4/15 kB
2026-01-19T16:16:22.3117395Z Progress (3): 4.0/4.2 MB | 1.5/8.4 MB | 15 kB    
2026-01-19T16:16:22.3117869Z Progress (3): 4.0/4.2 MB | 1.5/8.4 MB | 15 kB
2026-01-19T16:16:22.3118422Z Progress (3): 4.0/4.2 MB | 1.6/8.4 MB | 15 kB
2026-01-19T16:16:22.3118902Z Progress (3): 4.0/4.2 MB | 1.6/8.4 MB | 15 kB
2026-01-19T16:16:22.3119413Z Progress (3): 4.0/4.2 MB | 1.6/8.4 MB | 15 kB
2026-01-19T16:16:22.3119925Z Progress (3): 4.0/4.2 MB | 1.6/8.4 MB | 15 kB
2026-01-19T16:16:22.3121212Z Progress (3): 4.0/4.2 MB | 1.6/8.4 MB | 15 kB
2026-01-19T16:16:22.3121575Z Progress (3): 4.0/4.2 MB | 1.6/8.4 MB | 15 kB
2026-01-19T16:16:22.3121910Z Progress (3): 4.0/4.2 MB | 1.7/8.4 MB | 15 kB
2026-01-19T16:16:22.3122245Z Progress (3): 4.0/4.2 MB | 1.7/8.4 MB | 15 kB
2026-01-19T16:16:22.3122568Z                                              
2026-01-19T16:16:22.3123008Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chrome-driver/4.16.1/selenium-chrome-driver-4.16.1.jar (15 kB at 24 kB/s)
2026-01-19T16:16:22.3123619Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v119/4.16.1/selenium-devtools-v119-4.16.1.jar
2026-01-19T16:16:22.3179076Z Progress (2): 4.0/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3179736Z Progress (2): 4.1/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3180225Z Progress (2): 4.1/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3180700Z Progress (2): 4.1/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3181168Z Progress (2): 4.1/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3181645Z Progress (2): 4.1/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3182121Z Progress (2): 4.1/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3182578Z Progress (2): 4.2/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3183062Z Progress (2): 4.2/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3183676Z Progress (2): 4.2/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3184153Z Progress (2): 4.2/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3184613Z Progress (2): 4.2/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3185083Z Progress (2): 4.2/4.2 MB | 1.7/8.4 MB
2026-01-19T16:16:22.3185542Z Progress (2): 4.2/4.2 MB | 1.8/8.4 MB
2026-01-19T16:16:22.3186023Z Progress (2): 4.2/4.2 MB | 1.8/8.4 MB
2026-01-19T16:16:22.3186692Z Progress (2): 4.2/4.2 MB | 1.8/8.4 MB
2026-01-19T16:16:22.3207250Z Progress (2): 4.2/4.2 MB | 1.8/8.4 MB
2026-01-19T16:16:22.3209682Z Progress (2): 4.2 MB | 1.8/8.4 MB    
2026-01-19T16:16:22.3210243Z                                  
2026-01-19T16:16:22.3210916Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.14.5/byte-buddy-1.14.5.jar (4.2 MB at 6.5 MB/s)
2026-01-19T16:16:22.3212197Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v120/4.16.1/selenium-devtools-v120-4.16.1.jar
2026-01-19T16:16:22.3212887Z Progress (1): 1.8/8.4 MB
2026-01-19T16:16:22.3215203Z Progress (1): 1.8/8.4 MB
2026-01-19T16:16:22.3221369Z Progress (1): 1.9/8.4 MB
2026-01-19T16:16:22.3222365Z Progress (1): 1.9/8.4 MB
2026-01-19T16:16:22.3230575Z Progress (2): 1.9/8.4 MB | 7.7/37 kB
2026-01-19T16:16:22.3231769Z Progress (2): 1.9/8.4 MB | 7.7/37 kB
2026-01-19T16:16:22.3234398Z Progress (2): 1.9/8.4 MB | 12/37 kB 
2026-01-19T16:16:22.3236979Z Progress (2): 1.9/8.4 MB | 29/37 kB
2026-01-19T16:16:22.3238937Z Progress (2): 1.9/8.4 MB | 29/37 kB
2026-01-19T16:16:22.3243073Z Progress (2): 1.9/8.4 MB | 37 kB   
2026-01-19T16:16:22.3243511Z                                 
2026-01-19T16:16:22.3244116Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-chromium-driver/4.16.1/selenium-chromium-driver-4.16.1.jar (37 kB at 57 kB/s)
2026-01-19T16:16:22.3278217Z Progress (1): 1.9/8.4 MB
2026-01-19T16:16:22.3278761Z                         
2026-01-19T16:16:22.3279399Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v85/4.16.1/selenium-devtools-v85-4.16.1.jar
2026-01-19T16:16:22.3280641Z Progress (1): 1.9/8.4 MB
2026-01-19T16:16:22.3281126Z Progress (1): 1.9/8.4 MB
2026-01-19T16:16:22.3281594Z Progress (1): 2.0/8.4 MB
2026-01-19T16:16:22.3282011Z Progress (1): 2.0/8.4 MB
2026-01-19T16:16:22.3282600Z Progress (2): 2.0/8.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3288452Z Progress (2): 2.0/8.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3290958Z Progress (2): 2.0/8.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3293548Z Progress (2): 2.0/8.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3296415Z Progress (2): 2.0/8.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3298662Z Progress (2): 2.0/8.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3300704Z Progress (2): 2.0/8.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3303073Z Progress (2): 2.0/8.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3306737Z Progress (2): 2.0/8.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3328211Z Progress (2): 2.1/8.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3329597Z Progress (2): 2.1/8.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3330408Z Progress (2): 2.1/8.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3331795Z Progress (2): 2.1/8.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3334155Z Progress (2): 2.1/8.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3334923Z Progress (2): 2.1/8.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3335625Z Progress (2): 2.1/8.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3337196Z Progress (2): 2.1/8.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3338001Z Progress (2): 2.1/8.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3338705Z Progress (3): 2.1/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3339466Z Progress (3): 2.1/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3359876Z Progress (3): 2.1/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3364427Z Progress (3): 2.1/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3370615Z Progress (3): 2.2/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3372429Z Progress (3): 2.2/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3374427Z Progress (3): 2.2/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3376209Z Progress (3): 2.2/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3378710Z Progress (3): 2.2/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3380923Z Progress (3): 2.2/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3382668Z Progress (3): 2.3/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3388821Z Progress (3): 2.3/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3389408Z Progress (3): 2.3/8.4 MB | 0.1/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3389873Z Progress (3): 2.3/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3391248Z Progress (3): 2.3/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3391746Z Progress (3): 2.3/8.4 MB | 0.1/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3392072Z Progress (3): 2.3/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3392406Z Progress (3): 2.3/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3392740Z Progress (3): 2.3/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3393091Z Progress (3): 2.3/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3394523Z Progress (3): 2.3/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3395280Z Progress (3): 2.3/8.4 MB | 0.2/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3395992Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3419083Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3419644Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3420106Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3420539Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3420997Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3421413Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3421868Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3422392Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3422854Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3423345Z Progress (3): 2.3/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3423765Z Progress (3): 2.4/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3424237Z Progress (3): 2.4/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3438988Z Progress (3): 2.4/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3442998Z Progress (3): 2.4/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3446755Z Progress (3): 2.4/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3447284Z Progress (3): 2.4/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3447791Z Progress (3): 2.4/8.4 MB | 0.3/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3451261Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3453111Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3453830Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3456098Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3462060Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3463913Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3477501Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3478467Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3479265Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3479744Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.2/1.4 MB
2026-01-19T16:16:22.3480317Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-19T16:16:22.3482397Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-19T16:16:22.3483478Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-19T16:16:22.3485167Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-19T16:16:22.3486320Z Progress (3): 2.4/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-19T16:16:22.3487160Z Progress (3): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-19T16:16:22.3487699Z Progress (3): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-19T16:16:22.3488315Z Progress (3): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-19T16:16:22.3489062Z Progress (3): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-19T16:16:22.3507826Z Progress (3): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB
2026-01-19T16:16:22.3508688Z Progress (4): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3509198Z Progress (4): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3509765Z Progress (4): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3510872Z Progress (4): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0/1.4 MB
2026-01-19T16:16:22.3511428Z Progress (4): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3512135Z Progress (4): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3521322Z Progress (4): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB
2026-01-19T16:16:22.3522486Z Progress (5): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0/1.0 MB
2026-01-19T16:16:22.3522971Z Progress (5): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0/1.0 MB
2026-01-19T16:16:22.3523533Z Progress (5): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0/1.0 MB
2026-01-19T16:16:22.3524645Z Progress (5): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0/1.0 MB
2026-01-19T16:16:22.3525186Z Progress (5): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3525728Z Progress (5): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3538166Z Progress (5): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3539841Z Progress (5): 2.5/8.4 MB | 0.4/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3540425Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3543221Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3543739Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3545319Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3545704Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3559017Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3559935Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3562040Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3563396Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3564145Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3564925Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3565665Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3587902Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3588636Z Progress (5): 2.5/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3589190Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3589702Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3590252Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3590752Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3591276Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3604081Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3607547Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3608147Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3608872Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.1/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3609565Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3610390Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3610984Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3611449Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3640363Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3641039Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3641612Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3642356Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.1/1.0 MB
2026-01-19T16:16:22.3642858Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3643417Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3644053Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3645214Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3645607Z Progress (5): 2.6/8.4 MB | 0.5/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3645980Z Progress (5): 2.6/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3646340Z Progress (5): 2.6/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3646905Z Progress (5): 2.6/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3647271Z Progress (5): 2.6/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3647658Z Progress (5): 2.6/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3648045Z Progress (5): 2.6/8.4 MB | 0.6/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3660861Z Progress (5): 2.6/8.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3661468Z Progress (5): 2.6/8.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3662599Z Progress (5): 2.6/8.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3662975Z Progress (5): 2.6/8.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3663587Z Progress (5): 2.6/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3663955Z Progress (5): 2.6/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3664323Z Progress (5): 2.6/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3664675Z Progress (5): 2.6/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3678668Z Progress (5): 2.6/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3684429Z Progress (5): 2.7/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3684854Z Progress (5): 2.7/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3685222Z Progress (5): 2.7/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3685607Z Progress (5): 2.7/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3685958Z Progress (5): 2.7/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3686320Z Progress (5): 2.7/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3686866Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3698464Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3701880Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.2/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3702737Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3703257Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3704462Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3705000Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3706434Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3708117Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3711667Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.2/1.0 MB
2026-01-19T16:16:22.3712066Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3712615Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3715093Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3768327Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3769023Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3769597Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3770099Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3770561Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3771038Z Progress (5): 2.8/8.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3771488Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3772610Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3772995Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3773333Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3773714Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3774092Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3774458Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3774822Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3775185Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3775951Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3776325Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3776867Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3798260Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3798706Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.3/1.0 MB
2026-01-19T16:16:22.3799129Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3799533Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3799931Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3800368Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3800764Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3801165Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3801539Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3801897Z Progress (5): 2.8/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3802281Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3802653Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3803159Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3803539Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3804163Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3804838Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3805212Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.3/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3822058Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3822781Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3824676Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3826169Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3828098Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3831930Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3834663Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3836185Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3845144Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3847198Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3847944Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.4/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3848792Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.7/1.4 MB | 0.5/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3850301Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3850689Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3851050Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3851410Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3851780Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3852146Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3852498Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.4/1.0 MB
2026-01-19T16:16:22.3852872Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3853218Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3853586Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3887512Z Progress (5): 2.9/8.4 MB | 0.8/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3896158Z Progress (5): 2.9/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3896931Z Progress (5): 2.9/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3897436Z Progress (5): 2.9/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3898285Z Progress (5): 2.9/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3898782Z Progress (5): 2.9/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3899237Z Progress (5): 2.9/8.4 MB | 0.9/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3899956Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3900762Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3901232Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3901722Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3902195Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3902796Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3903250Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3903776Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3904235Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.5/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3904708Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3905154Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3905643Z Progress (5): 2.9/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3906229Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3906905Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3907461Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3908015Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3908539Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3909145Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3909745Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3910247Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3910841Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.8/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3911330Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.5/1.0 MB
2026-01-19T16:16:22.3911858Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3912360Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3912900Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3913363Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3913837Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3914283Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3914768Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3915306Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3915831Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3916279Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3916952Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.6/1.0 MB
2026-01-19T16:16:22.3917421Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 0.9/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3938202Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3939022Z Progress (5): 3.0/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3939781Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3940558Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3941295Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3942033Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3942774Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3943519Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3944262Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3944988Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.6/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3945813Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3946751Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3953640Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3954807Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3955180Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3955544Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3956054Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3956411Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3956968Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3957329Z Progress (5): 3.1/8.4 MB | 1.0/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3957693Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3958041Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3958409Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3977871Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.3978524Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.4015494Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.4016162Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.4016864Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.4017347Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.4017845Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.4018298Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.4018792Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.4019253Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.4019723Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.7/1.0 MB
2026-01-19T16:16:22.4020173Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4020644Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.0/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4021120Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4021575Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4022104Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4022582Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4024469Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4025067Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4025532Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4026014Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4026463Z Progress (5): 3.1/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4027526Z Progress (5): 3.2/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4028377Z Progress (5): 3.2/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4028937Z Progress (5): 3.2/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4029662Z Progress (5): 3.2/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4030134Z Progress (5): 3.2/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4030580Z Progress (5): 3.2/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4031057Z Progress (5): 3.3/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4031518Z Progress (5): 3.3/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4032620Z Progress (5): 3.3/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4033014Z Progress (5): 3.3/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4033497Z Progress (5): 3.3/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4058090Z Progress (5): 3.3/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4062976Z Progress (5): 3.3/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4063639Z Progress (5): 3.3/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4064127Z Progress (5): 3.3/8.4 MB | 1.1/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4064736Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4065412Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4065874Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4067110Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4067661Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4068142Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.7/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4068631Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.8/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4069091Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.8/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4069600Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.8/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4070062Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.8/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4070555Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.8/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4071006Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.8/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4071498Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4071968Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4072458Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4076640Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4081762Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4085247Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.8/1.0 MB
2026-01-19T16:16:22.4085758Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.9/1.0 MB
2026-01-19T16:16:22.4086254Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.9/1.0 MB
2026-01-19T16:16:22.4086935Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.9/1.0 MB
2026-01-19T16:16:22.4087775Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.9/1.0 MB
2026-01-19T16:16:22.4088253Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.9/1.0 MB
2026-01-19T16:16:22.4088746Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.9/1.0 MB
2026-01-19T16:16:22.4089238Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 0.9/1.0 MB
2026-01-19T16:16:22.4089749Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4090252Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4090886Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.1/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4138297Z Progress (5): 3.3/8.4 MB | 1.2/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4138858Z Progress (5): 3.3/8.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4139385Z Progress (5): 3.3/8.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4139849Z Progress (5): 3.3/8.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4140329Z Progress (5): 3.3/8.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4140865Z Progress (5): 3.3/8.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4141443Z Progress (5): 3.3/8.4 MB | 1.3/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4141910Z Progress (5): 3.3/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4143028Z Progress (5): 3.3/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4143424Z Progress (5): 3.3/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4143805Z Progress (5): 3.3/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4144162Z Progress (5): 3.4/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4144531Z Progress (5): 3.4/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4144894Z Progress (5): 3.4/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4145272Z Progress (5): 3.4/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4145655Z Progress (5): 3.4/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4146036Z Progress (5): 3.4/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4146404Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4146974Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4147319Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4147689Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4148055Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4148851Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 0.9/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4149224Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4149607Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4149981Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4150355Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4151248Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.2/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4151805Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4152183Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4176128Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4176949Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4177551Z Progress (5): 3.5/8.4 MB | 1.4/1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4178018Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB    
2026-01-19T16:16:22.4178491Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0/1.0 MB
2026-01-19T16:16:22.4178977Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0 MB    
2026-01-19T16:16:22.4179424Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0 MB
2026-01-19T16:16:22.4179886Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0 MB
2026-01-19T16:16:22.4180461Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0 MB
2026-01-19T16:16:22.4180974Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0 MB
2026-01-19T16:16:22.4181493Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.3/1.4 MB | 1.0/1.4 MB | 1.0 MB
2026-01-19T16:16:22.4181994Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.4/1.4 MB | 1.0/1.4 MB | 1.0 MB
2026-01-19T16:16:22.4182518Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.4/1.4 MB | 1.0/1.4 MB | 1.0 MB
2026-01-19T16:16:22.4183014Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.4/1.4 MB | 1.0/1.4 MB | 1.0 MB
2026-01-19T16:16:22.4215207Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.4/1.4 MB | 1.0/1.4 MB | 1.0 MB
2026-01-19T16:16:22.4219219Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.4/1.4 MB | 1.0/1.4 MB | 1.0 MB
2026-01-19T16:16:22.4222727Z Progress (5): 3.5/8.4 MB | 1.4 MB | 1.4 MB | 1.0/1.4 MB | 1.0 MB    
2026-01-19T16:16:22.4226169Z                                                                 
2026-01-19T16:16:22.4233319Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v85/4.16.1/selenium-devtools-v85-4.16.1.jar (1.0 MB at 1.4 MB/s)
2026-01-19T16:16:22.4238631Z Progress (4): 3.5/8.4 MB | 1.4 MB | 1.4 MB | 1.0/1.4 MB
2026-01-19T16:16:22.4239223Z                                                        
2026-01-19T16:16:22.4239768Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v119/4.16.1/selenium-devtools-v119-4.16.1.jar (1.4 MB at 1.9 MB/s)
2026-01-19T16:16:22.4240601Z Progress (3): 3.5/8.4 MB | 1.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4241042Z Progress (3): 3.5/8.4 MB | 1.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4241508Z Progress (3): 3.5/8.4 MB | 1.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4241924Z Progress (3): 3.5/8.4 MB | 1.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4242365Z Progress (3): 3.5/8.4 MB | 1.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4243297Z Progress (3): 3.5/8.4 MB | 1.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4243740Z                                               
2026-01-19T16:16:22.4244992Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v118/4.16.1/selenium-devtools-v118-4.16.1.jar (1.4 MB at 1.9 MB/s)
2026-01-19T16:16:22.4245571Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-edge-driver/4.16.1/selenium-edge-driver-4.16.1.jar
2026-01-19T16:16:22.4246004Z Progress (2): 3.5/8.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4246328Z Progress (2): 3.5/8.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4246822Z Progress (2): 3.5/8.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4247129Z Progress (2): 3.5/8.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4247482Z Progress (2): 3.6/8.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4247807Z Progress (2): 3.6/8.4 MB | 1.1/1.4 MB
2026-01-19T16:16:22.4248107Z                                      
2026-01-19T16:16:22.4248513Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-firefox-driver/4.16.1/selenium-firefox-driver-4.16.1.jar
2026-01-19T16:16:22.4249067Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-ie-driver/4.16.1/selenium-ie-driver-4.16.1.jar
2026-01-19T16:16:22.4249473Z Progress (2): 3.6/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4249805Z Progress (2): 3.6/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4250135Z Progress (2): 3.6/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4250449Z Progress (2): 3.6/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4250753Z Progress (2): 3.6/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4252105Z Progress (2): 3.6/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4253382Z Progress (2): 3.6/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4254098Z Progress (2): 3.6/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4254846Z Progress (2): 3.7/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4256043Z Progress (2): 3.7/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4258344Z Progress (2): 3.7/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4280923Z Progress (2): 3.7/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4283493Z Progress (2): 3.7/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4286074Z Progress (2): 3.7/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4288427Z Progress (2): 3.7/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4292797Z Progress (2): 3.7/8.4 MB | 1.2/1.4 MB
2026-01-19T16:16:22.4293125Z Progress (2): 3.7/8.4 MB | 1.3/1.4 MB
2026-01-19T16:16:22.4293455Z Progress (2): 3.7/8.4 MB | 1.3/1.4 MB
2026-01-19T16:16:22.4293803Z Progress (2): 3.7/8.4 MB | 1.3/1.4 MB
2026-01-19T16:16:22.4294128Z Progress (2): 3.7/8.4 MB | 1.3/1.4 MB
2026-01-19T16:16:22.4294433Z Progress (2): 3.7/8.4 MB | 1.3/1.4 MB
2026-01-19T16:16:22.4294745Z Progress (2): 3.8/8.4 MB | 1.3/1.4 MB
2026-01-19T16:16:22.4295194Z Progress (2): 3.8/8.4 MB | 1.3/1.4 MB
2026-01-19T16:16:22.4295493Z Progress (2): 3.8/8.4 MB | 1.3/1.4 MB
2026-01-19T16:16:22.4295792Z Progress (2): 3.8/8.4 MB | 1.3/1.4 MB
2026-01-19T16:16:22.4296141Z Progress (2): 3.8/8.4 MB | 1.3/1.4 MB
2026-01-19T16:16:22.4317813Z Progress (2): 3.8/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4319826Z Progress (2): 3.8/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4321023Z Progress (2): 3.8/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4321598Z Progress (2): 3.8/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4322666Z Progress (2): 3.8/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4323226Z Progress (2): 3.8/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4323767Z Progress (2): 3.8/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4324296Z Progress (2): 3.8/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4324762Z Progress (2): 3.8/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4325234Z Progress (2): 3.9/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4325761Z Progress (2): 3.9/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4326224Z Progress (2): 3.9/8.4 MB | 1.4/1.4 MB
2026-01-19T16:16:22.4328442Z Progress (2): 3.9/8.4 MB | 1.4 MB    
2026-01-19T16:16:22.4329230Z                                  
2026-01-19T16:16:22.4331180Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-devtools-v120/4.16.1/selenium-devtools-v120-4.16.1.jar (1.4 MB at 1.9 MB/s)
2026-01-19T16:16:22.4332189Z Progress (1): 3.9/8.4 MB
2026-01-19T16:16:22.4333006Z Progress (1): 3.9/8.4 MB
2026-01-19T16:16:22.4333708Z                         
2026-01-19T16:16:22.4334637Z Downloading from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-safari-driver/4.16.1/selenium-safari-driver-4.16.1.jar
2026-01-19T16:16:22.4339111Z Progress (1): 3.9/8.4 MB
2026-01-19T16:16:22.4341952Z Progress (1): 3.9/8.4 MB
2026-01-19T16:16:22.4344212Z Progress (1): 4.0/8.4 MB
2026-01-19T16:16:22.4347309Z Progress (1): 4.0/8.4 MB
2026-01-19T16:16:22.4350020Z Progress (1): 4.0/8.4 MB
2026-01-19T16:16:22.4352222Z Progress (1): 4.0/8.4 MB
2026-01-19T16:16:22.4378465Z Progress (1): 4.0/8.4 MB
2026-01-19T16:16:22.4378846Z Progress (1): 4.0/8.4 MB
2026-01-19T16:16:22.4379314Z Progress (1): 4.1/8.4 MB
2026-01-19T16:16:22.4379709Z Progress (1): 4.1/8.4 MB
2026-01-19T16:16:22.4380113Z Progress (1): 4.1/8.4 MB
2026-01-19T16:16:22.4381849Z Progress (1): 4.1/8.4 MB
2026-01-19T16:16:22.4382287Z Progress (1): 4.1/8.4 MB
2026-01-19T16:16:22.4384183Z Progress (1): 4.1/8.4 MB
2026-01-19T16:16:22.4384581Z Progress (1): 4.2/8.4 MB
2026-01-19T16:16:22.4384912Z Progress (1): 4.2/8.4 MB
2026-01-19T16:16:22.4385190Z Progress (1): 4.2/8.4 MB
2026-01-19T16:16:22.4385825Z Progress (1): 4.2/8.4 MB
2026-01-19T16:16:22.4386158Z Progress (1): 4.2/8.4 MB
2026-01-19T16:16:22.4386661Z Progress (1): 4.2/8.4 MB
2026-01-19T16:16:22.4410159Z Progress (1): 4.3/8.4 MB
2026-01-19T16:16:22.4412432Z Progress (1): 4.3/8.4 MB
2026-01-19T16:16:22.4414772Z Progress (1): 4.3/8.4 MB
2026-01-19T16:16:22.4416411Z Progress (1): 4.3/8.4 MB
2026-01-19T16:16:22.4422104Z Progress (1): 4.3/8.4 MB
2026-01-19T16:16:22.4423419Z Progress (1): 4.3/8.4 MB
2026-01-19T16:16:22.4423941Z Progress (1): 4.4/8.4 MB
2026-01-19T16:16:22.4424393Z Progress (1): 4.4/8.4 MB
2026-01-19T16:16:22.4425637Z Progress (1): 4.4/8.4 MB
2026-01-19T16:16:22.4426187Z Progress (2): 4.4/8.4 MB | 7.7/83 kB
2026-01-19T16:16:22.4427409Z Progress (2): 4.4/8.4 MB | 8.2/83 kB
2026-01-19T16:16:22.4427987Z Progress (2): 4.4/8.4 MB | 25/83 kB 
2026-01-19T16:16:22.4428498Z Progress (2): 4.4/8.4 MB | 41/83 kB
2026-01-19T16:16:22.4430469Z Progress (2): 4.4/8.4 MB | 57/83 kB
2026-01-19T16:16:22.4430815Z Progress (2): 4.4/8.4 MB | 74/83 kB
2026-01-19T16:16:22.4431164Z Progress (2): 4.4/8.4 MB | 83 kB   
2026-01-19T16:16:22.4448782Z Progress (3): 4.4/8.4 MB | 83 kB | 7.7/15 kB
2026-01-19T16:16:22.4449354Z Progress (3): 4.4/8.4 MB | 83 kB | 15 kB    
2026-01-19T16:16:22.4449841Z Progress (3): 4.4/8.4 MB | 83 kB | 15 kB
2026-01-19T16:16:22.4450333Z Progress (3): 4.4/8.4 MB | 83 kB | 15 kB
2026-01-19T16:16:22.4450793Z                                         
2026-01-19T16:16:22.4451635Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-firefox-driver/4.16.1/selenium-firefox-driver-4.16.1.jar (83 kB at 109 kB/s)
2026-01-19T16:16:22.4452333Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-core/7.27.2/cucumber-core-7.27.2.jar
2026-01-19T16:16:22.4453029Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-edge-driver/4.16.1/selenium-edge-driver-4.16.1.jar (15 kB at 20 kB/s)
2026-01-19T16:16:22.4454417Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin/7.27.2/cucumber-gherkin-7.27.2.jar
2026-01-19T16:16:22.4457751Z Progress (1): 4.4/8.4 MB
2026-01-19T16:16:22.4460180Z Progress (1): 4.5/8.4 MB
2026-01-19T16:16:22.4462580Z Progress (1): 4.5/8.4 MB
2026-01-19T16:16:22.4465332Z Progress (1): 4.5/8.4 MB
2026-01-19T16:16:22.4470736Z Progress (1): 4.5/8.4 MB
2026-01-19T16:16:22.4472470Z Progress (2): 4.5/8.4 MB | 4.1/17 kB
2026-01-19T16:16:22.4474014Z Progress (2): 4.5/8.4 MB | 17 kB    
2026-01-19T16:16:22.4498351Z Progress (2): 4.5/8.4 MB | 17 kB
2026-01-19T16:16:22.4499216Z                                 
2026-01-19T16:16:22.4499855Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-ie-driver/4.16.1/selenium-ie-driver-4.16.1.jar (17 kB at 22 kB/s)
2026-01-19T16:16:22.4501210Z Progress (1): 4.5/8.4 MB
2026-01-19T16:16:22.4501737Z Progress (1): 4.6/8.4 MB
2026-01-19T16:16:22.4502176Z                         
2026-01-19T16:16:22.4503386Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin-messages/7.27.2/cucumber-gherkin-messages-7.27.2.jar
2026-01-19T16:16:22.4504955Z Progress (1): 4.6/8.4 MB
2026-01-19T16:16:22.4506190Z Progress (1): 4.6/8.4 MB
2026-01-19T16:16:22.4507057Z Progress (1): 4.6/8.4 MB
2026-01-19T16:16:22.4507574Z Progress (1): 4.6/8.4 MB
2026-01-19T16:16:22.4509422Z Progress (1): 4.6/8.4 MB
2026-01-19T16:16:22.4509990Z Progress (1): 4.7/8.4 MB
2026-01-19T16:16:22.4511870Z Progress (1): 4.7/8.4 MB
2026-01-19T16:16:22.4512254Z Progress (1): 4.7/8.4 MB
2026-01-19T16:16:22.4512539Z Progress (1): 4.7/8.4 MB
2026-01-19T16:16:22.4514727Z Progress (1): 4.7/8.4 MB
2026-01-19T16:16:22.4517805Z Progress (1): 4.7/8.4 MB
2026-01-19T16:16:22.4520375Z Progress (1): 4.8/8.4 MB
2026-01-19T16:16:22.4521819Z Progress (1): 4.8/8.4 MB
2026-01-19T16:16:22.4524469Z Progress (1): 4.8/8.4 MB
2026-01-19T16:16:22.4527545Z Progress (1): 4.8/8.4 MB
2026-01-19T16:16:22.4530353Z Progress (1): 4.8/8.4 MB
2026-01-19T16:16:22.4531967Z Progress (1): 4.8/8.4 MB
2026-01-19T16:16:22.4536402Z Progress (1): 4.8/8.4 MB
2026-01-19T16:16:22.4540408Z Progress (1): 4.9/8.4 MB
2026-01-19T16:16:22.4540738Z Progress (1): 4.9/8.4 MB
2026-01-19T16:16:22.4542761Z Progress (1): 4.9/8.4 MB
2026-01-19T16:16:22.4545998Z Progress (1): 4.9/8.4 MB
2026-01-19T16:16:22.4547546Z Progress (1): 4.9/8.4 MB
2026-01-19T16:16:22.4568411Z Progress (1): 4.9/8.4 MB
2026-01-19T16:16:22.4569133Z Progress (1): 5.0/8.4 MB
2026-01-19T16:16:22.4569762Z Progress (1): 5.0/8.4 MB
2026-01-19T16:16:22.4570078Z Progress (1): 5.0/8.4 MB
2026-01-19T16:16:22.4570367Z Progress (1): 5.0/8.4 MB
2026-01-19T16:16:22.4570664Z Progress (1): 5.0/8.4 MB
2026-01-19T16:16:22.4570956Z Progress (1): 5.0/8.4 MB
2026-01-19T16:16:22.4571383Z Progress (1): 5.1/8.4 MB
2026-01-19T16:16:22.4571674Z Progress (1): 5.1/8.4 MB
2026-01-19T16:16:22.4575239Z Progress (1): 5.1/8.4 MB
2026-01-19T16:16:22.4578812Z Progress (1): 5.1/8.4 MB
2026-01-19T16:16:22.4582800Z Progress (1): 5.1/8.4 MB
2026-01-19T16:16:22.4586378Z Progress (1): 5.1/8.4 MB
2026-01-19T16:16:22.4606899Z Progress (1): 5.2/8.4 MB
2026-01-19T16:16:22.4607544Z Progress (2): 5.2/8.4 MB | 7.7/27 kB
2026-01-19T16:16:22.4608025Z Progress (2): 5.2/8.4 MB | 16/27 kB 
2026-01-19T16:16:22.4608516Z Progress (2): 5.2/8.4 MB | 16/27 kB
2026-01-19T16:16:22.4609028Z Progress (2): 5.2/8.4 MB | 16/27 kB
2026-01-19T16:16:22.4609516Z Progress (2): 5.2/8.4 MB | 16/27 kB
2026-01-19T16:16:22.4610164Z Progress (2): 5.2/8.4 MB | 27 kB   
2026-01-19T16:16:22.4610674Z                                 
2026-01-19T16:16:22.4611344Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-safari-driver/4.16.1/selenium-safari-driver-4.16.1.jar (27 kB at 35 kB/s)
2026-01-19T16:16:22.4612590Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/gherkin/34.0.0/gherkin-34.0.0.jar
2026-01-19T16:16:22.4618918Z Progress (1): 5.2/8.4 MB
2026-01-19T16:16:22.4623600Z Progress (1): 5.2/8.4 MB
2026-01-19T16:16:22.4631772Z Progress (1): 5.3/8.4 MB
2026-01-19T16:16:22.4635857Z Progress (1): 5.3/8.4 MB
2026-01-19T16:16:22.4636456Z Progress (1): 5.3/8.4 MB
2026-01-19T16:16:22.4658290Z Progress (2): 5.3/8.4 MB | 0/3.0 MB
2026-01-19T16:16:22.4662295Z Progress (2): 5.3/8.4 MB | 0/3.0 MB
2026-01-19T16:16:22.4662630Z Progress (2): 5.3/8.4 MB | 0/3.0 MB
2026-01-19T16:16:22.4662946Z Progress (2): 5.3/8.4 MB | 0/3.0 MB
2026-01-19T16:16:22.4663262Z Progress (2): 5.3/8.4 MB | 0/3.0 MB
2026-01-19T16:16:22.4663579Z Progress (2): 5.3/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4663884Z Progress (2): 5.3/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4664516Z Progress (2): 5.4/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4688546Z Progress (2): 5.4/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4689198Z Progress (2): 5.4/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4689802Z Progress (2): 5.4/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4690294Z Progress (2): 5.4/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4690814Z Progress (2): 5.4/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4691310Z Progress (2): 5.4/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4691795Z Progress (2): 5.5/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4692268Z Progress (2): 5.5/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4692775Z Progress (2): 5.5/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4693608Z Progress (2): 5.5/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4694601Z Progress (2): 5.5/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4695181Z Progress (2): 5.5/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4695700Z Progress (2): 5.5/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4696249Z Progress (2): 5.5/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4697515Z Progress (3): 5.5/8.4 MB | 0.1/3.0 MB | 7.5 kB
2026-01-19T16:16:22.4698064Z                                               
2026-01-19T16:16:22.4698640Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin/7.27.2/cucumber-gherkin-7.27.2.jar (7.5 kB at 9.5 kB/s)
2026-01-19T16:16:22.4699933Z Downloading from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-core/3.27.4/assertj-core-3.27.4.jar
2026-01-19T16:16:22.4703442Z Progress (2): 5.5/8.4 MB | 0.1/3.0 MB
2026-01-19T16:16:22.4706055Z Progress (2): 5.5/8.4 MB | 0.2/3.0 MB
2026-01-19T16:16:22.4706372Z Progress (2): 5.5/8.4 MB | 0.2/3.0 MB
2026-01-19T16:16:22.4706950Z Progress (2): 5.5/8.4 MB | 0.2/3.0 MB
2026-01-19T16:16:22.4710800Z Progress (2): 5.5/8.4 MB | 0.2/3.0 MB
2026-01-19T16:16:22.4711162Z Progress (2): 5.5/8.4 MB | 0.2/3.0 MB
2026-01-19T16:16:22.4711507Z Progress (2): 5.5/8.4 MB | 0.2/3.0 MB
2026-01-19T16:16:22.4711802Z Progress (2): 5.5/8.4 MB | 0.2/3.0 MB
2026-01-19T16:16:22.4713421Z Progress (2): 5.6/8.4 MB | 0.2/3.0 MB
2026-01-19T16:16:22.4738433Z Progress (2): 5.6/8.4 MB | 0.2/3.0 MB
2026-01-19T16:16:22.4739097Z Progress (2): 5.6/8.4 MB | 0.2/3.0 MB
2026-01-19T16:16:22.4739709Z Progress (2): 5.6/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4740040Z Progress (2): 5.6/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4740353Z Progress (2): 5.6/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4740670Z Progress (2): 5.6/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4740985Z Progress (2): 5.6/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4741304Z Progress (2): 5.6/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4741616Z Progress (2): 5.6/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4741936Z Progress (2): 5.6/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4745423Z Progress (2): 5.6/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4747717Z Progress (2): 5.6/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4787619Z Progress (2): 5.7/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4788016Z Progress (2): 5.7/8.4 MB | 0.3/3.0 MB
2026-01-19T16:16:22.4788344Z Progress (2): 5.7/8.4 MB | 0.4/3.0 MB
2026-01-19T16:16:22.4788662Z Progress (2): 5.7/8.4 MB | 0.4/3.0 MB
2026-01-19T16:16:22.4788977Z Progress (2): 5.7/8.4 MB | 0.4/3.0 MB
2026-01-19T16:16:22.4789314Z Progress (3): 5.7/8.4 MB | 0.4/3.0 MB | 7.7/29 kB
2026-01-19T16:16:22.4789660Z Progress (3): 5.7/8.4 MB | 0.4/3.0 MB | 16/29 kB 
2026-01-19T16:16:22.4790022Z Progress (3): 5.7/8.4 MB | 0.4/3.0 MB | 16/29 kB
2026-01-19T16:16:22.4790532Z Progress (3): 5.7/8.4 MB | 0.4/3.0 MB | 16/29 kB
2026-01-19T16:16:22.4790869Z Progress (3): 5.7/8.4 MB | 0.4/3.0 MB | 16/29 kB
2026-01-19T16:16:22.4791195Z Progress (3): 5.7/8.4 MB | 0.4/3.0 MB | 16/29 kB
2026-01-19T16:16:22.4791524Z Progress (3): 5.8/8.4 MB | 0.4/3.0 MB | 16/29 kB
2026-01-19T16:16:22.4791845Z Progress (3): 5.8/8.4 MB | 0.4/3.0 MB | 29 kB   
2026-01-19T16:16:22.4792143Z                                              
2026-01-19T16:16:22.4792563Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-gherkin-messages/7.27.2/cucumber-gherkin-messages-7.27.2.jar (29 kB at 37 kB/s)
2026-01-19T16:16:22.4813959Z Progress (2): 5.8/8.4 MB | 0.4/3.0 MB
2026-01-19T16:16:22.4814336Z                                      
2026-01-19T16:16:22.4814724Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/28.1.0/messages-28.1.0.jar
2026-01-19T16:16:22.4815138Z Progress (2): 5.8/8.4 MB | 0.4/3.0 MB
2026-01-19T16:16:22.4815455Z Progress (2): 5.8/8.4 MB | 0.4/3.0 MB
2026-01-19T16:16:22.4815763Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4816077Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4816383Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4838337Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4839283Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4840408Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4841007Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4841522Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4842042Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4843222Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4843830Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4844404Z Progress (2): 5.8/8.4 MB | 0.5/3.0 MB
2026-01-19T16:16:22.4844728Z Progress (2): 5.8/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4845048Z Progress (2): 5.9/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4849559Z Progress (2): 5.9/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4883088Z Progress (2): 5.9/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4883699Z Progress (2): 5.9/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4884283Z Progress (2): 5.9/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4884775Z Progress (2): 5.9/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4885273Z Progress (2): 5.9/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4886195Z Progress (2): 6.0/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4887577Z Progress (2): 6.0/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4888165Z Progress (2): 6.0/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4888637Z Progress (2): 6.0/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4889800Z Progress (2): 6.0/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4890605Z Progress (2): 6.0/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4891367Z Progress (2): 6.0/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4891985Z Progress (2): 6.0/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4893004Z Progress (2): 6.0/8.4 MB | 0.6/3.0 MB
2026-01-19T16:16:22.4893566Z Progress (2): 6.0/8.4 MB | 0.7/3.0 MB
2026-01-19T16:16:22.4897662Z Progress (2): 6.0/8.4 MB | 0.7/3.0 MB
2026-01-19T16:16:22.4898046Z Progress (2): 6.0/8.4 MB | 0.7/3.0 MB
2026-01-19T16:16:22.4899469Z Progress (2): 6.0/8.4 MB | 0.7/3.0 MB
2026-01-19T16:16:22.4900513Z Progress (2): 6.0/8.4 MB | 0.7/3.0 MB
2026-01-19T16:16:22.4902233Z Progress (2): 6.0/8.4 MB | 0.7/3.0 MB
2026-01-19T16:16:22.4906103Z Progress (2): 6.0/8.4 MB | 0.7/3.0 MB
2026-01-19T16:16:22.4908861Z Progress (3): 6.0/8.4 MB | 0.7/3.0 MB | 0/1.4 MB
2026-01-19T16:16:22.4911106Z Progress (3): 6.0/8.4 MB | 0.8/3.0 MB | 0/1.4 MB
2026-01-19T16:16:22.4918509Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0/1.4 MB
2026-01-19T16:16:22.4919373Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0/1.4 MB
2026-01-19T16:16:22.4924265Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0/1.4 MB
2026-01-19T16:16:22.4925014Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0/1.4 MB
2026-01-19T16:16:22.4927443Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0/1.4 MB
2026-01-19T16:16:22.4930388Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0/1.4 MB
2026-01-19T16:16:22.4935475Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0/1.4 MB
2026-01-19T16:16:22.4936720Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.4937077Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.4945637Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.4946023Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.4954463Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.4955094Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.4955437Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.4955762Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.4959633Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.4963725Z Progress (3): 6.1/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.4967804Z Progress (3): 6.2/8.4 MB | 0.8/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5001920Z Progress (3): 6.2/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5005864Z Progress (3): 6.2/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5009822Z Progress (3): 6.2/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5013365Z Progress (3): 6.2/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5013948Z Progress (3): 6.2/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5014560Z Progress (3): 6.2/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5016986Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5017622Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5037484Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5039805Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5040175Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5040823Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5041189Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5041527Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5041850Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.1/1.4 MB
2026-01-19T16:16:22.5042194Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5042522Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5042837Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5043237Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5043578Z Progress (3): 6.3/8.4 MB | 0.9/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5043924Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5044428Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5044769Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5045104Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5046198Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5046696Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5060128Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5063944Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5065544Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.2/1.4 MB
2026-01-19T16:16:22.5067514Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5069038Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5079393Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5080378Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5081195Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5083551Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5085304Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5085789Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5086283Z Progress (3): 6.3/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5091898Z Progress (3): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5097204Z Progress (3): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5097853Z Progress (3): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5100158Z Progress (3): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB
2026-01-19T16:16:22.5100684Z Progress (4): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB | 7.7/98 kB
2026-01-19T16:16:22.5101258Z Progress (4): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB | 16/98 kB 
2026-01-19T16:16:22.5103133Z Progress (4): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB | 32/98 kB
2026-01-19T16:16:22.5105395Z Progress (4): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB | 49/98 kB
2026-01-19T16:16:22.5107076Z Progress (4): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB | 65/98 kB
2026-01-19T16:16:22.5107627Z Progress (4): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB | 81/98 kB
2026-01-19T16:16:22.5108179Z Progress (4): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB | 98/98 kB
2026-01-19T16:16:22.5127862Z Progress (4): 6.4/8.4 MB | 1.0/3.0 MB | 0.3/1.4 MB | 98 kB   
2026-01-19T16:16:22.5128527Z Progress (4): 6.4/8.4 MB | 1.1/3.0 MB | 0.3/1.4 MB | 98 kB
2026-01-19T16:16:22.5129225Z Progress (4): 6.4/8.4 MB | 1.1/3.0 MB | 0.3/1.4 MB | 98 kB
2026-01-19T16:16:22.5129770Z Progress (4): 6.4/8.4 MB | 1.1/3.0 MB | 0.3/1.4 MB | 98 kB
2026-01-19T16:16:22.5130355Z Progress (4): 6.4/8.4 MB | 1.1/3.0 MB | 0.3/1.4 MB | 98 kB
2026-01-19T16:16:22.5131392Z Progress (4): 6.4/8.4 MB | 1.1/3.0 MB | 0.3/1.4 MB | 98 kB
2026-01-19T16:16:22.5131946Z Progress (4): 6.4/8.4 MB | 1.1/3.0 MB | 0.3/1.4 MB | 98 kB
2026-01-19T16:16:22.5132443Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.3/1.4 MB | 98 kB
2026-01-19T16:16:22.5140957Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.3/1.4 MB | 98 kB
2026-01-19T16:16:22.5141334Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.3/1.4 MB | 98 kB
2026-01-19T16:16:22.5141682Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.4/1.4 MB | 98 kB
2026-01-19T16:16:22.5142006Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.4/1.4 MB | 98 kB
2026-01-19T16:16:22.5142362Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.4/1.4 MB | 98 kB
2026-01-19T16:16:22.5142812Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.4/1.4 MB | 98 kB
2026-01-19T16:16:22.5143153Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.4/1.4 MB | 98 kB
2026-01-19T16:16:22.5143499Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.4/1.4 MB | 98 kB
2026-01-19T16:16:22.5159944Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB | 98 kB
2026-01-19T16:16:22.5161553Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB | 98 kB
2026-01-19T16:16:22.5162518Z Progress (4): 6.4/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB | 98 kB
2026-01-19T16:16:22.5163152Z Progress (4): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB | 98 kB
2026-01-19T16:16:22.5163980Z Progress (4): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB | 98 kB
2026-01-19T16:16:22.5165051Z Progress (4): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB | 98 kB
2026-01-19T16:16:22.5165613Z Progress (4): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB | 98 kB
2026-01-19T16:16:22.5166336Z Progress (4): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB | 98 kB
2026-01-19T16:16:22.5170032Z Progress (4): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB | 98 kB
2026-01-19T16:16:22.5170371Z                                                           
2026-01-19T16:16:22.5170770Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/messages/28.1.0/messages-28.1.0.jar (98 kB at 118 kB/s)
2026-01-19T16:16:22.5171273Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/pretty-formatter/2.1.0/pretty-formatter-2.1.0.jar
2026-01-19T16:16:22.5187813Z Progress (3): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5190689Z Progress (3): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5191401Z Progress (3): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5192078Z Progress (3): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5193427Z Progress (3): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5195247Z Progress (3): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5195856Z Progress (3): 6.5/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5197126Z Progress (3): 6.6/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5200747Z Progress (3): 6.6/8.4 MB | 1.2/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5203031Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5205657Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5208231Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5211437Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5214494Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5225077Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5227932Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.5/1.4 MB
2026-01-19T16:16:22.5228763Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5229374Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5231383Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5231984Z Progress (3): 6.6/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5234245Z Progress (3): 6.7/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5238198Z Progress (3): 6.7/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5240017Z Progress (3): 6.7/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5241926Z Progress (3): 6.7/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5243332Z Progress (3): 6.7/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5245594Z Progress (3): 6.7/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5248977Z Progress (3): 6.7/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5287910Z Progress (3): 6.7/8.4 MB | 1.3/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5291950Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5293694Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5295422Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5299792Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5301599Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5304203Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.6/1.4 MB
2026-01-19T16:16:22.5306002Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.7/1.4 MB
2026-01-19T16:16:22.5307920Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.7/1.4 MB
2026-01-19T16:16:22.5312294Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.7/1.4 MB
2026-01-19T16:16:22.5312635Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.7/1.4 MB
2026-01-19T16:16:22.5312979Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.7/1.4 MB
2026-01-19T16:16:22.5313324Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.7/1.4 MB
2026-01-19T16:16:22.5313644Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5313978Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5314288Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5314716Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5315050Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5315380Z Progress (3): 6.7/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5315700Z Progress (3): 6.8/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5316041Z Progress (3): 6.8/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5316347Z Progress (3): 6.8/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5338087Z Progress (3): 6.8/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5338976Z Progress (3): 6.8/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5340716Z Progress (3): 6.8/8.4 MB | 1.4/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5341158Z Progress (3): 6.8/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5341481Z Progress (3): 6.8/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5348981Z Progress (3): 6.8/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5349412Z Progress (3): 6.8/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5350259Z Progress (3): 6.8/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5350636Z Progress (3): 6.8/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5355744Z Progress (3): 6.8/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5356119Z Progress (3): 6.8/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5356647Z Progress (3): 6.9/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5356984Z Progress (3): 6.9/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5357312Z Progress (3): 6.9/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5357657Z Progress (3): 6.9/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5357975Z Progress (3): 6.9/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5358296Z Progress (3): 6.9/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5358654Z Progress (3): 6.9/8.4 MB | 1.5/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5359038Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5359374Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.8/1.4 MB
2026-01-19T16:16:22.5359704Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5360058Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5360389Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5362704Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5363951Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5365355Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5365923Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5366994Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5370256Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5374121Z Progress (3): 6.9/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5377647Z Progress (3): 7.0/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5377998Z Progress (3): 7.0/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5381917Z Progress (3): 7.0/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5384633Z Progress (3): 7.0/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5408019Z Progress (3): 7.0/8.4 MB | 1.6/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5412471Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5412933Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 0.9/1.4 MB
2026-01-19T16:16:22.5415188Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5415554Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5415879Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5416187Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5416714Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5417060Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5417390Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5417726Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5418051Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5439460Z Progress (3): 7.0/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5440152Z Progress (3): 7.1/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5440823Z Progress (3): 7.1/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5443478Z Progress (3): 7.1/8.4 MB | 1.7/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5444061Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5445122Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5445598Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5446067Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5448937Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5450123Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.0/1.4 MB
2026-01-19T16:16:22.5474493Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5480247Z Progress (4): 7.1/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB | 7.7/43 kB
2026-01-19T16:16:22.5482713Z Progress (4): 7.1/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB | 16/43 kB 
2026-01-19T16:16:22.5484336Z Progress (4): 7.1/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB | 32/43 kB
2026-01-19T16:16:22.5485955Z Progress (4): 7.1/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB | 43 kB   
2026-01-19T16:16:22.5488261Z                                                           
2026-01-19T16:16:22.5499324Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/pretty-formatter/2.1.0/pretty-formatter-2.1.0.jar (43 kB at 50 kB/s)
2026-01-19T16:16:22.5500276Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5500851Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5501345Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5501949Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5502489Z Progress (3): 7.1/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5502967Z Progress (3): 7.2/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5503490Z Progress (3): 7.2/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5503944Z                                                   
2026-01-19T16:16:22.5504465Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.6.0/query-13.6.0.jar
2026-01-19T16:16:22.5505037Z Progress (3): 7.2/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5505543Z Progress (3): 7.2/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5506025Z Progress (3): 7.2/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5506693Z Progress (3): 7.2/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5507193Z Progress (3): 7.2/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5507699Z Progress (3): 7.2/8.4 MB | 1.8/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5508177Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5508681Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5515630Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5516346Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5517473Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5517978Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5699257Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5700381Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5701001Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5701554Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5702111Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5703058Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.1/1.4 MB
2026-01-19T16:16:22.5704110Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.2/1.4 MB
2026-01-19T16:16:22.5704889Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.2/1.4 MB
2026-01-19T16:16:22.5705427Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.2/1.4 MB
2026-01-19T16:16:22.5706094Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.2/1.4 MB
2026-01-19T16:16:22.5706960Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.2/1.4 MB
2026-01-19T16:16:22.5707507Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.2/1.4 MB
2026-01-19T16:16:22.5708251Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5709148Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5709675Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5710178Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5710883Z Progress (3): 7.2/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5711466Z Progress (3): 7.3/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5712082Z Progress (3): 7.3/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5712761Z Progress (3): 7.3/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5713309Z Progress (3): 7.3/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5714233Z Progress (3): 7.3/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5717120Z Progress (3): 7.3/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5717793Z Progress (3): 7.4/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5718396Z Progress (3): 7.4/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB
2026-01-19T16:16:22.5718951Z Progress (4): 7.4/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB | 7.7/219 kB
2026-01-19T16:16:22.5719560Z Progress (4): 7.4/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB | 16/219 kB 
2026-01-19T16:16:22.5720164Z Progress (4): 7.4/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB | 32/219 kB
2026-01-19T16:16:22.5720711Z Progress (4): 7.4/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB | 48/219 kB
2026-01-19T16:16:22.5722321Z Progress (4): 7.4/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB | 65/219 kB
2026-01-19T16:16:22.5722707Z Progress (4): 7.4/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB | 66/219 kB
2026-01-19T16:16:22.5753794Z Progress (4): 7.4/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5754234Z Progress (4): 7.4/8.4 MB | 1.9/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5754611Z Progress (4): 7.4/8.4 MB | 2.0/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5754983Z Progress (4): 7.4/8.4 MB | 2.0/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5755367Z Progress (4): 7.4/8.4 MB | 2.0/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5755731Z Progress (4): 7.4/8.4 MB | 2.0/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5756099Z Progress (4): 7.4/8.4 MB | 2.0/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5756458Z Progress (4): 7.4/8.4 MB | 2.0/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5757153Z Progress (4): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5757519Z Progress (4): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5757893Z Progress (4): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5758275Z Progress (5): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 82/219 kB | 7.7/31 kB
2026-01-19T16:16:22.5758650Z Progress (5): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 82/219 kB | 12/31 kB 
2026-01-19T16:16:22.5759031Z Progress (5): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 82/219 kB | 29/31 kB
2026-01-19T16:16:22.5759392Z Progress (5): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 82/219 kB | 31 kB   
2026-01-19T16:16:22.5759707Z                                                                       
2026-01-19T16:16:22.5760076Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/query/13.6.0/query-13.6.0.jar (31 kB at 35 kB/s)
2026-01-19T16:16:22.5787937Z Progress (4): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5788345Z Progress (4): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5788663Z                                                               
2026-01-19T16:16:22.5789052Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/testng-xml-formatter/0.5.0/testng-xml-formatter-0.5.0.jar
2026-01-19T16:16:22.5789502Z Progress (4): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 82/219 kB
2026-01-19T16:16:22.5789851Z Progress (4): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 98/219 kB
2026-01-19T16:16:22.5790202Z Progress (4): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 115/219 kB
2026-01-19T16:16:22.5790696Z Progress (4): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 115/219 kB
2026-01-19T16:16:22.5791047Z Progress (4): 7.4/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 131/219 kB
2026-01-19T16:16:22.5791391Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 131/219 kB
2026-01-19T16:16:22.5793860Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 147/219 kB
2026-01-19T16:16:22.5795853Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.3/1.4 MB | 147/219 kB
2026-01-19T16:16:22.5880646Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 147/219 kB
2026-01-19T16:16:22.5881984Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 147/219 kB
2026-01-19T16:16:22.5882774Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 147/219 kB
2026-01-19T16:16:22.5883356Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 147/219 kB
2026-01-19T16:16:22.5883912Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 147/219 kB
2026-01-19T16:16:22.5884476Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 164/219 kB
2026-01-19T16:16:22.5885045Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 180/219 kB
2026-01-19T16:16:22.5885641Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 197/219 kB
2026-01-19T16:16:22.5887693Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 213/219 kB
2026-01-19T16:16:22.5888300Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 219 kB    
2026-01-19T16:16:22.5888836Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 219 kB
2026-01-19T16:16:22.5889375Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4/1.4 MB | 219 kB
2026-01-19T16:16:22.5890111Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4 MB | 219 kB    
2026-01-19T16:16:22.5890681Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5891821Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5892944Z Progress (4): 7.5/8.4 MB | 2.1/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5893605Z Progress (4): 7.5/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5894355Z Progress (4): 7.5/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5894904Z Progress (4): 7.5/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5895586Z Progress (4): 7.5/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5895976Z Progress (4): 7.5/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5896326Z Progress (4): 7.6/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5896892Z Progress (4): 7.6/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5897247Z Progress (4): 7.6/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5897597Z Progress (4): 7.6/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5897931Z Progress (4): 7.6/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5898280Z Progress (4): 7.6/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5898617Z Progress (4): 7.7/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5898957Z Progress (4): 7.7/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5899297Z Progress (4): 7.7/8.4 MB | 2.2/3.0 MB | 1.4 MB | 219 kB
2026-01-19T16:16:22.5899603Z                                                        
2026-01-19T16:16:22.5899982Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/gherkin/34.0.0/gherkin-34.0.0.jar (219 kB at 241 kB/s)
2026-01-19T16:16:22.5900517Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/tag-expressions/6.1.2/tag-expressions-6.1.2.jar
2026-01-19T16:16:22.5901042Z Downloaded from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-core/3.27.4/assertj-core-3.27.4.jar (1.4 MB at 1.5 MB/s)
2026-01-19T16:16:22.5901566Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-expressions/18.0.1/cucumber-expressions-18.0.1.jar
2026-01-19T16:16:22.5918852Z Progress (2): 7.7/8.4 MB | 2.2/3.0 MB
2026-01-19T16:16:22.5919296Z Progress (2): 7.7/8.4 MB | 2.2/3.0 MB
2026-01-19T16:16:22.5919622Z Progress (2): 7.7/8.4 MB | 2.2/3.0 MB
2026-01-19T16:16:22.5920100Z Progress (2): 7.7/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5920414Z Progress (2): 7.7/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5920721Z Progress (2): 7.7/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5921034Z Progress (2): 7.7/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5924272Z Progress (2): 7.7/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5925892Z Progress (2): 7.7/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5928324Z Progress (2): 7.7/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5930688Z Progress (2): 7.7/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5932749Z Progress (2): 7.7/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5934859Z Progress (2): 7.8/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5936776Z Progress (2): 7.8/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5938736Z Progress (2): 7.8/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5940768Z Progress (2): 7.8/8.4 MB | 2.3/3.0 MB
2026-01-19T16:16:22.5967743Z Progress (2): 7.8/8.4 MB | 2.4/3.0 MB
2026-01-19T16:16:22.5968363Z Progress (2): 7.8/8.4 MB | 2.4/3.0 MB
2026-01-19T16:16:22.5968911Z Progress (2): 7.8/8.4 MB | 2.4/3.0 MB
2026-01-19T16:16:22.5969473Z Progress (2): 7.8/8.4 MB | 2.4/3.0 MB
2026-01-19T16:16:22.5970059Z Progress (2): 7.8/8.4 MB | 2.4/3.0 MB
2026-01-19T16:16:22.5971815Z Progress (2): 7.8/8.4 MB | 2.4/3.0 MB
2026-01-19T16:16:22.5972142Z Progress (2): 7.8/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5972483Z Progress (2): 7.8/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5972791Z Progress (2): 7.8/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5973103Z Progress (2): 7.8/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5973410Z Progress (2): 7.8/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5973723Z Progress (2): 7.9/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5974030Z Progress (2): 7.9/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5977846Z Progress (2): 7.9/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5980474Z Progress (2): 7.9/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5981561Z Progress (2): 7.9/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5984064Z Progress (2): 7.9/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5986768Z Progress (2): 7.9/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5989636Z Progress (2): 7.9/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5991700Z Progress (2): 7.9/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.5994311Z Progress (2): 7.9/8.4 MB | 2.5/3.0 MB
2026-01-19T16:16:22.6017896Z Progress (2): 7.9/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6028759Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6034194Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6039106Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6044111Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6046256Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6052256Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6054469Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6058153Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6058825Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6059328Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6059659Z Progress (2): 8.0/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6059989Z Progress (2): 8.1/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6060302Z Progress (2): 8.1/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6060625Z Progress (2): 8.1/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6060939Z Progress (2): 8.1/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6061257Z Progress (2): 8.1/8.4 MB | 2.6/3.0 MB
2026-01-19T16:16:22.6061568Z Progress (2): 8.1/8.4 MB | 2.7/3.0 MB
2026-01-19T16:16:22.6061880Z Progress (2): 8.1/8.4 MB | 2.7/3.0 MB
2026-01-19T16:16:22.6062203Z Progress (2): 8.1/8.4 MB | 2.7/3.0 MB
2026-01-19T16:16:22.6062516Z Progress (2): 8.1/8.4 MB | 2.7/3.0 MB
2026-01-19T16:16:22.6062837Z Progress (2): 8.1/8.4 MB | 2.7/3.0 MB
2026-01-19T16:16:22.6063185Z Progress (3): 8.1/8.4 MB | 2.7/3.0 MB | 7.7/17 kB
2026-01-19T16:16:22.6063533Z Progress (3): 8.1/8.4 MB | 2.7/3.0 MB | 16/17 kB 
2026-01-19T16:16:22.6063863Z Progress (3): 8.1/8.4 MB | 2.7/3.0 MB | 17 kB   
2026-01-19T16:16:22.6064170Z                                              
2026-01-19T16:16:22.6064582Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/testng-xml-formatter/0.5.0/testng-xml-formatter-0.5.0.jar (17 kB at 18 kB/s)
2026-01-19T16:16:22.6065171Z Progress (2): 8.1/8.4 MB | 2.7/3.0 MB
2026-01-19T16:16:22.6085640Z Progress (2): 8.1/8.4 MB | 2.7/3.0 MB
2026-01-19T16:16:22.6086024Z Progress (2): 8.2/8.4 MB | 2.7/3.0 MB
2026-01-19T16:16:22.6086352Z Progress (2): 8.2/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6086823Z                                      
2026-01-19T16:16:22.6087186Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/datatable/7.27.2/datatable-7.27.2.jar
2026-01-19T16:16:22.6087585Z Progress (2): 8.2/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6087901Z Progress (2): 8.2/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6088364Z Progress (2): 8.2/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6091859Z Progress (3): 8.2/8.4 MB | 2.8/3.0 MB | 7.5/13 kB
2026-01-19T16:16:22.6093987Z Progress (3): 8.2/8.4 MB | 2.8/3.0 MB | 13 kB    
2026-01-19T16:16:22.6097918Z Progress (3): 8.2/8.4 MB | 2.8/3.0 MB | 13 kB
2026-01-19T16:16:22.6098698Z                                              
2026-01-19T16:16:22.6100197Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/tag-expressions/6.1.2/tag-expressions-6.1.2.jar (13 kB at 15 kB/s)
2026-01-19T16:16:22.6104225Z Progress (2): 8.2/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6106823Z Progress (2): 8.2/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6108055Z Progress (2): 8.2/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6108760Z                                      
2026-01-19T16:16:22.6109535Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-plugin/7.27.2/cucumber-plugin-7.27.2.jar
2026-01-19T16:16:22.6147479Z Progress (2): 8.2/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6150553Z Progress (2): 8.2/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6150956Z Progress (2): 8.3/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6152070Z Progress (2): 8.3/8.4 MB | 2.8/3.0 MB
2026-01-19T16:16:22.6152484Z Progress (2): 8.3/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6153034Z Progress (2): 8.3/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6153412Z Progress (2): 8.3/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6153838Z Progress (2): 8.3/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6154173Z Progress (2): 8.3/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6154655Z Progress (2): 8.3/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6177239Z Progress (2): 8.3/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6177819Z Progress (2): 8.4/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6178189Z Progress (2): 8.4/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6178539Z Progress (2): 8.4/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6178987Z Progress (2): 8.4/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6179322Z Progress (2): 8.4/8.4 MB | 2.9/3.0 MB
2026-01-19T16:16:22.6179821Z Progress (3): 8.4/8.4 MB | 2.9/3.0 MB | 7.7/79 kB
2026-01-19T16:16:22.6209431Z Progress (3): 8.4/8.4 MB | 2.9/3.0 MB | 7.7/79 kB
2026-01-19T16:16:22.6209821Z Progress (3): 8.4/8.4 MB | 2.9/3.0 MB | 16/79 kB 
2026-01-19T16:16:22.6211480Z Progress (3): 8.4/8.4 MB | 2.9/3.0 MB | 29/79 kB
2026-01-19T16:16:22.6211848Z Progress (3): 8.4/8.4 MB | 2.9/3.0 MB | 45/79 kB
2026-01-19T16:16:22.6212177Z Progress (3): 8.4/8.4 MB | 2.9/3.0 MB | 61/79 kB
2026-01-19T16:16:22.6212512Z Progress (3): 8.4/8.4 MB | 2.9/3.0 MB | 78/79 kB
2026-01-19T16:16:22.6212843Z Progress (3): 8.4/8.4 MB | 2.9/3.0 MB | 79 kB   
2026-01-19T16:16:22.6213146Z                                              
2026-01-19T16:16:22.6213556Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-expressions/18.0.1/cucumber-expressions-18.0.1.jar (79 kB at 85 kB/s)
2026-01-19T16:16:22.6214001Z Progress (2): 8.4/8.4 MB | 3.0/3.0 MB
2026-01-19T16:16:22.6214316Z Progress (2): 8.4/8.4 MB | 3.0/3.0 MB
2026-01-19T16:16:22.6214644Z Progress (2): 8.4/8.4 MB | 3.0/3.0 MB
2026-01-19T16:16:22.6214957Z Progress (2): 8.4/8.4 MB | 3.0/3.0 MB
2026-01-19T16:16:22.6215280Z Progress (2): 8.4/8.4 MB | 3.0/3.0 MB
2026-01-19T16:16:22.6215587Z Progress (2): 8.4/8.4 MB | 3.0 MB    
2026-01-19T16:16:22.6215891Z Progress (2): 8.4/8.4 MB | 3.0 MB
2026-01-19T16:16:22.6216369Z Progress (2): 8.4/8.4 MB | 3.0 MB
2026-01-19T16:16:22.6217080Z Progress (2): 8.4/8.4 MB | 3.0 MB
2026-01-19T16:16:22.6217400Z Progress (2): 8.4 MB | 3.0 MB    
2026-01-19T16:16:22.6217682Z                              
2026-01-19T16:16:22.6218070Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/docstring/7.27.2/docstring-7.27.2.jar
2026-01-19T16:16:22.6218597Z Downloaded from central: https://repo.maven.apache.org/maven2/org/seleniumhq/selenium/selenium-manager/4.13.0/selenium-manager-4.13.0.jar (8.4 MB at 8.9 MB/s)
2026-01-19T16:16:22.6219153Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-core/7.27.2/cucumber-core-7.27.2.jar (3.0 MB at 3.2 MB/s)
2026-01-19T16:16:22.6219792Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/html-formatter/21.13.0/html-formatter-21.13.0.jar
2026-01-19T16:16:22.6220294Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/junit-xml-formatter/0.8.1/junit-xml-formatter-0.8.1.jar
2026-01-19T16:16:22.6324650Z Progress (1): 3.4/33 kB
2026-01-19T16:16:22.6325160Z Progress (1): 20/33 kB 
2026-01-19T16:16:22.6328834Z Progress (1): 33 kB   
2026-01-19T16:16:22.6329169Z                    
2026-01-19T16:16:22.6329628Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-plugin/7.27.2/cucumber-plugin-7.27.2.jar (33 kB at 35 kB/s)
2026-01-19T16:16:22.6330140Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/ci-environment/10.0.1/ci-environment-10.0.1.jar
2026-01-19T16:16:22.6423833Z Progress (1): 7.7/287 kB
2026-01-19T16:16:22.6432114Z Progress (1): 16/287 kB 
2026-01-19T16:16:22.6432568Z Progress (2): 16/287 kB | 7.7/14 kB
2026-01-19T16:16:22.6433361Z Progress (2): 16/287 kB | 14 kB    
2026-01-19T16:16:22.6435914Z Progress (2): 32/287 kB | 14 kB
2026-01-19T16:16:22.6436225Z                                
2026-01-19T16:16:22.6436797Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/docstring/7.27.2/docstring-7.27.2.jar (14 kB at 15 kB/s)
2026-01-19T16:16:22.6442507Z Progress (1): 49/287 kB
2026-01-19T16:16:22.6443205Z                        
2026-01-19T16:16:22.6443965Z Downloading from central: https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.jar
2026-01-19T16:16:22.6467547Z Progress (1): 65/287 kB
2026-01-19T16:16:22.6468228Z Progress (2): 65/287 kB | 7.7/14 kB
2026-01-19T16:16:22.6471024Z Progress (2): 65/287 kB | 14 kB    
2026-01-19T16:16:22.6471499Z                                
2026-01-19T16:16:22.6472056Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/junit-xml-formatter/0.8.1/junit-xml-formatter-0.8.1.jar (14 kB at 15 kB/s)
2026-01-19T16:16:22.6501919Z Progress (1): 81/287 kB
2026-01-19T16:16:22.6502532Z Progress (1): 98/287 kB
2026-01-19T16:16:22.6503433Z Progress (1): 114/287 kB
2026-01-19T16:16:22.6503851Z Progress (1): 131/287 kB
2026-01-19T16:16:22.6504340Z Progress (1): 147/287 kB
2026-01-19T16:16:22.6506907Z Progress (1): 163/287 kB
2026-01-19T16:16:22.6508050Z Progress (1): 180/287 kB
2026-01-19T16:16:22.6508461Z Progress (1): 196/287 kB
2026-01-19T16:16:22.6508979Z Progress (1): 213/287 kB
2026-01-19T16:16:22.6509428Z Progress (1): 229/287 kB
2026-01-19T16:16:22.6509722Z                         
2026-01-19T16:16:22.6510081Z Downloading from central: https://repo.maven.apache.org/maven2/org/testng/testng/7.11.0/testng-7.11.0.jar
2026-01-19T16:16:22.6520937Z Progress (1): 245/287 kB
2026-01-19T16:16:22.6527824Z Progress (1): 262/287 kB
2026-01-19T16:16:22.6533783Z Progress (1): 278/287 kB
2026-01-19T16:16:22.6534388Z Progress (2): 278/287 kB | 7.7/50 kB
2026-01-19T16:16:22.6543033Z Progress (2): 278/287 kB | 16/50 kB 
2026-01-19T16:16:22.6552035Z Progress (2): 278/287 kB | 32/50 kB
2026-01-19T16:16:22.6552574Z Progress (2): 278/287 kB | 49/50 kB
2026-01-19T16:16:22.6552937Z Progress (2): 278/287 kB | 50 kB   
2026-01-19T16:16:22.6553247Z                                 
2026-01-19T16:16:22.6553808Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/ci-environment/10.0.1/ci-environment-10.0.1.jar (50 kB at 51 kB/s)
2026-01-19T16:16:22.6554317Z Downloading from central: https://repo.maven.apache.org/maven2/org/jcommander/jcommander/1.83/jcommander-1.83.jar
2026-01-19T16:16:22.6557708Z Progress (1): 287 kB
2026-01-19T16:16:22.6558264Z                     
2026-01-19T16:16:22.6558817Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/html-formatter/21.13.0/html-formatter-21.13.0.jar (287 kB at 294 kB/s)
2026-01-19T16:16:22.6566701Z Downloading from central: https://repo.maven.apache.org/maven2/org/webjars/jquery/3.7.1/jquery-3.7.1.jar
2026-01-19T16:16:22.6673502Z Progress (1): 6.8 kB
2026-01-19T16:16:22.6673815Z                     
2026-01-19T16:16:22.6674229Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apiguardian/apiguardian-api/1.1.2/apiguardian-api-1.1.2.jar (6.8 kB at 6.9 kB/s)
2026-01-19T16:16:22.6682185Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-testng/7.27.2/cucumber-testng-7.27.2.jar
2026-01-19T16:16:22.6721874Z Progress (1): 16/90 kB
2026-01-19T16:16:22.6745365Z Progress (1): 33/90 kB
2026-01-19T16:16:22.6746132Z Progress (1): 49/90 kB
2026-01-19T16:16:22.6747167Z Progress (1): 57/90 kB
2026-01-19T16:16:22.6747736Z Progress (1): 74/90 kB
2026-01-19T16:16:22.6748191Z Progress (1): 90 kB   
2026-01-19T16:16:22.6748473Z                    
2026-01-19T16:16:22.6748867Z Downloaded from central: https://repo.maven.apache.org/maven2/org/jcommander/jcommander/1.83/jcommander-1.83.jar (90 kB at 90 kB/s)
2026-01-19T16:16:22.6755044Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-java/7.27.2/cucumber-java-7.27.2.jar
2026-01-19T16:16:22.6768664Z Progress (1): 4.1/308 kB
2026-01-19T16:16:22.6822387Z Progress (1): 20/308 kB 
2026-01-19T16:16:22.6822697Z Progress (1): 37/308 kB
2026-01-19T16:16:22.6822967Z Progress (1): 53/308 kB
2026-01-19T16:16:22.6823249Z Progress (1): 61/308 kB
2026-01-19T16:16:22.6823507Z Progress (1): 78/308 kB
2026-01-19T16:16:22.6823767Z Progress (1): 94/308 kB
2026-01-19T16:16:22.6824037Z Progress (2): 94/308 kB | 7.7/992 kB
2026-01-19T16:16:22.6824325Z Progress (2): 94/308 kB | 16/992 kB 
2026-01-19T16:16:22.6824605Z Progress (2): 94/308 kB | 32/992 kB
2026-01-19T16:16:22.6824889Z Progress (2): 94/308 kB | 49/992 kB
2026-01-19T16:16:22.6825166Z Progress (2): 94/308 kB | 65/992 kB
2026-01-19T16:16:22.6825438Z Progress (2): 94/308 kB | 81/992 kB
2026-01-19T16:16:22.6825724Z Progress (2): 94/308 kB | 98/992 kB
2026-01-19T16:16:22.6826006Z Progress (2): 94/308 kB | 114/992 kB
2026-01-19T16:16:22.6826289Z Progress (2): 94/308 kB | 131/992 kB
2026-01-19T16:16:22.6826744Z Progress (2): 94/308 kB | 147/992 kB
2026-01-19T16:16:22.6827033Z Progress (2): 111/308 kB | 147/992 kB
2026-01-19T16:16:22.6827562Z Progress (2): 127/308 kB | 147/992 kB
2026-01-19T16:16:22.6832174Z Progress (2): 143/308 kB | 147/992 kB
2026-01-19T16:16:22.6837778Z Progress (2): 160/308 kB | 147/992 kB
2026-01-19T16:16:22.6843067Z Progress (2): 160/308 kB | 163/992 kB
2026-01-19T16:16:22.6851434Z Progress (2): 160/308 kB | 180/992 kB
2026-01-19T16:16:22.6857820Z Progress (2): 176/308 kB | 180/992 kB
2026-01-19T16:16:22.6895309Z Progress (2): 193/308 kB | 180/992 kB
2026-01-19T16:16:22.6895898Z Progress (2): 193/308 kB | 196/992 kB
2026-01-19T16:16:22.6896463Z Progress (2): 193/308 kB | 213/992 kB
2026-01-19T16:16:22.6897151Z Progress (2): 209/308 kB | 213/992 kB
2026-01-19T16:16:22.6897641Z Progress (2): 209/308 kB | 229/992 kB
2026-01-19T16:16:22.6898100Z Progress (2): 225/308 kB | 229/992 kB
2026-01-19T16:16:22.6898575Z Progress (2): 225/308 kB | 245/992 kB
2026-01-19T16:16:22.6899058Z Progress (2): 242/308 kB | 245/992 kB
2026-01-19T16:16:22.6899514Z Progress (2): 258/308 kB | 245/992 kB
2026-01-19T16:16:22.6899985Z Progress (2): 262/308 kB | 245/992 kB
2026-01-19T16:16:22.6900451Z Progress (2): 279/308 kB | 245/992 kB
2026-01-19T16:16:22.6901689Z Progress (2): 295/308 kB | 245/992 kB
2026-01-19T16:16:22.6902347Z Progress (2): 308 kB | 245/992 kB    
2026-01-19T16:16:22.6903014Z                                  
2026-01-19T16:16:22.6903658Z Downloaded from central: https://repo.maven.apache.org/maven2/org/webjars/jquery/3.7.1/jquery-3.7.1.jar (308 kB at 306 kB/s)
2026-01-19T16:16:22.6904371Z Downloading from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-picocontainer/7.27.2/cucumber-picocontainer-7.27.2.jar
2026-01-19T16:16:22.6905027Z Progress (1): 262/992 kB
2026-01-19T16:16:22.6905599Z Progress (1): 278/992 kB
2026-01-19T16:16:22.6906063Z Progress (1): 294/992 kB
2026-01-19T16:16:22.6919313Z Progress (1): 311/992 kB
2026-01-19T16:16:22.6919880Z Progress (1): 327/992 kB
2026-01-19T16:16:22.6920367Z Progress (1): 344/992 kB
2026-01-19T16:16:22.6920666Z Progress (1): 360/992 kB
2026-01-19T16:16:22.6920968Z Progress (1): 376/992 kB
2026-01-19T16:16:22.6921266Z Progress (1): 393/992 kB
2026-01-19T16:16:22.6921593Z Progress (1): 409/992 kB
2026-01-19T16:16:22.6921890Z Progress (1): 426/992 kB
2026-01-19T16:16:22.6922187Z Progress (1): 442/992 kB
2026-01-19T16:16:22.6922475Z Progress (1): 458/992 kB
2026-01-19T16:16:22.6922763Z Progress (1): 475/992 kB
2026-01-19T16:16:22.6937159Z Progress (1): 491/992 kB
2026-01-19T16:16:22.6937498Z Progress (1): 507/992 kB
2026-01-19T16:16:22.6937833Z Progress (1): 524/992 kB
2026-01-19T16:16:22.6938210Z Progress (1): 540/992 kB
2026-01-19T16:16:22.6938552Z Progress (2): 540/992 kB | 7.7/22 kB
2026-01-19T16:16:22.6938897Z Progress (2): 540/992 kB | 16/22 kB 
2026-01-19T16:16:22.6939240Z Progress (2): 540/992 kB | 22 kB   
2026-01-19T16:16:22.6939569Z Progress (2): 557/992 kB | 22 kB
2026-01-19T16:16:22.6939899Z                                 
2026-01-19T16:16:22.6940325Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-testng/7.27.2/cucumber-testng-7.27.2.jar (22 kB at 21 kB/s)
2026-01-19T16:16:22.6944033Z Progress (1): 573/992 kB
2026-01-19T16:16:22.6946729Z Progress (1): 589/992 kB
2026-01-19T16:16:22.6949092Z Progress (2): 589/992 kB | 8.2/747 kB
2026-01-19T16:16:22.6960594Z Progress (2): 606/992 kB | 8.2/747 kB
2026-01-19T16:16:22.6978791Z Progress (2): 606/992 kB | 25/747 kB 
2026-01-19T16:16:22.6984566Z Progress (2): 622/992 kB | 25/747 kB
2026-01-19T16:16:22.6985164Z Progress (2): 639/992 kB | 25/747 kB
2026-01-19T16:16:22.6986998Z                                     
2026-01-19T16:16:22.6988331Z Downloading from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer/2.15.2/picocontainer-2.15.2.jar
2026-01-19T16:16:22.6990166Z Progress (2): 655/992 kB | 25/747 kB
2026-01-19T16:16:22.6992307Z Progress (2): 671/992 kB | 25/747 kB
2026-01-19T16:16:22.6994710Z Progress (2): 688/992 kB | 25/747 kB
2026-01-19T16:16:22.7017871Z Progress (2): 704/992 kB | 25/747 kB
2026-01-19T16:16:22.7018730Z Progress (2): 720/992 kB | 25/747 kB
2026-01-19T16:16:22.7019453Z Progress (2): 720/992 kB | 41/747 kB
2026-01-19T16:16:22.7020193Z Progress (2): 720/992 kB | 57/747 kB
2026-01-19T16:16:22.7020894Z Progress (2): 720/992 kB | 74/747 kB
2026-01-19T16:16:22.7021566Z Progress (2): 720/992 kB | 90/747 kB
2026-01-19T16:16:22.7022291Z Progress (2): 720/992 kB | 106/747 kB
2026-01-19T16:16:22.7022975Z Progress (2): 720/992 kB | 123/747 kB
2026-01-19T16:16:22.7023661Z Progress (2): 720/992 kB | 131/747 kB
2026-01-19T16:16:22.7024387Z Progress (2): 737/992 kB | 131/747 kB
2026-01-19T16:16:22.7025048Z Progress (2): 737/992 kB | 147/747 kB
2026-01-19T16:16:22.7025724Z Progress (2): 753/992 kB | 147/747 kB
2026-01-19T16:16:22.7026432Z Progress (2): 753/992 kB | 164/747 kB
2026-01-19T16:16:22.7028208Z Progress (2): 770/992 kB | 164/747 kB
2026-01-19T16:16:22.7029816Z Progress (2): 770/992 kB | 180/747 kB
2026-01-19T16:16:22.7030644Z Progress (2): 786/992 kB | 180/747 kB
2026-01-19T16:16:22.7031349Z Progress (2): 786/992 kB | 197/747 kB
2026-01-19T16:16:22.7032105Z Progress (2): 802/992 kB | 197/747 kB
2026-01-19T16:16:22.7032793Z Progress (2): 802/992 kB | 213/747 kB
2026-01-19T16:16:22.7033768Z Progress (2): 819/992 kB | 213/747 kB
2026-01-19T16:16:22.7034509Z Progress (2): 835/992 kB | 213/747 kB
2026-01-19T16:16:22.7035276Z Progress (2): 851/992 kB | 213/747 kB
2026-01-19T16:16:22.7035950Z Progress (2): 868/992 kB | 213/747 kB
2026-01-19T16:16:22.7036829Z Progress (2): 884/992 kB | 213/747 kB
2026-01-19T16:16:22.7048452Z Progress (2): 901/992 kB | 213/747 kB
2026-01-19T16:16:22.7050572Z Progress (2): 901/992 kB | 229/747 kB
2026-01-19T16:16:22.7051044Z Progress (2): 901/992 kB | 246/747 kB
2026-01-19T16:16:22.7055505Z Progress (2): 901/992 kB | 262/747 kB
2026-01-19T16:16:22.7060562Z Progress (2): 901/992 kB | 279/747 kB
2026-01-19T16:16:22.7065347Z Progress (2): 901/992 kB | 295/747 kB
2026-01-19T16:16:22.7067682Z Progress (2): 901/992 kB | 311/747 kB
2026-01-19T16:16:22.7068758Z Progress (2): 901/992 kB | 328/747 kB
2026-01-19T16:16:22.7069332Z Progress (2): 917/992 kB | 328/747 kB
2026-01-19T16:16:22.7069850Z Progress (2): 933/992 kB | 328/747 kB
2026-01-19T16:16:22.7070377Z Progress (2): 950/992 kB | 328/747 kB
2026-01-19T16:16:22.7071387Z Progress (2): 966/992 kB | 328/747 kB
2026-01-19T16:16:22.7071919Z Progress (2): 966/992 kB | 344/747 kB
2026-01-19T16:16:22.7072461Z Progress (2): 966/992 kB | 360/747 kB
2026-01-19T16:16:22.7073003Z Progress (2): 983/992 kB | 360/747 kB
2026-01-19T16:16:22.7073589Z Progress (2): 983/992 kB | 377/747 kB
2026-01-19T16:16:22.7075730Z Progress (2): 992 kB | 377/747 kB    
2026-01-19T16:16:22.7076284Z                                  
2026-01-19T16:16:22.7077603Z Downloaded from central: https://repo.maven.apache.org/maven2/org/testng/testng/7.11.0/testng-7.11.0.jar (992 kB at 967 kB/s)
2026-01-19T16:16:22.7088135Z Progress (1): 393/747 kB
2026-01-19T16:16:22.7089776Z Progress (1): 410/747 kB
2026-01-19T16:16:22.7090657Z Progress (1): 426/747 kB
2026-01-19T16:16:22.7091476Z Progress (2): 426/747 kB | 7.5/108 kB
2026-01-19T16:16:22.7092340Z                                      
2026-01-19T16:16:22.7093143Z Downloading from central: https://repo.maven.apache.org/maven2/net/masterthought/cucumber-reporting/5.8.3/cucumber-reporting-5.8.3.jar
2026-01-19T16:16:22.7100181Z Progress (2): 426/747 kB | 24/108 kB
2026-01-19T16:16:22.7119509Z Progress (2): 426/747 kB | 40/108 kB
2026-01-19T16:16:22.7119841Z Progress (2): 442/747 kB | 40/108 kB
2026-01-19T16:16:22.7120179Z Progress (2): 459/747 kB | 40/108 kB
2026-01-19T16:16:22.7122325Z Progress (2): 459/747 kB | 57/108 kB
2026-01-19T16:16:22.7122674Z Progress (2): 475/747 kB | 57/108 kB
2026-01-19T16:16:22.7124582Z Progress (2): 475/747 kB | 65/108 kB
2026-01-19T16:16:22.7124930Z Progress (2): 475/747 kB | 81/108 kB
2026-01-19T16:16:22.7125279Z Progress (2): 492/747 kB | 81/108 kB
2026-01-19T16:16:22.7125625Z Progress (2): 492/747 kB | 98/108 kB
2026-01-19T16:16:22.7125997Z Progress (2): 508/747 kB | 98/108 kB
2026-01-19T16:16:22.7126316Z Progress (2): 508/747 kB | 108 kB   
2026-01-19T16:16:22.7131708Z Progress (2): 524/747 kB | 108 kB
2026-01-19T16:16:22.7136710Z Progress (2): 541/747 kB | 108 kB
2026-01-19T16:16:22.7161216Z Progress (2): 557/747 kB | 108 kB
2026-01-19T16:16:22.7165939Z Progress (2): 573/747 kB | 108 kB
2026-01-19T16:16:22.7166888Z Progress (2): 590/747 kB | 108 kB
2026-01-19T16:16:22.7167348Z Progress (2): 606/747 kB | 108 kB
2026-01-19T16:16:22.7167803Z Progress (2): 623/747 kB | 108 kB
2026-01-19T16:16:22.7168307Z Progress (2): 639/747 kB | 108 kB
2026-01-19T16:16:22.7168803Z Progress (2): 655/747 kB | 108 kB
2026-01-19T16:16:22.7169251Z Progress (2): 672/747 kB | 108 kB
2026-01-19T16:16:22.7169677Z Progress (2): 688/747 kB | 108 kB
2026-01-19T16:16:22.7170104Z Progress (2): 705/747 kB | 108 kB
2026-01-19T16:16:22.7170593Z Progress (2): 721/747 kB | 108 kB
2026-01-19T16:16:22.7171069Z Progress (2): 737/747 kB | 108 kB
2026-01-19T16:16:22.7171492Z                                  
2026-01-19T16:16:22.7172732Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/datatable/7.27.2/datatable-7.27.2.jar (108 kB at 105 kB/s)
2026-01-19T16:16:22.7173298Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.18.0/jackson-datatype-jsr310-2.18.0.jar
2026-01-19T16:16:22.7188935Z Progress (1): 747 kB
2026-01-19T16:16:22.7189752Z                     
2026-01-19T16:16:22.7190336Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-java/7.27.2/cucumber-java-7.27.2.jar (747 kB at 721 kB/s)
2026-01-19T16:16:22.7191258Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.jar
2026-01-19T16:16:22.7208360Z Progress (1): 7.7/336 kB
2026-01-19T16:16:22.7211919Z Progress (1): 16/336 kB 
2026-01-19T16:16:22.7213187Z Progress (1): 29/336 kB
2026-01-19T16:16:22.7221124Z Progress (1): 45/336 kB
2026-01-19T16:16:22.7228545Z Progress (1): 61/336 kB
2026-01-19T16:16:22.7234035Z Progress (1): 78/336 kB
2026-01-19T16:16:22.7237379Z Progress (1): 94/336 kB
2026-01-19T16:16:22.7257752Z Progress (1): 111/336 kB
2026-01-19T16:16:22.7258333Z Progress (1): 127/336 kB
2026-01-19T16:16:22.7258812Z Progress (1): 143/336 kB
2026-01-19T16:16:22.7259259Z Progress (1): 160/336 kB
2026-01-19T16:16:22.7259708Z Progress (1): 176/336 kB
2026-01-19T16:16:22.7260206Z Progress (1): 193/336 kB
2026-01-19T16:16:22.7260649Z Progress (1): 209/336 kB
2026-01-19T16:16:22.7265432Z Progress (1): 225/336 kB
2026-01-19T16:16:22.7272383Z Progress (1): 242/336 kB
2026-01-19T16:16:22.7279524Z Progress (1): 258/336 kB
2026-01-19T16:16:22.7286318Z Progress (1): 274/336 kB
2026-01-19T16:16:22.7293711Z Progress (1): 291/336 kB
2026-01-19T16:16:22.7300611Z Progress (1): 307/336 kB
2026-01-19T16:16:22.7307024Z Progress (1): 324/336 kB
2026-01-19T16:16:22.7312680Z Progress (1): 336 kB    
2026-01-19T16:16:22.7315026Z                     
2026-01-19T16:16:22.7316201Z Downloaded from central: https://repo.maven.apache.org/maven2/org/picocontainer/picocontainer/2.15.2/picocontainer-2.15.2.jar (336 kB at 320 kB/s)
2026-01-19T16:16:22.7324840Z Downloading from central: https://repo.maven.apache.org/maven2/joda-time/joda-time/2.13.0/joda-time-2.13.0.jar
2026-01-19T16:16:22.7398073Z Progress (1): 7.7/531 kB
2026-01-19T16:16:22.7399652Z Progress (1): 16/531 kB 
2026-01-19T16:16:22.7402481Z Progress (1): 25/531 kB
2026-01-19T16:16:22.7402800Z Progress (1): 41/531 kB
2026-01-19T16:16:22.7403108Z Progress (1): 57/531 kB
2026-01-19T16:16:22.7403402Z Progress (1): 74/531 kB
2026-01-19T16:16:22.7403703Z Progress (1): 82/531 kB
2026-01-19T16:16:22.7404011Z Progress (1): 98/531 kB
2026-01-19T16:16:22.7431083Z Progress (1): 115/531 kB
2026-01-19T16:16:22.7433904Z Progress (1): 131/531 kB
2026-01-19T16:16:22.7435767Z Progress (1): 147/531 kB
2026-01-19T16:16:22.7438317Z Progress (1): 164/531 kB
2026-01-19T16:16:22.7441196Z Progress (1): 180/531 kB
2026-01-19T16:16:22.7443188Z Progress (1): 197/531 kB
2026-01-19T16:16:22.7445438Z Progress (1): 213/531 kB
2026-01-19T16:16:22.7448408Z Progress (1): 229/531 kB
2026-01-19T16:16:22.7451838Z Progress (1): 246/531 kB
2026-01-19T16:16:22.7453960Z Progress (2): 246/531 kB | 7.7/132 kB
2026-01-19T16:16:22.7456644Z Progress (2): 246/531 kB | 8.2/132 kB
2026-01-19T16:16:22.7457726Z Progress (2): 246/531 kB | 25/132 kB 
2026-01-19T16:16:22.7461079Z Progress (2): 246/531 kB | 41/132 kB
2026-01-19T16:16:22.7462074Z Progress (2): 246/531 kB | 57/132 kB
2026-01-19T16:16:22.7464735Z Progress (2): 246/531 kB | 74/132 kB
2026-01-19T16:16:22.7465555Z Progress (2): 246/531 kB | 90/132 kB
2026-01-19T16:16:22.7469014Z Progress (2): 246/531 kB | 106/132 kB
2026-01-19T16:16:22.7469512Z Progress (2): 246/531 kB | 123/132 kB
2026-01-19T16:16:22.7489534Z Progress (2): 246/531 kB | 132 kB    
2026-01-19T16:16:22.7490198Z Progress (2): 262/531 kB | 132 kB
2026-01-19T16:16:22.7490886Z Progress (2): 279/531 kB | 132 kB
2026-01-19T16:16:22.7493028Z Progress (2): 295/531 kB | 132 kB
2026-01-19T16:16:22.7493372Z Progress (2): 311/531 kB | 132 kB
2026-01-19T16:16:22.7498570Z Progress (2): 328/531 kB | 132 kB
2026-01-19T16:16:22.7498935Z Progress (2): 344/531 kB | 132 kB
2026-01-19T16:16:22.7499377Z                                  
2026-01-19T16:16:22.7499823Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/datatype/jackson-datatype-jsr310/2.18.0/jackson-datatype-jsr310-2.18.0.jar (132 kB at 123 kB/s)
2026-01-19T16:16:22.7500415Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-configuration2/2.11.0/commons-configuration2-2.11.0.jar
2026-01-19T16:16:22.7509125Z Progress (1): 360/531 kB
2026-01-19T16:16:22.7513269Z Progress (1): 377/531 kB
2026-01-19T16:16:22.7537874Z Progress (1): 393/531 kB
2026-01-19T16:16:22.7538478Z Progress (1): 410/531 kB
2026-01-19T16:16:22.7539012Z Progress (1): 426/531 kB
2026-01-19T16:16:22.7539782Z Progress (1): 442/531 kB
2026-01-19T16:16:22.7540278Z Progress (1): 459/531 kB
2026-01-19T16:16:22.7540586Z Progress (1): 475/531 kB
2026-01-19T16:16:22.7540890Z Progress (1): 492/531 kB
2026-01-19T16:16:22.7541182Z Progress (1): 508/531 kB
2026-01-19T16:16:22.7541484Z Progress (1): 524/531 kB
2026-01-19T16:16:22.7549548Z Progress (1): 531 kB    
2026-01-19T16:16:22.7550154Z                     
2026-01-19T16:16:22.7550824Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/velocity/velocity-engine-core/2.3/velocity-engine-core-2.3.jar (531 kB at 495 kB/s)
2026-01-19T16:16:22.7551648Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.11.0/commons-text-1.11.0.jar
2026-01-19T16:16:22.7567811Z Progress (1): 7.7/639 kB
2026-01-19T16:16:22.7607714Z Progress (1): 16/639 kB 
2026-01-19T16:16:22.7608568Z Progress (1): 32/639 kB
2026-01-19T16:16:22.7609596Z Progress (1): 49/639 kB
2026-01-19T16:16:22.7610097Z Progress (1): 65/639 kB
2026-01-19T16:16:22.7610592Z Progress (1): 66/639 kB
2026-01-19T16:16:22.7611283Z Progress (1): 82/639 kB
2026-01-19T16:16:22.7611769Z Progress (1): 98/639 kB
2026-01-19T16:16:22.7612235Z Progress (1): 115/639 kB
2026-01-19T16:16:22.7612715Z Progress (1): 131/639 kB
2026-01-19T16:16:22.7613194Z Progress (1): 147/639 kB
2026-01-19T16:16:22.7613673Z Progress (1): 164/639 kB
2026-01-19T16:16:22.7614174Z Progress (1): 180/639 kB
2026-01-19T16:16:22.7614802Z Progress (1): 197/639 kB
2026-01-19T16:16:22.7615270Z Progress (1): 213/639 kB
2026-01-19T16:16:22.7636818Z Progress (1): 229/639 kB
2026-01-19T16:16:22.7641048Z Progress (1): 246/639 kB
2026-01-19T16:16:22.7641618Z Progress (1): 262/639 kB
2026-01-19T16:16:22.7642109Z Progress (1): 279/639 kB
2026-01-19T16:16:22.7642636Z Progress (1): 295/639 kB
2026-01-19T16:16:22.7649134Z Progress (1): 311/639 kB
2026-01-19T16:16:22.7655640Z Progress (1): 328/639 kB
2026-01-19T16:16:22.7661189Z Progress (1): 344/639 kB
2026-01-19T16:16:22.7687420Z Progress (1): 360/639 kB
2026-01-19T16:16:22.7692381Z Progress (1): 377/639 kB
2026-01-19T16:16:22.7694403Z Progress (1): 393/639 kB
2026-01-19T16:16:22.7694930Z Progress (1): 410/639 kB
2026-01-19T16:16:22.7695439Z Progress (1): 426/639 kB
2026-01-19T16:16:22.7696001Z Progress (1): 442/639 kB
2026-01-19T16:16:22.7696626Z Progress (1): 459/639 kB
2026-01-19T16:16:22.7697141Z Progress (1): 475/639 kB
2026-01-19T16:16:22.7697676Z Progress (1): 492/639 kB
2026-01-19T16:16:22.7698305Z Progress (1): 508/639 kB
2026-01-19T16:16:22.7698646Z Progress (1): 524/639 kB
2026-01-19T16:16:22.7702885Z Progress (2): 524/639 kB | 5.3 kB
2026-01-19T16:16:22.7703359Z                                  
2026-01-19T16:16:22.7703910Z Downloaded from central: https://repo.maven.apache.org/maven2/io/cucumber/cucumber-picocontainer/7.27.2/cucumber-picocontainer-7.27.2.jar (5.3 kB at 4.9 kB/s)
2026-01-19T16:16:22.7717692Z Downloading from central: https://repo.maven.apache.org/maven2/org/jsoup/jsoup/1.18.1/jsoup-1.18.1.jar
2026-01-19T16:16:22.7737239Z Progress (1): 541/639 kB
2026-01-19T16:16:22.7737942Z Progress (1): 557/639 kB
2026-01-19T16:16:22.7738517Z Progress (1): 573/639 kB
2026-01-19T16:16:22.7739086Z Progress (1): 590/639 kB
2026-01-19T16:16:22.7739644Z Progress (1): 606/639 kB
2026-01-19T16:16:22.7740215Z Progress (1): 623/639 kB
2026-01-19T16:16:22.7740740Z Progress (1): 639/639 kB
2026-01-19T16:16:22.7767964Z Progress (1): 639 kB    
2026-01-19T16:16:22.7768634Z                     
2026-01-19T16:16:22.7769359Z Downloaded from central: https://repo.maven.apache.org/maven2/joda-time/joda-time/2.13.0/joda-time-2.13.0.jar (639 kB at 584 kB/s)
2026-01-19T16:16:22.7770254Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/owasp-java-html-sanitizer/20240325.1/owasp-java-html-sanitizer-20240325.1.jar
2026-01-19T16:16:22.7771037Z Progress (1): 7.7/247 kB
2026-01-19T16:16:22.7771621Z Progress (1): 16/247 kB 
2026-01-19T16:16:22.7772211Z Progress (1): 29/247 kB
2026-01-19T16:16:22.7772795Z Progress (1): 45/247 kB
2026-01-19T16:16:22.7773595Z Progress (1): 61/247 kB
2026-01-19T16:16:22.7774184Z Progress (1): 78/247 kB
2026-01-19T16:16:22.7774767Z Progress (1): 94/247 kB
2026-01-19T16:16:22.7775327Z Progress (1): 111/247 kB
2026-01-19T16:16:22.7775945Z Progress (1): 127/247 kB
2026-01-19T16:16:22.7776944Z Progress (1): 143/247 kB
2026-01-19T16:16:22.7777579Z Progress (1): 160/247 kB
2026-01-19T16:16:22.7778197Z Progress (1): 176/247 kB
2026-01-19T16:16:22.7778784Z Progress (1): 193/247 kB
2026-01-19T16:16:22.7788529Z Progress (1): 209/247 kB
2026-01-19T16:16:22.7794766Z Progress (1): 225/247 kB
2026-01-19T16:16:22.7800789Z Progress (1): 242/247 kB
2026-01-19T16:16:22.7809883Z Progress (1): 247 kB    
2026-01-19T16:16:22.7814868Z                     
2026-01-19T16:16:22.7822204Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-text/1.11.0/commons-text-1.11.0.jar (247 kB at 224 kB/s)
2026-01-19T16:16:22.7825523Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java8-shim/20240325.1/java8-shim-20240325.1.jar
2026-01-19T16:16:22.7828882Z Progress (1): 7.7/665 kB
2026-01-19T16:16:22.7831007Z Progress (1): 16/665 kB 
2026-01-19T16:16:22.7831667Z Progress (1): 32/665 kB
2026-01-19T16:16:22.7833529Z Progress (1): 49/665 kB
2026-01-19T16:16:22.7835403Z Progress (1): 65/665 kB
2026-01-19T16:16:22.7847831Z Progress (1): 81/665 kB
2026-01-19T16:16:22.7849611Z Progress (1): 98/665 kB
2026-01-19T16:16:22.7849932Z Progress (1): 114/665 kB
2026-01-19T16:16:22.7850236Z Progress (1): 131/665 kB
2026-01-19T16:16:22.7850537Z Progress (1): 147/665 kB
2026-01-19T16:16:22.7857184Z Progress (1): 163/665 kB
2026-01-19T16:16:22.7861786Z Progress (1): 180/665 kB
2026-01-19T16:16:22.7869169Z Progress (1): 196/665 kB
2026-01-19T16:16:22.7874662Z Progress (1): 213/665 kB
2026-01-19T16:16:22.7881088Z Progress (1): 229/665 kB
2026-01-19T16:16:22.7888102Z Progress (1): 245/665 kB
2026-01-19T16:16:22.7888436Z Progress (1): 262/665 kB
2026-01-19T16:16:22.7891828Z Progress (1): 278/665 kB
2026-01-19T16:16:22.7893646Z Progress (1): 294/665 kB
2026-01-19T16:16:22.7901697Z Progress (1): 311/665 kB
2026-01-19T16:16:22.7902336Z Progress (1): 327/665 kB
2026-01-19T16:16:22.7910990Z Progress (1): 344/665 kB
2026-01-19T16:16:22.7917744Z Progress (1): 360/665 kB
2026-01-19T16:16:22.7918376Z Progress (1): 376/665 kB
2026-01-19T16:16:22.7943437Z Progress (2): 376/665 kB | 8.2/453 kB
2026-01-19T16:16:22.7944086Z Progress (2): 376/665 kB | 25/453 kB 
2026-01-19T16:16:22.7945374Z Progress (2): 376/665 kB | 41/453 kB
2026-01-19T16:16:22.7947008Z Progress (2): 376/665 kB | 57/453 kB
2026-01-19T16:16:22.7948033Z Progress (2): 376/665 kB | 66/453 kB
2026-01-19T16:16:22.7948576Z Progress (2): 376/665 kB | 82/453 kB
2026-01-19T16:16:22.7949314Z Progress (2): 376/665 kB | 98/453 kB
2026-01-19T16:16:22.7949802Z Progress (2): 376/665 kB | 115/453 kB
2026-01-19T16:16:22.7950135Z Progress (2): 376/665 kB | 131/453 kB
2026-01-19T16:16:22.7950450Z Progress (2): 393/665 kB | 131/453 kB
2026-01-19T16:16:22.7950787Z Progress (2): 409/665 kB | 131/453 kB
2026-01-19T16:16:22.7951101Z Progress (2): 426/665 kB | 131/453 kB
2026-01-19T16:16:22.7951422Z Progress (2): 442/665 kB | 131/453 kB
2026-01-19T16:16:22.7951732Z Progress (2): 458/665 kB | 131/453 kB
2026-01-19T16:16:22.7952049Z Progress (2): 475/665 kB | 131/453 kB
2026-01-19T16:16:22.7959885Z Progress (2): 491/665 kB | 131/453 kB
2026-01-19T16:16:22.8056155Z Progress (2): 507/665 kB | 131/453 kB
2026-01-19T16:16:22.8058385Z Progress (2): 524/665 kB | 131/453 kB
2026-01-19T16:16:22.8060803Z Progress (2): 540/665 kB | 131/453 kB
2026-01-19T16:16:22.8061358Z Progress (2): 557/665 kB | 131/453 kB
2026-01-19T16:16:22.8061898Z Progress (2): 573/665 kB | 131/453 kB
2026-01-19T16:16:22.8062397Z Progress (2): 589/665 kB | 131/453 kB
2026-01-19T16:16:22.8063194Z Progress (2): 606/665 kB | 131/453 kB
2026-01-19T16:16:22.8063733Z Progress (2): 622/665 kB | 131/453 kB
2026-01-19T16:16:22.8064714Z Progress (2): 639/665 kB | 131/453 kB
2026-01-19T16:16:22.8065268Z Progress (2): 655/665 kB | 131/453 kB
2026-01-19T16:16:22.8067366Z Progress (2): 655/665 kB | 147/453 kB
2026-01-19T16:16:22.8067794Z Progress (2): 655/665 kB | 164/453 kB
2026-01-19T16:16:22.8068226Z Progress (2): 655/665 kB | 180/453 kB
2026-01-19T16:16:22.8068562Z Progress (2): 655/665 kB | 197/453 kB
2026-01-19T16:16:22.8068913Z Progress (2): 655/665 kB | 213/453 kB
2026-01-19T16:16:22.8069246Z Progress (2): 655/665 kB | 229/453 kB
2026-01-19T16:16:22.8069584Z Progress (2): 655/665 kB | 246/453 kB
2026-01-19T16:16:22.8069913Z Progress (2): 655/665 kB | 262/453 kB
2026-01-19T16:16:22.8070249Z Progress (2): 655/665 kB | 279/453 kB
2026-01-19T16:16:22.8070558Z Progress (2): 655/665 kB | 295/453 kB
2026-01-19T16:16:22.8070888Z Progress (2): 655/665 kB | 311/453 kB
2026-01-19T16:16:22.8071413Z Progress (2): 655/665 kB | 328/453 kB
2026-01-19T16:16:22.8071989Z Progress (2): 655/665 kB | 344/453 kB
2026-01-19T16:16:22.8072317Z Progress (2): 655/665 kB | 360/453 kB
2026-01-19T16:16:22.8072642Z Progress (2): 655/665 kB | 377/453 kB
2026-01-19T16:16:22.8072983Z Progress (2): 655/665 kB | 393/453 kB
2026-01-19T16:16:22.8073323Z Progress (3): 655/665 kB | 393/453 kB | 7.7/242 kB
2026-01-19T16:16:22.8073682Z Progress (3): 655/665 kB | 393/453 kB | 12/242 kB 
2026-01-19T16:16:22.8074028Z Progress (3): 655/665 kB | 393/453 kB | 29/242 kB
2026-01-19T16:16:22.8074397Z Progress (3): 655/665 kB | 393/453 kB | 45/242 kB
2026-01-19T16:16:22.8074761Z Progress (3): 655/665 kB | 393/453 kB | 61/242 kB
2026-01-19T16:16:22.8075827Z Progress (3): 655/665 kB | 393/453 kB | 78/242 kB
2026-01-19T16:16:22.8076277Z Progress (3): 655/665 kB | 393/453 kB | 94/242 kB
2026-01-19T16:16:22.8076854Z Progress (3): 655/665 kB | 393/453 kB | 111/242 kB
2026-01-19T16:16:22.8077226Z Progress (3): 655/665 kB | 393/453 kB | 127/242 kB
2026-01-19T16:16:22.8077597Z Progress (3): 655/665 kB | 393/453 kB | 143/242 kB
2026-01-19T16:16:22.8077912Z Progress (3): 655/665 kB | 393/453 kB | 160/242 kB
2026-01-19T16:16:22.8078237Z Progress (3): 655/665 kB | 393/453 kB | 176/242 kB
2026-01-19T16:16:22.8078593Z Progress (3): 655/665 kB | 393/453 kB | 193/242 kB
2026-01-19T16:16:22.8078923Z Progress (3): 655/665 kB | 393/453 kB | 209/242 kB
2026-01-19T16:16:22.8079231Z Progress (3): 655/665 kB | 393/453 kB | 225/242 kB
2026-01-19T16:16:22.8079578Z Progress (3): 655/665 kB | 393/453 kB | 242/242 kB
2026-01-19T16:16:22.8079914Z Progress (3): 655/665 kB | 393/453 kB | 242 kB    
2026-01-19T16:16:22.8080497Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 7.7/936 kB
2026-01-19T16:16:22.8081130Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 16/936 kB 
2026-01-19T16:16:22.8081464Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 32/936 kB
2026-01-19T16:16:22.8081808Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 49/936 kB
2026-01-19T16:16:22.8082169Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 49/936 kB
2026-01-19T16:16:22.8082492Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 66/936 kB
2026-01-19T16:16:22.8082820Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 82/936 kB
2026-01-19T16:16:22.8083750Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 98/936 kB
2026-01-19T16:16:22.8084112Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 115/936 kB
2026-01-19T16:16:22.8084469Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 131/936 kB
2026-01-19T16:16:22.8084892Z Progress (5): 655/665 kB | 393/453 kB | 242 kB | 131/936 kB | 7.7/12 kB
2026-01-19T16:16:22.8085371Z Progress (5): 655/665 kB | 393/453 kB | 242 kB | 131/936 kB | 8.2/12 kB
2026-01-19T16:16:22.8085737Z Progress (5): 655/665 kB | 393/453 kB | 242 kB | 131/936 kB | 12 kB    
2026-01-19T16:16:22.8086066Z Progress (5): 655/665 kB | 393/453 kB | 242 kB | 147/936 kB | 12 kB
2026-01-19T16:16:22.8086423Z Progress (5): 655/665 kB | 393/453 kB | 242 kB | 164/936 kB | 12 kB
2026-01-19T16:16:22.8111656Z Progress (5): 655/665 kB | 393/453 kB | 242 kB | 180/936 kB | 12 kB
2026-01-19T16:16:22.8112025Z Progress (5): 655/665 kB | 393/453 kB | 242 kB | 197/936 kB | 12 kB
2026-01-19T16:16:22.8112351Z                                                                    
2026-01-19T16:16:22.8113073Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java8-shim/20240325.1/java8-shim-20240325.1.jar (12 kB at 10 kB/s)
2026-01-19T16:16:22.8113687Z Downloading from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java10-shim/20240325.1/java10-shim-20240325.1.jar
2026-01-19T16:16:22.8114202Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 213/936 kB
2026-01-19T16:16:22.8114805Z Progress (4): 655/665 kB | 393/453 kB | 242 kB | 229/936 kB
2026-01-19T16:16:22.8115198Z Progress (4): 665 kB | 393/453 kB | 242 kB | 229/936 kB    
2026-01-19T16:16:22.8115576Z Progress (4): 665 kB | 393/453 kB | 242 kB | 246/936 kB
2026-01-19T16:16:22.8115945Z Progress (4): 665 kB | 393/453 kB | 242 kB | 262/936 kB
2026-01-19T16:16:22.8116313Z Progress (4): 665 kB | 393/453 kB | 242 kB | 279/936 kB
2026-01-19T16:16:22.8117362Z                                                        
2026-01-19T16:16:22.8117819Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-configuration2/2.11.0/commons-configuration2-2.11.0.jar (665 kB at 591 kB/s)
2026-01-19T16:16:22.8118432Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/jcl-over-slf4j/2.0.16/jcl-over-slf4j-2.0.16.jar
2026-01-19T16:16:22.8120768Z Progress (3): 393/453 kB | 242 kB | 295/936 kB
2026-01-19T16:16:22.8121114Z Progress (3): 393/453 kB | 242 kB | 311/936 kB
2026-01-19T16:16:22.8121460Z Progress (3): 393/453 kB | 242 kB | 328/936 kB
2026-01-19T16:16:22.8121777Z Progress (3): 393/453 kB | 242 kB | 344/936 kB
2026-01-19T16:16:22.8122086Z Progress (3): 393/453 kB | 242 kB | 360/936 kB
2026-01-19T16:16:22.8122417Z Progress (3): 393/453 kB | 242 kB | 377/936 kB
2026-01-19T16:16:22.8122754Z Progress (3): 393/453 kB | 242 kB | 393/936 kB
2026-01-19T16:16:22.8123059Z Progress (3): 393/453 kB | 242 kB | 410/936 kB
2026-01-19T16:16:22.8123726Z Progress (3): 393/453 kB | 242 kB | 426/936 kB
2026-01-19T16:16:22.8124074Z Progress (3): 410/453 kB | 242 kB | 426/936 kB
2026-01-19T16:16:22.8124387Z Progress (3): 426/453 kB | 242 kB | 426/936 kB
2026-01-19T16:16:22.8124722Z Progress (3): 442/453 kB | 242 kB | 426/936 kB
2026-01-19T16:16:22.8125053Z Progress (3): 453 kB | 242 kB | 426/936 kB    
2026-01-19T16:16:22.8125328Z                                           
2026-01-19T16:16:22.8126212Z Downloaded from central: https://repo.maven.apache.org/maven2/org/jsoup/jsoup/1.18.1/jsoup-1.18.1.jar (453 kB at 401 kB/s)
2026-01-19T16:16:22.8127074Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.17.1/jackson-databind-2.17.1.jar
2026-01-19T16:16:22.8143054Z Progress (2): 242 kB | 442/936 kB
2026-01-19T16:16:22.8143593Z Progress (2): 242 kB | 459/936 kB
2026-01-19T16:16:22.8144916Z Progress (2): 242 kB | 475/936 kB
2026-01-19T16:16:22.8173994Z Progress (2): 242 kB | 492/936 kB
2026-01-19T16:16:22.8174726Z Progress (2): 242 kB | 508/936 kB
2026-01-19T16:16:22.8175261Z Progress (2): 242 kB | 524/936 kB
2026-01-19T16:16:22.8175770Z Progress (2): 242 kB | 541/936 kB
2026-01-19T16:16:22.8176805Z Progress (2): 242 kB | 557/936 kB
2026-01-19T16:16:22.8177133Z Progress (2): 242 kB | 573/936 kB
2026-01-19T16:16:22.8177442Z Progress (2): 242 kB | 590/936 kB
2026-01-19T16:16:22.8177927Z Progress (2): 242 kB | 606/936 kB
2026-01-19T16:16:22.8178246Z Progress (2): 242 kB | 623/936 kB
2026-01-19T16:16:22.8178553Z Progress (2): 242 kB | 639/936 kB
2026-01-19T16:16:22.8178833Z                                  
2026-01-19T16:16:22.8179304Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/owasp-java-html-sanitizer/20240325.1/owasp-java-html-sanitizer-20240325.1.jar (242 kB at 214 kB/s)
2026-01-19T16:16:22.8179956Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.17.1/jackson-annotations-2.17.1.jar
2026-01-19T16:16:22.8180420Z Progress (1): 655/936 kB
2026-01-19T16:16:22.8180881Z Progress (1): 672/936 kB
2026-01-19T16:16:22.8181253Z Progress (1): 688/936 kB
2026-01-19T16:16:22.8181570Z Progress (1): 705/936 kB
2026-01-19T16:16:22.8181886Z Progress (1): 721/936 kB
2026-01-19T16:16:22.8182190Z Progress (1): 737/936 kB
2026-01-19T16:16:22.8182503Z Progress (1): 754/936 kB
2026-01-19T16:16:22.8182811Z Progress (1): 770/936 kB
2026-01-19T16:16:22.8183124Z Progress (1): 786/936 kB
2026-01-19T16:16:22.8183433Z Progress (1): 803/936 kB
2026-01-19T16:16:22.8183739Z Progress (1): 819/936 kB
2026-01-19T16:16:22.8184060Z Progress (1): 836/936 kB
2026-01-19T16:16:22.8184369Z Progress (1): 852/936 kB
2026-01-19T16:16:22.8184684Z Progress (1): 868/936 kB
2026-01-19T16:16:22.8184985Z Progress (1): 885/936 kB
2026-01-19T16:16:22.8185293Z Progress (1): 901/936 kB
2026-01-19T16:16:22.8185599Z Progress (1): 918/936 kB
2026-01-19T16:16:22.8185910Z Progress (1): 934/936 kB
2026-01-19T16:16:22.8186213Z Progress (1): 936 kB    
2026-01-19T16:16:22.8186710Z                     
2026-01-19T16:16:22.8187148Z Downloaded from central: https://repo.maven.apache.org/maven2/net/masterthought/cucumber-reporting/5.8.3/cucumber-reporting-5.8.3.jar (936 kB at 824 kB/s)
2026-01-19T16:16:22.8187711Z Downloading from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.17.1/jackson-core-2.17.1.jar
2026-01-19T16:16:22.8287233Z Progress (1): 3.9 kB
2026-01-19T16:16:22.8288587Z                     
2026-01-19T16:16:22.8289165Z Downloaded from central: https://repo.maven.apache.org/maven2/com/googlecode/owasp-java-html-sanitizer/java10-shim/20240325.1/java10-shim-20240325.1.jar (3.9 kB at 3.4 kB/s)
2026-01-19T16:16:22.8295270Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/2.0.16/slf4j-simple-2.0.16.jar
2026-01-19T16:16:22.8337860Z Progress (1): 0/1.6 MB
2026-01-19T16:16:22.8343493Z Progress (1): 0/1.6 MB
2026-01-19T16:16:22.8347776Z Progress (2): 0/1.6 MB | 7.7/18 kB
2026-01-19T16:16:22.8348374Z Progress (2): 0/1.6 MB | 7.7/18 kB
2026-01-19T16:16:22.8352357Z Progress (2): 0.1/1.6 MB | 7.7/18 kB
2026-01-19T16:16:22.8352954Z Progress (2): 0.1/1.6 MB | 7.7/18 kB
2026-01-19T16:16:22.8357095Z Progress (2): 0.1/1.6 MB | 7.7/18 kB
2026-01-19T16:16:22.8357689Z Progress (2): 0.1/1.6 MB | 18 kB    
2026-01-19T16:16:22.8358223Z Progress (2): 0.1/1.6 MB | 18 kB
2026-01-19T16:16:22.8358829Z Progress (2): 0.1/1.6 MB | 18 kB
2026-01-19T16:16:22.8373186Z Progress (2): 0.1/1.6 MB | 18 kB
2026-01-19T16:16:22.8374444Z Progress (2): 0.1/1.6 MB | 18 kB
2026-01-19T16:16:22.8374779Z Progress (2): 0.1/1.6 MB | 18 kB
2026-01-19T16:16:22.8375123Z Progress (2): 0.2/1.6 MB | 18 kB
2026-01-19T16:16:22.8375446Z Progress (2): 0.2/1.6 MB | 18 kB
2026-01-19T16:16:22.8375784Z Progress (2): 0.2/1.6 MB | 18 kB
2026-01-19T16:16:22.8376105Z Progress (2): 0.2/1.6 MB | 18 kB
2026-01-19T16:16:22.8376433Z Progress (2): 0.2/1.6 MB | 18 kB
2026-01-19T16:16:22.8376941Z Progress (2): 0.2/1.6 MB | 18 kB
2026-01-19T16:16:22.8377257Z Progress (2): 0.3/1.6 MB | 18 kB
2026-01-19T16:16:22.8377595Z Progress (2): 0.3/1.6 MB | 18 kB
2026-01-19T16:16:22.8377931Z Progress (2): 0.3/1.6 MB | 18 kB
2026-01-19T16:16:22.8427165Z Progress (2): 0.3/1.6 MB | 18 kB
2026-01-19T16:16:22.8428140Z Progress (2): 0.3/1.6 MB | 18 kB
2026-01-19T16:16:22.8428683Z Progress (2): 0.3/1.6 MB | 18 kB
2026-01-19T16:16:22.8447209Z Progress (2): 0.3/1.6 MB | 18 kB
2026-01-19T16:16:22.8467279Z                                 
2026-01-19T16:16:22.8475805Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/jcl-over-slf4j/2.0.16/jcl-over-slf4j-2.0.16.jar (18 kB at 16 kB/s)
2026-01-19T16:16:22.8476747Z Downloading from central: https://repo.maven.apache.org/maven2/com/aventstack/extentreports/5.1.1/extentreports-5.1.1.jar
2026-01-19T16:16:22.8480451Z Progress (2): 0.3/1.6 MB | 4.1/582 kB
2026-01-19T16:16:22.8480804Z Progress (2): 0.3/1.6 MB | 20/582 kB 
2026-01-19T16:16:22.8481139Z Progress (2): 0.3/1.6 MB | 37/582 kB
2026-01-19T16:16:22.8481491Z Progress (2): 0.3/1.6 MB | 53/582 kB
2026-01-19T16:16:22.8481974Z Progress (2): 0.3/1.6 MB | 70/582 kB
2026-01-19T16:16:22.8482326Z Progress (2): 0.3/1.6 MB | 70/582 kB
2026-01-19T16:16:22.8482670Z Progress (2): 0.3/1.6 MB | 86/582 kB
2026-01-19T16:16:22.8483018Z Progress (2): 0.3/1.6 MB | 102/582 kB
2026-01-19T16:16:22.8483356Z Progress (2): 0.4/1.6 MB | 102/582 kB
2026-01-19T16:16:22.8483704Z Progress (2): 0.4/1.6 MB | 119/582 kB
2026-01-19T16:16:22.8484034Z Progress (2): 0.4/1.6 MB | 119/582 kB
2026-01-19T16:16:22.8484372Z Progress (2): 0.4/1.6 MB | 135/582 kB
2026-01-19T16:16:22.8484717Z Progress (2): 0.4/1.6 MB | 152/582 kB
2026-01-19T16:16:22.8485259Z Progress (2): 0.4/1.6 MB | 152/582 kB
2026-01-19T16:16:22.8485563Z Progress (2): 0.4/1.6 MB | 168/582 kB
2026-01-19T16:16:22.8486114Z Progress (2): 0.4/1.6 MB | 168/582 kB
2026-01-19T16:16:22.8486657Z Progress (2): 0.4/1.6 MB | 184/582 kB
2026-01-19T16:16:22.8487570Z Progress (2): 0.4/1.6 MB | 184/582 kB
2026-01-19T16:16:22.8487925Z Progress (2): 0.4/1.6 MB | 184/582 kB
2026-01-19T16:16:22.8488278Z Progress (2): 0.5/1.6 MB | 184/582 kB
2026-01-19T16:16:22.8488667Z Progress (2): 0.5/1.6 MB | 184/582 kB
2026-01-19T16:16:22.8489010Z Progress (2): 0.5/1.6 MB | 184/582 kB
2026-01-19T16:16:22.8489347Z Progress (2): 0.5/1.6 MB | 201/582 kB
2026-01-19T16:16:22.8489791Z Progress (2): 0.5/1.6 MB | 201/582 kB
2026-01-19T16:16:22.8490141Z Progress (2): 0.5/1.6 MB | 201/582 kB
2026-01-19T16:16:22.8490458Z Progress (2): 0.5/1.6 MB | 217/582 kB
2026-01-19T16:16:22.8490780Z Progress (2): 0.5/1.6 MB | 217/582 kB
2026-01-19T16:16:22.8491135Z Progress (3): 0.5/1.6 MB | 217/582 kB | 7.7/78 kB
2026-01-19T16:16:22.8491491Z Progress (3): 0.5/1.6 MB | 217/582 kB | 16/78 kB 
2026-01-19T16:16:22.8491840Z Progress (3): 0.5/1.6 MB | 217/582 kB | 32/78 kB
2026-01-19T16:16:22.8492180Z Progress (3): 0.5/1.6 MB | 217/582 kB | 49/78 kB
2026-01-19T16:16:22.8492538Z Progress (3): 0.5/1.6 MB | 217/582 kB | 65/78 kB
2026-01-19T16:16:22.8492854Z Progress (3): 0.5/1.6 MB | 217/582 kB | 78 kB   
2026-01-19T16:16:22.8493197Z Progress (3): 0.5/1.6 MB | 233/582 kB | 78 kB
2026-01-19T16:16:22.8493557Z Progress (3): 0.5/1.6 MB | 250/582 kB | 78 kB
2026-01-19T16:16:22.8493894Z Progress (3): 0.5/1.6 MB | 262/582 kB | 78 kB
2026-01-19T16:16:22.8494241Z Progress (3): 0.5/1.6 MB | 279/582 kB | 78 kB
2026-01-19T16:16:22.8494786Z Progress (3): 0.5/1.6 MB | 295/582 kB | 78 kB
2026-01-19T16:16:22.8495150Z Progress (3): 0.5/1.6 MB | 311/582 kB | 78 kB
2026-01-19T16:16:22.8495492Z Progress (3): 0.5/1.6 MB | 328/582 kB | 78 kB
2026-01-19T16:16:22.8495846Z Progress (3): 0.5/1.6 MB | 344/582 kB | 78 kB
2026-01-19T16:16:22.8496895Z Progress (3): 0.5/1.6 MB | 360/582 kB | 78 kB
2026-01-19T16:16:22.8497284Z Progress (3): 0.5/1.6 MB | 377/582 kB | 78 kB
2026-01-19T16:16:22.8497631Z Progress (3): 0.5/1.6 MB | 393/582 kB | 78 kB
2026-01-19T16:16:22.8497982Z Progress (3): 0.5/1.6 MB | 410/582 kB | 78 kB
2026-01-19T16:16:22.8498324Z Progress (3): 0.5/1.6 MB | 410/582 kB | 78 kB
2026-01-19T16:16:22.8498682Z Progress (3): 0.5/1.6 MB | 426/582 kB | 78 kB
2026-01-19T16:16:22.8499025Z Progress (3): 0.6/1.6 MB | 426/582 kB | 78 kB
2026-01-19T16:16:22.8499380Z Progress (3): 0.6/1.6 MB | 442/582 kB | 78 kB
2026-01-19T16:16:22.8499711Z Progress (3): 0.6/1.6 MB | 442/582 kB | 78 kB
2026-01-19T16:16:22.8500057Z Progress (3): 0.6/1.6 MB | 442/582 kB | 78 kB
2026-01-19T16:16:22.8500390Z Progress (3): 0.6/1.6 MB | 459/582 kB | 78 kB
2026-01-19T16:16:22.8500886Z Progress (3): 0.6/1.6 MB | 459/582 kB | 78 kB
2026-01-19T16:16:22.8501240Z Progress (3): 0.6/1.6 MB | 475/582 kB | 78 kB
2026-01-19T16:16:22.8501582Z Progress (3): 0.6/1.6 MB | 475/582 kB | 78 kB
2026-01-19T16:16:22.8501922Z Progress (3): 0.6/1.6 MB | 492/582 kB | 78 kB
2026-01-19T16:16:22.8502239Z Progress (3): 0.6/1.6 MB | 492/582 kB | 78 kB
2026-01-19T16:16:22.8504006Z Progress (3): 0.6/1.6 MB | 508/582 kB | 78 kB
2026-01-19T16:16:22.8505130Z Progress (4): 0.6/1.6 MB | 508/582 kB | 78 kB | 7.7/16 kB
2026-01-19T16:16:22.8505473Z Progress (4): 0.6/1.6 MB | 508/582 kB | 78 kB | 16 kB    
2026-01-19T16:16:22.8505764Z                                                      
2026-01-19T16:16:22.8506313Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-simple/2.0.16/slf4j-simple-2.0.16.jar (16 kB at 13 kB/s)
2026-01-19T16:16:22.8507624Z Downloading from central: https://repo.maven.apache.org/maven2/io/reactivex/rxjava3/rxjava/3.1.6/rxjava-3.1.6.jar
2026-01-19T16:16:22.8512638Z Progress (3): 0.6/1.6 MB | 524/582 kB | 78 kB
2026-01-19T16:16:22.8513862Z Progress (3): 0.6/1.6 MB | 541/582 kB | 78 kB
2026-01-19T16:16:22.8514633Z Progress (3): 0.6/1.6 MB | 557/582 kB | 78 kB
2026-01-19T16:16:22.8515122Z Progress (3): 0.6/1.6 MB | 573/582 kB | 78 kB
2026-01-19T16:16:22.8516980Z Progress (3): 0.6/1.6 MB | 582 kB | 78 kB    
2026-01-19T16:16:22.8517317Z                                          
2026-01-19T16:16:22.8517734Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-annotations/2.17.1/jackson-annotations-2.17.1.jar (78 kB at 67 kB/s)
2026-01-19T16:16:22.8521026Z Downloading from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.jar
2026-01-19T16:16:22.8547402Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-core/2.17.1/jackson-core-2.17.1.jar (582 kB at 497 kB/s)
2026-01-19T16:16:22.8548266Z Downloading from central: https://repo.maven.apache.org/maven2/org/freemarker/freemarker/2.3.32/freemarker-2.3.32.jar
2026-01-19T16:16:22.8552086Z Progress (1): 0.6/1.6 MB
2026-01-19T16:16:22.8552718Z Progress (1): 0.7/1.6 MB
2026-01-19T16:16:22.8553039Z Progress (1): 0.7/1.6 MB
2026-01-19T16:16:22.8553336Z Progress (1): 0.7/1.6 MB
2026-01-19T16:16:22.8553681Z Progress (1): 0.7/1.6 MB
2026-01-19T16:16:22.8553979Z Progress (1): 0.7/1.6 MB
2026-01-19T16:16:22.8554275Z Progress (1): 0.7/1.6 MB
2026-01-19T16:16:22.8554577Z Progress (1): 0.8/1.6 MB
2026-01-19T16:16:22.8554887Z Progress (1): 0.8/1.6 MB
2026-01-19T16:16:22.8568746Z Progress (1): 0.8/1.6 MB
2026-01-19T16:16:22.8569072Z Progress (1): 0.8/1.6 MB
2026-01-19T16:16:22.8569392Z Progress (1): 0.8/1.6 MB
2026-01-19T16:16:22.8569696Z Progress (1): 0.8/1.6 MB
2026-01-19T16:16:22.8570008Z Progress (1): 0.9/1.6 MB
2026-01-19T16:16:22.8570312Z Progress (1): 0.9/1.6 MB
2026-01-19T16:16:22.8570615Z Progress (1): 0.9/1.6 MB
2026-01-19T16:16:22.8570909Z Progress (1): 0.9/1.6 MB
2026-01-19T16:16:22.8575423Z Progress (1): 0.9/1.6 MB
2026-01-19T16:16:22.8582035Z Progress (1): 0.9/1.6 MB
2026-01-19T16:16:22.8588933Z Progress (1): 1.0/1.6 MB
2026-01-19T16:16:22.8595784Z Progress (1): 1.0/1.6 MB
2026-01-19T16:16:22.8619674Z Progress (1): 1.0/1.6 MB
2026-01-19T16:16:22.8620269Z Progress (1): 1.0/1.6 MB
2026-01-19T16:16:22.8620787Z Progress (1): 1.0/1.6 MB
2026-01-19T16:16:22.8621336Z Progress (1): 1.0/1.6 MB
2026-01-19T16:16:22.8621807Z Progress (1): 1.0/1.6 MB
2026-01-19T16:16:22.8622286Z Progress (1): 1.1/1.6 MB
2026-01-19T16:16:22.8622752Z Progress (1): 1.1/1.6 MB
2026-01-19T16:16:22.8623216Z Progress (1): 1.1/1.6 MB
2026-01-19T16:16:22.8623676Z Progress (1): 1.1/1.6 MB
2026-01-19T16:16:22.8624155Z Progress (1): 1.1/1.6 MB
2026-01-19T16:16:22.8624609Z Progress (1): 1.1/1.6 MB
2026-01-19T16:16:22.8625071Z Progress (1): 1.2/1.6 MB
2026-01-19T16:16:22.8625555Z Progress (1): 1.2/1.6 MB
2026-01-19T16:16:22.8626058Z Progress (1): 1.2/1.6 MB
2026-01-19T16:16:22.8632719Z Progress (1): 1.2/1.6 MB
2026-01-19T16:16:22.8639059Z Progress (1): 1.2/1.6 MB
2026-01-19T16:16:22.8645049Z Progress (1): 1.2/1.6 MB
2026-01-19T16:16:22.8651337Z Progress (1): 1.2/1.6 MB
2026-01-19T16:16:22.8657570Z Progress (1): 1.3/1.6 MB
2026-01-19T16:16:22.8663614Z Progress (1): 1.3/1.6 MB
2026-01-19T16:16:22.8671500Z Progress (1): 1.3/1.6 MB
2026-01-19T16:16:22.8690567Z Progress (2): 1.3/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8692362Z Progress (2): 1.3/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8693898Z Progress (2): 1.3/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8698354Z Progress (2): 1.3/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8698873Z Progress (2): 1.3/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8699511Z Progress (2): 1.4/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8700279Z Progress (2): 1.4/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8705043Z Progress (2): 1.4/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8705559Z Progress (2): 1.4/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8706055Z Progress (2): 1.4/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8706698Z Progress (2): 1.4/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8708346Z Progress (2): 1.5/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8708990Z Progress (2): 1.5/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8709702Z Progress (2): 1.5/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8710457Z Progress (2): 1.5/1.6 MB | 0/1.0 MB
2026-01-19T16:16:22.8712920Z Progress (2): 1.5/1.6 MB | 0.1/1.0 MB
2026-01-19T16:16:22.8715498Z Progress (2): 1.5/1.6 MB | 0.1/1.0 MB
2026-01-19T16:16:22.8715997Z Progress (2): 1.5/1.6 MB | 0.1/1.0 MB
2026-01-19T16:16:22.8716637Z Progress (2): 1.5/1.6 MB | 0.1/1.0 MB
2026-01-19T16:16:22.8718023Z Progress (2): 1.5/1.6 MB | 0.1/1.0 MB
2026-01-19T16:16:22.8721222Z Progress (2): 1.5/1.6 MB | 0.1/1.0 MB
2026-01-19T16:16:22.8723909Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0/2.7 MB
2026-01-19T16:16:22.8727814Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0/2.7 MB
2026-01-19T16:16:22.8728372Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0/2.7 MB
2026-01-19T16:16:22.8732466Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0/2.7 MB
2026-01-19T16:16:22.8733040Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.1/2.7 MB
2026-01-19T16:16:22.8734643Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.1/2.7 MB
2026-01-19T16:16:22.8735204Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.1/2.7 MB
2026-01-19T16:16:22.8735710Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.1/2.7 MB
2026-01-19T16:16:22.8737441Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.1/2.7 MB
2026-01-19T16:16:22.8738016Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.1/2.7 MB
2026-01-19T16:16:22.8738548Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8795305Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8795962Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8796917Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8797499Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8798250Z Progress (3): 1.5/1.6 MB | 0.1/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8798924Z Progress (3): 1.6/1.6 MB | 0.1/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8799578Z Progress (3): 1.6/1.6 MB | 0.2/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8800060Z Progress (3): 1.6/1.6 MB | 0.2/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8801164Z Progress (4): 1.6/1.6 MB | 0.2/1.0 MB | 0.2/2.7 MB | 7.7/12 kB
2026-01-19T16:16:22.8801708Z Progress (4): 1.6/1.6 MB | 0.2/1.0 MB | 0.2/2.7 MB | 8.2/12 kB
2026-01-19T16:16:22.8802860Z Progress (4): 1.6/1.6 MB | 0.2/1.0 MB | 0.2/2.7 MB | 12 kB    
2026-01-19T16:16:22.8803460Z Progress (4): 1.6/1.6 MB | 0.2/1.0 MB | 0.2/2.7 MB | 12 kB
2026-01-19T16:16:22.8804081Z Progress (4): 1.6/1.6 MB | 0.2/1.0 MB | 0.2/2.7 MB | 12 kB
2026-01-19T16:16:22.8804583Z Progress (4): 1.6/1.6 MB | 0.2/1.0 MB | 0.2/2.7 MB | 12 kB
2026-01-19T16:16:22.8805302Z                                                           
2026-01-19T16:16:22.8805860Z Downloaded from central: https://repo.maven.apache.org/maven2/org/reactivestreams/reactive-streams/1.0.4/reactive-streams-1.0.4.jar (12 kB at 9.8 kB/s)
2026-01-19T16:16:22.8806735Z Downloading from central: https://repo.maven.apache.org/maven2/org/projectlombok/lombok/1.18.26/lombok-1.18.26.jar
2026-01-19T16:16:22.8807793Z Progress (3): 1.6/1.6 MB | 0.2/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8808804Z Progress (3): 1.6/1.6 MB | 0.3/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8809336Z Progress (3): 1.6/1.6 MB | 0.3/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8809819Z Progress (3): 1.6/1.6 MB | 0.3/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8810420Z Progress (3): 1.6/1.6 MB | 0.3/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8811053Z Progress (3): 1.6/1.6 MB | 0.3/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8811662Z Progress (3): 1.6/1.6 MB | 0.3/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8812263Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8813515Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8814245Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8815225Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8815725Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8818213Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8818918Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8819530Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8820177Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8821110Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8823140Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8823753Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.2/2.7 MB
2026-01-19T16:16:22.8824327Z Progress (3): 1.6/1.6 MB | 0.4/1.0 MB | 0.3/2.7 MB
2026-01-19T16:16:22.8825162Z Progress (3): 1.6 MB | 0.4/1.0 MB | 0.3/2.7 MB    
2026-01-19T16:16:22.8825787Z Progress (3): 1.6 MB | 0.4/1.0 MB | 0.3/2.7 MB
2026-01-19T16:16:22.8826355Z Progress (3): 1.6 MB | 0.4/1.0 MB | 0.3/2.7 MB
2026-01-19T16:16:22.8829502Z Progress (3): 1.6 MB | 0.4/1.0 MB | 0.3/2.7 MB
2026-01-19T16:16:22.8830364Z Progress (3): 1.6 MB | 0.4/1.0 MB | 0.3/2.7 MB
2026-01-19T16:16:22.8830710Z Progress (3): 1.6 MB | 0.4/1.0 MB | 0.3/2.7 MB
2026-01-19T16:16:22.8831010Z Progress (3): 1.6 MB | 0.4/1.0 MB | 0.4/2.7 MB
2026-01-19T16:16:22.8831338Z Progress (3): 1.6 MB | 0.4/1.0 MB | 0.4/2.7 MB
2026-01-19T16:16:22.8831639Z                                               
2026-01-19T16:16:22.8832037Z Downloaded from central: https://repo.maven.apache.org/maven2/com/fasterxml/jackson/core/jackson-databind/2.17.1/jackson-databind-2.17.1.jar (1.6 MB at 1.4 MB/s)
2026-01-19T16:16:22.8832568Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.jar
2026-01-19T16:16:22.8833015Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0/1.7 MB
2026-01-19T16:16:22.8833354Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0/1.7 MB
2026-01-19T16:16:22.8833669Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0/1.7 MB
2026-01-19T16:16:22.8834274Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0/1.7 MB
2026-01-19T16:16:22.8834616Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.1/1.7 MB
2026-01-19T16:16:22.8834931Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.1/1.7 MB
2026-01-19T16:16:22.8835262Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.1/1.7 MB
2026-01-19T16:16:22.8836059Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.1/1.7 MB
2026-01-19T16:16:22.8836387Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.1/1.7 MB
2026-01-19T16:16:22.8836855Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.1/1.7 MB
2026-01-19T16:16:22.8837209Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8837553Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8837885Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8838207Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8838527Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8839157Z Progress (3): 0.4/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8839499Z Progress (3): 0.5/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8889207Z Progress (3): 0.5/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8891353Z Progress (3): 0.5/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8893100Z Progress (3): 0.5/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8894605Z Progress (3): 0.5/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8896646Z Progress (3): 0.5/1.0 MB | 0.4/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8905066Z Progress (3): 0.5/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8907788Z Progress (3): 0.5/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8909680Z Progress (3): 0.5/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8911651Z Progress (3): 0.5/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8913906Z Progress (3): 0.5/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8916296Z Progress (3): 0.5/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8918279Z Progress (3): 0.5/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8920370Z Progress (3): 0.5/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8922684Z Progress (3): 0.5/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8924459Z Progress (3): 0.5/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8926653Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8934808Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8937171Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8973924Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8974593Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8975684Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8976376Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.2/1.7 MB
2026-01-19T16:16:22.8977808Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.3/1.7 MB
2026-01-19T16:16:22.8978417Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.3/1.7 MB
2026-01-19T16:16:22.8979019Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.3/1.7 MB
2026-01-19T16:16:22.8979598Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.3/1.7 MB
2026-01-19T16:16:22.8980171Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.3/1.7 MB
2026-01-19T16:16:22.8980730Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.3/1.7 MB
2026-01-19T16:16:22.8982784Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.3/1.7 MB
2026-01-19T16:16:22.8983394Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8984855Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8985465Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8987040Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8987690Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8988319Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8989365Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8989889Z Progress (3): 0.6/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8990454Z Progress (3): 0.7/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8991035Z Progress (3): 0.7/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8991589Z Progress (3): 0.7/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8992081Z Progress (3): 0.7/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8992621Z Progress (3): 0.7/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8993860Z Progress (3): 0.7/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8994474Z Progress (3): 0.8/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8994982Z Progress (3): 0.8/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8995567Z Progress (3): 0.8/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8996364Z Progress (3): 0.8/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8997695Z Progress (3): 0.8/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8998322Z Progress (3): 0.8/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8998939Z Progress (3): 0.9/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.8999482Z Progress (3): 0.9/1.0 MB | 0.5/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9000050Z Progress (3): 0.9/1.0 MB | 0.6/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9000714Z Progress (3): 0.9/1.0 MB | 0.6/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9001271Z Progress (3): 0.9/1.0 MB | 0.6/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9001812Z Progress (3): 0.9/1.0 MB | 0.6/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9002460Z Progress (3): 0.9/1.0 MB | 0.6/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9003057Z Progress (3): 0.9/1.0 MB | 0.6/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9003655Z Progress (3): 0.9/1.0 MB | 0.7/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9004413Z Progress (3): 0.9/1.0 MB | 0.7/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9004941Z Progress (3): 0.9/1.0 MB | 0.7/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9007368Z Progress (3): 0.9/1.0 MB | 0.7/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9008265Z Progress (3): 0.9/1.0 MB | 0.7/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9009180Z Progress (3): 0.9/1.0 MB | 0.7/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9010188Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9010762Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9011298Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9018182Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9019143Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9019741Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.4/1.7 MB
2026-01-19T16:16:22.9020249Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.5/1.7 MB
2026-01-19T16:16:22.9021424Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.5/1.7 MB
2026-01-19T16:16:22.9021982Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.5/1.7 MB
2026-01-19T16:16:22.9022497Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.5/1.7 MB
2026-01-19T16:16:22.9023033Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.5/1.7 MB
2026-01-19T16:16:22.9023573Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.5/1.7 MB
2026-01-19T16:16:22.9024054Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.6/1.7 MB
2026-01-19T16:16:22.9024881Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.6/1.7 MB
2026-01-19T16:16:22.9026024Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.6/1.7 MB
2026-01-19T16:16:22.9026778Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.6/1.7 MB
2026-01-19T16:16:22.9027790Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.6/1.7 MB
2026-01-19T16:16:22.9030383Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.6/1.7 MB
2026-01-19T16:16:22.9031047Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB
2026-01-19T16:16:22.9031628Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB
2026-01-19T16:16:22.9032242Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB
2026-01-19T16:16:22.9033648Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB
2026-01-19T16:16:22.9034507Z Progress (3): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB
2026-01-19T16:16:22.9035895Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 7.7/658 kB
2026-01-19T16:16:22.9037237Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 16/658 kB 
2026-01-19T16:16:22.9037835Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 32/658 kB
2026-01-19T16:16:22.9038428Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 32/658 kB
2026-01-19T16:16:22.9038970Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 49/658 kB
2026-01-19T16:16:22.9039462Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 49/658 kB
2026-01-19T16:16:22.9040021Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 65/658 kB
2026-01-19T16:16:22.9040609Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 65/658 kB
2026-01-19T16:16:22.9040973Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 81/658 kB
2026-01-19T16:16:22.9041329Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 81/658 kB
2026-01-19T16:16:22.9041678Z Progress (4): 0.9/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 98/658 kB
2026-01-19T16:16:22.9042072Z Progress (4): 1.0/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 98/658 kB
2026-01-19T16:16:22.9042421Z Progress (4): 1.0/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 114/658 kB
2026-01-19T16:16:22.9042785Z Progress (4): 1.0/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 114/658 kB
2026-01-19T16:16:22.9043148Z Progress (4): 1.0/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 131/658 kB
2026-01-19T16:16:22.9043639Z Progress (4): 1.0/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 131/658 kB
2026-01-19T16:16:22.9043999Z Progress (4): 1.0/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9044360Z Progress (4): 1.0/1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9044714Z Progress (4): 1.0 MB | 0.8/2.7 MB | 0.7/1.7 MB | 147/658 kB    
2026-01-19T16:16:22.9045041Z                                                            
2026-01-19T16:16:22.9045456Z Downloaded from central: https://repo.maven.apache.org/maven2/com/aventstack/extentreports/5.1.1/extentreports-5.1.1.jar (1.0 MB at 836 kB/s)
2026-01-19T16:16:22.9046041Z Progress (3): 0.8/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9046394Z Progress (3): 0.9/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9046905Z Progress (3): 0.9/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9047254Z Progress (3): 0.9/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9047599Z Progress (3): 0.9/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9047933Z Progress (3): 0.9/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9048271Z Progress (3): 0.9/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9048605Z Progress (3): 0.9/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9048942Z Progress (3): 1.0/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9049272Z Progress (3): 1.0/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9049620Z Progress (3): 1.0/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9049975Z Progress (3): 1.0/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9050321Z Progress (3): 1.0/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9050662Z Progress (3): 1.0/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9051003Z Progress (3): 1.0/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9051329Z Progress (3): 1.0/2.7 MB | 0.7/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9051670Z Progress (3): 1.0/2.7 MB | 0.8/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9052007Z Progress (3): 1.0/2.7 MB | 0.8/1.7 MB | 147/658 kB
2026-01-19T16:16:22.9052351Z Progress (4): 1.0/2.7 MB | 0.8/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9052706Z Progress (4): 1.0/2.7 MB | 0.8/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9053063Z Progress (4): 1.0/2.7 MB | 0.8/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9053441Z Progress (4): 1.0/2.7 MB | 0.8/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9053798Z Progress (4): 1.0/2.7 MB | 0.8/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9054144Z Progress (4): 1.0/2.7 MB | 0.8/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9054496Z Progress (4): 1.0/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9054839Z Progress (4): 1.0/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9191524Z Progress (4): 1.0/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9191960Z Progress (4): 1.0/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9192322Z Progress (4): 1.0/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9192680Z Progress (4): 1.0/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9193009Z                                                              
2026-01-19T16:16:22.9193430Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-cucumber7-jvm/2.29.0/allure-cucumber7-jvm-2.29.0.jar
2026-01-19T16:16:22.9193883Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9194297Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9194644Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9194994Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9195333Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0/2.0 MB
2026-01-19T16:16:22.9195685Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9196034Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9196697Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9197048Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9197398Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9197747Z Progress (4): 1.1/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9198086Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9198433Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9198780Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9199120Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9199568Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9199911Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9200258Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.1/2.0 MB
2026-01-19T16:16:22.9200605Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9200948Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9201317Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 147/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9201664Z Progress (4): 1.2/2.7 MB | 0.9/1.7 MB | 163/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9202010Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 163/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9202352Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 180/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9202703Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 180/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9203041Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 196/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9203386Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 196/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9203729Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 213/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9204079Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 213/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9204423Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 229/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9204776Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 229/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9205121Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 229/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9205469Z Progress (4): 1.3/2.7 MB | 0.9/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9205816Z Progress (4): 1.4/2.7 MB | 0.9/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9206166Z Progress (4): 1.4/2.7 MB | 1.0/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9206652Z Progress (4): 1.4/2.7 MB | 1.0/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9207009Z Progress (4): 1.4/2.7 MB | 1.0/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9207354Z Progress (4): 1.4/2.7 MB | 1.0/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9207702Z Progress (4): 1.4/2.7 MB | 1.0/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9208043Z Progress (4): 1.4/2.7 MB | 1.0/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9208402Z Progress (4): 1.4/2.7 MB | 1.1/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9208752Z Progress (4): 1.4/2.7 MB | 1.1/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9209095Z Progress (4): 1.4/2.7 MB | 1.1/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9209444Z Progress (4): 1.4/2.7 MB | 1.1/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9209791Z Progress (4): 1.4/2.7 MB | 1.1/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9210143Z Progress (4): 1.4/2.7 MB | 1.1/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9210483Z Progress (4): 1.4/2.7 MB | 1.1/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9210844Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9211193Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9211535Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9211887Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9212386Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 245/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9212743Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 262/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9213105Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 262/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9213461Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 278/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9213821Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 278/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9214173Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 294/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9214535Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 294/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9214890Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 311/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9215365Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 327/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9215717Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 327/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9216073Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 344/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9216425Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 344/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9216930Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 360/658 kB | 0.2/2.0 MB
2026-01-19T16:16:22.9217258Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 360/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9217604Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 376/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9217938Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 376/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9218315Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 393/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9218686Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 393/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9219037Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 409/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9219371Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 409/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9219827Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 426/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9220159Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 426/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9220493Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 442/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9220852Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 458/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9221332Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 458/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9221655Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 475/658 kB | 0.3/2.0 MB
2026-01-19T16:16:22.9222016Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 475/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9222358Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 491/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9222685Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 491/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9223032Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 507/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9223395Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 507/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9223718Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 524/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9224063Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 524/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9224423Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9224752Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9225079Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9225489Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9225831Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9226160Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9226659Z Progress (4): 1.4/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9227037Z Progress (4): 1.5/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9227369Z Progress (4): 1.5/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9227711Z Progress (4): 1.5/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9228069Z Progress (4): 1.5/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9228486Z Progress (4): 1.5/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9228818Z Progress (4): 1.5/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9229176Z Progress (4): 1.6/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9229506Z Progress (4): 1.6/2.7 MB | 1.2/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9229834Z Progress (4): 1.6/2.7 MB | 1.3/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9230247Z Progress (4): 1.6/2.7 MB | 1.3/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9230601Z Progress (4): 1.6/2.7 MB | 1.3/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9230925Z Progress (4): 1.6/2.7 MB | 1.3/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9231389Z Progress (4): 1.6/2.7 MB | 1.3/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9231737Z Progress (4): 1.6/2.7 MB | 1.3/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9232066Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9232413Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9232768Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9233091Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.4/2.0 MB
2026-01-19T16:16:22.9233442Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9233795Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9234126Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9234454Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9234817Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9235156Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9235484Z Progress (4): 1.6/2.7 MB | 1.4/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9235838Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9236189Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9236673Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9237044Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9237398Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9237754Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.5/2.0 MB
2026-01-19T16:16:22.9238098Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.6/2.0 MB
2026-01-19T16:16:22.9238450Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.6/2.0 MB
2026-01-19T16:16:22.9238793Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.6/2.0 MB
2026-01-19T16:16:22.9239151Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.6/2.0 MB
2026-01-19T16:16:22.9239489Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.6/2.0 MB
2026-01-19T16:16:22.9361452Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.6/2.0 MB
2026-01-19T16:16:22.9367521Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.7/2.0 MB
2026-01-19T16:16:22.9368066Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.7/2.0 MB
2026-01-19T16:16:22.9368459Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.7/2.0 MB
2026-01-19T16:16:22.9368808Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.7/2.0 MB
2026-01-19T16:16:22.9369165Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.7/2.0 MB
2026-01-19T16:16:22.9369512Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.7/2.0 MB
2026-01-19T16:16:22.9369865Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.8/2.0 MB
2026-01-19T16:16:22.9370210Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.8/2.0 MB
2026-01-19T16:16:22.9370571Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.8/2.0 MB
2026-01-19T16:16:22.9370958Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.8/2.0 MB
2026-01-19T16:16:22.9371315Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.8/2.0 MB
2026-01-19T16:16:22.9371792Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.8/2.0 MB
2026-01-19T16:16:22.9372148Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9372498Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9372851Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9373188Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9373552Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9373917Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9374296Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9374831Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9375185Z Progress (4): 1.6/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9375529Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9375907Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 540/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9376266Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 557/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9376816Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 557/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9377179Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 573/658 kB | 0.9/2.0 MB
2026-01-19T16:16:22.9377562Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 573/658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9377912Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 589/658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9378242Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 589/658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9379098Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 606/658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9379448Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 606/658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9379785Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 622/658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9380155Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 622/658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9380498Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 639/658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9380828Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 639/658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9381183Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 655/658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9381623Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 658 kB | 1.0/2.0 MB    
2026-01-19T16:16:22.9381942Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 658 kB | 1.0/2.0 MB
2026-01-19T16:16:22.9382301Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 658 kB | 1.1/2.0 MB
2026-01-19T16:16:22.9382655Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 658 kB | 1.1/2.0 MB
2026-01-19T16:16:22.9383017Z Progress (4): 1.7/2.7 MB | 1.5/1.7 MB | 658 kB | 1.1/2.0 MB
2026-01-19T16:16:22.9383317Z                                                            
2026-01-19T16:16:22.9383788Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.14.0/commons-lang3-3.14.0.jar (658 kB at 529 kB/s)
2026-01-19T16:16:22.9384293Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-java-commons/2.29.0/allure-java-commons-2.29.0.jar
2026-01-19T16:16:22.9384737Z Progress (3): 1.7/2.7 MB | 1.5/1.7 MB | 1.1/2.0 MB
2026-01-19T16:16:22.9385058Z Progress (3): 1.7/2.7 MB | 1.5/1.7 MB | 1.1/2.0 MB
2026-01-19T16:16:22.9385369Z Progress (3): 1.7/2.7 MB | 1.5/1.7 MB | 1.1/2.0 MB
2026-01-19T16:16:22.9385708Z Progress (3): 1.7/2.7 MB | 1.5/1.7 MB | 1.1/2.0 MB
2026-01-19T16:16:22.9386036Z Progress (3): 1.7/2.7 MB | 1.5/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9386348Z Progress (3): 1.7/2.7 MB | 1.5/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9386853Z Progress (3): 1.7/2.7 MB | 1.5/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9387213Z Progress (3): 1.7/2.7 MB | 1.5/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9387528Z Progress (3): 1.7/2.7 MB | 1.5/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9387843Z Progress (3): 1.7/2.7 MB | 1.6/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9388178Z Progress (3): 1.7/2.7 MB | 1.6/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9388584Z Progress (3): 1.7/2.7 MB | 1.6/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9388886Z Progress (3): 1.7/2.7 MB | 1.6/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9389221Z Progress (3): 1.7/2.7 MB | 1.6/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9389555Z Progress (3): 1.7/2.7 MB | 1.6/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9389861Z Progress (3): 1.7/2.7 MB | 1.6/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9390191Z Progress (3): 1.7/2.7 MB | 1.7/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9390533Z Progress (3): 1.7/2.7 MB | 1.7/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9390850Z Progress (3): 1.7/2.7 MB | 1.7/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9391158Z Progress (3): 1.7/2.7 MB | 1.7/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9391637Z Progress (3): 1.7/2.7 MB | 1.7/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9391958Z Progress (3): 1.7/2.7 MB | 1.7/1.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9392266Z Progress (3): 1.7/2.7 MB | 1.7 MB | 1.2/2.0 MB    
2026-01-19T16:16:22.9392567Z                                               
2026-01-19T16:16:22.9392966Z Downloaded from central: https://repo.maven.apache.org/maven2/org/freemarker/freemarker/2.3.32/freemarker-2.3.32.jar (1.7 MB at 1.4 MB/s)
2026-01-19T16:16:22.9393348Z Progress (2): 1.7/2.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9393678Z Progress (2): 1.7/2.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9393991Z Progress (2): 1.7/2.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9394288Z Progress (2): 1.7/2.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9394587Z Progress (2): 1.7/2.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9394926Z Progress (2): 1.7/2.7 MB | 1.2/2.0 MB
2026-01-19T16:16:22.9395258Z Progress (2): 1.7/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9395611Z Progress (2): 1.7/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9395951Z Progress (2): 1.7/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9396297Z Progress (2): 1.8/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9396820Z Progress (2): 1.8/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9397144Z Progress (2): 1.8/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9397447Z Progress (2): 1.8/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9397767Z Progress (2): 1.8/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9398073Z Progress (2): 1.8/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9398393Z Progress (2): 1.8/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9398711Z Progress (2): 1.8/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9399031Z Progress (2): 1.8/2.7 MB | 1.3/2.0 MB
2026-01-19T16:16:22.9399343Z Progress (2): 1.8/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9399660Z Progress (2): 1.8/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9399981Z Progress (2): 1.8/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9400302Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9400628Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9400960Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9401287Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9401614Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9401940Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9402262Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9402594Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9402913Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9403250Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9403567Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9403936Z Progress (2): 1.9/2.7 MB | 1.4/2.0 MB
2026-01-19T16:16:22.9404258Z Progress (2): 1.9/2.7 MB | 1.5/2.0 MB
2026-01-19T16:16:22.9404588Z Progress (2): 1.9/2.7 MB | 1.5/2.0 MB
2026-01-19T16:16:22.9404922Z Progress (3): 1.9/2.7 MB | 1.5/2.0 MB | 7.7/25 kB
2026-01-19T16:16:22.9405265Z Progress (3): 1.9/2.7 MB | 1.5/2.0 MB | 16/25 kB 
2026-01-19T16:16:22.9405603Z Progress (3): 1.9/2.7 MB | 1.5/2.0 MB | 16/25 kB
2026-01-19T16:16:22.9405955Z Progress (3): 1.9/2.7 MB | 1.5/2.0 MB | 25 kB   
2026-01-19T16:16:22.9406289Z Progress (3): 1.9/2.7 MB | 1.5/2.0 MB | 25 kB
2026-01-19T16:16:22.9406818Z Progress (3): 1.9/2.7 MB | 1.5/2.0 MB | 25 kB
2026-01-19T16:16:22.9407123Z                                              
2026-01-19T16:16:22.9407695Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-cucumber7-jvm/2.29.0/allure-cucumber7-jvm-2.29.0.jar (25 kB at 20 kB/s)
2026-01-19T16:16:22.9408150Z Progress (2): 1.9/2.7 MB | 1.5/2.0 MB
2026-01-19T16:16:22.9408484Z Progress (2): 1.9/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9408810Z Progress (2): 1.9/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9409110Z                                      
2026-01-19T16:16:22.9409497Z Downloading from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-model/2.29.0/allure-model-2.29.0.jar
2026-01-19T16:16:22.9409928Z Progress (2): 1.9/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9410254Z Progress (2): 2.0/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9410712Z Progress (2): 2.0/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9411041Z Progress (2): 2.0/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9411376Z Progress (2): 2.0/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9411702Z Progress (2): 2.0/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9412045Z Progress (2): 2.0/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9412373Z Progress (2): 2.1/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9412704Z Progress (2): 2.1/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9413029Z Progress (2): 2.1/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9413361Z Progress (2): 2.1/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9413684Z Progress (2): 2.1/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9414005Z Progress (2): 2.1/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9414332Z Progress (2): 2.2/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9414656Z Progress (2): 2.2/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9414991Z Progress (2): 2.2/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9415315Z Progress (2): 2.2/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9415654Z Progress (2): 2.2/2.7 MB | 1.6/2.0 MB
2026-01-19T16:16:22.9415977Z Progress (2): 2.2/2.7 MB | 1.7/2.0 MB
2026-01-19T16:16:22.9416305Z Progress (2): 2.2/2.7 MB | 1.7/2.0 MB
2026-01-19T16:16:22.9416903Z Progress (2): 2.2/2.7 MB | 1.7/2.0 MB
2026-01-19T16:16:22.9417273Z Progress (2): 2.2/2.7 MB | 1.7/2.0 MB
2026-01-19T16:16:22.9417615Z Progress (2): 2.2/2.7 MB | 1.7/2.0 MB
2026-01-19T16:16:22.9417939Z Progress (2): 2.2/2.7 MB | 1.7/2.0 MB
2026-01-19T16:16:22.9418278Z Progress (2): 2.2/2.7 MB | 1.7/2.0 MB
2026-01-19T16:16:22.9421870Z Progress (2): 2.2/2.7 MB | 1.7/2.0 MB
2026-01-19T16:16:22.9422639Z Progress (2): 2.2/2.7 MB | 1.8/2.0 MB
2026-01-19T16:16:22.9425775Z Progress (2): 2.2/2.7 MB | 1.8/2.0 MB
2026-01-19T16:16:22.9426801Z Progress (2): 2.2/2.7 MB | 1.8/2.0 MB
2026-01-19T16:16:22.9427549Z Progress (2): 2.2/2.7 MB | 1.8/2.0 MB
2026-01-19T16:16:22.9429337Z Progress (2): 2.2/2.7 MB | 1.8/2.0 MB
2026-01-19T16:16:22.9430138Z Progress (2): 2.2/2.7 MB | 1.8/2.0 MB
2026-01-19T16:16:22.9430865Z Progress (2): 2.2/2.7 MB | 1.9/2.0 MB
2026-01-19T16:16:22.9432965Z Progress (2): 2.2/2.7 MB | 1.9/2.0 MB
2026-01-19T16:16:22.9433277Z Progress (2): 2.2/2.7 MB | 1.9/2.0 MB
2026-01-19T16:16:22.9433609Z Progress (2): 2.2/2.7 MB | 1.9/2.0 MB
2026-01-19T16:16:22.9433923Z Progress (2): 2.2/2.7 MB | 1.9/2.0 MB
2026-01-19T16:16:22.9434224Z Progress (2): 2.2/2.7 MB | 1.9/2.0 MB
2026-01-19T16:16:22.9434542Z Progress (2): 2.2/2.7 MB | 2.0/2.0 MB
2026-01-19T16:16:22.9434863Z Progress (2): 2.2/2.7 MB | 2.0/2.0 MB
2026-01-19T16:16:22.9439894Z Progress (2): 2.2/2.7 MB | 2.0 MB    
2026-01-19T16:16:22.9440243Z Progress (2): 2.2/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9441448Z Progress (2): 2.2/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9441752Z Progress (2): 2.3/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9444407Z Progress (2): 2.3/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9444805Z Progress (2): 2.3/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9445108Z Progress (2): 2.3/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9445400Z Progress (2): 2.3/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9450373Z Progress (2): 2.3/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9450712Z Progress (2): 2.4/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9451006Z Progress (2): 2.4/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9451331Z Progress (2): 2.4/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9452121Z Progress (2): 2.4/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9455957Z Progress (2): 2.4/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9479742Z Progress (2): 2.4/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9480086Z Progress (2): 2.5/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9480413Z Progress (2): 2.5/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9480703Z Progress (2): 2.5/2.7 MB | 2.0 MB
2026-01-19T16:16:22.9480976Z                                  
2026-01-19T16:16:22.9481379Z Downloaded from central: https://repo.maven.apache.org/maven2/org/projectlombok/lombok/1.18.26/lombok-1.18.26.jar (2.0 MB at 1.6 MB/s)
2026-01-19T16:16:22.9481815Z Progress (1): 2.5/2.7 MB
2026-01-19T16:16:22.9482102Z Progress (1): 2.5/2.7 MB
2026-01-19T16:16:22.9482387Z Progress (1): 2.5/2.7 MB
2026-01-19T16:16:22.9483487Z Progress (1): 2.6/2.7 MB
2026-01-19T16:16:22.9483824Z Progress (1): 2.6/2.7 MB
2026-01-19T16:16:22.9484140Z Progress (1): 2.6/2.7 MB
2026-01-19T16:16:22.9484418Z Progress (1): 2.6/2.7 MB
2026-01-19T16:16:22.9484697Z Progress (1): 2.6/2.7 MB
2026-01-19T16:16:22.9484998Z Progress (1): 2.6/2.7 MB
2026-01-19T16:16:22.9485332Z Progress (1): 2.7/2.7 MB
2026-01-19T16:16:22.9486146Z Progress (1): 2.7 MB    
2026-01-19T16:16:22.9488468Z                     
2026-01-19T16:16:22.9489298Z Downloaded from central: https://repo.maven.apache.org/maven2/io/reactivex/rxjava3/rxjava/3.1.6/rxjava-3.1.6.jar (2.7 MB at 2.1 MB/s)
2026-01-19T16:16:22.9490479Z Progress (1): 0/2.4 MB
2026-01-19T16:16:22.9492992Z Progress (1): 0/2.4 MB
2026-01-19T16:16:22.9493560Z Progress (1): 0/2.4 MB
2026-01-19T16:16:22.9494121Z Progress (1): 0.1/2.4 MB
2026-01-19T16:16:22.9495592Z Progress (1): 0.1/2.4 MB
2026-01-19T16:16:22.9497296Z Progress (1): 0.1/2.4 MB
2026-01-19T16:16:22.9499463Z Progress (1): 0.1/2.4 MB
2026-01-19T16:16:22.9508960Z Progress (1): 0.1/2.4 MB
2026-01-19T16:16:22.9509361Z Progress (1): 0.1/2.4 MB
2026-01-19T16:16:22.9513083Z Progress (1): 0.1/2.4 MB
2026-01-19T16:16:22.9517407Z Progress (1): 0.2/2.4 MB
2026-01-19T16:16:22.9522025Z Progress (1): 0.2/2.4 MB
2026-01-19T16:16:22.9526665Z Progress (1): 0.2/2.4 MB
2026-01-19T16:16:22.9531347Z Progress (1): 0.2/2.4 MB
2026-01-19T16:16:22.9536700Z Progress (1): 0.2/2.4 MB
2026-01-19T16:16:22.9540508Z Progress (1): 0.2/2.4 MB
2026-01-19T16:16:22.9547015Z Progress (1): 0.3/2.4 MB
2026-01-19T16:16:22.9551895Z Progress (1): 0.3/2.4 MB
2026-01-19T16:16:22.9556872Z Progress (1): 0.3/2.4 MB
2026-01-19T16:16:22.9564519Z Progress (1): 0.3/2.4 MB
2026-01-19T16:16:22.9581399Z Progress (1): 0.3/2.4 MB
2026-01-19T16:16:22.9582069Z Progress (1): 0.3/2.4 MB
2026-01-19T16:16:22.9582790Z Progress (1): 0.4/2.4 MB
2026-01-19T16:16:22.9583676Z Progress (1): 0.4/2.4 MB
2026-01-19T16:16:22.9587597Z Progress (1): 0.4/2.4 MB
2026-01-19T16:16:22.9587986Z Progress (1): 0.4/2.4 MB
2026-01-19T16:16:22.9588320Z Progress (1): 0.4/2.4 MB
2026-01-19T16:16:22.9588653Z Progress (1): 0.4/2.4 MB
2026-01-19T16:16:22.9588979Z Progress (1): 0.5/2.4 MB
2026-01-19T16:16:22.9589322Z Progress (2): 0.5/2.4 MB | 7.7/18 kB
2026-01-19T16:16:22.9600824Z Progress (2): 0.5/2.4 MB | 16/18 kB 
2026-01-19T16:16:22.9601193Z Progress (2): 0.5/2.4 MB | 18 kB   
2026-01-19T16:16:22.9601488Z                                 
2026-01-19T16:16:22.9601896Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-model/2.29.0/allure-model-2.29.0.jar (18 kB at 14 kB/s)
2026-01-19T16:16:22.9602322Z Progress (1): 0.5/2.4 MB
2026-01-19T16:16:22.9606651Z Progress (1): 0.5/2.4 MB
2026-01-19T16:16:22.9705576Z Progress (1): 0.5/2.4 MB
2026-01-19T16:16:22.9706197Z Progress (1): 0.5/2.4 MB
2026-01-19T16:16:22.9706958Z Progress (1): 0.5/2.4 MB
2026-01-19T16:16:22.9707456Z Progress (1): 0.6/2.4 MB
2026-01-19T16:16:22.9707770Z Progress (1): 0.6/2.4 MB
2026-01-19T16:16:22.9708088Z Progress (1): 0.6/2.4 MB
2026-01-19T16:16:22.9708413Z Progress (1): 0.6/2.4 MB
2026-01-19T16:16:22.9708715Z Progress (1): 0.6/2.4 MB
2026-01-19T16:16:22.9709026Z Progress (1): 0.6/2.4 MB
2026-01-19T16:16:22.9709391Z Progress (1): 0.7/2.4 MB
2026-01-19T16:16:22.9709691Z Progress (1): 0.7/2.4 MB
2026-01-19T16:16:22.9709986Z Progress (1): 0.7/2.4 MB
2026-01-19T16:16:22.9710433Z Progress (1): 0.7/2.4 MB
2026-01-19T16:16:22.9710724Z Progress (1): 0.7/2.4 MB
2026-01-19T16:16:22.9711028Z Progress (1): 0.7/2.4 MB
2026-01-19T16:16:22.9711322Z Progress (1): 0.8/2.4 MB
2026-01-19T16:16:22.9711625Z Progress (1): 0.8/2.4 MB
2026-01-19T16:16:22.9711920Z Progress (1): 0.8/2.4 MB
2026-01-19T16:16:22.9712213Z Progress (1): 0.8/2.4 MB
2026-01-19T16:16:22.9712511Z Progress (1): 0.8/2.4 MB
2026-01-19T16:16:22.9712806Z Progress (1): 0.8/2.4 MB
2026-01-19T16:16:22.9713117Z Progress (1): 0.9/2.4 MB
2026-01-19T16:16:22.9713430Z Progress (1): 0.9/2.4 MB
2026-01-19T16:16:22.9713744Z Progress (1): 0.9/2.4 MB
2026-01-19T16:16:22.9714034Z Progress (1): 0.9/2.4 MB
2026-01-19T16:16:22.9714436Z Progress (1): 0.9/2.4 MB
2026-01-19T16:16:22.9714745Z Progress (1): 0.9/2.4 MB
2026-01-19T16:16:22.9715076Z Progress (1): 1.0/2.4 MB
2026-01-19T16:16:22.9715427Z Progress (1): 1.0/2.4 MB
2026-01-19T16:16:22.9715739Z Progress (1): 1.0/2.4 MB
2026-01-19T16:16:22.9716015Z Progress (1): 1.0/2.4 MB
2026-01-19T16:16:22.9716317Z Progress (1): 1.0/2.4 MB
2026-01-19T16:16:22.9716802Z Progress (1): 1.0/2.4 MB
2026-01-19T16:16:22.9717131Z Progress (1): 1.0/2.4 MB
2026-01-19T16:16:22.9727610Z Progress (1): 1.1/2.4 MB
2026-01-19T16:16:22.9727973Z Progress (1): 1.1/2.4 MB
2026-01-19T16:16:22.9728651Z Progress (1): 1.1/2.4 MB
2026-01-19T16:16:22.9729490Z Progress (1): 1.1/2.4 MB
2026-01-19T16:16:22.9729964Z Progress (1): 1.1/2.4 MB
2026-01-19T16:16:22.9730515Z Progress (1): 1.1/2.4 MB
2026-01-19T16:16:22.9731539Z Progress (1): 1.2/2.4 MB
2026-01-19T16:16:22.9732014Z Progress (1): 1.2/2.4 MB
2026-01-19T16:16:22.9739101Z Progress (1): 1.2/2.4 MB
2026-01-19T16:16:22.9758924Z Progress (1): 1.2/2.4 MB
2026-01-19T16:16:22.9759458Z Progress (1): 1.2/2.4 MB
2026-01-19T16:16:22.9759780Z Progress (1): 1.2/2.4 MB
2026-01-19T16:16:22.9760075Z Progress (1): 1.3/2.4 MB
2026-01-19T16:16:22.9760374Z Progress (1): 1.3/2.4 MB
2026-01-19T16:16:22.9760671Z Progress (1): 1.3/2.4 MB
2026-01-19T16:16:22.9760978Z Progress (1): 1.3/2.4 MB
2026-01-19T16:16:22.9761283Z Progress (1): 1.3/2.4 MB
2026-01-19T16:16:22.9761589Z Progress (1): 1.3/2.4 MB
2026-01-19T16:16:22.9761880Z Progress (1): 1.4/2.4 MB
2026-01-19T16:16:22.9762171Z Progress (1): 1.4/2.4 MB
2026-01-19T16:16:22.9762475Z Progress (1): 1.4/2.4 MB
2026-01-19T16:16:22.9763695Z Progress (1): 1.4/2.4 MB
2026-01-19T16:16:22.9766911Z Progress (1): 1.4/2.4 MB
2026-01-19T16:16:22.9769917Z Progress (1): 1.4/2.4 MB
2026-01-19T16:16:22.9772829Z Progress (1): 1.5/2.4 MB
2026-01-19T16:16:22.9777413Z Progress (1): 1.5/2.4 MB
2026-01-19T16:16:22.9797702Z Progress (1): 1.5/2.4 MB
2026-01-19T16:16:22.9798599Z Progress (1): 1.5/2.4 MB
2026-01-19T16:16:22.9799516Z Progress (1): 1.5/2.4 MB
2026-01-19T16:16:22.9801836Z Progress (1): 1.5/2.4 MB
2026-01-19T16:16:22.9802176Z Progress (1): 1.6/2.4 MB
2026-01-19T16:16:22.9802509Z Progress (1): 1.6/2.4 MB
2026-01-19T16:16:22.9802811Z Progress (1): 1.6/2.4 MB
2026-01-19T16:16:22.9803113Z Progress (1): 1.6/2.4 MB
2026-01-19T16:16:22.9803419Z Progress (1): 1.6/2.4 MB
2026-01-19T16:16:22.9803727Z Progress (1): 1.6/2.4 MB
2026-01-19T16:16:22.9804016Z Progress (1): 1.7/2.4 MB
2026-01-19T16:16:22.9804311Z Progress (1): 1.7/2.4 MB
2026-01-19T16:16:22.9804600Z Progress (1): 1.7/2.4 MB
2026-01-19T16:16:22.9809370Z Progress (1): 1.7/2.4 MB
2026-01-19T16:16:22.9811012Z Progress (1): 1.7/2.4 MB
2026-01-19T16:16:22.9813073Z Progress (1): 1.7/2.4 MB
2026-01-19T16:16:22.9815964Z Progress (1): 1.8/2.4 MB
2026-01-19T16:16:22.9819346Z Progress (1): 1.8/2.4 MB
2026-01-19T16:16:22.9849516Z Progress (1): 1.8/2.4 MB
2026-01-19T16:16:22.9850037Z Progress (1): 1.8/2.4 MB
2026-01-19T16:16:22.9850354Z Progress (1): 1.8/2.4 MB
2026-01-19T16:16:22.9850658Z Progress (1): 1.8/2.4 MB
2026-01-19T16:16:22.9850965Z Progress (1): 1.9/2.4 MB
2026-01-19T16:16:22.9851265Z Progress (1): 1.9/2.4 MB
2026-01-19T16:16:22.9851588Z Progress (1): 1.9/2.4 MB
2026-01-19T16:16:22.9851890Z Progress (1): 1.9/2.4 MB
2026-01-19T16:16:22.9852185Z Progress (1): 1.9/2.4 MB
2026-01-19T16:16:22.9852475Z Progress (1): 1.9/2.4 MB
2026-01-19T16:16:22.9852912Z Progress (1): 1.9/2.4 MB
2026-01-19T16:16:22.9853205Z Progress (1): 2.0/2.4 MB
2026-01-19T16:16:22.9853503Z Progress (1): 2.0/2.4 MB
2026-01-19T16:16:22.9853793Z Progress (1): 2.0/2.4 MB
2026-01-19T16:16:22.9854093Z Progress (1): 2.0/2.4 MB
2026-01-19T16:16:22.9854388Z Progress (1): 2.0/2.4 MB
2026-01-19T16:16:22.9854687Z Progress (1): 2.0/2.4 MB
2026-01-19T16:16:22.9855014Z Progress (1): 2.1/2.4 MB
2026-01-19T16:16:22.9855297Z Progress (1): 2.1/2.4 MB
2026-01-19T16:16:22.9855603Z Progress (1): 2.1/2.4 MB
2026-01-19T16:16:22.9856713Z Progress (1): 2.1/2.4 MB
2026-01-19T16:16:22.9857025Z Progress (1): 2.1/2.4 MB
2026-01-19T16:16:22.9857355Z Progress (1): 2.1/2.4 MB
2026-01-19T16:16:22.9862036Z Progress (1): 2.2/2.4 MB
2026-01-19T16:16:22.9867802Z Progress (1): 2.2/2.4 MB
2026-01-19T16:16:22.9873495Z Progress (1): 2.2/2.4 MB
2026-01-19T16:16:22.9879355Z Progress (1): 2.2/2.4 MB
2026-01-19T16:16:22.9884963Z Progress (1): 2.2/2.4 MB
2026-01-19T16:16:22.9892907Z Progress (1): 2.2/2.4 MB
2026-01-19T16:16:22.9893478Z Progress (1): 2.3/2.4 MB
2026-01-19T16:16:22.9896950Z Progress (1): 2.3/2.4 MB
2026-01-19T16:16:22.9901129Z Progress (1): 2.3/2.4 MB
2026-01-19T16:16:22.9904832Z Progress (1): 2.3/2.4 MB
2026-01-19T16:16:22.9909281Z Progress (1): 2.3/2.4 MB
2026-01-19T16:16:22.9913024Z Progress (1): 2.3/2.4 MB
2026-01-19T16:16:22.9917396Z Progress (1): 2.4/2.4 MB
2026-01-19T16:16:22.9920892Z Progress (1): 2.4/2.4 MB
2026-01-19T16:16:22.9925280Z Progress (1): 2.4/2.4 MB
2026-01-19T16:16:22.9978785Z Progress (1): 2.4/2.4 MB
2026-01-19T16:16:22.9997229Z Progress (1): 2.4/2.4 MB
2026-01-19T16:16:22.9997752Z Progress (1): 2.4 MB    
2026-01-19T16:16:22.9998053Z                     
2026-01-19T16:16:22.9998481Z Downloaded from central: https://repo.maven.apache.org/maven2/io/qameta/allure/allure-java-commons/2.29.0/allure-java-commons-2.29.0.jar (2.4 MB at 1.9 MB/s)
2026-01-19T16:16:23.0427433Z [INFO] 
2026-01-19T16:16:23.0433915Z [INFO] --- resources:3.3.1:resources (default-resources) @ EpturaEngageAutomation-Android ---
2026-01-19T16:16:23.0510426Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.pom
2026-01-19T16:16:23.0681431Z Progress (1): 1.4 kB
2026-01-19T16:16:23.0687423Z Progress (1): 2.7 kB
2026-01-19T16:16:23.0688976Z                     
2026-01-19T16:16:23.0690682Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.pom (2.7 kB at 148 kB/s)
2026-01-19T16:16:23.0701483Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/5.1/plexus-5.1.pom
2026-01-19T16:16:23.0967381Z Progress (1): 697 B
2026-01-19T16:16:23.0968098Z Progress (1): 2.7 kB
2026-01-19T16:16:23.0968732Z Progress (1): 6.4 kB
2026-01-19T16:16:23.0969229Z Progress (1): 9.1 kB
2026-01-19T16:16:23.0969745Z Progress (1): 11 kB 
2026-01-19T16:16:23.0970250Z Progress (1): 16 kB
2026-01-19T16:16:23.0970767Z Progress (1): 20 kB
2026-01-19T16:16:23.0971269Z Progress (1): 23 kB
2026-01-19T16:16:23.0971751Z                    
2026-01-19T16:16:23.0972340Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/5.1/plexus-5.1.pom (23 kB at 866 kB/s)
2026-01-19T16:16:23.0978890Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.pom
2026-01-19T16:16:23.1152201Z Progress (1): 725 B
2026-01-19T16:16:23.1153508Z Progress (1): 2.4 kB
2026-01-19T16:16:23.1153825Z Progress (1): 4.4 kB
2026-01-19T16:16:23.1154125Z Progress (1): 8.5 kB
2026-01-19T16:16:23.1158519Z Progress (1): 8.8 kB
2026-01-19T16:16:23.1163137Z                     
2026-01-19T16:16:23.1163591Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.pom (8.8 kB at 487 kB/s)
2026-01-19T16:16:23.1182625Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/10/plexus-10.pom
2026-01-19T16:16:23.1377795Z Progress (1): 700 B
2026-01-19T16:16:23.1381403Z Progress (1): 2.7 kB
2026-01-19T16:16:23.1381735Z Progress (1): 6.4 kB
2026-01-19T16:16:23.1382049Z Progress (1): 9.2 kB
2026-01-19T16:16:23.1382355Z Progress (1): 11 kB 
2026-01-19T16:16:23.1382660Z Progress (1): 15 kB
2026-01-19T16:16:23.1382959Z Progress (1): 20 kB
2026-01-19T16:16:23.1383260Z Progress (1): 24 kB
2026-01-19T16:16:23.1386085Z Progress (1): 25 kB
2026-01-19T16:16:23.1387924Z                    
2026-01-19T16:16:23.1388593Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/10/plexus-10.pom (25 kB at 1.2 MB/s)
2026-01-19T16:16:23.1411780Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.3.1/maven-filtering-3.3.1.pom
2026-01-19T16:16:23.1602325Z Progress (1): 799 B
2026-01-19T16:16:23.1603338Z Progress (1): 2.3 kB
2026-01-19T16:16:23.1604635Z Progress (1): 5.6 kB
2026-01-19T16:16:23.1607698Z Progress (1): 6.0 kB
2026-01-19T16:16:23.1608344Z                     
2026-01-19T16:16:23.1609665Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.3.1/maven-filtering-3.3.1.pom (6.0 kB at 302 kB/s)
2026-01-19T16:16:23.1619363Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/39/maven-shared-components-39.pom
2026-01-19T16:16:23.1773711Z Progress (1): 812 B
2026-01-19T16:16:23.1774670Z Progress (1): 2.2 kB
2026-01-19T16:16:23.1778799Z Progress (1): 3.2 kB
2026-01-19T16:16:23.1779139Z                     
2026-01-19T16:16:23.1779617Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/39/maven-shared-components-39.pom (3.2 kB at 201 kB/s)
2026-01-19T16:16:23.1806844Z Downloading from central: https://repo.maven.apache.org/maven2/javax/inject/javax.inject/1/javax.inject-1.pom
2026-01-19T16:16:23.1961739Z Progress (1): 612 B
2026-01-19T16:16:23.1963286Z                    
2026-01-19T16:16:23.1979914Z Downloaded from central: https://repo.maven.apache.org/maven2/javax/inject/javax.inject/1/javax.inject-1.pom (612 B at 36 kB/s)
2026-01-19T16:16:23.1982669Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.pom
2026-01-19T16:16:23.2182246Z Progress (1): 1.0 kB
2026-01-19T16:16:23.2185770Z Progress (1): 2.7 kB
2026-01-19T16:16:23.2186375Z                     
2026-01-19T16:16:23.2187565Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.pom (2.7 kB at 131 kB/s)
2026-01-19T16:16:23.2218002Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.36/slf4j-parent-1.7.36.pom
2026-01-19T16:16:23.2369424Z Progress (1): 1.0 kB
2026-01-19T16:16:23.2374556Z Progress (1): 3.0 kB
2026-01-19T16:16:23.2378285Z Progress (1): 5.9 kB
2026-01-19T16:16:23.2381655Z Progress (1): 8.7 kB
2026-01-19T16:16:23.2383919Z Progress (1): 12 kB 
2026-01-19T16:16:23.2384255Z Progress (1): 14 kB
2026-01-19T16:16:23.2385805Z                    
2026-01-19T16:16:23.2387565Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-parent/1.7.36/slf4j-parent-1.7.36.pom (14 kB at 783 kB/s)
2026-01-19T16:16:23.2395412Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.pom
2026-01-19T16:16:23.2582175Z Progress (1): 910 B
2026-01-19T16:16:23.2604233Z Progress (1): 3.2 kB
2026-01-19T16:16:23.2610360Z                     
2026-01-19T16:16:23.2610817Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.pom (3.2 kB at 169 kB/s)
2026-01-19T16:16:23.2611397Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/15/spice-parent-15.pom
2026-01-19T16:16:23.2796235Z Progress (1): 1.2 kB
2026-01-19T16:16:23.2799145Z Progress (1): 3.7 kB
2026-01-19T16:16:23.2800474Z Progress (1): 7.3 kB
2026-01-19T16:16:23.2803093Z Progress (1): 8.4 kB
2026-01-19T16:16:23.2806979Z                     
2026-01-19T16:16:23.2811913Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/15/spice-parent-15.pom (8.4 kB at 398 kB/s)
2026-01-19T16:16:23.2824584Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/5/forge-parent-5.pom
2026-01-19T16:16:23.2986077Z Progress (1): 1.3 kB
2026-01-19T16:16:23.2987391Z Progress (1): 5.5 kB
2026-01-19T16:16:23.2990541Z Progress (1): 8.4 kB
2026-01-19T16:16:23.2991606Z                     
2026-01-19T16:16:23.2993076Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/5/forge-parent-5.pom (8.4 kB at 492 kB/s)
2026-01-19T16:16:23.3029223Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.0/plexus-utils-3.5.0.pom
2026-01-19T16:16:23.3186030Z Progress (1): 725 B
2026-01-19T16:16:23.3190737Z Progress (1): 2.4 kB
2026-01-19T16:16:23.3196107Z Progress (1): 4.5 kB
2026-01-19T16:16:23.3200109Z Progress (1): 8.0 kB
2026-01-19T16:16:23.3204990Z                     
2026-01-19T16:16:23.3207074Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.0/plexus-utils-3.5.0.pom (8.0 kB at 445 kB/s)
2026-01-19T16:16:23.3249821Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.11.0/commons-io-2.11.0.pom
2026-01-19T16:16:23.3411723Z Progress (1): 760 B
2026-01-19T16:16:23.3416812Z Progress (1): 2.1 kB
2026-01-19T16:16:23.3417347Z Progress (1): 5.2 kB
2026-01-19T16:16:23.3418162Z Progress (1): 7.6 kB
2026-01-19T16:16:23.3420970Z Progress (1): 10 kB 
2026-01-19T16:16:23.3421308Z Progress (1): 12 kB
2026-01-19T16:16:23.3421616Z Progress (1): 15 kB
2026-01-19T16:16:23.3421942Z Progress (1): 18 kB
2026-01-19T16:16:23.3422249Z Progress (1): 20 kB
2026-01-19T16:16:23.3422544Z                    
2026-01-19T16:16:23.3422945Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.11.0/commons-io-2.11.0.pom (20 kB at 1.1 MB/s)
2026-01-19T16:16:23.3435751Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/52/commons-parent-52.pom
2026-01-19T16:16:23.3645119Z Progress (1): 702 B
2026-01-19T16:16:23.3645784Z Progress (1): 1.8 kB
2026-01-19T16:16:23.3648620Z Progress (1): 3.1 kB
2026-01-19T16:16:23.3649220Z Progress (1): 4.6 kB
2026-01-19T16:16:23.3649729Z Progress (1): 6.7 kB
2026-01-19T16:16:23.3650236Z Progress (1): 8.1 kB
2026-01-19T16:16:23.3650754Z Progress (1): 10 kB 
2026-01-19T16:16:23.3651316Z Progress (1): 12 kB
2026-01-19T16:16:23.3651840Z Progress (1): 15 kB
2026-01-19T16:16:23.3652393Z Progress (1): 17 kB
2026-01-19T16:16:23.3652856Z Progress (1): 20 kB
2026-01-19T16:16:23.3653419Z Progress (1): 22 kB
2026-01-19T16:16:23.3653951Z Progress (1): 25 kB
2026-01-19T16:16:23.3654424Z Progress (1): 29 kB
2026-01-19T16:16:23.3654867Z Progress (1): 32 kB
2026-01-19T16:16:23.3655382Z Progress (1): 32 kB
2026-01-19T16:16:23.3655865Z Progress (1): 36 kB
2026-01-19T16:16:23.3656464Z Progress (1): 39 kB
2026-01-19T16:16:23.3657280Z Progress (1): 42 kB
2026-01-19T16:16:23.3658911Z Progress (1): 44 kB
2026-01-19T16:16:23.3659255Z Progress (1): 47 kB
2026-01-19T16:16:23.3659574Z Progress (1): 51 kB
2026-01-19T16:16:23.3659897Z Progress (1): 54 kB
2026-01-19T16:16:23.3660213Z Progress (1): 56 kB
2026-01-19T16:16:23.3660531Z Progress (1): 61 kB
2026-01-19T16:16:23.3660843Z Progress (1): 65 kB
2026-01-19T16:16:23.3661168Z Progress (1): 73 kB
2026-01-19T16:16:23.3661480Z Progress (1): 75 kB
2026-01-19T16:16:23.3661783Z Progress (1): 79 kB
2026-01-19T16:16:23.3662063Z                    
2026-01-19T16:16:23.3662462Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/52/commons-parent-52.pom (79 kB at 3.8 MB/s)
2026-01-19T16:16:23.3712912Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.7.2/junit-bom-5.7.2.pom
2026-01-19T16:16:23.3908580Z Progress (1): 911 B
2026-01-19T16:16:23.3912632Z Progress (1): 4.1 kB
2026-01-19T16:16:23.3916877Z Progress (1): 5.1 kB
2026-01-19T16:16:23.3920814Z                     
2026-01-19T16:16:23.3924891Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.7.2/junit-bom-5.7.2.pom (5.1 kB at 255 kB/s)
2026-01-19T16:16:23.3938514Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.pom
2026-01-19T16:16:23.4140066Z Progress (1): 728 B
2026-01-19T16:16:23.4141643Z Progress (1): 2.0 kB
2026-01-19T16:16:23.4144129Z Progress (1): 5.2 kB
2026-01-19T16:16:23.4144578Z Progress (1): 8.8 kB
2026-01-19T16:16:23.4145211Z Progress (1): 12 kB 
2026-01-19T16:16:23.4145609Z Progress (1): 15 kB
2026-01-19T16:16:23.4146008Z Progress (1): 17 kB
2026-01-19T16:16:23.4146399Z Progress (1): 18 kB
2026-01-19T16:16:23.4147176Z Progress (1): 21 kB
2026-01-19T16:16:23.4147653Z Progress (1): 24 kB
2026-01-19T16:16:23.4148115Z Progress (1): 27 kB
2026-01-19T16:16:23.4148511Z Progress (1): 30 kB
2026-01-19T16:16:23.4148902Z Progress (1): 31 kB
2026-01-19T16:16:23.4149391Z                    
2026-01-19T16:16:23.4149978Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.pom (31 kB at 1.5 MB/s)
2026-01-19T16:16:23.4192919Z Downloading from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.7.1/junit-bom-5.7.1.pom
2026-01-19T16:16:23.4390914Z Progress (1): 911 B
2026-01-19T16:16:23.4391276Z Progress (1): 4.1 kB
2026-01-19T16:16:23.4404372Z Progress (1): 5.1 kB
2026-01-19T16:16:23.4404688Z                     
2026-01-19T16:16:23.4405113Z Downloaded from central: https://repo.maven.apache.org/maven2/org/junit/junit-bom/5.7.1/junit-bom-5.7.1.pom (5.1 kB at 255 kB/s)
2026-01-19T16:16:23.4463520Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.jar
2026-01-19T16:16:23.4475677Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.jar
2026-01-19T16:16:23.4481247Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.3.1/maven-filtering-3.3.1.jar
2026-01-19T16:16:23.4495679Z Downloading from central: https://repo.maven.apache.org/maven2/javax/inject/javax.inject/1/javax.inject-1.jar
2026-01-19T16:16:23.4497177Z Downloading from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar
2026-01-19T16:16:23.4640768Z Progress (1): 7.7/85 kB
2026-01-19T16:16:23.4641504Z Progress (1): 16/85 kB 
2026-01-19T16:16:23.4647203Z Progress (1): 32/85 kB
2026-01-19T16:16:23.4647875Z Progress (1): 49/85 kB
2026-01-19T16:16:23.4648412Z Progress (1): 65/85 kB
2026-01-19T16:16:23.4648956Z Progress (1): 81/85 kB
2026-01-19T16:16:23.4655135Z Progress (1): 85 kB   
2026-01-19T16:16:23.4655731Z                    
2026-01-19T16:16:23.4656379Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.26/plexus-interpolation-1.26.jar (85 kB at 4.1 MB/s)
2026-01-19T16:16:23.4662557Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.jar
2026-01-19T16:16:23.4693610Z Progress (1): 2.5 kB
2026-01-19T16:16:23.4694221Z                     
2026-01-19T16:16:23.4694803Z Downloaded from central: https://repo.maven.apache.org/maven2/javax/inject/javax.inject/1/javax.inject-1.jar (2.5 kB at 125 kB/s)
2026-01-19T16:16:23.4699214Z Progress (1): 3.3/269 kB
2026-01-19T16:16:23.4699783Z Progress (1): 20/269 kB 
2026-01-19T16:16:23.4702680Z Progress (1): 36/269 kB
2026-01-19T16:16:23.4703219Z Progress (1): 52/269 kB
2026-01-19T16:16:23.4703708Z Progress (1): 69/269 kB
2026-01-19T16:16:23.4704188Z Progress (1): 85/269 kB
2026-01-19T16:16:23.4704926Z Progress (1): 102/269 kB
2026-01-19T16:16:23.4706015Z Progress (1): 118/269 kB
2026-01-19T16:16:23.4706859Z                         
2026-01-19T16:16:23.4707472Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar
2026-01-19T16:16:23.4731396Z Progress (1): 134/269 kB
2026-01-19T16:16:23.4731983Z Progress (1): 151/269 kB
2026-01-19T16:16:23.4732541Z Progress (1): 167/269 kB
2026-01-19T16:16:23.4733066Z Progress (1): 184/269 kB
2026-01-19T16:16:23.4733588Z Progress (1): 200/269 kB
2026-01-19T16:16:23.4734111Z Progress (1): 216/269 kB
2026-01-19T16:16:23.4734599Z Progress (1): 233/269 kB
2026-01-19T16:16:23.4735033Z Progress (1): 249/269 kB
2026-01-19T16:16:23.4735479Z Progress (1): 265/269 kB
2026-01-19T16:16:23.4736227Z Progress (1): 269 kB    
2026-01-19T16:16:23.4736902Z Progress (2): 269 kB | 7.7/55 kB
2026-01-19T16:16:23.4737379Z Progress (2): 269 kB | 16/55 kB 
2026-01-19T16:16:23.4737844Z Progress (2): 269 kB | 32/55 kB
2026-01-19T16:16:23.4738244Z Progress (2): 269 kB | 49/55 kB
2026-01-19T16:16:23.4744394Z Progress (2): 269 kB | 55 kB   
2026-01-19T16:16:23.4744929Z                             
2026-01-19T16:16:23.4745586Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-filtering/3.3.1/maven-filtering-3.3.1.jar (55 kB at 2.0 MB/s)
2026-01-19T16:16:23.4746303Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar
2026-01-19T16:16:23.4747347Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.1/plexus-utils-3.5.1.jar (269 kB at 9.6 MB/s)
2026-01-19T16:16:23.4753344Z Progress (1): 7.7/41 kB
2026-01-19T16:16:23.4759916Z Progress (1): 16/41 kB 
2026-01-19T16:16:23.4765962Z Progress (1): 32/41 kB
2026-01-19T16:16:23.4775911Z Progress (1): 41 kB   
2026-01-19T16:16:23.4776221Z                    
2026-01-19T16:16:23.4776751Z Downloaded from central: https://repo.maven.apache.org/maven2/org/slf4j/slf4j-api/1.7.36/slf4j-api-1.7.36.jar (41 kB at 1.4 MB/s)
2026-01-19T16:16:23.4879972Z Progress (1): 7.7/8.5 kB
2026-01-19T16:16:23.4881129Z Progress (1): 8.5 kB    
2026-01-19T16:16:23.4881884Z                     
2026-01-19T16:16:23.4883556Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-build-api/0.0.7/plexus-build-api-0.0.7.jar (8.5 kB at 223 kB/s)
2026-01-19T16:16:23.4896294Z Progress (1): 7.7/327 kB
2026-01-19T16:16:23.4897135Z Progress (1): 16/327 kB 
2026-01-19T16:16:23.4897510Z Progress (1): 32/327 kB
2026-01-19T16:16:23.4897808Z Progress (1): 49/327 kB
2026-01-19T16:16:23.4902827Z Progress (1): 65/327 kB
2026-01-19T16:16:23.4910047Z Progress (1): 81/327 kB
2026-01-19T16:16:23.4918514Z Progress (1): 98/327 kB
2026-01-19T16:16:23.4919166Z Progress (1): 114/327 kB
2026-01-19T16:16:23.4924831Z Progress (1): 131/327 kB
2026-01-19T16:16:23.4930009Z Progress (1): 147/327 kB
2026-01-19T16:16:23.4947827Z Progress (1): 163/327 kB
2026-01-19T16:16:23.4951397Z Progress (1): 180/327 kB
2026-01-19T16:16:23.4953159Z Progress (1): 196/327 kB
2026-01-19T16:16:23.4954921Z Progress (1): 213/327 kB
2026-01-19T16:16:23.4955458Z Progress (1): 229/327 kB
2026-01-19T16:16:23.4956008Z Progress (1): 245/327 kB
2026-01-19T16:16:23.4956784Z Progress (1): 262/327 kB
2026-01-19T16:16:23.4957646Z Progress (1): 278/327 kB
2026-01-19T16:16:23.4957953Z Progress (1): 294/327 kB
2026-01-19T16:16:23.4958257Z Progress (1): 311/327 kB
2026-01-19T16:16:23.4958547Z Progress (1): 327 kB    
2026-01-19T16:16:23.4958827Z                     
2026-01-19T16:16:23.4959215Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.11.0/commons-io-2.11.0.jar (327 kB at 7.1 MB/s)
2026-01-19T16:16:23.4988455Z Progress (1): 7.7/587 kB
2026-01-19T16:16:23.4989695Z Progress (1): 16/587 kB 
2026-01-19T16:16:23.4990239Z Progress (1): 32/587 kB
2026-01-19T16:16:23.4990727Z Progress (1): 49/587 kB
2026-01-19T16:16:23.4991039Z Progress (1): 65/587 kB
2026-01-19T16:16:23.4991342Z Progress (1): 81/587 kB
2026-01-19T16:16:23.4991633Z Progress (1): 98/587 kB
2026-01-19T16:16:23.4992086Z Progress (1): 114/587 kB
2026-01-19T16:16:23.4992388Z Progress (1): 131/587 kB
2026-01-19T16:16:23.4992691Z Progress (1): 147/587 kB
2026-01-19T16:16:23.4992986Z Progress (1): 163/587 kB
2026-01-19T16:16:23.4993287Z Progress (1): 180/587 kB
2026-01-19T16:16:23.4993577Z Progress (1): 196/587 kB
2026-01-19T16:16:23.4993880Z Progress (1): 213/587 kB
2026-01-19T16:16:23.4996764Z Progress (1): 229/587 kB
2026-01-19T16:16:23.4999898Z Progress (1): 245/587 kB
2026-01-19T16:16:23.5003356Z Progress (1): 262/587 kB
2026-01-19T16:16:23.5027145Z Progress (1): 278/587 kB
2026-01-19T16:16:23.5027676Z Progress (1): 294/587 kB
2026-01-19T16:16:23.5027998Z Progress (1): 311/587 kB
2026-01-19T16:16:23.5028455Z Progress (1): 327/587 kB
2026-01-19T16:16:23.5028751Z Progress (1): 344/587 kB
2026-01-19T16:16:23.5029042Z Progress (1): 360/587 kB
2026-01-19T16:16:23.5029334Z Progress (1): 376/587 kB
2026-01-19T16:16:23.5029621Z Progress (1): 393/587 kB
2026-01-19T16:16:23.5029912Z Progress (1): 409/587 kB
2026-01-19T16:16:23.5030204Z Progress (1): 426/587 kB
2026-01-19T16:16:23.5030526Z Progress (1): 442/587 kB
2026-01-19T16:16:23.5030812Z Progress (1): 458/587 kB
2026-01-19T16:16:23.5031127Z Progress (1): 475/587 kB
2026-01-19T16:16:23.5031439Z Progress (1): 491/587 kB
2026-01-19T16:16:23.5031753Z Progress (1): 507/587 kB
2026-01-19T16:16:23.5036334Z Progress (1): 524/587 kB
2026-01-19T16:16:23.5069053Z Progress (1): 540/587 kB
2026-01-19T16:16:23.5069587Z Progress (1): 557/587 kB
2026-01-19T16:16:23.5069881Z Progress (1): 573/587 kB
2026-01-19T16:16:23.5070166Z Progress (1): 587 kB    
2026-01-19T16:16:23.5070446Z                     
2026-01-19T16:16:23.5070848Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-lang3/3.12.0/commons-lang3-3.12.0.jar (587 kB at 11 MB/s)
2026-01-19T16:16:23.6339140Z [INFO] Copying 4 resources from src/main/resources to target/classes
2026-01-19T16:16:23.6443864Z [INFO] 
2026-01-19T16:16:23.6544345Z [INFO] --- compiler:3.11.0:compile (default-compile) @ EpturaEngageAutomation-Android ---
2026-01-19T16:16:23.6633038Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.3.4/maven-shared-utils-3.3.4.pom
2026-01-19T16:16:23.6850973Z Progress (1): 787 B
2026-01-19T16:16:23.6854856Z Progress (1): 2.3 kB
2026-01-19T16:16:23.6863913Z Progress (1): 4.3 kB
2026-01-19T16:16:23.6867741Z Progress (1): 5.8 kB
2026-01-19T16:16:23.6870679Z                     
2026-01-19T16:16:23.6872321Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.3.4/maven-shared-utils-3.3.4.pom (5.8 kB at 243 kB/s)
2026-01-19T16:16:23.6890157Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/34/maven-shared-components-34.pom
2026-01-19T16:16:23.7150830Z Progress (1): 798 B
2026-01-19T16:16:23.7151966Z Progress (1): 2.3 kB
2026-01-19T16:16:23.7152909Z Progress (1): 4.6 kB
2026-01-19T16:16:23.7155160Z Progress (1): 5.1 kB
2026-01-19T16:16:23.7155528Z                     
2026-01-19T16:16:23.7156033Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/34/maven-shared-components-34.pom (5.1 kB at 189 kB/s)
2026-01-19T16:16:23.7167751Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/34/maven-parent-34.pom
2026-01-19T16:16:23.7441827Z Progress (1): 721 B
2026-01-19T16:16:23.7447445Z Progress (1): 1.9 kB
2026-01-19T16:16:23.7449931Z Progress (1): 5.4 kB
2026-01-19T16:16:23.7450425Z Progress (1): 9.8 kB
2026-01-19T16:16:23.7454092Z Progress (1): 14 kB 
2026-01-19T16:16:23.7454575Z Progress (1): 19 kB
2026-01-19T16:16:23.7456661Z Progress (1): 23 kB
2026-01-19T16:16:23.7458382Z Progress (1): 26 kB
2026-01-19T16:16:23.7460186Z Progress (1): 27 kB
2026-01-19T16:16:23.7460994Z Progress (1): 30 kB
2026-01-19T16:16:23.7463121Z Progress (1): 34 kB
2026-01-19T16:16:23.7463634Z Progress (1): 37 kB
2026-01-19T16:16:23.7464192Z Progress (1): 40 kB
2026-01-19T16:16:23.7474989Z Progress (1): 43 kB
2026-01-19T16:16:23.7475352Z                    
2026-01-19T16:16:23.7475837Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/34/maven-parent-34.pom (43 kB at 1.5 MB/s)
2026-01-19T16:16:23.7477433Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.6/commons-io-2.6.pom
2026-01-19T16:16:23.7671127Z Progress (1): 774 B
2026-01-19T16:16:23.7697690Z Progress (1): 2.1 kB
2026-01-19T16:16:23.7698312Z Progress (1): 5.3 kB
2026-01-19T16:16:23.7698866Z Progress (1): 7.4 kB
2026-01-19T16:16:23.7699455Z Progress (1): 9.4 kB
2026-01-19T16:16:23.7699978Z Progress (1): 12 kB 
2026-01-19T16:16:23.7700708Z Progress (1): 14 kB
2026-01-19T16:16:23.7701207Z                    
2026-01-19T16:16:23.7701853Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.6/commons-io-2.6.pom (14 kB at 648 kB/s)
2026-01-19T16:16:23.7712156Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/42/commons-parent-42.pom
2026-01-19T16:16:23.7973046Z Progress (1): 707 B
2026-01-19T16:16:23.8007523Z Progress (1): 1.9 kB
2026-01-19T16:16:23.8008360Z Progress (1): 3.1 kB
2026-01-19T16:16:23.8009101Z Progress (1): 4.5 kB
2026-01-19T16:16:23.8009701Z Progress (1): 5.9 kB
2026-01-19T16:16:23.8010227Z Progress (1): 7.5 kB
2026-01-19T16:16:23.8010780Z Progress (1): 11 kB 
2026-01-19T16:16:23.8011363Z Progress (1): 14 kB
2026-01-19T16:16:23.8011954Z Progress (1): 17 kB
2026-01-19T16:16:23.8012516Z Progress (1): 20 kB
2026-01-19T16:16:23.8013052Z Progress (1): 23 kB
2026-01-19T16:16:23.8013615Z Progress (1): 26 kB
2026-01-19T16:16:23.8014199Z Progress (1): 29 kB
2026-01-19T16:16:23.8014756Z Progress (1): 31 kB
2026-01-19T16:16:23.8015319Z Progress (1): 34 kB
2026-01-19T16:16:23.8015889Z Progress (1): 34 kB
2026-01-19T16:16:23.8016442Z Progress (1): 37 kB
2026-01-19T16:16:23.8017209Z Progress (1): 40 kB
2026-01-19T16:16:23.8017777Z Progress (1): 44 kB
2026-01-19T16:16:23.8018437Z Progress (1): 48 kB
2026-01-19T16:16:23.8019004Z Progress (1): 53 kB
2026-01-19T16:16:23.8019566Z Progress (1): 55 kB
2026-01-19T16:16:23.8020129Z Progress (1): 59 kB
2026-01-19T16:16:23.8020706Z Progress (1): 60 kB
2026-01-19T16:16:23.8021319Z Progress (1): 62 kB
2026-01-19T16:16:23.8022349Z Progress (1): 65 kB
2026-01-19T16:16:23.8022854Z Progress (1): 66 kB
2026-01-19T16:16:23.8023386Z Progress (1): 68 kB
2026-01-19T16:16:23.8023938Z                    
2026-01-19T16:16:23.8024626Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/commons/commons-parent/42/commons-parent-42.pom (68 kB at 2.6 MB/s)
2026-01-19T16:16:23.8067537Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/18/apache-18.pom
2026-01-19T16:16:23.8308736Z Progress (1): 745 B
2026-01-19T16:16:23.8313815Z Progress (1): 2.1 kB
2026-01-19T16:16:23.8318825Z Progress (1): 3.9 kB
2026-01-19T16:16:23.8323640Z Progress (1): 8.0 kB
2026-01-19T16:16:23.8328581Z Progress (1): 12 kB 
2026-01-19T16:16:23.8332808Z Progress (1): 14 kB
2026-01-19T16:16:23.8341393Z Progress (1): 16 kB
2026-01-19T16:16:23.8347131Z                    
2026-01-19T16:16:23.8347825Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/18/apache-18.pom (16 kB at 580 kB/s)
2026-01-19T16:16:23.8378392Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom
2026-01-19T16:16:23.8596088Z Progress (1): 803 B
2026-01-19T16:16:23.8602144Z Progress (1): 2.3 kB
2026-01-19T16:16:23.8602708Z Progress (1): 4.7 kB
2026-01-19T16:16:23.8603827Z                     
2026-01-19T16:16:23.8604399Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.pom (4.7 kB at 206 kB/s)
2026-01-19T16:16:23.8621639Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom
2026-01-19T16:16:23.8830121Z Progress (1): 773 B
2026-01-19T16:16:23.8831783Z Progress (1): 2.4 kB
2026-01-19T16:16:23.8838381Z Progress (1): 4.2 kB
2026-01-19T16:16:23.8842319Z Progress (1): 6.4 kB
2026-01-19T16:16:23.8842844Z                     
2026-01-19T16:16:23.8844057Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-components/19/maven-shared-components-19.pom (6.4 kB at 276 kB/s)
2026-01-19T16:16:23.8865230Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/23/maven-parent-23.pom
2026-01-19T16:16:23.9137103Z Progress (1): 721 B
2026-01-19T16:16:23.9139144Z Progress (1): 1.9 kB
2026-01-19T16:16:23.9147233Z Progress (1): 5.9 kB
2026-01-19T16:16:23.9147828Z Progress (1): 10 kB 
2026-01-19T16:16:23.9148315Z Progress (1): 15 kB
2026-01-19T16:16:23.9150039Z Progress (1): 18 kB
2026-01-19T16:16:23.9150517Z Progress (1): 22 kB
2026-01-19T16:16:23.9150916Z Progress (1): 25 kB
2026-01-19T16:16:23.9151327Z Progress (1): 27 kB
2026-01-19T16:16:23.9151714Z Progress (1): 31 kB
2026-01-19T16:16:23.9152107Z Progress (1): 33 kB
2026-01-19T16:16:23.9152484Z                    
2026-01-19T16:16:23.9153612Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/23/maven-parent-23.pom (33 kB at 1.1 MB/s)
2026-01-19T16:16:23.9188048Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/apache/13/apache-13.pom
2026-01-19T16:16:23.9435599Z Progress (1): 749 B
2026-01-19T16:16:23.9440228Z Progress (1): 2.1 kB
2026-01-19T16:16:23.9444491Z Progress (1): 4.1 kB
2026-01-19T16:16:23.9448316Z Progress (1): 8.9 kB
2026-01-19T16:16:23.9480948Z Progress (1): 11 kB 
2026-01-19T16:16:23.9481594Z Progress (1): 14 kB
2026-01-19T16:16:23.9482036Z                    
2026-01-19T16:16:23.9483283Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/apache/13/apache-13.pom (14 kB at 499 kB/s)
2026-01-19T16:16:23.9496005Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/1.5.5/plexus-component-annotations-1.5.5.pom
2026-01-19T16:16:23.9723876Z Progress (1): 815 B
2026-01-19T16:16:23.9724534Z                    
2026-01-19T16:16:23.9728104Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/1.5.5/plexus-component-annotations-1.5.5.pom (815 B at 35 kB/s)
2026-01-19T16:16:23.9752996Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/1.5.5/plexus-containers-1.5.5.pom
2026-01-19T16:16:24.0016294Z Progress (1): 1.3 kB
2026-01-19T16:16:24.0024485Z Progress (1): 4.2 kB
2026-01-19T16:16:24.0024819Z                     
2026-01-19T16:16:24.0025240Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/1.5.5/plexus-containers-1.5.5.pom (4.2 kB at 151 kB/s)
2026-01-19T16:16:24.0043577Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/2.0.7/plexus-2.0.7.pom
2026-01-19T16:16:24.0257202Z Progress (1): 711 B
2026-01-19T16:16:24.0259992Z Progress (1): 2.7 kB
2026-01-19T16:16:24.0260510Z Progress (1): 6.3 kB
2026-01-19T16:16:24.0260995Z Progress (1): 9.1 kB
2026-01-19T16:16:24.0261450Z Progress (1): 13 kB 
2026-01-19T16:16:24.0261907Z Progress (1): 17 kB
2026-01-19T16:16:24.0262362Z Progress (1): 17 kB
2026-01-19T16:16:24.0265183Z                    
2026-01-19T16:16:24.0265820Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/2.0.7/plexus-2.0.7.pom (17 kB at 824 kB/s)
2026-01-19T16:16:24.0309474Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-java/1.1.2/plexus-java-1.1.2.pom
2026-01-19T16:16:24.0544708Z Progress (1): 1.3 kB
2026-01-19T16:16:24.0547553Z Progress (1): 4.2 kB
2026-01-19T16:16:24.0556282Z Progress (1): 5.0 kB
2026-01-19T16:16:24.0573613Z                     
2026-01-19T16:16:24.0577849Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-java/1.1.2/plexus-java-1.1.2.pom (5.0 kB at 199 kB/s)
2026-01-19T16:16:24.0578976Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-languages/1.1.2/plexus-languages-1.1.2.pom
2026-01-19T16:16:24.0838583Z Progress (1): 1.3 kB
2026-01-19T16:16:24.0847633Z Progress (1): 4.1 kB
2026-01-19T16:16:24.0852250Z                     
2026-01-19T16:16:24.0855418Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-languages/1.1.2/plexus-languages-1.1.2.pom (4.1 kB at 148 kB/s)
2026-01-19T16:16:24.0895158Z Downloading from central: https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.4/asm-9.4.pom
2026-01-19T16:16:24.1138689Z Progress (1): 1.3 kB
2026-01-19T16:16:24.1144182Z Progress (1): 2.4 kB
2026-01-19T16:16:24.1144861Z                     
2026-01-19T16:16:24.1145589Z Downloaded from central: https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.4/asm-9.4.pom (2.4 kB at 91 kB/s)
2026-01-19T16:16:24.1167846Z Downloading from central: https://repo.maven.apache.org/maven2/org/ow2/ow2/1.5.1/ow2-1.5.1.pom
2026-01-19T16:16:24.1436882Z Progress (1): 707 B
2026-01-19T16:16:24.1438188Z Progress (1): 2.1 kB
2026-01-19T16:16:24.1438796Z Progress (1): 3.6 kB
2026-01-19T16:16:24.1439409Z Progress (1): 5.7 kB
2026-01-19T16:16:24.1439899Z Progress (1): 8.0 kB
2026-01-19T16:16:24.1440383Z Progress (1): 11 kB 
2026-01-19T16:16:24.1440867Z                    
2026-01-19T16:16:24.1441461Z Downloaded from central: https://repo.maven.apache.org/maven2/org/ow2/ow2/1.5.1/ow2-1.5.1.pom (11 kB at 452 kB/s)
2026-01-19T16:16:24.1442225Z Downloading from central: https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.pom
2026-01-19T16:16:24.1686432Z Progress (1): 871 B
2026-01-19T16:16:24.1688397Z Progress (1): 3.4 kB
2026-01-19T16:16:24.1689076Z Progress (1): 6.6 kB
2026-01-19T16:16:24.1690588Z Progress (1): 10 kB 
2026-01-19T16:16:24.1691182Z Progress (1): 13 kB
2026-01-19T16:16:24.1691882Z Progress (1): 17 kB
2026-01-19T16:16:24.1707731Z                    
2026-01-19T16:16:24.1708333Z Downloaded from central: https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.pom (17 kB at 663 kB/s)
2026-01-19T16:16:24.1741284Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-api/2.13.0/plexus-compiler-api-2.13.0.pom
2026-01-19T16:16:24.1978416Z Progress (1): 1.1 kB
2026-01-19T16:16:24.1980974Z                     
2026-01-19T16:16:24.1981420Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-api/2.13.0/plexus-compiler-api-2.13.0.pom (1.1 kB at 48 kB/s)
2026-01-19T16:16:24.1982003Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler/2.13.0/plexus-compiler-2.13.0.pom
2026-01-19T16:16:24.2198134Z Progress (1): 1.2 kB
2026-01-19T16:16:24.2200071Z Progress (1): 4.1 kB
2026-01-19T16:16:24.2200820Z Progress (1): 7.3 kB
2026-01-19T16:16:24.2202171Z Progress (1): 8.4 kB
2026-01-19T16:16:24.2202470Z                     
2026-01-19T16:16:24.2202891Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler/2.13.0/plexus-compiler-2.13.0.pom (8.4 kB at 364 kB/s)
2026-01-19T16:16:24.2215492Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/10.0/plexus-components-10.0.pom
2026-01-19T16:16:24.2429854Z Progress (1): 1.3 kB
2026-01-19T16:16:24.2434447Z Progress (1): 2.7 kB
2026-01-19T16:16:24.2437144Z                     
2026-01-19T16:16:24.2437707Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/10.0/plexus-components-10.0.pom (2.7 kB at 122 kB/s)
2026-01-19T16:16:24.2459990Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-manager/2.13.0/plexus-compiler-manager-2.13.0.pom
2026-01-19T16:16:24.2685357Z Progress (1): 1.1 kB
2026-01-19T16:16:24.2687325Z                     
2026-01-19T16:16:24.2688472Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-manager/2.13.0/plexus-compiler-manager-2.13.0.pom (1.1 kB at 49 kB/s)
2026-01-19T16:16:24.2705625Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/2.1.1/plexus-component-annotations-2.1.1.pom
2026-01-19T16:16:24.2910261Z Progress (1): 770 B
2026-01-19T16:16:24.2911845Z                    
2026-01-19T16:16:24.2912380Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/2.1.1/plexus-component-annotations-2.1.1.pom (770 B at 38 kB/s)
2026-01-19T16:16:24.2923526Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/2.1.1/plexus-containers-2.1.1.pom
2026-01-19T16:16:24.3124162Z Progress (1): 1.3 kB
2026-01-19T16:16:24.3124688Z Progress (1): 4.9 kB
2026-01-19T16:16:24.3129817Z Progress (1): 6.0 kB
2026-01-19T16:16:24.3130443Z                     
2026-01-19T16:16:24.3131784Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-containers/2.1.1/plexus-containers-2.1.1.pom (6.0 kB at 287 kB/s)
2026-01-19T16:16:24.3149902Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/6.5/plexus-6.5.pom
2026-01-19T16:16:24.3396248Z Progress (1): 692 B
2026-01-19T16:16:24.3397148Z Progress (1): 2.7 kB
2026-01-19T16:16:24.3397466Z Progress (1): 6.4 kB
2026-01-19T16:16:24.3397771Z Progress (1): 9.2 kB
2026-01-19T16:16:24.3398079Z Progress (1): 11 kB 
2026-01-19T16:16:24.3398380Z Progress (1): 15 kB
2026-01-19T16:16:24.3398689Z Progress (1): 20 kB
2026-01-19T16:16:24.3399009Z Progress (1): 24 kB
2026-01-19T16:16:24.3399315Z Progress (1): 26 kB
2026-01-19T16:16:24.3399607Z                    
2026-01-19T16:16:24.3400273Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/6.5/plexus-6.5.pom (26 kB at 989 kB/s)
2026-01-19T16:16:24.3422012Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.13.0/plexus-compiler-javac-2.13.0.pom
2026-01-19T16:16:24.3701673Z Progress (1): 1.2 kB
2026-01-19T16:16:24.3702335Z                     
2026-01-19T16:16:24.3703055Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.13.0/plexus-compiler-javac-2.13.0.pom (1.2 kB at 43 kB/s)
2026-01-19T16:16:24.3728885Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compilers/2.13.0/plexus-compilers-2.13.0.pom
2026-01-19T16:16:24.3930188Z Progress (1): 1.3 kB
2026-01-19T16:16:24.3931194Z                     
2026-01-19T16:16:24.3931806Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compilers/2.13.0/plexus-compilers-2.13.0.pom (1.3 kB at 66 kB/s)
2026-01-19T16:16:24.3998913Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.3.4/maven-shared-utils-3.3.4.jar
2026-01-19T16:16:24.4017576Z Downloading from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.6/commons-io-2.6.jar
2026-01-19T16:16:24.4024020Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar
2026-01-19T16:16:24.4039285Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/1.5.5/plexus-component-annotations-1.5.5.jar
2026-01-19T16:16:24.4039873Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-java/1.1.2/plexus-java-1.1.2.jar
2026-01-19T16:16:24.4241185Z Progress (1): 7.7/153 kB
2026-01-19T16:16:24.4241905Z Progress (1): 16/153 kB 
2026-01-19T16:16:24.4243087Z Progress (2): 16/153 kB | 7.5/215 kB
2026-01-19T16:16:24.4243778Z Progress (2): 16/153 kB | 24/215 kB 
2026-01-19T16:16:24.4244335Z Progress (2): 32/153 kB | 24/215 kB
2026-01-19T16:16:24.4245103Z Progress (2): 32/153 kB | 40/215 kB
2026-01-19T16:16:24.4247834Z Progress (2): 49/153 kB | 40/215 kB
2026-01-19T16:16:24.4248237Z Progress (2): 49/153 kB | 57/215 kB
2026-01-19T16:16:24.4248587Z Progress (2): 65/153 kB | 57/215 kB
2026-01-19T16:16:24.4248915Z Progress (2): 65/153 kB | 73/215 kB
2026-01-19T16:16:24.4249251Z Progress (2): 81/153 kB | 73/215 kB
2026-01-19T16:16:24.4249585Z Progress (2): 81/153 kB | 89/215 kB
2026-01-19T16:16:24.4249928Z Progress (2): 98/153 kB | 89/215 kB
2026-01-19T16:16:24.4250263Z Progress (2): 98/153 kB | 106/215 kB
2026-01-19T16:16:24.4250615Z Progress (2): 114/153 kB | 106/215 kB
2026-01-19T16:16:24.4250949Z Progress (2): 114/153 kB | 122/215 kB
2026-01-19T16:16:24.4251503Z Progress (2): 114/153 kB | 130/215 kB
2026-01-19T16:16:24.4251842Z Progress (2): 131/153 kB | 130/215 kB
2026-01-19T16:16:24.4252190Z Progress (2): 131/153 kB | 147/215 kB
2026-01-19T16:16:24.4252532Z Progress (2): 147/153 kB | 147/215 kB
2026-01-19T16:16:24.4252873Z Progress (2): 147/153 kB | 163/215 kB
2026-01-19T16:16:24.4253218Z Progress (2): 153 kB | 163/215 kB    
2026-01-19T16:16:24.4253564Z Progress (2): 153 kB | 180/215 kB
2026-01-19T16:16:24.4253896Z Progress (2): 153 kB | 196/215 kB
2026-01-19T16:16:24.4254243Z Progress (2): 153 kB | 212/215 kB
2026-01-19T16:16:24.4254553Z                                  
2026-01-19T16:16:24.4254983Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-utils/3.3.4/maven-shared-utils-3.3.4.jar (153 kB at 6.7 MB/s)
2026-01-19T16:16:24.4255542Z Downloading from central: https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.4/asm-9.4.jar
2026-01-19T16:16:24.4255949Z Progress (1): 215 kB
2026-01-19T16:16:24.4256293Z Progress (2): 215 kB | 7.7/14 kB
2026-01-19T16:16:24.4256865Z Progress (2): 215 kB | 14 kB    
2026-01-19T16:16:24.4257177Z                             
2026-01-19T16:16:24.4257576Z Downloaded from central: https://repo.maven.apache.org/maven2/commons-io/commons-io/2.6/commons-io-2.6.jar (215 kB at 8.9 MB/s)
2026-01-19T16:16:24.4258112Z Downloading from central: https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.jar
2026-01-19T16:16:24.4258675Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-shared-incremental/1.1/maven-shared-incremental-1.1.jar (14 kB at 589 kB/s)
2026-01-19T16:16:24.4259260Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-api/2.13.0/plexus-compiler-api-2.13.0.jar
2026-01-19T16:16:24.4279764Z Progress (1): 7.7/55 kB
2026-01-19T16:16:24.4290758Z Progress (1): 16/55 kB 
2026-01-19T16:16:24.4291176Z Progress (2): 16/55 kB | 4.2 kB
2026-01-19T16:16:24.4291503Z Progress (2): 32/55 kB | 4.2 kB
2026-01-19T16:16:24.4291831Z Progress (2): 49/55 kB | 4.2 kB
2026-01-19T16:16:24.4292120Z                                
2026-01-19T16:16:24.4292566Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-component-annotations/1.5.5/plexus-component-annotations-1.5.5.jar (4.2 kB at 162 kB/s)
2026-01-19T16:16:24.4293137Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.0/plexus-utils-3.5.0.jar
2026-01-19T16:16:24.4293559Z Progress (1): 55 kB
2026-01-19T16:16:24.4293852Z                    
2026-01-19T16:16:24.4294268Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-java/1.1.2/plexus-java-1.1.2.jar (55 kB at 2.2 MB/s)
2026-01-19T16:16:24.4300100Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-manager/2.13.0/plexus-compiler-manager-2.13.0.jar
2026-01-19T16:16:24.4433406Z Progress (1): 7.7/334 kB
2026-01-19T16:16:24.4434817Z Progress (1): 16/334 kB 
2026-01-19T16:16:24.4437283Z Progress (1): 32/334 kB
2026-01-19T16:16:24.4438366Z Progress (1): 49/334 kB
2026-01-19T16:16:24.4440563Z Progress (1): 57/334 kB
2026-01-19T16:16:24.4444311Z Progress (1): 74/334 kB
2026-01-19T16:16:24.4444790Z Progress (1): 90/334 kB
2026-01-19T16:16:24.4445441Z Progress (1): 106/334 kB
2026-01-19T16:16:24.4445871Z Progress (1): 123/334 kB
2026-01-19T16:16:24.4446286Z Progress (1): 139/334 kB
2026-01-19T16:16:24.4446887Z Progress (1): 156/334 kB
2026-01-19T16:16:24.4447321Z Progress (1): 172/334 kB
2026-01-19T16:16:24.4447740Z Progress (1): 188/334 kB
2026-01-19T16:16:24.4448145Z Progress (1): 205/334 kB
2026-01-19T16:16:24.4448556Z Progress (1): 221/334 kB
2026-01-19T16:16:24.4448985Z Progress (2): 221/334 kB | 7.7/122 kB
2026-01-19T16:16:24.4449450Z Progress (2): 221/334 kB | 8.2/122 kB
2026-01-19T16:16:24.4449891Z Progress (2): 221/334 kB | 25/122 kB 
2026-01-19T16:16:24.4450242Z Progress (2): 238/334 kB | 25/122 kB
2026-01-19T16:16:24.4452815Z Progress (2): 238/334 kB | 41/122 kB
2026-01-19T16:16:24.4453130Z Progress (2): 238/334 kB | 57/122 kB
2026-01-19T16:16:24.4453919Z Progress (2): 254/334 kB | 57/122 kB
2026-01-19T16:16:24.4454244Z Progress (2): 254/334 kB | 74/122 kB
2026-01-19T16:16:24.4454547Z Progress (2): 262/334 kB | 74/122 kB
2026-01-19T16:16:24.4454876Z Progress (2): 262/334 kB | 90/122 kB
2026-01-19T16:16:24.4455185Z Progress (2): 262/334 kB | 106/122 kB
2026-01-19T16:16:24.4455499Z Progress (2): 279/334 kB | 106/122 kB
2026-01-19T16:16:24.4455819Z Progress (2): 279/334 kB | 122 kB    
2026-01-19T16:16:24.4456155Z Progress (2): 295/334 kB | 122 kB
2026-01-19T16:16:24.4456702Z Progress (2): 311/334 kB | 122 kB
2026-01-19T16:16:24.4457033Z                                  
2026-01-19T16:16:24.4457422Z Downloaded from central: https://repo.maven.apache.org/maven2/org/ow2/asm/asm/9.4/asm-9.4.jar (122 kB at 3.1 MB/s)
2026-01-19T16:16:24.4457848Z Progress (1): 328/334 kB
2026-01-19T16:16:24.4458156Z                         
2026-01-19T16:16:24.4458597Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.13.0/plexus-compiler-javac-2.13.0.jar
2026-01-19T16:16:24.4459058Z Progress (1): 334 kB
2026-01-19T16:16:24.4460187Z                     
2026-01-19T16:16:24.4460572Z Downloaded from central: https://repo.maven.apache.org/maven2/com/thoughtworks/qdox/qdox/2.0.3/qdox-2.0.3.jar (334 kB at 8.2 MB/s)
2026-01-19T16:16:24.4461016Z Progress (1): 7.7/27 kB
2026-01-19T16:16:24.4461309Z Progress (1): 12/27 kB 
2026-01-19T16:16:24.4461607Z Progress (1): 27 kB   
2026-01-19T16:16:24.4461880Z                    
2026-01-19T16:16:24.4462121Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-api/2.13.0/plexus-compiler-api-2.13.0.jar (27 kB at 643 kB/s)
2026-01-19T16:16:24.4478209Z Progress (1): 7.7/267 kB
2026-01-19T16:16:24.4478868Z Progress (1): 16/267 kB 
2026-01-19T16:16:24.4479215Z Progress (1): 32/267 kB
2026-01-19T16:16:24.4497541Z Progress (1): 48/267 kB
2026-01-19T16:16:24.4498345Z Progress (1): 65/267 kB
2026-01-19T16:16:24.4498878Z Progress (1): 81/267 kB
2026-01-19T16:16:24.4500071Z Progress (1): 98/267 kB
2026-01-19T16:16:24.4505869Z Progress (1): 114/267 kB
2026-01-19T16:16:24.4506690Z Progress (1): 130/267 kB
2026-01-19T16:16:24.4508662Z Progress (1): 147/267 kB
2026-01-19T16:16:24.4509015Z Progress (1): 163/267 kB
2026-01-19T16:16:24.4509327Z Progress (1): 180/267 kB
2026-01-19T16:16:24.4509650Z Progress (1): 196/267 kB
2026-01-19T16:16:24.4519656Z Progress (1): 212/267 kB
2026-01-19T16:16:24.4520011Z Progress (1): 229/267 kB
2026-01-19T16:16:24.4520351Z Progress (1): 245/267 kB
2026-01-19T16:16:24.4520676Z Progress (1): 261/267 kB
2026-01-19T16:16:24.4527223Z Progress (1): 267 kB    
2026-01-19T16:16:24.4527548Z                     
2026-01-19T16:16:24.4527986Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.5.0/plexus-utils-3.5.0.jar (267 kB at 5.5 MB/s)
2026-01-19T16:16:24.4530666Z Progress (1): 4.7 kB
2026-01-19T16:16:24.4531016Z                     
2026-01-19T16:16:24.4531446Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-manager/2.13.0/plexus-compiler-manager-2.13.0.jar (4.7 kB at 95 kB/s)
2026-01-19T16:16:24.4622617Z Progress (1): 7.7/23 kB
2026-01-19T16:16:24.4623068Z Progress (1): 12/23 kB 
2026-01-19T16:16:24.4626446Z Progress (1): 23 kB   
2026-01-19T16:16:24.4626991Z                    
2026-01-19T16:16:24.4627418Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-compiler-javac/2.13.0/plexus-compiler-javac-2.13.0.jar (23 kB at 386 kB/s)
2026-01-19T16:16:24.6369506Z [INFO] Changes detected - recompiling the module! :source
2026-01-19T16:16:24.6405596Z [INFO] Compiling 6 source files with javac [debug target 11] to target/classes
2026-01-19T16:16:26.8549317Z [INFO] 
2026-01-19T16:16:26.8552029Z [INFO] --- resources:3.3.1:testResources (default-testResources) @ EpturaEngageAutomation-Android ---
2026-01-19T16:16:26.8607011Z [INFO] skip non existing resourceDirectory /home/vsts/work/1/s/src/test/resources
2026-01-19T16:16:26.8628732Z [INFO] 
2026-01-19T16:16:26.8631178Z [INFO] --- compiler:3.11.0:testCompile (default-testCompile) @ EpturaEngageAutomation-Android ---
2026-01-19T16:16:26.8725027Z [INFO] Changes detected - recompiling the module! :dependency
2026-01-19T16:16:26.8726993Z [INFO] Compiling 6 source files with javac [debug target 11] to target/test-classes
2026-01-19T16:16:27.5075909Z [INFO] 
2026-01-19T16:16:27.5081490Z [INFO] --- surefire:3.0.0-M9:test (default-test) @ EpturaEngageAutomation-Android ---
2026-01-19T16:16:27.5172741Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/3.0.0-M9/maven-surefire-common-3.0.0-M9.pom
2026-01-19T16:16:27.5419772Z Progress (1): 818 B
2026-01-19T16:16:27.5421981Z Progress (1): 4.1 kB
2026-01-19T16:16:27.5428228Z Progress (1): 6.5 kB
2026-01-19T16:16:27.5428882Z                     
2026-01-19T16:16:27.5433239Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/3.0.0-M9/maven-surefire-common-3.0.0-M9.pom (6.5 kB at 240 kB/s)
2026-01-19T16:16:27.5470600Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/3.0.0-M9/surefire-api-3.0.0-M9.pom
2026-01-19T16:16:27.5677396Z Progress (1): 858 B
2026-01-19T16:16:27.5678066Z Progress (1): 2.8 kB
2026-01-19T16:16:27.5678590Z Progress (1): 3.4 kB
2026-01-19T16:16:27.5680359Z                     
2026-01-19T16:16:27.5681102Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/3.0.0-M9/surefire-api-3.0.0-M9.pom (3.4 kB at 161 kB/s)
2026-01-19T16:16:27.5717689Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-logger-api/3.0.0-M9/surefire-logger-api-3.0.0-M9.pom
2026-01-19T16:16:27.5937879Z Progress (1): 827 B
2026-01-19T16:16:27.5938234Z Progress (1): 2.4 kB
2026-01-19T16:16:27.5938966Z Progress (1): 3.6 kB
2026-01-19T16:16:27.5939400Z                     
2026-01-19T16:16:27.5939919Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-logger-api/3.0.0-M9/surefire-logger-api-3.0.0-M9.pom (3.6 kB at 163 kB/s)
2026-01-19T16:16:27.5975634Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-shared-utils/3.0.0-M9/surefire-shared-utils-3.0.0-M9.pom
2026-01-19T16:16:27.6162081Z Progress (1): 1.1 kB
2026-01-19T16:16:27.6167326Z Progress (1): 4.1 kB
2026-01-19T16:16:27.6170976Z                     
2026-01-19T16:16:27.6173516Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-shared-utils/3.0.0-M9/surefire-shared-utils-3.0.0-M9.pom (4.1 kB at 203 kB/s)
2026-01-19T16:16:27.6210300Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-api/3.0.0-M9/surefire-extensions-api-3.0.0-M9.pom
2026-01-19T16:16:27.6421363Z Progress (1): 827 B
2026-01-19T16:16:27.6422117Z Progress (1): 3.0 kB
2026-01-19T16:16:27.6422789Z Progress (1): 3.6 kB
2026-01-19T16:16:27.6423533Z                     
2026-01-19T16:16:27.6424180Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-api/3.0.0-M9/surefire-extensions-api-3.0.0-M9.pom (3.6 kB at 166 kB/s)
2026-01-19T16:16:27.6458967Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/3.0.0-M9/surefire-booter-3.0.0-M9.pom
2026-01-19T16:16:27.6656276Z Progress (1): 827 B
2026-01-19T16:16:27.6657302Z Progress (1): 2.9 kB
2026-01-19T16:16:27.6659668Z Progress (1): 4.3 kB
2026-01-19T16:16:27.6661973Z                     
2026-01-19T16:16:27.6662431Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/3.0.0-M9/surefire-booter-3.0.0-M9.pom (4.3 kB at 216 kB/s)
2026-01-19T16:16:27.6684692Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-spi/3.0.0-M9/surefire-extensions-spi-3.0.0-M9.pom
2026-01-19T16:16:27.6877594Z Progress (1): 873 B
2026-01-19T16:16:27.6880430Z Progress (1): 1.8 kB
2026-01-19T16:16:27.6881346Z                     
2026-01-19T16:16:27.6882033Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-spi/3.0.0-M9/surefire-extensions-spi-3.0.0-M9.pom (1.8 kB at 95 kB/s)
2026-01-19T16:16:27.6919258Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.1.1/maven-common-artifact-filters-3.1.1.pom
2026-01-19T16:16:27.7101746Z Progress (1): 798 B
2026-01-19T16:16:27.7102222Z Progress (1): 2.3 kB
2026-01-19T16:16:27.7102637Z Progress (1): 5.7 kB
2026-01-19T16:16:27.7111180Z Progress (1): 5.8 kB
2026-01-19T16:16:27.7111671Z                     
2026-01-19T16:16:27.7112128Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.1.1/maven-common-artifact-filters-3.1.1.pom (5.8 kB at 305 kB/s)
2026-01-19T16:16:27.7158502Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/3.2.5/maven-artifact-3.2.5.pom
2026-01-19T16:16:27.7342992Z Progress (1): 843 B
2026-01-19T16:16:27.7367924Z Progress (1): 2.3 kB
2026-01-19T16:16:27.7368435Z                     
2026-01-19T16:16:27.7369067Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-artifact/3.2.5/maven-artifact-3.2.5.pom (2.3 kB at 117 kB/s)
2026-01-19T16:16:27.7376740Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/3.2.5/maven-3.2.5.pom
2026-01-19T16:16:27.7546267Z Progress (1): 754 B
2026-01-19T16:16:27.7546805Z Progress (1): 1.9 kB
2026-01-19T16:16:27.7547123Z Progress (1): 3.4 kB
2026-01-19T16:16:27.7547408Z Progress (1): 5.3 kB
2026-01-19T16:16:27.7547707Z Progress (1): 11 kB 
2026-01-19T16:16:27.7548012Z Progress (1): 15 kB
2026-01-19T16:16:27.7548318Z Progress (1): 18 kB
2026-01-19T16:16:27.7548631Z Progress (1): 21 kB
2026-01-19T16:16:27.7567137Z Progress (1): 22 kB
2026-01-19T16:16:27.7567730Z                    
2026-01-19T16:16:27.7568362Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven/3.2.5/maven-3.2.5.pom (22 kB at 1.2 MB/s)
2026-01-19T16:16:27.7578586Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/25/maven-parent-25.pom
2026-01-19T16:16:27.7770477Z Progress (1): 729 B
2026-01-19T16:16:27.7773377Z Progress (1): 2.0 kB
2026-01-19T16:16:27.7785183Z Progress (1): 6.0 kB
2026-01-19T16:16:27.7787307Z Progress (1): 10 kB 
2026-01-19T16:16:27.7788473Z Progress (1): 15 kB
2026-01-19T16:16:27.7789080Z Progress (1): 18 kB
2026-01-19T16:16:27.7789655Z Progress (1): 23 kB
2026-01-19T16:16:27.7792502Z Progress (1): 24 kB
2026-01-19T16:16:27.7792841Z Progress (1): 27 kB
2026-01-19T16:16:27.7793166Z Progress (1): 30 kB
2026-01-19T16:16:27.7793476Z Progress (1): 32 kB
2026-01-19T16:16:27.7793799Z Progress (1): 37 kB
2026-01-19T16:16:27.7794111Z Progress (1): 37 kB
2026-01-19T16:16:27.7794405Z                    
2026-01-19T16:16:27.7794832Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-parent/25/maven-parent-25.pom (37 kB at 1.8 MB/s)
2026-01-19T16:16:27.7836780Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.3.0/plexus-utils-3.3.0.pom
2026-01-19T16:16:27.8044797Z Progress (1): 800 B
2026-01-19T16:16:27.8045477Z Progress (1): 2.6 kB
2026-01-19T16:16:27.8045954Z Progress (1): 4.9 kB
2026-01-19T16:16:27.8046404Z Progress (1): 5.2 kB
2026-01-19T16:16:27.8047153Z                     
2026-01-19T16:16:27.8047715Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-utils/3.3.0/plexus-utils-3.3.0.pom (5.2 kB at 247 kB/s)
2026-01-19T16:16:27.8074285Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-core/3.2.5/maven-core-3.2.5.pom
2026-01-19T16:16:27.8249829Z Progress (1): 790 B
2026-01-19T16:16:27.8254702Z Progress (1): 2.1 kB
2026-01-19T16:16:27.8259662Z Progress (1): 5.3 kB
2026-01-19T16:16:27.8268540Z Progress (1): 8.1 kB
2026-01-19T16:16:27.8269357Z                     
2026-01-19T16:16:27.8269906Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-core/3.2.5/maven-core-3.2.5.pom (8.1 kB at 424 kB/s)
2026-01-19T16:16:27.8304254Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings/3.2.5/maven-settings-3.2.5.pom
2026-01-19T16:16:27.8456376Z Progress (1): 823 B
2026-01-19T16:16:27.8460990Z Progress (1): 2.2 kB
2026-01-19T16:16:27.8461556Z                     
2026-01-19T16:16:27.8463735Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings/3.2.5/maven-settings-3.2.5.pom (2.2 kB at 128 kB/s)
2026-01-19T16:16:27.8483054Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings-builder/3.2.5/maven-settings-builder-3.2.5.pom
2026-01-19T16:16:27.8644455Z Progress (1): 823 B
2026-01-19T16:16:27.8649370Z Progress (1): 2.6 kB
2026-01-19T16:16:27.8650559Z                     
2026-01-19T16:16:27.8652117Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-settings-builder/3.2.5/maven-settings-builder-3.2.5.pom (2.6 kB at 153 kB/s)
2026-01-19T16:16:27.8668128Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.21/plexus-interpolation-1.21.pom
2026-01-19T16:16:27.8845060Z Progress (1): 1.3 kB
2026-01-19T16:16:27.8849936Z Progress (1): 1.5 kB
2026-01-19T16:16:27.8850299Z                     
2026-01-19T16:16:27.8850768Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-interpolation/1.21/plexus-interpolation-1.21.pom (1.5 kB at 86 kB/s)
2026-01-19T16:16:27.8863420Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.3.1/plexus-components-1.3.1.pom
2026-01-19T16:16:27.9049259Z Progress (1): 1.3 kB
2026-01-19T16:16:27.9052684Z Progress (1): 3.1 kB
2026-01-19T16:16:27.9053626Z                     
2026-01-19T16:16:27.9055150Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-components/1.3.1/plexus-components-1.3.1.pom (3.1 kB at 153 kB/s)
2026-01-19T16:16:27.9072703Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/3.3.1/plexus-3.3.1.pom
2026-01-19T16:16:27.9246266Z Progress (1): 703 B
2026-01-19T16:16:27.9248802Z Progress (1): 2.5 kB
2026-01-19T16:16:27.9251394Z Progress (1): 6.0 kB
2026-01-19T16:16:27.9251768Z Progress (1): 8.6 kB
2026-01-19T16:16:27.9252072Z Progress (1): 11 kB 
2026-01-19T16:16:27.9252353Z Progress (1): 16 kB
2026-01-19T16:16:27.9252643Z Progress (1): 20 kB
2026-01-19T16:16:27.9254791Z Progress (1): 20 kB
2026-01-19T16:16:27.9255382Z                    
2026-01-19T16:16:27.9257022Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus/3.3.1/plexus-3.3.1.pom (20 kB at 1.1 MB/s)
2026-01-19T16:16:27.9274793Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/17/spice-parent-17.pom
2026-01-19T16:16:27.9459628Z Progress (1): 1.2 kB
2026-01-19T16:16:27.9460386Z Progress (1): 3.4 kB
2026-01-19T16:16:27.9460866Z Progress (1): 6.7 kB
2026-01-19T16:16:27.9461362Z Progress (1): 6.8 kB
2026-01-19T16:16:27.9461759Z                     
2026-01-19T16:16:27.9462323Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/17/spice-parent-17.pom (6.8 kB at 356 kB/s)
2026-01-19T16:16:27.9482663Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/10/forge-parent-10.pom
2026-01-19T16:16:27.9679379Z Progress (1): 730 B
2026-01-19T16:16:27.9687579Z Progress (1): 2.5 kB
2026-01-19T16:16:27.9707274Z Progress (1): 8.6 kB
2026-01-19T16:16:27.9707857Z Progress (1): 12 kB 
2026-01-19T16:16:27.9708590Z Progress (1): 14 kB
2026-01-19T16:16:27.9709059Z                    
2026-01-19T16:16:27.9709639Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/10/forge-parent-10.pom (14 kB at 646 kB/s)
2026-01-19T16:16:27.9724186Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-sec-dispatcher/1.3/plexus-sec-dispatcher-1.3.pom
2026-01-19T16:16:27.9899582Z Progress (1): 1.3 kB
2026-01-19T16:16:27.9904771Z Progress (1): 3.0 kB
2026-01-19T16:16:27.9909028Z                     
2026-01-19T16:16:27.9913085Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-sec-dispatcher/1.3/plexus-sec-dispatcher-1.3.pom (3.0 kB at 156 kB/s)
2026-01-19T16:16:27.9926217Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/12/spice-parent-12.pom
2026-01-19T16:16:28.0093630Z Progress (1): 1.2 kB
2026-01-19T16:16:28.0093987Z Progress (1): 4.2 kB
2026-01-19T16:16:28.0099076Z Progress (1): 6.8 kB
2026-01-19T16:16:28.0099714Z                     
2026-01-19T16:16:28.0101056Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/spice/spice-parent/12/spice-parent-12.pom (6.8 kB at 378 kB/s)
2026-01-19T16:16:28.0123974Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/4/forge-parent-4.pom
2026-01-19T16:16:28.0299517Z Progress (1): 1.4 kB
2026-01-19T16:16:28.0300027Z Progress (1): 5.7 kB
2026-01-19T16:16:28.0303249Z Progress (1): 8.4 kB
2026-01-19T16:16:28.0303806Z                     
2026-01-19T16:16:28.0304723Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/4/forge-parent-4.pom (8.4 kB at 442 kB/s)
2026-01-19T16:16:28.0337569Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-cipher/1.4/plexus-cipher-1.4.pom
2026-01-19T16:16:28.0548096Z Progress (1): 1.4 kB
2026-01-19T16:16:28.0548768Z Progress (1): 2.1 kB
2026-01-19T16:16:28.0549909Z                     
2026-01-19T16:16:28.0550331Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/plexus/plexus-cipher/1.4/plexus-cipher-1.4.pom (2.1 kB at 109 kB/s)
2026-01-19T16:16:28.0550900Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/3.2.5/maven-repository-metadata-3.2.5.pom
2026-01-19T16:16:28.0714910Z Progress (1): 822 B
2026-01-19T16:16:28.0718124Z Progress (1): 2.2 kB
2026-01-19T16:16:28.0719848Z                     
2026-01-19T16:16:28.0720731Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-repository-metadata/3.2.5/maven-repository-metadata-3.2.5.pom (2.2 kB at 131 kB/s)
2026-01-19T16:16:28.0757437Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-api/3.2.5/maven-plugin-api-3.2.5.pom
2026-01-19T16:16:28.0912685Z Progress (1): 816 B
2026-01-19T16:16:28.0915022Z Progress (1): 2.5 kB
2026-01-19T16:16:28.0919520Z Progress (1): 3.0 kB
2026-01-19T16:16:28.0919842Z                     
2026-01-19T16:16:28.0920281Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-plugin-api/3.2.5/maven-plugin-api-3.2.5.pom (3.0 kB at 178 kB/s)
2026-01-19T16:16:28.0952496Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.3.5/org.eclipse.sisu.plexus-0.3.5.pom
2026-01-19T16:16:28.1153839Z Progress (1): 904 B
2026-01-19T16:16:28.1157934Z Progress (1): 3.2 kB
2026-01-19T16:16:28.1158769Z Progress (1): 4.3 kB
2026-01-19T16:16:28.1159209Z                     
2026-01-19T16:16:28.1159770Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.plexus/0.3.5/org.eclipse.sisu.plexus-0.3.5.pom (4.3 kB at 204 kB/s)
2026-01-19T16:16:28.1179529Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.3.5/sisu-plexus-0.3.5.pom
2026-01-19T16:16:28.1413186Z Progress (1): 860 B
2026-01-19T16:16:28.1414716Z Progress (1): 2.8 kB
2026-01-19T16:16:28.1417265Z Progress (1): 5.2 kB
2026-01-19T16:16:28.1417849Z Progress (1): 9.8 kB
2026-01-19T16:16:28.1418596Z Progress (1): 11 kB 
2026-01-19T16:16:28.1419135Z Progress (1): 14 kB
2026-01-19T16:16:28.1419570Z                    
2026-01-19T16:16:28.1420218Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-plexus/0.3.5/sisu-plexus-0.3.5.pom (14 kB at 572 kB/s)
2026-01-19T16:16:28.1460382Z Downloading from central: https://repo.maven.apache.org/maven2/javax/annotation/javax.annotation-api/1.2/javax.annotation-api-1.2.pom
2026-01-19T16:16:28.1631696Z Progress (1): 702 B
2026-01-19T16:16:28.1632651Z Progress (1): 2.0 kB
2026-01-19T16:16:28.1635937Z Progress (1): 3.4 kB
2026-01-19T16:16:28.1636326Z Progress (1): 5.5 kB
2026-01-19T16:16:28.1636843Z Progress (1): 8.7 kB
2026-01-19T16:16:28.1637174Z Progress (1): 12 kB 
2026-01-19T16:16:28.1645450Z Progress (1): 13 kB
2026-01-19T16:16:28.1646056Z                    
2026-01-19T16:16:28.1646942Z Downloaded from central: https://repo.maven.apache.org/maven2/javax/annotation/javax.annotation-api/1.2/javax.annotation-api-1.2.pom (13 kB at 746 kB/s)
2026-01-19T16:16:28.1656043Z Downloading from central: https://repo.maven.apache.org/maven2/net/java/jvnet-parent/3/jvnet-parent-3.pom
2026-01-19T16:16:28.1819367Z Progress (1): 838 B
2026-01-19T16:16:28.1822286Z Progress (1): 2.5 kB
2026-01-19T16:16:28.1824804Z Progress (1): 4.8 kB
2026-01-19T16:16:28.1825215Z                     
2026-01-19T16:16:28.1825829Z Downloaded from central: https://repo.maven.apache.org/maven2/net/java/jvnet-parent/3/jvnet-parent-3.pom (4.8 kB at 282 kB/s)
2026-01-19T16:16:28.1841701Z Downloading from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.2/cdi-api-1.2.pom
2026-01-19T16:16:28.2028357Z Progress (1): 1.0 kB
2026-01-19T16:16:28.2028757Z Progress (1): 3.3 kB
2026-01-19T16:16:28.2029128Z Progress (1): 5.8 kB
2026-01-19T16:16:28.2031546Z Progress (1): 6.3 kB
2026-01-19T16:16:28.2034394Z                     
2026-01-19T16:16:28.2035168Z Downloaded from central: https://repo.maven.apache.org/maven2/javax/enterprise/cdi-api/1.2/cdi-api-1.2.pom (6.3 kB at 330 kB/s)
2026-01-19T16:16:28.2048379Z Downloading from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/26/weld-parent-26.pom
2026-01-19T16:16:28.2225332Z Progress (1): 1.0 kB
2026-01-19T16:16:28.2230353Z Progress (1): 2.8 kB
2026-01-19T16:16:28.2231048Z Progress (1): 6.3 kB
2026-01-19T16:16:28.2231719Z Progress (1): 11 kB 
2026-01-19T16:16:28.2233934Z Progress (1): 16 kB
2026-01-19T16:16:28.2234331Z Progress (1): 19 kB
2026-01-19T16:16:28.2234696Z Progress (1): 22 kB
2026-01-19T16:16:28.2235065Z Progress (1): 26 kB
2026-01-19T16:16:28.2235417Z Progress (1): 31 kB
2026-01-19T16:16:28.2235750Z Progress (1): 32 kB
2026-01-19T16:16:28.2236060Z                    
2026-01-19T16:16:28.2236752Z Downloaded from central: https://repo.maven.apache.org/maven2/org/jboss/weld/weld-parent/26/weld-parent-26.pom (32 kB at 1.7 MB/s)
2026-01-19T16:16:28.2256797Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.inject/0.3.5/org.eclipse.sisu.inject-0.3.5.pom
2026-01-19T16:16:28.2440301Z Progress (1): 914 B
2026-01-19T16:16:28.2448304Z Progress (1): 2.6 kB
2026-01-19T16:16:28.2448939Z                     
2026-01-19T16:16:28.2450247Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/org.eclipse.sisu.inject/0.3.5/org.eclipse.sisu.inject-0.3.5.pom (2.6 kB at 138 kB/s)
2026-01-19T16:16:28.2472416Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-inject/0.3.5/sisu-inject-0.3.5.pom
2026-01-19T16:16:28.2653461Z Progress (1): 831 B
2026-01-19T16:16:28.2653787Z Progress (1): 2.8 kB
2026-01-19T16:16:28.2654091Z Progress (1): 5.0 kB
2026-01-19T16:16:28.2654380Z Progress (1): 9.6 kB
2026-01-19T16:16:28.2654673Z Progress (1): 11 kB 
2026-01-19T16:16:28.2654973Z Progress (1): 14 kB
2026-01-19T16:16:28.2655242Z                    
2026-01-19T16:16:28.2655860Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/sisu/sisu-inject/0.3.5/sisu-inject-0.3.5.pom (14 kB at 758 kB/s)
2026-01-19T16:16:28.2702164Z Downloading from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-classworlds/2.5.2/plexus-classworlds-2.5.2.pom
2026-01-19T16:16:28.2884318Z Progress (1): 930 B
2026-01-19T16:16:28.2897527Z Progress (1): 3.0 kB
2026-01-19T16:16:28.2899988Z Progress (1): 6.0 kB
2026-01-19T16:16:28.2900318Z Progress (1): 7.3 kB
2026-01-19T16:16:28.2900599Z                     
2026-01-19T16:16:28.2901025Z Downloaded from central: https://repo.maven.apache.org/maven2/org/codehaus/plexus/plexus-classworlds/2.5.2/plexus-classworlds-2.5.2.pom (7.3 kB at 348 kB/s)
2026-01-19T16:16:28.2913809Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-model-builder/3.2.5/maven-model-builder-3.2.5.pom
2026-01-19T16:16:28.3132747Z Progress (1): 836 B
2026-01-19T16:16:28.3134218Z Progress (1): 2.7 kB
2026-01-19T16:16:28.3139159Z Progress (1): 3.0 kB
2026-01-19T16:16:28.3139504Z                     
2026-01-19T16:16:28.3140870Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-model-builder/3.2.5/maven-model-builder-3.2.5.pom (3.0 kB at 130 kB/s)
2026-01-19T16:16:28.3238277Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-aether-provider/3.2.5/maven-aether-provider-3.2.5.pom
2026-01-19T16:16:28.3427474Z Progress (1): 811 B
2026-01-19T16:16:28.3428310Z Progress (1): 3.0 kB
2026-01-19T16:16:28.3428998Z Progress (1): 4.2 kB
2026-01-19T16:16:28.3429549Z                     
2026-01-19T16:16:28.3430238Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/maven-aether-provider/3.2.5/maven-aether-provider-3.2.5.pom (4.2 kB at 236 kB/s)
2026-01-19T16:16:28.3442019Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether-api/1.0.0.v20140518/aether-api-1.0.0.v20140518.pom
2026-01-19T16:16:28.3604760Z Progress (1): 938 B
2026-01-19T16:16:28.3613297Z Progress (1): 1.9 kB
2026-01-19T16:16:28.3616422Z                     
2026-01-19T16:16:28.3617389Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether-api/1.0.0.v20140518/aether-api-1.0.0.v20140518.pom (1.9 kB at 112 kB/s)
2026-01-19T16:16:28.3640752Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether/1.0.0.v20140518/aether-1.0.0.v20140518.pom
2026-01-19T16:16:28.3830856Z Progress (1): 799 B
2026-01-19T16:16:28.3831184Z Progress (1): 3.2 kB
2026-01-19T16:16:28.3831499Z Progress (1): 5.1 kB
2026-01-19T16:16:28.3831831Z Progress (1): 9.0 kB
2026-01-19T16:16:28.3832120Z Progress (1): 12 kB 
2026-01-19T16:16:28.3832441Z Progress (1): 17 kB
2026-01-19T16:16:28.3836697Z Progress (1): 20 kB
2026-01-19T16:16:28.3837950Z Progress (1): 23 kB
2026-01-19T16:16:28.3838288Z Progress (1): 28 kB
2026-01-19T16:16:28.3838608Z Progress (1): 30 kB
2026-01-19T16:16:28.3838934Z                    
2026-01-19T16:16:28.3839377Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether/1.0.0.v20140518/aether-1.0.0.v20140518.pom (30 kB at 1.5 MB/s)
2026-01-19T16:16:28.3857591Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether-spi/1.0.0.v20140518/aether-spi-1.0.0.v20140518.pom
2026-01-19T16:16:28.4028145Z Progress (1): 934 B
2026-01-19T16:16:28.4031880Z Progress (1): 2.1 kB
2026-01-19T16:16:28.4033196Z                     
2026-01-19T16:16:28.4034691Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether-spi/1.0.0.v20140518/aether-spi-1.0.0.v20140518.pom (2.1 kB at 114 kB/s)
2026-01-19T16:16:28.4048918Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether-util/1.0.0.v20140518/aether-util-1.0.0.v20140518.pom
2026-01-19T16:16:28.4229738Z Progress (1): 932 B
2026-01-19T16:16:28.4233440Z Progress (1): 2.2 kB
2026-01-19T16:16:28.4233987Z                     
2026-01-19T16:16:28.4234677Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether-util/1.0.0.v20140518/aether-util-1.0.0.v20140518.pom (2.2 kB at 115 kB/s)
2026-01-19T16:16:28.4248975Z Downloading from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether-impl/1.0.0.v20140518/aether-impl-1.0.0.v20140518.pom
2026-01-19T16:16:28.4551465Z Progress (1): 922 B
2026-01-19T16:16:28.4554647Z Progress (1): 3.5 kB
2026-01-19T16:16:28.4556243Z                     
2026-01-19T16:16:28.4557855Z Downloaded from central: https://repo.maven.apache.org/maven2/org/eclipse/aether/aether-impl/1.0.0.v20140518/aether-impl-1.0.0.v20140518.pom (3.5 kB at 112 kB/s)
2026-01-19T16:16:28.4577251Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/sisu/sisu-guice/3.2.3/sisu-guice-3.2.3.pom
2026-01-19T16:16:28.4763487Z Progress (1): 1.3 kB
2026-01-19T16:16:28.4764129Z Progress (1): 3.8 kB
2026-01-19T16:16:28.4765097Z Progress (1): 5.9 kB
2026-01-19T16:16:28.4765668Z Progress (1): 9.5 kB
2026-01-19T16:16:28.4767972Z Progress (1): 11 kB 
2026-01-19T16:16:28.4768290Z                    
2026-01-19T16:16:28.4768708Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/sisu/sisu-guice/3.2.3/sisu-guice-3.2.3.pom (11 kB at 576 kB/s)
2026-01-19T16:16:28.4784903Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/sisu/inject/guice-parent/3.2.3/guice-parent-3.2.3.pom
2026-01-19T16:16:28.4953192Z Progress (1): 798 B
2026-01-19T16:16:28.4958470Z Progress (1): 2.7 kB
2026-01-19T16:16:28.4962556Z Progress (1): 5.1 kB
2026-01-19T16:16:28.4967695Z Progress (1): 7.6 kB
2026-01-19T16:16:28.4972741Z Progress (1): 10 kB 
2026-01-19T16:16:28.4974777Z Progress (1): 13 kB
2026-01-19T16:16:28.4975339Z Progress (1): 13 kB
2026-01-19T16:16:28.4976836Z                    
2026-01-19T16:16:28.4977164Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/sisu/inject/guice-parent/3.2.3/guice-parent-3.2.3.pom (13 kB at 793 kB/s)
2026-01-19T16:16:28.4977476Z Downloading from central: https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/38/forge-parent-38.pom
2026-01-19T16:16:28.5148651Z Progress (1): 800 B
2026-01-19T16:16:28.5149084Z Progress (1): 2.5 kB
2026-01-19T16:16:28.5149526Z Progress (1): 5.0 kB
2026-01-19T16:16:28.5149978Z Progress (1): 8.7 kB
2026-01-19T16:16:28.5150401Z Progress (1): 12 kB 
2026-01-19T16:16:28.5150802Z Progress (1): 16 kB
2026-01-19T16:16:28.5153800Z Progress (1): 19 kB
2026-01-19T16:16:28.5155217Z                    
2026-01-19T16:16:28.5155673Z Downloaded from central: https://repo.maven.apache.org/maven2/org/sonatype/forge/forge-parent/38/forge-parent-38.pom (19 kB at 1.0 MB/s)
2026-01-19T16:16:28.5176344Z Downloading from central: https://repo.maven.apache.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.pom
2026-01-19T16:16:28.5339340Z Progress (1): 363 B
2026-01-19T16:16:28.5339859Z                    
2026-01-19T16:16:28.5342593Z Downloaded from central: https://repo.maven.apache.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.pom (363 B at 21 kB/s)
2026-01-19T16:16:28.5359507Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/16.0.1/guava-16.0.1.pom
2026-01-19T16:16:28.5514214Z Progress (1): 955 B
2026-01-19T16:16:28.5518924Z Progress (1): 2.8 kB
2026-01-19T16:16:28.5524876Z Progress (1): 5.2 kB
2026-01-19T16:16:28.5527440Z Progress (1): 6.1 kB
2026-01-19T16:16:28.5529168Z                     
2026-01-19T16:16:28.5562714Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava/16.0.1/guava-16.0.1.pom (6.1 kB at 359 kB/s)
2026-01-19T16:16:28.5563414Z Downloading from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/16.0.1/guava-parent-16.0.1.pom
2026-01-19T16:16:28.5714958Z Progress (1): 1.1 kB
2026-01-19T16:16:28.5719087Z Progress (1): 2.9 kB
2026-01-19T16:16:28.5720657Z Progress (1): 6.3 kB
2026-01-19T16:16:28.5727298Z Progress (1): 7.3 kB
2026-01-19T16:16:28.5729068Z                     
2026-01-19T16:16:28.5738143Z Downloaded from central: https://repo.maven.apache.org/maven2/com/google/guava/guava-parent/16.0.1/guava-parent-16.0.1.pom (7.3 kB at 408 kB/s)
2026-01-19T16:16:28.5796225Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/3.0.0-M9/maven-surefire-common-3.0.0-M9.jar
2026-01-19T16:16:28.5826441Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/3.0.0-M9/surefire-api-3.0.0-M9.jar
2026-01-19T16:16:28.5827422Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-logger-api/3.0.0-M9/surefire-logger-api-3.0.0-M9.jar
2026-01-19T16:16:28.5828054Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-api/3.0.0-M9/surefire-extensions-api-3.0.0-M9.jar
2026-01-19T16:16:28.5828641Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/3.0.0-M9/surefire-booter-3.0.0-M9.jar
2026-01-19T16:16:28.5970676Z Progress (1): 7.7/305 kB
2026-01-19T16:16:28.5971075Z Progress (1): 16/305 kB 
2026-01-19T16:16:28.5975249Z Progress (1): 29/305 kB
2026-01-19T16:16:28.5980936Z Progress (1): 45/305 kB
2026-01-19T16:16:28.5981262Z Progress (1): 61/305 kB
2026-01-19T16:16:28.5981550Z Progress (1): 78/305 kB
2026-01-19T16:16:28.5981850Z Progress (1): 94/305 kB
2026-01-19T16:16:28.6009235Z Progress (1): 111/305 kB
2026-01-19T16:16:28.6009793Z Progress (1): 115/305 kB
2026-01-19T16:16:28.6010227Z Progress (1): 131/305 kB
2026-01-19T16:16:28.6011179Z Progress (1): 147/305 kB
2026-01-19T16:16:28.6011609Z Progress (1): 164/305 kB
2026-01-19T16:16:28.6012021Z Progress (1): 180/305 kB
2026-01-19T16:16:28.6012412Z Progress (1): 197/305 kB
2026-01-19T16:16:28.6012810Z Progress (1): 213/305 kB
2026-01-19T16:16:28.6013204Z Progress (1): 229/305 kB
2026-01-19T16:16:28.6013611Z Progress (1): 246/305 kB
2026-01-19T16:16:28.6014005Z Progress (1): 262/305 kB
2026-01-19T16:16:28.6014424Z Progress (1): 279/305 kB
2026-01-19T16:16:28.6014821Z Progress (1): 295/305 kB
2026-01-19T16:16:28.6015288Z Progress (1): 305 kB    
2026-01-19T16:16:28.6015734Z                     
2026-01-19T16:16:28.6016325Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/maven-surefire-common/3.0.0-M9/maven-surefire-common-3.0.0-M9.jar (305 kB at 15 MB/s)
2026-01-19T16:16:28.6017302Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-spi/3.0.0-M9/surefire-extensions-spi-3.0.0-M9.jar
2026-01-19T16:16:28.6050694Z Progress (1): 7.7/25 kB
2026-01-19T16:16:28.6051326Z Progress (1): 16/25 kB 
2026-01-19T16:16:28.6051871Z Progress (1): 25 kB   
2026-01-19T16:16:28.6056910Z                    
2026-01-19T16:16:28.6057659Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-api/3.0.0-M9/surefire-extensions-api-3.0.0-M9.jar (25 kB at 1.1 MB/s)
2026-01-19T16:16:28.6058430Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.1.1/maven-common-artifact-filters-3.1.1.jar
2026-01-19T16:16:28.6098616Z Progress (1): 7.7/14 kB
2026-01-19T16:16:28.6103971Z Progress (1): 14 kB    
2026-01-19T16:16:28.6138552Z Progress (2): 14 kB | 7.7/117 kB
2026-01-19T16:16:28.6139605Z Progress (2): 14 kB | 16/117 kB 
2026-01-19T16:16:28.6140449Z Progress (2): 14 kB | 32/117 kB
2026-01-19T16:16:28.6140919Z Progress (2): 14 kB | 49/117 kB
2026-01-19T16:16:28.6141418Z Progress (2): 14 kB | 65/117 kB
2026-01-19T16:16:28.6141856Z Progress (2): 14 kB | 81/117 kB
2026-01-19T16:16:28.6142267Z Progress (2): 14 kB | 98/117 kB
2026-01-19T16:16:28.6142706Z Progress (2): 14 kB | 114/117 kB
2026-01-19T16:16:28.6143166Z Progress (2): 14 kB | 117 kB    
2026-01-19T16:16:28.6143539Z                             
2026-01-19T16:16:28.6144107Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-logger-api/3.0.0-M9/surefire-logger-api-3.0.0-M9.jar (14 kB at 437 kB/s)
2026-01-19T16:16:28.6145095Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-shared-utils/3.0.0-M9/surefire-shared-utils-3.0.0-M9.jar
2026-01-19T16:16:28.6145877Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-booter/3.0.0-M9/surefire-booter-3.0.0-M9.jar (117 kB at 3.8 MB/s)
2026-01-19T16:16:28.6146680Z Progress (1): 7.7/170 kB
2026-01-19T16:16:28.6147168Z Progress (1): 12/170 kB 
2026-01-19T16:16:28.6147582Z Progress (1): 29/170 kB
2026-01-19T16:16:28.6147992Z Progress (1): 45/170 kB
2026-01-19T16:16:28.6148498Z Progress (1): 61/170 kB
2026-01-19T16:16:28.6148921Z Progress (1): 78/170 kB
2026-01-19T16:16:28.6149348Z Progress (1): 94/170 kB
2026-01-19T16:16:28.6149766Z Progress (1): 111/170 kB
2026-01-19T16:16:28.6150187Z Progress (1): 127/170 kB
2026-01-19T16:16:28.6169099Z Progress (1): 143/170 kB
2026-01-19T16:16:28.6179214Z Progress (1): 160/170 kB
2026-01-19T16:16:28.6181116Z Progress (1): 170 kB    
2026-01-19T16:16:28.6182844Z                     
2026-01-19T16:16:28.6184802Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-api/3.0.0-M9/surefire-api-3.0.0-M9.jar (170 kB at 4.5 MB/s)
2026-01-19T16:16:28.6217682Z Progress (1): 7.7/8.1 kB
2026-01-19T16:16:28.6221084Z Progress (1): 8.1 kB    
2026-01-19T16:16:28.6222701Z                     
2026-01-19T16:16:28.6224778Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-extensions-spi/3.0.0-M9/surefire-extensions-spi-3.0.0-M9.jar (8.1 kB at 207 kB/s)
2026-01-19T16:16:28.6239189Z Progress (1): 7.7/61 kB
2026-01-19T16:16:28.6243075Z Progress (1): 16/61 kB 
2026-01-19T16:16:28.6243383Z Progress (1): 32/61 kB
2026-01-19T16:16:28.6243690Z Progress (1): 49/61 kB
2026-01-19T16:16:28.6246765Z Progress (1): 61 kB   
2026-01-19T16:16:28.6247071Z                    
2026-01-19T16:16:28.6247515Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/shared/maven-common-artifact-filters/3.1.1/maven-common-artifact-filters-3.1.1.jar (61 kB at 1.5 MB/s)
2026-01-19T16:16:28.6374275Z Progress (1): 0/2.1 MB
2026-01-19T16:16:28.6375044Z Progress (1): 0/2.1 MB
2026-01-19T16:16:28.6376003Z Progress (1): 0/2.1 MB
2026-01-19T16:16:28.6377364Z Progress (1): 0/2.1 MB
2026-01-19T16:16:28.6377711Z Progress (1): 0.1/2.1 MB
2026-01-19T16:16:28.6378002Z Progress (1): 0.1/2.1 MB
2026-01-19T16:16:28.6378284Z Progress (1): 0.1/2.1 MB
2026-01-19T16:16:28.6378581Z Progress (1): 0.1/2.1 MB
2026-01-19T16:16:28.6384024Z Progress (1): 0.1/2.1 MB
2026-01-19T16:16:28.6385185Z Progress (1): 0.1/2.1 MB
2026-01-19T16:16:28.6386416Z Progress (1): 0.2/2.1 MB
2026-01-19T16:16:28.6387867Z Progress (1): 0.2/2.1 MB
2026-01-19T16:16:28.6389398Z Progress (1): 0.2/2.1 MB
2026-01-19T16:16:28.6389940Z Progress (1): 0.2/2.1 MB
2026-01-19T16:16:28.6392269Z Progress (1): 0.2/2.1 MB
2026-01-19T16:16:28.6392791Z Progress (1): 0.2/2.1 MB
2026-01-19T16:16:28.6393123Z Progress (1): 0.3/2.1 MB
2026-01-19T16:16:28.6393418Z Progress (1): 0.3/2.1 MB
2026-01-19T16:16:28.6394122Z Progress (1): 0.3/2.1 MB
2026-01-19T16:16:28.6394766Z Progress (1): 0.3/2.1 MB
2026-01-19T16:16:28.6395039Z Progress (1): 0.3/2.1 MB
2026-01-19T16:16:28.6397809Z Progress (1): 0.3/2.1 MB
2026-01-19T16:16:28.6400005Z Progress (1): 0.4/2.1 MB
2026-01-19T16:16:28.6401303Z Progress (1): 0.4/2.1 MB
2026-01-19T16:16:28.6401889Z Progress (1): 0.4/2.1 MB
2026-01-19T16:16:28.6402479Z Progress (1): 0.4/2.1 MB
2026-01-19T16:16:28.6402931Z Progress (1): 0.4/2.1 MB
2026-01-19T16:16:28.6403367Z Progress (1): 0.4/2.1 MB
2026-01-19T16:16:28.6403795Z Progress (1): 0.5/2.1 MB
2026-01-19T16:16:28.6415445Z Progress (1): 0.5/2.1 MB
2026-01-19T16:16:28.6415995Z Progress (1): 0.5/2.1 MB
2026-01-19T16:16:28.6417336Z Progress (1): 0.5/2.1 MB
2026-01-19T16:16:28.6417899Z Progress (1): 0.5/2.1 MB
2026-01-19T16:16:28.6421733Z Progress (1): 0.5/2.1 MB
2026-01-19T16:16:28.6422612Z Progress (1): 0.6/2.1 MB
2026-01-19T16:16:28.6427662Z Progress (1): 0.6/2.1 MB
2026-01-19T16:16:28.6430345Z Progress (1): 0.6/2.1 MB
2026-01-19T16:16:28.6430694Z Progress (1): 0.6/2.1 MB
2026-01-19T16:16:28.6431016Z Progress (1): 0.6/2.1 MB
2026-01-19T16:16:28.6431316Z Progress (1): 0.6/2.1 MB
2026-01-19T16:16:28.6431597Z Progress (1): 0.7/2.1 MB
2026-01-19T16:16:28.6431893Z Progress (1): 0.7/2.1 MB
2026-01-19T16:16:28.6432415Z Progress (1): 0.7/2.1 MB
2026-01-19T16:16:28.6432721Z Progress (1): 0.7/2.1 MB
2026-01-19T16:16:28.6433026Z Progress (1): 0.7/2.1 MB
2026-01-19T16:16:28.6435285Z Progress (1): 0.7/2.1 MB
2026-01-19T16:16:28.6437982Z Progress (1): 0.8/2.1 MB
2026-01-19T16:16:28.6438723Z Progress (1): 0.8/2.1 MB
2026-01-19T16:16:28.6439662Z Progress (1): 0.8/2.1 MB
2026-01-19T16:16:28.6441347Z Progress (1): 0.8/2.1 MB
2026-01-19T16:16:28.6442798Z Progress (1): 0.8/2.1 MB
2026-01-19T16:16:28.6443713Z Progress (1): 0.8/2.1 MB
2026-01-19T16:16:28.6445233Z Progress (1): 0.9/2.1 MB
2026-01-19T16:16:28.6446178Z Progress (1): 0.9/2.1 MB
2026-01-19T16:16:28.6447917Z Progress (1): 0.9/2.1 MB
2026-01-19T16:16:28.6448822Z Progress (1): 0.9/2.1 MB
2026-01-19T16:16:28.6450054Z Progress (1): 0.9/2.1 MB
2026-01-19T16:16:28.6451192Z Progress (1): 0.9/2.1 MB
2026-01-19T16:16:28.6452886Z Progress (1): 0.9/2.1 MB
2026-01-19T16:16:28.6453504Z Progress (1): 1.0/2.1 MB
2026-01-19T16:16:28.6454097Z Progress (1): 1.0/2.1 MB
2026-01-19T16:16:28.6454599Z Progress (1): 1.0/2.1 MB
2026-01-19T16:16:28.6478881Z Progress (1): 1.0/2.1 MB
2026-01-19T16:16:28.6479867Z Progress (1): 1.0/2.1 MB
2026-01-19T16:16:28.6481380Z Progress (1): 1.0/2.1 MB
2026-01-19T16:16:28.6481710Z Progress (1): 1.1/2.1 MB
2026-01-19T16:16:28.6482008Z Progress (1): 1.1/2.1 MB
2026-01-19T16:16:28.6482320Z Progress (1): 1.1/2.1 MB
2026-01-19T16:16:28.6482627Z Progress (1): 1.1/2.1 MB
2026-01-19T16:16:28.6482940Z Progress (1): 1.1/2.1 MB
2026-01-19T16:16:28.6483246Z Progress (1): 1.1/2.1 MB
2026-01-19T16:16:28.6483842Z Progress (1): 1.2/2.1 MB
2026-01-19T16:16:28.6484173Z Progress (1): 1.2/2.1 MB
2026-01-19T16:16:28.6484494Z Progress (1): 1.2/2.1 MB
2026-01-19T16:16:28.6487375Z Progress (1): 1.2/2.1 MB
2026-01-19T16:16:28.6491075Z Progress (1): 1.2/2.1 MB
2026-01-19T16:16:28.6496921Z Progress (1): 1.2/2.1 MB
2026-01-19T16:16:28.6502458Z Progress (1): 1.3/2.1 MB
2026-01-19T16:16:28.6507609Z Progress (1): 1.3/2.1 MB
2026-01-19T16:16:28.6512948Z Progress (1): 1.3/2.1 MB
2026-01-19T16:16:28.6518247Z Progress (1): 1.3/2.1 MB
2026-01-19T16:16:28.6522387Z Progress (1): 1.3/2.1 MB
2026-01-19T16:16:28.6527193Z Progress (1): 1.3/2.1 MB
2026-01-19T16:16:28.6549125Z Progress (1): 1.4/2.1 MB
2026-01-19T16:16:28.6549607Z Progress (1): 1.4/2.1 MB
2026-01-19T16:16:28.6549904Z Progress (1): 1.4/2.1 MB
2026-01-19T16:16:28.6550227Z Progress (1): 1.4/2.1 MB
2026-01-19T16:16:28.6550550Z Progress (1): 1.4/2.1 MB
2026-01-19T16:16:28.6550876Z Progress (1): 1.4/2.1 MB
2026-01-19T16:16:28.6551176Z Progress (1): 1.5/2.1 MB
2026-01-19T16:16:28.6551471Z Progress (1): 1.5/2.1 MB
2026-01-19T16:16:28.6551758Z Progress (1): 1.5/2.1 MB
2026-01-19T16:16:28.6552090Z Progress (1): 1.5/2.1 MB
2026-01-19T16:16:28.6552402Z Progress (1): 1.5/2.1 MB
2026-01-19T16:16:28.6552693Z Progress (1): 1.5/2.1 MB
2026-01-19T16:16:28.6552975Z Progress (1): 1.6/2.1 MB
2026-01-19T16:16:28.6553274Z Progress (1): 1.6/2.1 MB
2026-01-19T16:16:28.6553609Z Progress (1): 1.6/2.1 MB
2026-01-19T16:16:28.6554082Z Progress (1): 1.6/2.1 MB
2026-01-19T16:16:28.6554408Z Progress (1): 1.6/2.1 MB
2026-01-19T16:16:28.6554695Z Progress (1): 1.6/2.1 MB
2026-01-19T16:16:28.6557374Z Progress (1): 1.7/2.1 MB
2026-01-19T16:16:28.6560530Z Progress (1): 1.7/2.1 MB
2026-01-19T16:16:28.6563541Z Progress (1): 1.7/2.1 MB
2026-01-19T16:16:28.6566821Z Progress (1): 1.7/2.1 MB
2026-01-19T16:16:28.6569902Z Progress (1): 1.7/2.1 MB
2026-01-19T16:16:28.6588897Z Progress (1): 1.7/2.1 MB
2026-01-19T16:16:28.6589420Z Progress (1): 1.8/2.1 MB
2026-01-19T16:16:28.6589724Z Progress (1): 1.8/2.1 MB
2026-01-19T16:16:28.6590020Z Progress (1): 1.8/2.1 MB
2026-01-19T16:16:28.6590328Z Progress (1): 1.8/2.1 MB
2026-01-19T16:16:28.6590770Z Progress (1): 1.8/2.1 MB
2026-01-19T16:16:28.6591093Z Progress (1): 1.8/2.1 MB
2026-01-19T16:16:28.6591428Z Progress (1): 1.9/2.1 MB
2026-01-19T16:16:28.6591735Z Progress (1): 1.9/2.1 MB
2026-01-19T16:16:28.6592033Z Progress (1): 1.9/2.1 MB
2026-01-19T16:16:28.6592323Z Progress (1): 1.9/2.1 MB
2026-01-19T16:16:28.6592639Z Progress (1): 1.9/2.1 MB
2026-01-19T16:16:28.6592956Z Progress (1): 1.9/2.1 MB
2026-01-19T16:16:28.6593265Z Progress (1): 1.9/2.1 MB
2026-01-19T16:16:28.6593566Z Progress (1): 2.0/2.1 MB
2026-01-19T16:16:28.6607142Z Progress (1): 2.0/2.1 MB
2026-01-19T16:16:28.6607495Z Progress (1): 2.0/2.1 MB
2026-01-19T16:16:28.6607799Z Progress (1): 2.0/2.1 MB
2026-01-19T16:16:28.6608086Z Progress (1): 2.0/2.1 MB
2026-01-19T16:16:28.6608362Z Progress (1): 2.0/2.1 MB
2026-01-19T16:16:28.6608651Z Progress (1): 2.1/2.1 MB
2026-01-19T16:16:28.6608971Z Progress (1): 2.1/2.1 MB
2026-01-19T16:16:28.6609634Z Progress (1): 2.1/2.1 MB
2026-01-19T16:16:28.6612823Z Progress (1): 2.1/2.1 MB
2026-01-19T16:16:28.6615931Z Progress (1): 2.1/2.1 MB
2026-01-19T16:16:28.6621623Z Progress (1): 2.1 MB    
2026-01-19T16:16:28.6623826Z                     
2026-01-19T16:16:28.6624884Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-shared-utils/3.0.0-M9/surefire-shared-utils-3.0.0-M9.jar (2.1 MB at 27 MB/s)
2026-01-19T16:16:28.7971125Z [INFO] Using auto detected provider org.apache.maven.surefire.testng.TestNGProvider
2026-01-19T16:16:28.8902898Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-testng/3.0.0-M9/surefire-testng-3.0.0-M9.jar
2026-01-19T16:16:28.9154934Z Progress (1): 7.7/47 kB
2026-01-19T16:16:28.9160670Z Progress (1): 12/47 kB 
2026-01-19T16:16:28.9161007Z Progress (1): 29/47 kB
2026-01-19T16:16:28.9161325Z Progress (1): 45/47 kB
2026-01-19T16:16:28.9161627Z Progress (1): 47 kB   
2026-01-19T16:16:28.9161922Z                    
2026-01-19T16:16:28.9162351Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-testng/3.0.0-M9/surefire-testng-3.0.0-M9.jar (47 kB at 1.8 MB/s)
2026-01-19T16:16:28.9181518Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-testng/3.0.0-M9/surefire-testng-3.0.0-M9.pom
2026-01-19T16:16:28.9410453Z Progress (1): 854 B
2026-01-19T16:16:28.9414523Z Progress (1): 3.4 kB
2026-01-19T16:16:28.9421037Z Progress (1): 4.0 kB
2026-01-19T16:16:28.9421363Z                     
2026-01-19T16:16:28.9423100Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-testng/3.0.0-M9/surefire-testng-3.0.0-M9.pom (4.0 kB at 166 kB/s)
2026-01-19T16:16:28.9441227Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-providers/3.0.0-M9/surefire-providers-3.0.0-M9.pom
2026-01-19T16:16:28.9664968Z Progress (1): 844 B
2026-01-19T16:16:28.9670389Z Progress (1): 2.5 kB
2026-01-19T16:16:28.9672124Z                     
2026-01-19T16:16:28.9672875Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-providers/3.0.0-M9/surefire-providers-3.0.0-M9.pom (2.5 kB at 110 kB/s)
2026-01-19T16:16:28.9852456Z Downloading from central: https://repo.maven.apache.org/maven2/junit/junit/3.8.2/junit-3.8.2.pom
2026-01-19T16:16:29.0049464Z Progress (1): 747 B
2026-01-19T16:16:29.0050062Z                    
2026-01-19T16:16:29.0067346Z Downloaded from central: https://repo.maven.apache.org/maven2/junit/junit/3.8.2/junit-3.8.2.pom (747 B at 37 kB/s)
2026-01-19T16:16:29.0074261Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-java5/3.0.0-M9/common-java5-3.0.0-M9.pom
2026-01-19T16:16:29.0313657Z Progress (1): 872 B
2026-01-19T16:16:29.0317659Z Progress (1): 2.6 kB
2026-01-19T16:16:29.0321611Z Progress (1): 2.7 kB
2026-01-19T16:16:29.0335853Z                     
2026-01-19T16:16:29.0339387Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-java5/3.0.0-M9/common-java5-3.0.0-M9.pom (2.7 kB at 117 kB/s)
2026-01-19T16:16:29.0438656Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-testng-utils/3.0.0-M9/surefire-testng-utils-3.0.0-M9.pom
2026-01-19T16:16:29.0638290Z Progress (1): 858 B
2026-01-19T16:16:29.0638730Z Progress (1): 2.8 kB
2026-01-19T16:16:29.0643693Z Progress (1): 3.0 kB
2026-01-19T16:16:29.0644038Z                     
2026-01-19T16:16:29.0645852Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-testng-utils/3.0.0-M9/surefire-testng-utils-3.0.0-M9.pom (3.0 kB at 139 kB/s)
2026-01-19T16:16:29.0777540Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-grouper/3.0.0-M9/surefire-grouper-3.0.0-M9.pom
2026-01-19T16:16:29.1018030Z Progress (1): 844 B
2026-01-19T16:16:29.1018765Z Progress (1): 2.9 kB
2026-01-19T16:16:29.1019286Z Progress (1): 3.3 kB
2026-01-19T16:16:29.1019594Z                     
2026-01-19T16:16:29.1020023Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-grouper/3.0.0-M9/surefire-grouper-3.0.0-M9.pom (3.3 kB at 134 kB/s)
2026-01-19T16:16:29.1114701Z Downloading from central: https://repo.maven.apache.org/maven2/org/testng/testng/5.10/testng-5.10.pom
2026-01-19T16:16:29.1341498Z Progress (1): 1.0 kB
2026-01-19T16:16:29.1349793Z Progress (1): 2.1 kB
2026-01-19T16:16:29.1353630Z                     
2026-01-19T16:16:29.1354324Z Downloaded from central: https://repo.maven.apache.org/maven2/org/testng/testng/5.10/testng-5.10.pom (2.1 kB at 92 kB/s)
2026-01-19T16:16:29.1379938Z Downloading from central: https://repo.maven.apache.org/maven2/junit/junit/4.13.2/junit-4.13.2.pom
2026-01-19T16:16:29.1595096Z Progress (1): 1.0 kB
2026-01-19T16:16:29.1595779Z Progress (1): 3.3 kB
2026-01-19T16:16:29.1596422Z Progress (1): 5.1 kB
2026-01-19T16:16:29.1597244Z Progress (1): 7.2 kB
2026-01-19T16:16:29.1597545Z Progress (1): 9.8 kB
2026-01-19T16:16:29.1597851Z Progress (1): 13 kB 
2026-01-19T16:16:29.1598144Z Progress (1): 16 kB
2026-01-19T16:16:29.1598427Z Progress (1): 21 kB
2026-01-19T16:16:29.1598718Z Progress (1): 25 kB
2026-01-19T16:16:29.1599003Z Progress (1): 27 kB
2026-01-19T16:16:29.1599297Z                    
2026-01-19T16:16:29.1599668Z Downloaded from central: https://repo.maven.apache.org/maven2/junit/junit/4.13.2/junit-4.13.2.pom (27 kB at 1.2 MB/s)
2026-01-19T16:16:29.1657509Z Downloading from central: https://repo.maven.apache.org/maven2/org/mockito/mockito-core/2.28.2/mockito-core-2.28.2.pom
2026-01-19T16:16:29.1900883Z Progress (1): 1.2 kB
2026-01-19T16:16:29.1910878Z Progress (1): 3.8 kB
2026-01-19T16:16:29.1924181Z Progress (1): 7.4 kB
2026-01-19T16:16:29.1924484Z Progress (1): 11 kB 
2026-01-19T16:16:29.1924767Z Progress (1): 15 kB
2026-01-19T16:16:29.1925054Z Progress (1): 18 kB
2026-01-19T16:16:29.1925328Z Progress (1): 20 kB
2026-01-19T16:16:29.1925592Z                    
2026-01-19T16:16:29.1925985Z Downloaded from central: https://repo.maven.apache.org/maven2/org/mockito/mockito-core/2.28.2/mockito-core-2.28.2.pom (20 kB at 773 kB/s)
2026-01-19T16:16:29.1952418Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.9.10/byte-buddy-1.9.10.pom
2026-01-19T16:16:29.2162242Z Progress (1): 1.0 kB
2026-01-19T16:16:29.2164469Z Progress (1): 4.1 kB
2026-01-19T16:16:29.2165541Z Progress (1): 8.0 kB
2026-01-19T16:16:29.2168166Z Progress (1): 10 kB 
2026-01-19T16:16:29.2169393Z                    
2026-01-19T16:16:29.2170198Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.9.10/byte-buddy-1.9.10.pom (10 kB at 469 kB/s)
2026-01-19T16:16:29.2196110Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.9.10/byte-buddy-parent-1.9.10.pom
2026-01-19T16:16:29.2414077Z Progress (1): 841 B
2026-01-19T16:16:29.2417941Z Progress (1): 2.0 kB
2026-01-19T16:16:29.2418658Z Progress (1): 4.3 kB
2026-01-19T16:16:29.2421473Z Progress (1): 6.3 kB
2026-01-19T16:16:29.2422393Z Progress (1): 8.6 kB
2026-01-19T16:16:29.2423077Z Progress (1): 12 kB 
2026-01-19T16:16:29.2423758Z Progress (1): 16 kB
2026-01-19T16:16:29.2425200Z Progress (1): 21 kB
2026-01-19T16:16:29.2425687Z Progress (1): 28 kB
2026-01-19T16:16:29.2426299Z Progress (1): 34 kB
2026-01-19T16:16:29.2427102Z Progress (1): 36 kB
2026-01-19T16:16:29.2427402Z                    
2026-01-19T16:16:29.2427809Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.9.10/byte-buddy-parent-1.9.10.pom (36 kB at 1.6 MB/s)
2026-01-19T16:16:29.2487440Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-agent/1.9.10/byte-buddy-agent-1.9.10.pom
2026-01-19T16:16:29.2728329Z Progress (1): 1.1 kB
2026-01-19T16:16:29.2728961Z Progress (1): 3.5 kB
2026-01-19T16:16:29.2735496Z Progress (1): 6.0 kB
2026-01-19T16:16:29.2738582Z                     
2026-01-19T16:16:29.2739663Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-agent/1.9.10/byte-buddy-agent-1.9.10.pom (6.0 kB at 241 kB/s)
2026-01-19T16:16:29.2784943Z Downloading from central: https://repo.maven.apache.org/maven2/org/objenesis/objenesis/2.6/objenesis-2.6.pom
2026-01-19T16:16:29.3047530Z Progress (1): 1.3 kB
2026-01-19T16:16:29.3049013Z Progress (1): 2.8 kB
2026-01-19T16:16:29.3049310Z                     
2026-01-19T16:16:29.3049698Z Downloaded from central: https://repo.maven.apache.org/maven2/org/objenesis/objenesis/2.6/objenesis-2.6.pom (2.8 kB at 103 kB/s)
2026-01-19T16:16:29.3068136Z Downloading from central: https://repo.maven.apache.org/maven2/org/objenesis/objenesis-parent/2.6/objenesis-parent-2.6.pom
2026-01-19T16:16:29.3298077Z Progress (1): 950 B
2026-01-19T16:16:29.3307878Z Progress (1): 3.0 kB
2026-01-19T16:16:29.3308684Z Progress (1): 4.8 kB
2026-01-19T16:16:29.3309609Z Progress (1): 8.4 kB
2026-01-19T16:16:29.3310492Z Progress (1): 12 kB 
2026-01-19T16:16:29.3310982Z Progress (1): 16 kB
2026-01-19T16:16:29.3311731Z Progress (1): 17 kB
2026-01-19T16:16:29.3313701Z                    
2026-01-19T16:16:29.3314292Z Downloaded from central: https://repo.maven.apache.org/maven2/org/objenesis/objenesis-parent/2.6/objenesis-parent-2.6.pom (17 kB at 688 kB/s)
2026-01-19T16:16:29.3383747Z Downloading from central: https://repo.maven.apache.org/maven2/org/powermock/powermock-reflect/2.0.9/powermock-reflect-2.0.9.pom
2026-01-19T16:16:29.3647333Z Progress (1): 1.3 kB
2026-01-19T16:16:29.3657237Z Progress (1): 4.9 kB
2026-01-19T16:16:29.3657828Z Progress (1): 7.8 kB
2026-01-19T16:16:29.3658440Z Progress (1): 7.9 kB
2026-01-19T16:16:29.3658900Z                     
2026-01-19T16:16:29.3659323Z Downloaded from central: https://repo.maven.apache.org/maven2/org/powermock/powermock-reflect/2.0.9/powermock-reflect-2.0.9.pom (7.9 kB at 303 kB/s)
2026-01-19T16:16:29.3666058Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.10.14/byte-buddy-1.10.14.pom
2026-01-19T16:16:29.3895308Z Progress (1): 980 B
2026-01-19T16:16:29.3901494Z Progress (1): 3.9 kB
2026-01-19T16:16:29.3901866Z Progress (1): 7.4 kB
2026-01-19T16:16:29.3902211Z Progress (1): 11 kB 
2026-01-19T16:16:29.3902534Z                    
2026-01-19T16:16:29.3902998Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.10.14/byte-buddy-1.10.14.pom (11 kB at 480 kB/s)
2026-01-19T16:16:29.3914003Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.10.14/byte-buddy-parent-1.10.14.pom
2026-01-19T16:16:29.4184168Z Progress (1): 843 B
2026-01-19T16:16:29.4186284Z Progress (1): 2.1 kB
2026-01-19T16:16:29.4186899Z Progress (1): 4.1 kB
2026-01-19T16:16:29.4187321Z Progress (1): 6.2 kB
2026-01-19T16:16:29.4187698Z Progress (1): 8.4 kB
2026-01-19T16:16:29.4188069Z Progress (1): 11 kB 
2026-01-19T16:16:29.4191317Z Progress (1): 15 kB
2026-01-19T16:16:29.4192517Z Progress (1): 19 kB
2026-01-19T16:16:29.4193864Z Progress (1): 31 kB
2026-01-19T16:16:29.4194240Z Progress (1): 36 kB
2026-01-19T16:16:29.4194773Z Progress (1): 41 kB
2026-01-19T16:16:29.4195112Z                    
2026-01-19T16:16:29.4195584Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.10.14/byte-buddy-parent-1.10.14.pom (41 kB at 1.5 MB/s)
2026-01-19T16:16:29.4248073Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-agent/1.10.14/byte-buddy-agent-1.10.14.pom
2026-01-19T16:16:29.4446078Z Progress (1): 1.1 kB
2026-01-19T16:16:29.4447161Z Progress (1): 3.6 kB
2026-01-19T16:16:29.4447790Z Progress (1): 6.5 kB
2026-01-19T16:16:29.4450110Z Progress (1): 9.6 kB
2026-01-19T16:16:29.4451347Z                     
2026-01-19T16:16:29.4452045Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-agent/1.10.14/byte-buddy-agent-1.10.14.pom (9.6 kB at 478 kB/s)
2026-01-19T16:16:29.4495832Z Downloading from central: https://repo.maven.apache.org/maven2/org/hamcrest/hamcrest-library/1.3/hamcrest-library-1.3.pom
2026-01-19T16:16:29.4697737Z Progress (1): 820 B
2026-01-19T16:16:29.4698451Z                    
2026-01-19T16:16:29.4699207Z Downloaded from central: https://repo.maven.apache.org/maven2/org/hamcrest/hamcrest-library/1.3/hamcrest-library-1.3.pom (820 B at 39 kB/s)
2026-01-19T16:16:29.4708738Z Downloading from central: https://repo.maven.apache.org/maven2/org/hamcrest/hamcrest-parent/1.3/hamcrest-parent-1.3.pom
2026-01-19T16:16:29.4929703Z Progress (1): 1.1 kB
2026-01-19T16:16:29.4949332Z Progress (1): 2.0 kB
2026-01-19T16:16:29.4951698Z                     
2026-01-19T16:16:29.4953354Z Downloaded from central: https://repo.maven.apache.org/maven2/org/hamcrest/hamcrest-parent/1.3/hamcrest-parent-1.3.pom (2.0 kB at 86 kB/s)
2026-01-19T16:16:29.4961598Z Downloading from central: https://repo.maven.apache.org/maven2/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.pom
2026-01-19T16:16:29.5177344Z Progress (1): 766 B
2026-01-19T16:16:29.5177901Z                    
2026-01-19T16:16:29.5178483Z Downloaded from central: https://repo.maven.apache.org/maven2/org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.pom (766 B at 35 kB/s)
2026-01-19T16:16:29.5210564Z Downloading from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-core/3.23.1/assertj-core-3.23.1.pom
2026-01-19T16:16:29.5418810Z Progress (1): 1.1 kB
2026-01-19T16:16:29.5423140Z Progress (1): 3.3 kB
2026-01-19T16:16:29.5423517Z Progress (1): 6.7 kB
2026-01-19T16:16:29.5423889Z Progress (1): 9.8 kB
2026-01-19T16:16:29.5424240Z Progress (1): 12 kB 
2026-01-19T16:16:29.5424567Z Progress (1): 15 kB
2026-01-19T16:16:29.5424918Z Progress (1): 17 kB
2026-01-19T16:16:29.5425286Z Progress (1): 21 kB
2026-01-19T16:16:29.5427103Z Progress (1): 24 kB
2026-01-19T16:16:29.5427539Z Progress (1): 24 kB
2026-01-19T16:16:29.5427881Z                    
2026-01-19T16:16:29.5428367Z Downloaded from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-core/3.23.1/assertj-core-3.23.1.pom (24 kB at 1.0 MB/s)
2026-01-19T16:16:29.5449337Z Downloading from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-parent-pom/2.2.17/assertj-parent-pom-2.2.17.pom
2026-01-19T16:16:29.5714605Z Progress (1): 967 B
2026-01-19T16:16:29.5715304Z Progress (1): 3.4 kB
2026-01-19T16:16:29.5717150Z Progress (1): 6.0 kB
2026-01-19T16:16:29.5719267Z Progress (1): 10 kB 
2026-01-19T16:16:29.5719968Z Progress (1): 16 kB
2026-01-19T16:16:29.5720372Z Progress (1): 18 kB
2026-01-19T16:16:29.5720841Z Progress (1): 21 kB
2026-01-19T16:16:29.5727170Z Progress (1): 24 kB
2026-01-19T16:16:29.5727906Z                    
2026-01-19T16:16:29.5728706Z Downloaded from central: https://repo.maven.apache.org/maven2/org/assertj/assertj-parent-pom/2.2.17/assertj-parent-pom-2.2.17.pom (24 kB at 868 kB/s)
2026-01-19T16:16:29.5766817Z Downloading from central: https://repo.maven.apache.org/maven2/org/mockito/mockito-bom/4.5.1/mockito-bom-4.5.1.pom
2026-01-19T16:16:29.6031071Z Progress (1): 1.4 kB
2026-01-19T16:16:29.6031411Z Progress (1): 3.0 kB
2026-01-19T16:16:29.6031703Z                     
2026-01-19T16:16:29.6032282Z Downloaded from central: https://repo.maven.apache.org/maven2/org/mockito/mockito-bom/4.5.1/mockito-bom-4.5.1.pom (3.0 kB at 119 kB/s)
2026-01-19T16:16:29.6083508Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.12.10/byte-buddy-1.12.10.pom
2026-01-19T16:16:29.6312773Z Progress (1): 950 B
2026-01-19T16:16:29.6313971Z Progress (1): 3.6 kB
2026-01-19T16:16:29.6314939Z Progress (1): 7.4 kB
2026-01-19T16:16:29.6315446Z Progress (1): 15 kB 
2026-01-19T16:16:29.6336975Z Progress (1): 17 kB
2026-01-19T16:16:29.6337653Z                    
2026-01-19T16:16:29.6338301Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy/1.12.10/byte-buddy-1.12.10.pom (17 kB at 664 kB/s)
2026-01-19T16:16:29.6339024Z Downloading from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.12.10/byte-buddy-parent-1.12.10.pom
2026-01-19T16:16:29.6584353Z Progress (1): 840 B
2026-01-19T16:16:29.6589450Z Progress (1): 2.1 kB
2026-01-19T16:16:29.6594156Z Progress (1): 4.0 kB
2026-01-19T16:16:29.6599579Z Progress (1): 6.2 kB
2026-01-19T16:16:29.6604286Z Progress (1): 8.2 kB
2026-01-19T16:16:29.6609264Z Progress (1): 11 kB 
2026-01-19T16:16:29.6614102Z Progress (1): 14 kB
2026-01-19T16:16:29.6619255Z Progress (1): 19 kB
2026-01-19T16:16:29.6624510Z Progress (1): 25 kB
2026-01-19T16:16:29.6629401Z Progress (1): 37 kB
2026-01-19T16:16:29.6633694Z Progress (1): 42 kB
2026-01-19T16:16:29.6641356Z Progress (1): 45 kB
2026-01-19T16:16:29.6641860Z                    
2026-01-19T16:16:29.6643039Z Downloaded from central: https://repo.maven.apache.org/maven2/net/bytebuddy/byte-buddy-parent/1.12.10/byte-buddy-parent-1.12.10.pom (45 kB at 1.5 MB/s)
2026-01-19T16:16:29.6710708Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-java5/3.0.0-M9/common-java5-3.0.0-M9.jar
2026-01-19T16:16:29.6727933Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-testng-utils/3.0.0-M9/surefire-testng-utils-3.0.0-M9.jar
2026-01-19T16:16:29.6732623Z Downloading from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-grouper/3.0.0-M9/surefire-grouper-3.0.0-M9.jar
2026-01-19T16:16:29.6913940Z Progress (1): 7.7/14 kB
2026-01-19T16:16:29.6932984Z Progress (1): 14 kB    
2026-01-19T16:16:29.6936400Z                    
2026-01-19T16:16:29.6939690Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-testng-utils/3.0.0-M9/surefire-testng-utils-3.0.0-M9.jar (14 kB at 645 kB/s)
2026-01-19T16:16:29.6940786Z Progress (1): 7.7/40 kB
2026-01-19T16:16:29.6942755Z Progress (1): 16/40 kB 
2026-01-19T16:16:29.6943334Z Progress (2): 16/40 kB | 7.5/17 kB
2026-01-19T16:16:29.6944906Z Progress (2): 32/40 kB | 7.5/17 kB
2026-01-19T16:16:29.6945226Z Progress (2): 40 kB | 7.5/17 kB   
2026-01-19T16:16:29.6945521Z Progress (2): 40 kB | 17 kB    
2026-01-19T16:16:29.6945804Z                            
2026-01-19T16:16:29.6946246Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/surefire-grouper/3.0.0-M9/surefire-grouper-3.0.0-M9.jar (40 kB at 1.9 MB/s)
2026-01-19T16:16:29.6947113Z Downloaded from central: https://repo.maven.apache.org/maven2/org/apache/maven/surefire/common-java5/3.0.0-M9/common-java5-3.0.0-M9.jar (17 kB at 753 kB/s)
2026-01-19T16:16:29.7098937Z [INFO] 
2026-01-19T16:16:29.7099317Z [INFO] -------------------------------------------------------
2026-01-19T16:16:29.7099668Z [INFO]  T E S T S
2026-01-19T16:16:29.7100014Z [INFO] -------------------------------------------------------
2026-01-19T16:16:30.3184601Z [INFO] Running TestSuite
2026-01-19T16:16:31.9839971Z 🚀 Starting local Appium server...
2026-01-19T16:16:32.2739958Z ✅ Local Appium server started
2026-01-19T16:16:32.5788064Z 
2026-01-19T16:16:32.5793007Z Scenario: CUMA-C98620 Verify that user is not able to login using wrong credentials. # file:///home/vsts/work/1/s/src/test/java/FeatureFiles/Login.feature:5
2026-01-19T16:16:32.5801344Z 📊 Starting scenario #1: CUMA-C98620 Verify that user is not able to login using wrong credentials.
2026-01-19T16:16:32.5844372Z 🚀 Creating new driver instance
2026-01-19T16:16:32.5932020Z java.io.FileNotFoundException: src/main/resources/config.properties (No such file or directory)
2026-01-19T16:16:32.5933000Z 	at java.base/java.io.FileInputStream.open0(Native Method)
2026-01-19T16:16:32.5933657Z 	at java.base/java.io.FileInputStream.open(FileInputStream.java:219)
2026-01-19T16:16:32.5934388Z 	at java.base/java.io.FileInputStream.<init>(FileInputStream.java:157)
2026-01-19T16:16:32.5935069Z 	at java.base/java.io.FileInputStream.<init>(FileInputStream.java:112)
2026-01-19T16:16:32.5935721Z 	at appium.webdriver.extensions.Utility.<clinit>(Utility.java:16)
2026-01-19T16:16:32.5936396Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:32.5951251Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:32.5951940Z 	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2026-01-19T16:16:32.5952638Z 	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2026-01-19T16:16:32.5953451Z 	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2026-01-19T16:16:32.5954147Z 	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
2026-01-19T16:16:32.5954764Z 	at io.cucumber.java.Invoker.doInvoke(Invoker.java:66)
2026-01-19T16:16:32.5955346Z 	at io.cucumber.java.Invoker.invoke(Invoker.java:24)
2026-01-19T16:16:32.5955961Z 	at io.cucumber.java.AbstractGlueDefinition.invokeMethod(AbstractGlueDefinition.java:47)
2026-01-19T16:16:32.5957066Z 	at io.cucumber.java.JavaHookDefinition.execute(JavaHookDefinition.java:68)
2026-01-19T16:16:32.5957738Z 	at io.cucumber.core.runner.CoreHookDefinition.execute(CoreHookDefinition.java:47)
2026-01-19T16:16:32.5958416Z 	at io.cucumber.core.runner.HookDefinitionMatch.runStep(HookDefinitionMatch.java:21)
2026-01-19T16:16:32.5959085Z 	at io.cucumber.core.runner.ExecutionMode$1.execute(ExecutionMode.java:10)
2026-01-19T16:16:32.5959706Z 	at io.cucumber.core.runner.TestStep.executeStep(TestStep.java:81)
2026-01-19T16:16:32.5960279Z 	at io.cucumber.core.runner.TestStep.run(TestStep.java:53)
2026-01-19T16:16:32.5967000Z 	at io.cucumber.core.runner.TestCase.run(TestCase.java:80)
2026-01-19T16:16:32.5967634Z 	at io.cucumber.core.runner.Runner.runPickle(Runner.java:77)
2026-01-19T16:16:32.5968283Z 	at io.cucumber.testng.TestNGCucumberRunner.lambda$runScenario$1(TestNGCucumberRunner.java:135)
2026-01-19T16:16:32.5968984Z 	at io.cucumber.core.runtime.CucumberExecutionContext.lambda$runTestCase$5(CucumberExecutionContext.java:136)
2026-01-19T16:16:32.5969726Z 	at io.cucumber.core.runtime.RethrowingThrowableCollector.executeAndThrow(RethrowingThrowableCollector.java:23)
2026-01-19T16:16:32.5973504Z 	at io.cucumber.core.runtime.CucumberExecutionContext.runTestCase(CucumberExecutionContext.java:136)
2026-01-19T16:16:32.5974279Z 	at io.cucumber.testng.TestNGCucumberRunner.runScenario(TestNGCucumberRunner.java:132)
2026-01-19T16:16:32.5974939Z 	at io.cucumber.testng.AbstractTestNGCucumberTests.runScenario(AbstractTestNGCucumberTests.java:35)
2026-01-19T16:16:32.5975560Z 	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
2026-01-19T16:16:32.5976759Z 	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
2026-01-19T16:16:32.5977471Z 	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
2026-01-19T16:16:32.5978200Z 	at java.base/java.lang.reflect.Method.invoke(Method.java:566)
2026-01-19T16:16:32.5979347Z 	at org.testng.internal.invokers.MethodInvocationHelper.invokeMethod(MethodInvocationHelper.java:141)
2026-01-19T16:16:32.5993697Z 	at org.testng.internal.invokers.TestInvoker.invokeMethod(TestInvoker.java:687)
2026-01-19T16:16:32.5994667Z 	at org.testng.internal.invokers.TestInvoker.invokeTestMethod(TestInvoker.java:230)
2026-01-19T16:16:32.5995389Z 	at org.testng.internal.invokers.MethodRunner.runInSequence(MethodRunner.java:63)
2026-01-19T16:16:32.5996074Z 	at org.testng.internal.invokers.TestInvoker$MethodInvocationAgent.invoke(TestInvoker.java:995)
2026-01-19T16:16:32.5997081Z 	at org.testng.internal.invokers.TestInvoker.invokeTestMethods(TestInvoker.java:203)
2026-01-19T16:16:32.5997867Z 	at org.testng.internal.invokers.TestMethodWorker.invokeTestMethods(TestMethodWorker.java:154)
2026-01-19T16:16:32.5998591Z 	at org.testng.internal.invokers.TestMethodWorker.run(TestMethodWorker.java:134)
2026-01-19T16:16:32.5999236Z 	at java.base/java.util.ArrayList.forEach(ArrayList.java:1541)
2026-01-19T16:16:32.5999846Z 	at org.testng.TestRunner.privateRun(TestRunner.java:741)
2026-01-19T16:16:32.6017213Z 	at org.testng.TestRunner.run(TestRunner.java:616)
2026-01-19T16:16:32.6017828Z 	at org.testng.SuiteRunner.runTest(SuiteRunner.java:421)
2026-01-19T16:16:32.6018432Z 	at org.testng.SuiteRunner.runSequentially(SuiteRunner.java:413)
2026-01-19T16:16:32.6019001Z 	at org.testng.SuiteRunner.privateRun(SuiteRunner.java:373)
2026-01-19T16:16:32.6019560Z 	at org.testng.SuiteRunner.run(SuiteRunner.java:312)
2026-01-19T16:16:32.6020131Z 	at org.testng.SuiteRunnerWorker.runSuite(SuiteRunnerWorker.java:52)
2026-01-19T16:16:32.6020713Z 	at org.testng.SuiteRunnerWorker.run(SuiteRunnerWorker.java:95)
2026-01-19T16:16:32.6021299Z 	at org.testng.TestNG.runSuitesSequentially(TestNG.java:1274)
2026-01-19T16:16:32.6021817Z 	at org.testng.TestNG.runSuitesLocally(TestNG.java:1208)
2026-01-19T16:16:32.6022318Z 	at org.testng.TestNG.runSuites(TestNG.java:1112)
2026-01-19T16:16:32.6022940Z 	at org.testng.TestNG.run(TestNG.java:1079)
2026-01-19T16:16:32.6023773Z 	at org.apache.maven.surefire.testng.TestNGExecutor.run(TestNGExecutor.java:324)
2026-01-19T16:16:32.6024372Z 	at org.apache.maven.surefire.testng.TestNGXmlTestSuite.execute(TestNGXmlTestSuite.java:74)
2026-01-19T16:16:32.6024987Z 	at org.apache.maven.surefire.testng.TestNGProvider.invoke(TestNGProvider.java:123)
2026-01-19T16:16:32.6025653Z 	at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:456)
2026-01-19T16:16:32.6026249Z 	at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:169)
2026-01-19T16:16:32.6027088Z 	at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:595)
2026-01-19T16:16:32.6027655Z 	at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:581)
2026-01-19T16:16:32.6028271Z         java.lang.ExceptionInInitializerError
2026-01-19T16:16:32.6028812Z         	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:32.6029381Z         	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:32.6029917Z         Caused by: java.lang.RuntimeException: Could not load config.properties file.
2026-01-19T16:16:32.6030525Z         	at appium.webdriver.extensions.Utility.<clinit>(Utility.java:21)
2026-01-19T16:16:32.6031079Z         	... 2 more
2026-01-19T16:16:32.6031967Z   ↷ Given User is on Login page                                                      # com.client.app.stepDefs.LoginStepDef.UserLogin()
2026-01-19T16:16:32.6033209Z   ↷ When User attempts Forms Login with wrong password as "incorrectpassword"        # com.client.app.stepDefs.LoginStepDef.user_performs_Forms_Login_with_invalid_credentials(java.lang.String)
2026-01-19T16:16:32.6037276Z   ↷ Then Verify authentication failed message                                        # com.client.app.stepDefs.LoginStepDef.verify_invalid_Forms_login()
2026-01-19T16:16:32.6038097Z 📊 Completed scenario #1 out of 1
2026-01-19T16:16:32.6238729Z 
2026-01-19T16:16:32.6239883Z Scenario: CUMA-C226538 Perform Login with valid credentials # file:///home/vsts/work/1/s/src/test/java/FeatureFiles/Login.feature:11
2026-01-19T16:16:32.6240843Z 📊 Starting scenario #2: CUMA-C226538 Perform Login with valid credentials
2026-01-19T16:16:32.6241647Z 🚀 Creating new driver instance
2026-01-19T16:16:32.6242192Z         java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:32.6242842Z         	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:32.6243493Z         	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:32.6244273Z   ↷ Given User is on Login page                             # com.client.app.stepDefs.LoginStepDef.UserLogin()
2026-01-19T16:16:32.6245061Z   ↷ When User performs Forms Login                          # com.client.app.stepDefs.LoginStepDef.User_performs_Forms_Login()
2026-01-19T16:16:32.6245831Z   ↷ Then User successfully logged-in                        # com.client.app.stepDefs.LoginStepDef.verify_UserLogin()
2026-01-19T16:16:32.6246468Z 📊 Completed scenario #2 out of 2
2026-01-19T16:16:32.6793006Z 🧹 Cleaning up resources and quitting driver
2026-01-19T16:16:32.6799018Z 🛑 Stopping local Appium server...
2026-01-19T16:16:32.7810379Z ✅ Local Appium server stopped
2026-01-19T16:16:33.2857353Z 🚀 Starting local Appium server...
2026-01-19T16:16:33.3018974Z ✅ Local Appium server started
2026-01-19T16:16:33.3523954Z 
2026-01-19T16:16:33.3525224Z Scenario: CUMA-C255123 Verify the building the user has currently selected is shown at the top of the overlay # file:///home/vsts/work/1/s/src/test/java/FeatureFiles/UserProfile.feature:4
2026-01-19T16:16:33.3526700Z 📊 Starting scenario #1: CUMA-C255123 Verify the building the user has currently selected is shown at the top of the overlay
2026-01-19T16:16:33.3527575Z 🚀 Creating new driver instance
2026-01-19T16:16:33.3528157Z         java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.3528787Z         	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.3529463Z         	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.3530302Z   ↷ Given User is on user profile page                                                                        # com.client.app.stepDefs.UserProfileStepDef.user_is_on_profile_page()
2026-01-19T16:16:33.3533105Z   ↷ When User tap on default location option of personal space                                                # com.client.app.stepDefs.UserProfileStepDef.user_tap_on_default_location_option()
2026-01-19T16:16:33.3533890Z   ↷ Then Building name is displayed at the top of floor overlay                                               # com.client.app.stepDefs.UserProfileStepDef.user_tap_on_floor_option()
2026-01-19T16:16:33.3534414Z 📊 Completed scenario #1 out of 1
2026-01-19T16:16:33.3763297Z 
2026-01-19T16:16:33.3765858Z Scenario Outline: CUMA-C255126 Verify the pop up shown on log out button on Default setting screen. # file:///home/vsts/work/1/s/src/test/java/FeatureFiles/UserProfile.feature:15
2026-01-19T16:16:33.3767143Z 📊 Starting scenario #2: CUMA-C255126 Verify the pop up shown on log out button on Default setting screen.
2026-01-19T16:16:33.3769126Z 🚀 Creating new driver instance
2026-01-19T16:16:33.3769584Z         java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.3770305Z         	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.3771021Z         	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.3771937Z   ↷ Given User is on user profile page                                                              # com.client.app.stepDefs.UserProfileStepDef.user_is_on_profile_page()
2026-01-19T16:16:33.3772818Z   ↷ When User tap on the logout button                                                              # com.client.app.stepDefs.UserProfileStepDef.user_tap_on_logout_button()
2026-01-19T16:16:33.3773757Z   ↷ Then Pop up is shown on tapping logout button "Are you sure you want to log out?"               # com.client.app.stepDefs.UserProfileStepDef.popup_on_tapping_logout_button(java.lang.String)
2026-01-19T16:16:33.3774598Z 📊 Completed scenario #2 out of 2
2026-01-19T16:16:33.3855502Z 
2026-01-19T16:16:33.3866219Z Scenario: CUMA-C255127 Verify the Save button on Default setting screen.     # file:///home/vsts/work/1/s/src/test/java/FeatureFiles/UserProfile.feature:17
2026-01-19T16:16:33.3867350Z 📊 Starting scenario #3: CUMA-C255127 Verify the Save button on Default setting screen.
2026-01-19T16:16:33.3867951Z 🚀 Creating new driver instance
2026-01-19T16:16:33.3910149Z         java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.3917434Z         	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.3917963Z         	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.3918715Z   ↷ Given User is on user profile page                                       # com.client.app.stepDefs.UserProfileStepDef.user_is_on_profile_page()
2026-01-19T16:16:33.3919498Z   ↷ When User tap on country option of personal space and choose the country # com.client.app.stepDefs.UserProfileStepDef.user_tap_on_country_option()
2026-01-19T16:16:33.3920245Z   ↷ And User press the save button                                           # com.client.app.stepDefs.UserProfileStepDef.user_press_on_save_button()
2026-01-19T16:16:33.3920933Z   ↷ Then Changed value should get successfully updated                       # com.client.app.stepDefs.UserProfileStepDef.validate_saved_value()
2026-01-19T16:16:33.3921459Z 📊 Completed scenario #3 out of 3
2026-01-19T16:16:33.4042038Z 
2026-01-19T16:16:33.4042689Z Scenario: CUMA-C255125 Verify if the user chooses to close the overlay without making a selection, the previously selected country is not changed. # file:///home/vsts/work/1/s/src/test/java/FeatureFiles/UserProfile.feature:24
2026-01-19T16:16:33.4043694Z 📊 Starting scenario #4: CUMA-C255125 Verify if the user chooses to close the overlay without making a selection, the previously selected country is not changed.
2026-01-19T16:16:33.4044314Z 🚀 Creating new driver instance
2026-01-19T16:16:33.4044742Z         java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.4045248Z         	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.4045783Z         	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.4046791Z   ↷ Given User is on user profile page                                                                                                             # com.client.app.stepDefs.UserProfileStepDef.user_is_on_profile_page()
2026-01-19T16:16:33.4047979Z   ↷ When User tap on country option of personal space and choose the default country                                                               # com.client.app.stepDefs.UserProfileStepDef.user_tap_on_default_country_option()
2026-01-19T16:16:33.4048991Z   ↷ And User press the close button                                                                                                                # com.client.app.stepDefs.UserProfileStepDef.user_tap_on_close_button()
2026-01-19T16:16:33.4050206Z   ↷ Then Previously selected country should not be changed if no selection is made                                                                 # com.client.app.stepDefs.UserProfileStepDef.verify_country_name_not_changed()
2026-01-19T16:16:33.4051177Z 📊 Completed scenario #4 out of 4
2026-01-19T16:16:33.4162781Z 
2026-01-19T16:16:33.4190899Z Scenario: CUMA-C255124 Verify when the user presses the 'Floor' button, the Floor selection overlay appears # file:///home/vsts/work/1/s/src/test/java/FeatureFiles/UserProfile.feature:30
2026-01-19T16:16:33.4191994Z 📊 Starting scenario #5: CUMA-C255124 Verify when the user presses the 'Floor' button, the Floor selection overlay appears
2026-01-19T16:16:33.4192679Z 🚀 Creating new driver instance
2026-01-19T16:16:33.4193450Z         java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.4194064Z         	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.4194664Z         	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.4195548Z   ↷ Given User is on user profile page                                                                      # com.client.app.stepDefs.UserProfileStepDef.user_is_on_profile_page()
2026-01-19T16:16:33.4196404Z   ↷ When User tap on floor option                                                                           # com.client.app.stepDefs.UserProfileStepDef.user_tap_on_floor()
2026-01-19T16:16:33.4197658Z   ↷ Then The floor selection overlay appears                                                                # com.client.app.stepDefs.UserProfileStepDef.verify_floor_selection_overlay()
2026-01-19T16:16:33.4198377Z 📊 Completed scenario #5 out of 5
2026-01-19T16:16:33.4303584Z 
2026-01-19T16:16:33.4304360Z Scenario: CUMA-C255120-Verify when the user presses the Group button, the Group selection overlay appears. # file:///home/vsts/work/1/s/src/test/java/FeatureFiles/UserProfile.feature:35
2026-01-19T16:16:33.4305411Z 📊 Starting scenario #6: CUMA-C255120-Verify when the user presses the Group button, the Group selection overlay appears.
2026-01-19T16:16:33.4306190Z 🚀 Creating new driver instance
2026-01-19T16:16:33.4306868Z         java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.4307510Z         	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.4308166Z         	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.4309094Z   ↷ Given User is on user profile page                                                                     # com.client.app.stepDefs.UserProfileStepDef.user_is_on_profile_page()
2026-01-19T16:16:33.4310115Z   ↷ When User tap on group option                                                                          # com.client.app.stepDefs.UserProfileStepDef.user_tap_on_group()
2026-01-19T16:16:33.4311077Z   ↷ Then The group selection overlay appears                                                               # com.client.app.stepDefs.UserProfileStepDef.verify_group_selection_overlay()
2026-01-19T16:16:33.4311819Z 📊 Completed scenario #6 out of 6
2026-01-19T16:16:33.4448524Z 
2026-01-19T16:16:33.4465763Z Scenario: CUMA-C255324-Verify the current selection of floor is highlighted. # file:///home/vsts/work/1/s/src/test/java/FeatureFiles/UserProfile.feature:40
2026-01-19T16:16:33.4466825Z 📊 Starting scenario #7: CUMA-C255324-Verify the current selection of floor is highlighted.
2026-01-19T16:16:33.4467329Z 🚀 Creating new driver instance
2026-01-19T16:16:33.4467741Z         java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.4468254Z         	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.4468717Z         	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.4469384Z   ↷ Given User is on user profile page                                       # com.client.app.stepDefs.UserProfileStepDef.user_is_on_profile_page()
2026-01-19T16:16:33.4470224Z   ↷ When User tap on floor option                                            # com.client.app.stepDefs.UserProfileStepDef.user_tap_on_floor()
2026-01-19T16:16:33.4470909Z   ↷ Then The current selection of floor is highlighted                       # com.client.app.stepDefs.UserProfileStepDef.verify_floor_highlighted()
2026-01-19T16:16:33.4471405Z 📊 Completed scenario #7 out of 7
2026-01-19T16:16:33.4505702Z 
2026-01-19T16:16:33.4510440Z Scenario: CUMA-C255122-Verify the current selection of Group is highlighted. # file:///home/vsts/work/1/s/src/test/java/FeatureFiles/UserProfile.feature:45
2026-01-19T16:16:33.4511274Z 📊 Starting scenario #8: CUMA-C255122-Verify the current selection of Group is highlighted.
2026-01-19T16:16:33.4511711Z 🚀 Creating new driver instance
2026-01-19T16:16:33.4512102Z         java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.4512577Z         	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.4513021Z         	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.4513637Z   ↷ Given User is on user profile page                                       # com.client.app.stepDefs.UserProfileStepDef.user_is_on_profile_page()
2026-01-19T16:16:33.4514221Z   ↷ When User tap on group option                                            # com.client.app.stepDefs.UserProfileStepDef.user_tap_on_group()
2026-01-19T16:16:33.4514859Z   ↷ Then The current selection of Group is highlighted                       # com.client.app.stepDefs.UserProfileStepDef.verify_Group_highlighted()
2026-01-19T16:16:33.4515335Z 📊 Completed scenario #8 out of 8
2026-01-19T16:16:33.4850939Z 🧹 Cleaning up resources and quitting driver
2026-01-19T16:16:33.4851480Z 🛑 Stopping local Appium server...
2026-01-19T16:16:33.5871903Z ✅ Local Appium server stopped
2026-01-19T16:16:33.8012535Z [ERROR] Tests run: 10, Failures: 10, Errors: 0, Skipped: 0, Time elapsed: 3.42 s <<< FAILURE! - in TestSuite
2026-01-19T16:16:33.8013534Z [ERROR] TestRunner.LoginTestRunner.runScenario["CUMA-C98620 Verify that user is not able to login using wrong credentials.", "US #: Verify login flow for Eptura Engage  mobile Application"](1)  Time elapsed: 0.333 s  <<< FAILURE!
2026-01-19T16:16:33.8014308Z java.lang.ExceptionInInitializerError
2026-01-19T16:16:33.8014881Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.8015476Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.8016058Z Caused by: java.lang.RuntimeException: Could not load config.properties file.
2026-01-19T16:16:33.8016920Z 	at appium.webdriver.extensions.Utility.<clinit>(Utility.java:21)
2026-01-19T16:16:33.8017438Z 	... 2 more
2026-01-19T16:16:33.8017740Z 
2026-01-19T16:16:33.8018343Z [ERROR] TestRunner.LoginTestRunner.runScenario["CUMA-C226538 Perform Login with valid credentials", "US #: Verify login flow for Eptura Engage  mobile Application"](2)  Time elapsed: 0.017 s  <<< FAILURE!
2026-01-19T16:16:33.8019051Z java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8019600Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.8020140Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.8020407Z 
2026-01-19T16:16:33.8024574Z [ERROR] TestRunner.UserProfileTestRunner.runScenario["CUMA-C255123 Verify the building the user has currently selected is shown at the top of the overlay", "US #: User Profile"](1)  Time elapsed: 0.053 s  <<< FAILURE!
2026-01-19T16:16:33.8025313Z java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8025927Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.8026682Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.8027230Z 
2026-01-19T16:16:33.8027742Z [ERROR] TestRunner.UserProfileTestRunner.runScenario["CUMA-C255126 Verify the pop up shown on log out button on Default setting screen.", "US #: User Profile"](2)  Time elapsed: 0.024 s  <<< FAILURE!
2026-01-19T16:16:33.8028445Z java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8028929Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.8029537Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.8029823Z 
2026-01-19T16:16:33.8030285Z [ERROR] TestRunner.UserProfileTestRunner.runScenario["CUMA-C255127 Verify the Save button on Default setting screen.", "US #: User Profile"](3)  Time elapsed: 0.014 s  <<< FAILURE!
2026-01-19T16:16:33.8031248Z java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8031846Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.8032432Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.8032730Z 
2026-01-19T16:16:33.8033257Z [ERROR] TestRunner.UserProfileTestRunner.runScenario["CUMA-C255125 Verify if the user chooses to close the overlay without making a selection, the previously selected country is not changed.", "US #: User Profile"](4)  Time elapsed: 0.014 s  <<< FAILURE!
2026-01-19T16:16:33.8033997Z java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8034467Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.8035002Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.8046951Z 
2026-01-19T16:16:33.8047582Z [ERROR] TestRunner.UserProfileTestRunner.runScenario["CUMA-C255124 Verify when the user presses the 'Floor' button, the Floor selection overlay appears", "US #: User Profile"](5)  Time elapsed: 0.007 s  <<< FAILURE!
2026-01-19T16:16:33.8048309Z java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8048922Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.8049556Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.8049825Z 
2026-01-19T16:16:33.8050350Z [ERROR] TestRunner.UserProfileTestRunner.runScenario["CUMA-C255120-Verify when the user presses the Group button, the Group selection overlay appears.", "US #: User Profile"](6)  Time elapsed: 0.012 s  <<< FAILURE!
2026-01-19T16:16:33.8055699Z java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8056212Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.8057192Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.8057408Z 
2026-01-19T16:16:33.8057872Z [ERROR] TestRunner.UserProfileTestRunner.runScenario["CUMA-C255324-Verify the current selection of floor is highlighted.", "US #: User Profile"](7)  Time elapsed: 0.013 s  <<< FAILURE!
2026-01-19T16:16:33.8058410Z java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8058901Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.8059380Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.8059582Z 
2026-01-19T16:16:33.8060035Z [ERROR] TestRunner.UserProfileTestRunner.runScenario["CUMA-C255122-Verify the current selection of Group is highlighted.", "US #: User Profile"](8)  Time elapsed: 0.005 s  <<< FAILURE!
2026-01-19T16:16:33.8060596Z java.lang.NoClassDefFoundError: Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8061074Z 	at appium.webdriver.extensions.DriverFactory.createDriver(DriverFactory.java:69)
2026-01-19T16:16:33.8061700Z 	at appium.webdriver.extensions.Hooks.beforeScenario(Hooks.java:33)
2026-01-19T16:16:33.8061902Z 
2026-01-19T16:16:33.8246394Z [INFO] 
2026-01-19T16:16:33.8247087Z [INFO] Results:
2026-01-19T16:16:33.8247386Z [INFO] 
2026-01-19T16:16:33.8247671Z [ERROR] Failures: 
2026-01-19T16:16:33.8248454Z [ERROR]   LoginTestRunner.runScenario » NoClassDefFound Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8249046Z [ERROR]   LoginTestRunner.runScenario » ExceptionInInitializer
2026-01-19T16:16:33.8249703Z [ERROR]   UserProfileTestRunner.runScenario » NoClassDefFound Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8250603Z [ERROR]   UserProfileTestRunner.runScenario » NoClassDefFound Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8251478Z [ERROR]   UserProfileTestRunner.runScenario » NoClassDefFound Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8252354Z [ERROR]   UserProfileTestRunner.runScenario » NoClassDefFound Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8253206Z [ERROR]   UserProfileTestRunner.runScenario » NoClassDefFound Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8254041Z [ERROR]   UserProfileTestRunner.runScenario » NoClassDefFound Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8254851Z [ERROR]   UserProfileTestRunner.runScenario » NoClassDefFound Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8255625Z [ERROR]   UserProfileTestRunner.runScenario » NoClassDefFound Could not initialize class appium.webdriver.extensions.Utility
2026-01-19T16:16:33.8256289Z [INFO] 
2026-01-19T16:16:33.8256910Z [ERROR] Tests run: 10, Failures: 10, Errors: 0, Skipped: 0
2026-01-19T16:16:33.8257330Z [INFO] 
2026-01-19T16:16:33.8291724Z [INFO] ------------------------------------------------------------------------
2026-01-19T16:16:33.8297860Z [INFO] BUILD FAILURE
2026-01-19T16:16:33.8298365Z [INFO] ------------------------------------------------------------------------
2026-01-19T16:16:33.8309727Z [INFO] Total time:  27.615 s
2026-01-19T16:16:33.8310369Z [INFO] Finished at: 2026-01-19T16:16:33Z
2026-01-19T16:16:33.8310766Z [INFO] ------------------------------------------------------------------------
2026-01-19T16:16:33.8318694Z [ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:3.0.0-M9:test (default-test) on project EpturaEngageAutomation-Android: There are test failures.
2026-01-19T16:16:33.8325357Z [ERROR] 
2026-01-19T16:16:33.8325821Z [ERROR] Please refer to /home/vsts/work/1/s/target/surefire-reports for the individual test results.
2026-01-19T16:16:33.8326276Z [ERROR] Please refer to dump files (if any exist) [date].dump, [date]-jvmRun[N].dump and [date].dumpstream.
2026-01-19T16:16:33.8326826Z [ERROR] -> [Help 1]
2026-01-19T16:16:33.8327084Z [ERROR] 
2026-01-19T16:16:33.8327401Z [ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
2026-01-19T16:16:33.8327799Z [ERROR] Re-run Maven using the -X switch to enable full debug logging.
2026-01-19T16:16:33.8328117Z [ERROR] 
2026-01-19T16:16:33.8328479Z [ERROR] For more information about the errors and possible solutions, please read the following articles:
2026-01-19T16:16:33.8328926Z [ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException
2026-01-19T16:16:33.8645132Z 
2026-01-19T16:16:33.8662635Z The process '/usr/bin/mvn' failed with exit code 1
2026-01-19T16:16:33.8665131Z Could not retrieve code analysis results - Maven run failed.
2026-01-19T16:16:34.4230664Z Result Attachments will be stored in LogStore
2026-01-19T16:16:34.4318547Z Run Attachments will be stored in LogStore
2026-01-19T16:16:34.4819713Z ##[error]Build failed.
2026-01-19T16:16:34.4825606Z ##[section]Async Command Start: Publish test results
2026-01-19T16:16:34.5790463Z Publishing test results to test run '78'.
2026-01-19T16:16:34.5801611Z TestResults To Publish 10, Test run id:78
2026-01-19T16:16:34.5823187Z Test results publishing 10, remaining: 0. Test run id: 78
2026-01-19T16:16:35.3244695Z Published Test Run : https://dev.azure.com/EpturaEnterpriseDevOps/Enterprise/_TestManagement/Runs?runId=78&_a=runCharts
2026-01-19T16:16:35.4264910Z Flaky failed test results are opted out of pass percentage
2026-01-19T16:16:35.4383050Z ##[section]Async Command End: Publish test results
2026-01-19T16:16:35.4384193Z ##[section]Finishing: Run Tests