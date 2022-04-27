import tensorflow as tf

'''
如果你正在使用 Jupyter Notebook 或者 Python shell 进行编程，使用 tf.InteractiveSession 将比 tf.Session 更方便。
InteractiveSession 使自己成为默认会话，因此你可以使用 eval() 直接调用运行张量对象而不用显式调用会话。
'''

sess = tf.InteractiveSession()

v1 = tf.constant([1,2,3,4])
v2 = tf.constant([2,1,5,3])

v_add = tf.add(v1, v2)

print(v_add.eval())

sess.close()