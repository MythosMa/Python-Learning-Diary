# 求一个3*3矩阵主对角线元素之和。

a = [
     [1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]
    ]

sum = 0
for i in range(len(a[0])):
    sum += a[i][i]

print(sum)