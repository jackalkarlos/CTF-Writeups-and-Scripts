![image](https://user-images.githubusercontent.com/88983987/224642493-0d3e6fcf-693d-47c3-8b79-387b2491f057.png)

## Solution

We are looking encrypt.py and log.txt.

log.txt
```
SWYgeW91J3JlIHJlYWRpbmcgdGhpcywgeW91IGJldHRlciBiZSBtZS4KTW9zdCBsaWtlbHkgeW91IGZvcmdvdCwgdGhhdCB0aW1lIGlzIHRoZSBrZXkuCg==
mpq_wxkdim_qe_WTNQ
tvp euaapnbqpr vafhlk abtx ogwi aaif qr xxeg qe


072923373661312c3f2d66273661276537203f652429232b73352f283661312c3f2d6627362f22653124202a2124663c3c346a65322f22652a2e3365302028653b242a357334352d363366313b2835653a2f68653d28252628297529231e2b760c7124740c36062b2e6f661c3c3466282632326520282b353f3866233c2d2a2a2461322d36613624272966233c3366203d2d2f223b35232b3e2428317d616b1711
```

encrypt.py
```
def encrypt(message, key):
    encrypted = ""
    for i in range(len(message)):
        encrypted += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return encrypted.encode("utf-8").hex()

message = #//////ERROR ERROR ERROR
key = #/////// ERROR OERROR ERROR ERROR
encrypted = encrypt(message,key)
```

It is looking this code doing xor function and converting hex. We note aside. In the question it says we only have half of the program. Trying a manual decode first lines.

First line is Base64.

![image](https://user-images.githubusercontent.com/88983987/224643303-f88bc7b8-c992-4d2d-988f-d3043094c5ec.png)

It is saying "time" is key. Trying decrypting second line with vigenere and "time" key. 

![image](https://user-images.githubusercontent.com/88983987/224643536-07193dcd-b75c-4bcb-a071-3a2c6f719432.png)

It is saying key is "safe". Lets try decode it with time third line before trying safe. 

![image](https://user-images.githubusercontent.com/88983987/224643741-2e64163e-7b6c-41e4-8cd1-809d1a56e7a8.png)

Let convert hex to text last line and xor with safe.

<a href="https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'UTF8','string':'SAFE'%7D,'Standard',false)&input=MDcyOTIzMzczNjYxMzEyYzNmMmQ2NjI3MzY2MTI3NjUzNzIwM2Y2NTI0MjkyMzJiNzMzNTJmMjgzNjYxMzEyYzNmMmQ2NjI3MzYyZjIyNjUzMTI0MjAyYTIxMjQ2NjNjM2MzNDZhNjUzMjJmMjI2NTJhMmUzMzY1MzAyMDI4NjUzYjI0MmEzNTczMzQzNTJkMzYzMzY2MzEzYjI4MzU2NTNhMmY2ODY1M2QyODI1MjYyODI5NzUyOTIzMWUyYjc2MGM3MTI0NzQwYzM2MDYyYjJlNmY2NjFjM2MzNDY2MjgyNjMyMzI2NTIwMjgyYjM1M2YzODY2MjMzYzJkMmEyYTI0NjEzMjJkMzY2MTM2MjQyNzI5NjYyMzNjMzM2NjIwM2QyZDJmMjIzYjM1MjMyYjNlMjQyODMxN2Q2MTZiMTcxMQ">Cyber Chef Recipe</a>

![image](https://user-images.githubusercontent.com/88983987/224644069-9bf584e1-aabe-43ad-961d-7a1f3c29c5f8.png)

nicc{h3lp_m3_0b1_w@n}


