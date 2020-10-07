import math


def is_prime(number):
    if number < 2 or (number % 2 == 0 and number != 2):
        return False

    root = math.sqrt(number)
    x = 3
    while x <= root:
        if number % x == 0:
            return False

        x += 2

    return True


while True:
    num = int(input("Enter number: "))
    print("Is prime" if is_prime(num) else "Is not prime")
