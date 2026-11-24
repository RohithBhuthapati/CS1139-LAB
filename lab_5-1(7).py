n = int(input("Enter number: "))

s = 0
i = 1

if n > 0:
    while i * i <= n:
        if n % i == 0:
            s = s + i

            if i != n // i and n // i != n:
                s = s + n // i

        i = i + 1

    if s == n:
        print("Perfect number")
    else:
        print("Not a perfect number")
else:
    print("Invalid number")