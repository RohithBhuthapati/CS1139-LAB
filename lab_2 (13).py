basic_salary = float(input("Enter the basic salary: "))

HRA = 0.20 * basic_salary
TA = 0.05 * basic_salary
DA = 0.10 * basic_salary

gross_salary = basic_salary + HRA + TA + DA

if gross_salary < 300000:
    tax_rate = 0
    income_tax = 0

elif gross_salary <= 1000000:
    tax_rate = 10
    income_tax = 0.10 * gross_salary

elif gross_salary <= 2500000:
    tax_rate = 20
    income_tax = 0.20 * gross_salary

else:
    tax_rate = 30
    income_tax = 0.30 * gross_salary

print("Basic Salary:", basic_salary)
print("HRA:", HRA)
print("TA:", TA)
print("DA:", DA)
print("Gross Salary:", gross_salary)
print("Income Tax Slab:", tax_rate, "%")
print("Income Tax:", income_tax)