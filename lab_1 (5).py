x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x <= 0 or y <= 0:
    print("Invalid input")

elif y % x == 0:
    print("Y is divisible by X")

else:
    print("Y is not divisible by X")