import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import os
import geopandas as gp
from shapely.geometry import Point


china_map = gp.GeoDataFrame.from_file("C:/Users/Administrator/Desktop/map_shp/shipnew/中国行政区划2004_shp/dijishi_2004.shp", encoding = 'gb18030')
data2002com = pd.read_excel(r'C:\Users\Administrator\Desktop\经纬度数据\按公司名称\2002.xlsx')

# 几何图形
geo_ploy = china_map['geometry']
# 地图点
geo_point = gp.GeoSeries([Point(x, y) for x, y in zip(lng, lat)])

fig, ax = plt.subplots(figsize=(12, 8))

ax.set_aspect('equal')
# 几何图形绘制
geo_ploy.plot(ax=ax, color='white', edgecolor='black')

# 地图点标注
geo_point.plot(ax=ax, marker='o', color='black', markersize=0.1)
