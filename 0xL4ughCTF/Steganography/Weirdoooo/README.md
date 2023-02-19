# Weirdoooo [100 pts]

**Category:** Steganography
**Solves:** 37

## Description
>Too many numbers but i guess you know what you should do.



Author: xElessaway

## Solution
Soruda içerisinde bir sürü anlamsız sayı olan bir text dosyası veriliyordu. Biraz aşağı indiğinizde 255 sayısının bol bol tekrar ettiğini görebiliyoruz. Bir editor içerisinde (örn: EmEditor) 255 sayısını arattığımızda, bir flag gizlendiğini rahatlıkla anlayabiliyoruz.
![image](https://user-images.githubusercontent.com/88983987/219952984-2471dde4-693a-4067-94d2-f0f8963ac184.png)

Biraz yaklaştığımızda 1 ila 255 arası değişen sayıların flag metnini oluşturduğunu, 0'ın ise dış kenarları oluşturduğunu farkediyoruz.

![image](https://user-images.githubusercontent.com/88983987/219953031-cb80ae15-6390-41db-8974-592ae914f559.png)

0'ları bir tab boşluğu ile, 1-255 arasındaki sayıları siyah bir unicode karakter (■) ile değiştirecek bir script yazıyoruz. (scripti paylaştım) Çalıştırıp editor ile  scriptin oluşturduğu dosyaya bakıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219953171-66303bdf-6b45-4f4e-b9a6-8c795e751dee.png)



## Flag

0xL4ugh{NO7_JU$T_NUM63R5}
