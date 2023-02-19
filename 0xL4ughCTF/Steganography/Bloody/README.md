# Bloody [150 pts]

**Category:** Steganography
**Solves:** 25

## Description
>just line ? but it contain a lot of infoooooooos

good luck.
https://youtu.be/dQw4w9WgXcQ

Author: xElessaway

## Solution

Açıklamadaki linkte RickRoll'landıktan sonra zip'ten çıkarıp ilgili görseli alıyoruz. "just line ? but it contain a lot of infoooooooos" açıklaması biraz düşündürüyor.

Daha sonrasında daha önceki CTF'lerimden tecrübe ile metinler ile fotoğraf oluşturulabildiği geliyor aklıma. Her bir kare yada piksel bir harfi anlam ifade ediyor aslında. Biraz anlatmakta zorlandım ama birazdan daha iyi anlayacaksınız. 

Normalde bu veriyi çıkartma işlemini script ile yapmak daha verimli sonuç verir. Lakin CTF sırasında online tool'lar varken script yazmakla vakit kaybetmek bana pek mantıklı gelmiyor. Zaten kısıtlı bir süre için yarışıyoruz. 

https://stegonline.georgeom.net/upload

Bu adrese gidip fotoğrafı upload ediyoruz.

Extract Files/Data seçeneğini seçiyoruz.

![image](https://user-images.githubusercontent.com/88983987/219949581-a1887f08-e5c6-40f5-83ec-e7bb27b255f1.png)

Çizgiler kırmızı olduğu için R (Red) kanalındaki verileri almamız yetiyor. Hangi renk kanalında olduğunu bilmeseydik hepsini seçebilirdik fakat çıkacak veri çok daha büyük olurdu. Hepsini seçip Go diyoruz.

![image](https://user-images.githubusercontent.com/88983987/219949612-14d5903a-af7b-40ec-a33a-a82794c695c3.png)

"Download Extracted Data" seçeneği ile dosyayı indirdikten sonra indirdiğimiz dosyayı CyberChef'e atıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219949759-5e7b0746-8d6d-410b-9de7-fb3699a638f4.png)

Find/Replace seçeneği ile "ÿ" karakterini yok ediyoruz. Dikkat etmemiz gereken nokta "Simple String" seçili olması.

![image](https://user-images.githubusercontent.com/88983987/219949805-d5cad77b-22c4-42ac-9c1c-1d8a050581a0.png)

## Flag

0xL4ugh{R_G_B_FOR_TH3_W1N}
