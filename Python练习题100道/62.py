# 查找字符串

strA = input("请输入一个字符串：")
strB = input("请输入需要查找的字符串：")

print("找到了" if strA.find(strB) != -1 else "没找到")