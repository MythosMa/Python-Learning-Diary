# 有 n 个整数，使其前面各数顺序向后移 m 个位置，最后 m 个数变成最前面的 m 个数

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

m = 5
step = len(a) - m

b = a[:step]
a = a[step:]
a.extend(b)

print(a)