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
