# 输出一个随机数
import random

print(random.random()) # [0, 1) 的浮点数
print(random.randint(1, 10)) # [1, 10] 的整数
print(random.uniform(1, 10)) # [1, 10] 的浮点数
print(random.choice([1, 2, 3, 4, 5, 6, 7])) # 随机返回数组其中一个数

seq = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(seq) # 随机打乱数组顺序
print(seq)

print(random.sample(seq, 5)) # 随机取5个数

print(random.randrange(1, 10, 2)) # 随机取 [1, 10)的整数，以2为间隔，即 1, 3, 5, 7, 9中取

random.seed(a=None) # 重置随机种子