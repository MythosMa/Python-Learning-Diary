# 斐波那契数列

# def fib(n):
#     if(n == 0):
#         return 0
#     if(n == 1):
#         return 1
#     return fib(n - 1) + fib(n - 2)

def fib(n):
    if(n == 0):
        return 0
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

print(fib(10))
