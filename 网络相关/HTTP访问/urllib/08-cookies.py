import urllib.request

url = "需要cookie验证才能访问的链接"

headers = {
    'User-Agent': 'User-Agent,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    "Cookie": 'xxx手动粘贴cookie到这里'
}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

data = response.read()

with open("data.html", "wb") as f:
    f.write(data)

