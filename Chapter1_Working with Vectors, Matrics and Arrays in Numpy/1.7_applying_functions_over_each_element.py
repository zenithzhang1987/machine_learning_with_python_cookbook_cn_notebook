"""
Problem/问题：
You want to apply some function to all elements in an array.
对数组中所有元素使用方法
"""

import numpy as np

# 创建矩阵
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# 给所有元素加100
add_100 = lambda i: i+100

# 向量化方法
vectorized_add_100 = np.vectorize(add_100)

# 把方法应用到矩阵的所有元素上
vectorized_add_100(matrix)
"""
array([[101, 102, 103],
       [104, 105, 106],
       [107, 108, 109]])
"""


"""
The NumPy vectorize method converts a function into a function that can apply
to all elements in an array or slice of an array.
It’s worth noting that vectorize is essentially a for loop over the elements 
and does not increase performance. 
Furthermore, NumPy arrays allow us to perform operations between arrays even if their
dimensions are not the same (a process called broadcasting). 
For example, we can create a much simpler version of our solution using broadcasting:

matrix + 100

Broadcasting does not work for all shapes and situations, but it is a common way of
applying simple operations over all elements of a NumPy array

NumPy 的向量方法就是把一个方法变成可以应用于向量中多元素的方法。
如果只是用向量化方法遍历元素是没有意义的，也不会提升性能。
NumPy还可以同时操作两个不同维度的数组，比如下面这个例子:

matrix + 100

但是这种操作不是对所有情况都适用，但是它是对元素进行简单操作的常用方法。
"""

