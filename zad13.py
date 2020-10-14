def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def nww(a, b):
    return int(a * b / nwd(a, b))


a = int(input('a: '))
b = int(input('b: '))
c = int(input('b: '))

print(nww(nww(a, b), c))
