![image](https://user-images.githubusercontent.com/88983987/224654262-3da16842-96c6-4e5d-8c1b-a8ac226358a7.png)

## Solution
When we enter the site, an alert welcomes us. When we examine the source code of the site, we do not see any code to alert, but there is a javascript file. In addition, we encounter the text "My favorite Console is the Nintendo 64".

We access the javascript file from the source codes of the site.
```
<script type="text/javascript" language="javascript" src="js/nicc98.js"></script>
```
```
console.log("bmljY3tmbGlwX3RoM19zY3JpcHR9");
window.alert("Welcome to the web page of the NJIT Information and Cybersecurity Club!");
console.log("Alert successful.")
```
Decode with base64.

nicc{flip_th3_script}
