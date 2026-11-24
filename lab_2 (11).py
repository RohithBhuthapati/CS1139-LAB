x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

if x > y and x > z:
    print("X is largest")

elif y > x and y > z:
    print("Y is largest")

else:
    print("Z is largest")