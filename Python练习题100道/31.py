# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母

index = 1
chars = []
while True:
    inputChar = input(f"请输入第{index}个字母：")
    chars.append(inputChar.upper())
    match chars:
        case ["M"]:
            print("星期一")
            break
        case ["T", "U"]:
            print("星期二")
            break
        case ["W"]:
            print("星期三")
            break
        case ["T", "H"]:
            print("星期四")
            break
        case ["F"]:
            print("星期五")
            break
        case ["S", "A"]:
            print("星期六")
            break
        case ["S", "U"]:
            print("星期日")
            break
        case ["T"] | ["S"]:
            index += 1
        case _ :
            print("输入有误")
            chars.pop()


