chars = ["bbbb", "cccc", "aaaa", "dddd"]
# sorted不会修改原数组
print(sorted(chars))
print(sorted(chars, reverse=True))
print(chars)
# 调用数组的sort会改变原数组
chars.sort()
print(chars)
chars.sort(reverse=True)
print(chars)

print(len(chars))

for char in chars:
    print("This is a letter:" + char)

print("=========")

for value in range(1, 4):
    print(value)

print("=========")

for value in range(1, 5):
    print(value)

print("=========")

numbers = list(range(1, 5))
print(numbers)

print("=========")

numbers = list(range(1, 11, 2))
print(numbers)

print("=========")
numbers = [1, 3, 5, 7, 2, 4, 6, 8, 9, 10]
min = min(numbers)
max = max(numbers)
sum = sum(numbers)
print(min)
print(max)
print(sum)
