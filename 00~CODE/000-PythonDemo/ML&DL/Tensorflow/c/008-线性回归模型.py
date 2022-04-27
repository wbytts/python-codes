import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
# 设定学习率
learning_rate = 0.0001
# 训练迭代次数
train_steps = 10000
# 构造训练数据
train_X = np.array(
    [[3.3], [4.4], [5.5], [6.71], [6.93], [4.168], [9.799], [6.182], [7.59],
     [2.167], [7.042], [10.791], [5.313], [7.997], [5.654], [9.27], [3.1]],
    dtype=np.float32)
train_Y = np.array(
    [[1.7], [2.76], [2.09], [3.19], [1.694], [1.573], [3.366], [2.596], [2.53],
     [1.221], [2.827], [3.465], [1.65], [2.904], [2.42], [2.94], [1.3]],
    dtype=np.float32)
# 输入数据
X = tf.placeholder(tf.float32, [None, 1])
Y_ = tf.placeholder(tf.float32, [None, 1])
# 定义模型参数
w = tf.Variable(tf.random_normal([1, 1]), name="weight")
b = tf.Variable(tf.zeros([1]), name="bias")
# 构建模型Y = weight*X + bias
Y = tf.add(tf.matmul(X, w), b)
# 定义损失函数
loss = tf.reduce_sum(tf.pow((Y - Y_), 2)) / 17
# 选择随机梯度下降算法
train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
# 创建会话进行训练
with tf.Session() as sess:
    # 数据初始化
    sess.run(tf.global_variables_initializer())
    # 开始训练
    print("Start training!")
    # 训练1000次
    for i in range(0, 100000):
        sess.run(train_op, feed_dict={X: train_X, Y_: train_Y})
        # 每迭代10次，计算一次损失
        if i % 10 == 0:
            c = sess.run(loss, feed_dict={X: train_X, Y_: train_Y})
            print("Step:%d, loss = %.4f, w = %.4f, b = %.4f" %
                  (i, c, sess.run(w), sess.run(b)))
    final_loss = sess.run(loss, feed_dict={X: train_X, Y_: train_Y})
    weight, bias = sess.run([w, b])
    print("Step:%d, loss = %.4f, w = %.4f, b = %.4f" %
          (i, c, sess.run(w), sess.run(b)))
    print("Linear Regression Model: Y = %.4f*X + %.4f" % (weight, bias))
    # 绘制学得的模型直线
    plt.plot(train_X, train_Y, 'ro', label="Training data")
    plt.plot(train_X, weight * train_X + bias, label="Fitted line")
    plt.legend()
    plt.show()
