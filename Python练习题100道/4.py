# 输入某年某月某日，判断这一天是这一年的第几天？

year=int(input("请输入年:"))
month=int(input("请输入月:"))
day=int(input("请输入日:"))

sum = 0

days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
if 0 < month < 13:
    sum += days[month - 1]
else:
    print('月输入错误')
sum += day
if month > 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    sum += 1
print("你输入的时间是这一年的第",sum,"天")
