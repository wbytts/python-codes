# 导入tensorflow，这将导入 TensorFlow 库
import tensorflow as tf
# 看一下tenfsorflow的版本号
print(tf.__version__)
# 定义一个常量字符串
message = tf.constant('Hello World')
# 执行计算图，利用 with 语句定义 Session，并使用 run 来运行
# with tf.Session() as sess:
#     print(sess.run(message).decode())

sess = tf.Session()
print(sess.run(message))
sess.close()

'''
前面的代码分为以下三个主要部分：
第一部分 import 模块包含代码将使用的所有库，在目前的代码中只使用 TensorFlow，其中语句 import tensorflow as tf 则允许 Python 访问 TensorFlow 所有的类、方法和符号。
第二个模块包含图形定义部分...创建想要的计算图。在本例中计算图只有一个节点，tensor 常量消息由字符串“Welcome to the exciting world of Deep Neural Networks”构成。
第三个模块是通过会话执行计算图，这部分使用 with 关键字创建了会话，最后在会话中执行以上计算图。
'''

