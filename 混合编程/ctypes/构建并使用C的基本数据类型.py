
from ctypes import *
msvcrt = cdll.msvcrt

# 构建并使用 C 数据类型
i = c_int(9) # 构造C语言的int类型，并初始化为9
print(i)
print(i.value)

i.value = 1212
print(i.value)

str_cp = c_char_p(b"learn python ctypes")   # 构造C语言的char类型，字符串类型
print(str_cp)
print(str_cp.value)

str_cp = c_wchar_p("hello python")  # 构造C语言的宽字符类型，宽字符串类型
print(str_cp)
print(str_cp.value)

'''
常见的对应关系：
    ctypes py类型检查     C/C++ py类型检查                               python类型
    c_bool          _Bool                                    bool
    c_char          char                                     string
    c_wchar         wchar_t                                  string
    c_byte          char                                     int
    c_ubyte         unsiged char                             int
    c_short         short                                    int
    c_unshort       unsigned short                           int
    c_int           int                                      int
    c_uint          unsigned int                             int
    c_long          long                                     int
    c_ulong         unsigned long                            int
    c_longlong      __int64 或 long long                     int
    c_ulonglong     unsigned __int64 或 unsigned long long   int
    c_float         float                                    float
    c_double        double                                   float
    c_longdouble    long double                              float
    c_char_p        char *  ;(NUL terminated)                string   或None
    c_wchar_p       wchar_t * ;(NUL terminated)              string   或None
    c_void_p        void *                                   int      或None

    注：Python 中的类型，除了 None，int， long， Byte String，Unicode String 作为 C 函数的参数默认提供转换外，其它类型都必须显式提供转换
    None：对应 C 中的 NULL
    int,long： 对应 C 中的 int，具体实现时会根据机器字长自动适配。
    特别需要注意的是,在python3中:
    Byte String：对应 C 中的一个字符串指针 char * ，指向一块内存区域。(字符串前面会加小b, b"helloworld")
    Unicode String：对应 C 中一个宽字符串指针 wchar_t *，指向一块内存区域。(对应的就是字符串, "helloworld")
    在python2中恰好相反.

'''
