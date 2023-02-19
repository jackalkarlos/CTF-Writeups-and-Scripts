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





