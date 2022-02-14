import openpyxl
wb=openpyxl.load_workbook('demo.xlsx',data_only=True)
ws=wb.active
# print([[c.value for c in row] for row in ws['a1:d3']])
print(list(ws.values)[1:4])
