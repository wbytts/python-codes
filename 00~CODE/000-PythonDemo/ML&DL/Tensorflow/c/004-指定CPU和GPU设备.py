import tensorflow as tf

config = tf.ConfigProto(log_device_placement=True)

# 手动选择CPU进行操作
with tf.device('/cpu:0'):
    msg = tf.constant('hello')

sess = tf.Session(config)

print(sess.run(msg))