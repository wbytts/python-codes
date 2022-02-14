import openpyxl as ox

wb = ox.load_workbook('cz.xlsx')

ws1 = wb.create_sheet() #默认插在工作簿末尾
ws2 = wb.create_sheet('工作表asd')  # 创建的时候可以指定名字
ws3 = wb.create_sheet('工作表33', 2) # 创建的时候，也可以指定工作表的位置（-1表示插入到第一个位置之前）

# 在创建工作表的时候系统自动命名。他们按照序列依次命名 (Sheet, Sheet1, Sheet2, ...)。
# 可以手动修改工作表的名称 （使用 title 属性）
ws1.title = "第一个工作表"

# 标签栏的背景色默认为白色。你可以通过提供一个RRGGBB颜色码改变标签栏的字体颜色
ws1.sheet_properties.tabColor = "1072BA"

# 一旦你获取工作表的名字，你可以通过workbook的key，
# 或者openpyxl.workbook.Workbook.get_sheet_by_name()方法获取工作表

# 获取工作簿的所有工作表的名字
names = wb.get_sheet_names()

# 可以直接循环工作簿，得到工作表
for sheet in wb:
    print(sheet)
