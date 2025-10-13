from itertools import combinations
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
nCnd2 = list(combinations(range(n), n // 2))
abilities = []
for i, pick in enumerate(nCnd2):
    ability = 0
    for i in range(len(pick)):
        x = pick[i]
        for j in range(i+1, len(pick)):
            y = pick[j]
            ability += s[x][y] + s[y][x]
    abilities.append(ability)
best = 100 * 20 * 20 + 1
for i in range(len(abilities) // 2):
    best = min(best, abs(abilities[i] - abilities[-1-i]))
print(best)
