# 打印出杨辉三角形
# 1
# 1 1 
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

count = 10
result = []
for i in range(count):
    result.append([])
    for j in range(i + 1):
        result[i].append(0)

for i in range(count):
    result[i][0] = 1
    result[i][len(result[i]) - 1] = 1

for i in range(2, count):
    for j in range(1, len(result[i]) - 1):
        result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

for i in range(count):
    print(" ".join([str(strNum) for strNum in result[i]]))
