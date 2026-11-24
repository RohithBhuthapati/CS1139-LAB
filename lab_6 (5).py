n = int(input("Enter number of students: "))

first = 0
second = 0

for i in range(n):
    x = int(input("Enter distance: "))

    if x > first:
        second = first
        first = x
    elif x > second and x < first:
        second = x

print("Winning distance =", first)
print("Runner-up distance =", second)