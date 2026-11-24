s = input("Enter a sentence: ")

i = 0
capital = 0
small = 0
digit = 0
special = 0

while i < len(s):
    if s[i] >= 'A' and s[i] <= 'Z':
        capital += 1
    elif s[i] >= 'a' and s[i] <= 'z':
        small += 1
    elif s[i] >= '0' and s[i] <= '9':
        digit += 1
    else:
        special += 1

    i += 1

print("Capital letters =", capital)
print("Small letters =", small)
print("Digits =", digit)
print("Special characters =", special)