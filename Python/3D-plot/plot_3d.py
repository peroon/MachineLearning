# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from scipy import genfromtxt

#データ
data = np.array([
        [  80,  85, 100 ],
        [  96, 100, 100 ],
        [  54,  83,  98 ],
        [  80,  98,  98 ],
        [  90,  92,  91 ],
        [  84,  78,  82 ],
        [  79, 100,  96 ],
        [  88,  92,  92 ],
        [  98,  73,  72 ],
        [  75,  84,  85 ],
        [  92, 100,  96 ],
        [  96,  92,  90 ],
        [  99,  76,  91 ],
        [  75,  82,  88 ],
        [  90,  94,  94 ],
        [  54,  84,  87 ],
        [  92,  89,  62 ],
        [  88,  94,  97 ],
        ])

# グラフ作成
fig = pyplot.figure()
ax = Axes3D(fig)

# 軸ラベルの設定
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

# 表示範囲の設定
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)
ax.set_zlim(0, 100)

# グラフ描画
ax.plot(data[:,0], data[:,1], data[:,2], "o", color="#cccccc", ms=4, mew=0.5)
pyplot.show()