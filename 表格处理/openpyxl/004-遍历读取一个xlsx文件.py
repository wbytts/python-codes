from openpyxl import load_workbook

wb = load_workbook(r'C:\Users\hp\Desktop\okr_task_1.xlsx')
# wb = load_workbook(filename='sample.xlsx')

ws = wb.active

# 获取所有 value（生成器）
for row in ws.values:
    for value in row:
        print(value)
