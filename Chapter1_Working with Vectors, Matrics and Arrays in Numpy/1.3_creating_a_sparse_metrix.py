"""
Problem/问题：
Given data with very few nonzero values, you want to efficiently represent it.
如何高效的创建一个 绝大多数值 都为0 的矩阵
"""

"""
Solution/解决示例：
"""
import numpy as np
from scipy import sparse

# 创建 一个矩阵
matrix = np.array([[0, 0],
                   [0, 1],
                   [3, 0]])

# 创建 compressed sparse row (CSR) 压缩稀疏行 的矩阵
matrix_sparse = sparse.csr_matrix(matrix)

print(matrix_sparse)
"""
(1, 1)	1
(2, 0)	3
"""

"""
A frequent situation in machine learning is having a huge amount of data; 
however,most of the elements in the data are zeros. 
For example, imagine a matrix where the columns are every movie on Netflix, 
the rows are every Netflix user, 
and the values are how many times a user has watched that particular movie. 
This matrix would have tens of thousands of columns and millions of rows! 
However, since most users do not watch most movies, the vast majority of elements would be zero.

处理海量数据是机器学习经常会遇到的场景，而这海量的数据里大多数的数值都为0.
举个例子：
我们要创建一个矩阵，列是 Netflix 上的所以电影，行是 Netflix 的所有用户，
值就是每个用户对应每部电影的观影次数。
可以想象，这个矩阵有多么大，因为它有上万列，上百万行。
但是，因为大多数用户不会看特别多的电影，因此绝大多数的值都为 0.


A sparse matrix is a matrix in which most elements are 0. 
Sparse matrices store only nonzero elements and assume all other values will be zero, 
leading to significant computational savings. 
In our solution, we created a NumPy array with two nonzero values, 
then converted it into a sparse matrix. 

稀疏矩阵就是这种大多数值为0的矩阵。
稀疏矩阵值保存不是0的数值和它们的位置，其他位置的值都为空，节省了大量的空间。
在示例中，我们使用 Numpy 创建了只有两个非0值的矩阵，然后把他转换成了稀疏矩阵。
我们可以打印这个稀疏矩阵，并看到只有两个非0值的位置被保留了下来。


There are a number of types of sparse matrices. 
However, in compressed sparse row (CSR) matrices, 
(1, 1) and (2, 0) represent the (zero-indexed) indices of the nonzero values 1 and 3, respectively. 
For example, the element 1 is in the second row and second column. 

稀疏矩阵也有很多种类型，我们例子中使用的是 CSR 稀疏行压缩矩阵。
(1, 1) 和 (2, 0) 表示 非0值 1 和 3 的下标（下标从0开始计数）。
可以看到，1这个值在第二行第二列的位置上。

We can see the advantage of sparse matrices if we create a much 
larger matrix with many more zero elements and then compare this larger matrix
with our original sparse matrix:

当创建一个有很多0的大矩阵时，稀疏矩阵的优势会体现的更加明显：
"""

# 创建一个大矩阵
matrix_large = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                         [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# 创建 compressed sparse row (CSR) 压缩稀疏行 的矩阵
matrix_large_sparse = sparse.csr_matrix(matrix_large)

print(matrix_large_sparse)
"""
(1, 1)	1
(2, 0)	3
"""


"""
As we can see, despite the fact that we added many more zero elements in the larger
matrix, its sparse representation is exactly the same as our original sparse matrix.
That is, the addition of zero elements did not change the size of the sparse matrix.

我们看到，尽管我们在原有矩阵的基础上增加了很多0。但是使用稀疏矩阵，他们的占用空间是一致的。

As mentioned, there are many different types of sparse matrices, 
such as compressed sparse column, list of lists, and dictionary of keys. 
While an explanation of the different types and their implications is outside the scope of this book, 
it is worth noting that while there is no “best” sparse matrix type, there are meaningful differences among them, 
and we should be conscious about why we are choosing one type over another.

我们提到，有多种类型的稀疏矩阵，例如，列压缩稀疏矩阵，列表的列表，键值字典等。
但是本书对它们之间的不同不做深入讨论。
它们之间并没有非常大的不同，没有必要说那种类型就是最好的，我们只需要考虑不同场景下选择不同的类型。
"""

