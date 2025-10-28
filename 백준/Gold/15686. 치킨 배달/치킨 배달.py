from itertools import combinations
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
houses, chickens = [], []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2: chickens.append((i, j))
        elif grid[i][j] == 1: houses.append((i, j))
best = float('inf')
for pick in combinations(chickens, m):
    total = 0
    for hy, hx in houses:
        total += min(abs(hy-cy) + abs(hx-cx) for cy, cx in pick)
        if total >= best:
            break
    best = min(best, total)
print(best)