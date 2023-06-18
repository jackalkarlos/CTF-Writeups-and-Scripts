# CTF’e erişmek için URL: <a href="http://www.ibrahimbaloglu.com/2021/10/windows-forensics-challange.html"> Challenge </a>

# Ad Soyad ve E-posta adresimizi kaydettikten sonra ilk soruya geçebiliriz.

# 1. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/b5cc0578-f50f-4556-a1e9-f86642d184bd)

## Solution
1. soruda bizden indirdiğimiz imaj dosyasının Hash değerini istemekte. Hash değerine ulaşmak ve diğer incelemelerimizi yapabilmek için, imaj dosyasını FTK Imager üzerinde açmamız gerekmekte.

FTK Imager programını açtıktan sonra, sol üstteki "File" menüsünden "Add Evidence Item" seçeneğini seçiyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/28b39c07-3fc9-4263-8e97-998ec6ec3581)

Çıkan ekrandan "Image File" seçeneğini seçip, "Sonraki" butonuna basıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/faf028d4-81cc-42ed-9937-1eaf51c06dbe)

"Browse" butonuna tıklayıp, imajın yer aldığı konumu seçiyoruz. "Finish" butonuna tıklıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/1de7945b-2b88-4329-89cf-fe213b0ae66a)

Hash değerlerine aşağıdaki "Properties" menüsü altında erişebiliyoruz. MD5 Hash değerimizi alıyoruz.

```
MD5 Hash değerimiz: 4367a88268faa047989fe50f286ec3ba
```

# 2. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/6d246bb7-5a51-4f8f-a49b-b9460b2604bd)

## Solution

2. soruda "Kurulu işletim sisteminin adı ve sürümü" isteniyor. Bu veriler SOFTWARE adlı registry kayıtlarında tutulmaktadır.

SOFTWARE dosyasını almak için, FTK Imager üzerinden "C:\Windows\system32\config" konumuna gitmemiz gerekmekte. Bunun için sol üst tarafta bulunan "Evidence Tree" menüsünden "config" klasörüne ilerlememiz gerekiyor.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/7b342184-5dcf-4565-9582-48fe8f4c0f4e)

```Windows_10_Forensic_Image.e01 > Basic data partition (3) > root > Windows > System32 > config```

Ulaştıktan sonra, SOFTWARE ve SOFTWARE.LOG1, SOFTWARE.LOG2 dosyalarını export ediyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/3d2ea24b-ab36-4ab0-88e3-db4d6efd930d)

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/7e994b1d-36e9-4172-b595-64eba4d22804)

Export ettiğimiz dosyaları incelemek için "Registry Explorer" programını açıyoruz. "File" menüsünden "Load Hive" seçeneğini seçiyoruz. "SOFTWARE" dosyasını açıyoruz. 

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/06d84cfb-9be7-49e9-b39c-25d81f3f337d)

Uyarı gelirse sırasıyla "NO", sonra da "YES" onayını veriyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/5dcaaa86-0366-4a74-b5ca-2840ccf117d5)

Üstteki menüden "Available bookmarks" seçeneğine geliyoruz. "Key Name" altında "CurrentVersion" seçeneklerini kurcaladığımızda, sistemin Windows 10 Pro 2004 sürümü olduğunu görüyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/526809fc-278b-4b14-9932-942e7c1eaee7)

```Cevap: Windows 10 Pro 2004```

# 3. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/6d3b2021-4fe0-4aa6-817f-0e898cd3e032)

## Solution
3. soruda, 2. CurrentVersion seçeneğine geliyoruz. En altta InstallTime seçeneğine geliyoruz. Data kısmındaki veriye tıklıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/409f6881-ac06-494b-885e-99f8cbb9090a)

"Binary viewer" seçeneğine tıklıyoruz. Sağ alttan "Data interpreter" seçeneğine geliyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/f64ec9ae-e5a4-40e2-bcf1-c6ecc792d730)

Windows FILETIME (64 bit) yazısının yanında işletim sisteminin kurulum tarihine erişmiş oluyoruz. 

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/3fc3a9d7-3130-468c-b4b9-f93cd73ae0c0)

```Cevap: 2021-02-22 13:41:03```

# 4. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/ceb9916d-73fc-496b-a9a1-70201724d5ad)

## Solution
4. soruda FTK Imager ile aynı lokasyondan ("C:\Windows\system32\config") SYSTEM dosyasını alıyoruz. Registry Explorer ile SYSTEM dosyasını aynı şekilde açıyoruz. 

Interfaces klasörü altındaki kayıtları birazcık kurcaladıktan sonra, bulduğumuz değerlerin bir tanesinde cihazın aldığı son IP Adresine erişim sağlıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/5aeef06e-76e5-4e09-9ffe-a57ef99a78c6)

```Cevap: 192.168.52.131```

# 5. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/6ddd0f0f-628d-4fc0-94e6-613c2d2f037d)

## Solution

5. soruda FTK Imager ile aynı lokasyondan ("C:\Windows\system32\config") SAM dosyasını alıyoruz. Registry Explorer ile SAM dosyasını aynı şekilde açıyoruz.
"Users" klasörüne erişim sağlıyoruz, sağ taraftaki "User Accounts" menüsünde tüm kullanıcıların isimleri ve toplam giriş sayıları yazmakta. "Total Login Count" sütunu altında, giriş yapılan tek hesabın "ibaloglu" hesabı olduğunu ve toplamda 5 kez giriş yapıldığını öğreniyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/b20ac722-86ca-491e-ae82-76cd70fbc07d)

```Cevabımız "ibaloglu"```

# 6. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/9b4643af-81bf-4b11-ae21-f77fc420b2d1)

## Solution

6. soruda "FTP bağlantısı yapılan sunucunun IP adresi ve kullanıcısı isteniyor. İpucumuz ise "Filezilla".
Bunun için sunucu kayıtlarının tutulduğu dosyayı bulmamız gerekiyor. Lokasyonu: "C:/Users/ibaloglu/AppData/Roaming/FileZilla"

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/2436f53c-b4b4-4b81-880c-23fce8c4562d)

"recentservers.xml" adlı dosyaya tıkladığımızda, export etmemize gerek kalmadan önizlemesi gösteriliyor.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/ae894b6d-5271-4586-82b9-2dd326b8b237)

```Sunucunun "192.168.23.23:21" ve kullanıcı adının "ibaloglu" olduğunu görüyoruz.```

# 7. Soru ve 7.*

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/33c41c2b-93c9-41e1-9058-9c0a8e425bba)

## Solution

7. soruda bizden sistemde çalıştırılmış bir ağ tarama aracı olup olmadığını sormakta.
Sistem üzerinde son çalıştırılan programları listelemek için NTUSER.dat dosyasını VEYA Prefetch kayıtlarını incelemeye ihtiyacımız var. NTUSER.dat dosyasını almak için "C:/Users/ibaloglu" klasörüne gidiyoruz. Diğer dosyalarda yaptığımız gibi NTUSER.dat ve onun ismine benzerlik gösteren tüm dosyaları bir klasöre kaydediyoruz. 
Registry Explorer ile kaydettiğimiz dosyayı açtıktan sonra, "SOFTWARE" klasörü altında "NMAP" adlı bir programın kaydını görüyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/1f52501b-4816-4ae1-ad0e-f776ba3be585)

```Cevap: Evet, NMAP```

7.1. soruda bizden tarama aracının adını ve versiyonunu istemekte. Programın ismini zaten biliyoruz, 7. soruda aldığımız konum bilgisi ile programın kurulu olduğu yere gidiyoruz. (C:\Program Files (x86)\Nmap) Lokasyondaki "scan_log_nmap.xml" dosyasını kaydedip, sevdiğimiz bir text editörü ile açıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/7dc6b7bb-6c79-4f27-9788-b497ccb419a9)

<b>Yazıyı incelediğimizde versiyonun 7.92 olduğuna dair bir ibare görüyoruz. </b>

```Cevap: NMAP, 7.92```

7.2. soruda bizden taramanın başlangıç tarihini sormakta. Aynı dosya içerisinde "startstr" ile başlayan metinde başlangıç tarihini ve saatini görüntüleyebiliyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/253b8302-10c0-49f9-86dc-ee289afd7b84)

```Cevap: Tue Sep 21 16:24:36 2021```

7.3 soruda bizden tarama aracında kullanılan parameterleri sormakta. Aynı dosya içerisinde "args" ile başlayan metinde saldırganın girdiği komutu görebiliyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/7d887bab-fd3e-4ba4-b517-4f996996b990)

```Cevap: nmap -T4 -F 192.168.52.134```

7.4. soruda bizden tarama sonucunda açık olarak tespit edilen portları sormakta. Sonuçları hatasız olarak almak için elimle dosyayı birazcık düzeltiyorum. Düzelttiğim dosyayı incelediğimde, 5 tane açık port olduğunu görüyorum. 

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/6d9a7e39-1b02-4172-8146-76f765d9f4a7)

```Cevap: 135, 139, 445, 3389, 5357```

7.5. soruda bizden taratılan IP'ye ait MAC adresini istiyor. Aynı dosya içerisinde, port sonuçlarının altında MAC adresini görüntüleyebiliyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/fad503cd-04fe-47bb-841f-c6764b7b0652)

```Cevap: 00:0C:29:CD:D2:68```

# 8. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/b6f91838-1b49-4cee-9e09-e37b2be3b0c2)

## Solution
8. soruda bizden bilgisayara takılan USB Depolama Aygıtının takılma tarihini istemekte. 
Registry Explorer üstünde daha önce açtığımız SYSTEM dosyasına gidiyoruz. Registry hives menüsüne dönüyoruz. Sırasıyla 
ROOT > ControlSet001 > Enum > USBSTOR > Disk&Ven_SanDisk&Prod_Cruzer_Blade&Rev_1.00 > 4C530001220905112112&0 > Properties >  {83da6326-97a6-4088-9453-a1923f573b29} > 0064 klasörüne gidiyoruz. Sağ tarafta USB cihazının ilk takıldığı tarih gözükmekte.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/857c2074-fffc-43c3-9136-ac09956e44fc)

```Cevap: 2021-09-21 13:49:08```

# 9. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/57f4ee66-99dd-4360-a9d9-b74a817b43fd)

## Solution
9. soruda bizden bilgisayara takılan USB Depolama Aygıtının çıkartılma tarihini istemekte.
Registry Explorer üstünde daha önce açtığımız SYSTEM dosyasına gidiyoruz. Registry hives menüsüne dönüyoruz. Sırasıyla
ROOT > ControlSet001 > Enum > USBSTOR > Disk&Ven_SanDisk&Prod_Cruzer_Blade&Rev_1.00 > 4C530001220905112112&0 > Properties > {83da6326-97a6-4088-9453-a1923f573b29} > 0067 klasörüne gidiyoruz. Sağ tarafta USB cihazının ilk takıldığı tarih gözükmekte.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/9aef3ba3-79bd-4f84-be53-414582b9eb81)

```Cevap: 2021-09-21 13:51:52```

# 10. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/19473395-f3bc-48a9-95f0-ed221e944473)

## Solution
10. soruda bizden bilgisayara takılan USB Depolama Aygıtının seri numarasını istemekte. ROOT > ControlSet001 > Enum > USBSTOR > Disk&Ven_SanDisk&Prod_Cruzer_Blade&Rev_1.00 > 4C530001220905112112&0 dizinindeki "4C530001220905112112&0" USB aygıtının seri numarasını temsil etmekte. 

```Cevap: 4C530001220905112112&0```

# 11. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/2afe8a75-bc6d-46b2-8413-6af9dc66c313)

## Solution
11. soruda bizden "Kullanıcı parolalarını elde etmek için kullanılan zararlı yazılımın çalıştırılma tarihi" isteniyor. Windowsta yaygın olarak tanınan ve kullanıcı parolalarını çalmak amacıyla kullanılan ünlü bir yazılım var. Aradığımız yazılımın MimikAtz olduğunu varsayarak, Prefetch kayıtlarını inceliyoruz.

FTK Imager yardımı ile "C:/Windows/Prefetch" klasörünü export ediyoruz. Daha sonra "WinPrefetchView" programını çalıştırıyoruz. Options > Advanced Options seçeneğine girip, Prefetch Folder seçeneğine kaydettiğimiz klasörü gösteriyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/f3815770-d421-4ddf-b141-93d1bb3b9be4)

Daha sonra karşımıza çıkan listede ufak bir göz gezdiriyoruz. Gözümüze ismi değişik gelen, yanlış yazılmış, benzer yazılmış program isimlerine bakıyoruz. Bahsettiğim MimikAtz yazılımının listede olduğunu farkediyoruz. Çift tıklayıp detaylarına girdikten sonra, "Last Run Time" seçeneği altında cevaba erişiyoruz. Bir dahaki işlemlerde ihtiyacımız olacağı için WinPrefetchView'i kapatmıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/c3715bd7-53d3-46b2-a53d-b5298c750d31)

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/18cdeefa-5eb5-47ac-a217-20dd75950d13)

```Cevap: 21.09.2021 17:14:21, 21.09.2021 16:59:40```

# 12. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/70f08649-04fb-4854-88b0-f835eb245183)

## Solution
12. soruda bizden Mimikatz ile hangi aktif kullanıcıların parola bilgilerinin elde edildiğini istiyor. WinPrefetchView ile Mimikatz'ın olduğu konumu öğreniyoruz.
"C:/Users/ibaloglu/Downloads/mimikatz_trunk/x64"

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/585552e3-dd4d-4bea-9d27-4519ec77fe89)

FTK Imager yardımı ile Mimikatz'ın olduğu konuma gidiyoruz. Konumda "mimikatz_output.txt" adlı bir text dosyası ile karşılaşıyoruz. İncelediğimizde ibaloglu adlı kullanıcının NTLM ve SHA1 değerinin çalınmış olduğunu görüyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/25865f35-3f55-49f4-82d0-db33d86c1f4e)

```Cevap: ibaloglu```

# 13. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/e7e84231-8079-4d58-92d4-87b19a7dbacd)

## Solution
13. soruda bizden çalınan parolanın text halini istiyor. "https://crackstation.net/" adresine gidip, NTLM ve SHA1 değerini alt alta yazıyoruz. Captcha onaylamasını yaptıktan sonra, "Crack Hashes" butonuna basıyoruz. NTLM için "Password1" sonucunu çıkarıyor.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/916ca329-47e0-4ffb-990c-506413e8a3ef)

```Cevap: Password1```

# 14. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/1fe7e302-d43d-4845-9137-9bebefbb08dc)

## Solution

14. soruda bizden sistemdeki Prefetch sayısını istiyor. WinPrefetchView programında sol alt kısma bakıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/d8642167-d02a-4ab8-9e9d-ab0b3fae1406)

```Cevap: 167```

# 15. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/7d0140cc-d8ee-4ebb-8190-2d8f579c3635)

## Solution
15. soruda bizden paylaşıma açılmış dosyaları istiyor. SYSTEM dosyasını Registry Explorer ile açıyoruz. Available Bookmarks altından "Shares" klasörüne giriyoruz. Sağ tarafta paylaşıma açılmış dosyalar yazıyor.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/650bbbf0-63b7-45ff-afe5-f93533a67a77)

```Cevap: Temp ve Users```

# 16. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/e5495592-6ec2-4017-b2af-dcf753bc7ebc)

## Solution
16. soruda bizden paylaşıma açılmış klasörlerin içerisinde yer alan txt çıktısında yazan, aktif bağlantı kurulan IP adresi ve Yerel Bağlantı Portu istenmekte. Users klasörüne gittiğimizde içerisinde herhangi bir txt dosyası olmadığını görüyoruz. "C:/Users/ibaloglu/Appdata/Local/Temp" klasörüne gidiyoruz. 

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/b04dc1d7-9f8c-47f7-9f90-3a6c6eeeeeff)

"network_connection_ib.txt" adlı bir dosyaya rastlıyoruz. İçeriğini incelediğimizde bir takım bağlantı logları olduğunu görüyoruz. Txt dosyasında görüldüğü üzere 445 portundan, 192.168.52.134 adresine bağlantı sağlanmış.

```Cevap: 192.168.52.134, 445```

# 17. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/b69d21ad-146f-4b19-8b49-69eb1f6f7c24)

## Solution
17. soruda bizden 9/21/2021 tarihinde yapılmış uzak bağlantı işlemlerine dair tarih ve oturum açma tipi detaylarını istiyor. "C:/Windows/System32/winevt/Logs" dizini altından "Security.evtx" ve "Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx" dosyalarını export ediyoruz. EvtxExplorer programı ile aynı klasör içine kopyalıyoruz. Klasörün içerisinde terminali çalıştırıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/ecd4ccff-ea30-47ab-81bc-4cffb37475f8)

“EvtxECmd.exe -f “logfile” --csv “outputfolder” –-csvf security.csv” komutunda gerekli yerleri dolduruyoruz. Oluşan dosya içerisinde filtreleme yaparak devam ediyoruz. EventId sütunu altından "4624" filtrelemesi (başarılı giriş kodu) yapıyoruz. TimeCreated sütunu altından 09-21 araması yapıp çıkan sonuçlara filtre uyguluyoruz. Logon type kısmından "LogonType3" ve "LogonType 7" filtrelemesi uyguluyoruz. Thread kısmından küçükten büyüğe sıralama yapıyoruz ve kesin tarih-saatler elde ediyoruz. Çıkan sonuçları değerlendirmeye başlayabiliriz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/5733e9c3-5c3c-4fc0-a6a8-9b6f86b00a7a)


```Cevap: Oturum Açma Tipi 4624
Tarihler: 
2021-09-21 14:23:03.4899964
2021-09-21 16:12:06.6335956
2021-09-21 14:49:17.2927314
2021-09-21 14:23:00.6737119
(Salise farklar olan 1-2 kayıt var, onları atlayarak yazdım. Ana tarih ve dakikaları aldım.)
```

# 18. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/471d5b3a-132d-4bea-a1eb-e2f1ab1b8804)

## Solution
18. soruda oturum açılan makinenin IP adresini istemekte. Aynı tabloyu sağa kaydırarak IP Adresine erişim sağlıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/57b75c38-67c4-4ace-afdd-23368a30d586)

```Cevap: 192.168.52.134```

# 19. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/1e280b43-4dba-4e7d-a6f3-aa39f79fb35e)

## Solution 
19. soruda oturum açılırken kullanılan kullanıcı adını istemekte. PayloadData1 sütunu altında kullanıcı adını görüntülüyoruz. DESKTOP-69U8AFV domainine bağlı "ibaloglu" kullanıcısı.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/c3f73a19-5044-4f1d-9614-8b69d11b4938)

```Cevap: ibaloglu```

# 20. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/0ccfa7e5-6130-40f8-be0b-3c33157ffaf2)

## Solution

20. soruda "İnternet tarayıcısı üzerinden oturum açılan bir e-posta hizmeti var mı, Varsa; Oturum açan e-posta adresi nedir?" sorusu ile karşılaşıyoruz. Daha önce incelediğimiz Prefetch verilerine dayanaraktan makine sahibinin "Google Chrome" kullandığını düşünüyoruz. FTK Imager yardımı ile imaj içindeki Google Chrome geçmişinin depolandığı "C:\Users\ibaloglu\AppData\Local\Google\Chrome\User Data\Default" konumuna gidiyoruz. "History" dosyasını export ediyoruz.

Export ettiğimiz dosyayı SQLite yardımı ile açıyoruz. Veriyi görüntüle kısmına gelip, tablo kısmından "urls" seçeneğini seçiyoruz. Geçmişi inceleyerek aradığımız cevaplara ulaşıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/6beda165-b4bd-487e-9d42-23c48282ea87)

```Cevap: ProtonMail, Forensics_ibaloglu@protonmail.com```

# 21. Soru

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/44ba814a-efcb-40bd-bdfd-77a7cb711a5f)

## Solution
21. soruda bizden oturum açma tarihi ve saati isteniyor. SQLite üzerinden devam ediyoruz. "last_visit_time" sütunu, 7. satırdaki veriyi kopyalıyoruz. "13276709901254517"

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/dfe88ca0-0b6b-4048-8786-f7ef06a8c7ed)

İnternet üzerinden "Chrome Timestamp Converter" araması yapıp, ilk çıkan siteye giriyoruz. Çıkan kodu girip dönüştürüyoruz.
Hedef makinedeki Time-zone bizimkiyle aynı olduğu için direkt "Your time zone" kısmındaki sonucu alıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/31b13a35-8794-4aba-b052-bc46a2563478)

```Cevap: Salı, 21 Eylül 2021 17:58:21```

# 22, 23 ve 24. soru:

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/75210ebc-f4ca-4fe2-8084-cd61465cb284)

## Solution
Bu sorular için FTK Imager'den 2 dosya almamız gerekiyor.
```
"C:\$LOGFILE"
"C:\$Extend\$UsnJrnl\$J"
```
Bu dosyaları ayrı bir klasöre export ediyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/75210ebc-f4ca-4fe2-8084-cd61465cb284)

"NTFS Log Tracker" programını açtıktan sonra aktardığımız dosyaları seçiyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/39c56b4c-baa0-476f-b999-79041c27b46c)

"Parse" tuşuna bastıktan sonra, dosyaların kaydedileceği konum ve ismini seçiyoruz. Ardından "Start" butonuna basıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/b426f388-ecbe-49af-89f9-48f5d8960c8b)

İşlem bittikten sonra, "Export CSV" butonuna basıp dosyaların kaydedileceği klasörü seçiyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/cb877ff0-ea09-4d1a-ab8c-ac2b82812a32)

Oluşan "NLT_UsnJrnl_2021*" diye devam eden dosyayı Excel üzerinde açıyoruz. CTRL + F yaparak "OncekiAdimiBul" aratması yapıyoruz. Kayıtları incelediğimizde dosyanın eski adının "Windows_Forensic" olduğunu görüyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/b287aa1d-b599-4e37-bfdf-c44e3695ea90)

```22. Soru Cevap: Windows_ Forensic```

Aynı satırda değiştirilme tarihini görüyoruz.

23. Soru Cevap: 2021-09-21 18:06:58

24. soru için fazla bir çaba göstermeye gerek yok. FTK Imager ile makinenin masaüstü (Desktop) klasörüne gittiğimizde "OncekiAdimiBul" dosyasını görebiliyoruz.

24. Soru Cevap: Desktop

25. soruda bizden bir rar dosyasının şifresi isteniyor. Bunun için Brute-Force kullanacağız. Ben bunu linux ortamında yapmayı tercih ediyorum.

rar2john Flag.rar > output.txt
john output.txt --wordlist /usr/share/wordlists/rockyou.txt

Komutları ile BruteForce başlatıyoruz. İşlem biraz uzun sürebilir.

Cevap: infect

26. soruda Word dosyası içerisindeki Flag'i alıyoruz.

Cevap: Windows Forensic {Bu_benim_başarım}

27. soruda FTK Imager ile "C:\$Recycle.Bin\" içerisindeki "S-1-5-21-1302114328-2508369510-30667992-1000" SID numaralı klasörü export ediyoruz. 
$I Parser uygulamasını açıp kaydettiğimiz yeri ve yeni verilerin kaydedilmesini istediğimiz konumu seçip "Parse!" tuşuna basıyoruz.
İki dosya silindiğini ve isimlerinin "mimikatz.exe" ve "FileZilla_3.54.1_win64-setup.exe" olduğunu görüyoruz.

Cevap: FileZilla_3.54.1_win64-setup.exe ve mimikatz.exe

28. soruda cihazda "IMG_7294.JPG" adlı bir dosya olduğundan bahsediyor. Bu dosyayı bulduktan sonra 28, 29 ve 30. soruları cevaplayacağız. Bunun için ilk önce dosyanın konumunu ve kendisini bulmamız gerekiyor. Yine imdadımıza FTK Imager koşuyor. 

Bunun için 2 yöntemimiz var.
1- İmajı sisteme bağlayıp Windows'un arama özelliğini kullanmak:
İncelediğimiz imajın üstüne sağ tık ile tıklıyoruz, "Image Mounting" tıklıyoruz. Gelen menüde "Mount" tuşuna basıyoruz. Daha sonra bilgisayarım kısmında oluşan, dataların yer aldığı Yerel Disk'e erişim sağlıyoruz. Arama kısmından IMG_7294.JPG araması yapıyoruz. Konumu AppData\Local kısmında.
2- İmajın lokasyon bilgilerini çıkartmak:
Basic Data Partition (3)'ün üstüne sağ tık ile tıklıyoruz, Export Directory List butonunu seçiyoruz. Dosyayı kaydedeceğimiz konumu ve ismini seçip "Kaydet" butonuna basıyoruz. İşlemin tamamlanmasını bekliyoruz. Oluşan Excel dosyasında ufak bir aratma yaparak sonuca ulaşıyoruz. Tavsiye edilen yöntem genellikle budur. Bu yönteme alışmanızı şiddetle tavsiye ederim.

Konumu AppData\Local kısmında demiştik. Dosyayı kolaylıkla erişebileceğimiz bir yere export ediyoruz. İnternet üzerinden "https://exiftool.org/" adresinden işletim sistemimize uygun olan Exiftool versiyonunu indiriyoruz. İnen exe dosyasını export ettiğimiz fotoğraf ile aynı klasöre alıyoruz. Terminali klasörde çalıştırıyoruz ve "exiftool(-k).exe" IMG_7294.JPG.copy0 komutunu çalıştırıyoruz. 

Karşımıza çıkan detaylar fotoğraf dosyasının bilgilerini içeriyor. Telefon modelinin "iPhone SE (2nd generation)" olduğunu görüyoruz.

Cevap: iPhone SE (2nd generation) 

29. soruda aynı tabloda "Flash:" yazısının karşısında "Off, Did Not Fire" yazısını görüyoruz. Bu flaşın açık olmadığı anlamına geliyor.

Cevap: Flash Kapalı

30. soruda aynı tabloda Date/Time Original ve Create Date karşısında fotoğrafın orjinal oluşturulma tarihini ve saatini görüntüleyebiliyoruz.

Cevap: 2021:09:21 18:27:32

31. soruda daha önce yaptığımız gibi Registry Explorer yardımı ile SYSTEM dosyasını açıyoruz. Available Bookmarks menüsü altında ilk Windows klasörüne geliyoruz. Sağ tarafta ShutdownTime değerinin üstüne tıklıyoruz.
Sağ alttan Data Interpreter seçeneğini seçiyoruz. "Windows Filetime (64 bit)" karşısında aradığımız tarih ve saate rastlıyoruz.

Cevap: 2021-02-22 13:42:42

32. soruda, 28. soruda olduğu gibi imajı sisteme bağlıyoruz. "Autoruns" adlı forensic programını çalıştırıyoruz. Sol üstteki "File" seçeneğinin altından "Analyze Offline System" seçeneğini seçiyoruz.
Çıkan menüde sisteme bağladığımız imajın "Windows" klasörünü gösteriyoruz. Alttaki kısım otomatik olarak tamamlanıyor. "OK" tuşuna basıp devam ediyoruz. Kısa bir süre bekletiyor ve sonra inceleme işlemimize başlıyoruz.
Logon sekmesi altında otomatik çalıştırılan işlemlerin: "cmd.exe, vmtoolsd.exe, vm3dservice.exe, onedrivesetup.exe, chrmstp.exe" olduğunu ve diğer işlemlerin sistem dosyası olduğunu görüntülüyoruz.

Cevap: "cmd.exe, vmtoolsd.exe, vm3dservice.exe, onedrivesetup.exe, chrmstp.exe"
