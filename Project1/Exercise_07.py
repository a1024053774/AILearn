import pandas as pd

# 创建数据字典
data = {
    'Name': ['Lemon', 'Jack', 'Peter'],
    'City': ['长沙', '上海', '深圳'],
    'Math': [80, 90, 60],
    'Chem': [90, 75, 80]
}

# 使用数据字典创建DataFrame
df = pd.DataFrame(data)

# 打印DataFrame
print(df)
