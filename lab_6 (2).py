n = int(input("Enter N: "))

i = 1

while i <= 1000:
    if i % n != 0 or i % 4 == 0:
        i += 1
        continue

    print(i, end=" ")
    i += 1