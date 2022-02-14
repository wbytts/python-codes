import hashlib

# 固定加盐
md5 = hashlib.md5('学习'.encode('utf-8'))  # 学习就是固定的盐
md5.update('a'.encode('utf-8'))
print(md5.hexdigest())
