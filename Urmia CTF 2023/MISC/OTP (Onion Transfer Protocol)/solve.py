#I hated this chall lol bcs i waited 4 hours for flag :D. Just run "dir" on ftp and take list of files. Format it with cyberchef. It should be like this:
#line1
#line2
#line3
#
#And run this script (i did!)

import socket
import socks
import re

tor_proxy_host = '127.0.0.1'  # Tor proxy'nin çalıştığı localhost IP adresi
tor_proxy_port = 9050  # Tor proxy'nin portu

target_host = 'otpxxwpvfjume6kdlii5gcghgg53lj7gnl7hoigg4sx2wc45xwasw7id.onion'
target_port = 21  # Bağlanmak istediğiniz hedef port numarası (21: FTP örneği)

# Tor proxy üzerinden bağlantı kurma
sock = socks.socksocket()
sock.set_proxy(socks.SOCKS5, tor_proxy_host, tor_proxy_port)
sock.connect((target_host, target_port))

response = sock.recv(4096)
print(f'{response.decode("utf-8")}')

user= "USER myuser\r\n".encode()
passw= "PASS mypass\r\n".encode()
sock.send(user)
response= sock.recv(4096)
print(response)

sock.send(passw)
response = sock.recv(4096)
print(response)


regex = r"\d+"
epsvmsg="EPSV\r\n".encode()
sock.send(epsvmsg)
response=sock.recv(4096)
response=response.decode("latin-1")
sayilar = re.findall(regex, response)
portmumble = int(sayilar[1])

with open("text.txt","r") as dosyaliste:
        dosyaliste=dosyaliste.read().split("\n")

for i in dosyaliste:
        retr_command = f"CWD {i}\r\n"
        sock.send(retr_command.encode())
        response= sock.recv(4096)

        retr_command= f"RETR flag.txt\r\n"
        sock.send(retr_command.encode())

        sock2 = socks.socksocket()
        sock2.set_proxy(socks.SOCKS5, tor_proxy_host, tor_proxy_port)
        sock2.connect((target_host,portmumble))
        print(sock2.recv(4096).decode())
        sock2.close()


        response=sock.recv(4096)
        response_code = int(response[:3])

        cdup_command = "CDUP\r\n"
        sock.send(cdup_command.encode())
        response=sock.recv(4096)
sock.close()
