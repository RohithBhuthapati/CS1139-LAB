def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

n = int(input())

d = {}

for i in range(n):
    name, marks = input().split()
    grade = get_grade(int(marks))

    print(name + ":", grade)

    if grade in d:
        d[grade] += 1
    else:
        d[grade] = 1

print("Grade count:")
print(d)