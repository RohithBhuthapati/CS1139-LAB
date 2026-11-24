s = input("Enter a sentence: ")

result = ""

for ch in s:
    if ch not in result:
        result = result + ch

print(result)