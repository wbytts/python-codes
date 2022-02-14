import tkinter as tk
from tkinter import ttk
import sympy as sp

# 让程序美化输出
sp.init_printing(use_unicode=True, pretty_print=True)

# 定义海伦公式
a, b, c = sp.symbols('a b c')
p = (a + b + c) / 2
hailun = sp.sqrt(p * (p - a) * (p - b) * (p - c))

x = float(input("x="))
y = float(input("y="))
z = float(input("z="))

# 求值
sp.pprint(hailun.subs([(a, sp.Rational(x)), (b, sp.Rational(y)), (c, sp.Rational(z))]))
