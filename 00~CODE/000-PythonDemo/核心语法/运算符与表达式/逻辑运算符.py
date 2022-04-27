"""

not A    非(一元)：真变假，假变真
A and B  与(二元)：两边都为真，才是真，否则为假
A or  B  或(二元)：两边都为假，才是假，否则为真


and 和 or 其实没有优先级，只是简单的从左到右进行运算

非布尔类型值的真假：
    一般是 非零即真、非空即真
"""

print("not True    \t===>\t", not True)
print("not False    \t===>\t", not False)

print("True and True\t===>\t", True and True)
print("True and False\t===>\t", True and False)
print("False and True\t===>\t", False and True)
print("False and False\t===>\t", False and False)

print("True or True\t===>\t", True or True)
print("True or False\t===>\t", True or False)
print("False or True\t===>\t", False or True)
print("False or False\t===>\t", False or False)

