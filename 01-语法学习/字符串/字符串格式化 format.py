
'''
template_str.format()

占位符语法：
    { fieldname component !conversionflag :formatspec}
    fieldname：可选的数字或者关键字
    component：有这大于等于零个的 .name 或 [index] 引用的字符串，它可以被省略以使用完整的参数值。
                其中的引用值用来获取参数的属性或索引值
    conversionflag：如果出现则以 ! 开始，后面跟着 r s a，分别表示在这个值上调用 repr str ascii 内置函数
    formatspec：如果出现则以 : 开始，后面跟着文本，指定了如何表示该值，包括很多细节。
                formatspec也可以包含嵌套的只有字段名称的 {} 格式化字符串，
                它从参数列表动态地获取值（和格式化表达式中的 * 类似）
        [[fill]align][sign][#][0][width][,][.precision][typecode]
            fill：可以是除了 { 和 } 之外的任意填充字符
            align：可以是 < > = ^
                <：左对齐
                >：右对齐
                =：符号字符后的填充
                ^：居中对齐
            sign：+、-、空格
            ,逗号：表示从python2.7和python3.1开始使用的千分位分隔符
            width：最小宽度
            percision：精度
            typecode：几乎与格式化表达式 % 里使用的相同

单独的对象也可以用 format 内置函数来格式化，
在用户自定义的类中，还可以使用 __format__ 运算符重载方法来定制
format内置函数会运行主体对象的 __format__ 方法
'''
