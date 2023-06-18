# CTF’e erişmek için URL: <a href="http://www.ibrahimbaloglu.com/2021/10/windows-forensics-challange.html"> Challenge </a>

# Ad Soyad ve E-posta adresimizi kaydettikten sonra ilk soruya geçebiliriz.

# 1. Soru
![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/1126bbc5-2db9-4ae3-a369-0706b142a4da)

## Solution

Hash değerine ulaşmak ve diğer incelemelerimizi yapabilmek için, imaj dosyasını FTK Imager üzerinde açmamız gerekmekte.

FTK Imager programını açtıktan sonra, sol üstteki “File” menüsünden “Add Evidence Item” seçeneğini seçiyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/9ccc2729-1795-4df0-b1e2-f2559ebafa3d)

Çıkan ekrandan “Image File” seçeneğini seçip, “Sonraki” butonuna basıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/335cf85c-ef58-4332-813d-e435084ceb10)

“Browse” butonuna tıklayıp, imajın yer aldığı konumu seçiyoruz. “Finish” butonuna tıklıyoruz.

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/78679585-1d2c-4e43-ab74-4f494e4d8a1b)

Hash değerlerine aşağıdaki “Properties” menüsü altında erişebiliyoruz. MD5 Hash değerimizi alıyoruz.
