import os
# 导入tensorflow，这将导入 TensorFlow 库
import tensorflow as tf

# 用于忽略级别 2 及以下的消息（级别 1 是提示，级别 2 是警告，级别 3 是错误）
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

# 看一下tenfsorflow的版本号
print(tf.__version__)
# 定义一个常量字符串
message = tf.constant('Hello World')
# 执行计算图，利用 with 语句定义 Session，并使用 run 来运行
with tf.Session() as sess:
    print(sess.run(message).decode())
