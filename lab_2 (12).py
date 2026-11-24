salary = float(input("Enter the basic salary: "))

HRA = 0.20 * salary
TA = 0.05 * salary
DA = 0.10 * salary

gross_salary = salary + HRA + TA + DA

print("HRA:", HRA)
print("TA:", TA)
print("DA:", DA)
print("Gross Salary:", gross_salary)