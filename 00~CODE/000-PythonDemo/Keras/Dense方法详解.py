'''
Dense 是 Keras定义网络层的基本方法

keras.layers.Dense(units, # 该层有几个神经元
				  activation=None, # 该层使用的激活函数
				  use_bias=True, # 是否添加偏置项
				  kernel_initializer='glorot_uniform', # 权重初始化方法
				  bias_initializer='zeros', # 偏置值初始化方法
				  kernel_regularizer=None, # 权重规范化函数
				  bias_regularizer=None, # 偏置值规范化方法
			      activity_regularizer=None, # 输出的规范化方法
				  kernel_constraint=None, # 权重变化限制函数
				  bias_constraint=None # 偏置值变化限制函数
				  )

'''

from tensorflow import keras

# 举例
# 这里定义了一个有512个节点，使用sigmoid激活函数的神经层
keras.layers.Dense(512, activation='sigmoid', input_dim=2, use_bias=True)
