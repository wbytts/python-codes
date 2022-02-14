import urllib.request
import urllib.parse

post_url = 'http://fanyi.baidu.com/sug'
word = input('请输入你要查询的英文单词:')

form_data = {
    'kw': word
}

headers = {
        "User-Agent": "User-Agent,Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }

# 处理post表单数据
form_data = urllib.parse.urlencode(form_data).encode()
request = urllib.request.Request(url=post_url, headers=headers)

response = urllib.request.urlopen(request, data=form_data)

print(response.read().decode())

