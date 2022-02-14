import requests

# 默认情况下，除了 HEAD, Requests 会自动处理所有重定向
# 可以使用响应对象的 history 方法来追踪重定向。
# Response.history 是一个 Response 对象的列表，为了完成请求而创建了这些对象。这个对象列表按照从最老到最近的请求进行排序。

# 如果你使用的是GET、OPTIONS、POST、PUT、PATCH 或者 DELETE，那么你可以通过 allow_redirects 参数禁用重定向处理

# 如果你使用了 HEAD，你也可以启用重定向
# r = requests.head('http://github.com', allow_redirects=True)
