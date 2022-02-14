import requests

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

"""
注意: 定制 header 的优先级低于某些特定的信息源，例如：
    如果在 .netrc 中设置了用户认证信息，使用 headers= 设置的授权就不会生效。而如果设置了 auth= 参数，``.netrc`` 的设置就无效了。
    如果被重定向到别的主机，授权 header 就会被删除。
    代理授权 header 会被 URL 中提供的代理身份覆盖掉。
    在我们能判断内容长度的情况下，header 的 Content-Length 会被改写。

Requests 不会基于定制 header 的具体情况改变自己的行为。只不过在最后的请求中，所有的 header 信息都会被传递进去
所有的 header 值必须是 string、bytestring 或者 unicode。尽管传递 unicode header 也是允许的，但不建议这样做。
"""
