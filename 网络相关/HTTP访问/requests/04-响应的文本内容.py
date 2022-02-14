import requests

r = requests.get('https://api.github.com/events')

print(r.text) # Requests 会自动解码来自服务器的内容。大多数 unicode 字符集都能被无缝地解码。

# 请求发出后，Requests 会基于 HTTP 头部对响应的编码作出有根据的推测。
# 当你访问 r.text 之时，Requests 会使用其推测的文本编码。
# 你可以找出 Requests 使用了什么编码，并且能够使用 r.encoding 属性来改变它
# 如果你改变了编码，每当你访问 r.text ，Request 都将会使用 r.encoding 的新值
