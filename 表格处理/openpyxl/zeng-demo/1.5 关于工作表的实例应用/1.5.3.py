import openpyxl
wb=openpyxl.load_workbook('模板.xlsx')
for m in range(1,13):
    wb.copy_worksheet(wb['000']).title='%d月'%m
wb.remove(wb['000'])
wb.save('2018年各月表格.xlsx')
