import openpyxl as opx

import sys
sys.path.append(r"D:\projects\Python\CommonPyCode")


wb = opx.Workbook()
ws = wb.active

# 直接通过 工作表['B4'] 的形式访问单元格数据（获取值，设置值）
ws['B4'] = 'Hello World'

# 通过 cell 方法获取单元格
c = ws.cell(row=1, column=1, value='#')

# 用 cell 方法获取表格，不指定 value ，会把值覆盖吗？  不会！
# 如果 cell 方法不指定 value 参数，则是获取而不修改
c2 = ws.cell(row=4, column=2)
print(c2)


wb.save(r'f:\data\excel\test.xlsx')

