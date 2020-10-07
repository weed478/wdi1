"""
a + b = c
b + c = d
c + d = year

c + (b + c) = year
(a + b) + (b + (a + b)) = year

x * a + y * b = year
y * b = year - x * a
b = (year - x * a) / y

a
b
a + b
a + 2b
2a + 3b
3a + 5b
5a + 8b
8a + 13b ; a = 9 b = 3
"""

year = 2020

x = 1
y = 1

lowestSum = -1
foundA = -1

while year > x:
    a = 0
    while year > x * a:
        a += 1
        b = (year - x * a) / y

        if (year - x * a) % y == 0:
            b = int(b)
            if lowestSum < 0:
                lowestSum = a + b
                foundA = a

            elif a + b < lowestSum:
                lowestSum = a + b
                foundA = a

    y = x + y
    x = y - x

if lowestSum < 0:
    print("Not found")
else:
    print("a={}\tb={}".format(foundA, lowestSum - foundA))
