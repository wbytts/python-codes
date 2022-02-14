import pickle

m = [1, 2, 3, 4, 5]

# 将 Python 对象序列化为二进制串
# pickle.dumps(对象) -> 二进制串
res = pickle.dumps(m)
print(res)

# 将二进制串加载为对象，这里的二进制串一定要是 pickle.dumps 返回的才可以
# pickle(二进制串) -> 对象
read_m = pickle.loads(res)
print(read_m)
