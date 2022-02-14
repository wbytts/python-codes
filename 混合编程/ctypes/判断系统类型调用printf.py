import platform
from ctypes import *

if platform.system() == 'Windows':
    libc = cdll.LoadLibrary('msvcrt.dll')
elif platform.system() == 'Linux':
    libc = cdll.LoadLibrary(b'libc.so.6')

libc.printf(b'Hello world!\n')
