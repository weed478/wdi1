import math


def is_prime(number):
    if number == 2 or 3:
        return True

    if number < 2 or (number % 2 == 0 or number % 3 == 0):
        return False

    root = math.sqrt(number)
    x = 5
    while x <= root:
        if number % x == 0:
            return False
        x += 2
        if number % x == 0:
            return False
        x += 4

    return True


while True:
    num = int(input("Enter number: "))
    print("Is prime" if is_prime(num) else "Is not prime")
