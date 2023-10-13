# 输出 9*9 乘法口诀表

for i in range(1, 10):
    list = []
    for j in range(i, 10):
        result = str(i) + "*" + str(j) + "=" + str(i * j)
        list.append(result)
    print(list, end="\n")