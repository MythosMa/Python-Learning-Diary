# 求0—7所能组成的奇数个数

# 奇数取决于个位数 -> 个位数时 1 3 5 7 四个
#                   十位数时 十位数有1-7 所以是 7 * 4
#                    百位数时 有 百位 1-7  十位 0-7 所以是 7 * 8 * 4
#                    千位 7 * 8 * 8 * 4

max = 100000
numStr = f"{max}"

sum = 4
start = 4
for i in range(2 , len(numStr)):
    if i <= 2:
        start *= 7
    else:
        start *= 8
    
    sum += start

print(sum)