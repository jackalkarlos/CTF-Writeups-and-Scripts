
# IGU Siber Güvenlik Kulübünün Tanıtım Günü İçin Hazırlanan Sorular ve Çözümü


İlk başta sizlere bir karekod sayfası dağıttık. Bu karekodları Google Lens veya benzeri bir uygulama ile taratarak 20 adet karekodun içinden sizi websitesine yönlendirecek karekodu bulmanız gerekiyordu.

![soru1-1](https://user-images.githubusercontent.com/88983987/206112959-6f9603c6-8077-4211-a491-b50f763676c3.png)
![WhatsApp Görsel 2022-12-06 saat 23 30 26](https://user-images.githubusercontent.com/88983987/206113010-62f201d9-e0e7-4536-b704-cf94a4d3453d.jpg)

## Doğru karekodu bulduğunuzda yönlendirildiğiniz site sizi aşağıdaki gibi bir ekran ile karşılıyordu.
![WhatsApp Görsel 2022-12-09 saat 01 11 06](https://user-images.githubusercontent.com/88983987/206578123-88b9167a-32aa-4271-9bba-90e0032e7c7d.jpg)

## Bu aşamada yapılabilecek başka bir şey olmadığı için şifre denememiz gerekiyor. Yanlış bir şifre denemesinden sonra bizi 2 adet belge karşılıyor.
![WhatsApp Görsel 2022-12-09 saat 01 19 35](https://user-images.githubusercontent.com/88983987/206579374-8fae5db9-a1ae-4765-b187-f2fbbb1b6e20.jpg)

## İlk önce "Rapor" yazılı belgeyi açıyoruz. Açıkça söylemem gerekirse, bu raddede kafanızı karıştırabilmek için bol bol gereksiz detay ekledim:) Bizim için gerekli bilgiyi sağlayacak olan kısım 2. sayfadaydı.

![rapor-2](https://user-images.githubusercontent.com/88983987/206580778-e2ae4fca-e96f-4ade-8250-0357fc56e7fd.png)

Bu kısımda, kişinin intih*r veya m*dde yöneliminin olmadığını, olayın muhtemelen bir suikast olduğunu ve OSINT ile kişinin bilgisayarının şifresini bulmaya çalıştığımızı farkediyoruz. Sonrasında raporda belirtilen "kırmızı defter" delilini incelemek için diğer belgeyi indirip açıyoruz.

## Kırmızı Defter
![kirmizidefter-1](https://user-images.githubusercontent.com/88983987/206581235-523c2d85-1fab-4a81-b943-898063d7f27d.png)
## Defterin ilk sayfalarında, günlüğe yeni başlandığı ve bizim işimize yarayabilecek bir bilgi olmadığını farkediyoruz. İkinci sayfaya geçiyoruz.
![kirmizidefter-2](https://user-images.githubusercontent.com/88983987/206581346-6a729d2d-a9aa-406e-bc27-8aaf30e84164.png)
## İkinci sayfada Şevval'in "Arda" adında, sinir sorunları olan şüpheli bir arkadaşı olduğunu farkediyoruz. Suikast ihtimalini güçlendiriyor. Üçüncü sayfaya geçiyoruz.
![kirmizidefter-3](https://user-images.githubusercontent.com/88983987/206581949-c2fb1c15-866f-456d-a4ab-f6be5d1845de.png)
## Üçüncü sayfada Şevval'in sosyal medya hesaplarının kullanıcı adı ve şifresini defterine not ettiğini farkediyoruz. 
Giriş yapmayı denesekte başarısız oluyoruz. Bu kadar basit bir şifreyi defterine not etmesi şüphe uyandırıyor. Sosyal medya hesaplarını incelemeye başlıyoruz.
![WhatsApp Görsel 2022-12-09 saat 01 45 15](https://user-images.githubusercontent.com/88983987/206582984-979fda9f-b99d-406f-914f-555f50e84f6f.jpg)

Biyografide bir "soğuk..." yazısı dışında hiçbir şey bulamıyoruz. "0" gönderi, "2" takipçi ve random takip edilenler.. Twitter hesabına geçiyoruz.
![image](https://user-images.githubusercontent.com/88983987/206586884-0b883514-70fe-4dfe-b7eb-ff1bdce62dcf.png)
## "Ilık" yazısı dikkatimizi çekiyor
![image](https://user-images.githubusercontent.com/88983987/206586974-c3722e75-4df8-4b15-a9a2-cdf4c4f95a7c.png)
## Hesabı incelemeye başlıyoruz.
![image](https://user-images.githubusercontent.com/88983987/206588817-274026df-9d39-4b37-b478-c96b27d30f4c.png)
## İlk 3 tweet'te ilgimizi çekecek bir şey yok, sıradan paylaşımlar. Devam ediyoruz.
![image](https://user-images.githubusercontent.com/88983987/206589164-0c9ca946-2dae-47c0-93bc-04ec5eab3213.png)
## Dış kaynaktan yüklenen bir "Never Gonna Give You Up" videosu karşımıza çıkıyor. Videoya tıklıyoruz.
![image](https://user-images.githubusercontent.com/88983987/206589343-c47ce7a3-5197-42b1-82b5-04cc062cd3d4.png)
Yorumların arasında dolaşırken Şevval'in yorumu dikkatimizi çekiyor. Sözlerin çok güzel olduğundan bahsediyor. Ayrıca klubümüzün hesabının bıraktığı "Sıcak.." yorumu, durumdan iyice emin olmamızı sağlıyor.<br>
![image](https://user-images.githubusercontent.com/88983987/206589454-914c4bfb-c645-4e54-bdf7-ade887255c31.png)<br>
Şarkının açıklamasında bulunan sözleri inceliyoruz. Sözlerin bulunduğu kısımda bir kullanıcı adı ve şifre bulunduğunu farkediyoruz.<br>
![image](https://user-images.githubusercontent.com/88983987/206589784-cee443a5-d6ee-4d04-a611-02ab34d5bb6e.png)<br>
Bulduğumuz kullanıcı adı ve şifreyi siteye girdiğimizde bize flag'i veriyor.<br>
![WhatsApp Görsel 2022-12-09 saat 02 43 08](https://user-images.githubusercontent.com/88983987/206590021-35b5f8ef-80bc-4f41-b4cc-8f017d7b32a0.jpg)


