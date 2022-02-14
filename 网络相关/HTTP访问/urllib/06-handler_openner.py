import urllib.request


def handler_openner():
    # urllib.request.urlopen()
    # 点进去看urlopen的源码可以知道，系统的urlopen并没有添加代理的功能，所以需要我们自定义这个功能

    # 安全套接层：SSL，第三方的CA数字证书
    # http与https的一个区别，http是80端口，https是443端口

    # urlopen为什么可以请求数据
    # 根据源码可以看出，是由于 openner，而openner又由handler而来

    url = "http://www.baidu.com"
    # 创建自己的处理器
    handler = urllib.request.HTTPHandler()
    # 创建自己的openner
    openner = urllib.request.build_opener(handler)
    # 用openner去请求
    response = openner.open(url)
    print(response.read().decode("utf-8"))


handler_openner()
