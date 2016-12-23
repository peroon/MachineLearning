# -*- coding: utf-8 -*-
import tensorflow as tf

matrix1 = tf.constant([[3., 3.]]) #行列
matrix2 = tf.constant([[2.],[2.]]) #行列
product = tf.matmul(matrix1, matrix2) #積

sess = tf.Session()# 準備
result = sess.run(product)# 実行

print(result) #=>[[12.]]
sess.close()