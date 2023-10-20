# 输入一个奇数，然后判断最少几个 9 除于该数的结果为整数

inputNum = int(input("请输入一个奇数:"))

sum = 0
a = 9
b = 1
count = 0

while b:
    sum, a, count = sum + a, a * 10, count + 1
    b = sum % inputNum

print(f"{count}个9组成的{sum}可以被{inputNum}整除，答案是{sum}/{inputNum}={int(sum / inputNum)}")