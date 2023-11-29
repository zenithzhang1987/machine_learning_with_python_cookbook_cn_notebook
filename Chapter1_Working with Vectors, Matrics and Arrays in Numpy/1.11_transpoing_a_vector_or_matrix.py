"""
Problem/问题：
You want to change the shape (number of rows and columns) of an array without
changing the element values
矩阵变形
"""

import numpy as np

# 创建 4*3 的矩阵
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [10, 11, 12]])

# 变形 2*6 矩阵
matrix.reshape(2, 6)
"""
array([[1, 2, 3, 4, 5, 6],
       [7, 8, 9, 10, 11, 12]])
"""

# 使用 -1
matrix.reshape(1, -1)
"""
array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
"""

# 整数入参
matrix.reshape(12)
print(matrix.reshape(12))
"""
array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]])
"""

"""
reshape allows us to restructure an array so that we maintain the same data but
organize it as a different number of rows and columns. The only requirement is that
the shape of the original and new matrix contain the same number of elements (i.e.,
are the same size). We can see the size of a matrix using size:

当我们想把同样的数据放入不同行数列数的矩阵中处理时，我们可以使用矩阵变形的手段。
注意：变形前后矩阵的 行数与列数的乘积保持不变。

One useful argument in reshape is -1, which effectively means “as many as needed,”
so reshape(1, -1) means one row and as many columns as needed:

有时我们不想计算新的行数或列数时，可以使用 -1，表示尽可能多。
reshape(1, -1) 就表示变形成 1行 尽可能多的列的矩阵。

Finally, if we provide one integer, reshape will return a one-dimensional array of that
length:

如果我们提供了一个整数，就会返回一个长度是这个整数的 1 维数组。
"""
