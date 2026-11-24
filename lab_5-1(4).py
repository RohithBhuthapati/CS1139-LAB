n = int(input("Enter number: "))
p = int(input("Enter power: "))

if n > 0 and p > 0:
    result = 1
    i = 1

    while i <= p:
        result = result * n
        i = i + 1

    print("Answer =", result)
else:
    print("Invalid input")