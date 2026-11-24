n = int(input("Enter a number: "))

fact = 1

if n < 0:
    print("Invalid input")
else:
    while n > 0:
        fact = fact * n
        n = n - 1

    print("Factorial =", fact)