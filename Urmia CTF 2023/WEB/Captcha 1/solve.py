import re
import requests
from PIL import Image
import pytesseract
import io
import base64

s = requests.Session()
url = "https://captcha1.uctf.ir/"

while True:
        r = s.get(url)
        pattern = r'data:image\/\w+;base64,([^"]+)'
        match = re.search(pattern, r.text)
        image_data = base64.b64decode(match.group(1))
        image = Image.open(io.BytesIO(image_data))
        ocr_text = pytesseract.image_to_string(image)
        print(r.text)
        print(s.cookies.get_dict())
        sendit=s.post(url,data={'captcha':ocr_text})
