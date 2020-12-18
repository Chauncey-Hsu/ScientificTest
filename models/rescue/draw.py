# 读取csv至字典
import csv

from numpy.core._multiarray_umath import zeros
import matplotlib.pyplot as plt

csvFile = open("导出沉船报警记录.csv", "r", encoding='utf-8-sig')
reader = csv.reader(csvFile)

lonlat = zeros((2848, 2))
for item in reader:
    # 忽略第一行
    if reader.line_num == 1:
        continue
    # 计算网格号
    lonlat[reader.line_num, 0] = item[4]
    lonlat[reader.line_num, 1] = item[5]

csvFile.close()


#  citys
csvFile = open("浙江省市经纬度.csv", "r", encoding='utf-8-sig')
reader = csv.reader(csvFile)

citys = zeros((100, 2))
for item in reader:
    # 忽略第一行
    if reader.line_num == 1:
        continue
    # 计算网格号
    citys[reader.line_num, 0] = item[1]
    citys[reader.line_num, 1] = item[2]

csvFile.close()

fig = plt.figure(figsize=(20, 12))
ax1 = fig.add_subplot(111)
# 设置标题
ax1.set_title('Scatter Plot')
# 设置X轴标签
plt.xlabel('X')
# 设置Y轴标签
plt.ylabel('Y')
# 画散点图
ax1.scatter(x=lonlat[:, 0], y=lonlat[:, 1], c='r', marker='.')
ax1.scatter(x=citys[:, 0], y=citys[:, 1], c='b', marker='.')

# 设置图标
plt.legend('x1')
# 显示所画的图
plt.show()

plt.close()
