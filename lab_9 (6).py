menu = input().split()
prices = list(map(int, input().split()))
orders = input().split()

total = 0

for i in range(len(menu)):
    count = 0

    for item in orders:
        if item == menu[i]:
            count += 1

    if count > 0:
        cost = count * prices[i]
        print(menu[i], "x", count, "=", cost)
        total += cost

print("Total:", total)