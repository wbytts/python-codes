import requests

r = requests.get('https://api.github.com/events')
print(r.json()) # 如果 JSON 解码失败， r.json() 就会抛出一个异常。

"""
成功调用 r.json() 并**不**意味着响应的成功。
有的服务器会在失败的响应中包含一个 JSON 对象（比如 HTTP 500 的错误细节）。
这种 JSON 会被解码返回。
要检查请求是否成功，请使用 r.raise_for_status() 或者检查 r.status_code 是否和你的期望相同。
"""
