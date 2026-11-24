cost = int(input("Enter cost: "))
rev = int(input("Enter revenue: "))

if cost == rev:
    print("Break even")

elif cost < rev:
    profit = rev - cost
    print("Profit:", profit)

else:
    loss = cost - rev
    print("Loss:", loss)