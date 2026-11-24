a = list(map(int, input().split()))
v = int(input())

t = tuple(a)

print("Tuple:", t)
print("Length:", len(t))
print("Count of", v, ":", t.count(v))
print("First index of", v, ":", t.index(v))