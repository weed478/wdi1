def is_ideal(number):
    if number == 1:
        return False

    factor_sum = 1
    x = 2
    while x * x < number:
        div, mod = divmod(number, x)
        if mod == 0:
            factor_sum += x
            if x != div:
                factor_sum += div
        x += 1

    return factor_sum == number


def is_prime(n):
    if n <= 1 or n % 2 == 0:
        return False
    i = 2
    while i <= n / 2:
        if n % i == 0:
            return False
        i += 1

    return True


def gen_perfect(n):
    i = 1
    while True:
        num = 2 ** i - 1
        num2 = num * pow(2, i - 1)
        if not num2 <= n:
            break
        if is_prime(num):
            print("{} jest wspaniałe".format(num2))
        i += 1


# too slow someone help :(
for i in range(10000):
    if is_ideal(i):
        print("{} jest wspaniałe".format(i))

print("=========================")

# faster
gen_perfect(100000000000000000)
