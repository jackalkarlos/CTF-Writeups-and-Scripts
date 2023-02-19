# Zar [136 pts]

**Category:** Steganography
**Solves:** 19

## Description
>Fast as zaraki boi. try to find him.

Author: xElessaway

#### Hint 

## Solution
Fotoğraf üzerinde StegSeek, Binwalk gibi türlü türlü araçları denedikten sonra bir sonuç alamıyoruz. "cat" ile fotoğrafı okumaya çalıştığımızda son satırların boş olduğunu farkediyoruz. Fotoğrafı "nano" ile açınca son satırlarda cidden bir kodlama olduğunu farkediyoruz.
![image](https://user-images.githubusercontent.com/88983987/219953325-085966e5-d7ef-4463-bb96-7881ca2126b7.png)
Tail komutu ile sadece kodlama olan son satırları alıyoruz. Boşluklar sondan 57. satırdan başlıyor.

NOT: Boşluk kodlaması "Whitespace encoding" türünde olduğu için '.ws' uzantısı ile kaydediyoruz.
```
┌──(root㉿kali)-[/home/kali/Desktop]
└─# tail -n 56 Zar.jpg > encoding.ws
```
Aşağıdaki linkten decode ediyoruz.

https://www.dcode.fr/whitespace-language

![image](https://user-images.githubusercontent.com/88983987/219953528-4c20e286-2c80-4dcd-93c9-ff7d4eb6e1c2.png)


## Flag

0xL4ugh{F4S5_45_Z4R4K1_B0I}
