# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

def printLevel(score):
    if score >= 90:
        print("A")
    elif score >= 60:
        print("B")
    else:
        print("C")

printLevel(int(input("请输入分数:")))