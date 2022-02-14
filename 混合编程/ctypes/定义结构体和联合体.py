from ctypes import *

msvcrt = cdll.msvcrt


# 使用 python 定义 C语言的结构体
class color_rgb(Structure):
    """
    ctypes.Structure C语言结构体的Python封装类
    python类继承 ctypes.Structure，C类型.结构体
    _fields_ 定义结构体字段   [(字段名称, 字段类型), .....]
    同：
        struct color_rgb
        {
            char r;
            char g;
            char b;
        }
    """
    _fields_ = [
        ('r', c_char),
        ('g', c_char),
        ('b', c_char),
    ]


color = color_rgb()
color.r = 123
color.g = 234
color.b = 222

print(ord(color.b))

color = color_rgb(111, 222, 121)
print(ord(color.b))


# 使用python 定义联合体（共用体）
class barley(Union):
    '''
    python类继承 ctypes.Union
    _fields_ 定义联合体字段 [(字段名称, 字段类型), .....]
    '''
    _fields_ = [
        ("barley_long", c_long),
        ("barley_int", c_int),
        ("barley_char", c_char * 8)
    ]


val = input("Enter the amount of barley:")
bar = barley(int(val))
print(bar.barley_long, bar.barley_int, bar.barley_char)
