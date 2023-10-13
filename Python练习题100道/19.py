# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
from functools import reduce

def cal(n):
    results = []
    for i in range(1, n):
        if n % i == 0:
            results.append(i)
    if len(results) > 0 and reduce(lambda x,y : x + y, results) == n:
        return f"{n}={"+".join(str(num) for num in results)}"
    return False

results = []
for i in range(2, 1001):
    result = cal(i)
    if result:
        results.append(result)

print(results)