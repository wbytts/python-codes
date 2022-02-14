import openpyxl

wb = openpyxl.load_workbook(r'cz.xlsx')

"""
其他属性：
    ws.read_only：判断是否以read_only模式打开Excel文档
    encoding：获取文档的字符编码集
    properties：获取文档的其他一些属性
    sheetnames：获取工作簿中的工作表名组成的列表
"""