"""
Problem/问题：
You need to select one or more elements in a vector or matrix.
读取向量或矩阵中的元素值
"""

import numpy as np

# 创建向量
vector = np.array([1, 2, 3, 4, 5, 6])

# 创建矩阵
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 向量中 下标为3（下标从0开始）的元素
vector[2]
"""
3
"""

# 矩阵中 第二行，第二列 的元素
matrix[1, 1]
"""
5
"""

"""
Like most things in Python, NumPy arrays are zero-indexed, meaning that the index
of the first element is 0, not 1. With that caveat, NumPy offers a wide variety of
methods for selecting (i.e., indexing and slicing) elements or groups of elements in
arrays:

和python一样（和所有编程语言一样), NumPy 数组的下标都是从0开始的。
基于此点，NumPy 提供多种读取数组元素的方法(和python基本一样）：
"""

# 读取 向量中所有元素
vector[:]
"""
array([1, 2, 3, 4, 5, 6])
"""

# 读取 下标 小于 3 （不包括3）的所有元素
vector[:3]
"""
array([1, 2, 3])
"""

# 读取 下标 大于 3 （包括3）的所有元素
vector[3:]
"""
array([4, 5, 6])
"""

# 读取 最后一个元素
vector[-1]
"""
6
"""

# 翻转向量
vector[::-1]
"""
array([6, 5, 4, 3, 2, 1])
"""

# 读取 矩阵 前两行 所有列
matrix[:2, :]
"""
array([[1, 2, 3],
       [4, 5, 6]])
"""

# 读取 矩阵 所有行 第二列
matrix[:, 1:2]
"""
array([[2],
       [5],
       [8]])
"""

