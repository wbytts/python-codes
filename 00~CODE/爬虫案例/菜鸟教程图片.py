import requests
import re
import base64

url = 'https://www.runoob.com/'
response = requests.get(url)

html_text = response.content.decode('utf8')
base6_imgs = re.findall(r'<img .* src="(.*?)">', html_text)

count = 0
for img_b64 in base6_imgs:
    if img_b64.startswith('data'):
        imgdata = base64.b64decode(img_b64.split(',')[1])
        with open('f:/temp/cainiao/' + str(count) + '.png', 'wb') as f:
            f.write(imgdata)
            count += 1
    else:
        print(img_b64)
