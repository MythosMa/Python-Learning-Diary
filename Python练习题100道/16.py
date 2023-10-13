# 输出指定格式的日期

import datetime

# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print(datetime.date.today().strftime('%d/%m/%Y'))
 
# 创建日期对象
myBirthday = datetime.date(1988, 11, 17)
 
print(myBirthday.strftime('%d/%m/%Y'))
 
# 日期算术运算
myBirthdayNextDay = myBirthday + datetime.timedelta(days=1)
 
print(myBirthdayNextDay.strftime('%d/%m/%Y'))
 
# 日期替换
myBirthdayNextYear = myBirthday.replace(year=myBirthday.year + 1)
 
print(myBirthdayNextYear.strftime('%d/%m/%Y'))