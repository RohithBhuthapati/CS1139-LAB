n = int(input())

stock = {}

for i in range(n):
    item, qty = input().split()
    stock[item] = int(qty)

q = int(input())

for i in range(q):
    a = input().split()

    action = a[0]
    item = a[1]
    qty = int(a[2])

    if action == "SELL":
        if stock[item] >= qty:
            stock[item] -= qty
        else:
            print("Insufficient stock:", item)

    elif action == "ADD":
        if item in stock:
            stock[item] += qty
        else:
            stock[item] = qty

for item in stock:
    print(item, stock[item])