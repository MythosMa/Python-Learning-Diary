# 有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中

a = [4, 5, 8, 11, 23, 27, 66, 89, 435, 879, 9264]
inputNum = int(input("请输入一个数："))

start = 0
end = len(a) - 1

if inputNum > a[end]:
    a.append(inputNum)
else:
    while start != end:
        index = int((start + end) / 2)
        if a[index] < inputNum:
            start = index if start != index else index + 1
        else:
            end = index
    a.insert(start, inputNum)

print(a)
