def simple_interest(p, r, t=1):
    return p * r * t / 100

p = float(input())
r = float(input())

print("1 year:", simple_interest(p, r))
print("3 years:", simple_interest(p, r, 3))