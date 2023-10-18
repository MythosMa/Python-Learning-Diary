# 输入3个数a,b,c，按大小顺序输出

a = int(input("请输入数字a："))
b = int(input("请输入数字b："))
c = int(input("请输入数字c："))

result = [a, b, c]
result.sort()

print(" ".join(str(num) for num in result))
