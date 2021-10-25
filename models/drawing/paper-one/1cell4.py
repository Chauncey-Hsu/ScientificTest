import numpy
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图

# 数据

# 数据１
data1 = np.arange(24).reshape((8, 3))
# data的值如下：
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]
#  [12 13 14]
#  [15 16 17]
#  [18 19 20]
#  [21 22 23]]
x1 = data1[:, 0]  # [ 0  3  6  9 12 15 18 21]
y1 = data1[:, 1]  # [ 1  4  7 10 13 16 19 22]
z1 = data1[:, 2]  # [ 2  5  8 11 14 17 20 23]

# 数据２
# 经度
a = np.random.rand(45,1) + 122
b = [122.0]
bb = np.array(b).reshape(1,1)
c = [123.0]
cc = np.array(c).reshape(1,1)
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
zz = np.array(z).reshape(47,1)
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
# ax.scatter(x1, y1, z1, c='r', label='顺序点')
ax.scatter(x2, y2, z2, c='g', label='position')

# 绘制图例
ax.legend(loc='best')

# 添加坐标轴(顺序是Z, Y, X)
ax.set_zlabel('timestamp', fontdict={'size': 10, 'color': 'blue'})
ax.set_ylabel('latitude', fontdict={'size': 10, 'color': 'blue'})
ax.set_xlabel('longitude', fontdict={'size': 10, 'color': 'blue'})

ax.set
# 展示
plt.show()
