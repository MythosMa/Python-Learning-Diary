# 使用lambda来创建匿名函数

PRINT_LAMBDA = lambda n : print(f"得到了{n}")
ADD_LAMBDA = lambda x, y : x + y

PRINT_LAMBDA(ADD_LAMBDA(1, 2))