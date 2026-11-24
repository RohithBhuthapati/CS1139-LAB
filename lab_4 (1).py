salary = float(input("Enter salary: "))
years = int(input("Enter years of service: "))

if salary >= 0 and years >= 0:
    if years > 5:
        bonus = salary * 5 / 100
        print("Bonus:", bonus)
    else:
        print("No bonus")
else:
    print("Invalid input")