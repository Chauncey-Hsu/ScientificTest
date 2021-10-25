import matplotlib
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#定义坐标轴
from models.rescue.drawLonlat import x, y

fig4 = plt.figure()
ax4 = plt.axes(projection='3d')

#生成三维数据
xx = np.random.random(20)*10-5   #取100个随机数，范围在5~5之间
yy = np.random.random(20)*10-5
X, Y = np.meshgrid(xx, yy)
Z = np.sin(np.sqrt(X**2+Y**2))

#作图
ax4.scatter(X,Y,Z,alpha=0.3,c=np.random.random(400),s=np.random.randint(10,20, size=(20, 40)))     #生成散点.利用c控制颜色序列,s控制大小

#设定显示范围

plt.show()

#函数定义
matplotlib.pyplot.scatter(x, y,
	s=None,   #散点的大小 array  scalar
	c=None,   #颜色序列   array、sequency
	marker=None,   #点的样式
	cmap=None,    #colormap 颜色样式
	norm=None,    #归一化  归一化的颜色camp
	vmin=None, vmax=None,    #对应上面的归一化范围
 	alpha=None,     #透明度
	linewidths=None,   #线宽
	verts=None,   #
	edgecolors=None,  #边缘颜色
	data=None,

	)
