n = int(input("Enter a number: "))

octal = ""

while n > 0:
    r = n % 8
    octal = str(r) + octal
    n = n // 8

print("Octal =", octal)