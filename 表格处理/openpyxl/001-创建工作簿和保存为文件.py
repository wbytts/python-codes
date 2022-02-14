import openpyxl as ox

# 创建一个工作簿
wb = ox.Workbook()

# 工作簿始终至少创建一个工作表
# 获取活动工作表
ws = wb.active

# 设置一个单元格的内容
ws['A1'] = 42

# 将工作簿保存为一个文件
wb.save("sample.xlsx")


