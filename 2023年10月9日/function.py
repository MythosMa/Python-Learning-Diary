def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end="  | ")
        a, b = b, a + b

# fib(100)


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
    print("========================================================================")

# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# def foo(name, /, **kwds):
#     return 'name' in kwds

# # print(foo(1, name=2))

# pool = [1, 2, 3, 4, 5, 6, 7]

# def roundPlay():
#     result = pool[2:]
#     pool = pool[:2]

# roundPlay()
# print(pool)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[:9])
