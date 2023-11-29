"""
Problem/问题：
You need to transform a matrix into a one-dimensional array.
高效拍平矩阵
"""

import numpy as np

# 创建 的矩阵
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])

# 拍平矩阵
matrix.flatten()
"""
array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
"""

# 使用 -1
matrix.reshape(1, -1)
"""
array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
"""

# 创建两个矩阵
matrix_a = np.array([[1, 2],
                     [3, 4]])
matrix_b = np.array([[5, 6],
                     [7, 8]])
matrix_list = [matrix_a, matrix_b]

# 使用 ravel 方法, 拍平矩阵列表
np.ravel(matrix_list)
"""
array([[1, 2, 3, 4, 5, 6, 7, 8]])
"""

"""
我们来拍平矩阵，就是把矩阵变为 1 维数组。
我们可以用 flatten 方法
也可以用 reshape(1, -1)，就是将矩阵变形的特殊情况
也可以用 ravel 方法

ravel方法比 flatten方法更高效，因为ravel是在原矩阵上进行操作，而flatten是复制原矩阵，然后在复制的矩阵上操作。
ravel方法还可以同时处理多个矩阵。
"""
