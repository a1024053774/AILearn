import numpy as np

# 创建一个10x10的全0矩阵
matrix = np.zeros((10, 10))

# 设置1,3,5,7,9行的0,2,4,6,8列为1
# 0行到10行，步长为2
matrix[0:10:2, 0:10:2] = 1

# 打印结果
print(matrix)

