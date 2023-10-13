# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制

a = int(input("请输入a："))
n = int(input("请输入n："))

sum = 0
numbers = []

for i in range(1, n + 1):
    if i == 1:
        numbers.append(a)
        sum = a
    else:
        numbers.append(numbers[i - 2] * 10 + a)
        sum += numbers[i - 2] * 10 + a

print(f"{'+'.join([str(number) for number in numbers])}={sum}")