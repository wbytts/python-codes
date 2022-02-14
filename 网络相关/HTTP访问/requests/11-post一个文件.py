import requests

url = 'http://httpbin.org/post'
files = {'file': open('01-发送一个简单的get请求.py', 'rb')}

# 也可以显式地设置文件名，文件类型，请求头
# files = {'file': ('report.xls', open('report.xls', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}

r = requests.post(url, files=files)
print(r.text)


"""
如果你发送一个非常大的文件作为 multipart/form-data 请求，你可能希望将请求做成数据流。
默认下 requests 不支持, 但有个第三方包 requests-toolbelt 是支持的。
"""
