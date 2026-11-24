n = int(input("Enter number: "))
d = int(input("Enter digit: "))

count = 0

if n > 0 and 0 <= d <= 9:
    while n > 0:
        r = n % 10

        if r == d:
            count = count + 1

        n = n // 10

    print("Count =", count)
else:
    print("Invalid input")