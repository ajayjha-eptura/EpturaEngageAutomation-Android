2025-11-22T14:26:22.7857660Z ##[section]Starting: Setup Android SDK and Create Emulator with Google Play
2025-11-22T14:26:22.7870800Z ==============================================================================
2025-11-22T14:26:22.7871080Z Task         : Bash
2025-11-22T14:26:22.7871240Z Description  : Run a Bash script on macOS, Linux, or Windows
2025-11-22T14:26:22.7871430Z Version      : 3.259.0
2025-11-22T14:26:22.7871620Z Author       : Microsoft Corporation
2025-11-22T14:26:22.7871790Z Help         : https://docs.microsoft.com/azure/devops/pipelines/tasks/utility/bash
2025-11-22T14:26:22.7872050Z ==============================================================================
2025-11-22T14:26:23.1059010Z Generating script.
2025-11-22T14:26:23.1190370Z ========================== Starting Command Output ===========================
2025-11-22T14:26:23.4829120Z [command]/bin/bash /Users/runner/work/_temp/bfbd22b0-02d0-47f6-a668-20fb24c613e8.sh
2025-11-22T14:26:23.4852670Z 📱 Configuring Android SDK with Google Play support...
2025-11-22T14:26:23.4881520Z ANDROID_HOME: /Users/runner/Library/Android/sdk
2025-11-22T14:26:23.5883260Z ANDROID_SDK_ROOT: /Users/runner/Library/Android/sdk
2025-11-22T14:26:23.6712450Z 📋 Android SDK structure:
2025-11-22T14:26:23.6751920Z total 48
2025-11-22T14:26:23.6786950Z drwxr-xr-x  15 runner  staff    480 Nov 11 13:59 .
2025-11-22T14:26:23.6812170Z drwxr-xr-x   3 runner  staff     96 Nov 11 13:53 ..
2025-11-22T14:26:23.6824800Z -rw-r--r--   1 runner  staff     16 Nov 11 14:10 .knownPackages
2025-11-22T14:26:23.6832800Z drwxr-xr-x   2 runner  staff     64 Nov 11 13:58 .temp
2025-11-22T14:26:23.6841580Z drwxr-xr-x   9 runner  staff    288 Nov 11 13:57 build-tools
2025-11-22T14:26:23.6877830Z drwxr-xr-x   4 runner  staff    128 Nov 11 13:58 cmake
2025-11-22T14:26:23.6887440Z drwxr-xr-x   3 runner  staff     96 Nov 11 13:53 cmdline-tools
2025-11-22T14:26:23.6906110Z drwxr-xr-x  29 runner  staff    928 Nov 11 13:54 emulator
2025-11-22T14:26:23.6913650Z drwxr-xr-x   4 runner  staff    128 Nov 11 13:58 extras
2025-11-22T14:26:23.7035150Z drwxr-xr-x   3 runner  staff     96 Nov 11 13:53 licenses
2025-11-22T14:26:23.7070150Z drwxr-xr-x   6 runner  staff    192 Nov 11 13:56 ndk
2025-11-22T14:26:23.7081150Z -rw-r--r--   1 runner  staff  19099 Nov 11 13:59 packages-list.txt
2025-11-22T14:26:23.7094360Z drwxr-xr-x  15 runner  staff    480 Nov 11 13:54 platform-tools
2025-11-22T14:26:23.7105660Z drwxr-xr-x  17 runner  staff    544 Nov 11 13:58 platforms
2025-11-22T14:26:23.7112120Z drwxr-xr-x  14 runner  staff    448 Nov 11 13:59 tools
2025-11-22T14:26:23.7127130Z 📝 Accepting Android SDK licenses...
2025-11-22T14:26:25.7881790Z Loading local repository...                                                     
2025-11-22T14:26:25.8200470Z [=========                              ] 25% Loading local repository...       
2025-11-22T14:26:26.9191810Z [=========                              ] 25% Fetch remote repository...        
2025-11-22T14:26:28.2979650Z [==========                             ] 26% Fetch remote repository...        
2025-11-22T14:26:28.3983870Z [============                           ] 31% Fetch remote repository...        
2025-11-22T14:26:28.4708480Z [============                           ] 32% Fetch remote repository...        
2025-11-22T14:26:28.4904460Z [=============                          ] 33% Fetch remote repository...        
2025-11-22T14:26:28.5075080Z [=============                          ] 35% Fetch remote repository...        
2025-11-22T14:26:28.6077560Z [==============                         ] 36% Fetch remote repository...        
2025-11-22T14:26:28.6243970Z [==============                         ] 37% Fetch remote repository...        
2025-11-22T14:26:28.6460870Z [===============                        ] 38% Fetch remote repository...        
2025-11-22T14:26:28.7073900Z [===============                        ] 39% Fetch remote repository...        
2025-11-22T14:26:28.7280660Z [================                       ] 40% Fetch remote repository...        
2025-11-22T14:26:28.7536220Z [================                       ] 41% Fetch remote repository...        
2025-11-22T14:26:28.7624990Z [================                       ] 42% Fetch remote repository...        
2025-11-22T14:26:28.7788190Z [=================                      ] 44% Fetch remote repository...        
2025-11-22T14:26:28.7818440Z [=================                      ] 45% Fetch remote repository...        
2025-11-22T14:26:28.7869160Z [==================                     ] 46% Fetch remote repository...        
2025-11-22T14:26:28.7913040Z [==================                     ] 47% Fetch remote repository...        
2025-11-22T14:26:28.7968790Z [===================                    ] 48% Fetch remote repository...        
2025-11-22T14:26:28.8086810Z [===================                    ] 49% Fetch remote repository...        
2025-11-22T14:26:28.8325160Z [====================                   ] 50% Fetch remote repository...        
2025-11-22T14:26:28.8383090Z [====================                   ] 51% Fetch remote repository...        
2025-11-22T14:26:28.8615080Z [====================                   ] 53% Fetch remote repository...        
2025-11-22T14:26:28.8685150Z [=====================                  ] 54% Fetch remote repository...        
2025-11-22T14:26:28.8756750Z [=====================                  ] 55% Fetch remote repository...        
2025-11-22T14:26:28.8819590Z [======================                 ] 56% Fetch remote repository...        
2025-11-22T14:26:28.8896500Z [======================                 ] 57% Fetch remote repository...        
2025-11-22T14:26:28.8947130Z [=======================                ] 58% Fetch remote repository...        
2025-11-22T14:26:28.9602500Z [=======================                ] 59% Fetch remote repository...        
2025-11-22T14:26:28.9715510Z [========================               ] 60% Fetch remote repository...        
2025-11-22T14:26:28.9851800Z [========================               ] 61% Fetch remote repository...        
2025-11-22T14:26:28.9946990Z [=========================              ] 63% Fetch remote repository...        
2025-11-22T14:26:29.0040810Z [=========================              ] 64% Fetch remote repository...        
2025-11-22T14:26:29.0081720Z [=========================              ] 65% Fetch remote repository...        
2025-11-22T14:26:29.0190160Z [==========================             ] 66% Fetch remote repository...        
2025-11-22T14:26:29.0261650Z [==========================             ] 67% Fetch remote repository...        
2025-11-22T14:26:29.0625440Z [===========================            ] 68% Fetch remote repository...        
2025-11-22T14:26:29.0866870Z [===========================            ] 69% Fetch remote repository...        
2025-11-22T14:26:29.1017660Z [============================           ] 70% Fetch remote repository...        
2025-11-22T14:26:29.1255760Z [============================           ] 72% Fetch remote repository...        
2025-11-22T14:26:29.1401420Z [=============================          ] 73% Fetch remote repository...        
2025-11-22T14:26:29.1508490Z [=============================          ] 74% Fetch remote repository...        
2025-11-22T14:26:29.1614680Z [=============================          ] 75% Fetch remote repository...        
2025-11-22T14:26:29.1733770Z [=============================          ] 75% Computing updates...              
2025-11-22T14:26:29.1812000Z [=======================================] 100% Computing updates...             
2025-11-22T14:26:29.2466940Z 6 of 7 SDK package licenses not accepted.
2025-11-22T14:26:29.2528560Z Review licenses that have not been accepted (y/N)? 
2025-11-22T14:26:29.2608420Z 1/6: License android-googletv-license:
2025-11-22T14:26:29.2715530Z ---------------------------------------
2025-11-22T14:26:29.2786860Z Terms and Conditions
2025-11-22T14:26:29.3084710Z 
2025-11-22T14:26:29.3176750Z This is the Google TV Add-on for the Android Software Development Kit License Agreement.
2025-11-22T14:26:29.3299460Z 
2025-11-22T14:26:29.3363810Z 1. Introduction
2025-11-22T14:26:29.3369180Z 
2025-11-22T14:26:29.3371810Z 1.1 The Google TV Add-on for the Android Software Development Kit (referred to in this License Agreement as the "Google TV Add-on" and specifically including the Android system files, packaged APIs, and Google APIs add-ons) is licensed to you subject to the terms of this License Agreement. This License Agreement forms a legally binding contract between you and Google in relation to your use of the Google TV Add-on.
2025-11-22T14:26:29.3375220Z 
2025-11-22T14:26:29.3379530Z 1.2 "Google" means Google Inc., a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.
2025-11-22T14:26:29.3386460Z 
2025-11-22T14:26:29.3389180Z 2. Accepting this License Agreement
2025-11-22T14:26:29.3390200Z 
2025-11-22T14:26:29.3391770Z 2.1 In order to use the Google TV Add-on, you must first agree to this License Agreement. You may not use the Google TV Add-on if you do not accept this License Agreement.
2025-11-22T14:26:29.3394810Z 
2025-11-22T14:26:29.3396350Z 2.2 You can accept this License Agreement by:
2025-11-22T14:26:29.3397440Z 
2025-11-22T14:26:29.3398470Z (A) clicking to accept or agree to this License Agreement, where this option is made available to you; or
2025-11-22T14:26:29.3398850Z 
2025-11-22T14:26:29.3400190Z (B) by actually using the Google TV Add-on. In this case, you agree that use of the Google TV Add-on constitutes acceptance of the License Agreement from that point onwards.
2025-11-22T14:26:29.3402880Z 
2025-11-22T14:26:29.3403960Z 2.3 You may not use the Google TV Add-on and may not accept the Licensing Agreement if you are a person barred from receiving the Google TV Add-on under the laws of the United States or other countries including the country in which you are resident or from which you use the Google TV Add-on.
2025-11-22T14:26:29.3404590Z 
2025-11-22T14:26:29.3405460Z 2.4 If you are agreeing to be bound by this License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to this License Agreement. If you do not have the requisite authority, you may not accept the Licensing Agreement or use the Google TV Add-on on behalf of your employer or other entity.
2025-11-22T14:26:29.3406180Z 
2025-11-22T14:26:29.3406510Z 3. Google TV Add-on License from Google
2025-11-22T14:26:29.3406690Z 
2025-11-22T14:26:29.3407320Z 3.1 Subject to the terms of this License Agreement, Google grants you a limited, worldwide, royalty-free, non- assignable and non-exclusive license to use the Google TV Add-on solely to develop applications to run on the Google TV platform.
2025-11-22T14:26:29.3407760Z 
2025-11-22T14:26:29.3408680Z 3.2 You agree that Google or third parties own all legal right, title and interest in and to the Google TV Add-on, including any Intellectual Property Rights that subsist in the Google TV Add-on. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.
2025-11-22T14:26:29.3409390Z 
2025-11-22T14:26:29.3410630Z 3.3 Except to the extent required by applicable third party licenses, you may not copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the Google TV Add-on or any part of the Google TV Add-on. Except to the extent required by applicable third party licenses, you may not load any part of the Google TV Add-on onto a mobile handset, television, or any other hardware device except a personal computer, combine any part of the Google TV Add-on with other software, or distribute any software or device incorporating a part of the Google TV Add-on.
2025-11-22T14:26:29.3411680Z 
2025-11-22T14:26:29.3412290Z 3.4 Use, reproduction and distribution of components of the Google TV Add-on licensed under an open source software license are governed solely by the terms of that open source software license and not this License Agreement.
2025-11-22T14:26:29.3413560Z 
2025-11-22T14:26:29.3414710Z 3.5 You agree that the form and nature of the Google TV Add-on that Google provides may change without prior notice to you and that future versions of the Google TV Add-on may be incompatible with applications developed on previous versions of the Google TV Add-on. You agree that Google may stop (permanently or temporarily) providing the Google TV Add-on (or any features within the Google TV Add-on) to you or to users generally at Google's sole discretion, without prior notice to you.
2025-11-22T14:26:29.3415550Z 
2025-11-22T14:26:29.3416600Z 3.6 Nothing in this License Agreement gives you a right to use any of Google's or it’s licensors’ trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.
2025-11-22T14:26:29.3417060Z 
2025-11-22T14:26:29.3417960Z 3.7 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the Google TV Add-on.
2025-11-22T14:26:29.3418880Z 
2025-11-22T14:26:29.3419370Z 4. Use of the Google TV Add-on by You
2025-11-22T14:26:29.3419630Z 
2025-11-22T14:26:29.3420410Z 4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under this License Agreement in or to any software applications that you develop using the Google TV Add-on, including any intellectual property rights that subsist in those applications.
2025-11-22T14:26:29.3420960Z 
2025-11-22T14:26:29.3421780Z 4.2 You agree to use the Google TV Add-on and write applications only for purposes that are permitted by (a) this License Agreement and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).
2025-11-22T14:26:29.3422450Z 
2025-11-22T14:26:29.3423920Z 4.3 You agree that if you use the Google TV Add-on to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, your must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you explicit permission to do so.
2025-11-22T14:26:29.3425210Z 
2025-11-22T14:26:29.3426760Z 4.4 You agree that you will not engage in any activity with the Google TV Add-on, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google, Multichannel Video Program Distributors or any mobile communications carrier.
2025-11-22T14:26:29.3427600Z 
2025-11-22T14:26:29.3428490Z 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through the Google TV platform and/or applications for the Google TV platform, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.
2025-11-22T14:26:29.3429310Z 
2025-11-22T14:26:29.3430230Z 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under this License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.
2025-11-22T14:26:29.3431840Z 
2025-11-22T14:26:29.3432220Z 5. Your Developer Credentials
2025-11-22T14:26:29.3432360Z 
2025-11-22T14:26:29.3433100Z 5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.
2025-11-22T14:26:29.3433680Z 
2025-11-22T14:26:29.3434090Z 6. Privacy and Information
2025-11-22T14:26:29.3434260Z 
2025-11-22T14:26:29.3435410Z 6.1 In order to continually innovate and improve the Google TV Add-on, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the Google TV Add-on are being used and how they are being used. Before any of this information is collected, the Google TV Add-on will notify you and seek your consent. If you withhold consent, the information will not be collected.
2025-11-22T14:26:29.3437010Z 
2025-11-22T14:26:29.3437970Z 6.2 The data collected is examined in the aggregate to improve the Google TV Add-on and is maintained in accordance with Google's Privacy Policy.
2025-11-22T14:26:29.3438440Z 
2025-11-22T14:26:29.3438950Z 7. Third Party Applications for the Google TV Platform
2025-11-22T14:26:29.3439190Z 
2025-11-22T14:26:29.3440900Z 7.1 If you use the Google TV Add-on to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources.
2025-11-22T14:26:29.3442170Z 
2025-11-22T14:26:29.3443650Z 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners.
2025-11-22T14:26:29.3444640Z 
2025-11-22T14:26:29.3445580Z 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, this License Agreement does not affect your legal relationship with these third parties.
2025-11-22T14:26:29.3446220Z 
2025-11-22T14:26:29.3446680Z 8. Using Google TV APIs
2025-11-22T14:26:29.3446850Z 
2025-11-22T14:26:29.3449540Z 8.1 If you use any Google TV API to retrieve data from Google, you acknowledge that the data (“Google TV API Content”) may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service. Some portions of the Google TV API Content are licensed to Google by third parties, including but not limited to Tribune Media Services
2025-11-22T14:26:29.3451090Z 
2025-11-22T14:26:29.3452010Z 8.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-22T14:26:29.3454380Z 
2025-11-22T14:26:29.3454940Z 8.3 Except as explicitly permitted in Section 3 (Google TV Add-on License from Google), you must:
2025-11-22T14:26:29.3455320Z 
2025-11-22T14:26:29.3455910Z (a) not modify nor format the Google TV API Content except to the extent reasonably and technically necessary to optimize the display such Google TV API Content in your application;
2025-11-22T14:26:29.3456280Z 
2025-11-22T14:26:29.3456920Z (b) not edit the Google TV API Content in a manner that renders the Google TV API Content inaccurate of alters its inherent meaning (provided that displaying excerpts will not violate the foregoing); or
2025-11-22T14:26:29.3457330Z 
2025-11-22T14:26:29.3457980Z (c) not create any commercial audience measurement tool or service using the Google TV API Content
2025-11-22T14:26:29.3458730Z 
2025-11-22T14:26:29.3459160Z 9. Terminating this License Agreement
2025-11-22T14:26:29.3459320Z 
2025-11-22T14:26:29.3459770Z 9.1 This License Agreement will continue to apply until terminated by either you or Google as set out below.
2025-11-22T14:26:29.3460080Z 
2025-11-22T14:26:29.3460590Z 9.2 If you want to terminate this License Agreement, you may do so by ceasing your use of the Google TV Add-on and any relevant developer credentials.
2025-11-22T14:26:29.3460960Z 
2025-11-22T14:26:29.3461350Z 9.3 Google may at any time, terminate this License Agreement with you if:
2025-11-22T14:26:29.3461560Z 
2025-11-22T14:26:29.3461970Z (A) you have breached any provision of this License Agreement; or
2025-11-22T14:26:29.3462170Z 
2025-11-22T14:26:29.3462510Z (B) Google is required to do so by law; or
2025-11-22T14:26:29.3462700Z 
2025-11-22T14:26:29.3463330Z (C) the partner with whom Google offered certain parts of Google TV Add-on (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the Google TV Add-on to you; or
2025-11-22T14:26:29.3463920Z 
2025-11-22T14:26:29.3465040Z (D) Google decides to no longer providing the Google TV Add-on or certain parts of the Google TV Add-on to users in the country in which you are resident or from which you use the service, or the provision of the Google TV Add-on or certain Google TV Add-on services to you by Google is, in Google's sole discretion, no longer commercially viable.
2025-11-22T14:26:29.3465790Z 
2025-11-22T14:26:29.3466780Z 9.4 When this License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst this License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.
2025-11-22T14:26:29.3467580Z 
2025-11-22T14:26:29.3467900Z 10. DISCLAIMER OF WARRANTIES
2025-11-22T14:26:29.3468050Z 
2025-11-22T14:26:29.3468620Z 10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE GOOGLE TV ADD-ON IS AT YOUR SOLE RISK AND THAT THE GOOGLE TV ADD-ON IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.
2025-11-22T14:26:29.3469050Z 
2025-11-22T14:26:29.3469810Z 10.2 YOUR USE OF THE GOOGLE TV ADD-ON AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE GOOGLE TV ADD-ON IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE.
2025-11-22T14:26:29.3470380Z 
2025-11-22T14:26:29.3471050Z 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
2025-11-22T14:26:29.3471570Z 
2025-11-22T14:26:29.3472450Z 11. LIMITATION OF LIABILITY
2025-11-22T14:26:29.3472650Z 
2025-11-22T14:26:29.3473660Z 11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.
2025-11-22T14:26:29.3474750Z 
2025-11-22T14:26:29.3475300Z 12. Indemnification
2025-11-22T14:26:29.3475430Z 
2025-11-22T14:26:29.3476900Z 12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the Google TV Add-on, (b) any application you develop on the Google TV Add-on that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with this License Agreement.
2025-11-22T14:26:29.3478620Z 
2025-11-22T14:26:29.3478960Z 13. Changes to the License Agreement
2025-11-22T14:26:29.3479150Z 
2025-11-22T14:26:29.3479580Z 13.1 Google may make changes to the License Agreement as it distributes new versions of the Google TV Add-on.
2025-11-22T14:26:29.3479870Z 
2025-11-22T14:26:29.3480170Z 14. General Legal Terms
2025-11-22T14:26:29.3480330Z 
2025-11-22T14:26:29.3481170Z 14.1 This License Agreement constitute the whole legal agreement between you and Google and govern your use of the Google TV Add-on (excluding any services which Google may provide to you under a separate written agreement), and completely replace any prior agreements between you and Google in relation to the Google TV Add-on.
2025-11-22T14:26:29.3481760Z 
2025-11-22T14:26:29.3482540Z 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in this License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.
2025-11-22T14:26:29.3483150Z 
2025-11-22T14:26:29.3483960Z 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of this License Agreement is invalid, then that provision will be removed from this License Agreement without affecting the rest of this License Agreement. The remaining provisions of this License Agreement will continue to be valid and enforceable.
2025-11-22T14:26:29.3484740Z 
2025-11-22T14:26:29.3486450Z 14.4 You acknowledge and agree that Google’s API data licensors and each member of the group of companies of which Google is the parent shall be third party beneficiaries to this License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of this License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to this License Agreement.
2025-11-22T14:26:29.3487320Z 
2025-11-22T14:26:29.3488060Z 14.5 EXPORT RESTRICTIONS. THE GOOGLE TV ADD-ON IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE GOOGLE TV ADD-ON. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.
2025-11-22T14:26:29.3488610Z 
2025-11-22T14:26:29.3489380Z 14.6 The rights granted in this License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under this License Agreement without the prior written approval of the other party.
2025-11-22T14:26:29.3490470Z 
2025-11-22T14:26:29.3491630Z 14.7 This License Agreement, and your relationship with Google under this License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from this License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.
2025-11-22T14:26:29.3492570Z 
2025-11-22T14:26:29.3492660Z 
2025-11-22T14:26:29.3492950Z August 15, 2011
2025-11-22T14:26:29.3493340Z ---------------------------------------
2025-11-22T14:26:29.3493680Z Accept? (y/N): 
2025-11-22T14:26:29.3494020Z 2/6: License android-googlexr-license:
2025-11-22T14:26:29.3494680Z ---------------------------------------
2025-11-22T14:26:29.3495430Z To get started with the Android XR Emulator System Image SDK, you must agree to the following terms and conditions. As described below, please note that this is a preview, emulated version of the Android XR OS, subject to change, that you use at your own risk.
2025-11-22T14:26:29.3495890Z 
2025-11-22T14:26:29.3496280Z This is the Android XR Emulator System Image SDK License Agreement
2025-11-22T14:26:29.3496470Z 
2025-11-22T14:26:29.3496760Z 1. Introduction
2025-11-22T14:26:29.3496900Z 
2025-11-22T14:26:29.3497920Z 1.1 The Android Android XR Emulator System Image SDK (referred to in the License Agreement as the "SDK" and specifically including the Android system files,, packaged APIs, library files (if and when they are made available), and Google applications and APIs add-ons) is licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of the SDK.
2025-11-22T14:26:29.3498750Z 
2025-11-22T14:26:29.3499350Z 1.2 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: https://source.android.com/, as updated from time to time.
2025-11-22T14:26:29.3499750Z 
2025-11-22T14:26:29.3500370Z 1.3 "Google" means Google LLC, organized under the laws of the State of Delaware, USA, and operating under the laws of the USA with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA.
2025-11-22T14:26:29.3500770Z 
2025-11-22T14:26:29.3501100Z 2. Accepting this License Agreement
2025-11-22T14:26:29.3501280Z 
2025-11-22T14:26:29.3501750Z 2.1 In order to use the SDK, you must first agree to the License Agreement. You may not use the SDK if you do not accept the License Agreement.
2025-11-22T14:26:29.3502080Z 
2025-11-22T14:26:29.3502480Z 2.2 By clicking to accept and/or using this SDK, you hereby agree to the terms of the License Agreement.
2025-11-22T14:26:29.3502730Z 
2025-11-22T14:26:29.3503390Z 2.3 You may not use the SDK and may not accept the License Agreement if you are a person barred from receiving the SDK under the laws of the United States or other countries, including the country in which you are resident or from which you use the SDK.
2025-11-22T14:26:29.3503840Z 
2025-11-22T14:26:29.3504650Z 2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the SDK on behalf of your employer or other entity.
2025-11-22T14:26:29.3505310Z 
2025-11-22T14:26:29.3505610Z 3. SDK License from Google
2025-11-22T14:26:29.3505770Z 
2025-11-22T14:26:29.3506380Z 3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use the SDK solely to develop applications for Android XR.
2025-11-22T14:26:29.3507150Z 
2025-11-22T14:26:29.3507800Z 3.2 You may not use this SDK to develop applications for other platforms or to develop another SDK. You are of course free to develop applications for other platforms provided that this SDK is not used for that purpose.
2025-11-22T14:26:29.3508440Z 
2025-11-22T14:26:29.3509400Z 3.3 You agree that Google or third parties own all legal right, title and interest in and to the SDK, including any Intellectual Property Rights that subsist in the SDK. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.
2025-11-22T14:26:29.3510070Z 
2025-11-22T14:26:29.3511230Z 3.4 You may not use the SDK for any purpose not expressly permitted by the License Agreement. Except to the extent required by applicable third party licenses, you may not (a) copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the SDK or any part of the SDK; or (b) load any part of the SDK onto a mobile handset or any other hardware device except a personal computer, combine any part of the SDK with other software, or distribute any software or device incorporating a part of the SDK.
2025-11-22T14:26:29.3512520Z 
2025-11-22T14:26:29.3513420Z 3.5 Use, reproduction and distribution of components of the SDK licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement. You agree to remain a licensee in good standing in regard to such open source software licenses under all the rights granted and to refrain from any actions that may terminate, suspend, or breach such rights.
2025-11-22T14:26:29.3514120Z 
2025-11-22T14:26:29.3515080Z 3.6 You agree that the form and nature of the SDK that Google provides may change without prior notice to you and that future versions of the SDK may be incompatible with applications developed on previous versions of the SDK. You agree that Google may stop (permanently or temporarily) providing the SDK (or any features within the SDK) to you or to users generally at Google's sole discretion, without prior notice to you.
2025-11-22T14:26:29.3515780Z 
2025-11-22T14:26:29.3516340Z 3.7 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.
2025-11-22T14:26:29.3516680Z 
2025-11-22T14:26:29.3517210Z 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the SDK.
2025-11-22T14:26:29.3517610Z 
2025-11-22T14:26:29.3517900Z 4. Use of the SDK by You
2025-11-22T14:26:29.3518060Z 
2025-11-22T14:26:29.3518730Z 4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you develop using the SDK, including any intellectual property rights that subsist in those applications.
2025-11-22T14:26:29.3519250Z 
2025-11-22T14:26:29.3520040Z 4.2 You agree to use the SDK and write applications only for purposes that are permitted by (a) the License Agreement and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).
2025-11-22T14:26:29.3520650Z 
2025-11-22T14:26:29.3522170Z 4.3 You agree that if you use the SDK to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-22T14:26:29.3523740Z 
2025-11-22T14:26:29.3524620Z 4.4 You agree that you will not engage in any activity with the SDK, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier.
2025-11-22T14:26:29.3525270Z 
2025-11-22T14:26:29.3526070Z 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.
2025-11-22T14:26:29.3526980Z 
2025-11-22T14:26:29.3527850Z 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.
2025-11-22T14:26:29.3528510Z 
2025-11-22T14:26:29.3529270Z 4.7 The SDK is in development, and your testing and feedback are an important part of the development process. By using the SDK, you acknowledge that implementation of some features are still under development and that you should not rely on the SDK having the full functionality of a stable release.
2025-11-22T14:26:29.3529890Z 
2025-11-22T14:26:29.3530440Z 5. Your Developer Credentials
2025-11-22T14:26:29.3530650Z 
2025-11-22T14:26:29.3531610Z 5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.
2025-11-22T14:26:29.3532390Z 
2025-11-22T14:26:29.3532860Z 6. Privacy and Information
2025-11-22T14:26:29.3533090Z 
2025-11-22T14:26:29.3534380Z 6.1 In order to continually innovate and improve the SDK, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the SDK are being used and how they are being used. Before any of this information is collected, the SDK will notify you and seek your consent. If you withhold consent, the information will not be collected.
2025-11-22T14:26:29.3540960Z 
2025-11-22T14:26:29.3541630Z 6.2 The data collected is examined in the aggregate to improve the SDK and is maintained in accordance with Google's Privacy Policy, which is located at the following URL: https://policies.google.com/privacy
2025-11-22T14:26:29.3542030Z 
2025-11-22T14:26:29.3542490Z 6.3 Anonymized and aggregated sets of the data may be shared with Google partners to improve the SDK.
2025-11-22T14:26:29.3542730Z 
2025-11-22T14:26:29.3543030Z 7. Third Party Applications
2025-11-22T14:26:29.3543190Z 
2025-11-22T14:26:29.3544330Z 7.1 If you use the SDK to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources.
2025-11-22T14:26:29.3545850Z 
2025-11-22T14:26:29.3546870Z 7.2 You should be aware that the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners.
2025-11-22T14:26:29.3547700Z 
2025-11-22T14:26:29.3548380Z 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, the License Agreement does not affect your legal relationship with these third parties.
2025-11-22T14:26:29.3549240Z 
2025-11-22T14:26:29.3549540Z 8. Using Android APIs
2025-11-22T14:26:29.3549670Z 
2025-11-22T14:26:29.3550000Z 8.1 Google Data APIs
2025-11-22T14:26:29.3550680Z 
2025-11-22T14:26:29.3552030Z 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service.
2025-11-22T14:26:29.3553150Z 
2025-11-22T14:26:29.3555720Z 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so. If you use the Android Recognition Service API, documented at the following URL: https://developer.android.com/reference/android/speech/RecognitionService, as updated from time to time, you acknowledge that the use of the API is subject to the Data Processing Addendum for Products where Google is a Data Processor, which is located at the following URL: https://privacy.google.com/businesses/gdprprocessorterms/, as updated from time to time. By clicking to accept, you hereby agree to the terms of the Data Processing Addendum for Products where Google is a Data Processor.
2025-11-22T14:26:29.3557720Z 
2025-11-22T14:26:29.3558430Z 9. Terminating this License Agreement
2025-11-22T14:26:29.3558590Z 
2025-11-22T14:26:29.3559210Z 9.1 The License Agreement will continue to apply until terminated by either you or Google as set out below.
2025-11-22T14:26:29.3559590Z 
2025-11-22T14:26:29.3560080Z 9.2 If you want to terminate the License Agreement, you may do so by ceasing your use of the SDK and any relevant developer credentials.
2025-11-22T14:26:29.3560400Z 
2025-11-22T14:26:29.3562510Z 9.3 Google may at any time, terminate the License Agreement with you if: (A) you have breached any provision of the License Agreement; or (B) Google is required to do so by law; or (C) the partner with whom Google offered certain parts of SDK (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the SDK to you; or (D) Google decides to no longer provide the SDK or certain parts of the SDK to users in the country in which you are resident or from which you use the service, or the provision of the SDK or certain SDK services to you by Google is, in Google's sole discretion, no longer commercially viable.
2025-11-22T14:26:29.3564430Z 
2025-11-22T14:26:29.3565440Z 9.4 When the License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst the License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.
2025-11-22T14:26:29.3567950Z 
2025-11-22T14:26:29.3568300Z 10. DISCLAIMER OF WARRANTIES
2025-11-22T14:26:29.3568440Z 
2025-11-22T14:26:29.3569270Z 10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE SDK IS AT YOUR SOLE RISK AND THAT THE SDK IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.
2025-11-22T14:26:29.3569640Z 
2025-11-22T14:26:29.3570980Z 10.2 YOUR USE OF THE SDK AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE SDK IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE.
2025-11-22T14:26:29.3572370Z 
2025-11-22T14:26:29.3573490Z 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
2025-11-22T14:26:29.3574210Z 
2025-11-22T14:26:29.3574720Z 11. LIMITATION OF LIABILITY
2025-11-22T14:26:29.3575360Z 
2025-11-22T14:26:29.3577100Z 11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.
2025-11-22T14:26:29.3578460Z 
2025-11-22T14:26:29.3578880Z 12. Indemnification
2025-11-22T14:26:29.3579040Z 
2025-11-22T14:26:29.3580780Z 12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the SDK, (b) any application you develop on the SDK that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with the License Agreement.
2025-11-22T14:26:29.3582230Z 
2025-11-22T14:26:29.3582710Z 13. Changes to the License Agreement
2025-11-22T14:26:29.3582880Z 
2025-11-22T14:26:29.3584350Z 13.1 Google may make changes to the License Agreement as it distributes new versions of the SDK. When these changes are made, Google will make a new version of the License Agreement available on the website where the SDK is made available.
2025-11-22T14:26:29.3584970Z 
2025-11-22T14:26:29.3585400Z 14. General Legal Terms
2025-11-22T14:26:29.3585570Z 
2025-11-22T14:26:29.3586310Z 14.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of the SDK (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the SDK.
2025-11-22T14:26:29.3589370Z 
2025-11-22T14:26:29.3591290Z 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.
2025-11-22T14:26:29.3591900Z 
2025-11-22T14:26:29.3592810Z 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable.
2025-11-22T14:26:29.3594040Z 
2025-11-22T14:26:29.3595140Z 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement.
2025-11-22T14:26:29.3595940Z 
2025-11-22T14:26:29.3596610Z 14.5 EXPORT RESTRICTIONS. THE SDK IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE SDK. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.
2025-11-22T14:26:29.3599550Z 
2025-11-22T14:26:29.3600980Z 14.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party.
2025-11-22T14:26:29.3601710Z 
2025-11-22T14:26:29.3602880Z 14.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.
2025-11-22T14:26:29.3604270Z ---------------------------------------
2025-11-22T14:26:29.3604680Z Accept? (y/N): 
2025-11-22T14:26:29.3605040Z 3/6: License android-sdk-arm-dbt-license:
2025-11-22T14:26:29.3605710Z ---------------------------------------
2025-11-22T14:26:29.3606140Z Terms and Conditions
2025-11-22T14:26:29.3606390Z 
2025-11-22T14:26:29.3606810Z This is the Android Software Development Kit License Agreement
2025-11-22T14:26:29.3607040Z 
2025-11-22T14:26:29.3607330Z 1. Introduction
2025-11-22T14:26:29.3607480Z 
2025-11-22T14:26:29.3608280Z 1.1 The Android Software Development Kit (referred to in the License Agreement as the "SDK" and specifically including the Android system files, packaged APIs, and Google APIs add-ons) is licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of the SDK.
2025-11-22T14:26:29.3608930Z 
2025-11-22T14:26:29.3610080Z 1.2 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: http://source.android.com/, as updated from time to time.
2025-11-22T14:26:29.3610530Z 
2025-11-22T14:26:29.3612430Z 1.3 A "compatible implementation" means any Android device that (i) complies with the Android Compatibility Definition document, which can be found at the Android compatibility website (http://source.android.com/compatibility) and which may be updated from time to time; and (ii) successfully passes the Android Compatibility Test Suite (CTS).
2025-11-22T14:26:29.3613070Z 
2025-11-22T14:26:29.3613620Z 1.4 "Google" means Google Inc., a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.
2025-11-22T14:26:29.3614260Z 
2025-11-22T14:26:29.3614350Z 
2025-11-22T14:26:29.3614700Z 2. Accepting the License Agreement
2025-11-22T14:26:29.3615300Z 
2025-11-22T14:26:29.3615800Z 2.1 In order to use the SDK, you must first agree to the License Agreement. You may not use the SDK if you do not accept the License Agreement.
2025-11-22T14:26:29.3616140Z 
2025-11-22T14:26:29.3616540Z 2.2 By clicking to accept, you hereby agree to the terms of the License Agreement.
2025-11-22T14:26:29.3616790Z 
2025-11-22T14:26:29.3617440Z 2.3 You may not use the SDK and may not accept the License Agreement if you are a person barred from receiving the SDK under the laws of the United States or other countries, including the country in which you are resident or from which you use the SDK.
2025-11-22T14:26:29.3617910Z 
2025-11-22T14:26:29.3618780Z 2.4 If you are agreeing to be bound by the License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the SDK on behalf of your employer or other entity.
2025-11-22T14:26:29.3620230Z 
2025-11-22T14:26:29.3620450Z 
2025-11-22T14:26:29.3620970Z 3. SDK License from Google
2025-11-22T14:26:29.3621170Z 
2025-11-22T14:26:29.3621980Z 3.1 Subject to the terms of the License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable, non-exclusive, and non-sublicensable license to use the SDK solely to develop applications for compatible implementations of Android.
2025-11-22T14:26:29.3622570Z 
2025-11-22T14:26:29.3623700Z 3.2 You may not use this SDK to develop applications for other platforms (including non-compatible implementations of Android) or to develop another SDK. You are of course free to develop applications for other platforms, including non-compatible implementations of Android, provided that this SDK is not used for that purpose.
2025-11-22T14:26:29.3624320Z 
2025-11-22T14:26:29.3625660Z 3.3 You agree that Google or third parties own all legal right, title and interest in and to the SDK, including any Intellectual Property Rights that subsist in the SDK. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.
2025-11-22T14:26:29.3626480Z 
2025-11-22T14:26:29.3627330Z 3.4 You may not use the SDK for any purpose not expressly permitted by the License Agreement. Except to the extent required by applicable third party licenses, you may not copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the SDK or any part of the SDK.
2025-11-22T14:26:29.3627970Z 
2025-11-22T14:26:29.3631450Z 3.5 Use, reproduction and distribution of components of the SDK licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement.
2025-11-22T14:26:29.3632300Z 
2025-11-22T14:26:29.3633440Z 3.6 You agree that the form and nature of the SDK that Google provides may change without prior notice to you and that future versions of the SDK may be incompatible with applications developed on previous versions of the SDK. You agree that Google may stop (permanently or temporarily) providing the SDK (or any features within the SDK) to you or to users generally at Google's sole discretion, without prior notice to you.
2025-11-22T14:26:29.3634360Z 
2025-11-22T14:26:29.3634940Z 3.7 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.
2025-11-22T14:26:29.3635350Z 
2025-11-22T14:26:29.3636170Z 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the SDK.
2025-11-22T14:26:29.3636660Z 
2025-11-22T14:26:29.3636840Z 
2025-11-22T14:26:29.3637610Z 4. Use of the SDK by You
2025-11-22T14:26:29.3637800Z 
2025-11-22T14:26:29.3638590Z 4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you develop using the SDK, including any intellectual property rights that subsist in those applications.
2025-11-22T14:26:29.3639210Z 
2025-11-22T14:26:29.3640420Z 4.2 You agree to use the SDK and write applications only for purposes that are permitted by (a) the License Agreement and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).
2025-11-22T14:26:29.3641050Z 
2025-11-22T14:26:29.3643230Z 4.3 You agree that if you use the SDK to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-22T14:26:29.3644760Z 
2025-11-22T14:26:29.3646090Z 4.4 You agree that you will not engage in any activity with the SDK, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google or any mobile communications carrier.
2025-11-22T14:26:29.3646910Z 
2025-11-22T14:26:29.3647990Z 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.
2025-11-22T14:26:29.3648610Z 
2025-11-22T14:26:29.3649660Z 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.
2025-11-22T14:26:29.3650590Z 
2025-11-22T14:26:29.3652200Z 4.7 This software enables the execution of intellectual property owned by Arm Limited. You agree that your use of the software, that allows execution of ARM Instruction Set Architecture (“ISA”) compliant executables for application development and debug only on x86 desktop, laptop, customer on-premise servers, and customer-procured cloud-based environments.
2025-11-22T14:26:29.3652920Z 
2025-11-22T14:26:29.3653250Z 5. Your Developer Credentials
2025-11-22T14:26:29.3653430Z 
2025-11-22T14:26:29.3654360Z 5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.
2025-11-22T14:26:29.3654990Z 
2025-11-22T14:26:29.3655320Z 6. Privacy and Information
2025-11-22T14:26:29.3655490Z 
2025-11-22T14:26:29.3656530Z 6.1 In order to continually innovate and improve the SDK, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the SDK are being used and how they are being used. Before any of this information is collected, the SDK will notify you and seek your consent. If you withhold consent, the information will not be collected.
2025-11-22T14:26:29.3657760Z 
2025-11-22T14:26:29.3658830Z 6.2 The data collected is examined in the aggregate to improve the SDK and is maintained in accordance with Google's Privacy Policy.
2025-11-22T14:26:29.3659550Z 
2025-11-22T14:26:29.3660030Z 
2025-11-22T14:26:29.3660400Z 7. Third Party Applications
2025-11-22T14:26:29.3660540Z 
2025-11-22T14:26:29.3661750Z 7.1 If you use the SDK to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources.
2025-11-22T14:26:29.3663260Z 
2025-11-22T14:26:29.3665070Z 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners.
2025-11-22T14:26:29.3666330Z 
2025-11-22T14:26:29.3667130Z 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, the License Agreement does not affect your legal relationship with these third parties.
2025-11-22T14:26:29.3667660Z 
2025-11-22T14:26:29.3667780Z 
2025-11-22T14:26:29.3668080Z 8. Using Android APIs
2025-11-22T14:26:29.3668200Z 
2025-11-22T14:26:29.3668520Z 8.1 Google Data APIs
2025-11-22T14:26:29.3668640Z 
2025-11-22T14:26:29.3669640Z 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service.
2025-11-22T14:26:29.3670570Z 
2025-11-22T14:26:29.3672140Z 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so. If you use the Android Recognition Service API, documented at the following URL: https://developer.android.com/reference/android/speech/RecognitionService, as updated from time to time, you acknowledge that the use of the API is subject to the Data Processing Addendum for Products where Google is a Data Processor, which is located at the following URL: https://privacy.google.com/businesses/gdprprocessorterms/, as updated from time to time. By clicking to accept, you hereby agree to the terms of the Data Processing Addendum for Products where Google is a Data Processor.
2025-11-22T14:26:29.3673520Z 
2025-11-22T14:26:29.3673650Z 
2025-11-22T14:26:29.3673970Z 9. Terminating the License Agreement
2025-11-22T14:26:29.3674110Z 
2025-11-22T14:26:29.3674570Z 9.1 The License Agreement will continue to apply until terminated by either you or Google as set out below.
2025-11-22T14:26:29.3674820Z 
2025-11-22T14:26:29.3675770Z 9.2 If you want to terminate the License Agreement, you may do so by ceasing your use of the SDK and any relevant developer credentials.
2025-11-22T14:26:29.3676110Z 
2025-11-22T14:26:29.3677490Z 9.3 Google may at any time, terminate the License Agreement with you if: (A) you have breached any provision of the License Agreement; or (B) Google is required to do so by law; or (C) the partner with whom Google offered certain parts of SDK (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the SDK to you; or (D) Google decides to no longer provide the SDK or certain parts of the SDK to users in the country in which you are resident or from which you use the service, or the provision of the SDK or certain SDK services to you by Google is, in Google's sole discretion, no longer commercially viable.
2025-11-22T14:26:29.3678590Z 
2025-11-22T14:26:29.3679540Z 9.4 When the License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst the License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.
2025-11-22T14:26:29.3680510Z 
2025-11-22T14:26:29.3680610Z 
2025-11-22T14:26:29.3680960Z 10. DISCLAIMER OF WARRANTIES
2025-11-22T14:26:29.3681100Z 
2025-11-22T14:26:29.3681630Z 10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE SDK IS AT YOUR SOLE RISK AND THAT THE SDK IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.
2025-11-22T14:26:29.3682000Z 
2025-11-22T14:26:29.3682650Z 10.2 YOUR USE OF THE SDK AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE SDK IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE.
2025-11-22T14:26:29.3683180Z 
2025-11-22T14:26:29.3683850Z 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
2025-11-22T14:26:29.3684350Z 
2025-11-22T14:26:29.3684440Z 
2025-11-22T14:26:29.3684740Z 11. LIMITATION OF LIABILITY
2025-11-22T14:26:29.3684900Z 
2025-11-22T14:26:29.3685990Z 11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.
2025-11-22T14:26:29.3686860Z 
2025-11-22T14:26:29.3686960Z 
2025-11-22T14:26:29.3687300Z 12. Indemnification
2025-11-22T14:26:29.3687470Z 
2025-11-22T14:26:29.3688910Z 12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the SDK, (b) any application you develop on the SDK that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with the License Agreement.
2025-11-22T14:26:29.3690340Z 
2025-11-22T14:26:29.3690450Z 
2025-11-22T14:26:29.3690870Z 13. Changes to the License Agreement
2025-11-22T14:26:29.3691010Z 
2025-11-22T14:26:29.3691640Z 13.1 Google may make changes to the License Agreement as it distributes new versions of the SDK. When these changes are made, Google will make a new version of the License Agreement available on the website where the SDK is made available.
2025-11-22T14:26:29.3692490Z 
2025-11-22T14:26:29.3692580Z 
2025-11-22T14:26:29.3692950Z 14. General Legal Terms
2025-11-22T14:26:29.3693140Z 
2025-11-22T14:26:29.3694150Z 14.1 The License Agreement constitutes the whole legal agreement between you and Google and governs your use of the SDK (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the SDK.
2025-11-22T14:26:29.3694910Z 
2025-11-22T14:26:29.3695780Z 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.
2025-11-22T14:26:29.3696660Z 
2025-11-22T14:26:29.3697720Z 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable.
2025-11-22T14:26:29.3698400Z 
2025-11-22T14:26:29.3699570Z 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement.
2025-11-22T14:26:29.3700410Z 
2025-11-22T14:26:29.3701110Z 14.5 EXPORT RESTRICTIONS. THE SDK IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE SDK. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.
2025-11-22T14:26:29.3701820Z 
2025-11-22T14:26:29.3702810Z 14.6 The rights granted in the License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under the License Agreement without the prior written approval of the other party.
2025-11-22T14:26:29.3703420Z 
2025-11-22T14:26:29.3704680Z 14.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.
2025-11-22T14:26:29.3705640Z 
2025-11-22T14:26:29.3705740Z 
2025-11-22T14:26:29.3706040Z January 16, 2019
2025-11-22T14:26:29.3706410Z ---------------------------------------
2025-11-22T14:26:29.3706970Z Accept? (y/N): 
2025-11-22T14:26:29.3707340Z 4/6: License android-sdk-preview-license:
2025-11-22T14:26:29.3707730Z ---------------------------------------
2025-11-22T14:26:29.3708640Z To get started with the Android SDK Preview, you must agree to the following terms and conditions. As described below, please note that this is a preview version of the Android SDK, subject to change, that you use at your own risk. The Android SDK Preview is not a stable release, and may contain errors and defects that can result in serious damage to your computer systems, devices and data.
2025-11-22T14:26:29.3709570Z 
2025-11-22T14:26:29.3710000Z This is the Android SDK Preview License Agreement (the "License Agreement").
2025-11-22T14:26:29.3710350Z 
2025-11-22T14:26:29.3710810Z 1. Introduction
2025-11-22T14:26:29.3710990Z 
2025-11-22T14:26:29.3712550Z 1.1 The Android SDK Preview (referred to in the License Agreement as the “Preview” and specifically including the Android system files, packaged APIs, and Preview library files, if and when they are made available) is licensed to you subject to the terms of the License Agreement. The License Agreement forms a legally binding contract between you and Google in relation to your use of the Preview.
2025-11-22T14:26:29.3713240Z 
2025-11-22T14:26:29.3714480Z 1.2 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: http://source.android.com/, as updated from time to time.
2025-11-22T14:26:29.3714900Z 
2025-11-22T14:26:29.3715420Z 1.3 "Google" means Google Inc., a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.
2025-11-22T14:26:29.3716070Z 
2025-11-22T14:26:29.3716410Z 2. Accepting the License Agreement
2025-11-22T14:26:29.3716580Z 
2025-11-22T14:26:29.3717060Z 2.1 In order to use the Preview, you must first agree to the License Agreement. You may not use the Preview if you do not accept the License Agreement.
2025-11-22T14:26:29.3717440Z 
2025-11-22T14:26:29.3718060Z 2.2 By clicking to accept and/or using the Preview, you hereby agree to the terms of the License Agreement.
2025-11-22T14:26:29.3718320Z 
2025-11-22T14:26:29.3718970Z 2.3 You may not use the Preview and may not accept the License Agreement if you are a person barred from receiving the Preview under the laws of the United States or other countries including the country in which you are resident or from which you use the Preview.
2025-11-22T14:26:29.3719490Z 
2025-11-22T14:26:29.3720430Z 2.4 If you will use the Preview internally within your company or organization you agree to be bound by the License Agreement on behalf of your employer or other entity, and you represent and warrant that you have full legal authority to bind your employer or such entity to the License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the Preview on behalf of your employer or other entity.
2025-11-22T14:26:29.3721200Z 
2025-11-22T14:26:29.3721510Z 3. Preview License from Google
2025-11-22T14:26:29.3721680Z 
2025-11-22T14:26:29.3722540Z 3.1 Subject to the terms of the License Agreement, Google grants you a royalty-free, non-assignable, non-exclusive, non-sublicensable, limited, revocable license to use the Preview, personally or internally within your company or organization, solely to develop applications to run on the Android platform.
2025-11-22T14:26:29.3723130Z 
2025-11-22T14:26:29.3723990Z 3.2 You agree that Google or third parties owns all legal right, title and interest in and to the Preview, including any Intellectual Property Rights that subsist in the Preview. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.
2025-11-22T14:26:29.3724700Z 
2025-11-22T14:26:29.3726190Z 3.3 You may not use the Preview for any purpose not expressly permitted by the License Agreement. Except to the extent required by applicable third party licenses, you may not: (a) copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the Preview or any part of the Preview; or (b) load any part of the Preview onto a mobile handset or any other hardware device except a personal computer, combine any part of the Preview with other software, or distribute any software or device incorporating a part of the Preview.
2025-11-22T14:26:29.3727210Z 
2025-11-22T14:26:29.3728110Z 3.4 You agree that you will not take any actions that may cause or result in the fragmentation of Android, including but not limited to distributing, participating in the creation of, or promoting in any way a software development kit derived from the Preview.
2025-11-22T14:26:29.3728630Z 
2025-11-22T14:26:29.3729600Z 3.5 Use, reproduction and distribution of components of the Preview licensed under an open source software license are governed solely by the terms of that open source software license and not the License Agreement. You agree to remain a licensee in good standing in regard to such open source software licenses under all the rights granted and to refrain from any actions that may terminate, suspend, or breach such rights.
2025-11-22T14:26:29.3730310Z 
2025-11-22T14:26:29.3731260Z 3.6 You agree that the form and nature of the Preview that Google provides may change without prior notice to you and that future versions of the Preview may be incompatible with applications developed on previous versions of the Preview. You agree that Google may stop (permanently or temporarily) providing the Preview (or any features within the Preview) to you or to users generally at Google's sole discretion, without prior notice to you.
2025-11-22T14:26:29.3732200Z 
2025-11-22T14:26:29.3732810Z 3.7 Nothing in the License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.
2025-11-22T14:26:29.3733160Z 
2025-11-22T14:26:29.3733940Z 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the Preview.
2025-11-22T14:26:29.3734360Z 
2025-11-22T14:26:29.3734660Z 4. Use of the Preview by You
2025-11-22T14:26:29.3734830Z 
2025-11-22T14:26:29.3735550Z 4.1 Google agrees that nothing in the License Agreement gives Google any right, title or interest from you (or your licensors) under the License Agreement in or to any software applications that you develop using the Preview, including any intellectual property rights that subsist in those applications.
2025-11-22T14:26:29.3736220Z 
2025-11-22T14:26:29.3737080Z 4.2 You agree to use the Preview and write applications only for purposes that are permitted by (a) the License Agreement, and (b) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).
2025-11-22T14:26:29.3737700Z 
2025-11-22T14:26:29.3739100Z 4.3 You agree that if you use the Preview to develop applications, you will protect the privacy and legal rights of users. If users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If users provide you with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, each user has given you permission to do so.
2025-11-22T14:26:29.3740290Z 
2025-11-22T14:26:29.3741010Z 4.4 You agree that you will not engage in any activity with the Preview, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of Google or any third party.
2025-11-22T14:26:29.3741570Z 
2025-11-22T14:26:29.3742360Z 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Android and/or applications for Android, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.
2025-11-22T14:26:29.3743320Z 
2025-11-22T14:26:29.3744350Z 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under the License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.
2025-11-22T14:26:29.3745020Z 
2025-11-22T14:26:29.3746240Z 4.7 The Preview is in development, and your testing and feedback are an important part of the development process. By using the Preview, you acknowledge that implementation of some features are still under development and that you should not rely on the Preview having the full functionality of a stable release. You agree not to publicly distribute or ship any application using this Preview as this Preview will no longer be supported after the official Android SDK is released.
2025-11-22T14:26:29.3747260Z 
2025-11-22T14:26:29.3747820Z 5. Your Developer Credentials
2025-11-22T14:26:29.3747980Z 
2025-11-22T14:26:29.3748850Z 5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.
2025-11-22T14:26:29.3749470Z 
2025-11-22T14:26:29.3749790Z 6. Privacy and Information
2025-11-22T14:26:29.3749970Z 
2025-11-22T14:26:29.3750980Z 6.1 In order to continually innovate and improve the Preview, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the Preview are being used and how they are being used. Before any of this information is collected, the Preview will notify you and seek your consent. If you withhold consent, the information will not be collected.
2025-11-22T14:26:29.3751840Z 
2025-11-22T14:26:29.3779540Z 6.2 The data collected is examined in the aggregate to improve the Preview and is maintained in accordance with Google's Privacy Policy located at http://www.google.com/policies/privacy/.
2025-11-22T14:26:29.3780030Z 
2025-11-22T14:26:29.3780380Z 7. Third Party Applications
2025-11-22T14:26:29.3780520Z 
2025-11-22T14:26:29.3781710Z 7.1 If you use the Preview to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources.
2025-11-22T14:26:29.3782740Z 
2025-11-22T14:26:29.3784140Z 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners.
2025-11-22T14:26:29.3785160Z 
2025-11-22T14:26:29.3785880Z 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party.
2025-11-22T14:26:29.3786340Z 
2025-11-22T14:26:29.3786760Z 8. Using Google APIs
2025-11-22T14:26:29.3786980Z 
2025-11-22T14:26:29.3787350Z 8.1 Google APIs
2025-11-22T14:26:29.3787540Z 
2025-11-22T14:26:29.3789270Z 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service.
2025-11-22T14:26:29.3790390Z 
2025-11-22T14:26:29.3791270Z 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-22T14:26:29.3791870Z 
2025-11-22T14:26:29.3792370Z 9. Terminating the License Agreement
2025-11-22T14:26:29.3792570Z 
2025-11-22T14:26:29.3793140Z 9.1 the License Agreement will continue to apply until terminated by either you or Google as set out below.
2025-11-22T14:26:29.3793770Z 
2025-11-22T14:26:29.3794440Z 9.2 If you want to terminate the License Agreement, you may do so by ceasing your use of the Preview and any relevant developer credentials.
2025-11-22T14:26:29.3794870Z 
2025-11-22T14:26:29.3795450Z 9.3 Google may at any time, terminate the License Agreement, with or without cause, upon notice to you.
2025-11-22T14:26:29.3795770Z 
2025-11-22T14:26:29.3796780Z 9.4 The License Agreement will automatically terminate without notice or other action upon the earlier of: (A) when Google ceases to provide the Preview or certain parts of the Preview to users in the country in which you are resident or from which you use the service; and (B) Google issues a final release version of the Android SDK.
2025-11-22T14:26:29.3797520Z 
2025-11-22T14:26:29.3798220Z 9.5 When the License Agreement is terminated, the license granted to you in the License Agreement will terminate, you will immediately cease all use of the Preview, and the provisions of paragraphs 10, 11, 12 and 14 shall survive indefinitely.
2025-11-22T14:26:29.3798760Z 
2025-11-22T14:26:29.3799040Z 10. DISCLAIMERS
2025-11-22T14:26:29.3799200Z 
2025-11-22T14:26:29.3799710Z 10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE PREVIEW IS AT YOUR SOLE RISK AND THAT THE PREVIEW IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.
2025-11-22T14:26:29.3800730Z 
2025-11-22T14:26:29.3802060Z 10.2 YOUR USE OF THE PREVIEW AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE PREVIEW IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE. WITHOUT LIMITING THE FOREGOING, YOU UNDERSTAND THAT THE PREVIEW IS NOT A STABLE RELEASE AND MAY CONTAIN ERRORS, DEFECTS AND SECURITY VULNERABILITIES THAT CAN RESULT IN SIGNIFICANT DAMAGE, INCLUDING THE COMPLETE, IRRECOVERABLE LOSS OF USE OF YOUR COMPUTER SYSTEM OR OTHER DEVICE.
2025-11-22T14:26:29.3803020Z 
2025-11-22T14:26:29.3803690Z 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
2025-11-22T14:26:29.3804420Z 
2025-11-22T14:26:29.3804760Z 11. LIMITATION OF LIABILITY
2025-11-22T14:26:29.3804900Z 
2025-11-22T14:26:29.3805860Z 11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.
2025-11-22T14:26:29.3806650Z 
2025-11-22T14:26:29.3806950Z 12. Indemnification
2025-11-22T14:26:29.3807540Z 
2025-11-22T14:26:29.3809850Z 12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys’ fees) arising out of or accruing from (a) your use of the Preview, (b) any application you develop on the Preview that infringes any Intellectual Property Rights of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you of the License Agreement.
2025-11-22T14:26:29.3811050Z 
2025-11-22T14:26:29.3811430Z 13. Changes to the License Agreement
2025-11-22T14:26:29.3811640Z 
2025-11-22T14:26:29.3812310Z 13.1 Google may make changes to the License Agreement as it distributes new versions of the Preview. When these changes are made, Google will make a new version of the License Agreement available on the website where the Preview is made available.
2025-11-22T14:26:29.3813040Z 
2025-11-22T14:26:29.3813370Z 14. General Legal Terms
2025-11-22T14:26:29.3813510Z 
2025-11-22T14:26:29.3814520Z 14.1 the License Agreement constitutes the whole legal agreement between you and Google and governs your use of the Preview (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the Preview.
2025-11-22T14:26:29.3815080Z 
2025-11-22T14:26:29.3815790Z 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in the License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.
2025-11-22T14:26:29.3816360Z 
2025-11-22T14:26:29.3817120Z 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of the License Agreement is invalid, then that provision will be removed from the License Agreement without affecting the rest of the License Agreement. The remaining provisions of the License Agreement will continue to be valid and enforceable.
2025-11-22T14:26:29.3817780Z 
2025-11-22T14:26:29.3818820Z 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to the License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of the License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to the License Agreement.
2025-11-22T14:26:29.3819600Z 
2025-11-22T14:26:29.3820270Z 14.5 EXPORT RESTRICTIONS. THE PREVIEW IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE PREVIEW. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.
2025-11-22T14:26:29.3820780Z 
2025-11-22T14:26:29.3821480Z 14.6 The License Agreement may not be assigned or transferred by you without the prior written approval of Google, and any attempted assignment without such approval will be void. You shall not delegate your responsibilities or obligations under the License Agreement without the prior written approval of Google.
2025-11-22T14:26:29.3822030Z 
2025-11-22T14:26:29.3823140Z 14.7 The License Agreement, and your relationship with Google under the License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from the License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.
2025-11-22T14:26:29.3824280Z 
2025-11-22T14:26:29.3824530Z June 2014.
2025-11-22T14:26:29.3824850Z ---------------------------------------
2025-11-22T14:26:29.3825170Z Accept? (y/N): 
2025-11-22T14:26:29.3825470Z 5/6: License google-gdk-license:
2025-11-22T14:26:29.3825830Z ---------------------------------------
2025-11-22T14:26:29.3826230Z This is a Developer Preview of the GDK that is subject to change.
2025-11-22T14:26:29.3826420Z 
2025-11-22T14:26:29.3826690Z Terms and Conditions
2025-11-22T14:26:29.3826820Z 
2025-11-22T14:26:29.3827130Z This is the Glass Development Kit License Agreement.
2025-11-22T14:26:29.3827320Z 
2025-11-22T14:26:29.3827570Z 1. Introduction
2025-11-22T14:26:29.3827690Z 
2025-11-22T14:26:29.3828520Z 1.1 The Glass Development Kit (referred to in this License Agreement as the "GDK" and specifically including the Android system files, packaged APIs, and GDK library files, if and when they are made available) is licensed to you subject to the terms of this License Agreement. This License Agreement forms a legally binding contract between you and Google in relation to your use of the GDK.
2025-11-22T14:26:29.3829290Z 
2025-11-22T14:26:29.3829670Z 1.2 "Glass" means Glass devices and the Glass software stack for use on Glass devices.
2025-11-22T14:26:29.3829890Z 
2025-11-22T14:26:29.3829980Z 
2025-11-22T14:26:29.3830540Z 1.3 "Android" means the Android software stack for devices, as made available under the Android Open Source Project, which is located at the following URL: http://source.android.com/, as updated from time to time.
2025-11-22T14:26:29.3830950Z 
2025-11-22T14:26:29.3831440Z 1.4 "Google" means Google Inc., a Delaware corporation with principal place of business at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.
2025-11-22T14:26:29.3831760Z 
2025-11-22T14:26:29.3832050Z 2. Accepting this License Agreement
2025-11-22T14:26:29.3832200Z 
2025-11-22T14:26:29.3832660Z 2.1 In order to use the GDK, you must first agree to this License Agreement. You may not use the GDK if you do not accept this License Agreement.
2025-11-22T14:26:29.3833350Z 
2025-11-22T14:26:29.3834350Z 2.2 By clicking to accept, you hereby agree to the terms of this License Agreement.
2025-11-22T14:26:29.3834600Z 
2025-11-22T14:26:29.3835300Z 2.3 You may not use the GDK and may not accept the License Agreement if you are a person barred from receiving the GDK under the laws of the United States or other countries including the country in which you are resident or from which you use the GDK.
2025-11-22T14:26:29.3835810Z 
2025-11-22T14:26:29.3836800Z 2.4 If you are agreeing to be bound by this License Agreement on behalf of your employer or other entity, you represent and warrant that you have full legal authority to bind your employer or such entity to this License Agreement. If you do not have the requisite authority, you may not accept the License Agreement or use the GDK on behalf of your employer or other entity.
2025-11-22T14:26:29.3837610Z 
2025-11-22T14:26:29.3837920Z 3. GDK License from Google
2025-11-22T14:26:29.3838070Z 
2025-11-22T14:26:29.3838670Z 3.1 Subject to the terms of this License Agreement, Google grants you a limited, worldwide, royalty-free, non-assignable and non-exclusive license to use the GDK solely to develop applications to run on the Glass platform for Glass devices.
2025-11-22T14:26:29.3839670Z 
2025-11-22T14:26:29.3840660Z 3.2 You agree that Google or third parties own all legal right, title and interest in and to the GDK, including any Intellectual Property Rights that subsist in the GDK. "Intellectual Property Rights" means any and all rights under patent law, copyright law, trade secret law, trademark law, and any and all other proprietary rights. Google reserves all rights not expressly granted to you.
2025-11-22T14:26:29.3841440Z 
2025-11-22T14:26:29.3843650Z 3.3 You may not use the GDK for any purpose not expressly permitted by this License Agreement. Except to the extent required by applicable third party licenses, you may not: (a) copy (except for backup purposes), modify, adapt, redistribute, decompile, reverse engineer, disassemble, or create derivative works of the GDK or any part of the GDK; or (b) load any part of the GDK onto a mobile handset or wearable computing device or any other hardware device except a Glass device personal computer, combine any part of the GDK with other software, or distribute any software or device incorporating a part of the GDK.
2025-11-22T14:26:29.3845090Z 
2025-11-22T14:26:29.3845760Z 3.4 You agree that you will not take any actions that may cause or result in the fragmentation of Glass, including but not limited to distributing, participating in the creation of, or promoting in any way a software development kit derived from the GDK.
2025-11-22T14:26:29.3846220Z 
2025-11-22T14:26:29.3846800Z 3.5 Use, reproduction and distribution of components of the GDK licensed under an open source software license are governed solely by the terms of that open source software license and not this License Agreement.
2025-11-22T14:26:29.3847470Z 
2025-11-22T14:26:29.3848370Z 3.6 You agree that the form and nature of the GDK that Google provides may change without prior notice to you and that future versions of the GDK may be incompatible with applications developed on previous versions of the GDK. You agree that Google may stop (permanently or temporarily) providing the GDK (or any features within the GDK) to you or to users generally at Google's sole discretion, without prior notice to you.
2025-11-22T14:26:29.3849090Z 
2025-11-22T14:26:29.3849590Z 3.7 Nothing in this License Agreement gives you a right to use any of Google's trade names, trademarks, service marks, logos, domain names, or other distinctive brand features.
2025-11-22T14:26:29.3849950Z 
2025-11-22T14:26:29.3850460Z 3.8 You agree that you will not remove, obscure, or alter any proprietary rights notices (including copyright and trademark notices) that may be affixed to or contained within the GDK.
2025-11-22T14:26:29.3850840Z 
2025-11-22T14:26:29.3850930Z 
2025-11-22T14:26:29.3851790Z 3.9 Your use of any Android system files, packaged APIs, or other components of the GDK which are part of the Android Software Development Kit is subject to the terms of the Android Software Development Kit License Agreement located at http://developer.android.com/sdk/terms.html. These terms are hereby incorporated by reference into this License Agreement.
2025-11-22T14:26:29.3852440Z 
2025-11-22T14:26:29.3852740Z 4. Use of the GDK by You
2025-11-22T14:26:29.3852870Z 
2025-11-22T14:26:29.3853520Z 4.1 Google agrees that it obtains no right, title or interest from you (or your licensors) under this License Agreement in or to any software applications that you develop using the GDK, including any intellectual property rights that subsist in those applications.
2025-11-22T14:26:29.3854020Z 
2025-11-22T14:26:29.3855050Z 4.2 You agree to use the GDK and write applications only for purposes that are permitted by (a) this License Agreement, (b) the Glass Platform Developer Policies (located at https://developers.google.com/glass/policies, and hereby incorporated into this License Agreement by reference), and (c) any applicable law, regulation or generally accepted practices or guidelines in the relevant jurisdictions (including any laws regarding the export of data or software to and from the United States or other relevant countries).
2025-11-22T14:26:29.3855950Z 
2025-11-22T14:26:29.3857370Z 4.3 You agree that if you use the GDK to develop applications for general public users, you will protect the privacy and legal rights of those users. If the users provide you with user names, passwords, or other login information or personal information, you must make the users aware that the information will be available to your application, and you must provide legally adequate privacy notice and protection for those users. If your application stores personal or sensitive information provided by users, it must do so securely. If the user provides your application with Google Account information, your application may only use that information to access the user's Google Account when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-22T14:26:29.3858840Z 
2025-11-22T14:26:29.3859580Z 4.4 You agree that you will not engage in any activity with the GDK, including the development or distribution of an application, that interferes with, disrupts, damages, or accesses in an unauthorized manner the servers, networks, or other properties or services of any third party including, but not limited to, Google.
2025-11-22T14:26:29.3860150Z 
2025-11-22T14:26:29.3860900Z 4.5 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any data, content, or resources that you create, transmit or display through Glass and/or applications for Glass, and for the consequences of your actions (including any loss or damage which Google may suffer) by doing so.
2025-11-22T14:26:29.3861600Z 
2025-11-22T14:26:29.3862430Z 4.6 You agree that you are solely responsible for (and that Google has no responsibility to you or to any third party for) any breach of your obligations under this License Agreement, any applicable third party contract or Terms of Service, or any applicable law or regulation, and for the consequences (including any loss or damage which Google or any third party may suffer) of any such breach.
2025-11-22T14:26:29.3863100Z 
2025-11-22T14:26:29.3863190Z 
2025-11-22T14:26:29.3863980Z 4.7 The GDK is in development, and your testing and feedback are an important part of the development process. By using the GDK, you acknowledge that implementation of some features are still under development and that you should not rely on the GDK, Glass devices, Glass system software, Google Mirror API, or Glass services having the full functionality of a stable release.
2025-11-22T14:26:29.3864630Z 
2025-11-22T14:26:29.3864910Z 5. Your Developer Credentials
2025-11-22T14:26:29.3865060Z 
2025-11-22T14:26:29.3865730Z 5.1 You agree that you are responsible for maintaining the confidentiality of any developer credentials that may be issued to you by Google or which you may choose yourself and that you will be solely responsible for all applications that are developed under your developer credentials.
2025-11-22T14:26:29.3866260Z 
2025-11-22T14:26:29.3866530Z 6. Privacy and Information
2025-11-22T14:26:29.3866660Z 
2025-11-22T14:26:29.3866760Z 
2025-11-22T14:26:29.3867720Z 6.1 In order to continually innovate and improve the GDK, Google may collect certain usage statistics from the software including but not limited to a unique identifier, associated IP address, version number of the software, and information on which tools and/or services in the GDK are being used and how they are being used. Before any of this information is collected, the GDK will notify you and seek your consent. If you withhold consent, the information will not be collected.
2025-11-22T14:26:29.3868540Z 
2025-11-22T14:26:29.3868970Z 6.2 The data collected is examined in the aggregate to improve the GDK and is maintained in accordance with Google's Privacy Policy.
2025-11-22T14:26:29.3869270Z 
2025-11-22T14:26:29.3869550Z 7. Third Party Applications
2025-11-22T14:26:29.3869690Z 
2025-11-22T14:26:29.3870820Z 7.1 If you use the GDK to run applications developed by a third party or that access data, content or resources provided by a third party, you agree that Google is not responsible for those applications, data, content, or resources. You understand that all data, content or resources which you may access through such third party applications are the sole responsibility of the person from which they originated and that Google is not liable for any loss or damage that you may experience as a result of the use or access of any of those third party applications, data, content, or resources.
2025-11-22T14:26:29.3871790Z 
2025-11-22T14:26:29.3872770Z 7.2 You should be aware the data, content, and resources presented to you through such a third party application may be protected by intellectual property rights which are owned by the providers (or by other persons or companies on their behalf). You may not modify, rent, lease, loan, sell, distribute or create derivative works based on these data, content, or resources (either in whole or in part) unless you have been specifically given permission to do so by the relevant owners.
2025-11-22T14:26:29.3873710Z 
2025-11-22T14:26:29.3874370Z 7.3 You acknowledge that your use of such third party applications, data, content, or resources may be subject to separate terms between you and the relevant third party. In that case, this License Agreement does not affect your legal relationship with these third parties.
2025-11-22T14:26:29.3874890Z 
2025-11-22T14:26:29.3875160Z 8. Using Google APIs
2025-11-22T14:26:29.3875290Z 
2025-11-22T14:26:29.3875550Z 8.1 Google APIs
2025-11-22T14:26:29.3875670Z 
2025-11-22T14:26:29.3876670Z 8.1.1 If you use any API to retrieve data from Google, you acknowledge that the data may be protected by intellectual property rights which are owned by Google or those parties that provide the data (or by other persons or companies on their behalf). Your use of any such API may be subject to additional Terms of Service. You may not modify, rent, lease, loan, sell, distribute or create derivative works based on this data (either in whole or in part) unless allowed by the relevant Terms of Service.
2025-11-22T14:26:29.3877810Z 
2025-11-22T14:26:29.3878450Z 8.1.2 If you use any API to retrieve a user's data from Google, you acknowledge and agree that you shall retrieve data only with the user's explicit consent and only when, and for the limited purposes for which, the user has given you permission to do so.
2025-11-22T14:26:29.3878910Z 
2025-11-22T14:26:29.3879210Z 9. Terminating this License Agreement
2025-11-22T14:26:29.3879370Z 
2025-11-22T14:26:29.3879760Z 9.1 This License Agreement will continue to apply until terminated by either you or Google as set out below.
2025-11-22T14:26:29.3880030Z 
2025-11-22T14:26:29.3880480Z 9.2 If you want to terminate this License Agreement, you may do so by ceasing your use of the GDK and any relevant developer credentials.
2025-11-22T14:26:29.3880770Z 
2025-11-22T14:26:29.3881990Z 9.3 Google may at any time, terminate this License Agreement with you if: (A) you have breached any provision of this License Agreement; or (B) Google is required to do so by law; or (C) the partner with whom Google offered certain parts of GDK (such as APIs) to you has terminated its relationship with Google or ceased to offer certain parts of the GDK to you; or (D) Google decides to no longer provide the GDK or certain parts of the GDK to users in the country in which you are resident or from which you use the service, or the provision of the GDK or certain GDK services to you by Google is, in Google's sole discretion, no longer commercially viable.
2025-11-22T14:26:29.3883030Z 
2025-11-22T14:26:29.3883950Z 9.4 When this License Agreement comes to an end, all of the legal rights, obligations and liabilities that you and Google have benefited from, been subject to (or which have accrued over time whilst this License Agreement has been in force) or which are expressed to continue indefinitely, shall be unaffected by this cessation, and the provisions of paragraph 14.7 shall continue to apply to such rights, obligations and liabilities indefinitely.
2025-11-22T14:26:29.3884920Z 
2025-11-22T14:26:29.3885210Z 10. DISCLAIMER OF WARRANTIES
2025-11-22T14:26:29.3885350Z 
2025-11-22T14:26:29.3885860Z 10.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT YOUR USE OF THE GDK IS AT YOUR SOLE RISK AND THAT THE GDK IS PROVIDED "AS IS" AND "AS AVAILABLE" WITHOUT WARRANTY OF ANY KIND FROM GOOGLE.
2025-11-22T14:26:29.3886230Z 
2025-11-22T14:26:29.3886900Z 10.2 YOUR USE OF THE GDK AND ANY MATERIAL DOWNLOADED OR OTHERWISE OBTAINED THROUGH THE USE OF THE GDK IS AT YOUR OWN DISCRETION AND RISK AND YOU ARE SOLELY RESPONSIBLE FOR ANY DAMAGE TO YOUR COMPUTER SYSTEM OR OTHER DEVICE OR LOSS OF DATA THAT RESULTS FROM SUCH USE.
2025-11-22T14:26:29.3887540Z 
2025-11-22T14:26:29.3888200Z 10.3 GOOGLE FURTHER EXPRESSLY DISCLAIMS ALL WARRANTIES AND CONDITIONS OF ANY KIND, WHETHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO THE IMPLIED WARRANTIES AND CONDITIONS OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
2025-11-22T14:26:29.3888690Z 
2025-11-22T14:26:29.3888980Z 11. LIMITATION OF LIABILITY
2025-11-22T14:26:29.3889110Z 
2025-11-22T14:26:29.3890050Z 11.1 YOU EXPRESSLY UNDERSTAND AND AGREE THAT GOOGLE, ITS SUBSIDIARIES AND AFFILIATES, AND ITS LICENSORS SHALL NOT BE LIABLE TO YOU UNDER ANY THEORY OF LIABILITY FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL OR EXEMPLARY DAMAGES THAT MAY BE INCURRED BY YOU, INCLUDING ANY LOSS OF DATA, WHETHER OR NOT GOOGLE OR ITS REPRESENTATIVES HAVE BEEN ADVISED OF OR SHOULD HAVE BEEN AWARE OF THE POSSIBILITY OF ANY SUCH LOSSES ARISING.
2025-11-22T14:26:29.3890810Z 
2025-11-22T14:26:29.3891100Z 12. Indemnification
2025-11-22T14:26:29.3891220Z 
2025-11-22T14:26:29.3892710Z 12.1 To the maximum extent permitted by law, you agree to defend, indemnify and hold harmless Google, its affiliates and their respective directors, officers, employees and agents from and against any and all claims, actions, suits or proceedings, as well as any and all losses, liabilities, damages, costs and expenses (including reasonable attorneys fees) arising out of or accruing from (a) your use of the GDK, (b) any application you develop on the GDK that infringes any copyright, trademark, trade secret, trade dress, patent or other intellectual property right of any person or defames any person or violates their rights of publicity or privacy, and (c) any non-compliance by you with this License Agreement.
2025-11-22T14:26:29.3893900Z 
2025-11-22T14:26:29.3894200Z 13. Changes to the License Agreement
2025-11-22T14:26:29.3894360Z 
2025-11-22T14:26:29.3894970Z 13.1 Google may make changes to the License Agreement as it distributes new versions of the GDK. When these changes are made, Google will make a new version of the License Agreement available on the website where the GDK is made available.
2025-11-22T14:26:29.3895440Z 
2025-11-22T14:26:29.3895720Z 14. General Legal Terms
2025-11-22T14:26:29.3895850Z 
2025-11-22T14:26:29.3896590Z 14.1 This License Agreement constitutes the whole legal agreement between you and Google and governs your use of the GDK (excluding any services which Google may provide to you under a separate written agreement), and completely replaces any prior agreements between you and Google in relation to the GDK.
2025-11-22T14:26:29.3897160Z 
2025-11-22T14:26:29.3897910Z 14.2 You agree that if Google does not exercise or enforce any legal right or remedy which is contained in this License Agreement (or which Google has the benefit of under any applicable law), this will not be taken to be a formal waiver of Google's rights and that those rights or remedies will still be available to Google.
2025-11-22T14:26:29.3898490Z 
2025-11-22T14:26:29.3899290Z 14.3 If any court of law, having the jurisdiction to decide on this matter, rules that any provision of this License Agreement is invalid, then that provision will be removed from this License Agreement without affecting the rest of this License Agreement. The remaining provisions of this License Agreement will continue to be valid and enforceable.
2025-11-22T14:26:29.3899950Z 
2025-11-22T14:26:29.3901040Z 14.4 You acknowledge and agree that each member of the group of companies of which Google is the parent shall be third party beneficiaries to this License Agreement and that such other companies shall be entitled to directly enforce, and rely upon, any provision of this License Agreement that confers a benefit on (or rights in favor of) them. Other than this, no other person or company shall be third party beneficiaries to this License Agreement.
2025-11-22T14:26:29.3901860Z 
2025-11-22T14:26:29.3902540Z 14.5 EXPORT RESTRICTIONS. THE GDK IS SUBJECT TO UNITED STATES EXPORT LAWS AND REGULATIONS. YOU MUST COMPLY WITH ALL DOMESTIC AND INTERNATIONAL EXPORT LAWS AND REGULATIONS THAT APPLY TO THE GDK. THESE LAWS INCLUDE RESTRICTIONS ON DESTINATIONS, END USERS AND END USE.
2025-11-22T14:26:29.3903230Z 
2025-11-22T14:26:29.3904010Z 14.6 The rights granted in this License Agreement may not be assigned or transferred by either you or Google without the prior written approval of the other party. Neither you nor Google shall be permitted to delegate their responsibilities or obligations under this License Agreement without the prior written approval of the other party.
2025-11-22T14:26:29.3904630Z 
2025-11-22T14:26:29.3905760Z 14.7 This License Agreement, and your relationship with Google under this License Agreement, shall be governed by the laws of the State of California without regard to its conflict of laws provisions. You and Google agree to submit to the exclusive jurisdiction of the courts located within the county of Santa Clara, California to resolve any legal matter arising from this License Agreement. Notwithstanding this, you agree that Google shall still be allowed to apply for injunctive remedies (or an equivalent type of urgent legal relief) in any jurisdiction.
2025-11-22T14:26:29.3906820Z 
2025-11-22T14:26:29.3907090Z November 19, 2013
2025-11-22T14:26:29.3907440Z ---------------------------------------
2025-11-22T14:26:29.3907780Z Accept? (y/N): 
2025-11-22T14:26:29.3908110Z 6/6: License mips-android-sysimage-license:
2025-11-22T14:26:29.3908500Z ---------------------------------------
2025-11-22T14:26:29.3910110Z MIPS Technologies, Inc. (“MIPS”) Internal Evaluation License Agreement for MIPS Android™ System Images for Android Software Development Kit (SDK): This Internal Evaluation License Agreement (this "Agreement") is entered into by and between MIPS and you (as an individual developer or a legal entity -- identified below as “Recipient”). MIPS shall make the Evaluation Software available to Recipient as described in accordance with the terms and conditions set forth below.
2025-11-22T14:26:29.3910950Z 
2025-11-22T14:26:29.3912390Z By clicking on the “Accept” button, downloading, installing, or otherwise using the Evaluation Materials (defined below), you agree to be bound by the terms of this Agreement effective as of the date you click “Accept” (the “Effective Date”), and if doing so on behalf of an entity, you represent that you are authorized to bind the entity to the terms and conditions of this Agreement. If you do not agree to be bound by the terms and conditions of this Agreement, do not download, install, or use the Evaluation Materials.
2025-11-22T14:26:29.3913280Z 
2025-11-22T14:26:29.3913640Z 1. DEFINITIONS. These terms shall have the following meanings:
2025-11-22T14:26:29.3913840Z 
2025-11-22T14:26:29.3914470Z 1.1 “MIPS” shall mean MIPS Technologies, Inc., a Delaware corporation having a principal place of business at: 955 East Arques Ave., Sunnyvale, CA 94085
2025-11-22T14:26:29.3914810Z 
2025-11-22T14:26:29.3915430Z 1.2 “Evaluation Software” shall mean MIPS Android™ emulator system images for Android Software Development Kit (SDK), as made available to Recipient.
2025-11-22T14:26:29.3915780Z 
2025-11-22T14:26:29.3916780Z 1.3 “Evaluation Materials" means, collectively, the Evaluation Software (in source and/or object code form) and documentation (including, without limitation, any design documents, specifications, reference manuals, and other related materials) related to the Evaluation Software as made available to Recipient.
2025-11-22T14:26:29.3917360Z 
2025-11-22T14:26:29.3919860Z 1.4 “Open Source Software” means any software that requires (as a condition of use, modification and/or distribution of such software) that such software or other software incorporated into, derived from or distributed with such software (a) be disclosed or distributed in source code form; or (b) be licensed by the user to third parties for the purpose of making and/or distributing derivative works; or (c) be redistributable at no charge. Open Source Software includes, without limitation, software licensed or distributed under any of the following licenses or distribution models, or licenses or distribution models substantially similar to any of the following: (a) GNU’s General Public License (GPL) or Lesser/Library GPL (LGPL), (b) the Artistic License (e.g., PERL), (c) the Mozilla Public License, (d) the Netscape Public License, (e) the Sun Community Source License (SCSL), (f) the Sun Industry Source License (SISL), (g) the Apache Software license and (h) the Common Public License (CPL).
2025-11-22T14:26:29.3921730Z 
2025-11-22T14:26:29.3922720Z 1.5 “Pre-Release Materials” means “alpha” or “beta” designated pre-release features, which may not be fully functional, which MIPS may substantially modify in producing any production version of the Evaluation Materials, and/or which is still under development by MIPS and/or MIPS’ suppliers.
2025-11-22T14:26:29.3923270Z 
2025-11-22T14:26:29.3924430Z 2. PURPOSE. MIPS desires to make the Evaluation Materials available to Recipient solely for Recipient's internal evaluation of the Evaluation Software to evaluate the desirability of cooperating with MIPS in developing products that are compatible with the Evaluation Software and/or to advise MIPS as to possible modifications to the Evaluation Software. Recipient may not disclose, distribute, modify (except to facilitate the above-mentioned internal evaluation), or make commercial use of the Evaluation Materials or any modifications of the Evaluation Materials.
2025-11-22T14:26:29.3925940Z 
2025-11-22T14:26:29.3927410Z THE EVALUATION MATERIALS ARE PROVIDED FOR EVALUATION PURPOSES ONLY AND MAY NOT BE MODIFIED (EXCEPT TO FACILITATE THE INTERNAL EVALUATION) OR DISTRIBUTED BY RECIPIENT OR INCORPORATED INTO RECIPIENT’S PRODUCTS OR SOFTWARE. PLEASE CONTACT A MIPS SALES REPRESENTATIVE TO LEARN ABOUT THE AVAILABILITY AND COST OF A COMMERCIAL VERSION OF THE EVALUATION SOFTWARE.
2025-11-22T14:26:29.3928080Z 
2025-11-22T14:26:29.3928780Z 3. TITLE. Title to the Evaluation Materials remains with MIPS or its suppliers. Recipient shall not mortgage, pledge or encumber the Evaluation Materials in any way. Recipient shall return all Evaluation Materials, keeping no copies, upon termination or expiration of this Agreement.
2025-11-22T14:26:29.3929350Z 
2025-11-22T14:26:29.3931760Z 4. LICENSE. MIPS grants Recipient a royalty-free, personal, nontransferable, nonexclusive license under its copyrights to use the Evaluation Software only for the purposes described in paragraph 2 above and only for a period beginning on the Effective Date and extending to the first anniversary of the Effective Date (the “Evaluation Period”). Unless otherwise communicated in writing by MIPS to Recipient, to the extent the Evaluation Software is provided in more than one delivery or release (each, a “Release”) the license grant in this Section 4 and the Evaluation Period shall apply to each Release, in which case the Evaluation Period shall begin on the date that the Release is made generally available and continue to the first anniversary of such date. Recipient may not make modifications to the Evaluation Software. Recipient shall not disassemble, reverse-engineer, or decompile any software that is not provided to Recipient in source code form.
2025-11-22T14:26:29.3933350Z 
2025-11-22T14:26:29.3933450Z 
2025-11-22T14:26:29.3934240Z EXCEPT AS PROVIDED HEREIN, NO OTHER LICENSE, EXPRESS OR IMPLIED, BY ESTOPPEL OR OTHERWISE, TO ANY OTHER MIPS INTELLECTUAL PROPERTY RIGHTS IS GRANTED TO THE RECIPIENT. OTHER THAN AS EXPLICITLY SET FORTH IN PARAGRAPH 2 ABOVE, NO RIGHT TO COPY, TO REPRODUCE, TO MODIFY, OR TO CREATE DERIVATIVE WORKS OF, THE EVALUATION MATERIALS IS GRANTED HEREIN.
2025-11-22T14:26:29.3934870Z 
2025-11-22T14:26:29.3935560Z 5. NO OBLIGATION. Recipient shall have no duty to purchase or license any product from MIPS. MIPS and its suppliers shall have no obligation to provide support for, or develop a non-evaluation version of, the Evaluation Software or to license any version of it.
2025-11-22T14:26:29.3936060Z 
2025-11-22T14:26:29.3938520Z 6. MODIFICATIONS. This Agreement does not obligate Recipient to provide MIPS with comments or suggestions regarding Evaluation Materials. However, should Recipient provide MIPS with comments or suggestions for the modification, correction, improvement or enhancement of (a) the Evaluation Materials or (b) MIPS products or processes which may embody the Evaluation Materials, then Recipient agrees to grant and hereby grants to MIPS a non-exclusive, irrevocable, worldwide, fully paid-up, royalty-free license, with the right to sublicense MIPS’ licensees and customers, under Recipient’s Intellectual property rights, to use and disclose such comments and suggestions in any manner MIPS chooses and to display, perform, copy, make, have made, use, sell, offer to sell, import, and otherwise dispose of MIPS’ and its sublicensee’s products embodying such comments and suggestions in any manner and via any media MIPS chooses, without reference to the source.
2025-11-22T14:26:29.3940500Z 
2025-11-22T14:26:29.3941810Z 7. WARRANTY DISCLAIMER. MIPS AND ITS SUPPLIERS MAKE NO WARRANTIES WITH RESPECT TO EVALUATION MATERIALS, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE, OR ANY IMPLIED WARRANTY OF NONINFRINGEMENT WITH RESPECT TO THIRD PARTY INTELLECTUAL PROPERTY. RECIPIENT ACKNOWLEDGES AND AGREES THAT THE EVALUATION MATERIALS ARE PROVIDED “AS IS,” WITHOUT WARRANTY OF ANY KIND.
2025-11-22T14:26:29.3942900Z 
2025-11-22T14:26:29.3944280Z 8. LIMITATION OF LIABILITY. MIPS AND ITS SUPPLIERS SHALL NOT BE LIABLE FOR ANY PROPERTY DAMAGE, PERSONAL INJURY, LOSS OF PROFITS, INTERRUPTION OF BUSINESS OR FOR ANY DIRECT, INDIRECT, SPECIAL, CONSEQUENTIAL OR INCIDENTAL DAMAGES, HOWEVER CAUSED OR ALLEGED, WHETHER FOR BREACH OF WARRANTY, CONTRACT, STRICT LIABILITY OR OTHERWISE, INCLUDING WITHOUT LIMITATION, UNDER TORT OR OTHER LEGAL THEORY. MIPS AND ITS SUPPLIERS DISCLAIM ANY AND ALL LIABILITY, INCLUDING LIABILITY FOR INFRINGEMENT OF ANY INTELLECTUAL PROPERTY RIGHTS OF ANY KIND RELATING TO THE EVALUATION MATERIALS.
2025-11-22T14:26:29.3945280Z 
2025-11-22T14:26:29.3946120Z 9. EXPIRATION. MIPS may terminate this Agreement immediately after a breach by Recipient or otherwise at MIPS’ reasonable discretion and upon five (5) business days’ notice to Recipient.
2025-11-22T14:26:29.3946510Z 
2025-11-22T14:26:29.3946770Z 10. GENERAL.
2025-11-22T14:26:29.3946890Z 
2025-11-22T14:26:29.3949000Z 10.1 Controlling Law. This Agreement shall be governed by California law excluding its choice of law rules. With the exception of MIPS’ rights to enforce its intellectual property rights and any confidentiality obligations under this Agreement or any licenses distributed with the Evaluation Materials, all disputes and any claims arising under or relating to this Agreement shall be subject to the exclusive jurisdiction and venue of the state and federal courts located in Santa Clara County, California. Each party hereby agrees to jurisdiction and venue in the courts set forth in the preceding sentence. The parties agree that the United Nations Convention on Contracts for the International Sale of Goods is specifically excluded from application to this Agreement. The parties consent to the personal jurisdiction of the above courts.
2025-11-22T14:26:29.3950390Z 
2025-11-22T14:26:29.3951430Z 10.2 Remedies. Recipient acknowledges and agrees that any breach of confidentiality obligations under this Agreement or any licenses distributed with the Evaluation Materials, as well as any disclosure, commercialization, or public use of the Evaluation Materials, would cause irreparable injury to MIPS, and therefore Recipient agrees to consent to, and hereby consents to, the grant of an injunction by any court of competent jurisdiction in the event of an actual or threatened breach.
2025-11-22T14:26:29.3952270Z 
2025-11-22T14:26:29.3953740Z 10.3 Assignment. Recipient may not delegate, assign or transfer this Agreement, the license granted or any of Recipient’s rights, obligations, or duties hereunder, expressly, by implication, by operation of law, by way of merger (regardless of whether Recipient is the surviving entity) or acquisition, or otherwise and any attempt to do so, without MIPS’ express prior written consent, shall be ineffective, null and void. MIPS may freely assign this Agreement, and its rights and obligations hereunder, in its sole discretion.
2025-11-22T14:26:29.3954910Z 
2025-11-22T14:26:29.3955900Z 10.4 Entire Agreement. This Agreement constitutes the entire agreement between Recipient and MIPS and supersedes in their entirety any and all oral or written agreements previously existing between Recipient and MIPS with respect to the subject matter hereof. This Agreement may only be amended or supplemented by a writing that refers explicitly to this Agreement and that is signed or otherwise accepted by duly authorized representatives of Recipient and MIPS.
2025-11-22T14:26:29.3956710Z 
2025-11-22T14:26:29.3957670Z 10.5 Severability. In the event that any provision of this Agreement is finally adjudicated to be unenforceable or invalid under any applicable law, such unenforceability or invalidity shall not render this Agreement unenforceable or invalid as a whole, and, in such event, such unenforceable or invalid provision shall be interpreted so as to best accomplish the objectives of such provision within the limits of applicable law or applicable court decisions.
2025-11-22T14:26:29.3958600Z 
2025-11-22T14:26:29.3961110Z 10.6 Export Regulations / Export Control. Recipient shall not export, either directly or indirectly, any product, service or technical data or system incorporating the Evaluation Materials without first obtaining any required license or other necessary approval from the U.S. Department of Commerce or any other governing agency or department of the United States Government. In the event any product is exported from the United States or re-exported from a foreign destination by Recipient, Recipient shall ensure that the distribution and export/re-export or import of the product is in compliance with all applicable laws, regulations, orders, or other restrictions of the U.S. Export Administration Regulations and the appropriate foreign government. Recipient agrees that neither it nor any of its subsidiaries will export/re-export any technical data, process, product, or service, directly or indirectly, to any country for which the United States government or any agency thereof or the foreign government from where it is shipping requires an export license, or other governmental approval, without first obtaining such license or approval. Recipient also agrees to implement measures to ensure that foreign national employees are authorized to receive any information controlled by U.S. export control laws. An export is "deemed" to take place when information is released to a foreign national wherever located.
2025-11-22T14:26:29.3963400Z 
2025-11-22T14:26:29.3965470Z 10.7 Special Terms for Pre-Release Materials. If so indicated in the description of the Evaluation Software, the Evaluation Software may contain Pre-Release Materials. Recipient hereby understands, acknowledges and agrees that: (i) Pre-Release Materials may not be fully tested and may contain bugs or errors; (ii) Pre-Release materials are not suitable for commercial release in their current state; (iii) regulatory approvals for Pre-Release Materials (such as UL or FCC) have not been obtained, and Pre-Release Materials may therefore not be certified for use in certain countries or environments or may not be suitable for certain applications and (iv) MIPS can provide no assurance that it will ever produce or make generally available a production version of the Pre-Release Materials . MIPS is not under any obligation to develop and/or release or offer for sale or license a final product based upon the Pre-Release Materials and may unilaterally elect to abandon the Pre-Release Materials or any such development platform at any time and without any obligation or liability whatsoever to Recipient or any other person.
2025-11-22T14:26:29.3967460Z 
2025-11-22T14:26:29.3968280Z ANY PRE-RELEASE MATERIALS ARE NON-QUALIFIED AND, AS SUCH, ARE PROVIDED “AS IS” AND “AS AVAILABLE”, POSSIBLY WITH FAULTS, AND WITHOUT REPRESENTATION OR WARRANTY OF ANY KIND.
2025-11-22T14:26:29.3968850Z 
2025-11-22T14:26:29.3970140Z 10.8 Open Source Software. In the event Open Source software is included with Evaluation Software, such Open Source software is licensed pursuant to the applicable Open Source software license agreement identified in the Open Source software comments in the applicable source code file(s) and/or file header as indicated in the Evaluation Software. Additional detail may be available (where applicable) in the accompanying on-line documentation. With respect to the Open Source software, nothing in this Agreement limits any rights under, or grants rights that supersede, the terms of any applicable Open Source software license agreement.
2025-11-22T14:26:29.3971440Z ---------------------------------------
2025-11-22T14:26:29.3971830Z Accept? (y/N): All SDK package licenses accepted
2025-11-22T14:26:29.3972000Z 
2025-11-22T14:26:29.3972510Z 🔄 Updating SDK manager...
2025-11-22T14:26:30.9040730Z Loading package information...                                                  
2025-11-22T14:26:31.2625670Z Loading local repository...                                                     
2025-11-22T14:26:31.2628210Z [                                       ] 3% Loading local repository...        
2025-11-22T14:26:31.2995310Z [                                       ] 3% Fetch remote repository...         
2025-11-22T14:26:31.9734600Z [=                                      ] 3% Fetch remote repository...         
2025-11-22T14:26:32.1160220Z [=                                      ] 4% Fetch remote repository...         
2025-11-22T14:26:32.1516380Z [=                                      ] 5% Fetch remote repository...         
2025-11-22T14:26:32.2301460Z [==                                     ] 5% Fetch remote repository...         
2025-11-22T14:26:32.4892820Z [==                                     ] 6% Fetch remote repository...         
2025-11-22T14:26:32.7474900Z [==                                     ] 7% Fetch remote repository...         
2025-11-22T14:26:32.7604260Z [==                                     ] 7% Computing updates...               
2025-11-22T14:26:32.7667920Z [===                                    ] 8% Computing updates...               
2025-11-22T14:26:32.7800800Z [===                                    ] 10% Computing updates...              
2025-11-22T14:26:32.7928410Z No updates available
2025-11-22T14:26:32.8454580Z [=======================================] 100% Computing updates...             
2025-11-22T14:26:32.8475800Z 
2025-11-22T14:26:32.8636160Z 📦 Installing SDK components with Google Play Store...
2025-11-22T14:26:35.1459870Z Loading package information...                                                  
2025-11-22T14:26:35.3980370Z Loading local repository...                                                     
2025-11-22T14:26:35.4047430Z [                                       ] 3% Loading local repository...        
2025-11-22T14:26:35.4238780Z [                                       ] 3% Fetch remote repository...         
2025-11-22T14:26:36.2422860Z [=                                      ] 3% Fetch remote repository...         
2025-11-22T14:26:36.5111510Z [=                                      ] 4% Fetch remote repository...         
2025-11-22T14:26:36.6011590Z [=                                      ] 5% Fetch remote repository...         
2025-11-22T14:26:36.7669990Z [==                                     ] 5% Fetch remote repository...         
2025-11-22T14:26:37.0079210Z [==                                     ] 6% Fetch remote repository...         
2025-11-22T14:26:37.1419050Z [==                                     ] 7% Fetch remote repository...         
2025-11-22T14:26:37.1522960Z [==                                     ] 7% Computing updates...               
2025-11-22T14:26:37.2382070Z [===                                    ] 8% Computing updates...               
2025-11-22T14:26:37.2555030Z [===                                    ] 10% Computing updates...              
2025-11-22T14:26:38.1885900Z [===                                    ] 10% Installing Google Play Intel x86_6
2025-11-22T14:26:38.9955240Z [===                                    ] 10% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:26:41.9037930Z [====                                   ] 10% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:26:47.8585330Z [====                                   ] 11% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:26:54.2349740Z [====                                   ] 12% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:27:00.2939280Z [=====                                  ] 13% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:27:06.5555360Z [=====                                  ] 14% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:27:09.9173840Z [=====                                  ] 15% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:27:15.0556730Z [======                                 ] 15% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:27:29.9336050Z [======                                 ] 16% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:27:37.5122560Z [======                                 ] 17% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:27:37.5154270Z [=======                                ] 18% Downloading x86_64-30_r10-darwin.z
2025-11-22T14:27:37.6074870Z [=======                                ] 18% Unzipping...                      
2025-11-22T14:27:37.6343720Z [=======                                ] 18% Unzipping... x86_64/advancedFeatur
2025-11-22T14:27:37.6345430Z [=======                                ] 18% Unzipping... x86_64/build.prop    
2025-11-22T14:27:37.6346980Z [=======                                ] 18% Unzipping... x86_64/data/         
2025-11-22T14:27:37.6348480Z [=======                                ] 18% Unzipping... x86_64/data/misc/    
2025-11-22T14:27:37.6349830Z [=======                                ] 18% Unzipping... x86_64/data/misc/emul
2025-11-22T14:27:37.6353320Z [=======                                ] 18% Unzipping... x86_64/data/misc/gcec
2025-11-22T14:27:37.6357020Z [=======                                ] 18% Unzipping... x86_64/data/misc/apns
2025-11-22T14:27:37.6378150Z [=======                                ] 18% Unzipping... x86_64/data/misc/wifi
2025-11-22T14:27:37.6395500Z [=======                                ] 18% Unzipping... x86_64/data/system/  
2025-11-22T14:27:37.6396990Z [=======                                ] 18% Unzipping... x86_64/data/system/di
2025-11-22T14:27:37.6410400Z [=======                                ] 18% Unzipping... x86_64/data/local.pro
2025-11-22T14:27:37.7232260Z [=======                                ] 18% Unzipping... x86_64/encryptionkey.
2025-11-22T14:27:37.9004530Z [=======                                ] 18% Unzipping... x86_64/kernel-ranchu 
2025-11-22T14:27:38.0007300Z [=======                                ] 18% Unzipping... x86_64/NOTICE.txt    
2025-11-22T14:27:38.1009780Z [=======                                ] 18% Unzipping... x86_64/ramdisk.img   
2025-11-22T14:27:38.2011630Z [=======                                ] 18% Unzipping... x86_64/source.propert
2025-11-22T14:27:41.9112840Z [=======                                ] 18% Unzipping... x86_64/system.img    
2025-11-22T14:27:45.5931370Z [=======                                ] 19% Unzipping... x86_64/system.img    
2025-11-22T14:27:47.5399590Z [=======                                ] 20% Unzipping... x86_64/system.img    
2025-11-22T14:27:49.8914590Z [========                               ] 20% Unzipping... x86_64/system.img    
2025-11-22T14:27:52.7110270Z [========                               ] 21% Unzipping... x86_64/system.img    
2025-11-22T14:27:55.3306770Z [========                               ] 22% Unzipping... x86_64/system.img    
2025-11-22T14:27:59.7421120Z [=========                              ] 23% Unzipping... x86_64/system.img    
2025-11-22T14:28:06.1417630Z [=========                              ] 24% Unzipping... x86_64/system.img    
2025-11-22T14:28:07.5632130Z [=========                              ] 25% Unzipping... x86_64/system.img    
2025-11-22T14:28:07.5860290Z [=========                              ] 25% Unzipping... x86_64/userdata.img  
2025-11-22T14:28:11.2111720Z [=========                              ] 25% Unzipping... x86_64/vendor.img    
2025-11-22T14:28:11.2882110Z [=========                              ] 25% Unzipping... x86_64/VerifiedBootPa
2025-11-22T14:28:11.5776010Z [===============                        ] 40% Unzipping... x86_64/VerifiedBootPa
2025-11-22T14:28:11.9079200Z [===============                        ] 40% Installing Android SDK Build-Tools
2025-11-22T14:28:12.2694630Z [===============                        ] 40% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:12.4540910Z [================                       ] 40% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:12.5693760Z [================                       ] 41% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:12.6802750Z [================                       ] 42% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:12.7919640Z [=================                      ] 43% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:12.8954420Z [=================                      ] 44% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:12.9534730Z [=================                      ] 45% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:13.0135770Z [==================                     ] 45% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:13.1233370Z [==================                     ] 46% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:13.2836940Z [==================                     ] 47% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:13.3059610Z [==================                     ] 48% Downloading f6d24b187cc6bd534c6c37
2025-11-22T14:28:13.3262770Z [==================                     ] 48% Unzipping... x86_64/VerifiedBootPa
2025-11-22T14:28:13.4054760Z [==================                     ] 48% Unzipping... android-11/          
2025-11-22T14:28:13.4088670Z [==================                     ] 48% Unzipping... android-11/aapt      
2025-11-22T14:28:13.4150010Z [===================                    ] 48% Unzipping... android-11/aapt      
2025-11-22T14:28:13.4447190Z [===================                    ] 48% Unzipping... android-11/aapt2     
2025-11-22T14:28:13.4704600Z [===================                    ] 48% Unzipping... android-11/aarch64-li
2025-11-22T14:28:13.4750460Z [===================                    ] 48% Unzipping... android-11/aidl      
2025-11-22T14:28:13.4752910Z [===================                    ] 48% Unzipping... android-11/apksigner 
2025-11-22T14:28:13.4781710Z [===================                    ] 48% Unzipping... android-11/arm-linux-
2025-11-22T14:28:13.4818120Z [===================                    ] 48% Unzipping... android-11/bcc_compat
2025-11-22T14:28:13.4888200Z [===================                    ] 48% Unzipping... android-11/core-lambd
2025-11-22T14:28:13.4910070Z [===================                    ] 48% Unzipping... android-11/d8        
2025-11-22T14:28:13.4946060Z [===================                    ] 48% Unzipping... android-11/dexdump   
2025-11-22T14:28:13.5091730Z [===================                    ] 48% Unzipping... android-11/dx        
2025-11-22T14:28:13.5100400Z [===================                    ] 48% Unzipping... android-11/i686-linux
2025-11-22T14:28:13.5103500Z [===================                    ] 48% Unzipping... android-11/lib/      
2025-11-22T14:28:13.5106540Z [===================                    ] 48% Unzipping... android-11/lib/apksig
2025-11-22T14:28:13.5112190Z [===================                    ] 48% Unzipping... android-11/lib/d8.jar
2025-11-22T14:28:13.5153050Z [===================                    ] 49% Unzipping... android-11/lib/d8.jar
2025-11-22T14:28:13.5156690Z [===================                    ] 49% Unzipping... android-11/lib/dx.jar
2025-11-22T14:28:13.5159760Z [===================                    ] 49% Unzipping... android-11/lib/shrink
2025-11-22T14:28:13.5162300Z [===================                    ] 49% Unzipping... android-11/lib64/    
2025-11-22T14:28:13.5164640Z [===================                    ] 49% Unzipping... android-11/lib64/liba
2025-11-22T14:28:13.5167200Z [===================                    ] 49% Unzipping... android-11/lib64/libb
2025-11-22T14:28:13.5690830Z [===================                    ] 49% Unzipping... android-11/lib64/libc
2025-11-22T14:28:13.6456140Z [===================                    ] 50% Unzipping... android-11/lib64/libc
2025-11-22T14:28:13.6906250Z [====================                   ] 50% Unzipping... android-11/lib64/libc
2025-11-22T14:28:13.7131340Z [====================                   ] 50% Unzipping... android-11/lib64/libL
2025-11-22T14:28:14.0973540Z [====================                   ] 51% Unzipping... android-11/lib64/libL
2025-11-22T14:28:14.1560690Z [====================                   ] 52% Unzipping... android-11/lib64/libL
2025-11-22T14:28:14.1574740Z [====================                   ] 52% Unzipping... android-11/lld       
2025-11-22T14:28:14.1578760Z [====================                   ] 52% Unzipping... android-11/lld-bin/  
2025-11-22T14:28:14.2607470Z [====================                   ] 52% Unzipping... android-11/lld-bin/ll
2025-11-22T14:28:14.4044540Z [=====================                  ] 53% Unzipping... android-11/lld-bin/ll
2025-11-22T14:28:14.4222650Z [=====================                  ] 54% Unzipping... android-11/lld-bin/ll
2025-11-22T14:28:14.4323680Z [=====================                  ] 54% Unzipping... android-11/llvm-rs-cc
2025-11-22T14:28:14.4341610Z [=====================                  ] 54% Unzipping... android-11/mainDexCla
2025-11-22T14:28:14.4346060Z [=====================                  ] 54% Unzipping... android-11/mipsel-lin
2025-11-22T14:28:14.4411690Z [=====================                  ] 54% Unzipping... android-11/NOTICE.txt
2025-11-22T14:28:14.6348490Z [=====================                  ] 54% Unzipping... android-11/renderscri
2025-11-22T14:28:14.7154110Z [=====================                  ] 55% Unzipping... android-11/renderscri
2025-11-22T14:28:14.7976470Z [=====================                  ] 55% Unzipping... android-11/runtime.pr
2025-11-22T14:28:14.7978420Z [=====================                  ] 55% Unzipping... android-11/source.pro
2025-11-22T14:28:14.7980360Z [=====================                  ] 55% Unzipping... android-11/split-sele
2025-11-22T14:28:14.7985930Z [=====================                  ] 55% Unzipping... android-11/x86_64-lin
2025-11-22T14:28:14.7988480Z [=====================                  ] 55% Unzipping... android-11/zipalign  
2025-11-22T14:28:14.7989970Z [===========================            ] 70% Unzipping... android-11/zipalign  
2025-11-22T14:28:14.8365270Z [===========================            ] 70% Installing Android SDK Platform 30
2025-11-22T14:28:14.9368990Z [===========================            ] 70% Downloading platform-30_r03.zip...
2025-11-22T14:28:15.0371930Z [============================           ] 70% Downloading platform-30_r03.zip...
2025-11-22T14:28:15.1335990Z [============================           ] 71% Downloading platform-30_r03.zip...
2025-11-22T14:28:15.1436020Z [============================           ] 72% Downloading platform-30_r03.zip...
2025-11-22T14:28:15.3217650Z [=============================          ] 73% Downloading platform-30_r03.zip...
2025-11-22T14:28:15.3536220Z [=============================          ] 74% Downloading platform-30_r03.zip...
2025-11-22T14:28:15.4100350Z [=============================          ] 75% Downloading platform-30_r03.zip...
2025-11-22T14:28:15.4712160Z [==============================         ] 75% Downloading platform-30_r03.zip...
2025-11-22T14:28:15.5806410Z [==============================         ] 76% Downloading platform-30_r03.zip...
2025-11-22T14:28:15.8252910Z [==============================         ] 77% Downloading platform-30_r03.zip...
2025-11-22T14:28:16.3869270Z [==============================         ] 77% Unzipping... android-11/zipalign  
2025-11-22T14:28:16.4019600Z [==============================         ] 77% Unzipping... android-11/          
2025-11-22T14:28:16.4149620Z [==============================         ] 77% Unzipping... android-11/android.ja
2025-11-22T14:28:16.4423930Z [===============================        ] 78% Unzipping... android-11/android.ja
2025-11-22T14:28:16.5714350Z [===============================        ] 79% Unzipping... android-11/android.ja
2025-11-22T14:28:16.6030170Z [===============================        ] 80% Unzipping... android-11/android.ja
2025-11-22T14:28:16.6096350Z [================================       ] 80% Unzipping... android-11/android.ja
2025-11-22T14:28:16.6140410Z [================================       ] 80% Unzipping... android-11/optional/ 
2025-11-22T14:28:16.6168800Z [================================       ] 80% Unzipping... android-11/optional/a
2025-11-22T14:28:16.6187390Z [================================       ] 80% Unzipping... android-11/optional/o
2025-11-22T14:28:16.6286390Z [================================       ] 80% Unzipping... android-11/optional/a
2025-11-22T14:28:16.6547940Z [================================       ] 80% Unzipping... android-11/optional/o
2025-11-22T14:28:16.6595710Z [================================       ] 80% Unzipping... android-11/templates/
2025-11-22T14:28:16.6643400Z [================================       ] 80% Unzipping... android-11/core-for-s
2025-11-22T14:28:16.6699700Z [================================       ] 81% Unzipping... android-11/core-for-s
2025-11-22T14:28:16.6730530Z [================================       ] 81% Unzipping... android-11/build.prop
2025-11-22T14:28:16.6774660Z [================================       ] 81% Unzipping... android-11/android-st
2025-11-22T14:28:16.6786610Z [================================       ] 81% Unzipping... android-11/uiautomato
2025-11-22T14:28:16.6810350Z [================================       ] 81% Unzipping... android-11/source.pro
2025-11-22T14:28:16.6838830Z [================================       ] 81% Unzipping... android-11/data/     
2025-11-22T14:28:16.6936720Z [================================       ] 81% Unzipping... android-11/data/servi
2025-11-22T14:28:16.6968480Z [================================       ] 81% Unzipping... android-11/data/NOTIC
2025-11-22T14:28:16.6970310Z [================================       ] 81% Unzipping... android-11/data/widge
2025-11-22T14:28:16.7000480Z [================================       ] 81% Unzipping... android-11/data/broad
2025-11-22T14:28:16.7057120Z [================================       ] 81% Unzipping... android-11/data/api-v
2025-11-22T14:28:16.7077620Z [================================       ] 81% Unzipping... android-11/data/featu
2025-11-22T14:28:16.7102210Z [================================       ] 81% Unzipping... android-11/data/annot
2025-11-22T14:28:16.7126930Z [================================       ] 81% Unzipping... android-11/data/res/ 
2025-11-22T14:28:16.9084010Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:16.9303590Z [================================       ] 81% Unzipping... android-11/data/res/l
2025-11-22T14:28:16.9765530Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:16.9817810Z [================================       ] 81% Unzipping... android-11/data/res/m
2025-11-22T14:28:17.0114000Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.0166910Z [================================       ] 81% Unzipping... android-11/data/res/a
2025-11-22T14:28:17.0484440Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.1785840Z [================================       ] 81% Unzipping... android-11/data/res/d
2025-11-22T14:28:17.1941450Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.1950170Z [================================       ] 81% Unzipping... android-11/data/res/x
2025-11-22T14:28:17.1995920Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.1999910Z [================================       ] 81% Unzipping... android-11/data/res/l
2025-11-22T14:28:17.2007240Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.3833360Z [================================       ] 81% Unzipping... android-11/data/res/l
2025-11-22T14:28:17.3942540Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.3952650Z [================================       ] 81% Unzipping... android-11/data/res/r
2025-11-22T14:28:17.5139680Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.6096280Z [================================       ] 81% Unzipping... android-11/data/res/x
2025-11-22T14:28:17.6110760Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.6114690Z [================================       ] 81% Unzipping... android-11/data/res/r
2025-11-22T14:28:17.6116540Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.7768380Z [================================       ] 81% Unzipping... android-11/data/res/a
2025-11-22T14:28:17.8648030Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.8669820Z [================================       ] 81% Unzipping... android-11/data/res/r
2025-11-22T14:28:17.8825350Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:17.8866320Z [================================       ] 81% Unzipping... android-11/data/res/c
2025-11-22T14:28:17.8886730Z [================================       ] 81% Unzipping... android-11/data/res/v
2025-11-22T14:28:18.1917090Z [================================       ] 81% Unzipping... android-11/data/res/d
2025-11-22T14:28:18.6901560Z [================================       ] 82% Unzipping... android-11/data/res/d
2025-11-22T14:28:18.6965630Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:18.6976400Z [================================       ] 82% Unzipping... android-11/data/res/t
2025-11-22T14:28:18.7023850Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:18.7047260Z [================================       ] 82% Unzipping... android-11/data/res/x
2025-11-22T14:28:18.7355140Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:18.7368030Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:18.7742460Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:18.7755050Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:18.7794890Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:18.7805590Z [================================       ] 82% Unzipping... android-11/data/res/l
2025-11-22T14:28:18.8522390Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:18.8532240Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:18.8549550Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:18.8624070Z [================================       ] 82% Unzipping... android-11/data/res/d
2025-11-22T14:28:18.8834310Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:18.9093240Z [================================       ] 82% Unzipping... android-11/data/res/d
2025-11-22T14:28:19.0297820Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.0311850Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:19.0519600Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.0534230Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:19.1230590Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.1234740Z [================================       ] 82% Unzipping... android-11/data/res/m
2025-11-22T14:28:19.1269700Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.1280700Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:19.1353410Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.1383410Z [================================       ] 82% Unzipping... android-11/data/res/c
2025-11-22T14:28:19.1401820Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.1454950Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:19.1526520Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.1544900Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:19.1553590Z [================================       ] 82% Unzipping... android-11/data/res/x
2025-11-22T14:28:19.2291190Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.6528440Z [================================       ] 82% Unzipping... android-11/data/res/d
2025-11-22T14:28:19.6529220Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.6532090Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:19.6721930Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.6734440Z [================================       ] 82% Unzipping... android-11/data/res/m
2025-11-22T14:28:19.6898600Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.6908400Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:19.7337980Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.7359660Z [================================       ] 82% Unzipping... android-11/data/res/r
2025-11-22T14:28:19.7436840Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.7454650Z [================================       ] 82% Unzipping... android-11/data/res/i
2025-11-22T14:28:19.7652190Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.7720690Z [================================       ] 82% Unzipping... android-11/data/res/d
2025-11-22T14:28:19.7763320Z [================================       ] 82% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.7821500Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:19.7832780Z [=================================      ] 83% Unzipping... android-11/data/res/m
2025-11-22T14:28:19.7855010Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:20.0806670Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-22T14:28:20.1017560Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:20.1032460Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-22T14:28:20.1145200Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:20.1226410Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-22T14:28:20.2042290Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:20.2047100Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-22T14:28:20.2048590Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:20.2052160Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-22T14:28:20.2053900Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:20.2057890Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-22T14:28:20.2061940Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:20.2214050Z [=================================      ] 83% Unzipping... android-11/data/res/x
2025-11-22T14:28:20.2588920Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:20.2595430Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-22T14:28:20.3457480Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:20.9259820Z [=================================      ] 83% Unzipping... android-11/data/res/d
2025-11-22T14:28:20.9621450Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:20.9633790Z [=================================      ] 83% Unzipping... android-11/data/res/a
2025-11-22T14:28:21.0451400Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.0458060Z [=================================      ] 83% Unzipping... android-11/data/res/r
2025-11-22T14:28:21.0546210Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.0552290Z [=================================      ] 83% Unzipping... android-11/data/res/m
2025-11-22T14:28:21.0559580Z [=================================      ] 83% Unzipping... android-11/data/res/x
2025-11-22T14:28:21.0831490Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.0991840Z [=================================      ] 83% Unzipping... android-11/data/res/a
2025-11-22T14:28:21.1425470Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.1603960Z [=================================      ] 83% Unzipping... android-11/data/res/i
2025-11-22T14:28:21.1673990Z [=================================      ] 83% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.1980850Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.1986360Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-22T14:28:21.2064940Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.2072690Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-22T14:28:21.2101890Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.2111820Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-22T14:28:21.2390220Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.2415330Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-22T14:28:21.2439660Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.2449500Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-22T14:28:21.2702120Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.2801810Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-22T14:28:21.2807540Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.2817350Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-22T14:28:21.2989910Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.3019400Z [=================================      ] 84% Unzipping... android-11/data/res/m
2025-11-22T14:28:21.3146110Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.3212890Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-22T14:28:21.3215580Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.3233110Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-22T14:28:21.3911060Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.3917800Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-22T14:28:21.3985970Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.4049020Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-22T14:28:21.4235890Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.4240610Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-22T14:28:21.4270250Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.4287880Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-22T14:28:21.4296330Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.4592550Z [=================================      ] 84% Unzipping... android-11/data/res/c
2025-11-22T14:28:21.4859290Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:21.4861470Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-22T14:28:21.4875120Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:22.2551620Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-22T14:28:22.3552720Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:22.4554660Z [=================================      ] 84% Unzipping... android-11/data/res/m
2025-11-22T14:28:22.5557300Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:22.6559430Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-22T14:28:22.7562410Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:22.8564310Z [=================================      ] 84% Unzipping... android-11/data/res/m
2025-11-22T14:28:22.9557900Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:22.9621610Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-22T14:28:22.9642580Z [=================================      ] 84% Unzipping... android-11/data/res/l
2025-11-22T14:28:22.9662490Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:22.9672910Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-22T14:28:22.9768280Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:22.9795740Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-22T14:28:22.9839590Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:22.9901820Z [=================================      ] 84% Unzipping... android-11/data/res/r
2025-11-22T14:28:23.0292300Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:23.0409700Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-22T14:28:23.0468100Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:23.0553170Z [=================================      ] 84% Unzipping... android-11/data/res/d
2025-11-22T14:28:23.0634010Z [=================================      ] 84% Unzipping... android-11/data/res/v
2025-11-22T14:28:23.0660370Z [=================================      ] 84% Unzipping... android-11/data/categ
2025-11-22T14:28:23.0661130Z [=================================      ] 84% Unzipping... android-11/data/activ
2025-11-22T14:28:23.0695840Z [=================================      ] 84% Unzipping... android-11/sdk.proper
2025-11-22T14:28:23.0917390Z [=================================      ] 84% Unzipping... android-11/skins/    
2025-11-22T14:28:23.1009970Z [=================================      ] 84% Unzipping... android-11/skins/WXGA
2025-11-22T14:28:23.2491480Z [=================================      ] 84% Unzipping... android-11/skins/WQVG
2025-11-22T14:28:23.2516690Z [=================================      ] 84% Unzipping... android-11/skins/NOTI
2025-11-22T14:28:23.2622540Z [=================================      ] 84% Unzipping... android-11/skins/HVGA
2025-11-22T14:28:23.2689930Z [=================================      ] 84% Unzipping... android-11/skins/WVGA
2025-11-22T14:28:23.2735140Z [=================================      ] 84% Unzipping... android-11/skins/WQVG
2025-11-22T14:28:23.2736760Z [=================================      ] 85% Unzipping... android-11/skins/WQVG
2025-11-22T14:28:23.2784540Z [=================================      ] 85% Unzipping... android-11/skins/WVGA
2025-11-22T14:28:23.2830540Z [=================================      ] 85% Unzipping... android-11/skins/QVGA
2025-11-22T14:28:23.2911630Z [=================================      ] 85% Unzipping... android-11/skins/WXGA
2025-11-22T14:28:23.2959210Z [=================================      ] 85% Unzipping... android-11/skins/WSVG
2025-11-22T14:28:23.3018490Z [=================================      ] 85% Unzipping... android-11/skins/WXGA
2025-11-22T14:28:23.3058940Z [=================================      ] 85% Unzipping... android-11/framework.
2025-11-22T14:28:23.3185650Z [=======================================] 100% Unzipping... android-11/framework
2025-11-22T14:28:23.3218720Z 
2025-11-22T14:28:23.3541480Z ✅ SDK components installation completed
2025-11-22T14:28:28.4006180Z 🔍 Verifying system image installation...
2025-11-22T14:28:28.4007260Z Checking path: /Users/runner/Library/Android/sdk/system-images/android-30/google_apis_playstore/x86_64
2025-11-22T14:28:28.4007920Z ✅ Google Play system image found!
2025-11-22T14:28:28.4081370Z total 5947648
2025-11-22T14:28:28.4083010Z drwxr-xr-x  15 runner  staff         480 Nov 22 14:28 .
2025-11-22T14:28:28.4083550Z drwxr-xr-x   3 runner  staff          96 Nov 22 14:28 ..
2025-11-22T14:28:28.4084020Z -rw-r--r--   1 runner  staff     2936563 Nov 22 14:27 NOTICE.txt
2025-11-22T14:28:28.4084680Z -rw-r--r--   1 runner  staff         356 Nov 22 14:28 VerifiedBootParams.textproto
2025-11-22T14:28:28.4085490Z -rw-r--r--   1 runner  staff         424 Nov 22 14:27 advancedFeatures.ini
2025-11-22T14:28:28.4086010Z -rw-r--r--   1 runner  staff        2095 Nov 22 14:27 build.prop
2025-11-22T14:28:28.4086440Z drwxr-xr-x   5 runner  staff         160 Nov 22 14:27 data
2025-11-22T14:28:28.4086890Z -rw-r--r--   1 runner  staff    18874368 Nov 22 14:27 encryptionkey.img
2025-11-22T14:28:28.4087370Z -rw-r--r--   1 runner  staff    16559680 Nov 22 14:27 kernel-ranchu
2025-11-22T14:28:28.4087860Z -rw-r--r--   1 runner  staff       19113 Nov 22 14:28 package.xml
2025-11-22T14:28:28.4088310Z -rw-r--r--   1 runner  staff     1346686 Nov 22 14:27 ramdisk.img
2025-11-22T14:28:28.4088770Z -rw-r--r--   1 runner  staff         304 Nov 22 14:27 source.properties
2025-11-22T14:28:28.4089230Z -rw-r--r--   1 runner  staff  2832203776 Nov 22 14:28 system.img
2025-11-22T14:28:28.4089720Z -rw-r--r--   1 runner  staff     1048576 Nov 22 14:28 userdata.img
2025-11-22T14:28:28.4091050Z -rw-r--r--   1 runner  staff   167772160 Nov 22 14:28 vendor.img
2025-11-22T14:28:28.4092020Z 🔧 Verifying ADB...
2025-11-22T14:28:28.6597400Z Android Debug Bridge version 1.0.41
2025-11-22T14:28:28.6598540Z Version 36.0.0-13206524
2025-11-22T14:28:28.6599820Z Installed as /Users/runner/Library/Android/sdk/platform-tools/adb
2025-11-22T14:28:28.6601050Z Running on Darwin 23.6.0 (x86_64)
2025-11-22T14:28:28.6608240Z 📋 Installed system images:
2025-11-22T14:28:30.4517730Z   system-images;android-30;google_apis_playstore;x86_64 | 10            | Google Play Intel x86_64 Atom System Image | system-images/android-30/google_apis_playstore/x86_64
2025-11-22T14:28:30.4557170Z 
2025-11-22T14:28:30.4579490Z 📱 Creating Android Emulator with Google Play Store...
2025-11-22T14:28:30.9159510Z Creating emulator with Google Play Store support...
2025-11-22T14:28:32.5347210Z Loading local repository...                                                     
2025-11-22T14:28:32.5557660Z [=========                              ] 25% Loading local repository...       
2025-11-22T14:28:32.5724190Z [=========                              ] 25% Fetch remote repository...        
2025-11-22T14:28:32.5825200Z [=======================================] 100% Fetch remote repository...       
2025-11-22T14:28:33.6210920Z 🔍 Verifying emulator creation...
2025-11-22T14:28:33.9041280Z test_emulator_playstore
2025-11-22T14:28:33.9678780Z ✅ Emulator 'test_emulator_playstore' created successfully
2025-11-22T14:28:33.9691080Z 🚀 Starting emulator with optimized settings...
2025-11-22T14:28:33.9704860Z Emulator PID: 8721
2025-11-22T14:28:33.9708670Z ⏳ Waiting for emulator device to be detected...
2025-11-22T14:28:33.9987790Z * daemon not running; starting now at tcp:5037
2025-11-22T14:28:37.3718790Z * daemon started successfully
2025-11-22T14:37:23.8428250Z ✅ Device detected
2025-11-22T14:37:23.8431010Z ⏳ Waiting for boot_completed flag...
2025-11-22T14:37:24.1694080Z ✅ Boot completed flag set!
2025-11-22T14:37:24.1697830Z ⏳ Waiting for Android system services (max 90 seconds)...
2025-11-22T14:37:27.7105180Z ✅ All critical services are ready!
2025-11-22T14:37:27.7106020Z ⏳ Allowing system to stabilize (15 seconds)...
2025-11-22T14:37:42.8711500Z 🔍 Final system verification...
2025-11-22T14:37:42.8825730Z ❌ ADB shell connection failed
2025-11-22T14:37:42.8865330Z 
2025-11-22T14:37:42.8976630Z ##[error]Bash exited with code '1'.
2025-11-22T14:37:42.9039180Z ##[section]Finishing: Setup Android SDK and Create Emulator with Google Play