import datetime


# wedlug zadania
def f(x):
    return (x % 2) * (3 * x + 1) + (1 - x % 2) * x / 2


# optymalizacja
def g(x):
    if (x % 2) == 0:
        return x / 2, 1
    return (3 * x + 1) / 2, 2


def ciong(a):
    steps = 0

    while a != 1:
        a, _temp = g(a)  # optimized
        steps += _temp

    return steps


max_steps = 0
number = 0

start = datetime.datetime.now()

for i in range(2, 10000, 1):
    steps = ciong(i)
    if steps > max_steps:
        max_steps = steps
        number = i

finish = datetime.datetime.now()
print(finish - start)

print("For value {}, maximum steps = {}".format(number, max_steps))
