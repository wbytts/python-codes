from tensorflow import keras

# 定义模型
model = keras.Sequential()
model.add(keras.layers.Dense(784, input_dim=784, kernel_initializer='normal', activation= 'tanh'))
model.add(keras.layers.Dense(512, kernel_initializer='normal', activation= 'tanh'))
model.add(keras.layers.Dense(512, kernel_initializer='normal', activation= 'tanh'))
model.add(keras.layers.Dense(10, kernel_initializer='normal', activation= 'softmax'))

# 编译模型
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# 拟合模型
model.fit(x_train, y_train, epochs=10, batch_size=200, verbose=1)
