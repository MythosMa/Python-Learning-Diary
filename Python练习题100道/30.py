# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

inputNumber = int(input("请输入一个5位数的正整数："))
numberStr = str(inputNumber)
flag = True

for i in range(2):
    if numberStr[i] != numberStr[-i - 1]:
        flag = False
        break
if flag:
    print(f"{inputNumber}是回文数")
else:
    print(f"{inputNumber}不是回文数")