from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws['A1'] = '姓名'


ws.cell(row=4, column=2, value=10)

for i in range(1, 100):
    for j in range(1, 100):
        ws.cell(row=i, column=j, value=i + j)

# 获取一个区域
cell_range = ws['A1':'C2']

colC = ws['C']
col_range = ws['C:D']
row10 = ws[10]
row_range = ws[5:10]

# 先遍历行，再遍历列
for row in ws.iter_rows(min_row=1, max_col=3, max_row=2):
    for cell in row:
        print(cell)

# 先遍历列，再遍历行
for col in ws.iter_cols(min_row=1, max_col=3, max_row=2):
    for cell in col:
        print(cell)

# 获取所有行，所有列（生成器）
rows = ws.rows
print(rows)
columns = ws.columns
print(columns)

# 获取所有 value（生成器）
print(ws.values)
for row in ws.values:
    for value in row:
        print(value)

for row in ws.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
    print(row)

wb.save('sample.xlsx')
