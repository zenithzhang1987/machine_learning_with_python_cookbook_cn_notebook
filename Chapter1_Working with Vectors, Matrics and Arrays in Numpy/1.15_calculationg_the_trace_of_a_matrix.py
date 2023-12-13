"""
Problem/问题：
You need to get the diagonal elements of a matrix.
Numpy 取矩阵的对角线
"""

import numpy as np

# 创建 的矩阵
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 取矩阵对角线上的值
matrix.diagonal()
"""
array([1, 5, 9])
"""

# 对角线向上移动
matrix.diagonal(1)
"""
array([2, 6])
"""

# 对角线向下移动
matrix.diagonal(-1)
"""
array([4, 8])
"""

"""
要拿矩阵对角线上的值，可以使用
matrix.diagonal()

还可以带上偏移量参数，
让对角线上移或下移拿值，很方便
"""
