x = int(input())
y = int(input())
n = int(input())

count = 0

for i in range(x, y):
    if i % n != 0:
        print(i, end=" ")
        count = count + 1

print()
print(count)