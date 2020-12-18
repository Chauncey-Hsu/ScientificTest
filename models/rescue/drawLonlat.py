# -*- coding: utf-8 -*-
# coding=utf-8

# 导入必要的模块
from numpy import *
import matplotlib.pyplot as plt

# 产生测试数据
'''
x = np.arange(1,10)
y = x
'''

data_spa = zeros((1000, 100))
for i in range(0, 100, 1):
    data_spa[200, i] = 1
for i in range(0, 1000, 1):
    data_spa[i, 5] = 1

data_spa_1 = zeros((100000, 2))
for x in range(0, 1000, 1):
    for y in range(0, 100, 1):
        if data_spa[x, y] == 1:
            data_spa_1[100 * x + y, 0] = x
            data_spa_1[100 * x + y, 1] = y

fig = plt.figure()
ax1 = fig.add_subplot(111)
# 设置标题
ax1.set_title('Scatter Plot')
# 设置X轴标签
plt.xlabel('X')
# 设置Y轴标签
plt.ylabel('Y')
# 画散点图
ax1.scatter(x=data_spa_1[:, 0], y=data_spa_1[:, 1], c='r', marker='.')
# 设置图标
plt.legend('x1')
# 显示所画的图
plt.show()

plt.close()
