"""
Problem/问题：
You need to create a vector.
创建向量
"""

"""
Solution/解决示例：
"""
# 引入numpy 包
import numpy as np

# 创建 只有一行的 向量
vector_row = np.array([1, 2, 3])

# 创建 只有一列的 向量
vector_column = np.array([[1],
                          [2],
                          [3]])

# print(vector_row)
# print(vector_column)

"""
Discussion
NumPy’s main data structure is the multidimensional array. A vector is just an array
with a single dimension. To create a vector, we simply create a one-dimensional array.
Just like vectors, these arrays can be represented horizontally (i.e., rows) or vertically
(i.e., columns).

讨论
NumPy 中主要的数据结构就是多维数组
向量 只有一个维度的数组
要创建向量，我们只需要简单的创建一维数组
和向量一样，数组可以横向创建（就是 行）或者 纵向创建（就是 列）
"""