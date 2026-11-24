v = float(input("Enter water: "))
n = int(input("Enter days: "))

if v >= 0 and n >= 0:
    v = 200 + (v - 200) * (0.95 ** n)
    print("Water =", v)
else:
    print("Invalid input")