"""
Problem/问题：
You need to find the maximum or minimum value in an array.
寻找数组的最大或最小值
"""

import numpy as np

# 创建矩阵
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 最大值
np.max(matrix)

# 最小值
np.min(matrix)

# 找到每列的最大值
np.max(matrix, axis=0)
"""
array([7, 8, 9])
"""

# 找到每行的最大值
np.max(matrix, axis=1)
"""
array([3, 6, 9])
"""

"""
Often we want to know the maximum and minimum value in an array or subset of
an array. This can be accomplished with the max and min methods. Using the axis
parameter, we can also apply the operation along a certain axis:

我们经常会需要算一个矩阵的或者数组的最大最小值。
我们可以用 max min 方法来实现。
使用 axis 参数 （0 表示 列， 1 表示 行), 可以实现找到某列的最大最小值

"""