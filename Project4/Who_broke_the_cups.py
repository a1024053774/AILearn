def check_statements(answer):
    correct_count = 0
    # 检查甲的陈述：不是我
    if answer != '甲':
        correct_count += 1
    # 检查乙的陈述：是丙
    if answer == '丙':
        correct_count += 1
    # 检查丙的陈述：是丁
    if answer == '丁':
        correct_count += 1
    # 检查丁的陈述：丙在胡说
    if answer != '丙':
        correct_count += 1
    return correct_count

# 构造答案空间
answer_space = ['甲', '乙', '丙', '丁']
right_answer = ''

# 逐一测试答案
for answer in answer_space:
    correct_count = check_statements(answer)
    if correct_count == 3:
        right_answer = answer
        break

if right_answer:
    print(f'打翻杯子的是：{right_answer}')
else:
    print('无法推理出谁打翻了杯子！')
