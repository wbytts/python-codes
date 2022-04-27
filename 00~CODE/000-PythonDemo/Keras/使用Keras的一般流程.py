'''
使用Keras的一般流程：
    导入Keras
    定义模型
    编译模型
    训练模型
    评估模型
    保存模型
'''

from tensorflow import keras
import os

# 使用 GPU版本时 忽略 CPU 的 AVX 警告
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
'''
在定义模型时我们有两种选择，
    一是使用keras.models.Sequential()方法定义次序模型，这种方法定义的模型将会从头到尾依次执行，
    二是使用函数式API定义更加灵活的高级模型
'''

x_train = []
y_train = []

# 实例化一个次序模型
model = keras.models.Sequential()

# 使用model.add方法添加隐层
# model.add(···)
# model.add(···)

# 编译模型
# 在编译操作中，我们需要定义模型使用的优化方法，损失函数，评估模型的指标等
model.compile(loss=keras.losses.mean_squared_error,
              optimizer=keras.optimizers.Adam(0.01),
              metrics=['accuracy'])

# 训练模型
# 在这里可以指定批处理数、训练的世代数等参数
model.fit(x_train, y_train, batch_size=10, epochs=5)

# 评估模型
# 同样可以指定批处理数等参数
model.evaluate(x=None,
               y=None,
               batch_size=None,
               verbose=1,
               sample_weight=None,
               steps=None)

# 保存模型
# 模型训练完成之后，我们使用model.save()方法来保存模型
# 最终模型会被保存为h5格式的文件
model.save('model.h5')
