# BACKDOOR-CTF-BLENDER-WRITE-UP
BACKDOOR CTF BLENDER WRITE UP

Soruda bize sadece bir adet blender fotoğrafı veriliyordu. CTF Checklist denemelerimi tek tek yaparken, resmin içine gömülmüş birkaç veriyi binwalk ile tespit ettim.<br> 
![image](https://user-images.githubusercontent.com/88983987/208731526-eef659c8-32ca-4abd-9931-3092f20d6f52.png)<br>
Dosyaları incelemeye başladığımda işime yarayabilecek veriler arasında resmin kendisini ve bir adet zip dosyasını buldum.<br>
![image](https://user-images.githubusercontent.com/88983987/208731691-2feca221-d8c6-4667-93b0-eaa00f3fab77.png)<br>
Zip dosyasını çıkarttıktan sonra "file *" komutu ile dosyaların türünü belirledim. PNG dosyası olduklarını farkettim. Onları sırasıyla "blend" olacak şekilde png eki ile yeniden adlandırdım.<br>
![image](https://user-images.githubusercontent.com/88983987/208732017-cc70c2fd-ede8-4041-a843-82b46b2ddec9.png)<br>
![image](https://user-images.githubusercontent.com/88983987/208732409-ea8661b6-8b56-44ea-befd-250e8aad6096.png)<br>
Fotoğraflar kilobayt boyutunda ve hiçbir şey ifade etmiyordu. Bu yüzden ASCII verilerini okumayı denemek istedim. Bunun için yazdığım scripti repo'ya ekledim.<br>
![image](https://user-images.githubusercontent.com/88983987/208732722-35cda07e-0a6e-4f95-a172-3e1453dfdde0.png)<br>
Karşıma bir takım veriler çıktı. Asıl ilgimi çeken "ob.data.body" kısmındaki veriler oldu. Bunların morse kodu olduğunu tahmin ediyorum.<br>
![image](https://user-images.githubusercontent.com/88983987/208733071-1820f84d-8932-43f2-8106-3cf769e75f02.png)<br>
CyberChef üzerinden "From Morse" özelliği ile Decode edebilmek için sadece gövdedeki veriler kalacak şekilde temizliyorum.<br>
![image](https://user-images.githubusercontent.com/88983987/208733535-00a54127-ae9d-4b11-adeb-3ab62c709cb8.png)<br>
![image](https://user-images.githubusercontent.com/88983987/208733697-f41be20f-e0ec-43c0-b853-dff20abf4267.png)
"BORNTOSTANDOUTSOWON'TBLEND"
