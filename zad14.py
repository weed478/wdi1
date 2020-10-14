# Wartosci pochodnych cos(x)
#
# cos'(x) = -sin(x)
# cos''(x) = -cos(x)
# cos'''(x) = sin(x)
# cos''''(x) = cos(x)
#
# cos(0) = 1
# cos'(0) = 0
# cos''(0) = -1
# cos'''(0) = 0
#
# cos(x) = 1 + 0*x - 1(1/2!)*x^2 + 0(1/3!)*x^3 +1(1/4!)*x^4
# cos(x) = 1 - (1/2!)*x^2 + (1/4!)*x^4 - (1/6!)&x^6 + (1/8!)*x^8
#

import math

n = -1.0
x = -1.0
while n < 0:
    try:
        x = float(input("Enter x (arg of cos): "))
        n = int(input("Enter n (accuracy): "))
    except ValueError:
        print("Not a number")
        continue

    if n < 0:
        print("n > 0   plz")


def cos_maclaurin(x, n):
    total = 1.0
    last = 1

    for i in range(n):
        last = last * (-1) * (x * x) / ((2 * i + 1) * (2 * i + 2))
        total += last
    return total


print("Lib.math = {:.7}".format(math.cos(x)))
print("cos_maclaurin = {:.7}".format(cos_maclaurin(x, n)))
