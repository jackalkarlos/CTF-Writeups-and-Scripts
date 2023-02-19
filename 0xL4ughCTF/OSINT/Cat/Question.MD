# Cat [100 pts]

**Category:** Osint
**Solves:** 123

## Description
>i lost my cat a while ago , and recently i found a photo of it can you help me track my cat by getting the location of this image. 

flag is in the format: 0xL4ugh{Latitude,Longitude}. Use the 6 digits after the decimal point. (ex: 112.1234567 --> 112.123456)

Author :0xMesbaha

## Solution
![10472912333_57c751743a_w](https://user-images.githubusercontent.com/88983987/219947625-c4b61c17-92aa-448f-8b09-69131871aa86.jpg)

Soruda bizden kedinin olduğu konumu istiyor.

Sol altta bir isim görüyoruz. 

<b>"Saswat Kumar Dash"</b>

Bu ismi Google Görseller üzerinde aratıyoruz, ve kişinin çektiği fotoğrafları Flicker üzerinde paylaştığını görüyoruz.

![image](https://user-images.githubusercontent.com/88983987/219947675-29092aa5-89ee-458e-99f0-dff83682c736.png)

Resimdeki linkten ilerleyerek kişinin Flicker profiline girip aynı fotoğrafı buluyoruz.

https://www.flickr.com/photos/95789140@N05/10472912333/

Açıklama kısmında lokasyonun paylaşıldığını görüyoruz. Tıklıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219947726-13bb4a7c-9e83-4506-9d35-61fdf8f7f0c0.png)

Bizi bu linke yolluyor.

https://www.flickr.com/search/?lat=29.386886&lon=47.977166&radius=0.25&has_geo=1&view_all=1

Linkten latitude and longitude değerlerine ulaşıyoruz. Noktalı kısımdan sonraki ilk 6 değeri alıyoruz.


## Flag

0xL4ugh{29.386886_47.977166}

