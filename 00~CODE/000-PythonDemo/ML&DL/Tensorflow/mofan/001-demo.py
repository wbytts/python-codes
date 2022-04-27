import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# 开始创建结构
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))  # 权重，随机生成一个
biases = tf.Variable(tf.zeros_like(tf.constant([1]))) # 偏置
y = Weights * x_data + biases
# 计算 loss, 预测的y和实际的 y_data 的差别
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
# 初始化
init = tf.initialize_all_variables()

# 激活
sess = tf.Session()
sess.run(init)

