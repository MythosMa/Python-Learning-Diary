# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5

def cal(n):
    origin = n
    results = []
    divider = 2
    for divider in range(2, origin):
        while n % divider == 0:
            results.append(divider)
            n /= int(divider)
        if n <= 1:
            break
    return results


def printFormat(n, results):
    resultString = "*".join([str(number) for number in results])
    print(f"{n}={resultString}")


inputNumber = int(input("请输入一个正整数："))
results = cal(inputNumber)
if len(results) == 0:
    print(inputNumber, "是素数")
else:
    printFormat(inputNumber, results)