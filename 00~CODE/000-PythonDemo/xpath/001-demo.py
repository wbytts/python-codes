from lxml import etree
import requests

response = requests.get("http://www.baidu.com")
data = response.content.decode("utf-8")

# 1. 抓解析类型
xpath_data = etree.HTML(data)

# xpath语法
"""
1. 节点 /
2. 跨节点 //x[xxx="xxx"]
3. 下标从1开始，且下标只能取平级标签
"""

# 2. 调用xpath的方法
result = xpath_data.xpath("/html/head/title/text()")
print(result)
result = xpath_data.xpath("//a/text()")
print(result)
result = xpath_data.xpath("//a/@href")
print(result)

