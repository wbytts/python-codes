from openpyxl import Workbook

# 创建一个工作簿
wb = Workbook()
ws = wb.active

cell = ws['A1']

cell.value = 'Hello World'

# 将工作簿保存为一个文件
wb.save("sample.xlsx")
