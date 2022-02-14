"""
copy_worksheet 在Workbook内拷贝表格
"""

import openpyxl as ox

wb = ox.load_workbook('cz.xlsx')

ws_copy = wb.copy_worksheet(wb['Sheet1'])

wb.save('cz.xlsx')