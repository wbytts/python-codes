import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)  #读取数据
#x为训练图像占位符，y为图片标签
x = tf.placeholder(tf.float32, [None, 784])
y_label = tf.placeholder(tf.float32, [None, 10])
#将单张图片从784维向量重新还原成28*28的矩阵图片,-1表示形状第一维的大小是由x自动确定的
x_image = tf.reshape(x, [-1, 28, 28, 1])

#第一层卷积
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1],padding='SAME')

def max_pool_2X2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1],
                          padding='SAME')
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2X2(h_conv1)
#第二层卷积
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2X2(h_conv2)

#全连接层
W_fc1 = weight_variable([7*7*64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)
#使用dropout,keep_prop是一个占位符，训练时为0.5，测试时为1
keep_prop = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prop)

W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.matmul(h_fc1, W_fc2) + b_fc2

#不采用softmax计算交叉熵的方法
#采用
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y_label, logits=y_conv))
#定义train_step
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

#定义测试的准确率
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_label, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#创建session,对变量初始化
sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

#训练2000步
for i in range(1500):
    batch = mnist.train.next_batch(50)
    #每100步报告一次准确率
    if i%100 == 0:
        train_accuracy = accuracy.eval(feed_dict={
            x: batch[0], y_label: batch[1], keep_prop: 1.0})
        print('step %d , training accuracy %.2f'%(i, train_accuracy))
    train_step.run(feed_dict={
            x: batch[0], y_label: batch[1], keep_prop: 0.2})
#print('test accuracy %.3f'%accuracy.eval(feed_dict={
#    x: mnist.test.images, y_label: mnist.test.labels, keep_prop: 1.0}))
print('test accuracy %.2f'%accuracy.eval(feed_dict={
    x: mnist.test.images[0: 2000], y_label: mnist.test.labels[0: 2000], keep_prop: 1.0}))



