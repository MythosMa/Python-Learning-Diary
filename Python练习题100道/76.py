# 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

def fn(n, start):
    sum = 0
    for i in range(2 - start, n + 1, 2):
        sum += 1 / i
    return sum

n = int(input("请输入一个数："))
print(fn(n, n % 2))