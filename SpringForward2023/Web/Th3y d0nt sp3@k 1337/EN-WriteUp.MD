![image](https://user-images.githubusercontent.com/88983987/224655668-7edbccc3-a492-4850-b62a-baf1f22c0377.png)

## Solution
This question opens after solving the NICC 98 question. There is text in the question: "make sure we stop robots from crawling around where they don't belong."

We using the robots.txt file to control the crawling of search engines' robots on the site. It will probably ask us to reach the r0b0ts.txt file because there is a conversation about leet. We try both possibilities.

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

