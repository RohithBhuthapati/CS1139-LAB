n = int(input("Enter a positive number: "))

if n > 0:
    for i in range(1, 21):
        print(n, "x", i, "=", n * i)
else:
    print("Invalid input")