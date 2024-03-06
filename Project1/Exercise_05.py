import numpy as np

# 构建数组
arr = np.arange(16).reshape(4, 4)
print("Original array:\n", arr)

# 输出第2列
print("\nColumn 2:")
print(arr[:, 1])  # 列的索引为1

# 输出3-4列
print("\nColumns 3-4:")
print(arr[:, 2:4])  # 包括索引为2的列，不包括索引为4的列

# 输出2、4列
print("\nColumns 2 and 4:")
print(arr[:, [1, 3]])  # 直接使用列的索引列表

# 将值为4、7的两个点修改为0
arr[arr == 4] = 0
arr[arr == 7] = 0
print("\nArray after replacing 4 and 7 with 0:\n", arr)

# 过滤出<5的值
print("\nValues less than 5:")
print(arr[arr < 5])  # 使用布尔索引
