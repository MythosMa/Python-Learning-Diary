# 编写input()和output()函数输入，输出5个学生的数据记录




def inputData(result):
    data = []
    name =  input("请输入学生姓名：")
    a =  int(input(f"请输入{name}的数学成绩："))
    b =  int(input(f"请输入{name}的语文成绩："))
    c =  int(input(f"请输入{name}的英语成绩："))
    data.append(f"姓名：{name}")
    data.append(f"数学成绩：{a}")
    data.append(f"语文成绩：{b}")
    data.append(f"英语成绩：{c}")
    result.append(data)

def outputData(data):
    print(data)

result = []
count = int(input("请输入学生数量："))
for i in range(count):
    inputData(result)

for i in range(count):
    outputData(result[i])