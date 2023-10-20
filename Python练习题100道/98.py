# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存

file_name = input("请输入文件名：")
str = input("请输入一个字符串: ")

# 打开文件以写入模式
with open(file_name, 'w') as file:
    file.write(str.upper())

print("字符已写入文件", file_name)