# 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中

fp = open("test-1.txt")
a = fp.read()
fp.close()

fp = open("test-2.txt")
b = fp.read()
fp.close()

c = list(a + b)
c.sort()

file_name = "test-3.txt"

with open(file_name, 'w') as file:
    file.write("".join(c))

print("字符已写入文件", file_name)