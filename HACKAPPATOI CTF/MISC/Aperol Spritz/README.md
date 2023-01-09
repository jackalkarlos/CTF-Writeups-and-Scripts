
Bu soruda bize bir adet jpg dosyası veriliyor. İçeriğinde işimize yarayabilecek bir şey yok gibi gözüküyor. Steghide ya da binwalk gibi araçlar ile tarattığımızda herhangi bir sonuç bulamıyoruz. Fakat Steghide bize bir uyarı veriyor.
![Ekran görüntüsü 2022-12-12 135706](https://user-images.githubusercontent.com/88983987/207029027-ed381d94-5642-4471-97f9-7c7cd78ae8ff.png)<br>
Bu uyarının anlamı dosyanın bizim gördüğümüzün dışında 4539 byte daha içerdiği. Hint'e baktığımızda "size is matter" yazısını görüyoruz. 
![image](https://user-images.githubusercontent.com/88983987/207029134-d21ad4a0-8e30-4422-95d1-63f0c5712c6c.png) <br>
Hint ve uyarıdan yola çıkarak bizim gördüğümüzün dışında kalan alanı görebilmek için dosyanın hex kodlarındaki resim çözünürlüğü ile oynamamız gerekiyor.
CyberChef'i açıp dosyayı önce hex haline getiriyoruz. Bunun için "To Hex" aracını kullanıyoruz.
![image](https://user-images.githubusercontent.com/88983987/207029344-3bc93e22-9e09-4dfe-a107-0ddd3895add9.png)
Sonrasında hex kodlarını düzenleyip, resmi görüntüleyebilmek için, hex kodlarını kopyalıyoruz ve "To Hex" aracını siliyoruz. Sırasıyla "From Hex" ve "Render Image" araçlarını ekliyoruz.
![image](https://user-images.githubusercontent.com/88983987/207029597-afc30350-ea3e-423a-9602-9f0490a989ab.png)
Sonrasında hex kodları içerisinde resmin çözünürlüğünün gizlendiği alanı bulabilmek için ufak bir google araştırması yapıyoruz. JPEG dosyalarının belirli "marker"leri olduğunu ve bunların düzenlenebildiğini görüyoruz. Ekstra kaynakları makale sonunda ekleyeceğim.
![image](https://user-images.githubusercontent.com/88983987/207029934-c1b84aea-f5c8-4806-bd20-d06b32ee0839.png)
Başlangıç framelerinin 2 farklı türü olduğunu görüyoruz. İlkini hex kodları içinde arattığımızda herhangi bir sonuç bulamıyoruz. Fakat 2. seçeneği arattığımızda karşımıza çıkıyor.
![image](https://user-images.githubusercontent.com/88983987/207030142-9644f4da-9be2-485b-8832-f75737b98d90.png)
Bu kısmı neye göre düzenleyeceğimizi aşağıdaki tablodan inceliyoruz.
![image](https://user-images.githubusercontent.com/88983987/207030612-22901216-c55b-4e3a-a3f1-aac41791c381.png)<br>
6. basamaktaki hex değerini 3 arttırdığımızda flag karşımıza çıkıyor. Stegonagrafinin ne kadar ileri gidebileceğine dair en güzel örneklerden birisi.
![image](https://user-images.githubusercontent.com/88983987/207030831-c4bf59a0-456e-42fa-8a65-83db97d6d90b.png)

Sources:
https://blog.cyberhacktics.com/hiding-information-by-changing-an-images-height/<br>
https://docs.fileformat.com/image/jpeg/<br>
https://en.wikipedia.org/wiki/JPEG#Syntax_and_structure
