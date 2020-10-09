"""
x^x = 2020
x^x - 2020 = 0
"""


def f(x):
    return pow(x, x) - 2020


eps = 10e-5
a = 4.5  # f(a) < 0
b = 5    # f(b) > 0


while abs(a - b) > eps:
    mid = (a + b) / 2

    if f(mid) < 0:
        a = mid
    else:
        b = mid

x = (a + b) / 2
print("x = {}".format(x))

approxX = 4.832
assert (abs(approxX - x) < 10e-3)
