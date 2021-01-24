import sys

import numpy as np
# np.set_printoptions(threshold=sys.maxsize)
# 7. 数组拆分
a = np.floor(10 * np.random.random((2, 12)))
print(a)
print(np.hsplit(a, 3))


# 6. 将不同数组堆叠在一起
a = 10 * np.random.random((2, 2))
b = np.floor(a)
c = np.floor(10 * np.random.random((2, 2)))
# print(b)
# print(c)
# print(np.vstack((b, c)))
# print(np.column_stack((b, c)))
# 5. 索引 切片 迭代
a = np.arange(10)**3
a[:5:2] = 22
a[ : :-1]
# print(a)
# print(a[1:3])
# print(a)
# print(a)
b = np.arange(12).reshape(3, 4)
# print(b)
# for x in b.flat:
#     print(x)
# print(b.T)
b.resize(4, 3)
# print(b)

#4 通函数
a = np.arange(3)
b = np.array([2., -1., 4.])
# print(a)
# print(b)
# print(np.exp(a))
# print(np.sqrt(a))
# print(np.add(a, b))


#3 基本操作
a = np.array([20, 30, 40, 50])
b = np.arange(4)
# print(a-b)
# print(b**2)
# print(10*np.sin(a))
# print(a < 35)
a = np.array([[1, 1], [0, 1]])
b = np.array([[2, 0], [3, 4]])
# print(a * b)
# print(a @ b)
# print(a.dot(b))

a = np.ones((2, 3), dtype=int)
# print(a)
b = np.random.random((2, 3))
# print(b)
a = a * 3
# print(a)

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, np.pi, 3)
c = a + b
# print(a)
# print(b)
# print(b.dtype.name)
# print(c.dtype)
d = np.exp(c * 1j)
# print(d.dtype.name)
a = np.random.random((2, 3))
# print(a)
# print(a.sum())
# print(a.max())
# print(a.min())

b = np.arange(12).reshape(3, 4)
# print(b)
# print(b.sum(axis=0))
# print(b.sum(axis=1))
# print(b.cumsum(axis=1))
# 2.数组创建
c = np.array([(1, 2, 3), (4, 5, 6)])
# print(c.dtype)
d = np.zeros((3, 4))
# print(d)
e = np.ones((2, 3, 4), dtype=np.int16)
# print(e)
f = np.empty((2, 3))
# print(f)
g = np.arange(0, 10, 2)
# print(g)
h = np.linspace(0, 10, 5)
# print(h)
i = np.linspace(0, 2 * np.pi, 100)
# print(i)
j = np.sin(i)
# print(j)


# 1.属性
a = np.arange(15).reshape(3, 5)
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)
# print(a.dtype)
# print(a.itemsize)
# print(a.data)
# print(type(a))
b = np.array([6, 7, 8])
# print(b)
# print(type(b))
