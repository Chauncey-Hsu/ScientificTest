import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

k, b = np.mgrid[1:3:30j, 4:6:30j]
f_kb = 3 * k ** 2 + 2 * b + 1

ax = plt.subplot(111, projection='3d')
ax.plot_surface(k, b, f_kb, rstride=1, cstride=1)
ax.set_xlabel('k')
ax.set_ylabel('b')
ax.set_zlabel('ErrorArray')
p.show()
