a = list(map(int, input().split()))

largest = a[0]
smallest = a[0]

for n in a:
    if n > largest:
        largest = n

    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)