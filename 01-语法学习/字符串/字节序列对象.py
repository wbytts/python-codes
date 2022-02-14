
B = bytearray(b'spam')
print(B)
B.extend(b'xyz')
print(B)
s = B.decode()
print(s)

'''
bytearray支持文本的原位置转换，但仅仅适用于字符编码至多8位宽（如ASCII），其他所有的字符串依然是不可变的
bytearray融合了不可变的字节字符串（它所用的 b... 语法在py3中是必须的，在2.x中是可选的）和可变列表两者的特性

bytearray是bytes的一个可修改的变体
'''
