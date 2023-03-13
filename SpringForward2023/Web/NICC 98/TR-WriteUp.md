![image](https://user-images.githubusercontent.com/88983987/224654262-3da16842-96c6-4e5d-8c1b-a8ac226358a7.png)

## Çözüm
Siteye girdiğimizde bizi bir alert karşılıyor. Sitenin kaynak kodunu incelediğimizde alert verecek bir kod görmüyoruz ancak bir javascript dosyası var. Ayrıca "My favorite Console is the Nintendo 64" yazısı ile karşılaşıyoruz.

Sitenin kaynak kodlarından javascript dosyasına ulaşıyoruz.
```
<script type="text/javascript" language="javascript" src="js/nicc98.js"></script>
```
```
console.log("bmljY3tmbGlwX3RoM19zY3JpcHR9");
window.alert("Welcome to the web page of the NJIT Information and Cybersecurity Club!");
console.log("Alert successful.")
```
Base64 ile decode ediyoruz.

nicc{flip_th3_script}
