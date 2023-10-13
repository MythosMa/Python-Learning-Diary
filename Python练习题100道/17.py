# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

inputStr = input("随便输入一串字符：")
letterCount = 0
spaceCount = 0
numberCount = 0
otherCount = 0

for char in inputStr:
    if char.isalpha():
        letterCount += 1
    elif char.isspace():
        spaceCount += 1
    elif char.isdigit():
        numberCount += 1
    else:
        otherCount += 1

print(f"letters: {letterCount}, spaces: {spaceCount}, numbers: {numberCount}, ohters: {otherCount}")