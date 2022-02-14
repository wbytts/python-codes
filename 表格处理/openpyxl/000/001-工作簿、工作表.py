from openpyxl import Workbook, load_workbook

# 创建工作表对象
wb = Workbook()

"""
还可以从文件加载：
wb2 = load_workbook('test.xlsx')
"""

# 在Excel工作簿中至少包含一个工作表，可以通过 workbook.active 来获取当前活动的工作表
ws = wb.active

# 在默认情况下，活动工作表总被设置为0。可修改
# 还可以创建新的工作表
ws1 = wb.create_sheet('s1')  # 在末尾插入
ws2 = wb.create_sheet('s2', 0)  # 在第一个位置插入
ws3 = wb.create_sheet('s3', -1)  # 在开头

# 新建表的时候将自动按数字命名，并可以通过 ws.title 来修改工作表名称
ws1.title = '啦啦啦'

# 默认情况下，选项卡的背景是白色，可以将 RRGGBB 值赋给 ws.sheet_properties.tabColor 属性来改变颜色
ws1.sheet_properties.tabColor = 'FF0000'


# 获取工作表的几种方式
# 1. wb.active 获取当前活动的工作表
# 2. wb[工作表名]  通过工作表的名称获取工作表


# wb.sheetnames 获取一个工作表的名称列表

# 复制工作表
# wb.copy_worksheet(ws)


# 保存工作簿
# 此操作将覆盖现有文件而不发出警告
# 文件扩展名不必是xlsx或xlsm，但如果不使用正式扩展名，则可能在使用其他应用程序直接打开文件时遇到一些问题。
# 由于OOXML文件基本上是ZIP文件，因此您还可以使用您喜爱的ZIP压缩文档管理器打开它。
wb.save(r'f:/temp/excel/a.xlsx')
