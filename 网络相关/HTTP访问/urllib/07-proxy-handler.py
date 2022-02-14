import urllib.request


def create_proxy_handler():
    url = "http://www.baidu.com"

    proxy = {
        # 免费的写法
        "http": "http://36.27.28.215:9999"
    }

    # 代理的处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)

    # 创建自己的openner
    openner = urllib.request.build_opener(proxy_handler)
    # 拿着代理ip去发送请求
    response = openner.open(url)

    print(response.read().decode("utf-8"))



create_proxy_handler()
