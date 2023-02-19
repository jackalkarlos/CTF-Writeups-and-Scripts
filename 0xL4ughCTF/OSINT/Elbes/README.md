# El Bes [308 pts]

**Category:** Osint
**Solves:** 17

## Description
>"Hamada elbes" is a wanted cyber  criminal that escaped from police 
can u know where is he escaping ?

Author : abdoghazy<br>
Flag: 0xL4ugh{Country_City_IPoftheevidence}

#### Hint
* the twitter account supposed to appear when u search for him idk the reason for some people didn't get the account when then search by his name 


but anyway guys u can use this username : "7amada_Elbes"

## Solution

Aslında hesabı ilk başta suçlunun hesabını Twitter'da aratarak bulmamız gerekiyordu. Fakat hesap bazı ülkelerde hala arama sonuçlarında indexlenmemişti. Türkiye'de buna dahildi. VPN açarak hesabı buldum fakat 5 dakika sonrasında hint olarak kullanıcı adı yayınlandı :) 

7amada_Elbes hesabını Twitter üzerinde aratıyoruz.

Kullanıcının Mısır'da olduğu bilgisine ulaşıyoruz. Bunu not edip, kenara yazıyoruz. 
![image](https://user-images.githubusercontent.com/88983987/219948118-c7737e19-4cdf-4490-9695-4d0190f2998c.png)

Daha sonrasında kullanıcının attığı bir tweet ile karşılaşıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219948183-63acfc95-b263-4e29-8343-4ec2d2f60fb7.png)

Resimde maalesef hiçbir detay okunmuyordu. Kullanıcının Mısır'da olduğu bilgisine ulaştığımızı hatırlıyoruz, Mısır üzerindeki sokak kameralarını internet üzerinden aratıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219948245-40c45984-ba44-4a0d-8596-e0bdeb5fa55d.png)

İkinci sayfada bir kameranın birebir aynı olduğunu farkediyoruz. Tıklatıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219948467-1dfc53d8-6518-4454-ace3-a8b0373c2537.png)

Alt kısımda Suez şehrinde olduğu yazıyor. Not ediyoruz.

![image](https://user-images.githubusercontent.com/88983987/219948533-23b63b80-98d0-4f49-81bc-f8a0d09466bb.png)

IP adresini almak için kamera üstüne 1 kez tıklıyoruz.

![image](https://user-images.githubusercontent.com/88983987/219948560-ca80aa4c-b9c6-46c5-97f1-91973e3c288b.png)


## Flag

0xL4ugh{Egypt_Suez_197.166.232.101}
