n = int(input("Enter first number: "))
m = int(input("Enter second number: "))

temp = n
rev = 0

while temp > 0:
    d = temp % 10
    rev = rev * 10 + d
    temp = temp // 10

if rev == m:
    print("Reverse numbers")
else:
    print("Not reverse numbers")