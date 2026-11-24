n = int(input("Enter 5 digit number: "))

if 10000 <= n <= 99999:
    a = n // 10000
    b = (n // 1000) % 10
    c = (n // 100) % 10
    d = (n // 10) % 10
    e = n % 10

    largest = a
    pos = 1

    if b > largest:
        largest = b
        pos = 2
    if c > largest:
        largest = c
        pos = 3
    if d > largest:
        largest = d
        pos = 4
    if e > largest:
        largest = e
        pos = 5

    print("Largest digit =", largest)
    print("Position =", pos)
else:
    print("Invalid number")