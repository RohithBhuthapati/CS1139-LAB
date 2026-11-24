s = input()

u = 0
l = 0
d = 0
sp = 0

for ch in s:
    if ch.isupper():
        u = 1
    elif ch.islower():
        l = 1
    elif ch.isdigit():
        d = 1
    elif ch != " ":
        sp = 1

total = u + l + d + sp

if len(s) < 8:
    print("WEAK")
elif total == 4:
    print("STRONG")
elif total >= 2:
    print("MODERATE")
else:
    print("WEAK")