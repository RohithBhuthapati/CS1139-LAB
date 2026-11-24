a = tuple(map(int, input().split()))

even = []

for n in a:
    if n % 2 == 0:
        even.append(n)

t = tuple(even)

print(t)