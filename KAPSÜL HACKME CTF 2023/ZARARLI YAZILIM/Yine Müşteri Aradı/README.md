## Description
> Soruda paylaşılan virüs dosyası PyInstaller ile paketlenmişti. Pyinstxtractor kullanarak paketi ayrıştırdık. Sonrasında uncompyle6 kullanarak kaynak kodlarını elde ettik. Kaynak kodları şu şekilde.
```
# uncompyle6 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: 1001010110111101111110010101010010101.py
import random as r, string, datetime as g1011011001010101001010101011101010101010101, uuid, requests
from Crypto.Cipher import AES as a
from Crypto.Util.Padding import pad
import os, subprocess as v

def a1011011001010101001010101011101010101010101(f1011011001010101001010101011101010101010101, h1011011001010101001010101011101010101010101, x1011011001010101001010101011101010101010101):
    command = f'reg add "{f1011011001010101001010101011101010101010101}" /v "{h1011011001010101001010101011101010101010101}" /d "{x1011011001010101001010101011101010101010101}" /f'
    v.run(command, shell=True)


def b1011011001010101001010101011101010101010101(file_path, y10101010101010100110101010101010111110001010):
    y10101010101010100110101010101010111110001010 = y10101010101010100110101010101010111110001010.encode('utf-8')
    y10101010101010100110101010101010111110001010 = y10101010101010100110101010101010111110001010[:32].ljust(32, b'\x00')
    iv = os.urandom(16)
    cipher = a.new(y10101010101010100110101010101010111110001010, a.MODE_CBC, iv)
    with open(file_path, 'rb') as (file):
        plaintext = file.read()
    ciphertext = cipher.encrypt(pad(plaintext, a.block_size))
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as (file):
        file.write(iv + ciphertext)
    print('Dosya şifreleme tamamlandı. Şifreli dosya: ', encrypted_file_path)


def d1011011001010101001010101011101010101010101(seed):
    r.seed(seed)
    key_length = r.randint(5, 10)
    y10101010101010100110101010101010111110001010 = ''.join((r.choice(string.ascii_lowercase) for _ in range(key_length)))
    return y10101010101010100110101010101010111110001010


def d1011011001010101001010101011101010101010101s(num_keys):
    keys = []
    seed = g1011011001010101001010101011101010101010101.datetime.now().strftime('%Y%m%d%H%M%S')
    for _ in range(num_keys):
        y10101010101010100110101010101010111110001010 = d1011011001010101001010101011101010101010101(seed)
        keys.append(y10101010101010100110101010101010111110001010)
        seed = y10101010101010100110101010101010111110001010

    return keys


def main():
    f1011011001010101001010101011101010101010101 = 'HKEY_CURRENT_USER\\Software\\HACKME_HATIRA'
    h1011011001010101001010101011101010101010101 = 'HACKME!'
    x1011011001010101001010101011101010101010101 = 'Bu !zararsız! dosyayı kendi bilgisayarımda çalıştırdığım için özür dilerim. Bir daha böyle !zararsız! dosyaları kendi bilgisayarımda çalıştırmayacağım ;)'
    try:
        a1011011001010101001010101011101010101010101(f1011011001010101001010101011101010101010101, h1011011001010101001010101011101010101010101, x1011011001010101001010101011101010101010101)
    except:
        pass

    num_keys = 1
    keys = d1011011001010101001010101011101010101010101s(num_keys)
    file_path = 'fffxxssdaxdas.hackme'
    y10101010101010100110101010101010111110001010 = str(keys[0])
    b1011011001010101001010101011101010101010101(file_path, y10101010101010100110101010101010111110001010)


if __name__ == '__main__':
    choice = int(input('Merhaba, bu dosyayı kendi bilgisayarında çalıştırmamalıydın. Sana ufak bir hatıra bıraktım ;) Yine de kendi bilgisayarında çalıştırmaya devam etmek istersen 1 yaz ve gönder:\n'))
    if choice == 1:
        main()
# okay decompiling 1001010110111101111110010101010010101.pyc
```

Virüs dosyayı AES ile şifreliyor. IV olarak 16 bytelik random bir değer kullanıyor ve bunu dosyanın ilk 16 byte'sına yazıyor. Dosyanın geri kalan kısmı da şifrelenmiş dosyayı içeriyor.

```
  iv = os.urandom(16)
    cipher = a.new(y10101010101010100110101010101010111110001010, a.MODE_CBC, iv)
    with open(file_path, 'rb') as (file):
        plaintext = file.read()
    ciphertext = cipher.encrypt(pad(plaintext, a.block_size))
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as (file):
        file.write(iv + ciphertext)
```

Key değeri saniyelik değere göre üretiliyor. Dosyanın dakikasal değiştirilme tarihine göre bir dakika içindeki 60 saniyenin üretebileceği tüm seed ihtimallerini hesapladım. 
Değiştirilme tarihi: 22.05.2023 01:41

Çözüm scripti aşağıdaki gibidir:

## Solution


```
import string
import random
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import datetime

def generate_key(seed):
    random.seed(seed)
    key_length = random.randint(5, 10)
    key = ''.join(random.choice(string.ascii_lowercase) for _ in range(key_length))
    return key


def decrypt_file(file_path, seed):
    key = generate_key(seed)
    key = key.encode('utf-8')
    key = key.ljust(32, b'\x00')
    iv_size = 16
    with open(file_path, 'rb') as file:
        ciphertext = file.read()
    iv = ciphertext[:iv_size]
    ciphertext = ciphertext[iv_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
    decrypted_file_path = file_path + '.decrypted'
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)
    print('çözdüm he: ', decrypted_file_path)


seed_list = ['202305220141{:02d}'.format(second) for second in range(60)]

for seed in seed_list:
    try:
        decrypt_file("fffxxssdaxdas.hackme.encrypted", seed)
    except:
        pass
```
