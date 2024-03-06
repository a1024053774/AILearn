import numpy as np

# 创建两个2x3的随机数组
arr1 = np.random.rand(2, 3)
arr2 = np.random.rand(2, 3)

# 垂直堆叠arr1和arr2
arr_vstacked = np.vstack((arr1, arr2))

# 打印结果
print("Array 1:\n", arr1)
print("\nArray 2:\n", arr2)
print("\nVertically Stacked Array:\n", arr_vstacked)
