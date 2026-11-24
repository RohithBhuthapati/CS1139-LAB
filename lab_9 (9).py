n = int(input())

count = {}

for i in range(n):
    name = input().lower().split()

    first = name[0]
    last = name[1]

    key = first + "." + last

    if key in count:
        count[key] += 1
        email = key + str(count[key]) + "@jklu.edu.in"
    else:
        count[key] = 1
        email = key + "@jklu.edu.in"

    print(email)