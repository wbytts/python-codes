import openpyxl as ox

wb = ox.load_workbook('cz.xlsx')
# 以索引值的方式获取工作表
ws = wb.worksheets[0]

# 单元格数据获取方法
# 1. A1表示法    工作表['A1'] # 字母大写和小写都可以
# 2. 行列表示法  工作表.cell(行, 列)   # 这里的行列是从1开始的！
# 也可以 ws.cell('A1')、ws.cell(row=xxx, column=xxx)

for i in range(1, 100):
    for j in range(1, 20):
        cell = ws.cell(i, j)  # 获取i行j列的单元格
        print(cell.value, end='')  # 打印单元格的值
    print()
