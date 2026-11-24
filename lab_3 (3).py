a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))

if a <= 0 or b <= 0 or c <= 0 or a+b+c != 180:
    print("Invalid triangle")
elif a < 90 and b < 90 and c < 90:
    print("Acute triangle")
elif a == 90 or b == 90 or c == 90:
    print("Right triangle")
else:
    print("Obtuse triangle")