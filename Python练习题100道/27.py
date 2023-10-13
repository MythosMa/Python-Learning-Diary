# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来

def output(str, result, length):
    if length <= 0:
        return
    result.append(str[length - 1])
    return output(str, result, length - 1)

result = []
inputStr = input("请输入一串字符:")
output(inputStr, result, len(inputStr))
print("".join(result))