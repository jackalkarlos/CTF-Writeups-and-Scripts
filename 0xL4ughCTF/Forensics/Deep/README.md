# Deep [185 pts]

**Category:** Forensics
**Solves:** 20

## Description
>One of the companies called you to investigate a suspicious computer system. You need to use your skills to find out what happened. they tried to get you a part of the partition so can you find out the secret behind that attack?

Download: https://drive.google.com/file/d/1wzJv11RyrqwLP6UI3rrGMOLlKEchuj1N/view?usp=sharing


Author: xElessaway

#### Hint 

## Solution

İndirdiğimiz zip dosyasını normal bir arşiv programı ile açtığımızda bunun bir disk imajı olabileceğini görüyoruz.

![image](https://user-images.githubusercontent.com/88983987/219961841-8152732f-1889-4f0d-b5e5-d98a8c714e2f.png)

Gizli dosya olması ihtimaline karşı mantıksal olarak değil fiziksel olarak okumak için dosyayı FTK Imager ile açıyoruz. Belki de ihtiyaç yoktur ama ben emin olmak istedim.

![image](https://user-images.githubusercontent.com/88983987/219961873-cd82d4cd-62b5-419c-8029-807e32e29d50.png)

![image](https://user-images.githubusercontent.com/88983987/219961890-60e7eb81-a967-491e-a534-e3d52b6e29e7.png)

![image](https://user-images.githubusercontent.com/88983987/219961917-20fefbae-8b3f-4fa3-a14c-a05d77882794.png)

Burdan sonrası dosyaları detaylıca incelemek oluyor. Fazla dosya olmadığı için tek tek incelerken "developer" kullanıcısının powershell geçmişine denk geliyorum.
```
/Users/developer/AppData/Roaming/Microsoft/Windows/PowerShell/PSReadLine/ConsoleHost_history.txt
```
![image](https://user-images.githubusercontent.com/88983987/219962120-9f6e9bd0-5d85-41c6-b864-4809ecdcad82.png)

Dosyayı okurken, bir metni "0x06" hex'i ile xor'ladığını görüyoruz.

![image](https://user-images.githubusercontent.com/88983987/219962265-827ef173-c2b8-429c-8e03-3dce71d90050.png)

CyberChef is your friend.

![image](https://user-images.githubusercontent.com/88983987/219962291-92c92dd9-30d3-499d-95bd-892c09a0b31e.png)

## Flag

0xL4ugh{Y0u_AR3_G0OD_1NV3571G70R}
