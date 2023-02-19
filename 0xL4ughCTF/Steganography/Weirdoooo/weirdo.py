with open('dosya.txt', 'r') as dosya:
	icerik = dosya.read()
for i in range(1,256):
	icerik=icerik.replace(str(i),'■')
icerik=icerik.replace("0 ","    ")

with open('dosya2.txt', 'w') as dosya:
    dosya.write(icerik)
