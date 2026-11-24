s = input("Enter a string: ")
k = int(input("Enter shift: "))

result = ""

for ch in s:
    if ch >= 'a' and ch <= 'z':
        n = (ord(ch) - 97 + k) % 26
        result = result + chr(n + 97)

    elif ch >= 'A' and ch <= 'Z':
        n = (ord(ch) - 65 + k) % 26
        result = result + chr(n + 65)

print(result)