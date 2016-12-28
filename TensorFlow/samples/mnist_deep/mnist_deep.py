# -*- coding: utf-8 -*-

print "start load data..."
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
print "end load data"

import tensorflow as tf
sess = tf.InteractiveSession() #MNIST easyのときも使ってたので、作法とする

# 学習データとしてすでにあるものはplaceholder宣言して入れる
x = tf.placeholder(tf.float32, shape=[None, 784])
y_ = tf.placeholder(tf.float32, shape=[None, 10])

# 調整パラメータはVariable
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

# Variableを全部宣言したらinitする
sess.run(tf.global_variables_initializer())

y = tf.matmul(x,W) + b

# クロスエントロピーの平均をロス関数とする
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, y_))

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

for i in range(1000):
  if i%100 == 0:
      print i
  batch = mnist.train.next_batch(100)
  train_step.run(feed_dict={x: batch[0], y_: batch[1]})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1)) #正解不正解のTrue/False配列
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
print(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels})) #=> 0.9182

# いよいよディープラーニング
# CNN

# 重み変数を作る関数
def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)

# バイアスを作る関数
def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)

# ストライドは1でたたみこむ（えっ
def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

# プーリングサイズも固定？
def max_pool_2x2(x):
  return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                        strides=[1, 2, 2, 1], padding='SAME')

# 1層目の重みとバイアス
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

# 入力を変形
x_image = tf.reshape(x, [-1,28,28,1])

# 1層の出力をreluに食わせる
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
# 結果をプーリングして微小変化に頑健にする
h_pool1 = max_pool_2x2(h_conv1)

# 第二層
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

# 1層のプーリング結果を出力として同様に。最後はrelu
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# 2x2プーリングを2回通ったので画像サイズが1/4になっている (7x7画像)

# fc = fully connected
# 今までも全結合だったのでは？
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

# こんどはそれを1024にひきのばす？

# いつものようにかけ算
h_pool2_flat = tf.reshape(h_pool2, [-1, 7*7*64]) # 7*7*64 = 3136
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# 結果を読み出す前にドロップアウトする
# ドロップアウトは、
#  訓練時ON
#  テスト時OFF
# その切り替えのためにplaceholder
keep_prob = tf.placeholder(tf.float32)
# 出力をドロップアウト関数へ
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 最後10次元に落とす
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

# 差はクロスエントロピー
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_conv, y_))
# 最適化はAdam
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
# 実際に実行
sess.run(tf.global_variables_initializer())

# 学習時間計測
import time
start = time.time()

# 学習＆識別率表示
# train_num = 20000
train_num = 500
for i in range(train_num):
  batch = mnist.train.next_batch(50) #バッチサイズがeasyのときより小さくなっている。パラメータが多いからか
  if i%100 == 0:
    train_accuracy = accuracy.eval(feed_dict={x:batch[0], y_: batch[1], keep_prob: 1.0}) #訓練時の識別率を見るときはdropoutしない
    print("step %d, training accuracy %g"%(i, train_accuracy))
  train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5}) #訓練時は半分をドロップアウト

print("test accuracy %g"%accuracy.eval(feed_dict={
    x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0}))

# 何秒かかったか
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time)) + "[sec]"

# 500step
## Mac CPU : elapsed_time:161.193413019[sec]
## Mac GPU : AMD-GPUなのでCUDA利用できず中止