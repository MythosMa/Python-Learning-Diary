# 求输入数字的平方，如果平方运算后小于 50 则退出

while True:
    inputNumber = int(input("请输入一个数："))
    cul = inputNumber ** 2
    print(f"{inputNumber}的平方是：{cul}")
    if cul < 50:
        print(f"这次计算结果小于50，退出程序")
        break