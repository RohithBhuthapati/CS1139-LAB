s = input("Enter a sentence: ")
s = s.lower()

flag = True

for ch in "abcdefghijklmnopqrstuvwxyz":
    if ch not in s:
        flag = False

if flag:
    print("Pangram")
else:
    print("Not a pangram")