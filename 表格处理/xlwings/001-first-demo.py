import xlwings as xw

print(xw.__path__)
print(xw.__version__)

# 建立Excel表连接
# 也可以不指定工作表地址，直接与电脑中的活动表格进行交互，使用 xw.Range('A1').value 之类的
# wb = xw.Book()  # 这将创建一个新的工作簿
# wb = xw.Book('FileName.xlsx')  # 连接到当前工作目录中的现有文件
# wb = xw.Book(r'C:\path\to\file.xlsx')  # 在Windows上：使用原始字符串来转义反斜杠
wb = xw.Book(r"C:\Users\hp\Desktop\risk\baseinfo.xls")
# 实例化工作表对象
sht = wb.sheets["baseinfo"]

# 工作表的绝对路径
print(wb.fullname)
# 工作簿的名字
print(sht.name)

# 在单元格中写入数据
sht.range('A1').value = "xlwings"

# 读取单元格内容
v = sht.range('A1').value
print(v)
sht.range('A1').value = "ID"

# 清除单元格的内容和样式
sht.range('A1').clear()

# 获取单元格的列标
print(sht.range('A1').column)
# 获取单元格的行标
print(sht.range('A1').row)

# 获取单元格的行高
print(sht.range('A1').row_height)
# 获取单元格的列宽
print(sht.range('A1').column_width)

# 列宽自适应
sht.range('A1').columns.autofit()
# 行高自适应
sht.range('A1').rows.autofit()

# 给单元格上背景色
sht.range('A1').color = (34, 139, 34)
# 获取单元格的背景色
print(sht.range('A1').color)
# 清除单元格的颜色
sht.range('A1').color = None

# 输入公式，相应单元格会出现计算结果
sht.range('A1').formula = '=SUM(B6:B7)'
# 获取单元格的公式
print(sht.range('A1').formula_array)

# 在单元格中批量写入数据，只需要指定起始的单元格即可
sht.range('A2').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]

# 读取表中批量数据，使用expand()方法
print(sht.range('A2').expand().value)
