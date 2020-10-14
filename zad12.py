def nwd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

print(nwd(nwd(a, b), c))


