import requests
r = requests.get('https://api.github.com/events')
print(r.content) # Requests 会自动为你解码 gzip 和 deflate 传输编码的响应数据。
