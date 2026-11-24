Income = int(input("Enter the income: "))

if Income <= 20000:
    tax = 0.02 * Income
    print("Tax payable is:", tax)

elif Income <= 50000:
    tax = 400 + 0.025 * (Income - 20000)
    print("Tax payable is:", tax)

else:
    tax = 1150 + 0.035 * (Income - 50000)
    print("Tax payable is:", tax)