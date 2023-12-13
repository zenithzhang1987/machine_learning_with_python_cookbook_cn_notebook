"""
Problem/问题：
You want to generate pseudorandom values.
Numpy 生成随机数
"""

import numpy as np

# 设置随机种子
np.random.seed(0)

# 生成3个 0.0-1.0之间的随机数
np.random.random(3)
"""
array([ 0.5488135 , 0.71518937, 0.60276338])
"""
# 生成3个 0-10之间的整数
np.random.randint(0, 11, 3)
"""
array([3, 7, 9])
"""

# 生成正态分布三个随机数，平均值为0，标准差为 1
np.random.normal(0.0, 1.0, 3)
"""
array([-1.42232584, 1.52006949, -0.29139398])
"""

# 生成logistic分布三个随机数，平均值为0，平均值为 0.0，scale 为 1.0
np.random.logistic(0.0, 1.0, 3)
"""
array([-0.98118713, -0.08939902, 1.46416405])
"""

# 从均匀分布中，生成 >=1 且 < 2 的三个随机数
np.random.uniform(1.0, 2.0, 3)
"""
array([ 1.47997717, 1.3927848 , 1.83607876])
"""


"""
Numpy 生成随机数可以使用
np.random

np.random.seed() 设置随机种子
随机算法的初始值，设定初始值后，每次随机得到的数是一样的。
不设置随机种子，系统会使用时间做初始值，每次随机数都不一样

随机数的生成有各种算法，np.random也提供了丰富的支持：

"""

