# GetTheparts [50 pts]

**Category:** Forensics
**Solves:** 46

## Description
>what if we group the atmoics ? we get a cool shape


Author: MMOX

#### Hint 

## Solution
Verilen "EzPz.pcap" dosyasını WireShark ile açıyoruz. Her streamda TCP Payload içerisinde bir hex kodu ile karşılaşıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219962457-a8b4f7b8-131c-44bf-980d-c1b4b4408167.png)

TCP Payload içerisindeki verileri çıkartacak bir script yazıyoruz. 

NOT: Ekte paylaşılan script, python2 üzerinde çalışır.
```
from scapy.all import *

pcap = rdpcap("EzPz.pcap")

for pkt in pcap:
    if Raw in pkt:
        print pkt[Raw]
```

Verileri döngüyle aldığımız için alt alta yazılıyor, script içinde düzeltebiliriz ancak vakit kaybetmek istemedim. 

![image](https://user-images.githubusercontent.com/88983987/219962796-22afd2a7-ed4f-4bd7-9f52-e75798e23847.png)

CyberChef is your friend.

İlk satırı siliyoruz.

![image](https://user-images.githubusercontent.com/88983987/219962828-e4f589d0-8131-443f-9615-1cb5a87a1cce.png)

Altalta satırları yanyana boşlukla yazılacak şekilde ayarlıyoruz. Satır atlama kodu "\n".

![image](https://user-images.githubusercontent.com/88983987/219962866-c0d7dafd-0ed9-4062-9a38-cb9102661024.png)

Hex başlıklarından kurtuluyoruz. "0x" 

![image](https://user-images.githubusercontent.com/88983987/219962909-8540c2b8-d752-480e-921c-53a455dc1422.png)

Dosyayı hex'ten çevirdiğimizde PNG dosyası olduğunu farkediyoruz.

![image](https://user-images.githubusercontent.com/88983987/219962943-34207d32-ce86-4233-a5ef-28f3511879aa.png)

Render Image ile renderliyoruz.

![image](https://user-images.githubusercontent.com/88983987/219963003-1a2906b7-b585-4804-916b-2dc71991cc61.png)

CyberChef linki maalesef çok uzun olduğu için paylaşamıyorum, sorun yaşamanız durumunda bana Twitter üzerinden ulaşabilirsiniz.

## Flag

0xL4ugh{By735_3verywh3r3_WE3333}
