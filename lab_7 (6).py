a = [0, 0, 0, 0, 0]

while True:
    n = int(input("Enter number: "))

    if n == -1:
        break

    if n >= 1 and n <= 2:
        a[0] = a[0] + 1
    elif n >= 3 and n <= 4:
        a[1] = a[1] + 1
    elif n >= 5 and n <= 6:
        a[2] = a[2] + 1
    elif n >= 7 and n <= 8:
        a[3] = a[3] + 1
    elif n >= 9 and n <= 10:
        a[4] = a[4] + 1

total = sum(a)

groups = ["1-2", "3-4", "5-6", "7-8", "9-10"]

for i in range(5):
    if total > 0:
        p = a[i] * 100 / total
    else:
        p = 0

    print(groups[i], "# " * a[i], format(p, ".2f"), "%")