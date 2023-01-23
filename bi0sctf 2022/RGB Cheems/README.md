<h1>Açıkça konuşmam gerekirse şu zamana kadar en çok eğlendiğim ve bir şeyler öğrenmeme katkı sağlayan sorulardan birisiydi:)<br></h1>
Daha önce hiç Unity oyunu incelememiştim veya üzerinde reverse işlemi denememiştim. Bu yüzden ilk işim oyunu oynamaya çalışmak oldu :)<br>
Oyunda tatlı mı tatlı bir "Doge" ana karakterimiz var. Ana hikayemiz çok basit. Önümüzdeki bir takım rakiplere ölmeden altınları toplayarak bölümü geçmeye çalışıyoruz. Oyunda bir süre ilerledikten sonra oyunda ileriye gitmek imkansız oluyor. Çünkü zıplama mesafemizi aşan bir kısımla karşılaşıyoruz.

![image](https://user-images.githubusercontent.com/88983987/214165191-12800235-bb48-47f9-9d28-1427ea8bd9ef.png)<br>

Bu kısımda zıplama mesafemizi arttırmamız gerektiğini farkediyorum. Nasıl yapacağımı araştırmaya başlıyorum. Cheat Engine adlı programda memory değerlerine müdahale ederek zıplama değerlerini bulmaya çalışıyorum lakin nafile.. Biraz daha araştırma yaptıktan sonra /Chall_Data/Managed klasörü içerisinde Unity oyunlarının belkemiği olan "Assembly-CSharp.dll" adlı bir dosya olduğunu farkediyorum. Bu dosyayı açıp kurcalayabileceğim dnSpy adlı bir program kuruyorum. <br>

![image](https://user-images.githubusercontent.com/88983987/214164545-a54a09c1-4c18-4fdf-8eab-a31a710bee87.png)<br>

Zıplama değerlerini bulmak için kurcalamaya başlıyorum. İngilizce terimlerden dümdüz devam ediyorum :) Mekaniklerin altında kullanıcı kontrollerini içeren bir class buluyorum. İncelemeye başladıktan sonra zıplama değerinin hesaplandığı yere denk geliyorum. <br>

![image](https://user-images.githubusercontent.com/88983987/214168745-0ebefa0a-2c0f-4182-bc1f-16b5d85e916c.png)<br>

Sağ tık "Sınıfı Düzenle" tuşuna tıklayıp, bulduğumuz kısmı dümdüz 99f gibi hayvani bi değer ile değiştiriyoruz.<br>

![image](https://user-images.githubusercontent.com/88983987/214169901-671776be-edd4-42d7-b84b-2921c6cf697c.png)<br>

Derle tuşuna basıyoruz ve sonrasında sol üstteki Dosya seçeneğinden "Modülü kaydet" tuşuna basıyoruz. Ta, da! Oyunu tekrar açıyoruz ve Doge artık süper Doge! Uçabiliyor..

![image](https://user-images.githubusercontent.com/88983987/214170428-ee21b2f2-804a-4428-95ef-ea761fe31e9b.png)<br>

Oyunu azıcık oynayıp, gizli asansör tümseği bulduktan sonra flag'e erişiyosunuz, bu kısım teknik bilgi istemiyorkdfmksdofmsd<br>

![image](https://user-images.githubusercontent.com/88983987/214170587-298f2dd3-a61f-4da2-a0a6-be17cf753141.png)

![image](https://user-images.githubusercontent.com/88983987/214170710-747fa907-8021-405b-a546-269f029210fe.png)

<b>bi0sctf{GG!_H4X_FOR_TH3_WIN}</b>
<h1>NOT: Kendiniz deneyebilmeniz için orjinal oyun dosyasını rar olarak paylaştım. Ayriyeten benim sırf can sıkıntısına yaptığım süper zıplama, ölümsüzlük, anti jumpstun gibi hilelerin olduğu dll dosyasını paylaştım. Denemek isterseniz bakabilirsinizskfdmkodsmo. Son olarak SUPER DOGE videosu...</h1>

https://www.youtube.com/watch?v=gjoUSHgr7Cw&ab_channel=AMK
