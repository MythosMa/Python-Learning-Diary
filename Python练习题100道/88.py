# 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊
import random

array = []
for i in range(1, 51):
    array.append(i)

random.shuffle(array)
array = array[:7]

for i in array:
    print(f"{i} -> " + "*" * i)