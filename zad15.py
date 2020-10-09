from math import sqrt


# recurrent solution

def whatever(n):
    if n > 0:
        return sqrt(0.5 + 0.5 * whatever(n - 1))
    else:
        return sqrt(0.5)


pi = 1

for i in range(998):
    pi *= whatever(i)

pi = 2 / pi

print("pi = {}".format(pi))
assert abs(pi - 3.141) < 10e-3


# iterating solution

pi = 1
w = sqrt(0.5)

for i in range(10000):
    pi *= w
    w = sqrt(0.5 + 0.5 * w)

pi = 2 / pi

print("pi = {}".format(pi))
assert abs(pi - 3.141) < 10e-3
