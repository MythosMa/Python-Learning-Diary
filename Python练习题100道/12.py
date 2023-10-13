# 判断101-200之间有多少个素数，并输出所有素数
from math import sqrt

count = 0
for i in range(101, 201):
    start = 2
    end = int(sqrt(i))
    isResult = True
    for k in range(start, end + 1):
        if i % k == 0:
            isResult = False
            break
    if isResult:
        count += 1
        print(i)
        
print("共有素数:", count, "个")