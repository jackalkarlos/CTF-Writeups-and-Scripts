from PIL import Image

listem = ["b.png","l.png","e.png","n.png","d.png"]

for i in listem:
	foto = Image.open(i)
	veriler = foto.getdata()
	ascii_veriler = [chr(x) for x in veriler]
	x = ''.join(ascii_veriler)
	print(x)
