def factors(number):
    factor = 2
    while factor*factor < number:
        div, mod = divmod(number, factor)
        if mod == 0:
            print(factor)
            number = div
            factor = 2
            continue

        factor += 1

    print(number)


n = -1
while True:
    n = int(input("Enter number: "))
    if n < 1:
        print("Must be > 0")
    else:
        break

factors(n)
