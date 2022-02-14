import openpyxl
wb=openpyxl.load_workbook('test.xlsx')
ws=wb.active
rngs=ws['a2:e71']
print(['%s-%d'%(row[0].value,sum([c.value for c in row][1:])) for row in rngs])