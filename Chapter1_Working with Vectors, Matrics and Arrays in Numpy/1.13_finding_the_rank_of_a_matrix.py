"""
Problem/问题：
You need to transpose a vector or matrix.
Numpy 矩阵转置
"""

import numpy as np

# 创建 的矩阵
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 求矩阵转置，行列互换
matrix.T
"""
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
"""

# 向量转置
np.array([1, 2, 3, 4, 5, 6]).T
"""
array([1, 2, 3, 4, 5, 6])
"""

# 向量转置
np.array([[1, 2, 3, 4, 5, 6]]).T
"""
array([[1],
       [2], 
       [3], 
       [4], 
       [5], 
       [6]])
"""



"""
matrix.T
矩阵转置，就是矩阵的行和列互换。
是线性代数处理矩阵的常见操作。

和线性代数不同的是，numpy是无法对向量做转置，因为向量代表一组值。
如果想对向量转置，把向量用双括号包装成矩阵的一行，就可以了。
"""