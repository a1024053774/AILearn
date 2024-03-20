#任务2:此处需自定义一个函数judge_repeat()
def judge_repeat(item, list_real):
    if item in list_real:
        return 1
    else:
        return 0

# 对已经整理好的综合数据库real_list进行最终的结果判断
def judge_last(list):
    for i in list:
        if (i == '23'):
            for i in list:
                if (i == '12'):
                    for i in list:
                        if (i == '21'):
                            for i in list:
                                if (i == '13'):
                                    print("黄褐色，有斑点,哺乳类，食肉类->金钱豹\n")
                                    print("所识别的动物为金钱豹")
                                    return 0
                                elif (i == '14'):
                                    print("黄褐色，有黑色条纹，哺乳类，食肉类->虎\n")
                                    print("所识别的动物为虎")
                                    return 0
        elif (i == '24'):
            for i in list:
                if (i == '13'):
                    for i in list:
                        if (i == '15'):
                            for i in list:
                                if (i == '16'):
                                    print("有斑点，有黑色条纹，长脖，蹄类->长颈鹿\n")
                                    print("所识别的动物为长颈鹿")
                                    return 0
        elif (i == '14'):
            for i in list:
                if (i == '24'):
                    print("有黑色条纹，蹄类->斑马\n")
                    print("所识别的动物为斑马")
                    return 0
        elif (i == '20'):
            for i in list:
                if (i == '22'):
                    print("善飞，鸟类->信天翁\n")
                    print("所识别的动物为信天翁")
                    return 0
        elif (i == '22'):
            for i in list:
                if (i == '4'):
                    for i in list:
                        if (i == '15'):
                            for i in list:
                                if (i == '16'):
                                    print("不会飞，长脖，长腿，鸟类->鸵鸟\n")
                                    print("所识别的动物为鸵鸟")
                                    return 0
                elif (i == '18'):
                    for i in list:
                        if (i == '19'):
                            print("会游泳，黑白二色，鸟类->企鹅\n")
                            print("所识别的动物为企鹅")
                            return 0
#任务3:此处增加企鹅识别模块,并尝试运行代码进行试验,展示结果


        else:
            if (list.index(i) != len(list) - 1):
                continue
            else:
                print("\n根据所给条件无法判断为何种动物")

dict_before = {'1': '有毛发', '2': '产奶', '3': '有羽毛', '4': '不会飞', '5': '会下蛋', '6': '吃肉', '7': '有犬齿',
               '8': '有爪', '9': '眼盯前方', '10': '有蹄', '11': '反刍', '12': '黄褐色', '13': '有斑点', '14': '有黑色条纹',
               '15': '长脖', '16': '长腿', '17': '会飞', '18': '会游泳', '19': '黑白二色', '20': '善飞', '21': '哺乳类',
               '22': '鸟类', '23': '食肉类', '24': '蹄类', '25': '金钱豹', '26': '虎', '27': '长颈鹿', '28': '斑马',
               '29': '鸵鸟', '30': '企鹅', '31': '信天翁'}
print('''输入对应条件前面的数字:
                                *******************************************************
                                * 1:有毛发   2:产奶     3:有羽毛   4:不会飞      5:会下蛋   *
                                * 6:吃肉     7:有犬齿   8:有爪     9:眼盯前方    10:有蹄    *
                                * 11:反刍    12:黄褐色  13:有斑点  14:有黑色条纹  15:长脖   *
                                * 16:长腿    17:会飞  18:会游泳  19:黑白二色    20:善飞    *
                                * 21:哺乳类  22:鸟类    23:食肉类  24:蹄类                *
                                *******************************************************
                                *******************当输入数字0时!程序结束******************
     ''')

# 综合数据库
list_real = []
while (1):
    # 循环输入前提条件所对应的字典中的键
    num_real = input("请输入：")
    list_real.append(num_real)
    # if (任务1:此处需要编码, 输入0 时结束循环):
    if (num_real == '0'):
        break
    else:
        continue

print("\n")
print("前提条件为：")
# 输出前提条件

for i in range(0, len(list_real) - 1):
    print(dict_before[list_real[i]], end=" ")
print("\n")
print("推理过程如下：")

# 遍历综合数据库list_real中的前提条件,存入推理中间结果,综合数据库已有事实则不再添加
for i in list_real:
    if (i == '1'):
        if (judge_repeat('21', list_real) == 0):  #查看list_real中有没有 21
            list_real.append('21')
            print("有毛发->哺乳类")
    elif (i == '2'):
        if (judge_repeat('21', list_real) == 0): #查看list_real中有没有 21
            list_real.append('21')
            print("产奶->哺乳类")
    elif (i == '3'):
        if (judge_repeat('22', list_real) == 0):  #查看list_real中有没有 22
            list_real.append('22')
            print("有羽毛->鸟类")
    elif (i == '17'):
        for i in list_real:
            if (i == '5'):
                if (judge_repeat('22', list_real) == 0):
                    list_real.append('22')
                    print("会飞，会下蛋->鸟类")

    elif (i == '6'):
        if (judge_repeat('23', list_real) == 0):
            list_real.append('23')
            print("食肉->食肉类")

    elif (i == '7'):
        for i in list_real:
            if (i == '8'):
                for i in list_real:
                    if (i == '9'):
                        if (judge_repeat('23', list_real) == 0):
                            list_real.append('23')
                            print("有犬齿,有爪,眼盯前方->食肉类")
    elif (i == '10'):
        for i in list_real:
            if (i == '21'):
                if (judge_repeat('24', list_real) == 0):
                    list_real.append('24')
                    print("有蹄，哺乳类->蹄类")
    elif (i == '11'):
        for i in list_real:
            if (i == '21'):
                if (judge_repeat('24', list_real) == 0):
                    list_real.append('24')
                    print("反刍，哺乳类->蹄类")
    else:
        if (list_real.index(i) != len(list_real) - 1):
            continue
        else:
            break
#任务4: 根据给定规则，修正以下代码存在的错误============
# for i in list_real:
#     if (i == '17'):
#         for i in list_real:
#             if (i == '5'):
#                 if (judge_repeat('22', list_real) == 0):
#                     list_real.append('22')
#                     print("会飞，会下蛋->鸟类")
#
#     elif (i == '6'):
#         if (judge_repeat('23', list_real) == 0):
#             list_real.append('23')
#             print("食肉->食肉类")
#
#     elif (i == '7'):
#         for i in list_real:
#             if (i == '8'):
#                 for i in list_real:
#                     if (i == '9'):
#                         if (judge_repeat('23', list_real) == 0):
#                             list_real.append('23')
#                             print("有犬齿,有爪,眼盯前方->食肉类")
#     elif (i == '10'):
#         for i in list_real:
#             if (i == '21'):
#                 if (judge_repeat('24', list_real) == 0):
#                     list_real.append('24')
#                     print("有蹄，哺乳类->蹄类")
#     elif (i == '11'):
#         for i in list_real:
#             if (i == '21'):
#                 if (judge_repeat('24', list_real) == 0):
#                     list_real.append('24')
#                     print("反刍，哺乳类->蹄类")
#     else:
#         if (i != len(list_real) - 1):
#             continue
#         else:
#             break

#任务5:思考题: 上面两个for循环是否可以简单地将第二个for循环中的elif分支挪到第一个for循环中,整合实现只用一个for循环? 为什么?

judge_last(list_real)

