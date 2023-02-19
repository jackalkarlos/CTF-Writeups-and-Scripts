# Tricky [250 pts]

**Category:** Forensics
**Solves:** 33

## Description
>Our Company is hacked and we wanna know the reason 
can you investigate in the accident 

Author: abdoghazy
https://drive.google.com/file/d/1hQQ9noJflh5kLIg5N6GnXN0oYda7c6XG/view?usp=share_link

#### Hint 

## Solution

Cidden adı kadar Tricky bir soruydu :) Bize şirketlerinin neden hacklendiğini soruyor. Bu olayı araştırmamızı istiyor. Sağ tık, Follow TCP Stream diyerek iletişimi detaylıca izliyoruz. İlk 490 TCP Stream içerisinde hiçbir terslik gözükmüyor. Normal kullanıcılar giriş yapıyorlar, işlemlerini halledip çıkıyorlar. Fakat 493. TCP Streaminde bir terslik var.

Birisi /upload.php sayfası aracılığı ile "favicon.ico" dosyası yüklüyor fakat içerisinde garip bir payload var..

![image](https://user-images.githubusercontent.com/88983987/219964131-c7182570-8b52-4f85-896a-c57d6ea4642a.png)

Requestteki encoding dolayısıyla doğrudan dönen cevabı göremiyoruz. Ya da, ben beceremedim:) Fakat Export seçeneği ile favicon dosyalarını bir klasöre export ediyoruz.

![image](https://user-images.githubusercontent.com/88983987/219964283-7e683112-0fd7-4f66-a33e-0b530409aebc.png)

Filtreleme..

![image](https://user-images.githubusercontent.com/88983987/219964338-c2662b7b-d660-4b09-a730-08b2c64d830c.png)

Kaydet diyerek hepsini bir klasöre aktardıktan sonra içeriklerini incelemeye başlıyoruz.

İlk dosya gayet normal.

![image](https://user-images.githubusercontent.com/88983987/219964420-bce44e48-3c33-44d3-8016-881a5397796b.png)

İkinci dosyaya bakıyoruz. (favicon(1).ico)

![image](https://user-images.githubusercontent.com/88983987/219964445-0edc5384-0818-48f3-b174-b721e06f7b9c.png)

![image](https://user-images.githubusercontent.com/88983987/219964516-a90be3c2-2028-4997-9033-1f3a13b783e1.png)

![image](https://user-images.githubusercontent.com/88983987/219964458-052fb542-15c6-4428-aa34-5fdab6ff965b.png)

Kalan favicon dosyasını incelemeden önce sonraki stream'i inceliyoruz. İçinde bir payload olması olası.

497. TCP STREAM

![image](https://user-images.githubusercontent.com/88983987/219964597-84711d72-9d38-4f26-94e8-cbdb1863bbb8.png)

.secret adlı dosyayı tersten okuyor, base64 ile şifreliyor, daha sonrasında base64ü tersine çeviriyor. wtf dude?

favicon(2) dosyamıza bakıyoruz. Ters bir base64 kodu buluyoruz.

![image](https://user-images.githubusercontent.com/88983987/219964673-6555e6bf-232d-4d84-8d80-d64da2977c15.png)

Tersine çeviriyoruz.
```
fWVub0RfcyFfZWduZWxsYWhDXzUhaFRfeWxsQG5pRntoZ3U0THgwCg==
```
Decode ediyoruz.
```
}enoD_s!_egnellahC_5!hT_yll@niF{hgu4Lx0
```
Tersine çeviriyoruz.
```
0xL4ugh{Fin@lly_Th!5_Challenge_!s_Done}
```

## Flag
0xL4ugh{Fin@lly_Th!5_Challenge_!s_Done}

