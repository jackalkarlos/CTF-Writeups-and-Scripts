# PVE 1 [150 pts]

**Category:** Forensics
**Solves:** 50

## Description
>An attacker attacked our server. we got a dump so can you investigate it for us?

Q1: What is the operating system and kernal version of the dump

Download: https://drive.google.com/file/d/1IV95rb5VH8K2PD27zN-K53HC8NNL8njE/view?usp=sharing

Flag format: 0xL4ugh{OsName_theFullKernalVersion}
Author: xElessaway

#### Hint 

## Solution

Bu seride imajı inceleyebilmemiz için bir volatility profili inşaa etmemiz gerekicek. Hem ilk soruyu cevaplayabilmek için, hem bu profili inşaa edebilmek için çalıştırmamız gereken bir komut var.

NOT: 4. soruya kadar hepsini sadece strings ve grep ile çözebilirsiniz fakat bu durumda 5. soruyu çözemeyeceksiniz, ayrıca bu beklenmeyen bir çözüm türüdür. CTF üzerindeyseniz strings ile çözebildiğinizi çözüp 5. soruya öyle başlayın, zaman bazında size puan kazandıracaktır. İlk önce nasıl bir profil inşaa edebileceğinizi anlatacağım, sonrasında soruları çözmeye başlayacağım. Örneğin ikinci soru normalde bash history ile alınıyor, ama ```grep apache``` ile de çekilebiliyor.
```
└─# strings PVE.vmem | grep -i --text "Linux " | head
*Linux UI
*Linux UI
*Linux UH
Linux 4.4.0-186-generic Ubuntu 16.04.7 LTS
if [ -e /proc/cmdline ]; then #linux only - future proofing against BSD and Hurd :)
linux|linux console
linux   H
Failed to load SELinux policy
SELinux policy denies access.
Linux version 4.4.0-186-generic (buildd@lcy01-amd64-002) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.12) ) #216-Ubuntu SMP Wed Jul 1 05:34:05 UTC 2020 (Ubuntu 4.4.0-186.216-generic 4.4.228)
```


## Flag
0xL4ugh{Ubuntu_4.4.0-186-generic}

## Profil İnşaası

Sistemimizin "Ubuntu 16.04.7 LTS" üzerinde çalıştığını öğrenmiştik. Bir sanal makine oluşturup içine bu sürümü kuracağız.

https://releases.ubuntu.com/16.04/ubuntu-16.04.7-desktop-amd64.iso

Bu adresten indirip sanal makinenize kurabilirsiniz. Daha hızlı kurulum için kurulum esnasında ekstra paketleri indirme seçeneğini pas geçmesini isteyin. (ubuntu kurulumunu da anlattırmayın yani...)

Makineyi başlatıyoruz.

Şifre sorarsa, kurulum sırasında belirlediğiniz şifredir.

Root kullanıcısına geçiyoruz.

![image](https://user-images.githubusercontent.com/88983987/219966315-b6b8ed50-9191-4a1c-9c8c-8100ac1bf9f6.png)

İmajdaki kernel versiyonumuzun "4.4.0-186-generic" olduğunu öğrenmiştik. Aynı kerneli makine üzerine kuruyoruz.

```
apt-get install linux-image-4.4.0-186-generic linux-modules-4.4.0-186-generic linux-headers-4.4.0-186-generic -y
```

![image](https://user-images.githubusercontent.com/88983987/219966617-d16b94a2-a68e-4804-a963-e3576bb050de.png)

Bende zaten kurulu olduğu için direkt kurulu olduğuna dair uyarı verdi.

Bir sonraki aşamada volatility profili oluşturabilmek için volatilityi clonelamamız gerekiyor. Bunun içinde önce git'i kurmamız gerekiyor. Ayrıca profilimizi kurabilmek için dwarfdump adlı bir araca daha ihtiyacımız olacak.
```
apt-get install git dwarfdump -y
```
Daha öncesinde kurmuştum.

![image](https://user-images.githubusercontent.com/88983987/219966725-68ab9781-d947-44fc-8dbc-4824e568cfc5.png)
```
git clone https://github.com/volatilityfoundation/volatility.git
```
Klonlamaya çalıştığım yerde aynı adda bir klasör olduğu için hata verdi, fakat sizde sorunsuz işlemi tamamlayacak.
![image](https://user-images.githubusercontent.com/88983987/219966764-9832fc1c-6882-4c27-92c9-93937538677f.png)

Daha sonrasında cihazı kurduğumuz kernel'e rebootluyoruz. Bunun için sanal makineyi kapatıyoruz, açılırken ESC tuşuna basıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219966879-0bd3078a-630b-43a8-bcf8-be8600edf3b7.png)

![image](https://user-images.githubusercontent.com/88983987/219966891-3ed1bb76-b14a-495f-b7df-35b521cccde0.png)

Enter tuşuna tıklayıp boot ediyoruz.

![image](https://user-images.githubusercontent.com/88983987/219966982-e6f52f68-486f-4dfb-85c1-9630912c6938.png)

Doğru kernel üzerindeyiz:)

Volatility'in profil oluşturma aracını kullanabilmek için Linux kernel plugin'ini kurmamız gerekiyor. Aşağıdaki komutları çalıştırıyoruz.
```
cd /volatility/tools/linux/
make
```

![image](https://user-images.githubusercontent.com/88983987/219967031-a786af38-b550-43a3-8d74-1d16d685534b.png)

Sonunda profil paketimizi oluşturmak için aşağıdaki komutu çalıştırıyoruz.

```
zip $(lsb_release -i -s)_$(uname -r)_profile.zip module.dwarf /boot/System.map-$(uname -r)
```

![image](https://user-images.githubusercontent.com/88983987/219967144-1405de2a-cdb4-4ac7-a5dc-42dfbdee717b.png)

Burdan sonra oluşan zip dosyasını nasıl kendi makinenize alacağınız size kalmış, ben python3 ile http.server açarak aktarıyorum.
ifconfig ile cihazımızın ipsini öğreniyoruz.

![image](https://user-images.githubusercontent.com/88983987/219967207-619900f9-93ca-447a-a2bd-3d665d8fc2ba.png)

```
python3 -m http.server 8081
```
![image](https://user-images.githubusercontent.com/88983987/219967266-61e28a39-1136-4abd-8913-9ade4fc887e1.png)

Host makinemizde:
```
wget http://192.168.1.46:8081/Ubuntu_4.4.0-186-generic_profile.zip
```
Artık Ubuntu ile bir işimiz kalmadı, kapatabiliriz.

Host makinesine aldığımız zip dosyasını volatility içerisinde aşağıdaki gibi volatility/plugins/overlays/linux konumuna kopyalıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219967792-27559012-f712-4e06-b09d-53922ecb64da.png)

Kopyaladığımız profilin ismini öğrenmek için aşağıdaki komutu çalıştırıyoruz.
```
python vol2.py --info | grep "Linux"
```
![image](https://user-images.githubusercontent.com/88983987/219967867-9dfecbe1-3ecd-410c-8257-889a63d5dcdf.png)

Artık soruların nasıl çözüldüğüne geçebiliriz. 4. soruya kadar beklenen ve beklenmeyen çözüm türlerini paylaşacağım. Son soruda neden bunu yaptığımı anlayacaksınız.

# PVE 2 [100 pts]

**Category:** Forensics
**Solves:** 54

## Description
>Q2: What is the version of the apache server?

Files: Same as PVE 1
flag format : 0xL4ugh{*.*.*}

Author xElessaway

## Solution
Beklenen çözüm türü:

Bunu öğrenebilmek için memory imajı alınırken bu paketin kurulmuş ya da açılmış olması gerekiyor, memory içinde bir yerinin olması gerekiyor. Bu yüzden bash history içerisinde apache komutunu aratıyoruz.

```
python2 vol.py -f /home/kali/Desktop/PVE.vmem  --profile=LinuxUbuntu_4_4_0-186-generic_profilex64 linux_bash | grep "apache"
```
![image](https://user-images.githubusercontent.com/88983987/219968150-42e0b9dd-2f3e-4224-a047-8fabbc96eb83.png)

En son kurulmuş olan paketin numarasını alıyoruz.

Beklenmeyen çözüm türü:
```
strings /home/kali/Desktop/PVE.vmem | grep --text "apache" | head
```
![image](https://user-images.githubusercontent.com/88983987/219968111-40db994f-9e78-47e0-aa34-62bb2c41c7a7.png)

## Flag
0xL4ugh{2.2.14}

# PVE 3 [150 pts]

**Category:** Forensics
**Solves:** 55

## Description
>Q3: We think that there was a suspicious process can you look what is it and reterive the flag ?

Files: Same As PVE 1

Author: xElessaway

## Solution
Beklenen Çözüm:
Processlere aşağıdaki komut ile bakıyoruz.
```
python2 vol.py -f /home/kali/Desktop/PVE.vmem  --profile=LinuxUbuntu_4_4_0-186-generic_profilex64 linux_psaux 
```
5808 process no'lu DontRunMeImVirus dosyası dikkatimizi çekiyor.

![image](https://user-images.githubusercontent.com/88983987/219968693-31631658-8d22-441c-85bb-1d5151a45a4c.png)

Dosyayı almak için linux_find_file kullanacağız. Fakat bunun için dosyanın konumunu bilmemiz gerekiyor. Bize yardımcı olacak bir şey sunup sunmadığına bakmak için linux_bash komutunu çalıştırıyoruz.
```
python2 vol.py -f /home/kali/Desktop/PVE.vmem  --profile=LinuxUbuntu_4_4_0-186-generic_profilex64 linux_bash
```

![image](https://user-images.githubusercontent.com/88983987/219968780-49e5da89-ec0b-4628-8473-79e8d28a5303.png)

Bingo! Dosyanın C kodunun nerede olduğunu biliyoruz. Yapmamız gereken tek şey onu extract edip okumak. 

İlk önce linux_find_file ile offset'ini çıkarıyoruz.
```
└─$ python2 vol.py -f /home/kali/Desktop/PVE.vmem  --profile=LinuxUbuntu_4_4_0-186-generic_profilex64 linux_find_file -F /mnt/f/dontopenmenimvirus.c
Volatility Foundation Volatility Framework 2.6.1
Inode Number                  Inode File Path
---------------- ------------------ ---------
            2103 0xffff880017c68600 /mnt/f/dontopenmenimvirus.c
```
Sonrasında yine linux_find_file ile extract ediyoruz.
```
└─$ python2 vol.py -f /home/kali/Desktop/PVE.vmem  --profile=LinuxUbuntu_4_4_0-186-generic_profilex64 linux_find_file -i 0xffff880017c68600 -O virus.c
Volatility Foundation Volatility Framework 2.6.1
```
Ve dosyayı cat ile okuyoruz.
```
└─$ cat virus.c                      
#include<stdio.h>
#include <unistd.h>



int main(void){
    char flag[] = "0xL4ugh{H1DD3N_1N_PR0CE$$}";
        sleep(696969);
        return 0;
}             
```
Beklenmeyen çözüm:
```
┌──(kali㉿kali)-[~/Scripts/volatility]
└─$ strings /home/kali/Desktop/PVE.vmem | grep --text "0xL4ugh" | head
    char flag[] = "0xL4ugh{H1DD3N_1N_PR0CE$$}";
0xL4ugh{H
0xL4ugh{H1DD3N_1N_PR0CE$$}
sudo echo "0xL4ugh{S4D_Y0U_G07_M3}" > flag.txt
echo "0xL4ugh{S4D_Y0U_G07_M3}" > flag.txt
0xL4ugh{H
    char flag[] = "0xL4ugh{H1DD3N_1N_PR0CE$$}";
    char flag[] = "0xL4ugh{H1DD3N_1N_PR0CE$$}";
0xL4ugh{H
 ```                                            
## Flag
0xL4ugh{H1DD3N_1N_PR0CE$$}

# PVE 4 [100 pts]

**Category:** Forensics
**Solves:** 58

## Description
>Q4: There is something hidden in somewhere but can you find where ?

Files: Same as PVE 1

Author: xElessaway

## Solution
Bir şeyler suspect, görebiliyorum.. Bash history okumaya dönüyoruz.

Beklenen Çözüm:
```
┌──(kali㉿kali)-[~/Scripts/volatility]
└─$ python2 vol.py -f /home/kali/Desktop/PVE.vmem  --profile=LinuxUbuntu_4_4_0-186-generic_profilex64 linux_bash | head -n 20
Volatility Foundation Volatility Framework 2.6.1
Pid      Name                 Command Time                   Command
-------- -------------------- ------------------------------ -------
    1034 bash                 2023-02-15 16:33:22 UTC+0000   pwd
    1034 bash                 2023-02-15 16:33:22 UTC+0000   cat flag.txt
    1034 bash                 2023-02-15 16:33:22 UTC+0000   ls
    1034 bash                 2023-02-15 16:33:22 UTC+0000   apache2 --version
    1034 bash                 2023-02-15 16:33:22 UTC+0000   sudo apt-get install apache2
    1034 bash                 2023-02-15 16:33:22 UTC+0000   clear
    1034 bash                 2023-02-15 16:33:22 UTC+0000   ls
    1034 bash                 2023-02-15 16:33:22 UTC+0000   are you ready ?
    1034 bash                 2023-02-15 16:33:22 UTC+0000   su
    1034 bash                 2023-02-15 16:33:22 UTC+0000   echo "0xL4ugh{S4D_Y0U_G07_M3}" > flag.txt
    1034 bash                 2023-02-15 16:33:22 UTC+0000   apache2 -version
    1034 bash                 2023-02-15 16:33:22 UTC+0000   sudo apt install apache=2.4.51-1+ubuntu20.04.1+deb.sury.org+1
    1034 bash                 2023-02-15 16:33:22 UTC+0000   sudo apt-get install apache2=2.2.14-5ubuntu16.04.7
    1034 bash                 2023-02-15 16:33:22 UTC+0000   clear
    1034 bash                 2023-02-15 16:33:22 UTC+0000   sudo apt-get install apache
    1034 bash                 2023-02-15 16:33:22 UTC+0000   sudo su
    1034 bash                 2023-02-15 16:33:22 UTC+0000   ls
    1034 bash                 2023-02-15 16:33:22 UTC+0000   sudo apt install apache=2.4.51-1+ubuntu16.04.7+deb.sury.org+1
```
Beklenmeyen Çözüm:
```
┌──(kali㉿kali)-[~/Scripts/volatility]
└─$ strings /home/kali/Desktop/PVE.vmem | grep --text "0xL4ugh" | head                                             
[23dsudo echo "0xL4ugh{S4D_Y0U_G07_M3}" > flag.txt
```
## Flag
0xL4ugh{S4D_Y0U_G07_M3}

# PVE 5 [379 pts]

**Category:** Forensics
**Solves:** 12

## Description
>Q5: The attack got the password of the user but can you?

Files: Same as PVE 1

Author: xElessaway

## Solution

Bana kalırsa, en eğlenceli soru buydu. Ayrıca, neden soruları beklenen yolla yapmalısınız sorusunun cevabı niteliğindeydi. Soruda bizden bir kullanıcının parolasını istiyor. Kullanıcı paroları nerde saklanır? /etc/shadow ve /etc/passwd dosyaları. Bunları bulup extract edeceğiz. 
```
┌──(kali㉿kali)-[~/Scripts/volatility]
└─$ python2 vol.py -f /home/kali/Desktop/PVE.vmem  --profile=LinuxUbuntu_4_4_0-186-generic_profilex64 linux_find_file -F /etc/shadow
Volatility Foundation Volatility Framework 2.6.1
Inode Number                  Inode File Path
---------------- ------------------ ---------
         1044994 0xffff88001817bbf8 /etc/shadow
                                                                                                                                                                         
┌──(kali㉿kali)-[~/Scripts/volatility]
└─$ python2 vol.py -f /home/kali/Desktop/PVE.vmem  --profile=LinuxUbuntu_4_4_0-186-generic_profilex64 linux_find_file -i 0xffff88001817bbf8 -O /home/kali/Desktop/hash/shadow
Volatility Foundation Volatility Framework 2.6.1
                                                                                                                                                                         
┌──(kali㉿kali)-[~/Scripts/volatility]
└─$ python2 vol.py -f /home/kali/Desktop/PVE.vmem  --profile=LinuxUbuntu_4_4_0-186-generic_profilex64 linux_find_file -F /etc/passwd
Volatility Foundation Volatility Framework 2.6.1
Inode Number                  Inode File Path
---------------- ------------------ ---------
         1048952 0xffff88001e144468 /etc/passwd
                                                                                                                                                                         
┌──(kali㉿kali)-[~/Scripts/volatility]
└─$ python2 vol.py -f /home/kali/Desktop/PVE.vmem  --profile=LinuxUbuntu_4_4_0-186-generic_profilex64 linux_find_file -i 0xffff88001e14446  -O /home/kali/Desktop/hash/passwd
Volatility Foundation Volatility Framework 2.6.1
```

John ile kırabilmek için uygun formata getiriyoruz.

```
┌──(kali㉿kali)-[~/Desktop/hash]
└─$ unshadow passwd shadow 
```

```
┌──(kali㉿kali)-[~/Desktop/hash]
└─$ cat shadow 
root:!:19402:0:99999:7:::
daemon:*:18484:0:99999:7:::
bin:*:18484:0:99999:7:::
sys:*:18484:0:99999:7:::
sync:*:18484:0:99999:7:::
games:*:18484:0:99999:7:::
man:*:18484:0:99999:7:::
lp:*:18484:0:99999:7:::
mail:*:18484:0:99999:7:::
news:*:18484:0:99999:7:::
uucp:*:18484:0:99999:7:::
proxy:*:18484:0:99999:7:::
www-data:*:18484:0:99999:7:::
backup:*:18484:0:99999:7:::
list:*:18484:0:99999:7:::
irc:*:18484:0:99999:7:::
gnats:*:18484:0:99999:7:::
nobody:*:18484:0:99999:7:::
systemd-timesync:*:18484:0:99999:7:::
systemd-network:*:18484:0:99999:7:::
systemd-resolve:*:18484:0:99999:7:::
systemd-bus-proxy:*:18484:0:99999:7:::
syslog:*:18484:0:99999:7:::
_apt:*:18484:0:99999:7:::
messagebus:*:19402:0:99999:7:::
uuidd:*:19402:0:99999:7:::
mrx:$6$AkhWkiSy$MV4YekoydUoqhdnoJYWTHFpSWSsSTe53cTvuGNJLrE7FVMrKgDIEyyQio3ZPtnEX6524nSCenk2fYYV8mxwkL0:19404:0:99999:7:::
xElessaway:!:19403:0:99999:7:::
```
Normalde Linux üzerinde kırılabilir, fakat çok uzun sürdüğü için ben işlemi host makinem olan Windows'a aldım.

Ben daha önceden kırdığım için kırma aşaması gözükmüyor fakat hash %97 civarlarında kırılıyor. Kırarken biraz stres olmanız normal :)
```
D:\Siber Güvenlik\john-1.9.0-jumbo-1-win64\run>john.exe passwords.txt --wordlist=rockyou.txt
Warning: detected hash type "sha512crypt", but the string is also recognized as "sha512crypt-opencl"
Use the "--format=sha512crypt-opencl" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 256/256 AVX2 4x])
No password hashes left to crack (see FAQ)

D:\Siber Güvenlik\john-1.9.0-jumbo-1-win64\run>john --show passwords.txt
mrx:08041632890804163289:1000:1000:Super Mario,,,:/home/mrx:/bin/bash
```
## Flag

0xL4ugh{08041632890804163289}




