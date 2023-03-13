![image](https://user-images.githubusercontent.com/88983987/224648669-5a941b0d-d2d0-4aaa-afdc-4bd748f41443.png)

## Solution

When trying to open photo, it is not opening. "file" command is cant identify the file. 
```
┌──(kali㉿kali)-[~/Desktop]
└─$ file Image2.jpg
Image2.jpg: data
```

Let check magic bytes.

![image](https://user-images.githubusercontent.com/88983987/224649301-1b5a6f81-99cc-490e-a2ad-3a2222123530.png)

Typical JPG header should be "FF D8 FF E0 00 10 4A 46 49 46 00 01".

Resource: https://en.wikipedia.org/wiki/List_of_file_signatures

![image](https://user-images.githubusercontent.com/88983987/224649474-25a8f3dc-b635-4bcf-b2a4-5bd0188bb38f.png)

Fix and save it.

![image](https://user-images.githubusercontent.com/88983987/224649703-dee22fb1-be62-4836-9b4b-05d3d047311a.png)

nicc{F0rensics_M@gic_Byt3$!}
