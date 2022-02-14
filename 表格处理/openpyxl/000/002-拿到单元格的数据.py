

"""
直接访问一个单元格：ws['A4']
修改一个单元格内容：ws['A4'] = 3
通过方法访问一个单元格：ws.cell(row=3, column=4)
通过方法设置单元格的值：ws.cell(row=3, column=4, value=666)
"""

# 注：在内存中创建工作表时，它不包含“单元格”。它们是第一次访问时创建的。
# 由于这个特性，滚动单元格而不是直接访问单元格将在内存中创建所有单元格，即使您没有给它们赋值。

"""
访问多个单元格：
    通过切片访问单元格区域：ws['A1' : 'C2']
    单独指定行或者列的范围：ws['C']、ws['C:D']、ws[10]、ws[5:10]
    使用迭代器：ws.iter_rows()、ws.iter_cols()
    ws.rows、ws.columns
    ws.values 返回所有行，但只返回单元格值（iter_row之类的也可以设置values_only来只返回单元格值）

注：
    出于性能原因
    ws.iter_cols()在只读模式下不可用
    ws.columns在只读模式下不可用
"""

"""
拿到单元格对象之后，Cell，我们就可以给它赋值
c.value = 'hello world'
"""
