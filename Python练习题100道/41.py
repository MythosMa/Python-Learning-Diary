# 模仿静态变量的用法，使用类属性实现

class MyClass:
    static_value = 0

    def __init__(self, value) -> None:
        self.class_value = value

    def staticAdd(self):
        MyClass.static_value += 1

classA = MyClass(10)
classA.staticAdd()
print(classA.class_value)
print(classA.static_value)
classB = MyClass(20)
classB.staticAdd()
print(classB.class_value)
print(classB.static_value)
