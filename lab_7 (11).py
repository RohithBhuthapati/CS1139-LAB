s = input("Enter paragraph: ")

digits = 0
alphabets = 0
upper = 0
lower = 0
special = 0

for ch in s:
    if ch.isdigit():
        digits = digits + 1

    elif ch.isalpha():
        alphabets = alphabets + 1

        if ch.isupper():
            upper = upper + 1
        else:
            lower = lower + 1

    elif ch != " ":
        special = special + 1

print("Digits:", digits)
print("Alphabets:", alphabets)
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Special characters:", special)