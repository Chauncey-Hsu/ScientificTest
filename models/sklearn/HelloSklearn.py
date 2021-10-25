from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

dataSet = load_iris()
feature = dataSet['feature_names']  # 特征的名称
data = dataSet['data']  # 数据
target = dataSet['target_names']  # 标签的名称
label = dataSet['target']  # 数据对应的标签

pd.set_option('display.max_columns', None)  # 显示完整的列
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', None)  # 显示完整的行
pd.set_option('display.max_colwidth', 1000)

df = pd.DataFrame(np.column_stack((data, label)), columns=np.append(feature, 'label'))
# print(type(df))
# print(df.head(5))  # 查看前五行数据

rate = df.isnull().sum(axis=0).sort_values(ascending=False) / float(len(df))  # 检查缺失值比例
# print(type(rate))
# print(rate)

classRate = df['label'].value_counts()  # 检查数据类别的比例
# print(type(classRate))
# print(classRate)

# 数据标准化 z-core
from sklearn.preprocessing import StandardScaler

# print(type(data))
# print(data[:5])
standData = StandardScaler().fit_transform(data)
# print(standData[:5])

# 训练模型，以多元逻辑回归为例
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score

ss = ShuffleSplit(n_splits=1, test_size=0.2)  # 按比例拆分数据，80%用作训练
for tr, te in ss.split(data, label):
    xr = data[tr]
    xe = data[te]
    yr = label[tr]
    ye = label[te]
    clf = LogisticRegression(solver='lbfgs', multi_class='multinomial')
    clf.fit(xr, yr)
    predict = clf.predict(xe)
    print(classification_report(ye, predict))

# from sklearn.model_selection import GridSearchCV
#
# clf = LogisticRegression()
# gs = GridSearchCV(clf, parameters)
# gs.fit(data, label)
# gs.best_params_
