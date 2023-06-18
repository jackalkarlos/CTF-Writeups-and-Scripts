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

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/5aeef06e-76e5-4e09-9ffe-a57ef99a78c6)

Interfaces klasörü altındaki kayıtları birazcık kurcaladıktan sonra, bulduğumuz değerlerin bir tanesinde cihazın aldığı son IP Adresine erişim sağlıyoruz.

```Cevap: 192.168.52.131```

5. soruda FTK Imager ile aynı lokasyondan ("C:\Windows\system32\config") SAM dosyasını alıyoruz. Registry Explorer ile SAM dosyasını aynı şekilde açıyoruz.
"Users" klasörüne erişim sağlıyoruz, sağ taraftaki "User Accounts" menüsünde tüm kullanıcıların isimleri ve toplam giriş sayıları yazmakta. "Total Login Count" sütunu altında, giriş yapılan tek hesabın "ibaloglu" hesabı olduğunu ve toplamda 5 kez giriş yapıldığını öğreniyoruz.
Cevabımız "ibaloglu"

6. soruda "FTP bağlantısı yapılan sunucunun IP adresi ve kullanıcısı isteniyor. İpucumuz ise "Filezilla".
Bunun için sunucu kayıtlarının tutulduğu dosyayı bulmamız gerekiyor. Lokasyonu: "C:/Users/ibaloglu/AppData/Roaming/FileZilla"
"recentservers.xml" adlı dosyaya tıkladığımızda, export etmemize gerek kalmadan önizlemesi gösteriliyor.

Sunucunun "192.168.23.23:21" ve kullanıcı adının "ibaloglu" olduğunu görüyoruz.

7. soruda bizden sistemde çalıştırılmış bir ağ tarama aracı olup olmadığını sormakta.
Sistem üzerinde son çalıştırılan programları listelemek için NTUSER.dat dosyasını VEYA Prefetch kayıtlarını incelemeye ihtiyacımız var. NTUSER.dat dosyasını almak için "C:/Users/ibaloglu" klasörüne gidiyoruz. Diğer dosyalarda yaptığımız gibi NTUSER.dat ve onun ismine benzerlik gösteren tüm dosyaları bir klasöre kaydediyoruz. 
Registry Explorer ile kaydettiğimiz dosyayı açtıktan sonra, "SOFTWARE" klasörü altında "NMAP" adlı bir programın kaydını görüyoruz. İnternet üzerinden arama yaptığımızda bu programın bir ağ tarama aracı olduğunu anlıyoruz.
Cevap: Evet, NMAP

7.1. soruda bizden tarama aracının adını ve versiyonunu istemekte. Programın ismini zaten biliyoruz, 7. soruda aldığımız konum bilgisi ile programın kurulu olduğu yere gidiyoruz. (C:\Program Files (x86)\Nmap) Lokasyondaki "scan_log_nmap.xml" dosyasını kaydedip, sevdiğimiz bir text editörü ile açıyoruz. Ben WordPad ile açmayı tercih ettim.
Yazıyı incelediğimizde versiyonun 7.92 olduğuna dair bir ibare görüyoruz. Ekran görüntüsü üzerinde işaretleme yaptım.
Cevap: NMAP, 7.92

7.2. soruda bizden taramanın başlangıç tarihini sormakta. Aynı dosya içerisinde "startstr" ile başlayan metinde başlangıç tarihini ve saatini görüntüleyebiliyoruz.
Cevap: Tue Sep 21 16:24:36 2021

7.3 soruda bizden tarama aracında kullanılan parameterleri sormakta. Aynı dosya içerisinde "args" ile başlayan metinde saldırganın girdiği komutu görebiliyoruz.
Cevap: nmap -T4 -F 192.168.52.134

7.4. soruda bizden tarama sonucunda açık olarak tespit edilen portları sormakta. Sonuçları hatasız olarak almak için elimle dosyayı birazcık düzeltiyorum. Düzelttiğim dosyayı incelediğimde, 5 tane açık port olduğunu görüyorum. 
Cevap: 135, 139, 445, 3389, 5357

7.5. soruda bizden taratılan IP'ye ait MAC adresini istiyor. Aynı dosya içerisinde, port sonuçlarının altında MAC adresini görüntüleyebiliyoruz.
Cevap: 00:0C:29:CD:D2:68 

8. soruda bizden bilgisayara takılan USB Depolama Aygıtının takılma tarihini istemekte. 
Registry Explorer üstünde daha önce açtığımız SYSTEM dosyasına gidiyoruz. Registry hives menüsüne dönüyoruz. Sırasıyla 
ROOT > ControlSet001 > Enum > USBSTOR > Disk&Ven_SanDisk&Prod_Cruzer_Blade&Rev_1.00 > 4C530001220905112112&0 > Properties >  {83da6326-97a6-4088-9453-a1923f573b29} > 0064 klasörüne gidiyoruz. Sağ tarafta USB cihazının ilk takıldığı tarih gözükmekte.
Cevap: 2021-09-21 13:49:08

9. soruda bizden bilgisayara takılan USB Depolama Aygıtının çıkartılma tarihini istemekte. Aynı dizinde 0067 klasörüne gidiyoruz. Çıkartılma tarihi sağ tarafta gözükmekte.
Cevap: 2021-09-21 13:51:52

10. soruda bizden bilgisayara takılan USB Depolama Aygıtının seri numarasını istemekte. ROOT > ControlSet001 > Enum > USBSTOR > Disk&Ven_SanDisk&Prod_Cruzer_Blade&Rev_1.00 > 4C530001220905112112&0 dizinindeki "4C530001220905112112&0" USB aygıtının seri numarasını temsil etmekte. 
Cevap: 4C530001220905112112&0

11. soruda bizden "Kullanıcı parolalarını elde etmek için kullanılan zararlı yazılımın çalıştırılma tarihi" isteniyor. Windowsta yaygın olarak tanınan ve kullanıcı parolalarını çalmak amacıyla kullanılan ünlü bir yazılım var. Aradığımız yazılımın MimikAtz olduğunu varsayarak, Prefetch kayıtlarını inceliyoruz.

FTK Imager yardımı ile "C:/Windows/Prefetch" klasörünü export ediyoruz. Daha sonra "WinPrefetchView" programını çalıştırıyoruz. Options > Advanced Options seçeneğine girip, Prefetch Folder seçeneğine kaydettiğimiz klasörü gösteriyoruz.

Daha sonra karşımıza çıkan listede ufak bir göz gezdiriyoruz. Gözümüze ismi değişik gelen, yanlış yazılmış, benzer yazılmış program isimlerine bakıyoruz. Bahsettiğim MimikAtz yazılımının listede olduğunu farkediyoruz. Çift tıklayıp detaylarına girdikten sonra, "Last Run Time" seçeneği altında cevaba erişiyoruz. Bir dahaki işlemlerde ihtiyacımız olacağı için WinPrefetchView'i kapatmıyoruz.

Cevap: 21.09.2021 17:14:21, 21.09.2021 16:59:40

12. soruda bizden Mimikatz ile hangi aktif kullanıcıların parola bilgilerinin elde edildiğini istiyor. WinPrefetchView ile Mimikatz'ın olduğu konumu öğreniyoruz.
"C:/Users/ibaloglu/Downloads/mimikatz_trunk/x64"
FTK Imager yardımı ile Mimikatz'ın olduğu konuma gidiyoruz. Konumda "mimikatz_output.txt" adlı bir text dosyası ile karşılaşıyoruz. İncelediğimizde ibaloglu adlı kullanıcının NTLM ve SHA1 değerinin çalınmış olduğunu görüyoruz.

Cevap: ibaloglu

13. soruda bizden çalınan parolanın text halini istiyor. "https://crackstation.net/" adresine gidip, NTLM ve SHA1 değerini alt alta yazıyoruz. Captcha onaylamasını yaptıktan sonra, "Crack Hashes" butonuna basıyoruz. NTLM için "Password1" sonucunu çıkarıyor.

Cevap: Password1

14. soruda bizden sistemdeki Prefetch sayısını istiyor. WinPrefetchView programında sol alt kısma bakıyoruz.

Cevap: 167

15. soruda bizden paylaşıma açılmış dosyaları istiyor. SYSTEM dosyasını Registry Explorer ile açıyoruz. Available Bookmarks altından "Shares" klasörüne giriyoruz. Sağ tarafta paylaşıma açılmış dosyalar yazıyor.

Cevap: Temp ve Users

16. soruda bizden paylaşıma açılmış klasörlerin içerisinde yer alan txt çıktısında yazan, aktif bağlantı kurulan IP adresi ve Yerel Bağlantı Portu istenmekte. Users klasörüne gittiğimizde içerisinde herhangi bir txt dosyası olmadığını görüyoruz. "C:/Users/ibaloglu/Appdata/Local/Temp" klasörüne gidiyoruz. 
"network_connection_ib.txt" adlı bir dosyaya rastlıyoruz. İçeriğini incelediğimizde bir takım bağlantı logları olduğunu görüyoruz. Txt dosyasında görüldüğü üzere 445 portundan, 192.168.52.134 adresine bağlantı sağlanmış.

Cevap: 192.168.52.134, 445

17. soruda bizden 9/21/2021 tarihinde yapılmış uzak bağlantı işlemlerine dair tarih ve oturum açma tipi detaylarını istiyor. "C:/Windows/System32/winevt/Logs" dizini altından "Security.evtx" ve "Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx" dosyalarını export ediyoruz. EvtxExplorer programı ile aynı klasör içine kopyalıyoruz. Klasörün içerisinde terminali çalıştırıyoruz.

“EvtxECmd.exe -f “logfile” --csv “outputfolder” –-csvf security.csv” komutunda gerekli yerleri dolduruyoruz. Oluşan dosya içerisinde filtreleme yaparak devam ediyoruz. EventId sütunu altından "4624" filtrelemesi (başarılı giriş kodu) yapıyoruz. TimeCreated sütunu altından 09-21 araması yapıp çıkan sonuçlara filtre uyguluyoruz. Logon type kısmından "LogonType3" ve "LogonType 7" filtrelemesi uyguluyoruz. Thread kısmından küçükten büyüğe sıralama yapıyoruz ve kesin tarih-saatler elde ediyoruz. Çıkan sonuçları değerlendirmeye başlayabiliriz.

Cevap: Oturum Açma Tipi 4624
Tarihler: 
2021-09-21 14:23:03.4899964
2021-09-21 16:12:06.6335956
2021-09-21 14:49:17.2927314
2021-09-21 14:23:00.6737119
(Salise farklar olan 1-2 kayıt var, onları atlayarak yazdım. Ana tarih ve dakikaları aldım.)

18. soruda oturum açılan makinenin IP adresini istemekte. Aynı tabloyu sağa kaydırarak IP Adresine erişim sağlıyoruz.

Cevap: 192.168.52.134

19. soruda oturum açılırken kullanılan kullanıcı adını istemekte. PayloadData1 sütunu altında kullanıcı adını görüntülüyoruz. DESKTOP-69U8AFV domainine bağlı "ibaloglu" kullanıcısı.

Cevap: ibaloglu

20. soruda "İnternet tarayıcısı üzerinden oturum açılan bir e-posta hizmeti var mı, Varsa; Oturum açan e-posta adresi nedir?" sorusu ile karşılaşıyoruz. Daha önce incelediğimiz Prefetch verilerine dayanaraktan makine sahibinin "Google Chrome" kullandığını düşünüyoruz. FTK Imager yardımı ile imaj içindeki Google Chrome geçmişinin depolandığı "C:\Users\ibaloglu\AppData\Local\Google\Chrome\User Data\Default" konumuna gidiyoruz. "History" dosyasını export ediyoruz.

Export ettiğimiz dosyayı SQLite yardımı ile açıyoruz. Veriyi görüntüle kısmına gelip, tablo kısmından "urls" seçeneğini seçiyoruz. Geçmişi inceleyerek aradığımız cevaplara ulaşıyoruz.

Cevap: ProtonMail, Forensics_ibaloglu@protonmail.com

21. soruda bizden oturum açma tarihi ve saati isteniyor. SQLite üzerinden devam ediyoruz. "last_visit_time" sütunu, 7. satırdaki veriyi kopyalıyoruz. "13276709901254517"
İnternet üzerinden "Chrome Timestamp Converter" araması yapıp, ilk çıkan siteye giriyoruz. Çıkan kodu girip dönüştürüyoruz.
Hedef makinedeki Time-zone bizimkiyle aynı olduğu için direkt "Your time zone" kısmındaki sonucu alıyoruz.

Cevap: Salı, 21 Eylül 2021 17:58:21

22, 23 ve 24. soru:
Bu sorular için FTK Imager'den 2 dosya almamız gerekiyor.
"C:\$LOGFILE"
"C:\$Extend\$UsnJrnl\$J"
Bu dosyaları ayrı bir klasöre export ediyoruz.

"NTFS Log Tracker" programını açtıktan sonra aktardığımız dosyaları seçiyoruz.

"Parse" tuşuna bastıktan sonra, dosyaların kaydedileceği konum ve ismini seçiyoruz. Ardından "Start" butonuna basıyoruz.

İşlem bittikten sonra, "Export CSV" butonuna basıp dosyaların kaydedileceği klasörü seçiyoruz.

Oluşan "NLT_UsnJrnl_2021*" diye devam eden dosyayı Excel üzerinde açıyoruz. CTRL + F yaparak "OncekiAdimiBul" aratması yapıyoruz. Kayıtları incelediğimizde dosyanın eski adının "Windows_Forensic" olduğunu görüyoruz.

22. Soru Cevap: Windows_ Forensic

Aynı satırda değiştirilme tarihini görüyoruz.

23. Soru Cevap: 2021-09-21 18:06:58

24. soru için fazla bir çaba göstermeye gerek yok. FTK Imager ile makinenin masaüstü (Desktop) klasörüne gittiğimizde "OncekiAdimiBul" dosyasını görebiliyoruz.

24. Soru Cevap: Desktop

25. soruda bizden bir rar dosyasının şifresi isteniyor. Bunun için Brute-Force kullanacağız. Ben bunu linux ortamında yapmayı tercih ediyorum. (Windows için "Free RAR Password Recover" kullanılabilir.) Dosyayı sanal makine içerisine aktarıyoruz.

Terminalde "crunch 6 6 abcdefghijklmnopqrstuwvyz -o wordlist.txt(veya hangi ismi vermek isterseniz)" komutu ile bir wordlist oluşturuyoruz.

rar2john Flag.rar > output.txt
john output.txt --wordlist wordlist.txt

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
