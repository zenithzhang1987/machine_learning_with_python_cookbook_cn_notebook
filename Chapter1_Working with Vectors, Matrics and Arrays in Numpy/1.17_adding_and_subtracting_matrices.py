"""
Problem/问题：
You want to add or subtract two matrices.
Numpy 矩阵加减法
"""

import numpy as np

# 创建 的矩阵
matrix_a = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 2]])

matrix_b = np.array([[1, 3, 1],
                     [1, 3, 1],
                     [1, 1, 8]])

# 两个矩阵相加
np.add(matrix_a, matrix_b)
matrix_a + matrix_b
"""
array([[2, 4, 2], 
       [2, 4, 2], 
       [2, 2, 10]])
"""

# 两个矩阵相减
np.subtract(matrix_a, matrix_b)
matrix_a - matrix_b
"""
array([[0, -2, 0], 
       [0, -2, 0], 
       [0, -2, -6]])
"""

"""
Numpy 做矩阵加减法可以使用
np.add() 和 np.subtract()
还有一种简单的写法，使用 + -

（看到此处，我想吐槽，有+号-号，费什么劲儿呢？）
"""
