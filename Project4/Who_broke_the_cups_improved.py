def check_statements(answer):
    true_count = 0
    false_count = 0

    # 检查甲的陈述：不是我
    if answer != '甲':
        true_count += 1
    else:
        false_count += 1

    # 检查乙的陈述：是丙
    if answer == '丙':
        true_count += 1
    else:
        false_count += 1

    # 检查丙的陈述：是丁
    if answer == '丁':
        true_count += 1
    else:
        false_count += 1

    # 检查丁的陈述：丙在胡说
    if answer != '丙':
        true_count += 1
    else:
        false_count += 1

    return true_count, false_count

# 构造答案空间
answer_space = ['甲', '乙', '丙', '丁']
possibilities = []

# 逐一测试答案
for answer in answer_space:
    true_count, false_count = check_statements(answer)
    if true_count == 2 and false_count == 2:
        possibilities.append(answer)

if possibilities:
    print(f'可能打翻杯子的有：{possibilities}')
else:
    print('无法推理出谁打翻了杯子！')
