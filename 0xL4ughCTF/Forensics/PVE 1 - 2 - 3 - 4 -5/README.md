# PVE 1 [150 pts]

**Category:** Forensics
**Solves:** 50

## Description
>An attacker attacked our server. we got a dump so can you investigate it for us?

Q1: What is the operating system and kernal version of the dump

Download: https://drive.google.com/file/d/1IV95rb5VH8K2PD27zN-K53HC8NNL8njE/view?usp=sharing

Flag format: 0xL4ugh{OsName_theFullKernalVersion}
Author: xElessaway

#### Hint 

## Solution

Bu seride imajı inceleyebilmemiz için bir volatility profili inşaa etmemiz gerekicek. Hem ilk soruyu cevaplayabilmek için, hem bu profili inşaa edebilmek için çalıştırmamız gereken bir komut var.

NOT: 4. soruya kadar hepsini sadece strings ve grep ile çözebilirsiniz fakat bu durumda 5. soruyu çözemeyeceksiniz, ayrıca bu beklenmeyen bir çözüm türüdür. CTF üzerindeyseniz strings ile çözebildiğinizi çözüp 5. soruya öyle başlayın, zaman bazında size puan kazandıracaktır. İlk önce nasıl bir profil inşaa edebileceğinizi anlatacağım, sonrasında soruları çözmeye başlayacağım. Örneğin ikinci soru normalde bash history ile alınıyor, ama grep "apache" ile de çekilebiliyor.
```

└─# strings PVE.vmem | grep -i --text "Linux " | head
*Linux UI
*Linux UI
*Linux UH
Linux 4.4.0-186-generic Ubuntu 16.04.7 LTS
if [ -e /proc/cmdline ]; then #linux only - future proofing against BSD and Hurd :)
linux|linux console
linux   H
Failed to load SELinux policy
SELinux policy denies access.
Linux version 4.4.0-186-generic (buildd@lcy01-amd64-002) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12) ) #216-Ubuntu SMP Wed Jul 1 05:34:05 UTC 2020 (Ubuntu 4.4.0-186.216-generic 4.4.228)
```


## Flag
0xL4ugh{Ubuntu_4.4.0-186-generic}
