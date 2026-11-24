s = input("Enter a sentence: ")
w = input("Enter a word: ")

count = s.count(w)

if w in s:
    print("Word found")
else:
    print("Word not found")

print("Count:", count)


#without using inbuilt functions

s = input("Enter a sentence: ")
w = input("Enter a word: ")

count = 0

for i in range(len(s)):
    if s[i:i+len(w)] == w:
        count = count + 1

print("Count:", count)

if count > 0:
    print("Word found")
else:
    print("Word not found")