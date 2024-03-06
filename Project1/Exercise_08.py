import pandas as pd

# (1) 加载Score.xlsx文件，显示前3行
file_path = 'Score.xlsx'  # 假设文件位于当前工作目录，否则需要提供完整路径
df = pd.read_excel(file_path)
print("前3行数据：\n", df.head(3))

# (2) 显示列标签为“学号”和“综合成绩”的数据
selected_columns = df[['学号', '综合成绩']]
print("\n'学号'和'综合成绩'列的数据：\n", selected_columns)

# (3) 将数据框对象数据写入DataFrame2.csv文件，GBK编码
df.to_csv('DataFrame2.csv', encoding='GBK', index=False)
