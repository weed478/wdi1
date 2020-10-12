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


n = 137438691328
print("{} {}jest wspaniałe"
      .format(n, "" if is_ideal(n) else "nie "))
