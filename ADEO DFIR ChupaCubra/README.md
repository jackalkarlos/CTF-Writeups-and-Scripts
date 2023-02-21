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

2. Çözüm:

