holidays = int(input("Enter holidays: "))

if 0 <= holidays <= 365:
    workdays = 365 - holidays

    playtime = workdays * 63 + holidays * 127

    difference = 30000 - playtime

    if difference >= 0:
        print("Tom sleeps well")
        print("More sleep:", difference, "minutes")
    else:
        print("Tom will run away")
        print("Less sleep:", -difference, "minutes")
else:
    print("Invalid input")