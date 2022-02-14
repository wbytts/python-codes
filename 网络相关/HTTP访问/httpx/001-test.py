import httpx

url = 'http://www.baidu.com'
res = httpx.get(url)
print(res.text)

