import csv
import numpy as np
from models.clustering.outlier.ShipPosition import ShipPosition

# 初始化变量部分
# 参数：判定脱离编组的距离阈值 (单位：海里)
distance = 10
# 阈值换算为经纬度 (1纬度=60海里=601852米)
distanceCoordinate = distance/60
# 方格边长为距离阈值的两倍。
sideLenth = 2 * distanceCoordinate

# 中国浙江福建海域中，方格覆盖的经纬度
startLon = 120
endLon = 125
startLat = 29
endLat = 32

# 读取csv至字典
csvFile = open("导出8000.csv", "r", encoding='utf-8-sig')
reader = csv.reader(csvFile)

# 建立空字典
cellDic = {}
positionDic = {}

def getCellId(param, param1):

    pass


for item in reader:
    # 忽略第一行
    if reader.line_num == 1:
        continue
    # 计算网格号
    cellid = getCellId(item[2], item[3])
    # 放入到positionDic中
    position = ShipPosition(item[0], item[1], item[2], item[3], item[4], cellid)
    positionDic[item[0]] = position
    # 放入到cellDic中( 是否为null )
    collection = cellDic[cellid]
    collection.insert(position)

csvFile.close()
print(cellDic)
print(positionDic)
