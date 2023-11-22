"""
Problem/问题：
You want to calculate some descriptive statistics about an array.
计算数组的一些统计量
"""

import numpy as np

# 创建矩阵
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# mean 平均值: 5
np.mean(matrix)

# variance 方差 （离散程度的平均值）6.6666666666667
np.variance(matrix)

# std 标准差（方差的平方根）2.5819888974716112
np.std(matrix)


"""
我们来对数组做一些简单的统计。
用 mean 获得平均值。
用 variance 获得方差，用 std 获得标准差。
标准差是方差的平方根，表示一组数据的离散程度。

使用 axis 参数 （0 表示 列， 1 表示 行), 可以实现找到某列的统计量
"""
