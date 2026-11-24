import math

r = float(input("Enter radius: "))

if r < 0 or r > 100:
    print("Invalid")

else:
    area = math.pi * r ** 2

    print("Area of circle:", area)