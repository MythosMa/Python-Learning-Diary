# 打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

max = 7
lineData = [1, 3, 5, 7, 5, 3, 1]

for i in range(max):
    print(" " * int((max - lineData[i]) / 2), end="")
    print("*" * lineData[i])