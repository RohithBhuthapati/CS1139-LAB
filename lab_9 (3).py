a = input().split()

runs = 0
wickets = 0
boundaries = 0
over_runs = []
total = 0
balls = 0

for x in a:
    if x == "W":
        wickets += 1
    else:
        n = int(x)
        runs += n
        total += n

        if n == 4 or n == 6:
            boundaries += 1

    balls += 1

    if balls == 6:
        over_runs.append(total)
        total = 0
        balls = 0

if balls > 0:
    over_runs.append(total)

print("Total Runs:", runs)
print("Wickets:", wickets)
print("Boundaries:", boundaries)
print("Runs per over:", over_runs)