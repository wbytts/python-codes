import xlwt

# 新建一个工作簿
new_wb = xlwt.Workbook()
# 向工作簿中添加一个工作表
worksheet = new_wb.add_sheet('test-sheet')
# 向工作表中写入内容
worksheet.write(1, 1, 'ASD')
# 将工作簿进行保存
new_wb.save('f:/temp/test.xls')
