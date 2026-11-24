x = int(input("Enter X: "))
y = int(input("Enter Y: "))
n = int(input("Enter N: "))

for i in range(x + 1, y + 1):
    if i % n == 0:
        print(i)