n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
view = [
    [],
    [True, False, False, False],
    [True, False, True, False],
    [True, False, False, True],
    [True, False, True, True],
    [True, True, True, True]
    ]
cctv = []
for i, row in enumerate(grid):
    for j, item in enumerate(row):
        if item != 0 and item != 6:
            cctv.append((i, j))
from itertools import product
cases = list(product(range(4), repeat = len(cctv)))
best = n * m + 1
for c in cases:
    visible = [[item != 0 for item in row] for row in grid]
    for r, (y, x) in zip(c, cctv):
        cc = grid[y][x]
        for i, v in enumerate(view[cc]):
            if not v: continue
            dy, dx = dirs[(i + r) % 4]
            ny, nx = y + dy, x + dx
            while 0 <= ny < n and 0 <= nx < m and grid[ny][nx] != 6:
                visible[ny][nx] = True
                ny, nx = ny + dy, nx + dx
    blindspot = sum([row.count(False) for row in visible])
    best = min(best, blindspot)
print(best)