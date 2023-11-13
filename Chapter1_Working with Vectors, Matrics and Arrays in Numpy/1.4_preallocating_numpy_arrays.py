"""
Problem/问题：
You need to preallocate arrays of a given size with some value.
预生成默认值数据
"""

import numpy as np

# 生成 默认值为0 的 1*5 的向量
vector = np.zeros(shape=5)

print(vector)
"""
[0. 0. 0. 0. 0.]
"""

# 生成 默认值为 1 的 3*3 的 矩阵
matrix = np.full(shape=(3, 3), fill_value=1)

print(matrix)
"""
[[1 1 1]
 [1 1 1]
 [1 1 1]]
"""

"""
Generating arrays prefilled with data is useful for a number of purposes, such as
making code more performant or using synthetic data to test algorithms. In many
programming languages, preallocating an array of default values (such as 0s) is
considered common practice

生成带有默认值的数据集有很多用处，例如让代码更高效或者生成测试数据集。
在很多编程语言里，生成有默认值的数据集也会常常用到。
"""

