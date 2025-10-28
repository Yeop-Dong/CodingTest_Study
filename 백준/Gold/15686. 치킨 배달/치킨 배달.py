from itertools import combinations
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
houses, chickens = [], []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2: chickens.append((i, j))
        elif grid[i][j] == 1: houses.append((i, j))
picks = list(combinations(range(len(chickens)), r=m))
dist = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)
best = float('inf')
for pick in picks:
    sum = 0
    for hy, hx in houses:
        mincd = float('inf')
        for cidx in pick:
            cy, cx = chickens[cidx]
            cd = dist(hy, hx, cy, cx)
            mincd = min(mincd, cd)
        sum += mincd
    best = min(best, sum)
print(best)
