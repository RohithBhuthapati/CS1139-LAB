n = int(input("Enter N: "))

for i in range(1, n + 1):
    temp = i
    sum = 0
    digits = len(str(i))

    while temp > 0:
        r = temp % 10
        sum = sum + r ** digits
        temp = temp // 10

    if sum == i:
        print(i)