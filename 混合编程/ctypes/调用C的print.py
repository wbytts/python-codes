'''
直接从 C 库中调用 printf()函数打印一条消息，Windows 中的 C 库
位于 C:\WINDOWS\system32\msvcrt.dll，Linux 中的 C 库位于/lib/libc.so.6
'''

# 将 ctypes 中的名字引入
from ctypes import *  # @UnusedWildImport
# 打印windows 32位动态链接库的信息
print(windll.kernel32)
# 加载C库的动态链接文件
msvcrt = cdll.msvcrt
# 打印信息
print(msvcrt)
# 打印库中的 printf 函数信息
print(msvcrt.printf)
# 调用C语言的 printf 函数打印字符串
msg_str = b"Hello world!\n"
msvcrt.printf(b"Testing: %s", msg_str)
# 强制刷新缓冲区，立即输出，
# 若无此句，会导致下面的python语句输出结束了才输出下面的字符串
msvcrt.fflush(0)
