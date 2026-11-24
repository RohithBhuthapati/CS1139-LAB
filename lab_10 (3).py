a = input().split()

votes = {}

for name in a:
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

for name in votes:
    print(name + ":", votes[name])

winner = list(votes.keys())[0]

for name in votes:
    if votes[name] > votes[winner]:
        winner = name

print("Winner:", winner)