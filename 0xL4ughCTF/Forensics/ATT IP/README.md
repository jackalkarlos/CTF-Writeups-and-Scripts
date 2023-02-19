# ATT IP [50 pts]

**Category:** Forensics
**Solves:** 151

## Description
>This is a trojan , Can u identify the C2 server IP  and the port?

Flag format:  0xL4ugh{IP_PORT}

Author: MMOX

#### Hint 

## Solution
Bizden "pcap" dosyasından C2 sunucusunun adresini bulmamız isteniyor. Paylaşılan "AttIP" dosyasını Wireshark üzerinden açıp TCP iletişimini incelemeye başlıyoruz.

"tcp.stream eq 2"

2. TCP Stream'inde cihazın C2 sunucusuna TCP üzerinden veri gönderdiği anlaşılıyor.

![image](https://user-images.githubusercontent.com/88983987/219961663-5035a75c-a02b-4045-a8b3-c4cd1205e5b0.png)

## Flag
0xL4ugh{91.243.59.76_23927}

