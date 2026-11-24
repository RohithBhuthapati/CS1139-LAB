shape = input("Enter shape: ")

if shape == "square":
    a = float(input("Enter side: "))
    area = a * a

elif shape == "rectangle":
    a = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    area = a * b

elif shape == "circle":
    r = float(input("Enter radius: "))
    area = 3.14 * r * r

elif shape == "triangle":
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    area = 0.5 * b * h

else:
    print("Invalid shape")
    area = -1

if area >= 0:
    print("Area:", round(area, 3))