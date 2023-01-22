Yarışmada bize bir adet google drive linki veriliyor ve derine gitmemiz isteniyordu. Drive Linkini açtığımızda bir fotoğraf ile karşılaşıyoruz.<br>
![image](https://user-images.githubusercontent.com/88983987/213895757-2e01d1e1-1f79-4198-866d-fb167f37bc51.png)<br>
Fotoğrafta gözle görülebilir bir şey olmadığına emin olmadıktan sonra "derine git" cümlesini takip ederek steghide deniyorum. Fakat şifreli olduğunu görüyorum ve en hızlı tool olan stegseek ile şifreyi kırıyorum.<br>
<b>"└─# stegseek --crack -sf sea.jpg -wl /usr/share/wordlists/rockyou.txt"</b><br>
![image](https://user-images.githubusercontent.com/88983987/213895701-64617283-a77f-4c53-a457-b804627915ad.png)<br>
![image](https://user-images.githubusercontent.com/88983987/213895733-29b80d74-7ca7-45d8-a584-e58ed51655e3.png)<br>
Çıkan flag.txt dosyasında aradığımız şeyin burda olmadığı, daha da derine gitmemiz gerektiği söyleniyor. "La havle vela kuvveta" diyerek binwalka geçiyoruz:)<br>
"Daha da derine git" mesajını aldıktan sonra, verilerin içine gömülü verileri çıkartabilen "binwalk" aracını deniyoruz.<br>
<b>Not: Cihazınızı benim gibi sürekli rootta kullanmayın, bu makine dış ağa kapalı:)</b><br>
![image](https://user-images.githubusercontent.com/88983987/213895837-5fc24eb5-0a7a-49e5-8d5f-70460857b702.png)
Çıkan JPG dosyasını açmaya çalışıyoruz, fakat herhangi bir görüntü ile karşılaşamıyoruz. Hexeditor ile verilerini incelediğimizde dosya yapısının PNG dosya yapısına aşırı benzediğini, hatta birebir aynı olduğunu farkediyoruz. Bu detayı yakalamamıza yardımcı olan kısım, <b>"IHDR"</b> yazısı oluyor.
![image](https://user-images.githubusercontent.com/88983987/213895952-fba1428b-7f01-4de4-ae37-27892ee8850e.png)<br>
Dosyamızın aslında bir PNG dosyası olduğunu farkettikten sonra bunu hexeditor aracılığı ile düzeltiyoruz.<br>
![image](https://user-images.githubusercontent.com/88983987/213896028-274f7bb6-fbbb-4c09-88e3-9e1808531b9d.png)<br>
Fotoğraf kali'de bende hala açılmıyordu, Windows'a attığım zaman ise görüntü almayı başardım.<br>
![image](https://user-images.githubusercontent.com/88983987/213896065-bfa0e18c-752e-43d2-a8ea-c86856dcae68.png)<br>
Türlü steghide araçları denedikten sonra hiçbir şey bulamayınca, sorunun adı aklıma geldi. "Go Deep!". PNG fotoğraflarda saklanan verileri bulabilen TweakPNG adlı aracı denemeye karar verdim.<br><b>Not: Araç bir çok platformu destekliyor fakat compile etmeniz gerekiyor. Uğraşmamak için Windows üzerinde devam ettim.</b><br>
Açtığımda CRC hakkında hata verdikten sonra fotoğrafta gizlenen bir veri olduğuna emin oldum. Bu hatayı başka bir fotoğraf analiz aracında da keşfedebilirdik. Benim keşfetmem biraz tesadüfi oldu. Kali'de fotoğrafın açılmama sebebi de buydu.<br>
![image](https://user-images.githubusercontent.com/88983987/213896122-384c431c-7a9e-421b-b30f-f8c67452163e.png)<br>
Fotoğraf açıldıktan sonra F7'ye basarak önizleme kısmına geçtim.<br>
![image](https://user-images.githubusercontent.com/88983987/213896184-a8f9579f-c8cd-41ee-9068-ef87891d8bb9.png)<br>
En üstteki IHDR Chunk'ına 2 kez tıklatarak düzenleme ekranını açtım.<br>
![image](https://user-images.githubusercontent.com/88983987/213896263-7ac27182-279b-4faa-b79c-ed14c56e7310.png)<br>
Denizin altını görmek istediğim için height ayarını yavaş yavaş yükseltmeye başladım ve fotoğrafın gizli kısımlarının açılmaya başladığını gördüm. 410 yaptığımda ise flag ortaya çıktı.<br>
![image](https://user-images.githubusercontent.com/88983987/213896312-2842e61e-c1b0-4f07-99be-6a0e0f0430a7.png)<br>
<b>KCTF{g0_d33p_d0wn}</b>



