# 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组

count = int(input("输入数组长度："))
numbers = []
for i in range(count):
    numbers.append(int(input("请输入一个数字：")))

maxIndex = 0
for i in range(1, count):
    if numbers[maxIndex] < numbers[i]:
        maxIndex = i

if maxIndex != 0:
    numbers[0], numbers[maxIndex] = numbers[maxIndex], numbers[0]

minIndex = 0
for i in range(1, count):
    if numbers[minIndex] > numbers[i]:
        minIndex = i

if minIndex != count - 1:
    numbers[count - 1], numbers[minIndex] = numbers[minIndex], numbers[count - 1]

print(numbers)