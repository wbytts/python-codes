import requests

# 会话对象让你能够跨请求保持某些参数。它也会在同一个 Session 实例发出的所有请求之间保持 cookie
# 所以如果你向同一主机发送多个请求，底层的 TCP 连接将会被重用，从而带来显著的性能提升。

s = requests.Session()
# 可以提供缺省数据，这些数据在发送请求时会和参数合并
s.auth = ('user', 'pass')
s.headers.update({'x-test': 'true'})

r = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
print(r.text)
