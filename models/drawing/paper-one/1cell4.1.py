from datetime import timedelta, date, datetime
from mpl_toolkits.mplot3d import Axes3D  # 空间三维画图
import matplotlib.pyplot as plt
# 导入中文字体，避免显示乱码
import pylab as mpl
import numpy as np

# list_date = [1635149400, 1635147883, 1635147993, 1635147783, 1635150000]

f = np.random.rand(10, 1) + 122
m = [122.0]
mm = np.array(m).reshape(1, 1)
t = [123.0]
tt = np.array(t).reshape(1, 1)
dd = np.vstack((mm, f, tt))
print(dd)

# xx = [122.0, 122.1, 122.2, 122.5, 123.0]
# print(xx)
f = np.random.rand(10, 1) + 30
m = [30.0]
mm = np.array(m).reshape(1, 1)
t = [31.0]
tt = np.array(t).reshape(1, 1)
lat = np.vstack((mm, f, tt))
print(lat)


########合并######
y = np.vstack((lat , dd))
print(y)