from keras.layers.core import Dense, Activation  # 层次，激活函数
from keras.models import Sequential  # 神经网络
import pandas as pd  # 数据处理

import os

# 使用 GPU版本时 忽略 CPU 的 AVX 警告
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

path = r"F:\project\PythonDemo\Keras\data\model.xls"
data = pd.read_excel(path)

# data = data.as_matrix()  # 数组
data = data.values  # 新版本中使用 values 来代替 as_matrix
print(data)

p = 0.8  # 80%数据训练，20%的数据预测
train = data[:int(len(data) * p), :]  # 训练问题
test = data[int(len(data) * p):, :]  # 测试

net = Sequential()  # 构造神经网络

#  keras 新版本中 Dense参数名 output_dim 用 units
net.add(Dense(input_dim=3, units=14))  # 输入层，3个节点，14中间节点
net.add(Activation("relu"))  # 激活神经网络

net.add(Dense(input_dim=14, units=18))  # 输入层，3个节点，14中间节点
net.add(Activation("relu"))  # 激活神经网络

net.add(Dense(input_dim=18, units=1))  # 输入层，3个节点，14中间节点
net.add(Activation("sigmoid"))  # i外层输出

net.compile(
    loss="binary_crossentropy",
    optimizer="adam",
)  # 编译神经网络，加速方式
# 1  0.3,0.4 0.5 0.99

# 训练
net.fit(train[:, :3], train[:, 3], epochs=1000, batch_size=1)

last = net.predict_classes(train[:, :3]).reshape(len(train))

# 计算准确率
print((last == train[:, 3]).sum() / len(last))  # 精确率
# 0.9137931034482759
# 0.9353448275862069
