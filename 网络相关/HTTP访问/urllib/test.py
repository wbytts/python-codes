import urllib.request


def create_proxy_handler(ip):
    url = "http://www.baidu.com"

    proxy = {
        # 免费的写法
        "http": "http://" + ip
    }

    # 代理的处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)

    # 创建自己的openner
    openner = urllib.request.build_opener(proxy_handler)
    # 拿着代理ip去发送请求
    try:
        response = openner.open(url, timeout=20)
        print(ip, '有效')
    except:
        print(ip, '无效')

    # print(response.read().decode("utf-8"))



create_proxy_handler('193.242.151.44:8080')
