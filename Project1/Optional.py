from collections import Counter

# 初始化列表a
a = [3,2,5,7,3,8,4,1,1,3,2,4,12,1,5,1,8,2,9,5]

# (1)
a.append(1)  # 后面添加1
a.insert(0, 1)  # 前面添加1

# (2)
a.sort()

# (3)
count_dict = dict(Counter(a))

# (4)
elements_greater_than_5 = [(index, value) for index, value in enumerate(a) if value > 5]

# (5)
differences = [a[i+1] - a[i] for i in range(len(a)-1)]

# 打印结果
print("添加1后的列表:", a)
print("数字出现的次数:", count_dict)
print("大于5的元素及其位置:", elements_greater_than_5)
print("相邻两个元素的差:", differences)
