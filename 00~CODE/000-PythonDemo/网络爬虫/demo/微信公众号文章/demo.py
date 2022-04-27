import re

with open(r"C:\Users\hp\Desktop\PROJECT\PythonDemo\008-网络爬虫\demo\微信公众号文章\66F8.txt", "r", encoding="utf-8") as f:
    all = f.read()
    res = re.findall("hrefs=\"http://mp\.weixin\.qq\.com/s(.*?)\"", all)
    link_list = []
    for item in res:
       link_list.append("hrefs=\"http://mp\.weixin\.qq\.com/s" + item)

with open("link-list.txt", "w", encoding="utf-8") as f:
    for i in link_list:
        f.writelines(i)