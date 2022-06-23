import numpy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图

# 数据

# 数据１
z = [[122.5, 30.5, 1635149700]]
data1 = np.array(z).reshape(1, 3)
print(data1)
x1 = data1[:, 0]  # [ 0  3  6  9 12 15 18 21]
y1 = data1[:, 1]  # [ 1  4  7 10 13 16 19 22]
z1 = data1[:, 2]  # [ 2  5  8 11 14 17 20 23]


# 数据１
a1 = [[122.0, 30.0, 1635149400]]
data11 = np.array(a1).reshape(1, 3)
print(data11)
x11 = data11[:, 0]  # [ 0  3  6  9 12 15 18 21]
y11 = data11[:, 1]  # [ 1  4  7 10 13 16 19 22]
z11 = data11[:, 2]  #

a2 = [[123.0, 31.0, 1635150000]]
data12 = np.array(a2).reshape(1, 3)
print(data12)
x12 = data12[:, 0]  # [ 0  3  6  9 12 15 18 21]
y12 = data12[:, 1]  # [ 1  4  7 10 13 16 19 22]
z12 = data12[:, 2]  # [ 2  5


# 数据２
# 经度
a = np.random.rand(45, 1) + 122
b = [122.0]
bb = np.array(b).reshape(1, 1)
c = [123.0]
cc = np.array(c).reshape(1, 1)
xx = np.vstack((bb, a, cc))

# 纬度
f = np.random.rand(45, 1) + 30
m = [30.0]
mm = np.array(m).reshape(1, 1)
t = [31.0]
tt = np.array(t).reshape(1, 1)
yy = np.vstack((mm, f, tt))

# 时间
z = [1635149400,
     1635149583, 1635149893, 1635149993, 1635149693, 1635149593,
     1635149693, 1635149883, 1635149983, 1635149683, 1635149583,
     1635149693, 1635149883, 1635149983, 1635149683, 1635149583,
     1635149693, 1635149883, 1635149983, 1635149683, 1635149583,
     1635149693, 1635149883, 1635149983, 1635149683, 1635149583,
     1635149693, 1635149883, 1635149983, 1635149683, 1635149583,
     1635149693, 1635149883, 1635149983, 1635149683, 1635149583,
     1635149693, 1635149883, 1635149983, 1635149683, 1635149583,
     1635149693, 1635149883, 1635149983, 1635149683, 1635149583,
     1635150000]
zz = np.array(z).reshape(47, 1)
# 合并
data2 = numpy.vstack((xx.T, yy.T, zz.T))
data2 = data2.T
print(data2)

x2 = data2[:, 0]
y2 = data2[:, 1]
z2 = data2[:, 2]

# 绘制散点图
fig = plt.figure()
ax = Axes3D(fig)
# ax.scatter(x1, y1, z1, c='r', label='new model')
ax.scatter(x1, y1, z1, c='r', label='STGSM')
ax.scatter(x11, y11, z11, c='w')
ax.scatter(x12, y12, z12, c='w')

# 绘制图例
ax.legend(loc='best')

# 添加坐标轴(顺序是Z, Y, X)
ax.set_zlabel('timestamp', fontdict={'size': 10, 'color': 'blue'})
ax.set_ylabel('latitude', fontdict={'size': 10, 'color': 'blue'})
ax.set_xlabel('longitude', fontdict={'size': 10, 'color': 'blue'})

ax.set
# 展示
plt.show()
