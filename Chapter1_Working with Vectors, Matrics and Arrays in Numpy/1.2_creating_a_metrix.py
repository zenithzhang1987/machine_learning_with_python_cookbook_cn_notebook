"""
Problem/问题：
You need to create a metrix.
创建矩阵
"""

"""
Solution/解决示例：
"""
# 引入numpy 包
import numpy as np

# 创建 一个矩阵
matrix = np.array([[1, 2],
                   [1, 2],
                   [1, 2]])

# 方法二
matrix_obj = np.mat([[1, 2],
                     [1, 2],
                     [1, 2]])


# print(matrix)
# print(matrix_obj)

"""
Discussion
To create a matrix we can use a NumPy two-dimensional array. 
In our solution, the matrix contains three rows and two columns. 
NumPy actually has a dedicated matrix data structure.
However, the matrix data structure is not recommended for two reasons. 
First, arrays are the de facto standard data structure of NumPy. 
Second, the vast majority of NumPy operations return arrays, not matrix objects.

讨论
我们可以使用 二维数组 来创建 矩阵。
实例中，我们创建了一个 3 行 2 列 的矩阵。
NumPy 实际上有专用的矩阵数据结构（如方法二所示）。
但我们不推荐使用矩阵数据结构，有两点原因：
1 数组是 NumPy 底层实际的数据结构 
2 绝大多数 NumPy 的操作都会返回 数组，而不是矩阵
（所以在 NumPy 使用数组的数据结构会更直接）
"""

