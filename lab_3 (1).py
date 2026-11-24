

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
r = float(input("Enter radius: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

d = ((x2-x1)**2 + (y2-y1)**2)**1/2

if d < r:
    print("Inside the circle")
elif d == r:
    print("On the boundary")
else:
    print("Outside the circle")