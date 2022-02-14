# file: demo.pyx
from libc.math cimport sin
from libc.stdlib cimport atof

def foo(char *s):
    x = atof(s)
    return sin(x)

print(foo("3.1415"))  # 答案约等于0
