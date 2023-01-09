![image](https://user-images.githubusercontent.com/88983987/207185174-913cad4c-5e73-4760-bd2a-269cb215bfb8.png)<br>
Dosyayı Wireshark ile açtığımızda bir takım e-posta iletişimi görüyoruz. Çok fazla mail içeriği olduğu için üst kısımdan postaların sıralandırılmasını değiştirip hızlıca mail içeriklerine ulaşıyoruz.
Bu sıralamayı yapmak için üst kısımdaki sekmelerde "Info" yazısına 1 kez tıklatmak yeterli oluyor.
![image](https://user-images.githubusercontent.com/88983987/207185759-042a1ade-098c-45aa-bcbd-9825f22da3f7.png)<br>
Verileri incelediğimizde a harfi ile başlayıp z harfine kadar giden random veriler olduğunu görüyoruz. Veri kirletme işi gerçek hayatta anti-forensics için uygulanabilen bir teknik. Bunun için diğerlerinden farklı olabilecek ve dikkatimizi çekecek bir veri arıyoruz.<br>
![image](https://user-images.githubusercontent.com/88983987/207185979-af73a265-56ee-40ff-90ea-c2e82fcaa47f.png)<br>
En üst kısımdaki bir Base64 kodu dikkatimizi çekiyor. Decode ediyoruz. <br>
![image](https://user-images.githubusercontent.com/88983987/207186455-5675fd4e-b176-4ce4-8820-c178f94e460d.png)<br>
![image](https://user-images.githubusercontent.com/88983987/207188578-64db2de4-18ca-4540-b776-ec7c0c58d4eb.png)<br>
![image](https://user-images.githubusercontent.com/88983987/207190965-caf70c09-f0fa-48db-aa8c-339f692bc213.png)<br>
"https://www.base64decode.org/" sitesi ile decode ediyoruz. Karşımıza bir takım veriler geliyor. Bunların ne verisi olduğunu anlayabilmek için "dcode.fr/cipher-identifier" sitesinde taratıyoruz.
![image](https://user-images.githubusercontent.com/88983987/207191681-54bbde77-1cf4-4b03-b24d-7c4a6c278204.png)<br>
![image](https://user-images.githubusercontent.com/88983987/207191815-0f484821-7a3d-4f72-853b-5174136850c3.png)<br>
Verinin büyük ihtimalle "Hexadecimal data" olduğunu söylüyor. Veriyi çözümleyebilmek için "https://codepen.io/abdhass/full/jdRNdj" adresine gidiyoruz. Bu araç "Hexadecimal" verileri bir resime dönüştürmemize yarıyor. Veriyi kopyalayıp "Convert" butonuna bastıktan sonra flag bizi karşılıyor.<br>
![image](https://user-images.githubusercontent.com/88983987/207193072-26df40c5-068e-4fcc-a963-bbfbf35f1892.png)
