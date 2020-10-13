from math import sqrt


def series_a(a, b):
    return sqrt(a * b)


def series_b(a, b):
    return 0.5 * (a + b)


def average(a, b):
    epsilon = 10e-10

    while abs(a - b) > epsilon:
        a, b = series_a(a, b), series_b(a, b)

    return (a + b) * 0.5


num_a = 24
num_b = 6
avg = average(num_a, num_b)
print("Średnia geometryczna {} i {} = {}".format(num_a, num_b, avg))
