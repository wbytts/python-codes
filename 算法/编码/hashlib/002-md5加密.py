import hashlib
md5 = hashlib.md5()   # 初始MD5
md5.update("加密内容".encode('UTF-8'))   #放内容，编码集可随意
print(md5.hexdigest())		# 合成 输出

'''
其他方法，字节较长，算法越高，转化成的结果越复杂，安全程度越高，相应的效率就会越低。
# 最常用的是md5，平时加密的时候sha1
'''
