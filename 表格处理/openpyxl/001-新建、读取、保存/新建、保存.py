from openpyxl import Workbook

wb = Workbook()
sheet = wb.active
sheet['A1'] = 'Hello World'

for i in range(10):
    wb.create_sheet('sheet'+str(i), i+3)

wb.save(f'f:\data\excel\我的工作簿.xlsx')

# 每个工作簿创建完之后，默认会存在一个工作表worksheet，也可以自行创建新的工作表


