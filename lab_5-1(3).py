n = int(input("Enter limit: "))

large = 0
small = 0

while True:
    bill = int(input("Enter bill: "))

    if bill == -999:
        break

    if bill > n:
        large = large + 1
    else:
        small = small + 1

print(large)
print(small)