from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    player = list(map(int, input().split()))
    team = defaultdict(list)
    for i, t in enumerate(player):
        team[t].append(i)
    valid = set()
    for t in team:
        if len(team[t]) == 6:
            valid.add(t)
    player = [t for t in player if t in valid]
    team = defaultdict(list)
    for i, t in enumerate(player):
        team[t].append(i+1)
    for t in team:
        for i in range(1, len(team[t])):
            team[t][i] += team[t][i-1]
    winner = min(team, key = lambda x: (team[x][3], team[x][4], team[x][5]))
    print(winner)
    