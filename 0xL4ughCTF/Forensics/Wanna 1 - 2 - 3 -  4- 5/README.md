# Wanna 1 [50 pts]

**Category:** Forensics
**Solves:** 39

## Description
>MMOX company got a phishing campain and we need you to investigate it so we got you this dump.

Q1:What is the Sha256 of the Memory img?
Q2: What is the sutiable profile for the memory Dump ?

Download: https://drive.google.com/file/d/1wNBxQDFtioieSE5QvrpjnJ787-PpKtA9/view?usp=sharing

Flag: 0xL4ugh{ans1_ans2}

Author: MMOX

## Solution
İlk soruda bizden imajın SHA256 hash'i ve profili isteniyor.

```
┌──(kali㉿kali)-[~/Scripts/volatility]
└─$ sha256sum /home/kali/Desktop/WANNA/Wanna-MEM.vmem 
7f7c94e941d39f7b6217e98295c761c90d215eea0fe988327984d8f57bf86205  /home/kali/Desktop/WANNA/Wanna-MEM.vmem
```

İlk cevabımız SHA256 değeri, bu cepte dursun.

Profili öğrenmek için imageinfo komutunu çalıştırıyoruz.

Not: Windows 10 ve üzeri imajlar için volatility'i güncel tutmak çok önemli, yeni profiller eklendiğinde volatility'in imageinfo komutu başarısız olabilir.

```
┌──(kali㉿kali)-[~/Scripts/volatility]
└─$ python2 vol.py -f /home/kali/Desktop/WANNA/Wanna-MEM.vmem imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win10x64_19041
                     AS Layer1 : SkipDuplicatesAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/kali/Desktop/WANNA/Wanna-MEM.vmem)
                      PAE type : No PAE
                           DTB : 0x1ad002L
                          KDBG : 0xf8025f205b20L
          Number of Processors : 2
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0xfffff8025d43b000L
                KPCR for CPU 1 : 0xffff8f0028dc3000L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2023-02-15 16:23:06 UTC+0000
     Image local date and time : 2023-02-15 08:23:06 -0800
```

## Flag
0xL4ugh{7f7c94e941d39f7b6217e98295c761c90d215eea0fe988327984d8f57bf86205_Win10x64_19041}
# Wanna 2 [331 pts]

**Category:** Forensics
**Solves:** 14

## Description
>Q3: It was a phishing campaign what is the attacker email ?
Q4: What is the sha256 of the malicious file ?

File: Same as Wanna 1
Flag: 0xL4ugh{ans1_ans2}

Author: MMOX

## Solution
Bu denemenin, bir kimlik avı denemesi olduğunu söylüyor ve bizden attacker'in mailini istiyor. Ayrıca zararlı dosyanın sha256 değerini de istiyor. İlk önce çalışan mail uygulamasının türünü öğrenebilmek için psscan komutu çalıştırıyoruz.
```
┌──(root㉿kali)-[/home/kali/Scripts/volatility]
└─# python2 vol.py -f /home/kali/Desktop/WANNA/Wanna-MEM.vmem --profile=Win10x64_19041 psscan              
Volatility Foundation Volatility Framework 2.6.1
Offset(P)          Name                PID   PPID PDB                Time created                   Time exited                   
------------------ ---------------- ------ ------ ------------------ ------------------------------ ------------------------------
0x0000a20fe2b27080 SearchIndexer.     2144    668 0x000000000f3ad002 2023-02-15 13:50:25 UTC+0000                                 
0x0000a20fe2b55080 NisSrv.exe         3268    668 0x000000002c6b2002 2023-02-15 13:48:35 UTC+0000                                 
0x0000a20fe47752c0 svchost.exe         748    668 0x0000000013e9e002 2023-02-15 13:48:18 UTC+0000                                 
0x0000a20fe47782c0 svchost.exe         704    668 0x00000000179eb002 2023-02-15 13:48:18 UTC+0000                                 
0x0000a20fe477e2c0 svchost.exe        1012    668 0x0000000016be9002 2023-02-15 13:48:18 UTC+0000                                 
0x0000a20fe4f30080 SearchProtocol     4216   2144 0x0000000031a71002 2023-02-15 16:20:56 UTC+0000                                 
0x0000a20fe6652080 wininit.exe         528    420 0x000000000e1dd002 2023-02-15 13:48:16 UTC+0000                                 
0x0000a20fe6659080 csrss.exe           548    520 0x0000000012d59002 2023-02-15 13:48:16 UTC+0000                                 
0x0000a20fe66c2080 lsass.exe           692    528 0x0000000012774002 2023-02-15 13:48:17 UTC+0000                                 
0x0000a20fe679b2c0 svchost.exe         912    668 0x0000000014684002 2023-02-15 13:48:17 UTC+0000                                 
0x0000a20fe70c8080 StartMenuExper     4720    788 0x000000002bf59002 2023-02-15 13:51:01 UTC+0000                                 
0x0000a20fe70d10c0 dwm.exe            1016    620 0x000000001598a002 2023-02-15 13:48:18 UTC+0000                                 
0x0000a20fe70f2240 svchost.exe         552    668 0x00000000183d5002 2023-02-15 13:48:18 UTC+0000                                 
0x0000a20fe710c2c0 svchost.exe        1032    668 0x0000000014a65002 2023-02-15 13:48:18 UTC+0000                                 
0x0000a20fe71162c0 svchost.exe        1064    668 0x00000000190f3002 2023-02-15 13:48:18 UTC+0000                                 
0x0000a20fe7136240 svchost.exe        1128    668 0x0000000019390002 2023-02-15 13:48:18 UTC+0000                                 
0x0000a20fe7267080 svchost.exe        1496    668 0x000000001a157002 2023-02-15 13:48:18 UTC+0000                                 
0x0000a20fe7285080 backgroundTask     3716    788 0x000000000bb89002 2023-02-15 16:22:58 UTC+0000                                 
0x0000a20fe73c72c0 svchost.exe        1920    668 0x0000000002459002 2023-02-15 13:48:19 UTC+0000                                 
0x0000a20fe743d2c0 svchost.exe        2036    668 0x0000000020606002 2023-02-15 13:48:20 UTC+0000                                 
0x0000a20fe7489080 svchost.exe        1792    668 0x00000000228e4002 2023-02-15 13:48:20 UTC+0000                                 
0x0000a20fe755a080 ShellExperienc     5280    788 0x000000000b42f002 2023-02-15 13:53:07 UTC+0000                                 
0x0000a20fe755b2c0 svchost.exe        2608    668 0x00000000218dc002 2023-02-15 13:50:25 UTC+0000                                 
0x0000a20fe75aa340 spoolsv.exe        2200    668 0x00000000250ff002 2023-02-15 13:48:20 UTC+0000                                 
0x0000a20fe75ac240 svchost.exe        2172    668 0x0000000027057002 2023-02-15 13:48:20 UTC+0000                                 
0x0000a20fe768e0c0 VGAuthService.     2492    668 0x000000002960e002 2023-02-15 13:48:21 UTC+0000                                 
0x0000a20fe769d300 vmtoolsd.exe       2536    668 0x00000000235d0002 2023-02-15 13:48:21 UTC+0000                                 
0x0000a20fe76b4300 MsMpEng.exe        2568    668 0x0000000023939002 2023-02-15 13:48:21 UTC+0000                                 
0x0000a20fe7733080 svchost.exe        3104    668 0x0000000028367002 2023-02-15 13:48:25 UTC+0000                                 
0x0000a20fe7735280 dllhost.exe        3000    668 0x0000000025b94002 2023-02-15 13:48:23 UTC+0000                                 
0x0000a20fe7760080 svchost.exe        1100    668 0x000000003060f002 2023-02-15 13:48:25 UTC+0000                                 
0x0000a20fe78a5200 vm3dservice.ex     2680   2500 0x0000000026d85002 2023-02-15 13:48:21 UTC+0000                                 
0x0000a20fe7b57280 dasHost.exe        3196   1128 0x000000002f47f002 2023-02-15 13:48:25 UTC+0000                                 
0x0000a20fe7df6340 SgrmBroker.exe     1304    668 0x0000000006280002 2023-02-15 13:50:24 UTC+0000                                 
0x0000a20fe7e4f080 PhoneExperienc     6008    788 0x0000000008d9e002 2023-02-15 13:51:27 UTC+0000                                 
0x0000a20fe7e522c0 svchost.exe        3900    668 0x0000000031943002 2023-02-15 13:48:55 UTC+0000                                 
0x0000a20fe804e300 taskhostw.exe      3920    552 0x00000000294f4002 2023-02-15 13:50:54 UTC+0000                                 
0x0000a20fe8061080 sihost.exe         1084    552 0x0000000026698002 2023-02-15 13:50:54 UTC+0000                                 
0x0000a20fe80912c0 ApplicationFra     5332    788 0x0000000008fea002 2023-02-15 13:53:41 UTC+0000                                 
0x0000a20fe81ae280 ctfmon.exe         3496   1128 0x0000000029eac002 2023-02-15 13:50:54 UTC+0000                                 
0x0000a20fe8235340 explorer.exe       2324   1072 0x00000000236e4002 2023-02-15 13:50:55 UTC+0000                                 
0x0000a20fe8851080 conhost.exe        6976   7032 0x0000000035c4f002 2023-02-15 16:21:21 UTC+0000                                 
0x0000a20fe8888300 svchost.exe        4452    668 0x0000000002981002 2023-02-15 13:50:58 UTC+0000                                 
0x0000a20fe8b67300 RuntimeBroker.     5052    788 0x000000002d48a002 2023-02-15 13:51:04 UTC+0000                                 
0x0000a20fe8c312c0 dllhost.exe         988    788 0x000000003b794002 2023-02-15 13:53:24 UTC+0000                                 
0x0000a20fe8c46080 smartscreen.ex     5272    788 0x000000001fefe002 2023-02-15 13:51:16 UTC+0000                                 
0x0000a20fe8c47300 RuntimeBroker.     5180    788 0x000000001a719002 2023-02-15 13:51:13 UTC+0000                                 
0x0000a20fe8c4a240 SecurityHealth     5316   2324 0x00000000377b1002 2023-02-15 13:51:16 UTC+0000                                 
0x0000a20fe8c52240 SecurityHealth     5348    668 0x0000000015b46002 2023-02-15 13:51:17 UTC+0000                                 
0x0000a20fe8d7d080 OUTLOOK.EXE        5796   2324 0x000000000940b002 2023-02-15 16:20:45 UTC+0000                                 
0x0000a20fe9189080 wuauclt.exe        5924    552 0x0000000034269002 2023-02-15 16:22:36 UTC+0000                                 
0x0000a20fe919d080 MpCmdRun.exe       7032   2568 0x0000000035c12002 2023-02-15 16:21:21 UTC+0000                                 
0x0000a20fe91ae080 vmtoolsd.exe       5424   2324 0x000000003775e002 2023-02-15 13:51:17 UTC+0000                                 
0x0000a20fe9216080 taskhsvc.exe       6916   3780 0x00000000275e0002 2023-02-15 16:22:09 UTC+0000                                 
0x0000a20fe9225080 conhost.exe        5904   6916 0x0000000030c2e002 2023-02-15 16:22:09 UTC+0000                                 
0x0000a20fe923b080 SearchProtocol     5224   2144 0x000000001c4f2002 2023-02-15 16:21:13 UTC+0000                                 
0x0000a20fe92570c0 WINWORD.EXE        2064   2324 0x000000002bd9d002 2023-02-15 13:52:40 UTC+0000                                 
0x0000a20fe92ce080 MpCmdRun.exe       5920   3756 0x0000000023190002 2023-02-15 16:21:20 UTC+0000                                 
0x0000a20fe9346080 audiodg.exe        4864   2036 0x0000000000cb1002 2023-02-15 16:22:20 UTC+0000                                 
0x0000a20fe94020c0 TextInputHost.     1448    788 0x0000000031e72002 2023-02-15 13:53:22 UTC+0000                                 
0x0000a20fe9f1d240 MpSigStub.exe      3752   6216 0x0000000027a76002 2023-02-15 16:22:37 UTC+0000                                 
0x0000a20fea04a080 AM_Delta_Patch     6216   5924 0x00000000180ce002 2023-02-15 16:22:36 UTC+0000  
```
5796 PID'sinde OUTLOOK uygulamasını buluyoruz. Maillerde genellikle bulunan "From:" kalıbını 5796 PID'si içerisinde aratıyoruz.
```
┌──(root㉿kali)-[/home/kali/Scripts/volatility]
└─# python2 vol.py -f /home/kali/Desktop/WANNA/Wanna-MEM.vmem --profile=Win10x64_19041 yarascan --pid=5796 -Y "From:"
Volatility Foundation Volatility Framework 2.6.1
Rule: r1
Owner: Process OUTLOOK.EXE Pid 5796
0x0d1016d5  46 72 6f 6d 3a 20 48 52 20 3c 68 72 40 6d 6d 30   From:.HR.<hr@mm0
0x0d1016e5  78 2e 6c 61 62 3e 0d 0a 53 75 62 6a 65 63 74 3a   x.lab>..Subject:
0x0d1016f5  20 46 72 65 65 20 57 6f 72 6b 73 68 6f 70 20 46   .Free.Workshop.F
0x0d101705  6f 72 20 6f 75 72 20 65 6d 70 6c 6f 79 65 65 73   or.our.employees
0x0d101715  0d 0a 0d 0a 17 10 0d 01 00 00 00 00 00 00 00 64   ...............d
0x0d101725  00 db 0d 54 d0 78 5d 99 3a 1b 00 f8 4d 37 13 58   ...T.x].:...M7.X
0x0d101735  9e 5b 0b 44 17 10 0d 01 00 00 00 38 0d 3b 19 86   .[.D.......8.;..
0x0d101745  03 02 00 00 00 00 00 c0 00 00 00 00 00 00 46 2c   ..............F,
0x0d101755  80 00 00 64 17 10 0d 01 00 00 00 38 91 18 13 86   ...d.......8....
0x0d101765  03 02 00 00 00 00 00 c0 00 00 00 00 00 00 46 3b   ..............F;
0x0d101775  80 00 00 84 17 10 0d 01 00 00 00 b0 f6 0c 0d 86   ................
0x0d101785  03 02 00 00 00 00 00 c0 00 00 00 00 00 00 46 0a   ..............F.
0x0d101795  80 00 00 5b d4 71 5f de 3a 1b 08 a0 97 07 0d 98   ...[.q_.:.......
0x0d1017a5  da 0f 0d 0d 00 00 00 c0 d0 e0 f0 e6 56 63 bf cb   ............Vc..
0x0d1017b5  00 00 00 bc 17 10 0d ff ff ff ff ff ff ff ff ff   ................
0x0d1017c5  ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff   ................
```
İlk cevabımız: hr@mm0x.lab

2. sorunun cevabını alabilmek için, FTK Imager ile user.ad1 dosyasını açıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219972599-218cc212-59b6-4c76-adc9-96c647e60a7d.png)

![image](https://user-images.githubusercontent.com/88983987/219972610-380968ff-eb35-414c-90ab-cc2fb81e8378.png)

![image](https://user-images.githubusercontent.com/88983987/219972620-01869019-9b3a-4cfb-b422-e08c23444333.png)

Atamer kullanıcısının masaüstü dizinine gittiğimizde dropper olan "doc" dosyası ve ransomware notu ile karşılaşıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219972863-6507a7b9-3844-4aa8-b5ec-1bb7297218dc.png)

Export edip sha256 değerini alıyoruz.
```
┌──(root㉿kali)-[/home/kali/Scripts/volatility]
└─# sha256sum /home/kali/Desktop/RegistrationFormTemp.doc 
12913f9984b8b5a940ef114579b831c0f361feb5f5618ccea11f5cb166a08c47  /home/kali/Desktop/RegistrationFormTemp.doc
```

## Flag
0xL4ugh{hr@mm0x.lab_12913f9984b8b5a940ef114579b831c0f361feb5f5618ccea11f5cb166a08c47}

# Wanna 3 [329 pts]

**Category:** Forensics
**Solves:** 15

## Description
>Q5: What is the IP and the port that the attacker used to deliver the malware?
Q6: What is the pid of the 3 malicious process (Numerical order) ?

Files: Same as Wanna 1

Flag Format: 0xL4ugh{IP:Port_pid1_pid2_pid3}

Author:MMOX

## Solution

İlk soru için dropper olan doc dosyamızı online malware analiz araçlarına sokmamız yetiyor.

Dosyayı VirusTotal'e yükledim, Comments kısmında otomatik olarak tarayan malware analiz araçlarının yorumları ile karşılaştım. Inquest Labs sitesinin oluşturduğu linke girdim ve aşağı indim.

https://labs.inquest.net/dfi/hash/12913f9984b8b5a940ef114579b831c0f361feb5f5618ccea11f5cb166a08c47

![image](https://user-images.githubusercontent.com/88983987/219973033-eee19a37-7015-4243-bbce-44aa4591aced.png)

Ayrıca Thunder.exe process'inin suspect olduğunu aklımızda tutuyoruz.

İlk sorunun cevabı: 192.168.30.50:8585

2. sorunun cevabı için processleri inceliyoruz.
```
┌──(root㉿kali)-[/home/kali/Scripts/volatility]
└─# python2 vol.py -f /home/kali/Desktop/WANNA/Wanna-MEM.vmem --profile=Win10x64_19041 pstree
Volatility Foundation Volatility Framework 2.6.1
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xffffa20fe6652080:wininit.exe                       528    420      1      0 2023-02-15 13:48:16 UTC+0000
. 0xffffa20fe664b080:services.exe                     668    528      7      0 2023-02-15 13:48:17 UTC+0000
.. 0xffffa20fe710c2c0:svchost.exe                    1032    668      3      0 2023-02-15 13:48:18 UTC+0000
.. 0xffffa20fe7733080:svchost.exe                    3104    668     26      0 2023-02-15 13:48:25 UTC+0000
.. 0xffffa20fe70f2240:svchost.exe                     552    668     66      0 2023-02-15 13:48:18 UTC+0000
... 0xffffa20fe8061080:sihost.exe                    1084    552     10      0 2023-02-15 13:50:54 UTC+0000
... 0xffffa20fe9189080:wuauclt.exe                   5924    552      7      0 2023-02-15 16:22:36 UTC+0000
.... 0xffffa20fea04a080:AM_Delta_Patch               6216   5924      3      0 2023-02-15 16:22:36 UTC+0000
..... 0xffffa20fe9f1d240:MpSigStub.exe               3752   6216      4      0 2023-02-15 16:22:37 UTC+0000
... 0xffffa20fe804e300:taskhostw.exe                 3920    552      8      0 2023-02-15 13:50:54 UTC+0000
.. 0xffffa20fe76b4300:MsMpEng.exe                    2568    668     32      0 2023-02-15 13:48:21 UTC+0000
... 0xffffa20fe919d080:MpCmdRun.exe                  7032   2568      9      0 2023-02-15 16:21:21 UTC+0000
.... 0xffffa20fe8851080:conhost.exe                  6976   7032      5      0 2023-02-15 16:21:21 UTC+0000
.. 0xffffa20fe78102c0:svchost.exe                    2612    668     13      0 2023-02-15 13:48:21 UTC+0000
.. 0xffffa20fe7760080:svchost.exe                    1100    668      4      0 2023-02-15 13:48:25 UTC+0000
.. 0xffffa20fe768e0c0:VGAuthService.                 2492    668      2      0 2023-02-15 13:48:21 UTC+0000
.. 0xffffa20fe2b27080:SearchIndexer.                 2144    668     17      0 2023-02-15 13:50:25 UTC+0000
... 0xffffa20fe923b080:SearchProtocol                5224   2144      6      0 2023-02-15 16:21:13 UTC+0000
... 0xffffa20fe4f30080:SearchProtocol                4216   2144     19      0 2023-02-15 16:20:56 UTC+0000
... 0xffffa20fe8a852c0:SearchProtocol                6036   2144      7      0 2023-02-15 16:21:15 UTC+0000
.. 0xffffa20fe7136240:svchost.exe                    1128    668     19      0 2023-02-15 13:48:18 UTC+0000
... 0xffffa20fe7b57280:dasHost.exe                   3196   1128      5      0 2023-02-15 13:48:25 UTC+0000
... 0xffffa20fe81ae280:ctfmon.exe                    3496   1128     10      0 2023-02-15 13:50:54 UTC+0000
.. 0xffffa20fe75aa340:spoolsv.exe                    2200    668     12      0 2023-02-15 13:48:20 UTC+0000
.. 0xffffa20fe2b55080:NisSrv.exe                     3268    668     12      0 2023-02-15 13:48:35 UTC+0000
.. 0xffffa20fe9221080:svchost.exe                    6768    668      8      0 2023-02-15 16:22:25 UTC+0000
.. 0xffffa20fe47782c0:svchost.exe                     704    668     14      0 2023-02-15 13:48:18 UTC+0000
.. 0xffffa20fe80a3080:svchost.exe                    1144    668      9      0 2023-02-15 13:50:54 UTC+0000
.. 0xffffa20fe71162c0:svchost.exe                    1064    668      9      0 2023-02-15 13:48:18 UTC+0000
.. 0xffffa20fe71c02c0:svchost.exe                    1248    668     23      0 2023-02-15 13:48:18 UTC+0000
.. 0xffffa20fe8c52240:SecurityHealth                 5348    668      8      0 2023-02-15 13:51:17 UTC+0000
.. 0xffffa20fe75ac240:svchost.exe                    2172    668      9      0 2023-02-15 13:48:20 UTC+0000
.. 0xffffa20fe47752c0:svchost.exe                     748    668     16      0 2023-02-15 13:48:18 UTC+0000
.. 0xffffa20fe7489080:svchost.exe                    1792    668      7      0 2023-02-15 13:48:20 UTC+0000
.. 0xffffa20fe6736240:svchost.exe                     788    668     20      0 2023-02-15 13:48:17 UTC+0000
... 0xffffa20fe2adc080:RuntimeBroker.                4196    788      2      0 2023-02-15 13:53:08 UTC+0000
... 0xffffa20fe70c8080:StartMenuExper                4720    788      8      0 2023-02-15 13:51:01 UTC+0000
... 0xffffa20fe7285080:backgroundTask                3716    788      7      0 2023-02-15 16:22:58 UTC+0000
... 0xffffa20fe755a080:ShellExperienc                5280    788     11      0 2023-02-15 13:53:07 UTC+0000
... 0xffffa20fe8da6300:RuntimeBroker.                1708    788      1      0 2023-02-15 13:51:51 UTC+0000
... 0xffffa20fe8aaa300:RuntimeBroker.                4792    788      3      0 2023-02-15 13:51:02 UTC+0000
... 0xffffa20fe80912c0:ApplicationFra                5332    788      4      0 2023-02-15 13:53:41 UTC+0000
... 0xffffa20fe8ccb2c0:dllhost.exe                   4820    788      4      0 2023-02-15 13:54:23 UTC+0000
... 0xffffa20fe9af2080:WmiPrvSE.exe                  3412    788     10      0 2023-02-15 16:22:30 UTC+0000
... 0xffffa20fe79ca280:WmiPrvSE.exe                  2876    788     10      0 2023-02-15 13:48:22 UTC+0000
... 0xffffa20fe8b4d080:SearchApp.exe                 4924    788     28      0 2023-02-15 13:51:03 UTC+0000
... 0xffffa20fe7e4f080:PhoneExperienc                6008    788     13      0 2023-02-15 13:51:27 UTC+0000
... 0xffffa20fe8c46080:smartscreen.ex                5272    788      5      0 2023-02-15 13:51:16 UTC+0000
... 0xffffa20fe94020c0:TextInputHost.                1448    788     10      0 2023-02-15 13:53:22 UTC+0000
... 0xffffa20fe8c47300:RuntimeBroker.                5180    788      3      0 2023-02-15 13:51:13 UTC+0000
... 0xffffa20fe8b67300:RuntimeBroker.                5052    788      9      0 2023-02-15 13:51:04 UTC+0000
... 0xffffa20fe7d980c0:WmiPrvSE.exe                  3528    788      7      0 2023-02-15 13:48:42 UTC+0000
... 0xffffa20fe8c312c0:dllhost.exe                    988    788      7      0 2023-02-15 13:53:24 UTC+0000
.. 0xffffa20fe7df6340:SgrmBroker.exe                 1304    668      7      0 2023-02-15 13:50:24 UTC+0000
.. 0xffffa20fe755b2c0:svchost.exe                    2608    668      7      0 2023-02-15 13:50:25 UTC+0000
.. 0xffffa20fe7e522c0:svchost.exe                    3900    668     11      0 2023-02-15 13:48:55 UTC+0000
.. 0xffffa20fe7bd1280:msdtc.exe                      3404    668     11      0 2023-02-15 13:48:26 UTC+0000
.. 0xffffa20fe76362c0:svchost.exe                    2384    668     15      0 2023-02-15 13:48:21 UTC+0000
.. 0xffffa20fe8888300:svchost.exe                    4452    668      6      0 2023-02-15 13:50:58 UTC+0000
.. 0xffffa20fe73c72c0:svchost.exe                    1920    668     11      0 2023-02-15 13:48:19 UTC+0000
.. 0xffffa20fe679b2c0:svchost.exe                     912    668     13      0 2023-02-15 13:48:17 UTC+0000
.. 0xffffa20fe74882c0:svchost.exe                     436    668      6      0 2023-02-15 13:48:20 UTC+0000
.. 0xffffa20fe7735280:dllhost.exe                    3000    668     12      0 2023-02-15 13:48:23 UTC+0000
.. 0xffffa20fe477e2c0:svchost.exe                    1012    668     30      0 2023-02-15 13:48:18 UTC+0000
.. 0xffffa20fe769b080:vm3dservice.ex                 2500    668      2      0 2023-02-15 13:48:21 UTC+0000
... 0xffffa20fe78a5200:vm3dservice.ex                2680   2500      2      0 2023-02-15 13:48:21 UTC+0000
.. 0xffffa20fe7267080:svchost.exe                    1496    668     13      0 2023-02-15 13:48:18 UTC+0000
.. 0xffffa20fe769d300:vmtoolsd.exe                   2536    668     13      0 2023-02-15 13:48:21 UTC+0000
.. 0xffffa20fe743d2c0:svchost.exe                    2036    668     11      0 2023-02-15 13:48:20 UTC+0000
... 0xffffa20fe9346080:audiodg.exe                   4864   2036      8      0 2023-02-15 16:22:20 UTC+0000
. 0xffffa20fe66c2080:lsass.exe                        692    528      9      0 2023-02-15 13:48:17 UTC+0000
. 0xffffa20fe673a180:fontdrvhost.ex                   812    528      5      0 2023-02-15 13:48:17 UTC+0000
 0xffffa20fe4ff0140:csrss.exe                         444    420     10      0 2023-02-15 13:48:16 UTC+0000
 0xffffa20fe2a7e080:System                              4      0    150      0 2023-02-15 13:48:14 UTC+0000
. 0xffffa20fe2abc080:Registry                          92      4      4      0 2023-02-15 13:48:07 UTC+0000
. 0xffffa20fe2b5a040:MemCompression                  1800      4     26      0 2023-02-15 13:48:19 UTC+0000
. 0xffffa20fe4ad1040:smss.exe                         328      4      2      0 2023-02-15 13:48:14 UTC+0000
 0xffffa20fe6659080:csrss.exe                         548    520     12      0 2023-02-15 13:48:16 UTC+0000
 0xffffa20fe669f080:winlogon.exe                      620    520      5      0 2023-02-15 13:48:16 UTC+0000
. 0xffffa20fe8230340:userinit.exe                    1072    620      0 ------ 2023-02-15 13:50:55 UTC+0000
.. 0xffffa20fe8235340:explorer.exe                   2324   1072     79      0 2023-02-15 13:50:55 UTC+0000
... 0xffffa20fe92570c0:WINWORD.EXE                   2064   2324     14      0 2023-02-15 13:52:40 UTC+0000
.... 0xffffa20fe85472c0:Thunder.exe                  4296   2064      9      0 2023-02-15 16:21:14 UTC+0000
..... 0xffffa20fea057240:@WanaDecryptor              4240   4296      6      0 2023-02-15 16:22:16 UTC+0000
..... 0xffffa20fe8d5b300:@WanaDecryptor              3780   4296      2      0 2023-02-15 16:22:03 UTC+0000
...... 0xffffa20fe9216080:taskhsvc.exe               6916   3780      9      0 2023-02-15 16:22:09 UTC+0000
....... 0xffffa20fe9225080:conhost.exe               5904   6916      4      0 2023-02-15 16:22:09 UTC+0000
... 0xffffa20fe8d7d080:OUTLOOK.EXE                   5796   2324     25      0 2023-02-15 16:20:45 UTC+0000
... 0xffffa20fe91ae080:vmtoolsd.exe                  5424   2324     10      0 2023-02-15 13:51:17 UTC+0000
... 0xffffa20fe8c4a240:SecurityHealth                5316   2324      1      0 2023-02-15 13:51:16 UTC+0000
. 0xffffa20fe673b080:fontdrvhost.ex                   820    620      5      0 2023-02-15 13:48:17 UTC+0000
. 0xffffa20fe70d10c0:dwm.exe                         1016    620     15      0 2023-02-15 13:48:18 UTC+0000
 0xffffa20fe8d89340:OneDrive.exe                     3852   5860     24      0 2023-02-15 13:52:17 UTC+0000
 0xffffa20fe92ce080:MpCmdRun.exe                     5920   3756      7      0 2023-02-15 16:21:20 UTC+0000
```

Thunder.exe zaten şüpheliydi, 2 adet @WanaDecryptor adlı WannaCry Decryptor process'imiz var. Kendisi fidye istemesi ile meşhurdur.
2. sorunun cevabı: 3780,4240,4296
## Flag
0xL4ugh{192.168.30.50:8585_3780_4240_4296}

