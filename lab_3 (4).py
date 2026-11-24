n = int(input("Enter 4 digit number: "))

if 1000 <= n <= 9999:
    a = n // 1000
    b = (n // 100) % 10
    c = (n // 10) % 10
    d = n % 10

    s1 = a + b
    s2 = c + d

    print("First two digits sum =", s1)
    print("Last two digits sum =", s2)

    if s1 == s2:
        print("Both sums are equal")
    else:
        print("Both sums are not equal")
else:
    print("Invalid number")