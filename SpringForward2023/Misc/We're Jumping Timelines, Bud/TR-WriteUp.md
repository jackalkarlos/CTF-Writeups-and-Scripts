![image](https://user-images.githubusercontent.com/88983987/224680565-2f6416c7-45bb-4d0b-8c0d-04ef6de3b4f4.png)

## Solution

Dosyayı unzip yaparak çıkartıyoruz.

``` 
┌──(kali㉿kali)-[~/Desktop]
└─$ unzip hm.zip 
Archive:  hm.zip
   creating: out/
 extracting: out/0.zip               
 extracting: out/1.zip               
                                                                                                                                                                         
┌──(kali㉿kali)-[~/Desktop]
└─$ cd out           
``` 

İki adet zip ile karşılaşıyoruz. İlkini çıkartıyoruz.

``` 
┌──(kali㉿kali)-[~/Desktop/out]
└─$ unzip 0.zip 
Archive:  0.zip
   creating: 0/
                                                                                                                                                                         
┌──(kali㉿kali)-[~/Desktop/out]
└─$ cd 0  
                                                                                                                                                                         
┌──(kali㉿kali)-[~/Desktop/out/0]
└─$ ls -la
total 8
drwxr-xr-x 2 kali kali 4096 Mar 12 03:05 .
drwxr-xr-x 3 kali kali 4096 Mar 13 13:51 ..
``` 

İlk zip boş???


``` 
┌──(kali㉿kali)-[~/Desktop/out]
└─$ unzip 1.zip 
Archive:  1.zip
   creating: 1/
   creating: 1/S/
  inflating: 1/wjtb.jpg              
  inflating: 1/rotv.jpg              
   creating: 1/E/
  inflating: 1/skelly.jpg            
   creating: 1/A/                                                                                                                                                                
``` 

Dosyayı çıkardığımızda "A", "E" ve "S" adında 3 adet boş klasöre ve 3 fotoğrafa rastlıyoruz. Fotoğraflardan bazı veriler çıkartmamız gerekecek.

rotv.jpg
```
┌──(kali㉿kali)-[~/Desktop/out/1]
└─$ strings rotv.jpg | tail
/GY!3
>>=I
cJoaw
}~fO+]
Nw>e
~<<'
N{O3
>Zx=
Q       ={
GOODSKELLEBONES!
```

skelly.jpg (şifresiz)
```
┌──(kali㉿kali)-[~/Desktop/out/1]
└─$ steghide info skelly.jpg 
"skelly.jpg":
  format: jpeg
  capacity: 3.5 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "IV.txt":
    size: 17.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
                                                                                                                                                                         
┌──(kali㉿kali)-[~/Desktop/out/1]
└─$ steghide extract -sf skelly.jpg 
Enter passphrase: 
wrote extracted data to "IV.txt".

┌──(kali㉿kali)-[~/Desktop/out/1]
└─$ cat IV.txt 
whatagreatmascot
```

Soruda bir adet kod vardı. Şifrelemenin AES olduğunu da zaten klasör isimlerinden tahmin ediyorduk. Geriye AES'i çözmek kalıyor.

<a href="https://gchq.github.io/CyberChef/#recipe=AES_Decrypt(%7B'option':'UTF8','string':'GOODSKELLEBONES!'%7D,%7B'option':'UTF8','string':'whatagreatmascot'%7D,'CBC','Hex','Raw',%7B'option':'Hex','string':''%7D,%7B'option':'Hex','string':''%7D)&input=MWFiOWVkOWNjZDk2MjYxMmIyNDA3MDA5MTMyZGFiZGU">Cyber Chef Recipe</a>

![image](https://user-images.githubusercontent.com/88983987/224682859-cbbbe760-eae7-4e43-a996-fd9392b1ab85.png)

Ancak "iLOVEtheRadio!" çıktısı da flag olarak kabul edilmiyor. Bu metini wjtb.jpg üzerinde steghide şifresi olarak deniyoruz.
```
┌──(kali㉿kali)-[~/Desktop/out/1]
└─$ steghide info wjtb.jpg
"wjtb.jpg":
  format: jpeg
  capacity: 237.1 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "2.zip":
    size: 168.8 KB
    encrypted: rijndael-128, cbc
    compressed: yes
                                                                                                                                                                         
┌──(kali㉿kali)-[~/Desktop/out/1]
└─$ steghide extract -sf wjtb.jpg      
Enter passphrase: 
wrote extracted data to "2.zip".
```

2.zip adında bir dosya çıkıyor. Unzip edip içerisindeki resim üzerinde stegseek ile brute-force deniyoruz.
```
┌──(root㉿kali)-[/home/kali/Desktop/out/1]
└─# unzip 2.zip
Archive:  2.zip
   creating: 2/
  inflating: 2/huh.txt               
  inflating: 2/@NITE.jpg             
 extracting: 2/0.zip                 
                                                                                                                                                                         
┌──(root㉿kali)-[/home/kali/Desktop/out/1]
└─# cd 2 
                                                                                                                                                                         
┌──(root㉿kali)-[/home/…/Desktop/out/1/2]
└─# stegseek --crack -sf @NITE.jpg /usr/share/wordlists/rockyou.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "timetravel"      
[i] Original filename: "flag.txt".
[i] Extracting to "@NITE.jpg.out".

                                                                                                                                                                         
┌──(root㉿kali)-[/home/…/Desktop/out/1/2]
└─# cat @NITE.jpg.out     
nicc{whatever_happened_2_nicc@nite}
```
nicc{whatever_happened_2_nicc@nite}


        
