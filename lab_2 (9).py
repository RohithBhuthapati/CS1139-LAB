widget = int(input("Enter widgets ordered: "))

if widget >= 100:
    cost = widget * 0.20

else:
    cost = widget * 0.25

print("Cost:", cost)