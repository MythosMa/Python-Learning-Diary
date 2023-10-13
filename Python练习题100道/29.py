# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字

inputNumber = int(input("请输入一个不多于5位数的正整数："))
count = 0
result = []
for i in range(1, 6):
    result.append(inputNumber % 10)
    if inputNumber < 10:
        count = i
        break
    inputNumber = int(inputNumber / 10)

print(f"这是一个{count}位数")
print(f"从个位开始各个位数分别是{result}")


