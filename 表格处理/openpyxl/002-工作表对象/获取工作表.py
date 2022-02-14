import openpyxl as ox

wb = ox.load_workbook('cz.xlsx')

# 获取当前活动的工作表
sht1 = wb.active

# 以索引值的方式获取工作表
# wb.worksheets 以列表形式返回所有的WorkSheet
sht2 = wb.worksheets[0]

# 以工作表名获取
sht3 = wb['Sheet1']

# 循环工作表
for ws in wb.worksheets:
    print(ws)

# 获取所有工作表名
sheet_names = wb.sheetnames

# 获取指定工作表名
sht1_title = sht1.title
# 也可以修改工作表名
sht1.title = '123123123'

wb.save('cz-res.xlsx')

