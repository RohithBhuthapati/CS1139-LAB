s = input()
k = int(input())

result = ""

for ch in s:
    if ch == " ":
        result += " "
    else:
        new = (ord(ch) - ord('a') + k) % 26
        result += chr(new + ord('a'))

print(result)