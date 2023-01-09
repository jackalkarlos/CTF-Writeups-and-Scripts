# RZIPS: Recursive Zip Suite

#### **TR [ ENG ⇣ ]**

```
██████╗░███████╗██╗██████╗░░██████╗
██╔══██╗╚════██║██║██╔══██╗██╔════╝
██████╔╝░░███╔═╝██║██████╔╝╚█████╗░
██╔══██╗██╔══╝░░██║██╔═══╝░░╚═══██╗
██║░░██║███████╗██║██║░░░░░██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░░░░╚═════╝░

[ Nuri ACAR ] [ nuriacar.com ]

[ RZIPS ] [ Recursive ZIP Suite ] [ v0.0.6 : 20201207232323 ]

[ Menu ]
===============================================================================
.
... 1. Recursive Zipper
...... [+] Zips your files, directories recursively.
...... [+] Adds password(s) to your .zip files.

... 2. Recursive Unzipper [ Try one by one! ]
...... [+] Extracts .zip files. If necessary, performs recursively.
...... [+] Performs wordlist attack to password protected .zip files!
.......... You must have at least a wordlist file for wordlist attack!
...... [!] Directory must exists only one zip!
.......... If you have multiple, isolate one of them and unzip it. Then next...
.......... Remember! Try one by one!

... 8. About & Source Code Repository & Version History
... 9. Exit
===============================================================================

Select an Option

>>>
```

### **RZIPS: Recursive ZIP Suite**

Bir CTF (Capture the Flag) flag'i düşünün: İç içe 2020 defa ziplenmiş ve
yetmezmiş gibi zip dosyalarına parola konulmuş. Ya manuel, yani tek tek siz
açacaksınız ki gerek yok ya da bu işi bilgisayara yaptıracaksınız. Yedi gün
boyunca oturup bu programı yazdım. CTF (bazıları hariç) yedi güne kalmaz tabii
lakin gelecekteki CTF'lerde işe yarayacak faydalı bir programım oldu.
**Yalnızca CTF'e girdiğinizde değil, önemli dosyalarınızı, parola korumalı
olarak defalarca zipleyerek korumak için de kullanabilirsiniz.**

### **Ne yapar?**

```
[ Menu ]
===============================================================================
.
... 1. Recursive Zipper
...... [+] Zips your files, directories recursively.
...... [+] Adds password(s) to your .zip files.

... 2. Recursive Unzipper [ Try one by one! ]
...... [+] Extracts .zip files. If necessary, performs recursively.
...... [+] Performs wordlist attack to password protected .zip files!
.......... You must have at least a wordlist file for wordlist attack!
...... [!] Directory must exists only one zip!
.......... If you have multiple, isolate one of them and unzip it. Then next...
.......... Remember! Try one by one!

... 8. About & Source Code Repository & Version History
... 9. Exit
===============================================================================
```

`1.` Bir dosyayı veya dizini, girdiğiniz sayı kadar iç içe zipler. İsterseniz
iç içe zip dosyalarınızın ilk (dipteki) ve sonuncusuna (oluşan son zip
dosyası) birer parola koyarak koruma sağlayabilirsiniz.

`2.` `n` defa iç içe ziplenmiş bir zip dosyasını, tek tek açıp en içteki
dosyayı çıkartır. Eğer zip dosyaları parola korumalıysa, programa bir kelime
listesi (wordlist) verip içindeki tüm kelimeleri tek tek deneterek zip
parolasını kırmayı deneyebilirsiniz. **Dikkat! Dizinde (klasörde) tek bir zip
dosyası olmalı. Aynı klasörde açmak istediğiniz çok sayıda zip dosyası varsa,
içlerinden birini izole edip onu açın, ardından aynı şekilde sırayla
diğerlerini açın.**

`8.` Program hakkında bilgiler verir, kaynak kod deposuna yönlendirir,
versiyon geçmişini görüntüler.

`9.` Programdan çıkar.

**Ayrıca, ziplerken veya çıkarırken, eğer orijinal dosyaları korumak
isterseniz *zip_backup* isminde bir dosya oluşturarak dosyalarınızı korur. Bu
özelliği program içinden seçebilirsiniz.**

---

#### **ENG**

```
██████╗░███████╗██╗██████╗░░██████╗
██╔══██╗╚════██║██║██╔══██╗██╔════╝
██████╔╝░░███╔═╝██║██████╔╝╚█████╗░
██╔══██╗██╔══╝░░██║██╔═══╝░░╚═══██╗
██║░░██║███████╗██║██║░░░░░██████╔╝
╚═╝░░╚═╝╚══════╝╚═╝╚═╝░░░░░╚═════╝░

[ Nuri ACAR ] [ nuriacar.com ]

[ RZIPS ] [ Recursive ZIP Suite ] [ v0.0.6 : 20201207232323 ]

[ Menu ]
===============================================================================
.
... 1. Recursive Zipper
...... [+] Zips your files, directories recursively.
...... [+] Adds password(s) to your .zip files.

... 2. Recursive Unzipper [ Try one by one! ]
...... [+] Extracts .zip files. If necessary, performs recursively.
...... [+] Performs wordlist attack to password protected .zip files!
.......... You must have at least a wordlist file for wordlist attack!
...... [!] Directory must exists only one zip!
.......... If you have multiple, isolate one of them and unzip it. Then next...
.......... Remember! Try one by one!

... 8. About & Source Code Repository & Version History
... 9. Exit
===============================================================================

Select an Option

>>>
```

### **RZIPS: Recursive ZIP Suite**

Consider a CTF (Capture the Flag) flag: zipped 2020 times nested and password
set on zip files as if it wasn't enough. Either manually, you will open it one
by one, so there is no need or you will have this work done on the computer. I
sat down and wrote this program for seven days. CTF will not take up to seven
days (except some) of course, but I have had a useful program that will work
with future CTFs. **You can use it not only when you join the CTF, but also to
protect your important files by zipping them with passwords over and over
again.**

### **What does it?**

```
[ Menu ]
===============================================================================
.
... 1. Recursive Zipper
...... [+] Zips your files, directories recursively.
...... [+] Adds password(s) to your .zip files.

... 2. Recursive Unzipper [ Try one by one! ]
...... [+] Extracts .zip files. If necessary, performs recursively.
...... [+] Performs wordlist attack to password protected .zip files!
.......... You must have at least a wordlist file for wordlist attack!
...... [!] Directory must exists only one zip!
.......... If you have multiple, isolate one of them and unzip it. Then next...
.......... Remember! Try one by one!

... 8. About & Source Code Repository & Version History
... 9. Exit
===============================================================================
```

`1.` Zip a file or directory recursively in the number of times you enter. If
you want, you can protect the first (bottom) and last (last zip file) of your
nested zip files by putting a password.

`2.` It extracts a zip file that has been zipped nested `n` times one by one
and gets the innermost file. If zip files are password protected, you can try
to crack the zip password by giving the program a wordlist and checking all
the words in it one by one. **Attention! There should be a single zip file in
the directory (folder). If there are many zip files you want to open in the
same directory, isolate one of them and open it, then open the others
sequentially in the same way.**

`8.` Gives information about the program, directs to the source code
repository, displays version history.

`9.` Exits the program.

**It also protects your files while zipping or extracting, by creating a
directory called *zip_backup* if you want to preserve the original files. You
can choose this feature from within the program.**

