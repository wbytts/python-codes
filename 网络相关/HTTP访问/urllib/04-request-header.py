import urllib.request
from faker import Faker
from bs4 import BeautifulSoup

# 用于生成浏览器的 User-Agent
faker = Faker('zh_CN')


def load_baidu():
    url = "http://www.baidu.com"

    request_headers = {
        "User-Agent": faker.chrome()
    }

    # 创建请求对象
    request = urllib.request.Request(url, headers=request_headers)
    # 请求网络数据
    response = urllib.request.urlopen(request)

    # 请求头
    print(request.headers)

    # 响应头
    # print(response.headers)

    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, 'lxml')
    img_tags = soup('img')
    for img_tag in img_tags:
        print(img_tag.attrs['src'])


load_baidu()
