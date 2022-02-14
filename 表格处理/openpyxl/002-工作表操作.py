from openpyxl import Workbook

wb = Workbook()

# 工作簿始终至少创建一个工作表
# 获取活动工作表
ws = wb.active
# 设置工作表的标题
ws.title = "New Title"

# 创建指定标题的工作表
ws1 = wb.create_sheet("Mysheet")
ws2 = wb.create_sheet("Mysheet", 0)  # 在
ws3 = wb.create_sheet("Mysheet", -1)  # 在倒数第二个位置插入

# 通过标题获取单个工作表
ws4 = wb["New Title"]
# 获取工作表列表
print(wb.sheetnames)
# 或者直接遍历工作簿也可以的
for sheet in wb:
    print(sheet.title)


# 复制工作表
target = wb.copy_worksheet(ws)

# 工作表属性操作
# 工作表选项卡的颜色
ws.sheet_properties.tabColor = 'FF0000'

wb.save('sample.xlsx')
