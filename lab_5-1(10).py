n = int(input("Enter number: "))

count = 0
i = 1

if n > 0:
    while i <= n:
        if n % i == 0:
            print(i)
            count = count + 1

        i = i + 1

    print("Total divisors =", count)

    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")
else:
    print("Invalid number")