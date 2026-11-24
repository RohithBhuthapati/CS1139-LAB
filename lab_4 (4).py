h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))

if 0 <= h <= 23 and 0 <= m <= 59:
    m = m + 15

    if m >= 60:
        m = m - 60
        h = h + 1

    if h == 24:
        h = 0

    print(h, ":", str(m).zfill(2), sep="")
else:
    print("Invalid time")