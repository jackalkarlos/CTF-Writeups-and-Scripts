![image](https://user-images.githubusercontent.com/88983987/224676198-f4eac382-9389-4938-a47b-2f81570b6b42.png)

## Solution

İlk baktığımda bunun bir tür şifreleme ya da encoding olduğunu düşündüm. Hexahue'ye çok benziyordu. Bir çok yöntem denedim fakat işe yaramadı. En sonunda RGB kanallarına veri saklanabilen bir method olduğunu hatırladım. Bunu çözmek için "StegSolve-1.4.jar" aracını kullandım.
```
┌──(root㉿kali)-[/home/kali/Scripts]
└─# java -jar StegSolve-1.4.jar          
```

![image](https://user-images.githubusercontent.com/88983987/224677792-17448a92-917d-48ec-bb5d-7f3a3238bd0e.png)

Aşağı kaydırırken bazı kelime parçaları görüyoruz.

![image](https://user-images.githubusercontent.com/88983987/224677954-c407f0f8-d403-4083-b42b-4540f24ca00d.png)
```
"Nev"

"er"

"Gon"

"na"
```

Google üzerinde aratıyoruz.

![image](https://user-images.githubusercontent.com/88983987/224678247-e7455440-285d-4334-a9d2-bf9da1eab0f4.png)

Soruyu hatırlayın. "Who wrote this?"

nicc{Rick_Astley}

