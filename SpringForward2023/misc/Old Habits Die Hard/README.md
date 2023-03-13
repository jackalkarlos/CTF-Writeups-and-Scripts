![image](https://user-images.githubusercontent.com/88983987/224674857-411c6d04-0225-4910-b6ef-ed5b2be591e2.png)

## Solution

```
┌──(root㉿kali)-[/home/kali/Desktop]
└─# zip2john Encryptedfile.zip > hash.txt
ver 1.0 efh 5455 efh 7875 Encryptedfile.zip/Decrypted_Flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=33, decmplen=21, crc=85290318 ts=720B cs=720b type=0
                                                                                                                                                                         
┌──(root㉿kali)-[/home/kali/Desktop]
└─# john hash.txt --wordlist=wordlist.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 3 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
password567      (Encryptedfile.zip/Decrypted_Flag.txt)     
1g 0:00:00:00 DONE (2023-03-13 13:23) 20.00g/s 122880p/s 122880c/s 122880C/s 123456..bonita1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                                                                                                                                                                         
┌──(root㉿kali)-[/home/kali/Desktop]
└─# unzip Encryptedfile.zip 
Archive:  Encryptedfile.zip
[Encryptedfile.zip] Decrypted_Flag.txt password: 
 extracting: Decrypted_Flag.txt      
                                                                                                                                                                         
┌──(root㉿kali)-[/home/kali/Desktop]
└─# cat Decrypted_Flag.txt 
nicc{P@$$w0rd_l!$t$}
```
nicc{P@$$w0rd_l!$t$}

