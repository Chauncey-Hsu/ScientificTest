from sklearn.datasets import make_blobs, load_iris
import matplotlib.pyplot as plt

'''
测试 sklearn 数据集是什么样子，并展示出来
展示出的都是有监督的。
'''

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 莺尾花
# s, t = load_iris(True)  # 莺尾花 打印
# print(s)
# print(t)

n_samples = 1500
random_state = 170
x, y = make_blobs(n_samples=n_samples, random_state=random_state)
print(x.shape, y.shape)
# print(x)
# print(y)

plt.scatter(x[:, 0], x[:, 1], c=y)
plt.title(u"原始数据分布")
plt.show()
