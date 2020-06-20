import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# xx在-3到3之间以步长为0.01，yy在-3到3之间以步长0.01,生成间隔数值点
xx, yy = np.mgrid[-3:3:.1, -3:3:.1]
print(xx)
print(yy)

# 将xx , yy用ravel拉直，并用c_合并配对为二维张量，生成二维坐标点
# grid = np.c_[xx.ravel(), yy.ravel()]
# grid = tf.cast(grid, tf.float32)
# print(grid)
