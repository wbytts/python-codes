
'''
当在函数中使用未限定的变量名时，python将查找四个作用域并在第一次找到该变量名的地方停下来
    首先是，局部作用域 L
    其次是向外一层的def或lambda的局部作用域 E
    之后是全局作用域 G
    最后是内置作用域 B
    如果最终没找到，则会报错
'''
