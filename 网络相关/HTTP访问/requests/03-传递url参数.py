import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print(r.url)  # 打印URL，发现URL已经被编码了（值为None的键不会被编码到URL中）
