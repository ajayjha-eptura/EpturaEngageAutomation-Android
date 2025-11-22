2025-11-21T18:09:38.8089450Z ##[section]Starting: Setup Android SDK and Create Emulator with Google Play
2025-11-21T18:09:38.8111180Z ==============================================================================
2025-11-21T18:09:38.8111630Z Task         : Bash
2025-11-21T18:09:38.8111920Z Description  : Run a Bash script on macOS, Linux, or Windows
2025-11-21T18:09:38.8112260Z Version      : 3.259.0
2025-11-21T18:09:38.8113140Z Author       : Microsoft Corporation
2025-11-21T18:09:38.8113480Z Help         : https://docs.microsoft.com/azure/devops/pipelines/tasks/utility/bash
2025-11-21T18:09:38.8113930Z ==============================================================================
2025-11-21T18:09:39.3511210Z Generating script.
2025-11-21T18:09:39.3526990Z ========================== Starting Command Output ===========================
2025-11-21T18:09:39.3540050Z [command]/bin/bash /Users/runner/work/_temp/0c40b85f-c668-486d-9169-fda57745c2d3.sh
2025-11-21T18:09:39.3542690Z 📱 Configuring Android SDK with Google Play support...
2025-11-21T18:09:39.3544650Z ANDROID_HOME: /Users/runner/Library/Android/sdk
2025-11-21T18:09:39.3546740Z ANDROID_SDK_ROOT: /Users/runner/Library/Android/sdk
2025-11-21T18:09:39.3548520Z 📋 Android SDK structure:
2025-11-21T18:09:39.3551230Z total 48
2025-11-21T18:09:39.3552940Z drwxr-xr-x  15 runner  staff    480 Sep  8 06:36 .
2025-11-21T18:09:39.3555870Z drwxr-xr-x   3 runner  staff     96 Sep  8 06:32 ..
2025-11-21T18:09:39.3557460Z -rw-r--r--   1 runner  staff     16 Sep  8 06:47 .knownPackages
2025-11-21T18:09:39.3559310Z drwxr-xr-x   2 runner  staff     64 Sep  8 06:36 .temp
2025-11-21T18:09:39.3561340Z drwxr-xr-x   8 runner  staff    256 Sep  8 06:34 build-tools
2025-11-21T18:09:39.3563280Z drwxr-xr-x   3 runner  staff     96 Sep  8 06:36 cmake
2025-11-21T18:09:39.3565400Z drwxr-xr-x   3 runner  staff     96 Sep  8 06:32 cmdline-tools
2025-11-21T18:09:39.3567590Z drwxr-xr-x  29 runner  staff    928 Sep  8 06:33 emulator
2025-11-21T18:09:39.3569290Z drwxr-xr-x   4 runner  staff    128 Sep  8 06:36 extras
2025-11-21T18:09:39.3571770Z drwxr-xr-x   3 runner  staff     96 Sep  8 06:32 licenses
2025-11-21T18:09:39.3573060Z drwxr-xr-x   5 runner  staff    160 Sep  8 06:34 ndk
2025-11-21T18:09:39.3576100Z -rw-r--r--   1 runner  staff  18387 Sep  8 06:36 packages-list.txt
2025-11-21T18:09:39.3578600Z drwxr-xr-x  15 runner  staff    480 Sep  8 06:33 platform-tools
2025-11-21T18:09:39.3582420Z drwxr-xr-x  16 runner  staff    512 Sep  8 06:35 platforms
2025-11-21T18:09:39.3583840Z drwxr-xr-x  14 runner  staff    448 Sep  8 06:36 tools
2025-11-21T18:09:42.2730870Z 📝 Accepting Android SDK licenses...
2025-11-21T18:09:42.2731470Z Loading local repository...                                                     
2025-11-21T18:09:42.2799580Z [=========                              ] 25% Loading local repository...       
2025-11-21T18:09:43.8246070Z [=========                              ] 25% Fetch remote repository...        
2025-11-21T18:09:44.9590560Z [==========                             ] 26% Fetch remote repository...        
2025-11-21T18:09:45.0593450Z [============                           ] 31% Fetch remote repository...        
2025-11-21T18:09:45.1503790Z [============                           ] 32% Fetch remote repository...        
2025-11-21T18:09:45.1631190Z [=============                          ] 33% Fetch remote repository...        
2025-11-21T18:09:45.1805270Z [=============                          ] 35% Fetch remote repository...        
2025-11-21T18:09:45.1887610Z [==============                         ] 36% Fetch remote repository...        
2025-11-21T18:09:45.1942420Z [==============                         ] 37% Fetch remote repository...        
2025-11-21T18:09:45.1977950Z [===============                        ] 38% Fetch remote repository...        
2025-11-21T18:09:45.2279280Z [===============                        ] 39% Fetch remote repository...        
2025-11-21T18:09:45.2517560Z [================                       ] 40% Fetch remote repository...        
2025-11-21T18:09:45.3463250Z [================                       ] 41% Fetch remote repository...        
2025-11-21T18:09:45.3507260Z [================                       ] 42% Fetch remote repository...        
2025-11-21T18:09:45.3510930Z [=================                      ] 44% Fetch remote repository...        
2025-11-21T18:09:45.3592110Z [=================                      ] 45% Fetch remote repository...        
2025-11-21T18:09:45.3643910Z [==================                     ] 46% Fetch remote repository...        
2025-11-21T18:09:45.3949190Z [==================                     ] 47% Fetch remote repository...        
2025-11-21T18:09:45.3995340Z [===================                    ] 48% Fetch remote repository...        
2025-11-21T18:09:45.4042540Z [===================                    ] 49% Fetch remote repository...        
2025-11-21T18:09:45.5414390Z [====================                   ] 50% Fetch remote repository...        
2025-11-21T18:09:45.5911830Z [====================                   ] 51% Fetch remote repository...        
2025-11-21T18:09:45.6443190Z [====================                   ] 53% Fetch remote repository...        
2025-11-21T18:09:45.6743150Z [=====================                  ] 54% Fetch remote repository...        
2025-11-21T18:09:45.6791500Z [=====================                  ] 55% Fetch remote repository...        
2025-11-21T18:09:45.6815490Z [======================                 ] 56% Fetch remote repository...        
2025-11-21T18:09:45.6977040Z [======================                 ] 57% Fetch remote repository...        
2025-11-21T18:09:45.8001930Z [=======================                ] 58% Fetch remote repository...        
2025-11-21T18:09:46.0011870Z [=======================                ] 59% Fetch remote repository...        
2025-11-21T18:09:46.0673620Z [========================               ] 60% Fetch remote repository...        
2025-11-21T18:09:46.0992740Z [========================               ] 61% Fetch remote repository...        
2025-11-21T18:09:46.1182620Z [=========================              ] 63% Fetch remote repository...        
2025-11-21T18:09:46.1559440Z [=========================              ] 64% Fetch remote repository...        
2025-11-21T18:09:46.1562960Z [=========================              ] 65% Fetch remote repository...        
2025-11-21T18:09:46.1566690Z [==========================             ] 66% Fetch remote repository...        
2025-11-21T18:09:46.1570370Z [==========================             ] 67% Fetch remote repository...        
2025-11-21T18:09:46.1730670Z [===========================            ] 68% Fetch remote repository...        
2025-11-21T18:09:46.1737950Z [===========================            ] 69% Fetch remote repository...        
2025-11-21T18:09:46.3402990Z [============================           ] 70% Fetch remote repository...        
2025-11-21T18:09:46.3405450Z [============================           ] 72% Fetch remote repository...        
2025-11-21T18:09:46.4274900Z [=============================          ] 73% Fetch remote repository...        
2025-11-21T18:09:46.4531570Z [=============================          ] 74% Fetch remote repository...        
2025-11-21T18:09:46.4569530Z [=============================          ] 75% Fetch remote repository...        
2025-11-21T18:09:46.4572170Z [=============================          ] 75% Computing updates...              
2025-11-21T18:09:46.4575010Z [=======================================] 100% Computing updates...             
2025-11-21T18:09:46.5738190Z 6 of 7 SDK package licenses not accepted.
2025-11-21T18:09:46.5921360Z Review licenses that have not been accepted (y/N)? 
2025-11-21T18:09:46.5925560Z 1/6: License android-googletv-license:
2025-11-21T18:09:46.5927410Z ---------------------------------------
2025-11-21T18:09:46.5929130Z Terms and Conditions
2025-11-21T18:09:46.5930320Z 
2025-11-21T18:09:46.5933120Z This is the Google TV Add-on for the Android Software Development Kit License Agreement.
2025-11-21T18:09:46.5935590Z 
2025-11-21T18:09:46.5937200Z 1. Introduction
2025-11-21T18:09:46.5938420Z 
2025-11-21T18:09:46.5940520Z 1.1 The Google TV Add-on for the Android Software Development Kit (referred to in this License Agreement as the "Google TV Add-on" and specifically including the Android system files, packaged APIs, and Google APIs add-ons) is licensed to you subject to the terms of this License Agreement. This License Agreement forms a legally binding contract between you and Google in relation to your use of the Google TV Add-on.
2025-11-21T18:09:46.5942250Z 
2025-11-21T18:09:46.5944800Z 1.2 "Google" means Google Inc., a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.
2025-11-21T18:09:46.5947080Z 
2025-11-21T18:09:46.5950790Z 2. Accepting this License Agreement
2025-11-21T18:09:46.5953650Z 
2025-11-21T18:09:46.5955220Z 2.1 In order to use the Google TV Add-on, you must first agree to this License Agreement. You may not use the Google TV Add-on if you do not accept this License Agreement.
2025-11-21T18:09:46.5956020Z 
2025-11-21T18:09:46.5958410Z 2.2 You can accept this License Agreement by:
2025-11-21T18:09:46.5962350Z 
2025-11-21T18:09:46.5965460Z (A) clicking to accept or agree to this License Agreement, where this option is made available to you; or
2025-11-21T18:09:46.5968400Z 
2025-11-21T18:09:46.5971400Z (B) by actually using the Google TV Add-on. In this case, you agree that use of the Google TV Add-on constitutes acceptance of the License Agreement from that point onwards.
2025-11-21T18:09:46.5973760Z 
2025-11-21T18:09:46.5976330Z 2.3 You may not use the Google TV Add-on and may not accept the Licensing Agreement if you are a person barred from receiving the Google TV Add-on under the laws of the United States or other countries including the country in which you are resident or from which you use the Google TV Add-on.
2025-11-21T18:09:46.5977210Z 
2025-11-21T18:09:46.5978390Z 2.4 If you are agreeing to be bound by this License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to this License Agreement. If you do not have the requisite authority, you may not accept the Licensing Agreement or use the Google TV Add-on on behalf of your employer or other entity.
2025-11-21T18:09:46.5980120Z 
2025-11-21T18:09:46.5980840Z 3. Google TV Add-on License from Google
2025-11-21T18:09:46.5981120Z 
2025-11-21T18:09:46.5982400Z 3.1 Subject to the terms of this License Agreement, Google grants you a limited, worldwide, royalty-free, non- assignable and non-exclusive license to use the Google TV Add-on solely to develop applications to run on the Google TV platform.
2025-11-21T18:09:46.5983390Z 
2025-11-21T18:09:46.5985180Z 3.2 You agree that Google or third parties own all legal right, title and interest in and to the Google TV Add-on, including any Intellectual Property Rights that subsist in the Google TV Add-on. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.
2025-11-21T18:09:46.5986240Z 
2025-11-21T18:09:46.5987860Z 3.3 Except to the extent required by applicable third party licenses, you may not copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the Google TV Add-on or any part of the Google TV Add-on. Except to the extent required by applicable third party licenses, you may not load any part of the Google TV Add-on onto a mobile handset, television, or any other hardware device except a personal computer, combine any part of the Google TV Add-on with other software, or distribute any software or device incorporating a part of the Google TV Add-on.
2025-11-21T18:09:46.5989870Z 
2025-11-21T18:09:46.5990750Z 3.4 Use, reproduction and distribution of components of the Google TV Add-on licensed under an open source software license are governed solely by the terms of that open source software license and not this License Agreement.
2025-11-21T18:09:46.5991610Z 
2025-11-21T18:09:46.5992940Z 3.5 You agree that the form and nature of the Google TV Add-on that Google provides may change without prior notice to you and that future versions of the Google TV Add-on may be incompatible with applications developed on previous versions of the Google TV Add-on. You agree that Google may stop (permanently or temporarily) providing the Google TV Add-on (or any features within the Google TV Add-on) to you or to users generally at Google's sole discretion, without prior notice to you.
2025-11-21T18:09:46.5994060Z 
2025-11-21T18:09:46.5996440Z 3.6 Nothing in this License Agreement gives you a right to use any of Google's or it’s licensors’ trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.
2025-11-21T18:09:46.6000460Z 
2025-11-21T18:09:46.6002880Z 3.7 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the Google TV Add-on.
2025-11-21T18:09:46.6005840Z 
2025-11-21T18:09:46.6007660Z 4. Use of the Google TV Add-on by You
2025-11-21T18:09:46.6009940Z 
2025-11-21T18:09:46.6012350Z 4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under this License Agreement in or to any software applications that you develop using the Google TV Add-on, including any intellectual property rights that subsist in those applications.
2025-11-21T18:09:46.6015670Z 
2025-11-21T18:09:46.6018380Z 4.2 You agree to use the Google TV Add-on and write applications only for purposes that are permitted by (a) this License Agreement and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).
2025-11-21T18:09:46.6023510Z 
2025-11-21T18:09:46.6051140Z 4.3 You agree that if you use the Google TV Add-on to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, your must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you explicit permission to do so.
2025-11-21T18:09:46.6057220Z 
2025-11-21T18:09:46.6084330Z 4.4 You agree that you will not engage in any activity with the Google TV Add-on, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google, Multichannel Video Program Distributors or any mobile communications carrier.
2025-11-21T18:09:46.6118930Z 
2025-11-21T18:09:46.6120630Z 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through the Google TV platform and/or applications for the Google TV platform, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.
2025-11-21T18:09:46.6122610Z 
2025-11-21T18:09:46.6125060Z 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under this License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.
2025-11-21T18:09:46.6126870Z 
2025-11-21T18:09:46.6128630Z 5. Your Developer Credentials
2025-11-21T18:09:46.6129150Z 
2025-11-21T18:09:46.6131160Z 5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.
2025-11-21T18:09:46.6132310Z 
2025-11-21T18:09:46.6133770Z 6. Privacy and Information
2025-11-21T18:09:46.6134780Z 
2025-11-21T18:09:46.6137280Z 6.1 In order to continually innovate and improve the Google TV Add-on, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the Google TV Add-on are being used and how they are being used. Before any of this information is collected, the Google TV Add-on will notify you and seek your consent. If you withhold consent, the information will not be collected.
2025-11-21T18:09:46.6138850Z 
2025-11-21T18:09:46.6140930Z 6.2 The data collected is examined in the aggregate to improve the Google TV Add-on and is maintained in accordance with Google's Privacy Policy.
2025-11-21T18:09:46.6142030Z 
2025-11-21T18:09:46.6143710Z 7. Third Party Applications for the Google TV Platform
2025-11-21T18:09:46.6146510Z 
2025-11-21T18:09:46.6149590Z 7.1 If you use the Google TV Add-on to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources.
2025-11-21T18:09:46.6152930Z 
2025-11-21T18:09:46.6155750Z 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners.
2025-11-21T18:09:46.6162070Z 
2025-11-21T18:09:46.6167650Z 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, this License Agreement does not affect your legal relationship with these third parties.
2025-11-21T18:09:46.6170420Z 
2025-11-21T18:09:46.6172650Z 8. Using Google TV APIs
2025-11-21T18:09:46.6176040Z 
2025-11-21T18:09:46.6180200Z 8.1 If you use any Google TV API to retrieve data from Google, you acknowledge that the data (“Google TV API Content”) may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service. Some portions of the Google TV API Content are licensed to Google by third parties, including but not limited to Tribune Media Services
2025-11-21T18:09:46.6184220Z 
2025-11-21T18:09:46.6186590Z 8.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-21T18:09:46.6190320Z 
2025-11-21T18:09:46.6192610Z 8.3 Except as explicitly permitted in Section 3 (Google TV Add-on License from Google), you must:
2025-11-21T18:09:46.6194810Z 
2025-11-21T18:09:46.6207960Z (a) not modify nor format the Google TV API Content except to the extent reasonably and technically necessary to optimize the display such Google TV API Content in your application;
2025-11-21T18:09:46.6222320Z 
2025-11-21T18:09:46.6225250Z (b) not edit the Google TV API Content in a manner that renders the Google TV API Content inaccurate of alters its inherent meaning (provided that displaying excerpts will not violate the foregoing); or
2025-11-21T18:09:46.6232160Z 
2025-11-21T18:09:46.6234220Z (c) not create any commercial audience measurement tool or service using the Google TV API Content
2025-11-21T18:09:46.6236900Z 
2025-11-21T18:09:46.6238830Z 9. Terminating this License Agreement
2025-11-21T18:09:46.6240990Z 
2025-11-21T18:09:46.6243030Z 9.1 This License Agreement will continue to apply until terminated by either you or Google as set out below.
2025-11-21T18:09:46.6245100Z 
2025-11-21T18:09:46.6247220Z 9.2 If you want to terminate this License Agreement, you may do so by ceasing your use of the Google TV Add-on and any relevant developer credentials.
2025-11-21T18:09:46.6249990Z 
2025-11-21T18:09:46.6252570Z 9.3 Google may at any time, terminate this License Agreement with you if:
2025-11-21T18:09:46.6256860Z 
2025-11-21T18:09:46.6258980Z (A) you have breached any provision of this License Agreement; or
2025-11-21T18:09:46.6261930Z 
2025-11-21T18:09:46.6264300Z (B) Google is required to do so by law; or
2025-11-21T18:09:46.6267280Z 
2025-11-21T18:09:46.6271330Z (C) the partner with whom Google offered certain parts of Google TV Add-on (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the Google TV Add-on to you; or
2025-11-21T18:09:46.6274710Z 
2025-11-21T18:09:46.6277070Z (D) Google decides to no longer providing the Google TV Add-on or certain parts of the Google TV Add-on to users in the country in which you are resident or from which you use the service, or the provision of the Google TV Add-on or certain Google TV Add-on services to you by Google is, in Google's sole discretion, no longer commercially viable.
2025-11-21T18:09:46.6282220Z 
2025-11-21T18:09:46.6287810Z 9.4 When this License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst this License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.
2025-11-21T18:09:46.6292820Z 
2025-11-21T18:09:46.6294820Z 10. DISCLAIMER OF WARRANTIES
2025-11-21T18:09:46.6297400Z 
2025-11-21T18:09:46.6301130Z 10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE GOOGLE TV ADD-ON IS AT YOUR SOLE RISK AND THAT THE GOOGLE TV ADD-ON IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.
2025-11-21T18:09:46.6305140Z 
2025-11-21T18:09:46.6309570Z 10.2 YOUR USE OF THE GOOGLE TV ADD-ON AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE GOOGLE TV ADD-ON IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE.
2025-11-21T18:09:46.6312160Z 
2025-11-21T18:09:46.6313760Z 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
2025-11-21T18:09:46.6316100Z 
2025-11-21T18:09:46.6486110Z 11. LIMITATION OF LIABILITY
2025-11-21T18:09:46.6582900Z 
2025-11-21T18:09:46.6585700Z 11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.
2025-11-21T18:09:46.6594870Z 
2025-11-21T18:09:46.6596170Z 12. Indemnification
2025-11-21T18:09:46.6598070Z 
2025-11-21T18:09:46.6602480Z 12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the Google TV Add-on, (b) any application you develop on the Google TV Add-on that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with this License Agreement.
2025-11-21T18:09:46.6605950Z 
2025-11-21T18:09:46.6608100Z 13. Changes to the License Agreement
2025-11-21T18:09:46.6610210Z 
2025-11-21T18:09:46.6612150Z 13.1 Google may make changes to the License Agreement as it distributes new versions of the Google TV Add-on.
2025-11-21T18:09:46.6614220Z 
2025-11-21T18:09:46.6616040Z 14. General Legal Terms
2025-11-21T18:09:46.6618800Z 
2025-11-21T18:09:46.6621720Z 14.1 This License Agreement constitute the whole legal agreement between you and Google and govern your use of the Google TV Add-on (excluding any services which Google may provide to you under a separate written agreement), and completely replace any prior agreements between you and Google in relation to the Google TV Add-on.
2025-11-21T18:09:46.6624790Z 
2025-11-21T18:09:46.6627480Z 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in this License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.
2025-11-21T18:09:46.6632050Z 
2025-11-21T18:09:46.6634920Z 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of this License Agreement is invalid, then that provision will be removed from this License Agreement without affecting the rest of this License Agreement. The remaining provisions of this License Agreement will continue to be valid and enforceable.
2025-11-21T18:09:46.6638670Z 
2025-11-21T18:09:46.6642560Z 14.4 You acknowledge and agree that Google’s API data licensors and each member of the group of companies of which Google is the parent shall be third party beneficiaries to this License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of this License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to this License Agreement.
2025-11-21T18:09:46.6647130Z 
2025-11-21T18:09:46.6652390Z 14.5 EXPORT RESTRICTIONS. THE GOOGLE TV ADD-ON IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE GOOGLE TV ADD-ON. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.
2025-11-21T18:09:46.6716060Z 
2025-11-21T18:09:46.6719740Z 14.6 The rights granted in this License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under this License Agreement without the prior written approval of the other party.
2025-11-21T18:09:46.6723380Z 
2025-11-21T18:09:46.6727090Z 14.7 This License Agreement, and your relationship with Google under this License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from this License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.
2025-11-21T18:09:46.6731640Z 
2025-11-21T18:09:46.6733260Z 
2025-11-21T18:09:46.6736140Z August 15, 2011
2025-11-21T18:09:46.6739090Z ---------------------------------------
2025-11-21T18:09:46.6743230Z Accept? (y/N): 
2025-11-21T18:09:46.6746700Z 2/6: License android-googlexr-license:
2025-11-21T18:09:46.6747990Z ---------------------------------------
2025-11-21T18:09:46.6751770Z To get started with the Android XR Emulator System Image SDK, you must agree to the following terms and conditions. As described below, please note that this is a preview, emulated version of the Android XR OS, subject to change, that you use at your own risk.
2025-11-21T18:09:46.6754390Z 
2025-11-21T18:09:46.6758420Z This is the Android XR Emulator System Image SDK License Agreement
2025-11-21T18:09:46.6761020Z 
2025-11-21T18:09:46.6763450Z 1. Introduction
2025-11-21T18:09:46.6766350Z 
2025-11-21T18:09:46.6771990Z 1.1 The Android Android XR Emulator System Image SDK (referred to in the License Agreement as the "SDK" and specifically including the Android system files,, packaged APIs, library files (if and when they are made available), and Google applications and APIs add-ons) is licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of the SDK.
2025-11-21T18:09:46.6774980Z 
2025-11-21T18:09:46.6776840Z 1.2 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.
2025-11-21T18:09:46.6780090Z 
2025-11-21T18:09:46.6782420Z 1.3 "Google" means Google LLC, organized under the laws of the State of Delaware, USA, and operating under the laws of the USA with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA.
2025-11-21T18:09:46.6785360Z 
2025-11-21T18:09:46.6787630Z 2. Accepting this License Agreement
2025-11-21T18:09:46.6790350Z 
2025-11-21T18:09:46.6792280Z 2.1 In order to use the SDK, you must first agree to the License Agreement. You may not use the SDK if you do not accept the License Agreement.
2025-11-21T18:09:46.6794530Z 
2025-11-21T18:09:46.6796760Z 2.2 By clicking to accept and/or using this SDK, you hereby agree to the terms of the License Agreement.
2025-11-21T18:09:46.6800060Z 
2025-11-21T18:09:46.6802470Z 2.3 You may not use the SDK and may not accept the License Agreement if you are a person barred from receiving the SDK under the laws of the United States or other countries, including the country in which you are resident or from which you use the SDK.
2025-11-21T18:09:46.6804910Z 
2025-11-21T18:09:46.6807470Z 2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the SDK on behalf of your employer or other entity.
2025-11-21T18:09:46.6811290Z 
2025-11-21T18:09:46.6813350Z 3. SDK License from Google
2025-11-21T18:09:46.6815280Z 
2025-11-21T18:09:46.6817440Z 3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use the SDK solely to develop applications for Android XR.
2025-11-21T18:09:46.6820780Z 
2025-11-21T18:09:46.6822940Z 3.2 You may not use this SDK to develop applications for other platforms or to develop another SDK. You are of course free to develop applications for other platforms provided that this SDK is not used for that purpose.
2025-11-21T18:09:46.6825190Z 
2025-11-21T18:09:46.6829710Z 3.3 You agree that Google or third parties own all legal right, title and interest in and to the SDK, including any Intellectual Property Rights that subsist in the SDK. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.
2025-11-21T18:09:46.6832880Z 
2025-11-21T18:09:46.6835760Z 3.4 You may not use the SDK for any purpose not expressly permitted by the License Agreement. Except to the extent required by applicable third party licenses, you may not (a) copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the SDK or any part of the SDK; or (b) load any part of the SDK onto a mobile handset or any other hardware device except a personal computer, combine any part of the SDK with other software, or distribute any software or device incorporating a part of the SDK.
2025-11-21T18:09:46.6840850Z 
2025-11-21T18:09:46.6843400Z 3.5 Use, reproduction and distribution of components of the SDK licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement. You agree to remain a licensee in good standing in regard to such open source software licenses under all the rights granted and to refrain from any actions that may terminate, suspend, or breach such rights.
2025-11-21T18:09:46.6846930Z 
2025-11-21T18:09:46.6849960Z 3.6 You agree that the form and nature of the SDK that Google provides may change without prior notice to you and that future versions of the SDK may be incompatible with applications developed on previous versions of the SDK. You agree that Google may stop (permanently or temporarily) providing the SDK (or any features within the SDK) to you or to users generally at Google's sole discretion, without prior notice to you.
2025-11-21T18:09:46.6852850Z 
2025-11-21T18:09:46.6855380Z 3.7 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.
2025-11-21T18:09:46.6858610Z 
2025-11-21T18:09:46.6861180Z 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the SDK.
2025-11-21T18:09:46.6863830Z 
2025-11-21T18:09:46.6865560Z 4. Use of the SDK by You
2025-11-21T18:09:46.6867980Z 
2025-11-21T18:09:46.6870910Z 4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you develop using the SDK, including any intellectual property rights that subsist in those applications.
2025-11-21T18:09:46.6874170Z 
2025-11-21T18:09:46.6876470Z 4.2 You agree to use the SDK and write applications only for purposes that are permitted by (a) the License Agreement and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).
2025-11-21T18:09:46.6881830Z 
2025-11-21T18:09:46.6885050Z 4.3 You agree that if you use the SDK to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-21T18:09:46.6890800Z 
2025-11-21T18:09:46.6898740Z 4.4 You agree that you will not engage in any activity with the SDK, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier.
2025-11-21T18:09:46.6914030Z 
2025-11-21T18:09:46.6918440Z 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.
2025-11-21T18:09:46.6931950Z 
2025-11-21T18:09:46.6934930Z 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.
2025-11-21T18:09:46.6938740Z 
2025-11-21T18:09:46.6941290Z 4.7 The SDK is in development, and your testing and feedback are an important part of the development process. By using the SDK, you acknowledge that implementation of some features are still under development and that you should not rely on the SDK having the full functionality of a stable release.
2025-11-21T18:09:46.6944000Z 
2025-11-21T18:09:46.6945970Z 5. Your Developer Credentials
2025-11-21T18:09:46.6948060Z 
2025-11-21T18:09:46.6950610Z 5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.
2025-11-21T18:09:46.6953060Z 
2025-11-21T18:09:46.6955320Z 6. Privacy and Information
2025-11-21T18:09:46.6957250Z 
2025-11-21T18:09:46.6959810Z 6.1 In order to continually innovate and improve the SDK, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the SDK are being used and how they are being used. Before any of this information is collected, the SDK will notify you and seek your consent. If you withhold consent, the information will not be collected.
2025-11-21T18:09:46.6962650Z 
2025-11-21T18:09:46.6969880Z 6.2 The data collected is examined in the aggregate to improve the SDK and is maintained in accordance with Google's Privacy Policy, which is located at the following URL: https://policies.google.com/privacy
2025-11-21T18:09:46.6975800Z 
2025-11-21T18:09:46.6978570Z 6.3 Anonymized and aggregated sets of the data may be shared with Google partners to improve the SDK.
2025-11-21T18:09:46.6981710Z 
2025-11-21T18:09:46.6983820Z 7. Third Party Applications
2025-11-21T18:09:46.6988490Z 
2025-11-21T18:09:46.6993270Z 7.1 If you use the SDK to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources.
2025-11-21T18:09:46.7000090Z 
2025-11-21T18:09:46.7003380Z 7.2 You should be aware that the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners.
2025-11-21T18:09:46.7007420Z 
2025-11-21T18:09:46.7009840Z 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, the License Agreement does not affect your legal relationship with these third parties.
2025-11-21T18:09:46.7012520Z 
2025-11-21T18:09:46.7014570Z 8. Using Android APIs
2025-11-21T18:09:46.7017600Z 
2025-11-21T18:09:46.7019420Z 8.1 Google Data APIs
2025-11-21T18:09:46.7021570Z 
2025-11-21T18:09:46.7024910Z 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service.
2025-11-21T18:09:46.7031950Z 
2025-11-21T18:09:46.7038340Z 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so. If you use the Android Recognition Service API, documented at the following URL: https://developer.android.com/reference/android/speech/RecognitionService, as updated from time to time, you acknowledge that the use of the API is subject to the Data Processing Addendum for Products where Google is a Data Processor, which is located at the following URL: https://privacy.google.com/businesses/gdprprocessorterms/, as updated from time to time. By clicking to accept, you hereby agree to the terms of the Data Processing Addendum for Products where Google is a Data Processor.
2025-11-21T18:09:46.7046010Z 
2025-11-21T18:09:46.7047820Z 9. Terminating this License Agreement
2025-11-21T18:09:46.7050120Z 
2025-11-21T18:09:46.7052380Z 9.1 The License Agreement will continue to apply until terminated by either you or Google as set out below.
2025-11-21T18:09:46.7054890Z 
2025-11-21T18:09:46.7059710Z 9.2 If you want to terminate the License Agreement, you may do so by ceasing your use of the SDK and any relevant developer credentials.
2025-11-21T18:09:46.7061880Z 
2025-11-21T18:09:46.7065130Z 9.3 Google may at any time, terminate the License Agreement with you if: (A) you have breached any provision of the License Agreement; or (B) Google is required to do so by law; or (C) the partner with whom Google offered certain parts of SDK (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the SDK to you; or (D) Google decides to no longer provide the SDK or certain parts of the SDK to users in the country in which you are resident or from which you use the service, or the provision of the SDK or certain SDK services to you by Google is, in Google's sole discretion, no longer commercially viable.
2025-11-21T18:09:46.7068600Z 
2025-11-21T18:09:46.7071340Z 9.4 When the License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst the License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.
2025-11-21T18:09:46.7075440Z 
2025-11-21T18:09:46.7077920Z 10. DISCLAIMER OF WARRANTIES
2025-11-21T18:09:46.7080720Z 
2025-11-21T18:09:46.7083420Z 10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE SDK IS AT YOUR SOLE RISK AND THAT THE SDK IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.
2025-11-21T18:09:46.7085520Z 
2025-11-21T18:09:46.7087820Z 10.2 YOUR USE OF THE SDK AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE SDK IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE.
2025-11-21T18:09:46.7090090Z 
2025-11-21T18:09:46.7092520Z 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
2025-11-21T18:09:46.7096550Z 
2025-11-21T18:09:46.7098640Z 11. LIMITATION OF LIABILITY
2025-11-21T18:09:46.7100420Z 
2025-11-21T18:09:46.7103140Z 11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.
2025-11-21T18:09:46.7105820Z 
2025-11-21T18:09:46.7107720Z 12. Indemnification
2025-11-21T18:09:46.7109550Z 
2025-11-21T18:09:46.7112850Z 12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the SDK, (b) any application you develop on the SDK that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with the License Agreement.
2025-11-21T18:09:46.7116000Z 
2025-11-21T18:09:46.7117890Z 13. Changes to the License Agreement
2025-11-21T18:09:46.7119720Z 
2025-11-21T18:09:46.7126630Z 13.1 Google may make changes to the License Agreement as it distributes new versions of the SDK. When these changes are made, Google will make a new version of the License Agreement available on the website where the SDK is made available.
2025-11-21T18:09:46.7131820Z 
2025-11-21T18:09:46.7134380Z 14. General Legal Terms
2025-11-21T18:09:46.7137030Z 
2025-11-21T18:09:46.7139360Z 14.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of the SDK (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the SDK.
2025-11-21T18:09:46.7141530Z 
2025-11-21T18:09:46.7143640Z 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.
2025-11-21T18:09:46.7147990Z 
2025-11-21T18:09:46.7150550Z 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable.
2025-11-21T18:09:46.7153580Z 
2025-11-21T18:09:46.7156310Z 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement.
2025-11-21T18:09:46.7158960Z 
2025-11-21T18:09:46.7161450Z 14.5 EXPORT RESTRICTIONS. THE SDK IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE SDK. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.
2025-11-21T18:09:46.7163710Z 
2025-11-21T18:09:46.7166210Z 14.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party.
2025-11-21T18:09:46.7168700Z 
2025-11-21T18:09:46.7171630Z 14.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.
2025-11-21T18:09:46.7174800Z ---------------------------------------
2025-11-21T18:09:46.7176800Z Accept? (y/N): 
2025-11-21T18:09:46.7179000Z 3/6: License android-sdk-arm-dbt-license:
2025-11-21T18:09:46.7181000Z ---------------------------------------
2025-11-21T18:09:46.7183140Z Terms and Conditions
2025-11-21T18:09:46.7184750Z 
2025-11-21T18:09:46.7186930Z This is the Android Software Development Kit License Agreement
2025-11-21T18:09:46.7188630Z 
2025-11-21T18:09:46.7190620Z 1. Introduction
2025-11-21T18:09:46.7195370Z 
2025-11-21T18:09:46.7201120Z 1.1 The Android Software Development Kit (referred to in the License Agreement as the "SDK" and specifically including the Android system files, packaged APIs, and Google APIs add-ons) is licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of the SDK.
2025-11-21T18:09:46.7204160Z 
2025-11-21T18:09:46.7207010Z 1.2 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: http://source.android.com/, as updated from time to time.
2025-11-21T18:09:46.7210520Z 
2025-11-21T18:09:46.7213160Z 1.3 A "compatible implementation" means any Android device that (i) complies with the Android Compatibility Definition document, which can be found at the Android compatibility website (http://source.android.com/compatibility) and which may be updated from time to time; and (ii) successfully passes the Android Compatibility Test Suite (CTS).
2025-11-21T18:09:46.7226700Z 
2025-11-21T18:09:46.7229760Z 1.4 "Google" means Google Inc., a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.
2025-11-21T18:09:46.7231840Z 
2025-11-21T18:09:46.7234710Z 
2025-11-21T18:09:46.7237000Z 2. Accepting the License Agreement
2025-11-21T18:09:46.7239270Z 
2025-11-21T18:09:46.7243540Z 2.1 In order to use the SDK, you must first agree to the License Agreement. You may not use the SDK if you do not accept the License Agreement.
2025-11-21T18:09:46.7246640Z 
2025-11-21T18:09:46.7249020Z 2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.
2025-11-21T18:09:46.7252530Z 
2025-11-21T18:09:46.7256310Z 2.3 You may not use the SDK and may not accept the License Agreement if you are a person barred from receiving the SDK under the laws of the United States or other countries, including the country in which you are resident or from which you use the SDK.
2025-11-21T18:09:46.7259170Z 
2025-11-21T18:09:46.7265490Z 2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the SDK on behalf of your employer or other entity.
2025-11-21T18:09:46.7269470Z 
2025-11-21T18:09:46.7271050Z 
2025-11-21T18:09:46.7273230Z 3. SDK License from Google
2025-11-21T18:09:46.7274880Z 
2025-11-21T18:09:46.7278400Z 3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use the SDK solely to develop applications for compatible implementations of Android.
2025-11-21T18:09:46.7281610Z 
2025-11-21T18:09:46.7284560Z 3.2 You may not use this SDK to develop applications for other platforms (including non-compatible implementations of Android) or to develop another SDK. You are of course free to develop applications for other platforms, including non-compatible implementations of Android, provided that this SDK is not used for that purpose.
2025-11-21T18:09:46.7286850Z 
2025-11-21T18:09:46.7289630Z 3.3 You agree that Google or third parties own all legal right, title and interest in and to the SDK, including any Intellectual Property Rights that subsist in the SDK. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.
2025-11-21T18:09:46.7292010Z 
2025-11-21T18:09:46.7294690Z 3.4 You may not use the SDK for any purpose not expressly permitted by the License Agreement. Except to the extent required by applicable third party licenses, you may not copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the SDK or any part of the SDK.
2025-11-21T18:09:46.7296970Z 
2025-11-21T18:09:46.7299860Z 3.5 Use, reproduction and distribution of components of the SDK licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement.
2025-11-21T18:09:46.7301900Z 
2025-11-21T18:09:46.7304690Z 3.6 You agree that the form and nature of the SDK that Google provides may change without prior notice to you and that future versions of the SDK may be incompatible with applications developed on previous versions of the SDK. You agree that Google may stop (permanently or temporarily) providing the SDK (or any features within the SDK) to you or to users generally at Google's sole discretion, without prior notice to you.
2025-11-21T18:09:46.7307090Z 
2025-11-21T18:09:46.7309440Z 3.7 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.
2025-11-21T18:09:46.7311770Z 
2025-11-21T18:09:46.7314000Z 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the SDK.
2025-11-21T18:09:46.7316050Z 
2025-11-21T18:09:46.7317690Z 
2025-11-21T18:09:46.7320280Z 4. Use of the SDK by You
2025-11-21T18:09:46.7321930Z 
2025-11-21T18:09:46.7325260Z 4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you develop using the SDK, including any intellectual property rights that subsist in those applications.
2025-11-21T18:09:46.7327560Z 
2025-11-21T18:09:46.7329710Z 4.2 You agree to use the SDK and write applications only for purposes that are permitted by (a) the License Agreement and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).
2025-11-21T18:09:46.7330930Z 
2025-11-21T18:09:46.7333870Z 4.3 You agree that if you use the SDK to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-21T18:09:46.7335930Z 
2025-11-21T18:09:46.7338230Z 4.4 You agree that you will not engage in any activity with the SDK, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier.
2025-11-21T18:09:46.7339500Z 
2025-11-21T18:09:46.7341660Z 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.
2025-11-21T18:09:46.7342900Z 
2025-11-21T18:09:46.7345150Z 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.
2025-11-21T18:09:46.7346570Z 
2025-11-21T18:09:46.7350050Z 4.7 This software enables the execution of intellectual property owned by Arm Limited. You agree that your use of the software, that allows execution of ARM Instruction Set Architecture (“ISA”) compliant executables for application development and debug only on x86 desktop, laptop, customer on-premise servers, and customer-procured cloud-based environments.
2025-11-21T18:09:46.7351430Z 
2025-11-21T18:09:46.7353110Z 5. Your Developer Credentials
2025-11-21T18:09:46.7355180Z 
2025-11-21T18:09:46.7357310Z 5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.
2025-11-21T18:09:46.7360280Z 
2025-11-21T18:09:46.7362170Z 6. Privacy and Information
2025-11-21T18:09:46.7362790Z 
2025-11-21T18:09:46.7365180Z 6.1 In order to continually innovate and improve the SDK, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the SDK are being used and how they are being used. Before any of this information is collected, the SDK will notify you and seek your consent. If you withhold consent, the information will not be collected.
2025-11-21T18:09:46.7367230Z 
2025-11-21T18:09:46.7369510Z 6.2 The data collected is examined in the aggregate to improve the SDK and is maintained in accordance with Google's Privacy Policy.
2025-11-21T18:09:46.7371800Z 
2025-11-21T18:09:46.7373520Z 
2025-11-21T18:09:46.7375620Z 7. Third Party Applications
2025-11-21T18:09:46.7381160Z 
2025-11-21T18:09:46.7384960Z 7.1 If you use the SDK to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources.
2025-11-21T18:09:46.7386750Z 
2025-11-21T18:09:46.7389220Z 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners.
2025-11-21T18:09:46.7390600Z 
2025-11-21T18:09:46.7399390Z 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, the License Agreement does not affect your legal relationship with these third parties.
2025-11-21T18:09:46.9327070Z 
2025-11-21T18:09:46.9328410Z 
2025-11-21T18:09:46.9330800Z 8. Using Android APIs
2025-11-21T18:09:46.9331760Z 
2025-11-21T18:09:46.9334060Z 8.1 Google Data APIs
2025-11-21T18:09:46.9334720Z 
2025-11-21T18:09:46.9339010Z 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service.
2025-11-21T18:09:46.9345840Z 
2025-11-21T18:09:46.9350600Z 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so. If you use the Android Recognition Service API, documented at the following URL: https://developer.android.com/reference/android/speech/RecognitionService, as updated from time to time, you acknowledge that the use of the API is subject to the Data Processing Addendum for Products where Google is a Data Processor, which is located at the following URL: https://privacy.google.com/businesses/gdprprocessorterms/, as updated from time to time. By clicking to accept, you hereby agree to the terms of the Data Processing Addendum for Products where Google is a Data Processor.
2025-11-21T18:09:46.9355740Z 
2025-11-21T18:09:46.9357350Z 
2025-11-21T18:09:46.9360460Z 9. Terminating the License Agreement
2025-11-21T18:09:46.9360870Z 
2025-11-21T18:09:46.9366250Z 9.1 The License Agreement will continue to apply until terminated by either you or Google as set out below.
2025-11-21T18:09:46.9369400Z 
2025-11-21T18:09:46.9371390Z 9.2 If you want to terminate the License Agreement, you may do so by ceasing your use of the SDK and any relevant developer credentials.
2025-11-21T18:09:46.9384470Z 
2025-11-21T18:09:46.9388410Z 9.3 Google may at any time, terminate the License Agreement with you if: (A) you have breached any provision of the License Agreement; or (B) Google is required to do so by law; or (C) the partner with whom Google offered certain parts of SDK (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the SDK to you; or (D) Google decides to no longer provide the SDK or certain parts of the SDK to users in the country in which you are resident or from which you use the service, or the provision of the SDK or certain SDK services to you by Google is, in Google's sole discretion, no longer commercially viable.
2025-11-21T18:09:46.9392470Z 
2025-11-21T18:09:46.9395140Z 9.4 When the License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst the License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.
2025-11-21T18:09:46.9406510Z 
2025-11-21T18:09:46.9408330Z 
2025-11-21T18:09:46.9411600Z 10. DISCLAIMER OF WARRANTIES
2025-11-21T18:09:46.9412680Z 
2025-11-21T18:09:46.9414810Z 10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE SDK IS AT YOUR SOLE RISK AND THAT THE SDK IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.
2025-11-21T18:09:46.9417130Z 
2025-11-21T18:09:46.9419510Z 10.2 YOUR USE OF THE SDK AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE SDK IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE.
2025-11-21T18:09:46.9420900Z 
2025-11-21T18:09:46.9423070Z 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
2025-11-21T18:09:46.9424320Z 
2025-11-21T18:09:46.9426060Z 
2025-11-21T18:09:46.9428840Z 11. LIMITATION OF LIABILITY
2025-11-21T18:09:46.9430230Z 
2025-11-21T18:09:46.9435540Z 11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.
2025-11-21T18:09:46.9437230Z 
2025-11-21T18:09:46.9439190Z 
2025-11-21T18:09:46.9441790Z 12. Indemnification
2025-11-21T18:09:46.9443070Z 
2025-11-21T18:09:46.9446940Z 12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the SDK, (b) any application you develop on the SDK that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with the License Agreement.
2025-11-21T18:09:46.9449540Z 
2025-11-21T18:09:46.9451290Z 
2025-11-21T18:09:46.9454110Z 13. Changes to the License Agreement
2025-11-21T18:09:46.9455080Z 
2025-11-21T18:09:46.9458140Z 13.1 Google may make changes to the License Agreement as it distributes new versions of the SDK. When these changes are made, Google will make a new version of the License Agreement available on the website where the SDK is made available.
2025-11-21T18:09:46.9461220Z 
2025-11-21T18:09:46.9462440Z 
2025-11-21T18:09:46.9465140Z 14. General Legal Terms
2025-11-21T18:09:46.9466100Z 
2025-11-21T18:09:46.9469310Z 14.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of the SDK (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the SDK.
2025-11-21T18:09:46.9472210Z 
2025-11-21T18:09:46.9474610Z 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.
2025-11-21T18:09:46.9475710Z 
2025-11-21T18:09:46.9478660Z 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable.
2025-11-21T18:09:46.9481140Z 
2025-11-21T18:09:46.9483980Z 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement.
2025-11-21T18:09:46.9487770Z 
2025-11-21T18:09:46.9490640Z 14.5 EXPORT RESTRICTIONS. THE SDK IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE SDK. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.
2025-11-21T18:09:46.9495090Z 
2025-11-21T18:09:46.9498050Z 14.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party.
2025-11-21T18:09:46.9542460Z 
2025-11-21T18:09:46.9549960Z 14.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.
2025-11-21T18:09:46.9553580Z 
2025-11-21T18:09:46.9555500Z 
2025-11-21T18:09:46.9559240Z January 16, 2019
2025-11-21T18:09:46.9562540Z ---------------------------------------
2025-11-21T18:09:46.9565420Z Accept? (y/N): 
2025-11-21T18:09:46.9568150Z 4/6: License android-sdk-preview-license:
2025-11-21T18:09:46.9570870Z ---------------------------------------
2025-11-21T18:09:46.9574460Z To get started with the Android SDK Preview, you must agree to the following terms and conditions. As described below, please note that this is a preview version of the Android SDK, subject to change, that you use at your own risk. The Android SDK Preview is not a stable release, and may contain errors and defects that can result in serious damage to your computer systems, devices and data.
2025-11-21T18:09:46.9578950Z 
2025-11-21T18:09:46.9581200Z This is the Android SDK Preview License Agreement (the "License Agreement").
2025-11-21T18:09:46.9583730Z 
2025-11-21T18:09:46.9586580Z 1. Introduction
2025-11-21T18:09:46.9588850Z 
2025-11-21T18:09:46.9592300Z 1.1 The Android SDK Preview (referred to in the License Agreement as the “Preview” and specifically including the Android system files, packaged APIs, and Preview library files, if and when they are made available) is licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of the Preview.
2025-11-21T18:09:46.9595280Z 
2025-11-21T18:09:46.9597620Z 1.2 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: http://source.android.com/, as updated from time to time.
2025-11-21T18:09:46.9601530Z 
2025-11-21T18:09:46.9604180Z 1.3 "Google" means Google Inc., a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.
2025-11-21T18:09:46.9605270Z 
2025-11-21T18:09:46.9607860Z 2. Accepting the License Agreement
2025-11-21T18:09:46.9610150Z 
2025-11-21T18:09:46.9612540Z 2.1 In order to use the Preview, you must first agree to the License Agreement. You may not use the Preview if you do not accept the License Agreement.
2025-11-21T18:09:46.9614980Z 
2025-11-21T18:09:46.9617830Z 2.2 By clicking to accept and/or using the Preview, you hereby agree to the terms of the License Agreement.
2025-11-21T18:09:46.9620200Z 
2025-11-21T18:09:46.9623010Z 2.3 You may not use the Preview and may not accept the License Agreement if you are a person barred from receiving the Preview under the laws of the United States or other countries including the country in which you are resident or from which you use the Preview.
2025-11-21T18:09:46.9625690Z 
2025-11-21T18:09:46.9628580Z 2.4 If you will use the Preview internally within your company or organization you agree to be bound by the License Agreement on behalf of your employer or other entity, and you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the Preview on behalf of your employer or other entity.
2025-11-21T18:09:46.9632340Z 
2025-11-21T18:09:46.9634230Z 3. Preview License from Google
2025-11-21T18:09:46.9636890Z 
2025-11-21T18:09:46.9639200Z 3.1 Subject to the terms of the License Agreement, Google grants you a royalty-free, non-assignable, non-exclusive, non-sublicensable, limited, revocable license to use the Preview, personally or internally within your company or organization, solely to develop applications to run on the Android platform.
2025-11-21T18:09:46.9642420Z 
2025-11-21T18:09:46.9644870Z 3.2 You agree that Google or third parties owns all legal right, title and interest in and to the Preview, including any Intellectual Property Rights that subsist in the Preview. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.
2025-11-21T18:09:46.9647300Z 
2025-11-21T18:09:46.9650000Z 3.3 You may not use the Preview for any purpose not expressly permitted by the License Agreement. Except to the extent required by applicable third party licenses, you may not: (a) copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the Preview or any part of the Preview; or (b) load any part of the Preview onto a mobile handset or any other hardware device except a personal computer, combine any part of the Preview with other software, or distribute any software or device incorporating a part of the Preview.
2025-11-21T18:09:46.9653280Z 
2025-11-21T18:09:46.9655670Z 3.4 You agree that you will not take any actions that may cause or result in the fragmentation of Android, including but not limited to distributing, participating in the creation of, or promoting in any way a software development kit derived from the Preview.
2025-11-21T18:09:46.9657710Z 
2025-11-21T18:09:46.9660490Z 3.5 Use, reproduction and distribution of components of the Preview licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement. You agree to remain a licensee in good standing in regard to such open source software licenses under all the rights granted and to refrain from any actions that may terminate, suspend, or breach such rights.
2025-11-21T18:09:46.9664620Z 
2025-11-21T18:09:46.9667490Z 3.6 You agree that the form and nature of the Preview that Google provides may change without prior notice to you and that future versions of the Preview may be incompatible with applications developed on previous versions of the Preview. You agree that Google may stop (permanently or temporarily) providing the Preview (or any features within the Preview) to you or to users generally at Google's sole discretion, without prior notice to you.
2025-11-21T18:09:46.9671010Z 
2025-11-21T18:09:46.9673270Z 3.7 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.
2025-11-21T18:09:46.9675160Z 
2025-11-21T18:09:46.9677050Z 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the Preview.
2025-11-21T18:09:46.9678960Z 
2025-11-21T18:09:46.9680590Z 4. Use of the Preview by You
2025-11-21T18:09:46.9682160Z 
2025-11-21T18:09:46.9684270Z 4.1 Google agrees that nothing in the License Agreement gives Google any right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you develop using the Preview, including any intellectual property rights that subsist in those applications.
2025-11-21T18:09:46.9687510Z 
2025-11-21T18:09:46.9691000Z 4.2 You agree to use the Preview and write applications only for purposes that are permitted by (a) the License Agreement, and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).
2025-11-21T18:09:46.9694930Z 
2025-11-21T18:09:46.9699250Z 4.3 You agree that if you use the Preview to develop applications, you will protect the privacy and legal rights of users. If users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If users provide you with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, each user has given you permission to do so.
2025-11-21T18:09:46.9703750Z 
2025-11-21T18:09:46.9706190Z 4.4 You agree that you will not engage in any activity with the Preview, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of Google or any third party.
2025-11-21T18:09:46.9708880Z 
2025-11-21T18:09:46.9711740Z 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.
2025-11-21T18:09:46.9714250Z 
2025-11-21T18:09:46.9716660Z 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.
2025-11-21T18:09:46.9719210Z 
2025-11-21T18:09:46.9721760Z 4.7 The Preview is in development, and your testing and feedback are an important part of the development process. By using the Preview, you acknowledge that implementation of some features are still under development and that you should not rely on the Preview having the full functionality of a stable release. You agree not to publicly distribute or ship any application using this Preview as this Preview will no longer be supported after the official Android SDK is released.
2025-11-21T18:09:46.9724650Z 
2025-11-21T18:09:46.9726690Z 5. Your Developer Credentials
2025-11-21T18:09:46.9730040Z 
2025-11-21T18:09:46.9732590Z 5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.
2025-11-21T18:09:46.9734840Z 
2025-11-21T18:09:46.9736460Z 6. Privacy and Information
2025-11-21T18:09:46.9738100Z 
2025-11-21T18:09:46.9741510Z 6.1 In order to continually innovate and improve the Preview, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the Preview are being used and how they are being used. Before any of this information is collected, the Preview will notify you and seek your consent. If you withhold consent, the information will not be collected.
2025-11-21T18:09:46.9744910Z 
2025-11-21T18:09:46.9747430Z 6.2 The data collected is examined in the aggregate to improve the Preview and is maintained in accordance with Google's Privacy Policy located at http://www.google.com/policies/privacy/.
2025-11-21T18:09:46.9749670Z 
2025-11-21T18:09:46.9751890Z 7. Third Party Applications
2025-11-21T18:09:46.9754040Z 
2025-11-21T18:09:46.9758170Z 7.1 If you use the Preview to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources.
2025-11-21T18:09:46.9762230Z 
2025-11-21T18:09:46.9765260Z 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners.
2025-11-21T18:09:46.9769560Z 
2025-11-21T18:09:46.9772040Z 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party.
2025-11-21T18:09:46.9775660Z 
2025-11-21T18:09:46.9778090Z 8. Using Google APIs
2025-11-21T18:09:46.9780680Z 
2025-11-21T18:09:46.9783250Z 8.1 Google APIs
2025-11-21T18:09:46.9785970Z 
2025-11-21T18:09:46.9788290Z 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service.
2025-11-21T18:09:46.9789850Z 
2025-11-21T18:09:46.9792580Z 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-21T18:09:46.9793650Z 
2025-11-21T18:09:46.9796460Z 9. Terminating the License Agreement
2025-11-21T18:09:46.9799550Z 
2025-11-21T18:09:46.9802570Z 9.1 the License Agreement will continue to apply until terminated by either you or Google as set out below.
2025-11-21T18:09:46.9803080Z 
2025-11-21T18:09:46.9806090Z 9.2 If you want to terminate the License Agreement, you may do so by ceasing your use of the Preview and any relevant developer credentials.
2025-11-21T18:09:46.9806900Z 
2025-11-21T18:09:46.9811940Z 9.3 Google may at any time, terminate the License Agreement, with or without cause, upon notice to you.
2025-11-21T18:09:46.9816030Z 
2025-11-21T18:09:46.9821700Z 9.4 The License Agreement will automatically terminate without notice or other action upon the earlier of: (A) when Google ceases to provide the Preview or certain parts of the Preview to users in the country in which you are resident or from which you use the service; and (B) Google issues a final release version of the Android SDK.
2025-11-21T18:09:46.9824140Z 
2025-11-21T18:09:46.9827030Z 9.5 When the License Agreement is terminated, the license granted to you in the License Agreement will terminate, you will immediately cease all use of the Preview, and the provisions of paragraphs 10, 11, 12 and 14 shall survive indefinitely.
2025-11-21T18:09:46.9830260Z 
2025-11-21T18:09:46.9832450Z 10. DISCLAIMERS
2025-11-21T18:09:46.9850340Z 
2025-11-21T18:09:46.9856980Z 10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE PREVIEW IS AT YOUR SOLE RISK AND THAT THE PREVIEW IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.
2025-11-21T18:09:46.9857720Z 
2025-11-21T18:09:46.9860210Z 10.2 YOUR USE OF THE PREVIEW AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE PREVIEW IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE. WITHOUT LIMITING THE FOREGOING, YOU UNDERSTAND THAT THE PREVIEW IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.
2025-11-21T18:09:46.9863870Z 
2025-11-21T18:09:46.9867350Z 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
2025-11-21T18:09:46.9868690Z 
2025-11-21T18:09:46.9870420Z 11. LIMITATION OF LIABILITY
2025-11-21T18:09:46.9871980Z 
2025-11-21T18:09:46.9875910Z 11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.
2025-11-21T18:09:46.9878300Z 
2025-11-21T18:09:46.9880480Z 12. Indemnification
2025-11-21T18:09:46.9881130Z 
2025-11-21T18:09:46.9884920Z 12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys’ fees) arising out of or accruing from (a) your use of the Preview, (b) any application you develop on the Preview that infringes any Intellectual Property Rights of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you of the License Agreement.
2025-11-21T18:09:46.9886900Z 
2025-11-21T18:09:46.9889070Z 13. Changes to the License Agreement
2025-11-21T18:09:46.9889410Z 
2025-11-21T18:09:46.9890270Z 13.1 Google may make changes to the License Agreement as it distributes new versions of the Preview. When these changes are made, Google will make a new version of the License Agreement available on the website where the Preview is made available.
2025-11-21T18:09:46.9891400Z 
2025-11-21T18:09:46.9891830Z 14. General Legal Terms
2025-11-21T18:09:46.9893200Z 
2025-11-21T18:09:46.9895020Z 14.1 the License Agreement constitutes the whole legal agreement between you and Google and governs your use of the Preview (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the Preview.
2025-11-21T18:09:46.9896730Z 
2025-11-21T18:09:46.9900130Z 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.
2025-11-21T18:09:46.9901070Z 
2025-11-21T18:09:46.9902530Z 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable.
2025-11-21T18:09:46.9903600Z 
2025-11-21T18:09:46.9905290Z 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement.
2025-11-21T18:09:46.9906330Z 
2025-11-21T18:09:46.9907230Z 14.5 EXPORT RESTRICTIONS. THE PREVIEW IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE PREVIEW. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.
2025-11-21T18:09:46.9907900Z 
2025-11-21T18:09:46.9909450Z 14.6 The License Agreement may not be assigned or transferred by you without the prior written approval of Google, and any attempted assignment without such approval will be void. You shall not delegate your responsibilities or obligations under the License Agreement without the prior written approval of Google.
2025-11-21T18:09:46.9910730Z 
2025-11-21T18:09:46.9914510Z 14.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.
2025-11-21T18:09:46.9917330Z 
2025-11-21T18:09:46.9919790Z June 2014.
2025-11-21T18:09:46.9920920Z ---------------------------------------
2025-11-21T18:09:46.9922450Z Accept? (y/N): 
2025-11-21T18:09:46.9924300Z 5/6: License google-gdk-license:
2025-11-21T18:09:46.9925680Z ---------------------------------------
2025-11-21T18:09:46.9927710Z This is a Developer Preview of the GDK that is subject to change.
2025-11-21T18:09:46.9929170Z 
2025-11-21T18:09:46.9931320Z Terms and Conditions
2025-11-21T18:09:46.9932620Z 
2025-11-21T18:09:46.9935420Z This is the Glass Development Kit License Agreement.
2025-11-21T18:09:46.9939920Z 
2025-11-21T18:09:46.9942760Z 1. Introduction
2025-11-21T18:09:46.9945260Z 
2025-11-21T18:09:46.9947960Z 1.1 The Glass Development Kit (referred to in this License Agreement as the "GDK" and specifically including the Android system files, packaged APIs, and GDK library files, if and when they are made available) is licensed to you subject to the terms of this License Agreement. This License Agreement forms a legally binding contract between you and Google in relation to your use of the GDK.
2025-11-21T18:09:46.9949610Z 
2025-11-21T18:09:46.9951650Z 1.2 "Glass" means Glass devices and the Glass software stack for use on Glass devices.
2025-11-21T18:09:46.9952410Z 
2025-11-21T18:09:46.9953600Z 
2025-11-21T18:09:46.9956750Z 1.3 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: http://source.android.com/, as updated from time to time.
2025-11-21T18:09:46.9958890Z 
2025-11-21T18:09:46.9961960Z 1.4 "Google" means Google Inc., a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.
2025-11-21T18:09:46.9962680Z 
2025-11-21T18:09:46.9963220Z 2. Accepting this License Agreement
2025-11-21T18:09:46.9964400Z 
2025-11-21T18:09:46.9966600Z 2.1 In order to use the GDK, you must first agree to this License Agreement. You may not use the GDK if you do not accept this License Agreement.
2025-11-21T18:09:46.9967240Z 
2025-11-21T18:09:46.9967970Z 2.2 By clicking to accept, you hereby agree to the terms of this License Agreement.
2025-11-21T18:09:46.9968300Z 
2025-11-21T18:09:46.9969120Z 2.3 You may not use the GDK and may not accept the License Agreement if you are a person barred from receiving the GDK under the laws of the United States or other countries including the country in which you are resident or from which you use the GDK.
2025-11-21T18:09:46.9969730Z 
2025-11-21T18:09:46.9970780Z 2.4 If you are agreeing to be bound by this License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to this License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the GDK on behalf of your employer or other entity.
2025-11-21T18:09:46.9971660Z 
2025-11-21T18:09:46.9972030Z 3. GDK License from Google
2025-11-21T18:09:46.9972210Z 
2025-11-21T18:09:46.9973000Z 3.1 Subject to the terms of this License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable and non-exclusive license to use the GDK solely to develop applications to run on the Glass platform for Glass devices.
2025-11-21T18:09:46.9973610Z 
2025-11-21T18:09:46.9974730Z 3.2 You agree that Google or third parties own all legal right, title and interest in and to the GDK, including any Intellectual Property Rights that subsist in the GDK. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.
2025-11-21T18:09:46.9976780Z 
2025-11-21T18:09:46.9981170Z 3.3 You may not use the GDK for any purpose not expressly permitted by this License Agreement. Except to the extent required by applicable third party licenses, you may not: (a) copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the GDK or any part of the GDK; or (b) load any part of the GDK onto a mobile handset or wearable computing device or any other hardware device except a Glass device personal computer, combine any part of the GDK with other software, or distribute any software or device incorporating a part of the GDK.
2025-11-21T18:09:46.9983570Z 
2025-11-21T18:09:46.9986540Z 3.4 You agree that you will not take any actions that may cause or result in the fragmentation of Glass, including but not limited to distributing, participating in the creation of, or promoting in any way a software development kit derived from the GDK.
2025-11-21T18:09:46.9987900Z 
2025-11-21T18:09:46.9991230Z 3.5 Use, reproduction and distribution of components of the GDK licensed under an open source software license are governed solely by the terms of that open source software license and not this License Agreement.
2025-11-21T18:09:46.9992490Z 
2025-11-21T18:09:46.9994930Z 3.6 You agree that the form and nature of the GDK that Google provides may change without prior notice to you and that future versions of the GDK may be incompatible with applications developed on previous versions of the GDK. You agree that Google may stop (permanently or temporarily) providing the GDK (or any features within the GDK) to you or to users generally at Google's sole discretion, without prior notice to you.
2025-11-21T18:09:46.9996400Z 
2025-11-21T18:09:46.9998580Z 3.7 Nothing in this License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.
2025-11-21T18:09:46.9999640Z 
2025-11-21T18:09:47.0002110Z 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the GDK.
2025-11-21T18:09:47.0003160Z 
2025-11-21T18:09:47.0004760Z 
2025-11-21T18:09:47.0007410Z 3.9 Your use of any Android system files, packaged APIs, or other components of the GDK which are part of the Android Software Development Kit is subject to the terms of the Android Software Development Kit License Agreement located at http://developer.android.com/sdk/terms.html. These terms are hereby incorporated by reference into this License Agreement.
2025-11-21T18:09:47.0010610Z 
2025-11-21T18:09:47.0012150Z 4. Use of the GDK by You
2025-11-21T18:09:47.0014160Z 
2025-11-21T18:09:47.0016900Z 4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under this License Agreement in or to any software applications that you develop using the GDK, including any intellectual property rights that subsist in those applications.
2025-11-21T18:09:47.0018190Z 
2025-11-21T18:09:47.0022780Z 4.2 You agree to use the GDK and write applications only for purposes that are permitted by (a) this License Agreement, (b) the Glass Platform Developer Policies (located at https://developers.google.com/glass/policies, and hereby incorporated into this License Agreement by reference), and (c) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).
2025-11-21T18:09:47.0024580Z 
2025-11-21T18:09:47.0029010Z 4.3 You agree that if you use the GDK to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-21T18:09:47.0033620Z 
2025-11-21T18:09:47.0036540Z 4.4 You agree that you will not engage in any activity with the GDK, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google.
2025-11-21T18:09:47.0039220Z 
2025-11-21T18:09:47.0041870Z 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Glass and/or applications for Glass, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.
2025-11-21T18:09:47.0044670Z 
2025-11-21T18:09:47.0047630Z 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under this License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.
2025-11-21T18:09:47.0050920Z 
2025-11-21T18:09:47.0052340Z 
2025-11-21T18:09:47.0056410Z 4.7 The GDK is in development, and your testing and feedback are an important part of the development process. By using the GDK, you acknowledge that implementation of some features are still under development and that you should not rely on the GDK, Glass devices, Glass system software, Google Mirror API, or Glass services having the full functionality of a stable release.
2025-11-21T18:09:47.0058690Z 
2025-11-21T18:09:47.0060950Z 5. Your Developer Credentials
2025-11-21T18:09:47.0061620Z 
2025-11-21T18:09:47.0064150Z 5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.
2025-11-21T18:09:47.0065470Z 
2025-11-21T18:09:47.0067710Z 6. Privacy and Information
2025-11-21T18:09:47.0069210Z 
2025-11-21T18:09:47.0070550Z 
2025-11-21T18:09:47.0074400Z 6.1 In order to continually innovate and improve the GDK, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the GDK are being used and how they are being used. Before any of this information is collected, the GDK will notify you and seek your consent. If you withhold consent, the information will not be collected.
2025-11-21T18:09:47.0077490Z 
2025-11-21T18:09:47.0079450Z 6.2 The data collected is examined in the aggregate to improve the GDK and is maintained in accordance with Google's Privacy Policy.
2025-11-21T18:09:47.0081420Z 
2025-11-21T18:09:47.0083080Z 7. Third Party Applications
2025-11-21T18:09:47.0085000Z 
2025-11-21T18:09:47.0088760Z 7.1 If you use the GDK to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources.
2025-11-21T18:09:47.0091690Z 
2025-11-21T18:09:47.0093190Z 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners.
2025-11-21T18:09:47.0094710Z 
2025-11-21T18:09:47.0095590Z 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, this License Agreement does not affect your legal relationship with these third parties.
2025-11-21T18:09:47.0096310Z 
2025-11-21T18:09:47.0096670Z 8. Using Google APIs
2025-11-21T18:09:47.0096840Z 
2025-11-21T18:09:47.0097190Z 8.1 Google APIs
2025-11-21T18:09:47.0097350Z 
2025-11-21T18:09:47.0098650Z 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service.
2025-11-21T18:09:47.0100290Z 
2025-11-21T18:09:47.0102730Z 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-21T18:09:47.0104170Z 
2025-11-21T18:09:47.0106200Z 9. Terminating this License Agreement
2025-11-21T18:09:47.0106550Z 
2025-11-21T18:09:47.0107290Z 9.1 This License Agreement will continue to apply until terminated by either you or Google as set out below.
2025-11-21T18:09:47.0107740Z 
2025-11-21T18:09:47.0108320Z 9.2 If you want to terminate this License Agreement, you may do so by ceasing your use of the GDK and any relevant developer credentials.
2025-11-21T18:09:47.0108710Z 
2025-11-21T18:09:47.0110770Z 9.3 Google may at any time, terminate this License Agreement with you if: (A) you have breached any provision of this License Agreement; or (B) Google is required to do so by law; or (C) the partner with whom Google offered certain parts of GDK (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the GDK to you; or (D) Google decides to no longer provide the GDK or certain parts of the GDK to users in the country in which you are resident or from which you use the service, or the provision of the GDK or certain GDK services to you by Google is, in Google's sole discretion, no longer commercially viable.
2025-11-21T18:09:47.0112900Z 
2025-11-21T18:09:47.0115800Z 9.4 When this License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst this License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.
2025-11-21T18:09:47.0117490Z 
2025-11-21T18:09:47.0119500Z 10. DISCLAIMER OF WARRANTIES
2025-11-21T18:09:47.0121690Z 
2025-11-21T18:09:47.0124120Z 10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE GDK IS AT YOUR SOLE RISK AND THAT THE GDK IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.
2025-11-21T18:09:47.0125840Z 
2025-11-21T18:09:47.0128970Z 10.2 YOUR USE OF THE GDK AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE GDK IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE.
2025-11-21T18:09:47.0130350Z 
2025-11-21T18:09:47.0132320Z 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
2025-11-21T18:09:47.0133200Z 
2025-11-21T18:09:47.0133660Z 11. LIMITATION OF LIABILITY
2025-11-21T18:09:47.0133850Z 
2025-11-21T18:09:47.0135050Z 11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.
2025-11-21T18:09:47.0136360Z 
2025-11-21T18:09:47.0137400Z 12. Indemnification
2025-11-21T18:09:47.0139050Z 
2025-11-21T18:09:47.0143010Z 12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the GDK, (b) any application you develop on the GDK that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with this License Agreement.
2025-11-21T18:09:47.0144880Z 
2025-11-21T18:09:47.0146810Z 13. Changes to the License Agreement
2025-11-21T18:09:47.0148170Z 
2025-11-21T18:09:47.0150400Z 13.1 Google may make changes to the License Agreement as it distributes new versions of the GDK. When these changes are made, Google will make a new version of the License Agreement available on the website where the GDK is made available.
2025-11-21T18:09:47.0151380Z 
2025-11-21T18:09:47.0153090Z 14. General Legal Terms
2025-11-21T18:09:47.0154720Z 
2025-11-21T18:09:47.0156860Z 14.1 This License Agreement constitutes the whole legal agreement between you and Google and governs your use of the GDK (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the GDK.
2025-11-21T18:09:47.0158050Z 
2025-11-21T18:09:47.0161930Z 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in this License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.
2025-11-21T18:09:47.0164480Z 
2025-11-21T18:09:47.0167650Z 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of this License Agreement is invalid, then that provision will be removed from this License Agreement without affecting the rest of this License Agreement. The remaining provisions of this License Agreement will continue to be valid and enforceable.
2025-11-21T18:09:47.0169600Z 
2025-11-21T18:09:47.0172470Z 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to this License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of this License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to this License Agreement.
2025-11-21T18:09:47.0174360Z 
2025-11-21T18:09:47.0177330Z 14.5 EXPORT RESTRICTIONS. THE GDK IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE GDK. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.
2025-11-21T18:09:47.0178750Z 
2025-11-21T18:09:47.0181310Z 14.6 The rights granted in this License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under this License Agreement without the prior written approval of the other party.
2025-11-21T18:09:47.0182150Z 
2025-11-21T18:09:47.0184000Z 14.7 This License Agreement, and your relationship with Google under this License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from this License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.
2025-11-21T18:09:47.0185570Z 
2025-11-21T18:09:47.0187300Z November 19, 2013
2025-11-21T18:09:47.0189310Z ---------------------------------------
2025-11-21T18:09:47.0190850Z Accept? (y/N): 
2025-11-21T18:09:47.0193470Z 6/6: License mips-android-sysimage-license:
2025-11-21T18:09:47.0194140Z ---------------------------------------
2025-11-21T18:09:47.0199320Z MIPS Technologies, Inc. (“MIPS”) Internal Evaluation License Agreement for MIPS Android™ System Images for Android Software Development Kit (SDK): This Internal Evaluation License Agreement (this "Agreement") is entered into by and between MIPS and you (as an individual developer or a legal entity -- identified below as “Recipient”). MIPS shall make the Evaluation Software available to Recipient as described in accordance with the terms and conditions set forth below.
2025-11-21T18:09:47.0200900Z 
2025-11-21T18:09:47.0204100Z By clicking on the “Accept” button, downloading, installing, or otherwise using the Evaluation Materials (defined below), you agree to be bound by the terms of this Agreement effective as of the date you click “Accept” (the “Effective Date”), and if doing so on behalf of an entity, you represent that you are authorized to bind the entity to the terms and conditions of this Agreement. If you do not agree to be bound by the terms and conditions of this Agreement, do not download, install, or use the Evaluation Materials.
2025-11-21T18:09:47.0205480Z 
2025-11-21T18:09:47.0207540Z 1. DEFINITIONS. These terms shall have the following meanings:
2025-11-21T18:09:47.0208590Z 
2025-11-21T18:09:47.0211120Z 1.1 “MIPS” shall mean MIPS Technologies, Inc., a Delaware corporation having a principal place of business at: 955 East Arques Ave., Sunnyvale, CA 94085
2025-11-21T18:09:47.0212220Z 
2025-11-21T18:09:47.0214240Z 1.2 “Evaluation Software” shall mean MIPS Android™ emulator system images for Android Software Development Kit (SDK), as made available to Recipient.
2025-11-21T18:09:47.0215080Z 
2025-11-21T18:09:47.0217770Z 1.3 “Evaluation Materials" means, collectively, the Evaluation Software (in source and/or object code form) and documentation (including, without limitation, any design documents, specifications, reference manuals, and other related materials) related to the Evaluation Software as made available to Recipient.
2025-11-21T18:09:47.0219140Z 
2025-11-21T18:09:47.0225750Z 1.4 “Open Source Software” means any software that requires (as a condition of use, modification and/or distribution of such software) that such software or other software incorporated into, derived from or distributed with such software (a) be disclosed or distributed in source code form; or (b) be licensed by the user to third parties for the purpose of making and/or distributing derivative works; or (c) be redistributable at no charge. Open Source Software includes, without limitation, software licensed or distributed under any of the following licenses or distribution models, or licenses or distribution models substantially similar to any of the following: (a) GNU’s General Public License (GPL) or Lesser/Library GPL (LGPL), (b) the Artistic License (e.g., PERL), (c) the Mozilla Public License, (d) the Netscape Public License, (e) the Sun Community Source License (SCSL), (f) the Sun Industry Source License (SISL), (g) the Apache Software license and (h) the Common Public License (CPL).
2025-11-21T18:09:47.0230590Z 
2025-11-21T18:09:47.0234430Z 1.5 “Pre-Release Materials” means “alpha” or “beta” designated pre-release features, which may not be fully functional, which MIPS may substantially modify in producing any production version of the Evaluation Materials, and/or which is still under development by MIPS and/or MIPS’ suppliers.
2025-11-21T18:09:47.0235930Z 
2025-11-21T18:09:47.0239420Z 2. PURPOSE. MIPS desires to make the Evaluation Materials available to Recipient solely for Recipient's internal evaluation of the Evaluation Software to evaluate the desirability of cooperating with MIPS in developing products that are compatible with the Evaluation Software and/or to advise MIPS as to possible modifications to the Evaluation Software. Recipient may not disclose, distribute, modify (except to facilitate the above-mentioned internal evaluation), or make commercial use of the Evaluation Materials or any modifications of the Evaluation Materials.
2025-11-21T18:09:47.0241510Z 
2025-11-21T18:09:47.0245490Z THE EVALUATION MATERIALS ARE PROVIDED FOR EVALUATION PURPOSES ONLY AND MAY NOT BE MODIFIED (EXCEPT TO FACILITATE THE INTERNAL EVALUATION) OR DISTRIBUTED BY RECIPIENT OR INCORPORATED INTO RECIPIENT’S PRODUCTS OR SOFTWARE. PLEASE CONTACT A MIPS SALES REPRESENTATIVE TO LEARN ABOUT THE AVAILABILITY AND COST OF A COMMERCIAL VERSION OF THE EVALUATION SOFTWARE.
2025-11-21T18:09:47.0247490Z 
2025-11-21T18:09:47.0249900Z 3. TITLE. Title to the Evaluation Materials remains with MIPS or its suppliers. Recipient shall not mortgage, pledge or encumber the Evaluation Materials in any way. Recipient shall return all Evaluation Materials, keeping no copies, upon termination or expiration of this Agreement.
2025-11-21T18:09:47.0251460Z 
2025-11-21T18:09:47.0259080Z 4. LICENSE. MIPS grants Recipient a royalty-free, personal, nontransferable, nonexclusive license under its copyrights to use the Evaluation Software only for the purposes described in paragraph 2 above and only for a period beginning on the Effective Date and extending to the first anniversary of the Effective Date (the “Evaluation Period”). Unless otherwise communicated in writing by MIPS to Recipient, to the extent the Evaluation Software is provided in more than one delivery or release (each, a “Release”) the license grant in this Section 4 and the Evaluation Period shall apply to each Release, in which case the Evaluation Period shall begin on the date that the Release is made generally available and continue to the first anniversary of such date. Recipient may not make modifications to the Evaluation Software. Recipient shall not disassemble, reverse-engineer, or decompile any software that is not provided to Recipient in source code form.
2025-11-21T18:09:47.0262650Z 
2025-11-21T18:09:47.0265340Z 
2025-11-21T18:09:47.0266780Z EXCEPT AS PROVIDED HEREIN, NO OTHER LICENSE, EXPRESS OR IMPLIED, BY ESTOPPEL OR OTHERWISE, TO ANY OTHER MIPS INTELLECTUAL PROPERTY RIGHTS IS GRANTED TO THE RECIPIENT. OTHER THAN AS EXPLICITLY SET FORTH IN PARAGRAPH 2 ABOVE, NO RIGHT TO COPY, TO REPRODUCE, TO MODIFY, OR TO CREATE DERIVATIVE WORKS OF, THE EVALUATION MATERIALS IS GRANTED HEREIN.
2025-11-21T18:09:47.0267600Z 
2025-11-21T18:09:47.0268510Z 5. NO OBLIGATION. Recipient shall have no duty to purchase or license any product from MIPS. MIPS and its suppliers shall have no obligation to provide support for, or develop a non-evaluation version of, the Evaluation Software or to license any version of it.
2025-11-21T18:09:47.0269690Z 
2025-11-21T18:09:47.0273070Z 6. MODIFICATIONS. This Agreement does not obligate Recipient to provide MIPS with comments or suggestions regarding Evaluation Materials. However, should Recipient provide MIPS with comments or suggestions for the modification, correction, improvement or enhancement of (a) the Evaluation Materials or (b) MIPS products or processes which may embody the Evaluation Materials, then Recipient agrees to grant and hereby grants to MIPS a non-exclusive, irrevocable, worldwide, fully paid-up, royalty-free license, with the right to sublicense MIPS’ licensees and customers, under Recipient’s Intellectual property rights, to use and disclose such comments and suggestions in any manner MIPS chooses and to display, perform, copy, make, have made, use, sell, offer to sell, import, and otherwise dispose of MIPS’ and its sublicensee’s products embodying such comments and suggestions in any manner and via any media MIPS chooses, without reference to the source.
2025-11-21T18:09:47.0275360Z 
2025-11-21T18:09:47.0277090Z 7. WARRANTY DISCLAIMER. MIPS AND ITS SUPPLIERS MAKE NO WARRANTIES WITH RESPECT TO EVALUATION MATERIALS, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, OR ANY IMPLIED WARRANTY OF NONINFRINGEMENT WITH RESPECT TO THIRD PARTY INTELLECTUAL PROPERTY. RECIPIENT ACKNOWLEDGES AND AGREES THAT THE EVALUATION MATERIALS ARE PROVIDED “AS IS,” WITHOUT WARRANTY OF ANY KIND.
2025-11-21T18:09:47.0278080Z 
2025-11-21T18:09:47.0279630Z 8. LIMITATION OF LIABILITY. MIPS AND ITS SUPPLIERS SHALL NOT BE LIABLE FOR ANY PROPERTY DAMAGE, PERSONAL INJURY, LOSS OF PROFITS, INTERRUPTION OF BUSINESS OR FOR ANY DIRECT, INDIRECT, SPECIAL, CONSEQUENTIAL OR INCIDENTAL DAMAGES, HOWEVER CAUSED OR ALLEGED, WHETHER FOR BREACH OF WARRANTY, CONTRACT, STRICT LIABILITY OR OTHERWISE, INCLUDING WITHOUT LIMITATION, UNDER TORT OR OTHER LEGAL THEORY. MIPS AND ITS SUPPLIERS DISCLAIM ANY AND ALL LIABILITY, INCLUDING LIABILITY FOR INFRINGEMENT OF ANY INTELLECTUAL PROPERTY RIGHTS OF ANY KIND RELATING TO THE EVALUATION MATERIALS.
2025-11-21T18:09:47.0281010Z 
2025-11-21T18:09:47.0282190Z 9. EXPIRATION. MIPS may terminate this Agreement immediately after a breach by Recipient or otherwise at MIPS’ reasonable discretion and upon five (5) business days’ notice to Recipient.
2025-11-21T18:09:47.0282680Z 
2025-11-21T18:09:47.0283050Z 10. GENERAL.
2025-11-21T18:09:47.0283240Z 
2025-11-21T18:09:47.0286010Z 10.1 Controlling Law. This Agreement shall be governed by California law excluding its choice of law rules. With the exception of MIPS’ rights to enforce its intellectual property rights and any confidentiality obligations under this Agreement or any licenses distributed with the Evaluation Materials, all disputes and any claims arising under or relating to this Agreement shall be subject to the exclusive jurisdiction and venue of the state and federal courts located in Santa Clara County, California. Each party hereby agrees to jurisdiction and venue in the courts set forth in the preceding sentence. The parties agree that the United Nations Convention on Contracts for the International Sale of Goods is specifically excluded from application to this Agreement. The parties consent to the personal jurisdiction of the above courts.
2025-11-21T18:09:47.0287880Z 
2025-11-21T18:09:47.0289380Z 10.2 Remedies. Recipient acknowledges and agrees that any breach of confidentiality obligations under this Agreement or any licenses distributed with the Evaluation Materials, as well as any disclosure, commercialization, or public use of the Evaluation Materials, would cause irreparable injury to MIPS, and therefore Recipient agrees to consent to, and hereby consents to, the grant of an injunction by any court of competent jurisdiction in the event of an actual or threatened breach.
2025-11-21T18:09:47.0290930Z 
2025-11-21T18:09:47.0293000Z 10.3 Assignment. Recipient may not delegate, assign or transfer this Agreement, the license granted or any of Recipient’s rights, obligations, or duties hereunder, expressly, by implication, by operation of law, by way of merger (regardless of whether Recipient is the surviving entity) or acquisition, or otherwise and any attempt to do so, without MIPS’ express prior written consent, shall be ineffective, null and void. MIPS may freely assign this Agreement, and its rights and obligations hereunder, in its sole discretion.
2025-11-21T18:09:47.0294380Z 
2025-11-21T18:09:47.0295690Z 10.4 Entire Agreement. This Agreement constitutes the entire agreement between Recipient and MIPS and supersedes in their entirety any and all oral or written agreements previously existing between Recipient and MIPS with respect to the subject matter hereof. This Agreement may only be amended or supplemented by a writing that refers explicitly to this Agreement and that is signed or otherwise accepted by duly authorized representatives of Recipient and MIPS.
2025-11-21T18:09:47.0296770Z 
2025-11-21T18:09:47.0298050Z 10.5 Severability. In the event that any provision of this Agreement is finally adjudicated to be unenforceable or invalid under any applicable law, such unenforceability or invalidity shall not render this Agreement unenforceable or invalid as a whole, and, in such event, such unenforceable or invalid provision shall be interpreted so as to best accomplish the objectives of such provision within the limits of applicable law or applicable court decisions.
2025-11-21T18:09:47.0299130Z 
2025-11-21T18:09:47.0302370Z 10.6 Export Regulations / Export Control. Recipient shall not export, either directly or indirectly, any product, service or technical data or system incorporating the Evaluation Materials without first obtaining any required license or other necessary approval from the U.S. Department of Commerce or any other governing agency or department of the United States Government. In the event any product is exported from the United States or re-exported from a foreign destination by Recipient, Recipient shall ensure that the distribution and export/re-export or import of the product is in compliance with all applicable laws, regulations, orders, or other restrictions of the U.S. Export Administration Regulations and the appropriate foreign government. Recipient agrees that neither it nor any of its subsidiaries will export/re-export any technical data, process, product, or service, directly or indirectly, to any country for which the United States government or any agency thereof or the foreign government from where it is shipping requires an export license, or other governmental approval, without first obtaining such license or approval. Recipient also agrees to implement measures to ensure that foreign national employees are authorized to receive any information controlled by U.S. export control laws. An export is "deemed" to take place when information is released to a foreign national wherever located.
2025-11-21T18:09:47.0305610Z 
2025-11-21T18:09:47.0308390Z 10.7 Special Terms for Pre-Release Materials. If so indicated in the description of the Evaluation Software, the Evaluation Software may contain Pre-Release Materials. Recipient hereby understands, acknowledges and agrees that: (i) Pre-Release Materials may not be fully tested and may contain bugs or errors; (ii) Pre-Release materials are not suitable for commercial release in their current state; (iii) regulatory approvals for Pre-Release Materials (such as UL or FCC) have not been obtained, and Pre-Release Materials may therefore not be certified for use in certain countries or environments or may not be suitable for certain applications and (iv) MIPS can provide no assurance that it will ever produce or make generally available a production version of the Pre-Release Materials . MIPS is not under any obligation to develop and/or release or offer for sale or license a final product based upon the Pre-Release Materials and may unilaterally elect to abandon the Pre-Release Materials or any such development platform at any time and without any obligation or liability whatsoever to Recipient or any other person.
2025-11-21T18:09:47.0311050Z 
2025-11-21T18:09:47.0312110Z ANY PRE-RELEASE MATERIALS ARE NON-QUALIFIED AND, AS SUCH, ARE PROVIDED “AS IS” AND “AS AVAILABLE”, POSSIBLY WITH FAULTS, AND WITHOUT REPRESENTATION OR WARRANTY OF ANY KIND.
2025-11-21T18:09:47.0312700Z 
2025-11-21T18:09:47.0314340Z 10.8 Open Source Software. In the event Open Source software is included with Evaluation Software, such Open Source software is licensed pursuant to the applicable Open Source software license agreement identified in the Open Source software comments in the applicable source code file(s) and/or file header as indicated in the Evaluation Software. Additional detail may be available (where applicable) in the accompanying on-line documentation. With respect to the Open Source software, nothing in this Agreement limits any rights under, or grants rights that supersede, the terms of any applicable Open Source software license agreement.
2025-11-21T18:09:47.0316110Z ---------------------------------------
2025-11-21T18:09:47.0316650Z Accept? (y/N): All SDK package licenses accepted
2025-11-21T18:09:47.0317430Z 
2025-11-21T18:09:47.0319950Z 🔄 Updating SDK manager...
2025-11-21T18:09:48.3006310Z Loading package information...                                                  
2025-11-21T18:09:48.9129590Z Loading local repository...                                                     
2025-11-21T18:09:49.0134310Z [                                       ] 3% Loading local repository...        
2025-11-21T18:09:49.1140840Z [                                       ] 3% Fetch remote repository...         
2025-11-21T18:09:49.9436480Z [=                                      ] 3% Fetch remote repository...         
2025-11-21T18:09:50.1022700Z [=                                      ] 4% Fetch remote repository...         
2025-11-21T18:09:50.3438430Z [=                                      ] 5% Fetch remote repository...         
2025-11-21T18:09:50.3690860Z [==                                     ] 5% Fetch remote repository...         
2025-11-21T18:09:50.6899390Z [==                                     ] 6% Fetch remote repository...         
2025-11-21T18:09:50.7806930Z [==                                     ] 7% Fetch remote repository...         
2025-11-21T18:09:50.7982160Z [==                                     ] 7% Computing updates...               
2025-11-21T18:09:50.7984890Z [===                                    ] 8% Computing updates...               
2025-11-21T18:09:50.8008550Z [===                                    ] 10% Computing updates...              
2025-11-21T18:09:50.8012370Z Updating:
2025-11-21T18:09:50.8014840Z emulator
2025-11-21T18:09:51.8521160Z [===                                    ] 10% Installing Android Emulator       
2025-11-21T18:09:52.1323950Z [===                                    ] 10% Downloading emulator-darwin_x64-14
2025-11-21T18:09:52.3208900Z [====                                   ] 10% Downloading emulator-darwin_x64-14
2025-11-21T18:09:52.5379900Z [====                                   ] 11% Downloading emulator-darwin_x64-14
2025-11-21T18:09:53.0777190Z [====                                   ] 12% Downloading emulator-darwin_x64-14
2025-11-21T18:09:53.3875380Z [=====                                  ] 13% Downloading emulator-darwin_x64-14
2025-11-21T18:09:53.6930950Z [=====                                  ] 14% Downloading emulator-darwin_x64-14
2025-11-21T18:09:53.9666160Z [=====                                  ] 15% Downloading emulator-darwin_x64-14
2025-11-21T18:09:54.0599050Z [======                                 ] 15% Downloading emulator-darwin_x64-14
2025-11-21T18:09:54.2899250Z [======                                 ] 16% Downloading emulator-darwin_x64-14
2025-11-21T18:09:54.7333470Z [======                                 ] 17% Downloading emulator-darwin_x64-14
2025-11-21T18:09:54.8838700Z [=======                                ] 18% Downloading emulator-darwin_x64-14
2025-11-21T18:09:55.2109610Z [=======                                ] 19% Downloading emulator-darwin_x64-14
2025-11-21T18:09:55.3251470Z [=======                                ] 20% Downloading emulator-darwin_x64-14
2025-11-21T18:09:55.4216290Z [========                               ] 20% Downloading emulator-darwin_x64-14
2025-11-21T18:09:55.6455300Z [========                               ] 21% Downloading emulator-darwin_x64-14
2025-11-21T18:09:55.8336210Z [========                               ] 22% Downloading emulator-darwin_x64-14
2025-11-21T18:09:56.0026880Z [=========                              ] 23% Downloading emulator-darwin_x64-14
2025-11-21T18:09:56.2187460Z [=========                              ] 24% Downloading emulator-darwin_x64-14
2025-11-21T18:09:56.3758510Z [=========                              ] 25% Downloading emulator-darwin_x64-14
2025-11-21T18:09:56.4191260Z [==========                             ] 25% Downloading emulator-darwin_x64-14
2025-11-21T18:09:56.7526760Z [==========                             ] 26% Downloading emulator-darwin_x64-14
2025-11-21T18:09:56.8929510Z [==========                             ] 27% Downloading emulator-darwin_x64-14
2025-11-21T18:09:57.2339760Z [===========                            ] 28% Downloading emulator-darwin_x64-14
2025-11-21T18:09:57.4101840Z [===========                            ] 29% Downloading emulator-darwin_x64-14
2025-11-21T18:09:57.5266240Z [===========                            ] 30% Downloading emulator-darwin_x64-14
2025-11-21T18:09:57.6296270Z [============                           ] 30% Downloading emulator-darwin_x64-14
2025-11-21T18:09:57.8007960Z [============                           ] 31% Downloading emulator-darwin_x64-14
2025-11-21T18:09:57.9773590Z [============                           ] 32% Downloading emulator-darwin_x64-14
2025-11-21T18:09:57.9825900Z [============                           ] 33% Downloading emulator-darwin_x64-14
2025-11-21T18:09:58.2271580Z [============                           ] 33% Unzipping...                      
2025-11-21T18:09:58.3255150Z [============                           ] 33% Unzipping... emulator/            
2025-11-21T18:09:58.3481180Z [============                           ] 33% Unzipping... emulator/qsn         
2025-11-21T18:09:58.5178920Z [=============                          ] 33% Unzipping... emulator/qsn         
2025-11-21T18:09:58.6256860Z [=============                          ] 33% Unzipping... emulator/qemu-img    
2025-11-21T18:09:58.6864230Z [=============                          ] 33% Unzipping... emulator/crashreport 
2025-11-21T18:09:58.6875910Z [=============                          ] 33% Unzipping... emulator/lib64/      
2025-11-21T18:09:59.0207910Z [=============                          ] 33% Unzipping... emulator/lib64/gles_a
2025-11-21T18:09:59.0446400Z [=============                          ] 34% Unzipping... emulator/lib64/gles_a
2025-11-21T18:09:59.0502340Z [=============                          ] 34% Unzipping... emulator/lib64/libemu
2025-11-21T18:09:59.0572400Z [=============                          ] 34% Unzipping... emulator/lib64/liband
2025-11-21T18:09:59.3836670Z [=============                          ] 34% Unzipping... emulator/lib64/libgfx
2025-11-21T18:09:59.5044380Z [=============                          ] 34% Unzipping... emulator/lib64/libpro
2025-11-21T18:09:59.5456210Z [=============                          ] 34% Unzipping... emulator/lib64/liband
2025-11-21T18:09:59.5519060Z [=============                          ] 34% Unzipping... emulator/lib64/libima
2025-11-21T18:09:59.5536650Z [=============                          ] 34% Unzipping... emulator/lib64/liband
2025-11-21T18:09:59.5571620Z [=============                          ] 34% Unzipping... emulator/lib64/qt/   
2025-11-21T18:09:59.8406150Z [=============                          ] 34% Unzipping... emulator/lib64/qt/plu
2025-11-21T18:09:59.9983380Z [=============                          ] 34% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:00.4793250Z [=============                          ] 35% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:00.4972440Z [==============                         ] 35% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:00.5644960Z [==============                         ] 35% Unzipping... emulator/lib64/qt/res
2025-11-21T18:10:00.8524000Z [==============                         ] 36% Unzipping... emulator/lib64/qt/res
2025-11-21T18:10:01.0538690Z [==============                         ] 36% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:02.3743280Z [==============                         ] 37% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:03.1426990Z [===============                        ] 38% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:03.8055240Z [===============                        ] 39% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:04.0572570Z [===============                        ] 40% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:04.2683620Z [================                       ] 40% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:04.7866260Z [================                       ] 41% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:05.1398430Z [================                       ] 42% Unzipping... emulator/lib64/qt/lib
2025-11-21T18:10:05.1475050Z [================                       ] 42% Unzipping... emulator/lib64/qt/tra
2025-11-21T18:10:05.4473790Z [=================                      ] 43% Unzipping... emulator/lib64/qt/tra
2025-11-21T18:10:05.4524660Z [=================                      ] 43% Unzipping... emulator/lib64/libabs
2025-11-21T18:10:05.4577930Z [=================                      ] 43% Unzipping... emulator/lib64/liband
2025-11-21T18:10:05.4881300Z [=================                      ] 43% Unzipping... emulator/lib64/libpro
2025-11-21T18:10:05.7844830Z [=================                      ] 43% Unzipping... emulator/lib64/vulkan
2025-11-21T18:10:05.8199490Z [=================                      ] 44% Unzipping... emulator/lib64/vulkan
2025-11-21T18:10:05.8747540Z [=================                      ] 44% Unzipping... emulator/lib64/libsha
2025-11-21T18:10:05.8922330Z [=================                      ] 44% Unzipping... emulator/lib64/libgli
2025-11-21T18:10:05.9790830Z [=================                      ] 44% Unzipping... emulator/lib64/liband
2025-11-21T18:10:05.9791560Z [=================                      ] 44% Unzipping... emulator/include/    
2025-11-21T18:10:06.0024550Z [=================                      ] 44% Unzipping... emulator/include/flat
2025-11-21T18:10:06.0041750Z [=================                      ] 44% Unzipping... emulator/resources/  
2025-11-21T18:10:06.0119120Z [=================                      ] 44% Unzipping... emulator/resources/po
2025-11-21T18:10:06.0436480Z [=================                      ] 44% Unzipping... emulator/resources/To
2025-11-21T18:10:06.0561480Z [=================                      ] 44% Unzipping... emulator/resources/ma
2025-11-21T18:10:06.0565850Z [=================                      ] 44% Unzipping... emulator/resources/To
2025-11-21T18:10:06.0601300Z [=================                      ] 44% Unzipping... emulator/resources/ma
2025-11-21T18:10:06.1062420Z [=================                      ] 44% Unzipping... emulator/resources/To
2025-11-21T18:10:06.1163460Z [=================                      ] 45% Unzipping... emulator/resources/To
2025-11-21T18:10:06.2237390Z [=================                      ] 45% Unzipping... emulator/crashpad_han
2025-11-21T18:10:06.3236190Z [=================                      ] 45% Unzipping... emulator/bin64/      
2025-11-21T18:10:06.4239580Z [=================                      ] 45% Unzipping... emulator/bin64/fsck.e
2025-11-21T18:10:06.4292360Z [=================                      ] 45% Unzipping... emulator/bin64/mkfs.e
2025-11-21T18:10:06.4293570Z [=================                      ] 45% Unzipping... emulator/bin64/tune2f
2025-11-21T18:10:06.4294820Z [=================                      ] 45% Unzipping... emulator/bin64/resize
2025-11-21T18:10:06.4295390Z [=================                      ] 45% Unzipping... emulator/bin64/e2fsck
2025-11-21T18:10:06.4296240Z [=================                      ] 45% Unzipping... emulator/_CodeSignatu
2025-11-21T18:10:06.4297300Z [=================                      ] 45% Unzipping... emulator/NOTICE.csv  
2025-11-21T18:10:06.4298030Z [=================                      ] 45% Unzipping... emulator/._NOTICE.csv
2025-11-21T18:10:06.4298810Z [=================                      ] 45% Unzipping... emulator/LICENSE     
2025-11-21T18:10:06.4299690Z [=================                      ] 45% Unzipping... emulator/._LICENSE   
2025-11-21T18:10:06.4300540Z [=================                      ] 45% Unzipping... emulator/source.prope
2025-11-21T18:10:06.4301280Z [=================                      ] 45% Unzipping... emulator/._source.pro
2025-11-21T18:10:06.4302000Z [=================                      ] 45% Unzipping... emulator/emulator-che
2025-11-21T18:10:06.4492790Z [=================                      ] 45% Unzipping... emulator/netsimd     
2025-11-21T18:10:06.7278550Z [==================                     ] 45% Unzipping... emulator/netsimd     
2025-11-21T18:10:06.7840960Z [==================                     ] 46% Unzipping... emulator/netsimd     
2025-11-21T18:10:06.8386430Z [==================                     ] 46% Unzipping... emulator/android-info
2025-11-21T18:10:06.8519690Z [==================                     ] 46% Unzipping... emulator/._android-in
2025-11-21T18:10:06.8520750Z [==================                     ] 46% Unzipping... emulator/qemu/       
2025-11-21T18:10:07.8181930Z [==================                     ] 46% Unzipping... emulator/qemu/darwin-
2025-11-21T18:10:08.3289890Z [==================                     ] 47% Unzipping... emulator/qemu/darwin-
2025-11-21T18:10:08.8010540Z [===================                    ] 48% Unzipping... emulator/qemu/darwin-
2025-11-21T18:10:09.3387390Z [===================                    ] 49% Unzipping... emulator/qemu/darwin-
2025-11-21T18:10:09.4947850Z [===================                    ] 50% Unzipping... emulator/qemu/darwin-
2025-11-21T18:10:09.7787310Z [====================                   ] 50% Unzipping... emulator/qemu/darwin-
2025-11-21T18:10:10.4690180Z [====================                   ] 51% Unzipping... emulator/qemu/darwin-
2025-11-21T18:10:10.9604420Z [====================                   ] 52% Unzipping... emulator/qemu/darwin-
2025-11-21T18:10:11.8203980Z [=====================                  ] 53% Unzipping... emulator/qemu/darwin-
2025-11-21T18:10:12.4325440Z [=====================                  ] 54% Unzipping... emulator/qemu/darwin-
2025-11-21T18:10:12.4340200Z [=====================                  ] 54% Unzipping... emulator/mksdcard    
2025-11-21T18:10:12.4342610Z [=====================                  ] 54% Unzipping... emulator/lib/        
2025-11-21T18:10:12.4345910Z [=====================                  ] 54% Unzipping... emulator/lib/waterfal
2025-11-21T18:10:12.4354410Z [=====================                  ] 54% Unzipping... emulator/lib/emulator
2025-11-21T18:10:12.4378870Z [=====================                  ] 54% Unzipping... emulator/lib/pkgconfi
2025-11-21T18:10:12.4384200Z [=====================                  ] 54% Unzipping... emulator/lib/cmake/  
2025-11-21T18:10:12.4406050Z [=====================                  ] 54% Unzipping... emulator/lib/cmake/fl
2025-11-21T18:10:12.4420730Z [=====================                  ] 54% Unzipping... emulator/lib/emulator
2025-11-21T18:10:12.4424120Z [=====================                  ] 54% Unzipping... emulator/lib/control_
2025-11-21T18:10:12.4435380Z [=====================                  ] 54% Unzipping... emulator/lib/hardware
2025-11-21T18:10:12.4485820Z [=====================                  ] 54% Unzipping... emulator/lib/libflatb
2025-11-21T18:10:12.5226910Z [=====================                  ] 55% Unzipping... emulator/lib/libflatb
2025-11-21T18:10:12.5234470Z [=====================                  ] 55% Unzipping... emulator/lib/adb_serv
2025-11-21T18:10:12.5251820Z [=====================                  ] 55% Unzipping... emulator/lib/hostapd.
2025-11-21T18:10:12.5692060Z [=====================                  ] 55% Unzipping... emulator/lib/pc-bios/
2025-11-21T18:10:12.5704580Z [=====================                  ] 55% Unzipping... emulator/lib/snapshot
2025-11-21T18:10:12.5705750Z [=====================                  ] 55% Unzipping... emulator/lib/emu-orig
2025-11-21T18:10:12.5714650Z [=====================                  ] 55% Unzipping... emulator/lib/advanced
2025-11-21T18:10:12.5725340Z [=====================                  ] 55% Unzipping... emulator/lib/emulated
2025-11-21T18:10:12.5732330Z [=====================                  ] 55% Unzipping... emulator/lib/snapshot
2025-11-21T18:10:12.5740340Z [=====================                  ] 55% Unzipping... emulator/lib/emulated
2025-11-21T18:10:12.5748280Z [=====================                  ] 55% Unzipping... emulator/lib/emulator
2025-11-21T18:10:12.5790160Z [=====================                  ] 55% Unzipping... emulator/lib/ca-bundl
2025-11-21T18:10:12.5794770Z [=====================                  ] 55% Unzipping... emulator/lib/ui_contr
2025-11-21T18:10:12.5801450Z [=====================                  ] 55% Unzipping... emulator/lib/grpc_end
2025-11-21T18:10:12.7295240Z [=====================                  ] 55% Unzipping... emulator/nimble_bridg
2025-11-21T18:10:12.7559970Z [=====================                  ] 55% Unzipping... emulator/emulator    
2025-11-21T18:10:12.7593920Z [=====================                  ] 55% Unzipping... emulator/NOTICE.txt  
2025-11-21T18:10:12.9107570Z [=====================                  ] 55% Unzipping... emulator/._NOTICE.txt
2025-11-21T18:10:12.9108360Z [=======================================] 100% Unzipping... emulator/._NOTICE.tx
2025-11-21T18:10:13.1518770Z 
2025-11-21T18:10:13.2472420Z 📦 Installing SDK components with Google Play Store...
2025-11-21T18:10:14.6472930Z Loading package information...                                                  
2025-11-21T18:10:14.7814010Z Loading local repository...                                                     
2025-11-21T18:10:14.7819100Z [                                       ] 3% Loading local repository...        
2025-11-21T18:10:14.8064830Z [                                       ] 3% Fetch remote repository...         
2025-11-21T18:10:15.3039230Z [=                                      ] 3% Fetch remote repository...         
2025-11-21T18:10:15.5000990Z [=                                      ] 4% Fetch remote repository...         
2025-11-21T18:10:15.5419080Z [=                                      ] 5% Fetch remote repository...         
2025-11-21T18:10:15.7603910Z [==                                     ] 5% Fetch remote repository...         
2025-11-21T18:10:15.8654840Z [==                                     ] 6% Fetch remote repository...         
2025-11-21T18:10:16.0279580Z [==                                     ] 7% Fetch remote repository...         
2025-11-21T18:10:16.0283440Z [==                                     ] 7% Computing updates...               
2025-11-21T18:10:16.0285440Z [===                                    ] 8% Computing updates...               
2025-11-21T18:10:16.0287340Z [===                                    ] 10% Computing updates...              
2025-11-21T18:10:16.7398210Z [===                                    ] 10% Installing Google Play Intel x86_6
2025-11-21T18:10:17.3742820Z [===                                    ] 10% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:19.0268740Z [====                                   ] 10% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:21.2301040Z [====                                   ] 11% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:23.8635870Z [====                                   ] 12% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:25.9848290Z [=====                                  ] 13% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:29.0334650Z [=====                                  ] 14% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:31.2161790Z [=====                                  ] 15% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:32.6813460Z [======                                 ] 15% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:34.9639230Z [======                                 ] 16% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:40.5452890Z [======                                 ] 17% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:40.6504860Z [=======                                ] 18% Downloading x86_64-30_r10-darwin.z
2025-11-21T18:10:40.8391870Z [=======                                ] 18% Unzipping...                      
2025-11-21T18:10:40.8403620Z [=======                                ] 18% Unzipping... x86_64/advancedFeatur
2025-11-21T18:10:40.8406730Z [=======                                ] 18% Unzipping... x86_64/build.prop    
2025-11-21T18:10:40.8409180Z [=======                                ] 18% Unzipping... x86_64/data/         
2025-11-21T18:10:40.8417220Z [=======                                ] 18% Unzipping... x86_64/data/misc/    
2025-11-21T18:10:40.8419760Z [=======                                ] 18% Unzipping... x86_64/data/misc/emul
2025-11-21T18:10:40.8421770Z [=======                                ] 18% Unzipping... x86_64/data/misc/gcec
2025-11-21T18:10:40.8428740Z [=======                                ] 18% Unzipping... x86_64/data/misc/apns
2025-11-21T18:10:40.8431800Z [=======                                ] 18% Unzipping... x86_64/data/misc/wifi
2025-11-21T18:10:40.8433900Z [=======                                ] 18% Unzipping... x86_64/data/system/  
2025-11-21T18:10:40.8437450Z [=======                                ] 18% Unzipping... x86_64/data/system/di
2025-11-21T18:10:40.8440040Z [=======                                ] 18% Unzipping... x86_64/data/local.pro
2025-11-21T18:10:41.1658370Z [=======                                ] 18% Unzipping... x86_64/encryptionkey.
2025-11-21T18:10:42.4409140Z [=======                                ] 18% Unzipping... x86_64/kernel-ranchu 
2025-11-21T18:10:42.4896830Z [=======                                ] 18% Unzipping... x86_64/NOTICE.txt    
2025-11-21T18:10:42.5323050Z [=======                                ] 18% Unzipping... x86_64/ramdisk.img   
2025-11-21T18:10:42.5453760Z [=======                                ] 18% Unzipping... x86_64/source.propert
2025-11-21T18:10:58.4214420Z [=======                                ] 18% Unzipping... x86_64/system.img    
2025-11-21T18:11:04.2645550Z [=======                                ] 19% Unzipping... x86_64/system.img    
2025-11-21T18:11:07.1479840Z [=======                                ] 20% Unzipping... x86_64/system.img    
2025-11-21T18:11:10.0789340Z [========                               ] 20% Unzipping... x86_64/system.img    
2025-11-21T18:11:14.5503440Z [========                               ] 21% Unzipping... x86_64/system.img    
2025-11-21T18:11:18.9642620Z [========                               ] 22% Unzipping... x86_64/system.img    
2025-11-21T18:11:24.6833880Z [=========                              ] 23% Unzipping... x86_64/system.img    
2025-11-21T18:11:35.3083720Z [=========                              ] 24% Unzipping... x86_64/system.img    
2025-11-21T18:11:38.3575960Z [=========                              ] 25% Unzipping... x86_64/system.img    
2025-11-21T18:11:38.3680730Z [=========                              ] 25% Unzipping... x86_64/userdata.img  
2025-11-21T18:11:42.3431020Z [=========                              ] 25% Unzipping... x86_64/vendor.img    
2025-11-21T18:11:42.5257420Z [=========                              ] 25% Unzipping... x86_64/VerifiedBootPa
2025-11-21T18:11:43.1372990Z [===============                        ] 40% Unzipping... x86_64/VerifiedBootPa
2025-11-21T18:11:43.3983790Z [===============                        ] 40% Installing Android SDK Build-Tools
2025-11-21T18:11:43.6338100Z [===============                        ] 40% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:43.7620680Z [================                       ] 40% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:43.9011160Z [================                       ] 41% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:44.2536300Z [================                       ] 42% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:44.3543290Z [=================                      ] 43% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:44.4548100Z [=================                      ] 44% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:44.5552540Z [=================                      ] 45% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:44.6558240Z [==================                     ] 45% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:44.7563140Z [==================                     ] 46% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:44.8564070Z [==================                     ] 47% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:44.8949620Z [==================                     ] 48% Downloading f6d24b187cc6bd534c6c37
2025-11-21T18:11:44.9107460Z [==================                     ] 48% Unzipping... x86_64/VerifiedBootPa
2025-11-21T18:11:44.9192790Z [==================                     ] 48% Unzipping... android-11/          
2025-11-21T18:11:44.9264520Z [==================                     ] 48% Unzipping... android-11/aapt      
2025-11-21T18:11:44.9390420Z [===================                    ] 48% Unzipping... android-11/aapt      
2025-11-21T18:11:44.9405490Z [===================                    ] 48% Unzipping... android-11/aapt2     
2025-11-21T18:11:44.9437790Z [===================                    ] 48% Unzipping... android-11/aarch64-li
2025-11-21T18:11:44.9500770Z [===================                    ] 48% Unzipping... android-11/aidl      
2025-11-21T18:11:44.9588310Z [===================                    ] 48% Unzipping... android-11/apksigner 
2025-11-21T18:11:44.9688500Z [===================                    ] 48% Unzipping... android-11/arm-linux-
2025-11-21T18:11:44.9766730Z [===================                    ] 48% Unzipping... android-11/bcc_compat
2025-11-21T18:11:44.9779880Z [===================                    ] 48% Unzipping... android-11/core-lambd
2025-11-21T18:11:44.9811450Z [===================                    ] 48% Unzipping... android-11/d8        
2025-11-21T18:11:44.9896590Z [===================                    ] 48% Unzipping... android-11/dexdump   
2025-11-21T18:11:45.0193750Z [===================                    ] 48% Unzipping... android-11/dx        
2025-11-21T18:11:45.0454180Z [===================                    ] 48% Unzipping... android-11/i686-linux
2025-11-21T18:11:45.0458640Z [===================                    ] 48% Unzipping... android-11/lib/      
2025-11-21T18:11:45.0463020Z [===================                    ] 48% Unzipping... android-11/lib/apksig
2025-11-21T18:11:45.0734710Z [===================                    ] 48% Unzipping... android-11/lib/d8.jar
2025-11-21T18:11:45.0900950Z [===================                    ] 49% Unzipping... android-11/lib/d8.jar
2025-11-21T18:11:45.1052780Z [===================                    ] 49% Unzipping... android-11/lib/dx.jar
2025-11-21T18:11:45.1068330Z [===================                    ] 49% Unzipping... android-11/lib/shrink
2025-11-21T18:11:45.1077110Z [===================                    ] 49% Unzipping... android-11/lib64/    
2025-11-21T18:11:45.1595010Z [===================                    ] 49% Unzipping... android-11/lib64/liba
2025-11-21T18:11:45.1692420Z [===================                    ] 49% Unzipping... android-11/lib64/libb
2025-11-21T18:11:45.2422500Z [===================                    ] 49% Unzipping... android-11/lib64/libc
2025-11-21T18:11:45.3477590Z [===================                    ] 50% Unzipping... android-11/lib64/libc
2025-11-21T18:11:45.4094000Z [====================                   ] 50% Unzipping... android-11/lib64/libc
2025-11-21T18:11:45.4402890Z [====================                   ] 50% Unzipping... android-11/lib64/libL
2025-11-21T18:11:45.6805920Z [====================                   ] 51% Unzipping... android-11/lib64/libL
2025-11-21T18:11:45.8728990Z [====================                   ] 52% Unzipping... android-11/lib64/libL
2025-11-21T18:11:45.9735630Z [====================                   ] 52% Unzipping... android-11/lld       
2025-11-21T18:11:46.0739300Z [====================                   ] 52% Unzipping... android-11/lld-bin/  
2025-11-21T18:11:46.0865220Z [====================                   ] 52% Unzipping... android-11/lld-bin/ll
2025-11-21T18:11:46.2334430Z [=====================                  ] 53% Unzipping... android-11/lld-bin/ll
2025-11-21T18:11:46.2682220Z [=====================                  ] 54% Unzipping... android-11/lld-bin/ll
2025-11-21T18:11:46.2823060Z [=====================                  ] 54% Unzipping... android-11/llvm-rs-cc
2025-11-21T18:11:46.2850580Z [=====================                  ] 54% Unzipping... android-11/mainDexCla
2025-11-21T18:11:46.2865370Z [=====================                  ] 54% Unzipping... android-11/mipsel-lin
2025-11-21T18:11:46.3088730Z [=====================                  ] 54% Unzipping... android-11/NOTICE.txt
2025-11-21T18:11:46.5505910Z [=====================                  ] 54% Unzipping... android-11/renderscri
2025-11-21T18:11:46.6859510Z [=====================                  ] 55% Unzipping... android-11/renderscri
2025-11-21T18:11:46.7018160Z [=====================                  ] 55% Unzipping... android-11/runtime.pr
2025-11-21T18:11:46.7021150Z [=====================                  ] 55% Unzipping... android-11/source.pro
2025-11-21T18:11:46.7023740Z [=====================                  ] 55% Unzipping... android-11/split-sele
2025-11-21T18:11:46.7026420Z [=====================                  ] 55% Unzipping... android-11/x86_64-lin
2025-11-21T18:11:46.7029250Z [=====================                  ] 55% Unzipping... android-11/zipalign  
2025-11-21T18:11:46.7031770Z [===========================            ] 70% Unzipping... android-11/zipalign  
2025-11-21T18:11:46.7836750Z [===========================            ] 70% Installing Android SDK Platform 30
2025-11-21T18:11:46.8846240Z [===========================            ] 70% Downloading platform-30_r03.zip...
2025-11-21T18:11:46.9850700Z [============================           ] 70% Downloading platform-30_r03.zip...
2025-11-21T18:11:47.0753120Z [============================           ] 71% Downloading platform-30_r03.zip...
2025-11-21T18:11:47.1757940Z [============================           ] 72% Downloading platform-30_r03.zip...
2025-11-21T18:11:47.2761840Z [=============================          ] 73% Downloading platform-30_r03.zip...
2025-11-21T18:11:47.3765330Z [=============================          ] 74% Downloading platform-30_r03.zip...
2025-11-21T18:11:47.4771880Z [=============================          ] 75% Downloading platform-30_r03.zip...
2025-11-21T18:11:47.5369040Z [==============================         ] 75% Downloading platform-30_r03.zip...
2025-11-21T18:11:47.5860110Z [==============================         ] 76% Downloading platform-30_r03.zip...
2025-11-21T18:11:47.5904580Z [==============================         ] 77% Downloading platform-30_r03.zip...
2025-11-21T18:11:48.6060700Z [==============================         ] 77% Unzipping... android-11/zipalign  
2025-11-21T18:11:48.6547230Z [==============================         ] 77% Unzipping... android-11/          
2025-11-21T18:11:48.6600050Z [==============================         ] 77% Unzipping... android-11/android.ja
2025-11-21T18:11:48.6680760Z [===============================        ] 78% Unzipping... android-11/android.ja
2025-11-21T18:11:48.6916870Z [===============================        ] 79% Unzipping... android-11/android.ja
2025-11-21T18:11:48.7196290Z [===============================        ] 80% Unzipping... android-11/android.ja
2025-11-21T18:11:48.7449720Z [================================       ] 80% Unzipping... android-11/android.ja
2025-11-21T18:11:48.7483820Z [================================       ] 80% Unzipping... android-11/optional/ 
2025-11-21T18:11:48.7514100Z [================================       ] 80% Unzipping... android-11/optional/a
2025-11-21T18:11:48.7535720Z [================================       ] 80% Unzipping... android-11/optional/o
2025-11-21T18:11:48.7560270Z [================================       ] 80% Unzipping... android-11/optional/a
2025-11-21T18:11:48.7640560Z [================================       ] 80% Unzipping... android-11/optional/o
2025-11-21T18:11:48.7876710Z [================================       ] 80% Unzipping... android-11/templates/
2025-11-21T18:11:48.8333240Z [================================       ] 80% Unzipping... android-11/core-for-s
2025-11-21T18:11:48.8369640Z [================================       ] 81% Unzipping... android-11/core-for-s
2025-11-21T18:11:48.8444020Z [================================       ] 81% Unzipping... android-11/build.prop
2025-11-21T18:11:48.9052790Z [================================       ] 81% Unzipping... android-11/android-st
2025-11-21T18:11:48.9311200Z [================================       ] 81% Unzipping... android-11/uiautomato
2025-11-21T18:11:48.9313310Z [================================       ] 81% Unzipping... android-11/source.pro
2025-11-21T18:11:48.9314930Z [================================       ] 81% Unzipping... android-11/data/     
2025-11-21T18:11:48.9318260Z [================================       ] 81% Unzipping... android-11/data/servi
2025-11-21T18:11:48.9321360Z [================================       ] 81% Unzipping... android-11/data/NOTIC
2025-11-21T18:11:49.0156600Z [================================       ] 81% Unzipping... android-11/data/widge
2025-11-21T18:11:49.0160910Z [================================       ] 81% Unzipping... android-11/data/broad
2025-11-21T18:11:49.0534520Z [================================       ] 81% Unzipping... android-11/data/api-v
2025-11-21T18:11:49.0544780Z [================================       ] 81% Unzipping... android-11/data/featu
2025-11-21T18:11:49.0573910Z [================================       ] 81% Unzipping... android-11/data/annot
2025-11-21T18:11:49.0581370Z [================================       ] 81% Unzipping... android-11/data/res/ 
2025-11-21T18:11:49.0636380Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:49.0674580Z [================================       ] 81% Unzipping... android-11/data/res/l
2025-11-21T18:11:49.1391550Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:49.1401010Z [================================       ] 81% Unzipping... android-11/data/res/m
2025-11-21T18:11:49.1723830Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:49.1782950Z [================================       ] 81% Unzipping... android-11/data/res/a
2025-11-21T18:11:49.2304930Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:49.3654790Z [================================       ] 81% Unzipping... android-11/data/res/d
2025-11-21T18:11:49.3840120Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:49.3853890Z [================================       ] 81% Unzipping... android-11/data/res/x
2025-11-21T18:11:49.3916530Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:49.3926040Z [================================       ] 81% Unzipping... android-11/data/res/l
2025-11-21T18:11:49.3930180Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:49.5881780Z [================================       ] 81% Unzipping... android-11/data/res/l
2025-11-21T18:11:49.6132210Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:49.6153140Z [================================       ] 81% Unzipping... android-11/data/res/r
2025-11-21T18:11:49.7285040Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:49.8287920Z [================================       ] 81% Unzipping... android-11/data/res/x
2025-11-21T18:11:49.9291030Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:49.9830890Z [================================       ] 81% Unzipping... android-11/data/res/r
2025-11-21T18:11:50.0259000Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:50.1265960Z [================================       ] 81% Unzipping... android-11/data/res/a
2025-11-21T18:11:50.2266330Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:50.3269740Z [================================       ] 81% Unzipping... android-11/data/res/r
2025-11-21T18:11:50.4084780Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:50.4148600Z [================================       ] 81% Unzipping... android-11/data/res/c
2025-11-21T18:11:50.4198370Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-21T18:11:50.7030720Z [================================       ] 81% Unzipping... android-11/data/res/d
2025-11-21T18:11:51.6374520Z [================================       ] 82% Unzipping... android-11/data/res/d
2025-11-21T18:11:51.6869640Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:51.7340080Z [================================       ] 82% Unzipping... android-11/data/res/t
2025-11-21T18:11:51.7554770Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:51.7580950Z [================================       ] 82% Unzipping... android-11/data/res/x
2025-11-21T18:11:51.7601230Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:51.8605450Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:51.9476210Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:51.9527290Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:51.9624540Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:51.9663480Z [================================       ] 82% Unzipping... android-11/data/res/l
2025-11-21T18:11:51.9696810Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:51.9734840Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:51.9735970Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:51.9792990Z [================================       ] 82% Unzipping... android-11/data/res/d
2025-11-21T18:11:51.9831330Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:51.9843430Z [================================       ] 82% Unzipping... android-11/data/res/d
2025-11-21T18:11:52.1884330Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.2225700Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:52.2240790Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.2296550Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:52.2902910Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.2908770Z [================================       ] 82% Unzipping... android-11/data/res/m
2025-11-21T18:11:52.2944940Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.2961390Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:52.3040140Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.3056070Z [================================       ] 82% Unzipping... android-11/data/res/c
2025-11-21T18:11:52.3075540Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.3091940Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:52.3174870Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.3181340Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:52.3245510Z [================================       ] 82% Unzipping... android-11/data/res/x
2025-11-21T18:11:52.3697770Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.7273040Z [================================       ] 82% Unzipping... android-11/data/res/d
2025-11-21T18:11:52.7439000Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.7448650Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:52.7882110Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.7892120Z [================================       ] 82% Unzipping... android-11/data/res/m
2025-11-21T18:11:52.8078100Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.8088400Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:52.8565540Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.8578120Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-21T18:11:52.8711420Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:52.8734950Z [================================       ] 82% Unzipping... android-11/data/res/i
2025-11-21T18:11:52.9001550Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:53.0024860Z [================================       ] 82% Unzipping... android-11/data/res/d
2025-11-21T18:11:53.1028010Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-21T18:11:53.2030780Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:53.2287270Z [=================================      ] 83% Unzipping... android-11/data/res/m
2025-11-21T18:11:53.2290020Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:53.7295500Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-21T18:11:53.7618720Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:53.9630930Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-21T18:11:53.9755530Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:53.9778220Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-21T18:11:53.9887370Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:54.0866690Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-21T18:11:54.0929280Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:54.0972310Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-21T18:11:54.0999160Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:54.1011390Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-21T18:11:54.1018480Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:54.1084850Z [=================================      ] 83% Unzipping... android-11/data/res/x
2025-11-21T18:11:54.2176590Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:54.2186380Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-21T18:11:54.2608530Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:55.1127200Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-21T18:11:55.2386550Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:55.2408510Z [=================================      ] 83% Unzipping... android-11/data/res/a
2025-11-21T18:11:55.5058160Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:55.6060030Z [=================================      ] 83% Unzipping... android-11/data/res/r
2025-11-21T18:11:55.7063190Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:55.7440900Z [=================================      ] 83% Unzipping... android-11/data/res/m
2025-11-21T18:11:55.7484450Z [=================================      ] 83% Unzipping... android-11/data/res/x
2025-11-21T18:11:55.7690600Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:55.7708760Z [=================================      ] 83% Unzipping... android-11/data/res/a
2025-11-21T18:11:55.7724150Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:55.7736500Z [=================================      ] 83% Unzipping... android-11/data/res/i
2025-11-21T18:11:55.7747890Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-21T18:11:55.9976430Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:55.9989920Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-21T18:11:56.0121460Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.0134730Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-21T18:11:56.0182850Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.0193710Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-21T18:11:56.0616000Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.0649490Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-21T18:11:56.0690340Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.0700730Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-21T18:11:56.3133160Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.3316990Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-21T18:11:56.3318850Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.3322730Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-21T18:11:56.3626160Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.3643380Z [=================================      ] 84% Unzipping... android-11/data/res/m
2025-11-21T18:11:56.3924410Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.4621400Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-21T18:11:56.5632640Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.6636410Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-21T18:11:56.6864910Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.6903070Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-21T18:11:56.6908170Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:56.6918210Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-21T18:11:56.9975820Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:57.0979430Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-21T18:11:57.1853990Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:57.2021060Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-21T18:11:57.2062350Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:57.2099990Z [=================================      ] 84% Unzipping... android-11/data/res/c
2025-11-21T18:11:57.2148460Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:57.2462990Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-21T18:11:57.2535000Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:58.7830020Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-21T18:11:58.8055510Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:58.8075310Z [=================================      ] 84% Unzipping... android-11/data/res/m
2025-11-21T18:11:58.8362320Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:58.8384690Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-21T18:11:58.8401810Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:58.8416510Z [=================================      ] 84% Unzipping... android-11/data/res/m
2025-11-21T18:11:58.8496490Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:58.8510380Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-21T18:11:58.8550090Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-21T18:11:58.8661840Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:58.8678980Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-21T18:11:58.8823540Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:59.3639370Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-21T18:11:59.4536070Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:59.4553630Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-21T18:11:59.4894220Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:59.4970190Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-21T18:11:59.5017090Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:59.5062550Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-21T18:11:59.5540640Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-21T18:11:59.5546270Z [=================================      ] 84% Unzipping... android-11/data/categ
2025-11-21T18:11:59.5553860Z [=================================      ] 84% Unzipping... android-11/data/activ
2025-11-21T18:11:59.5572010Z [=================================      ] 84% Unzipping... android-11/sdk.proper
2025-11-21T18:11:59.5577150Z [=================================      ] 84% Unzipping... android-11/skins/    
2025-11-21T18:11:59.5657500Z [=================================      ] 84% Unzipping... android-11/skins/WXGA
2025-11-21T18:11:59.5752990Z [=================================      ] 84% Unzipping... android-11/skins/WQVG
2025-11-21T18:11:59.5900600Z [=================================      ] 84% Unzipping... android-11/skins/NOTI
2025-11-21T18:11:59.6011240Z [=================================      ] 84% Unzipping... android-11/skins/HVGA
2025-11-21T18:11:59.6039930Z [=================================      ] 84% Unzipping... android-11/skins/WVGA
2025-11-21T18:11:59.6163880Z [=================================      ] 84% Unzipping... android-11/skins/WQVG
2025-11-21T18:11:59.6221330Z [=================================      ] 85% Unzipping... android-11/skins/WQVG
2025-11-21T18:11:59.6250160Z [=================================      ] 85% Unzipping... android-11/skins/WVGA
2025-11-21T18:11:59.6332770Z [=================================      ] 85% Unzipping... android-11/skins/QVGA
2025-11-21T18:11:59.6551380Z [=================================      ] 85% Unzipping... android-11/skins/WXGA
2025-11-21T18:11:59.6554260Z [=================================      ] 85% Unzipping... android-11/skins/WSVG
2025-11-21T18:11:59.6576780Z [=================================      ] 85% Unzipping... android-11/skins/WXGA
2025-11-21T18:11:59.6644530Z [=================================      ] 85% Unzipping... android-11/framework.
2025-11-21T18:11:59.6813800Z [=======================================] 100% Unzipping... android-11/framework
2025-11-21T18:11:59.6816810Z 
2025-11-21T18:11:59.7233960Z ✅ SDK components installation completed
2025-11-21T18:12:04.8548440Z 🔍 Verifying system image installation...
2025-11-21T18:12:04.8960590Z Checking path: /Users/runner/Library/Android/sdk/system-images/android-30/google_apis_playstore/x86_64
2025-11-21T18:12:04.9149990Z ✅ Google Play system image found!
2025-11-21T18:12:04.9250480Z total 5947336
2025-11-21T18:12:04.9256190Z drwxr-xr-x  15 runner  staff         480 Nov 21 18:11 .
2025-11-21T18:12:04.9261650Z drwxr-xr-x   3 runner  staff          96 Nov 21 18:11 ..
2025-11-21T18:12:04.9273520Z -rw-r--r--   1 runner  staff     2936563 Nov 21 18:10 NOTICE.txt
2025-11-21T18:12:04.9276190Z -rw-r--r--   1 runner  staff         356 Nov 21 18:11 VerifiedBootParams.textproto
2025-11-21T18:12:04.9279090Z -rw-r--r--   1 runner  staff         424 Nov 21 18:10 advancedFeatures.ini
2025-11-21T18:12:04.9287630Z -rw-r--r--   1 runner  staff        2095 Nov 21 18:10 build.prop
2025-11-21T18:12:04.9294890Z drwxr-xr-x   5 runner  staff         160 Nov 21 18:10 data
2025-11-21T18:12:04.9309480Z -rw-r--r--   1 runner  staff    18874368 Nov 21 18:10 encryptionkey.img
2025-11-21T18:12:04.9312960Z -rw-r--r--   1 runner  staff    16559680 Nov 21 18:10 kernel-ranchu
2025-11-21T18:12:04.9316010Z -rw-r--r--   1 runner  staff       19113 Nov 21 18:11 package.xml
2025-11-21T18:12:04.9332300Z -rw-r--r--   1 runner  staff     1346686 Nov 21 18:10 ramdisk.img
2025-11-21T18:12:04.9373000Z -rw-r--r--   1 runner  staff         304 Nov 21 18:10 source.properties
2025-11-21T18:12:04.9374420Z -rw-r--r--   1 runner  staff  2832203776 Nov 21 18:11 system.img
2025-11-21T18:12:04.9375360Z -rw-r--r--   1 runner  staff     1048576 Nov 21 18:11 userdata.img
2025-11-21T18:12:04.9376020Z -rw-r--r--   1 runner  staff   167772160 Nov 21 18:11 vendor.img
2025-11-21T18:12:04.9377090Z 🔧 Verifying ADB...
2025-11-21T18:12:05.1356100Z Android Debug Bridge version 1.0.41
2025-11-21T18:12:05.1469030Z Version 36.0.0-13206524
2025-11-21T18:12:05.1474430Z Installed as /Users/runner/Library/Android/sdk/platform-tools/adb
2025-11-21T18:12:05.1480000Z Running on Darwin 22.6.0 (x86_64)
2025-11-21T18:12:05.1485300Z 📋 Installed system images:
2025-11-21T18:12:07.9440410Z   system-images;android-30;google_apis_playstore;x86_64 | 10            | Google Play Intel x86_64 Atom System Image | system-images/android-30/google_apis_playstore/x86_64
2025-11-21T18:12:07.9828600Z 
2025-11-21T18:12:07.9845320Z 📱 Creating Android Emulator with Google Play Store...
2025-11-21T18:12:08.6778740Z Creating emulator with Google Play Store support...
2025-11-21T18:12:11.1484320Z Loading local repository...                                                     
2025-11-21T18:12:11.1808310Z [=========                              ] 25% Loading local repository...       
2025-11-21T18:12:11.1871370Z [=========                              ] 25% Fetch remote repository...        
2025-11-21T18:12:11.2195180Z [=======================================] 100% Fetch remote repository...       
2025-11-21T18:12:12.8124340Z 🔍 Verifying emulator creation...
2025-11-21T18:12:13.1172440Z test_emulator_playstore
2025-11-21T18:12:13.2635180Z ✅ Emulator 'test_emulator_playstore' created successfully
2025-11-21T18:12:13.2884540Z 🚀 Starting emulator...
2025-11-21T18:12:13.3039510Z Emulator PID: 29429
2025-11-21T18:12:13.3197580Z ⏳ Waiting for emulator to be online...
2025-11-21T18:12:13.3224580Z * daemon not running; starting now at tcp:5037
2025-11-21T18:12:16.7094790Z * daemon started successfully
2025-11-21T19:46:52.9490930Z ⏳ Waiting for boot to complete...
2025-11-21T19:46:53.5618650Z ✅ Boot completed! Waiting for system to stabilize...
2025-11-21T19:47:23.7121230Z ⏳ Waiting for package manager service...
2025-11-21T19:47:24.2504710Z ✅ Package manager is ready
2025-11-21T19:47:24.2517980Z 📱 Emulator status:
2025-11-21T19:47:24.2910130Z List of devices attached
2025-11-21T19:47:24.2913280Z emulator-5554          device product:sdk_gphone_x86_64 model:sdk_gphone_x86_64 device:generic_x86_64_arm64 transport_id:1
2025-11-21T19:47:24.2914200Z 
2025-11-21T19:47:24.4544060Z Android version: 11
2025-11-21T19:47:24.7250230Z API Level: 30
2025-11-21T19:47:24.7254600Z 🔍 Checking for Google Play Store...
2025-11-21T19:47:25.4547250Z ✅ Google Play Store is present!
2025-11-21T19:47:27.7762900Z Play Store: versionName=48.8.07-29
2025-11-21T19:47:27.8206940Z Emulator Serial: emulator-5554
2025-11-21T19:47:27.8274650Z 
2025-11-21T19:47:27.8275530Z ✅ Android emulator setup complete!
2025-11-21T19:47:27.8730090Z 
2025-11-21T19:47:27.9576900Z ##[section]Finishing: Setup Android SDK and Create Emulator with Google Play