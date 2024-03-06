list1 = ['a', 2, '3', 4, '5', '6']

string_count = sum(isinstance(item, str) for item in list1)

print(f"字符串的个数是: {string_count}")