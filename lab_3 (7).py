n = int(input("Enter 3 digit number: "))

if 100 <= n <= 999:
    a = n // 100
    b = (n // 10) % 10
    c = n % 10

    s = a + b + c

    if n % s == 0:
        print("Harshad number")
    else:
        print("Not a Harshad number")
else:
    print("Invalid number")