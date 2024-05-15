def check_answers(answer):
    correct_count = 0
    # 判断A的说话正确成分
    if answer != '湖南人' and answer == '河南人':
        correct_count += 1
    elif answer != '湖南人' or answer == '河南人':
        correct_count += 0.5
    # 判断B的说话正确成分
    if answer != '河南人' and answer == '湖南人':
        correct_count += 1
    elif answer != '河南人' or answer == '湖南人':
        correct_count += 0.5
    # 判断C的说话正确成分
    if answer != '河南人' and answer != '河北人':
        correct_count += 1
    elif answer != '河南人' or answer != '河北人':
        correct_count += 0.5

    return correct_count

# 构造答案空间
answer_space = ['湖南人', '河南人', '河北人', '其他省人']
right_answer = 0

# 逐一测试答案
for answer in answer_space:
    correct_count = check_answers(answer)
    if correct_count == 1.5:
        print(answer)
        right_answer = 1  # 设置命中答案的标志为1
        break
if right_answer == 0:
    print(f'无法推理出小王来自哪个省！')
