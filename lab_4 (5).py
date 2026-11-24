n = int(input("Enter kilometers: "))
time = input("Enter day or night: ")

if n > 0 and (time == "day" or time == "night"):

    if time == "day":
        taxi = 33.58 + n * 37.89
    else:
        taxi = 33.58 + n * 43.17

    bus = n * 4.32
    train = n * 2.88

    if n < 20:
        print("Taxi:", taxi)

    elif n < 100:
        print("Cheapest price:", min(taxi, bus))

    else:
        print("Cheapest price:", min(taxi, bus, train))

else:
    print("Invalid input")