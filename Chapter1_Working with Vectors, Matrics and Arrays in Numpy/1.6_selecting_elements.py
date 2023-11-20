"""
Problem/问题：
You want to describe the shape, size, and dimensions of a matrix.
如何打印一个矩阵的信息
"""

import numpy as np

# 创建矩阵
matrix = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# 查看矩阵有多少行和列
matrix.shape
"""
(3, 4)
"""

# 查看矩阵有多少元素（行*列)
matrix.size
"""
12
"""

# 查看矩阵的维度
matrix.ndim
"""
2
"""


"""
This might seem basic (and it is); however, time and again it will be valuable to check
the shape and size of an array both for further calculations and simply as a gut check
after an operation.

别看这些操作非常基础（虽然确实是这样的）；但是，日后你会发现这些操作非常有用，
比如使用数组的形状和大小做进一步计算，或者在操作后进行一些检查。
"""
