# coding=utf-8
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

data = pd.read_csv('countries_data.csv', header=0)
# 绘制数据分布图
plt.scatter(data.Services_of_GDP, data.ages65_of_total, c="red", marker='o', label='countries')
plt.xlabel('Services_of_GDP')
plt.ylabel('data.ages65_of_total')
plt.legend(loc=2)
plt.show()

X = data[['Services_of_GDP', 'ages65_of_total']]
X = X.values
X = preprocessing.scale(X)  # 数据归一化
plt.scatter(X[:, 0], X[:, 1], c="red", marker='o', label='countries')
plt.xlabel('Services_of_GDP')
plt.ylabel('data.ages65_of_total')
plt.legend(loc=2)
plt.show()

estimator = DBSCAN(eps=1, min_samples=5, metric='euclidean').fit(X)  # 构造聚类器
estimator.fit(X)  # 聚类
label_pred = estimator.labels_  # 获取聚类标签
print(label_pred)
# 绘制聚类结果
x0 = X[label_pred == 0]
x1 = X[label_pred == 1]
x2 = X[label_pred == -1]
plt.scatter(x0[:, 0], x0[:, 1], c="red", marker='o', label='label0')
plt.scatter(x1[:, 0], x1[:, 1], c="green", marker='*', label='label1')
plt.scatter(x2[:, 0], x2[:, 1], c="blue", marker='+', label='label2')
plt.xlabel('Services_of_GDP')
plt.ylabel('data.ages65_of_total')
plt.legend(loc=2)
plt.show()
