# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np

# Create 100 phony x, y data points in NumPy, y = x * 0.1 + 0.3
# デフォルトだとfloat64
# randで0-1の間からの乱数
# 100はリスト幅
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

# TFの変数はデフォルトでfloat32
# 整数を入れたらint32
# 最適化され更新されていく変数はVariable宣言する
# W, bはテンソルとよばれる多次元行列になる
# 初期値について、Wは乱数を使っているけど、bは0なのはなぜだろう？？
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = W * x_data + b

# Minimize the mean squared errors.
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# Before starting, initialize the variables.  We will 'run' this first.
init = tf.global_variables_initializer()

# Launch the graph.
sess = tf.Session()
sess.run(init)

# Fit the line.
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))

# Learns best fit is W: [0.1], b: [0.3]
