a = int(input("a: "))
b = int(input("b: "))
n = int(input("c: "))


def beep(a, b, n):
    for n in range(n):
        print(b / a)
        a, b = b, a + b


beep(a, b, n)
