import openpyxl
wb=openpyxl.load_workbook('000.xlsx')
ws=wb.worksheets[0]
print(ws['b1'].value)
print(ws.cell(1,2).value)
print(openpyxl.load_workbook('000.xlsx').worksheets[0]['b1'].value)
