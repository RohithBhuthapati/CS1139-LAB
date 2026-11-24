pound = float(input("Enter the number of pounds of apples: "))

cash = float(input("Enter the amount of cash tendered: "))

cost = pound * 2.5

if cash >= cost:
    change = cash - cost
    print("Change:", change)

else:
    amount_owed = cost - cash
    print("You are owed:", amount_owed)