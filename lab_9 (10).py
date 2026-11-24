a = list(map(int, input().split()))

result = []

for n in a:
    if n != 0:
        result.append(n)

for n in a:
    if n == 0:
        result.append(n)

print(result)