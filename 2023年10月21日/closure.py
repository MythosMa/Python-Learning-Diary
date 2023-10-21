def createCount():
    a = 0
    def add():
        nonlocal a
        a = a + 1
        return a
    return add

a = createCount()
b = createCount()
print(a(), a(), a(), a(), a())
print(b(), b(), b())