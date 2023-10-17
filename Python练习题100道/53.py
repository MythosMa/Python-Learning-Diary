# 学习使用按位异或 ^ 。

# 0^0=0; 0^1=1; 1^0=1; 1^1=0

def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return (a, b)

print(swap(10, 20))
