# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高

# 解法一
allDistance = 0
start = 100

for i in range(1, 11):
    if i == 1:
        allDistance += start
    else:
        start /= 2
        allDistance += start * 2

print("第10次落地共经过", allDistance, "米")
print("第10次反弹", start / 2, "米")

# 解法2
down = [100.0]
up = [50]

for i in range(2, 11):
    down.append(down[i - 2] / 2)
    up.append(up[i - 2] / 2)

print("第10次落地共经过", sum(down[:10]) + sum(up[:9]), "米")
print("第10次反弹", up[9], "米")