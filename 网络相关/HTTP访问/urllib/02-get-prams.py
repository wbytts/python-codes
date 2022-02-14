import urllib.request
import urllib.parse
import string


def get_method_params(wd):
    url = "http://www.baidu.com/s?wd="
    # 拼接字符串
    final_url = url + wd
    # 将包含汉字的网址进行转义
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    # 发送网络请求
    response = urllib.request.urlopen(encode_new_url)
    print(response.read().decode("utf-8"))


get_method_params("美女")
