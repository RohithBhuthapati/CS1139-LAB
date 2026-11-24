color = input("Choose blue or red: ")
mode = input("Choose steady or flashing: ")

if color == "blue" and mode == "steady":
    print("Clear view")

elif color == "blue" and mode == "flashing":
    print("Clouds due")

elif color == "red" and mode == "steady":
    print("Rain ahead")

else:
    print("Snow instead")