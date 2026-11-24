#sum(i)

a = input("Enter numbers: ").split()

total = 0

for x in a:
    total = total + int(x)

print("Sum:", total)


#product (ii)

a = input("Enter numbers: ").split()

product = 1

for x in a:
    product = product * int(x)

print("Product:", product)


#smallest element (iii)

a = input("Enter numbers: ").split()

small = int(a[0])

for x in a:
    if int(x) < small:
        small = int(x)

print("Smallest:", small)