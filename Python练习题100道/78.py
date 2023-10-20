# 找到年龄最大的人，并输出

persons = {"a": 50, "b": 62, "c": 18, "d": 24}

targetKey = ""
targetValue = -1

for key, value in persons.items():
    if value > targetValue:
        targetKey, targetValue = key, value

print(f"{targetKey}:{targetValue}")
