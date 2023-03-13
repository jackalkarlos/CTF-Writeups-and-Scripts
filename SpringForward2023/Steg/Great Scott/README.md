![image](https://user-images.githubusercontent.com/88983987/224793504-c0791c78-145e-4374-b53c-43a9c1d0a2c7.png)

## Solution
No Password - Şifre Yok
```
┌──(kali㉿kali)-[~/Desktop]
└─$ steghide info great-scott.jpg
"great-scott.jpg":
  format: jpeg
  capacity: 32.0 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "steganopayload615282.txt":
    size: 30.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
                                                                                                                                                                         
┌──(kali㉿kali)-[~/Desktop]
└─$ steghide extract -sf great-scott.jpg 
Enter passphrase: 
wrote extracted data to "steganopayload615282.txt".
                                                                                                                                                                         
┌──(kali㉿kali)-[~/Desktop]
└─$ cat steganopayload615282.txt 
nicc{It's_All_About_the_Mets!} 
```

nicc{It's_All_About_the_Mets!} 
