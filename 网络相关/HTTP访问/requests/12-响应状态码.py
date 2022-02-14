import requests

r = requests.get('http://httpbin.org/get')
print(r.status_code)
print(r.status_code == requests.codes.ok)


# 如果有错误，可以用 bad_r.raise_for_status() 抛出异常
r.raise_for_status()

# 查看响应头
print(r.headers)
