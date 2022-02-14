import xlrd
# 1.1.0 之后的版本不支持 xlsx 格式了
# pip install xlrd==1.1.0

print(xlrd.__VERSION__)

# 打开 Excel 文件，叫做工作簿
wb = xlrd.open_workbook(r'D:\WeChatFiles\WeChat Files\wxid_9l1aneyw07ud22\FileStorage\File\2021-09\老OA关注数据.xlsx')
# 拿到工作表
# sheet_by_index 通过index获取sheet，从0开始
# sheet_by_name 通过sheet的名称获取sheet
sheet = wb.sheet_by_index(0)


"""
读取指定单元格的值：
   sheet.cell_value(行数, 列数)
   sheet.cell(行数, 列数).value
   sheet.row(行数)[列数].value
"""


print(sheet.cell_value(2, 3))
print(sheet.cell(2, 2).value)
# print(sheet.row(2)[2].value)

