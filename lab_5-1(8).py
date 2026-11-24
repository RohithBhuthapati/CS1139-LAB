n = int(input("Enter number of lines: "))

if n > 0:
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end=" ")
        print()
else:
    print("Invalid input")