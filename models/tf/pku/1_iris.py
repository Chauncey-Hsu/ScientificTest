# _*_ coding: UTF-8 _*_
# 利用鸢尾花数据集，实现前向传播、反向传播、loss曲线
# TODO 本模型可以做的优化是，把学习率调整成动态的，由大到小的。

import tensorflow as tf
from sklearn import datasets
from matplotlib import pyplot as plt
import numpy as np

x_data = datasets.load_iris().data
y_data = datasets.load_iris().target

seed = 100
np.random.seed(seed)
np.random.shuffle(x_data)
np.random.seed(seed)
np.random.shuffle(y_data)
tf.random.set_seed(seed)  # why TODO

x_train = x_data[:-30]
y_train = y_data[:-30]
x_test = x_data[-30:]
y_test = y_data[-30:]

# 矩阵相乘时，因数据类型不一致报错。
x_train = tf.cast(x_train, tf.float32)
x_test = tf.cast(x_test, tf.float32)

train_db = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(32)
test_db = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(32)

w1 = tf.Variable(tf.random.truncated_normal([4, 3], stddev=0.1, seed=1))  # 权重
b1 = tf.Variable(tf.random.truncated_normal([3], stddev=0.1, seed=1))  # 偏移量

lr = 0.1  # 学习率
train_loss_results = []  # 将每一轮的loss记录在此列表中，为后续绘画loss曲线提供数据。
test_acc = []  # 将每轮的acc记录在此表，为后续绘画acc曲线提供数据。
epoch = 500  # 循环500轮
loss_all = 0  # 每轮分为4step，loss_all记录着4step生成的4个loss之和

# 不短的求最接近正确的参数。
for epoch in range(epoch):
    for step, (x_train, y_train) in enumerate(train_db):  # 总共循环4次，每次是one slice, 这里的step 没有是没有用
        # print(x_train)
        # print(y_train)
        with tf.GradientTape() as tape:
            y = tf.matmul(x_train, w1) + b1
            y = tf.nn.softmax(y)
            y_ = tf.one_hot(y_train, depth=3)
            # print(y_)
            loss = tf.reduce_mean(tf.square(y_ - y))  # 采用均方误差损失函数，mse=mean() 注：与sqrt 开方所混淆，人写的错别很多，尤其是在状态不好的时候
            loss_all += loss.numpy()
        # 计算loss对各个参数的梯度
        grads = tape.gradient(loss, [w1, b1])

        # 实现梯度更新
        w1.assign_sub(lr * grads[0])
        b1.assign_sub(lr * grads[1])

    # 看每轮后的效果
    # 在经过1轮4step迭代后，
    print("Epoch{}, loss{}".format(epoch, loss_all / 4))
    train_loss_results.append(loss_all / 4)
    loss_all = 0

    # 测试部分
    total_corrent, total_number = 0, 0
    for x_test, y_test in test_db:
        y = tf.matmul(x_test, w1) + b1
        y = tf.nn.softmax(y)
        pred = tf.argmax(y, axis=1)
        pred = tf.cast(pred, y_test.dtype)
        # 若分类正确，则correct=1，否则为0，将bool型的结果转换为int型 。
        corrent = tf.cast(tf.equal(pred, y_test), dtype=tf.int32)
        # 将每个batch的current数累加起来
        corrent = tf.reduce_sum(corrent)
        # 将所有batch的current数累加起来
        total_corrent += corrent
        # 测试的样本总数，shape[0]返回变量的行数
        total_number += x_test.shape[0]

    # 总得准确率
    acc = total_corrent / total_number
    test_acc.append(acc)
    print("Test_acc:{}".format(acc))
    print('-------------------------------------')

# 总结
# 绘制 loss 曲线
plt.title("Loss Function Curve")
plt.xlabel('Epoch')  # X 轴变量名称，
plt.ylabel('Loss')
plt.plot(train_loss_results, label='$Loss$')  # 逐点画出train_loss_results值，并连线图标是Loss
plt.legend()  # 画出曲线图标
plt.show()

# 绘制 Accuracy 曲线
plt.title('Acc Curve')
plt.xlabel("Epoch")
plt.ylabel("Acc")
plt.plot(test_acc, label='$Accuracy$')
plt.legend()
plt.show()

print(w1,b1)

# 现实中，识别花朵类别，怎么解决，
# 一样是收集数据、找导向结果的公式、参数，
# 怎么优化参数，用数学公式或者算法，比如这里使用的典型的梯度下降算法。
# 怎么实现呢，用python+类库+...
