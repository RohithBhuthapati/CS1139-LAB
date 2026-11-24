s = input()

best = 1
count = 1
ch = s[0]

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        count = 1

    if count > best:
        best = count
        ch = s[i]

print(ch, best)