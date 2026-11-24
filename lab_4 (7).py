budget = float(input("Enter budget: "))
season = input("Enter season: ")

if budget < 0 or (season != "summer" and season != "winter"):
    print("Invalid input")

elif budget <= 100:
    place = "Bulgaria"

    if season == "summer":
        money = budget * 0.30
        stay = "Camp"
    else:
        money = budget * 0.70
        stay = "Hotel"

    print(place)
    print(stay)
    print(round(money, 2), "BGN")

elif budget <= 1000:
    place = "Balkans"

    if season == "summer":
        money = budget * 0.40
        stay = "Camp"
    else:
        money = budget * 0.80
        stay = "Hotel"

    print(place)
    print(stay)
    print(round(money, 2), "BGN")

else:
    money = budget * 0.90
    print("Europe")
    print("Hotel")
    print(round(money, 2), "BGN")