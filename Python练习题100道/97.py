# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止

file_name = input("请输入文件名：")

# 打开文件以写入模式
with open(file_name, 'w') as file:
    while True:
        char = input("请输入一个字符（输入 '#' 退出）: ")
        if char == '#':
            break
        file.write(char)

print("字符已写入文件", file_name)