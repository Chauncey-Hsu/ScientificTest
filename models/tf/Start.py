# __xuchuanqi__
import tensorflow as tf

# features = tf.constant(1, None, [2, 3], "hello")
# features = tf.constant(3.0)
# print(features)

# tmp = tf.Variable(tf.random.truncated_normal([3], stddev=0.1, seed=1))
# print(tmp)

# epoch = 50
# 不短的求最接近正确的参数。
# for eu in range(epoch):
#     print(epoch)

# b1 = tf.Variable(tf.constant(1,tf.float32,[2,3]))
# print(b1)
# lr = 0.1
# b1 = b1 + lr * 2  # 可训练的类型变为不可训练的张量类型。
# b1 = b1.assign_sub(lr * tf.Variable(tf.constant(2,tf.float32,[2,3]))) # 形状要匹配
# print(b1)

#         w1.assign_sub(lr * grads[0])

# x = tf.constant([[1, 1, 1], [1, 1, 2]])
# print(x.shape[1])
# print(tf.reduce_sum(x))
# print(tf.reduce_sum(x, 0))
# print(tf.reduce_sum(x, 1))
# print(tf.reduce_sum(x, 1, keepdims=True))
# print(tf.reduce_sum(x, [0, 1]))

print(tf.__path__)
print(tf.__version__)

