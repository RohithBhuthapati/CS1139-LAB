s = input()

digits = []
total = 0

for ch in s:
    if ch.isdigit():
        n = int(ch)
        digits.append(n)
        total += n

print(digits)
print("Sum:", total)