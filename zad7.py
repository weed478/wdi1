while True:
    number = int(input("Enter number: "))
    if number < 1:
        print("Must be > 0")
    else:
        break

a = 1
b = 1

while a * b < number:
    a, b = b, a + b

if a * b == number:
    print("No jest i fajnie")
else:
    print("Nie jest")
