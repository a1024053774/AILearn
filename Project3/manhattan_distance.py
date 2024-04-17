import numpy as np

def manhattan_distance(array1, array2):
    """
    计算两个 NumPy 数组之间的曼哈顿距离。

    参数:
        array1 (np.ndarray): 第一个数组，形状为 (N, D)，其中 N 是样本数，D 是维度数。
        array2 (np.ndarray): 第二个数组，与 array1 形状相同。

    返回:
        float or np.ndarray: 单个样本对之间的曼哈顿距离（如果输入是 1D 数组）或所有样本对之间的曼哈顿距离（如果输入是 2D 数组）。

    """
    return np.sum(np.abs(array1 - array2), axis=-1)

# 示例：计算两个二维点之间的曼哈顿距离
point1 = np.array([1, 2])
point2 = np.array([4, 5])

distance = manhattan_distance(point1, point2)
print("曼哈顿距离:", distance)

# 示例：计算两个二维点集之间的所有曼哈顿距离（每一对点之间的距离）
points1 = np.array([[1, 2], [3, 4]])
points2 = np.array([[4, 5], [6, 7]])

distances1 = manhattan_distance(points1, points2)
print("所有曼哈顿距离:\n", distances1)
distances2 = manhattan_distance(points1, points2).sum()
print("所有曼哈顿距离:\n", distances2)

'''
以上示例中
函数 manhattan_distance 接收两个 NumPy 数组作为参数。
使用 np.abs 函数计算两数组对应元素之间的绝对差值。
使用 np.sum 函数沿着最后一个轴（即维度轴）对绝对差值求和，得到每个样本对（或者单个样本对）的曼哈顿距离。
如果你的输入是一维数组（代表单个点），结果将直接返回单个曼哈顿距离值，如distance。
如果输入是二维数组（每一行代表一个点），结果将是所有样本对之间曼哈顿距离的数组，如distances1。
在后面加上.sum()即可计算出曼哈顿距离总和，如distances2。

'''


#以下为计算阵列（数组）之间相同位置数字不同个数，可用于启发函数
# 假设我们有两个相同大小的数组（此处为二维数组）
array1 = np.array([[1, 2, 3], [3, 4, 5]])
array2 = np.array([[2, 1, 3], [4, 3, 5]])

# 计算两个数组对应位置元素的差异
diff_array = array1 != array2

# 计算不同数字的数量（即非零元素数量）
num_different_elements = np.count_nonzero(diff_array)

print("不同数字的数量:", num_different_elements)