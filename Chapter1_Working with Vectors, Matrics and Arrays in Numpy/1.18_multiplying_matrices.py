"""
Problem/问题：
You want to add or subtract two matrices.
Numpy 矩阵相乘
"""

import numpy as np

# 创建 的矩阵
matrix_a = np.array([[1, 1],
                     [1, 2]])

matrix_b = np.array([[1, 3],
                     [1, 2]])

# 两个矩阵相加
np.dot(matrix_a, matrix_b)
matrix_a @ matrix_b
"""
array([[2, 5], 
       [3, 7]])
"""

# 矩阵相减
matrix_a * matrix_b
"""
array([[1, 3], 
       [1, 4]])
"""

"""
一般说矩阵乘法，是指矩阵乘积。

Numpy 做矩阵乘积就用 np.dot()
和之前看到的向量点积方法一样，
复习一下，向量点积是各个位置乘积之和

Python可以直接使用 @ 

只有在两个矩阵的列数和行数相同时乘积才有意义 。
它的意义是把许多数据紧凑地集中到一起，简便地表示一些复杂的模型。

如果使用 * 相乘，就是对应位置上的乘积
"""
