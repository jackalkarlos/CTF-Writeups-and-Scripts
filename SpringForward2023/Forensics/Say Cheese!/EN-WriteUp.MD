![image](https://user-images.githubusercontent.com/88983987/224647456-a6398643-152f-4717-9204-7e3a6c2a0fb8.png)

## Solution

"Can you find out what the make and model of the device used to take the selfie was?"

We need find out device type and model. We can extract metadata with exiftool.

```
┌──(kali㉿kali)-[~/Desktop]
└─$ exiftool Selfie.jpg 
ExifTool Version Number         : 12.56
File Name                       : Selfie.jpg
Directory                       : .
File Size                       : 46 kB
File Modification Date/Time     : 2023:03:11 05:31:43+03:00
File Access Date/Time           : 2023:03:11 05:31:43+03:00
File Inode Change Date/Time     : 2023:03:11 05:31:43+03:00
File Permissions                : -rw-rw-rw-
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Exif Byte Order                 : Little-endian (Intel, II)
Make                            : Security Camera
Camera Model Name               : Kmart Special
Image Width                     : 589
Image Height                    : 733
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 589x733
Megapixels                      : 0.432
```

nicc{Securiy_Camera_Kmart_Special}
