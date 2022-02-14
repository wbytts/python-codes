import csv
import json

# 创建文件对象
json_fp = open('list.json')
csv_fp = open('list.csv', 'w')

# 读取 json 内容
data_list = json.load(json_fp)
print(data_list)

# 获取标题
sheet_title = list(data_list[0].keys())
print(sheet_title)
sheet_data = []
for data in data_list:
    sheet_data.append(data.values())

# csv 写入器
writer = csv.writer(csv_fp)

# 写入表头
writer.writerow(sheet_title)

# 写入内容
writer.writerows(sheet_data)

# 关闭两个文件
json_fp.close()
csv_fp.close()