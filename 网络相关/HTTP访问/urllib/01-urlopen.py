import urllib.request

url = "http://www.baidu.com"
response = urllib.request.urlopen(url=url)

"""
response
    read()：读取的是二进制内容
    geturl()：获取请求的url
    getheaders()：获取头部信息
    getcode()：获取状态码
    readlines()：获取内容行组成的列表，字节类型
"""

data = response.read()
# print(data)
# 默认拿到的是二进制的数据
# 将获取的二进制内容转换成字符串
str_data = data.decode("utf-8")
print(str_data)
with open("baidu.html", "w", encoding="utf-8") as f:
    f.write(str_data)




