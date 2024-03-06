info = "name:My|age:28|gender:male"  # 原始字符串数据

# 使用 "|" 分割字符串，得到键值对的列表
info_pairs = info.split("|")

# 初始化一个空字典来存储结果
info_dict = {}

# 遍历键值对字符串，进一步分割并存储到字典中
for pair in info_pairs:
    key, value = pair.split(":")  # 使用 ":" 分割每个键值对
    info_dict[key] = value  # 将键值对存储到字典中

# 输出结果字典
print(info_dict)
