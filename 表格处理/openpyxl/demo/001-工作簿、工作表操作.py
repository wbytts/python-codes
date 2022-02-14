from openpyxl import Workbook

# 创建一个工作簿对象
wb = Workbook()

# 获取工作簿对象中活动的工作表
ws = wb.active

# 获取工作簿下所有工作表的名称列表
sheetname_list = wb.sheetnames
print(sheetname_list)

# 创建一个工作表
wb.create_sheet('一个工作表')  # 不写索引表示添加在最后，写-1表示添加在最前面

# 修改工作表的标题
ws.title = '测试一下，修改标题'

# 修改工作表，标签颜色
ws.sheet_properties.tabColor = "1072BA"
# ws.sheet_properties.xxx 其他属性可以自己探索一下

# 通过工作簿获取工作表
# wb['工作表名称']

print('-' * 50)
# 工作簿对象 wb 是一个可迭代对象
for sheet in wb:
    print(sheet.title)


# 拷贝工作表
target = wb.copy_worksheet(ws)

# 保存工作簿
wb.save(r'f:\data\excel\test.xlsx')
