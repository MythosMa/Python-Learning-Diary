# 求1+2!+3!+...+20!的和。

t = 1
sum = 0
for i in range(1, 21):
    t *= i
    sum += t

print(sum)
