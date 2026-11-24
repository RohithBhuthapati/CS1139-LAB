feet_to_meter = 0.305

length_ft = float(input("Enter length in feet: "))
width_ft = float(input("Enter width in feet: "))

length_m = length_ft * feet_to_meter
width_m = width_ft * feet_to_meter

area = length_m * width_m

print("Area in square metres:", area)