a1 = 1
b1 = 1
a2 = 1
b2 = 1

targetSum = int(input("> "))

sequenceSum = 0

while a1 <= targetSum:
    if sequenceSum == targetSum:
        print("Found")
        exit(0)

    sequenceSum += a1

    b1 = a1 + b1
    a1 = b1 - a1

    while sequenceSum > targetSum:
        sequenceSum -= a2
        b2 = a2 + b2
        a2 = b2 - a2

print("Not found")
