![image](https://user-images.githubusercontent.com/88983987/224651527-a17bc092-dbf5-4fef-bb51-565ffeda0856.png)

## Solution

.htaccess file looking like this
```
secret/.htaccess
            RewriteEngine On
            RewriteCond %{THE_REQUEST} flag
            RewriteRule ".*" "-" [F]
```

It is making filtering on request. If we can encode the "flag" word, we can access the file. Let make research for URL encoding.

https://www.w3schools.com/tags/ref_urlencode.ASP

Burp Suite can make this encoding for fast.

![image](https://user-images.githubusercontent.com/88983987/224652662-3b745dc4-2ac0-4f20-8214-9c85114af231.png)

![image](https://user-images.githubusercontent.com/88983987/224652718-16e4ddcf-f729-40b6-b6ef-35f49d688352.png)

![image](https://user-images.githubusercontent.com/88983987/224653064-806174f9-b37f-4179-9e17-db26892f6c59.png)

nicc{UrL_ENC0DED_STR1NgS_AR3_SC@ry}

