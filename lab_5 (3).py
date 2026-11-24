n = int(input("Enter N: "))

a = 0
b = 0

while True:
    num = int(input("Enter number: "))

    if num == -999:
        break

    if num % n == 0:
        a = a + 1
    else:
        b = b + 1

print("Divisible numbers =", a)
print("Non-divisible numbers =", b)