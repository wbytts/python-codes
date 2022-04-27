'''
Tensor 张量
支持的数据类型:
    tf.float16 半精度浮点数
    tf.float32 单精度浮点数
    tf.float64 双精度浮点数
    tf.bfloat16 截短浮点数
    tf.int8 8位有符号整数
    tf.int16 16位有符号整数
    tf.int32 32位有符号整数
    tf.int64 64为有符号整数
    tf.uint8 8位无符号整数
    tf.string 字符串
    tf.bool 布尔值
    tf.complex64 单精度复数
    tf.complex128 双精度复数
    tf.qint8 量化的8位有符号数
    tf.qint16 量化的16位有符号数
    tf.qint32 量化的32位有符号数
    tf.quint8 量化的8位无符号数
    tf.quint16 量化的16为无符号数

张量的属性：
    dtype：张量传输数据的类型
    name：张量在数据流图中的名称
    graph：张量所属的数据流图
    op：生成该张量的前置操作
    shape：张量传输数据的形状
    value_index：张量在该前置

张量的方法：
    eval：获取张量的值
    get_shape：获取张量的形状
    set_shape：修改张量的形状
    consumers：获取张量的后置操作

一元代数操作：
    abs、negative
二元代数操作：
    add、multiply、matmul、subtract

稀疏张量：SparseTensor
'''

import tensorflow as tf
# a,b一阶常张量
a = tf.constant(1.0)
b = tf.constant(2.0)
# c = a + b
c = tf.add(a, b)
print(a, b, c)

########################################

a = tf.constant(1.0, name = 'a')
b = tf.constant(2.0, name = 'b')
c = tf.add(a, b)
with tf.Session() as sess:
    print(c.eval())
    print(sess.run([a, b, c]))

########################################

a = tf.constant([[1, 2, 3], [4, 5, 6]], name = 'a')
b = tf.constant([[7, 8, 9], [10, 11, 12]], name = 'b')
c = tf.add(a, b)
with tf.Session() as sess:
    # 获取形状
    print(a.get_shape())
    # 获取后置操作
    print(a.consumers())
    # 取出张量值
    print(a.eval())

############################################
a = tf.constant([[-1, -2, -3], [4, 5, 6]], name = 'a')
b = tf.constant([[7, 8, 9], [10, 11, 12]], name = 'b')
c = tf.constant([[7, 8], [9, 10], [11, 12]], name = 'c')
# 对应元素相加
d = tf.add(a, b)
# 对应元素相减
f = tf.subtract(a, b)
# 对应元素相乘
e = tf.multiply(a, b)
# 矩阵相乘
g = tf.matmul(b, c)
with tf.Session() as sess:
    print(sess.run(d))
    print(sess.run(e))
    print(sess.run(f))
    print(sess.run(g))
    # 获取绝对值
    print(sess.run(tf.abs(a)))
    # 数据取相反数
    print(sess.run(tf.negative(a)))
    # 取出张量值
    print(a.eval())

# 稀疏张量
sp = tf.SparseTensor(indices = [[0, 2], [1, 3]], values = [1, 2], dense_shape = [3, 4])
with tf.Session() as sess:
    print(sp.eval())