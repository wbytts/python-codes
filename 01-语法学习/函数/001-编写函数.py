
'''
def 是可执行的代码
def 创建了一个对象并将其赋值给一个变量名（函数对象 -> 函数名）
函数也是一个对象，函数也可以携带任意的用户自定义属性，从而记录数据

lambda 创建一个对象，并将其作为结果返回
return 将一个结果对象传回给调用者
yield 向调用者发回一个结果对象，但是会记住它离开的位置

global 声明了一个模块级的可被赋值的变量：
    默认情况下，所有在一个函数中被赋值的对象都是这个函数的局部变量，并且仅在这个函数运行的过程中存在
    为了给一个外层模块中的变量赋值，函数需要在global语句中声明它

nolocal 声明了一个需要被赋值的外层函数变量
    允许一个函数对一个在其外层的def语句作用域中已有的名称进行赋值
    也就是说，同一函数在不同次的调用之间可以不必借助全局变量而存储信息

参数是通过赋值（对象引用）传递给函数的
除非显式指明形式参数与实际参数的对应，否则实际参数按位置赋值给形式参数
参数、返回值等不需要被声明
'''
