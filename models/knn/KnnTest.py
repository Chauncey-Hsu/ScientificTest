import csv
import random

# knn 分类编写结束，代码简单，但是学习到的地方很多。就像java中开始学习框架了一样。

with open("Prostate_Cancer.csv", 'r') as file:
    reader = csv.DictReader(file)

    datas = [row for row in reader]

# print(type(datas))
# for row in reader:
#     print(row)

# group by

random.shuffle(datas)

n = len(datas) // 3
datas_test = datas[0:n]
datas_train = datas[n:]


# 可调的地方一
def distance(d1, d2):
    res = 0
    for key in ("radius", "texture", "perimeter", "area", "smoothness", "compactness", "symmetry", "fractal_dimension"):
        res += (float(d1[key]) - float(d2[key])) ** 2
    var = res ** 0.5
    return var


# 可调的地方二
k = 4


# data 是单个未知最终结果的各个维度值集合


def knn(data):
    # 所有的距离求出
    res = [
        {"result": train["diagnosis_result"], "distance": distance(data, train)}
        for train in datas_train
    ]

    # 排序
    res = sorted(res, key=lambda item: item["distance"])

    # 前k个
    res2 = res[0:k]

    # 加权平均
    sum_dis = 0
    for point in res2:
        sum_dis += point["distance"]

    result = {"B": 0, "M": 0}
    for r in res2:
        result[r["result"]] = 1 - r["distance"] / sum_dis

    if result["B"] > result["M"]:
        return "B"
    else:
        return "M"


# 测试

precise = 0
for data in datas_test:
    if data["diagnosis_result"] == knn(data):
        precise += 1
print(precise / len(datas_test))
