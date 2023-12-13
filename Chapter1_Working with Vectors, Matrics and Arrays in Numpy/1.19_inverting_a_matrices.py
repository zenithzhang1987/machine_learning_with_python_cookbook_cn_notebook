"""
Problem/问题：
You want to calculate the inverse of a square matrix.
Numpy 求逆矩阵
"""

import numpy as np

# 创建 的矩阵
matrix = np.array([[1, 4],
                   [2, 5]])

# 求矩阵逆矩阵
matrix_inv = np.linalg.inv(matrix)
"""
array([[-1.66666667,  1.33333333], 
       [ 0.66666667, -0.33333333]])
"""

# 矩阵 * 逆矩阵 = 单位矩阵
matrix @ np.linalg.inv(matrix)
"""
array([[1, 0], 
       [0, 1]])
"""

"""
Numpy 求一个矩阵的逆矩阵乘就用 
np.linalg.inv()

矩阵*逆矩阵=单位矩阵
单位矩阵就是对角线为1，其它位置为0的方形矩阵

"""
