sec = int(input("Enter seconds: "))

hours = sec // 3600

rem_sec = sec % 3600

min = rem_sec // 60

seconds = rem_sec % 60

print(hours, ":", min, ":", seconds)