from matplotlib import pyplot as plot  # 用来绘制图形

import numpy as np  # 用来处理数据

from mpl_toolkits.mplot3d import Axes3D  # 用来给出三维坐标系。

figure = plot.figure()

# 画出三维坐标系：

axes = Axes3D(figure)

X = np.arange(122, 123, 0.125)

Y = np.arange(29, 30, 0.125)

# 限定图形的样式是网格线的样式：

X, Y = np.meshgrid(X, Y)
Z = 3 * (X) ** 2 + 2 * (Y) ** 2 + 5

# 绘制曲面，采用彩虹色着色：
# axes.set_position()
# axes.plot_surface(122.1, 29.6, 1)
# axes.plot_surface(122.5, 29.5, 1.2)
axes.plot_surface(X, Y, Z, cmap='rainbow')
# axes.plot_surface(X, Y, Z, cmap='rainbow')

# 图形可视化：

plot.show()