s = input()
ch = input()

count = 0
pos = []

for i in range(len(s)):
    if s[i] == ch:
        count += 1
        pos.append(i)

print("Count:", count)

if count == 0:
    print("Positions: -1")
else:
    print("Positions:", *pos)