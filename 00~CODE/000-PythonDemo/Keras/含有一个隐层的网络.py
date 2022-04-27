from tensorflow import keras
from keras.utils import plot_model
import numpy as np

import os

# 使用 GPU版本时 忽略 CPU 的 AVX 警告
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

x_train = np.random.rand(10000, 2)
y_train = 3 * x_train[:, 0] + 2 * x_train[:, 1] + 1
print(y_train.shape)

model = keras.models.Sequential()
# 使用add方法添加隐层
model.add(
    keras.layers.Dense(512, activation='sigmoid', input_dim=2, use_bias=True))

model.add(keras.layers.Dense(1, activation='sigmoid', use_bias=True))
# 编译模型
model.compile(loss=keras.losses.mean_squared_error,
              optimizer=keras.optimizers.Adam(0.01),
              metrics=['accuracy'])
# 训练模型
model.fit(x_train, y_train, batch_size=10)
# 输出：
