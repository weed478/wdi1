def e_gen(n):
    total = 1
    m = 1

    for n in range(n):
        m /= (n + 1)
        total += m
        print(total)

    return total


print(e_gen(10))
