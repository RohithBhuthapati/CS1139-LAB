total_classes = int(input("Enter total number of classes: "))

attended = int(input("Enter number of classes attended: "))

attended_percent = (attended / total_classes) * 100

print("Attendance percentage:", attended_percent)

if attended_percent >= 75:
    print("Eligible")

else:
    print("Not eligible")