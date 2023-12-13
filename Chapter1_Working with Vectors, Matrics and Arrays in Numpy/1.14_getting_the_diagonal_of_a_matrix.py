"""
Problem/问题：
Calculating Dot Products.
Numpy 向量点乘
"""

import numpy as np

# 创建 两个向量
vector_a = np.array([[1, 2, 3]])
vector_b = np.array([[4, 5, 6]])

# numpy 计算点积
np.dot(vector_a, vector_b)

# python 计算
vector_a @ vector_b
"""
32
"""

"""
向量点乘得到点积，又叫数量积，标量积
numpy使用方法 np.dot()
python可以直接使用运算符 @

点积就是 向量对应位置上点相乘之和

记住，
两个向量点积越大越相似
点积>0，向量夹角 0 - 90 度
点积=0，相互垂直
点积<0, 向量夹角 90-180 度

"""
