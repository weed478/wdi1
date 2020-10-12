a = 1
b = 1

while a < 1000000:
    print(a)
    a, b = b, a + b
    # b = a + b
    # a = b - a

