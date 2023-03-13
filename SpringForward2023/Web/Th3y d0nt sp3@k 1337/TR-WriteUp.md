![image](https://user-images.githubusercontent.com/88983987/224655668-7edbccc3-a492-4850-b62a-baf1f22c0377.png)

## Solution
Bu soru, NICC 98 sorusunu çözdükten sonra açılıyor, dolayısıyla bağlantılı sorular. Soru metninde "make sure we stop robots from crawling around where they don't belong." şeklinde bir kısım var.

Arama motorlarının robotlarının sitede gezinmesini kontrol altına almak için robots.txt dosyasını kullanırız. Muhtemelen leet ile ilgili bir muhabbet olduğu için r0b0ts.txt dosyasına ulaşmamızı isteyecek. İki ihtimali de deniyoruz.

robots.txt
```
User-Agent: *
Disallow: /
# Hey - make sure to change the user-agent
# What you put here doesn't work! Robots aren't speaking 1337, they just want to go to this page (robots.txt)!
# Example: 
# User-Agent: dangr0b0ts
# Disallow: /r0b0ts.txt
```
r0b0ts.txt
```
nicc{@lw@ys_ch3ck_4_r0b0ts}
```

nicc{@lw@ys_ch3ck_4_r0b0ts}

