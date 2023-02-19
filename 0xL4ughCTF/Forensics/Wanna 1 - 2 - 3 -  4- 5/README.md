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

Not: Windows 10 ve üzeri imajlarda volatility'i güncel tutmak çok önemli, yeni profiller eklendiğinde volatility'in imageinfo komutu başarısız olabilir.

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

