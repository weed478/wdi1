a = -1
while a < 0:
    try:
        a = float(input("Enter number: "))
    except ValueError:
        print("Not a number")
        continue

    if a < 0:
        print("Cannot be negative")

"""
x_k+1 = 0.5 * (x_k + a / x_k)
"""

x = 1
epsilon = 10e-10

while True:
    new_x = 0.5 * (x + a / x)

    if abs(new_x - x) < epsilon:
        x = new_x
        break

    x = new_x

print("sqrt({}) = {}".format(a, x))

from math import sqrt
assert abs(sqrt(a) - x) < epsilon
