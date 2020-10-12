def is_ideal(number):
    if number == 1:
        return False

    factor_sum = 1
    x = 2
    while x*x < number:
        div, mod = divmod(number, x)
        if mod == 0:
            factor_sum += x + div
        x += 1

    return factor_sum == number


# too slow someone help :(
for i in range(1000000):
    if is_ideal(i):
        print("{} jest wspaniałe".format(i))
